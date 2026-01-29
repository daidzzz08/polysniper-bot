import asyncio
import aiohttp
import logging
import os
import sys
from logging.handlers import RotatingFileHandler
from datetime import datetime
from typing import List, Dict, Any

from py_clob_client.client import ClobClient
from py_clob_client.exceptions import PolyApiException

from config.settings import BotConfig
from core.gamma_client import PolymarketGammaClient
from core.gas_monitor import PolygonGasMonitor
from core.ob_parser import CLOBOrderbookParser
from core.atomic_executor import AtomicArbitrageExecutor
from core.trade_logger import TradeLogger
from core.trade_logger import TradeLogger
from core.telegram_interface import TelegramBot
from core.websocket_client import PolymarketWebSocketClient
from core.paper_trader import PaperTrader

# Ensure logs directory exists
os.makedirs("logs", exist_ok=True)

# Configure Logging
log_formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(name)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

root_logger = logging.getLogger()
root_logger.setLevel(logging.INFO)

# Console Handler
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(log_formatter)
root_logger.addHandler(console_handler)

# File Handler (Rotating)
file_handler = RotatingFileHandler("logs/polysniper.log", maxBytes=5*1024*1024, backupCount=5, encoding='utf-8')
file_handler.setFormatter(log_formatter)
root_logger.addHandler(file_handler)
# Suppress noisy logs
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("telegram").setLevel(logging.WARNING)
logging.getLogger("httpcore").setLevel(logging.WARNING)

logger = logging.getLogger("PolySniper")

class PolySniperBot:
    """
    Main Bot Class for PolySniper.
    Orchestrates Market Discovery, Gas Monitoring, and Arbitrage Execution.
    """
    
    def __init__(self):
        # Load Config
        self.config = BotConfig.from_env()
        
        # Check Execution Mode
        self.dry_run = os.getenv("LIVE_TRADING", "False").lower() != "true"
        if self.dry_run:
            logger.warning("[WARNING] BOT RUNNING IN DRY RUN MODE. No real trades will be executed.")
            logger.warning("    Set LIVE_TRADING=true in .env to enable real trading.")
        else:
            logger.critical("[CRITICAL] BOT RUNNING IN LIVE TRADING MODE. REAL FUNDS AT RISK.")

        # Initialize Clob Client
        # Note: In production, use private key from env. For scanning/dry-run, public access might suffice if endpoints allow,
        # but ClobClient usually requires a key/creds for Auth.
        # Ensure credentials exist
        api_key = os.getenv("CLOB_API_KEY")
        if not api_key:
            logger.error("CLOB_API_KEY not found in environment variables.")
            raise ValueError("Missing CLOB_API_KEY")

        try:
            # chain_id 137 = Polygon Mainnet
            self.clob_client = ClobClient(
                host="https://clob.polymarket.com", 
                key=api_key,
                chain_id=137
            )
        except Exception as e:
            logger.error(f"Failed to initialize ClobClient: {e}")
            raise

        # Core Components (Initialized in start to share session)
        self.gamma_client = None
        self.gas_monitor = None
        self.ob_parser = CLOBOrderbookParser(self.clob_client)
        self.executor = AtomicArbitrageExecutor(self.clob_client)
        self.trade_logger = TradeLogger()
        self.paper_trader = PaperTrader(initial_balance_usd=100.0) # Match Config
        self.telegram_bot = TelegramBot(self)
        self.ws_client = None
        self.session = None
        
        # State
        self.paused = False
        self.start_time = datetime.now()
        self.markets_scanned_count = 0
        self.error_count = 0
        self.last_heartbeat_time = datetime.now()
        self.last_liquid_market_time = datetime.now()
        self.last_sanity_log_time = datetime.now()
        self.last_sanity_log_time = datetime.now()
        self.monitored_tokens = {} # Map token_id -> market_question
        self.token_map = {}        # Map token_id -> (market_id, outcome_label)
        self.market_prices = {}    # Map market_id -> {'YES': float, 'NO': float, 'question': str}
        self.market_depths = {}    # Map market_id -> {'YES': [], 'NO': []}
        self.update_debug_count = 0 

    async def initialize(self):
        """Perform any async initialization if needed."""
        self.session = aiohttp.ClientSession()
        self.gamma_client = PolymarketGammaClient(self.session)
        self.gas_monitor = PolygonGasMonitor(self.config.gas_station_url, self.session)
        self.ws_client = PolymarketWebSocketClient(on_orderbook_update=self.on_ws_update)
        
        logger.info("[INIT] PolySniper Bot Initialized (Hybrid Mode).")
        logger.info(f"   Capital: ${self.config.capital_usd}")
        logger.info(f"   Gas Threshold: {self.config.gas_threshold_gwei} Gwei")
        logger.info(f"   Min Spread: {self.config.min_spread_bps} bps")
        
        # Start Telegram Polling
        if self.telegram_bot.app:
            asyncio.create_task(self.telegram_bot.run())
            await self.telegram_bot.send_alert("[INIT] PolySniper Hybrid Bot Started!")

    async def on_ws_update(self, token_id: str, orderbook: dict):
        """Callback for real-time orderbook updates."""
        if self.paused:
            return

        self.update_debug_count += 1
        spread_bps = orderbook['spread_bps']
        best_bid = orderbook['best_bid']
        best_ask = orderbook['best_ask']
        asks_depth = orderbook.get('asks', []) # Full depth
        
        # 1. Lookup Market via Map
        map_data = self.token_map.get(token_id)
        if not map_data:
            return # Unknown token
            
        market_id, outcome = map_data # outcome is 'YES' or 'NO'
        
        # 2. Update Price & Depth State
        if market_id not in self.market_depths:
            self.market_depths[market_id] = {'YES': [], 'NO': []}
            
        self.market_depths[market_id][outcome] = asks_depth
        
        if market_id in self.market_prices:
            self.market_prices[market_id][outcome] = best_ask
            
        market_question = self.market_prices[market_id].get('question', 'Unknown')

        # --- SANITY CHECKS ---
        if spread_bps > 5000 or best_bid == 0:
             if self.update_debug_count % 100 == 0:
                 logger.debug(f"[FILTER] 👻 GHOST | {market_question} | Ask: {best_ask} | Bid: {best_bid} | Spread: {spread_bps}bps")
             return

        if spread_bps < 10000 and best_bid > 0:
            self.last_liquid_market_time = datetime.now()
            if (datetime.now() - self.last_sanity_log_time).total_seconds() > 60:
                 logger.info(f"[SANITY] ✅ Liquid Market Found | {market_question} | Token: {token_id} | Ask: {best_ask} | Bid: {best_bid}")
                 self.last_sanity_log_time = datetime.now()

        # --- TRUE ARBITRAGE LOGIC (VWAP) ---
        yes_depth = self.market_depths[market_id]['YES']
        no_depth = self.market_depths[market_id]['NO']
        
        # Only check if we have data for both sides
        if yes_depth and no_depth:
            # Calculate VWAP for Position Size
            size_usd = self.config.position_size_per_trade
            
            yes_res = self.ob_parser.calculate_vwap_buy(yes_depth, size_usd)
            no_res = self.ob_parser.calculate_vwap_buy(no_depth, size_usd)
            
            if yes_res and no_res:
                yes_vwap, yes_max = yes_res
                no_vwap, no_max = no_res
                
                total_cost_vwap = yes_vwap + no_vwap
                potential_profit = 1.0 - total_cost_vwap
                
                # Threshold
                min_profit_margin = self.config.min_spread_bps / 10000.0
                
                if potential_profit > min_profit_margin:
                    gas_ok = await self.gas_monitor.is_gas_acceptable(self.config.gas_threshold_gwei)
                    
                    if gas_ok:
                        profit_bps = int(potential_profit * 10000)
                        logger.info(f"[ARB] 🚀 TRUE ARB (VWAP) | {market_question} | Cost: {total_cost_vwap:.4f} | Profit: {profit_bps} bps")
                        
                        # EXECUTE using MAX PRICE for Limits (Sweep), but log Cost via VWAP
                        await self.execute_arbitrage(market_question, yes_max, no_max, total_cost_vwap, profit_bps, market_id=market_id)
                    else:
                         if self.update_debug_count % 50 == 0:
                             logger.debug(f"[FILTER] Gas too high for {market_question}")

    async def execute_arbitrage(self, market_question: str, yes_ask: float, no_ask: float, total_cost: float, profit_bps: int, market_id: str = None):
        """Handle execution logic."""
        status = "Dry Run" if self.dry_run else "Executed"
        
        logger.info(f"[ARB CHECK] {market_question} | YES: {yes_ask} | NO: {no_ask} | Cost: {total_cost}")

        # Paper Trade Simulation
        if self.dry_run:
            self.paper_trader.simulate_trade(
                market_question=market_question,
                yes_ask=yes_ask,
                no_ask=no_ask,
                total_cost=total_cost,
                position_size_usd=self.config.position_size_per_trade,
                gas_gwei= await self.gas_monitor.get_latest_standard_gas(),
                slippage_bps=self.config.simulated_slippage_bps
            )
        else:
             # LIVE TRADING
             if market_id:
                 # Find tokens from map
                 yes_token = next((t for t, v in self.token_map.items() if v[0] == market_id and v[1] == 'YES'), None)
                 no_token = next((t for t, v in self.token_map.items() if v[0] == market_id and v[1] == 'NO'), None)
                 
                 if yes_token and no_token:
                     await self.executor.execute_synthetic_arbitrage(
                         yes_token_id=yes_token,
                         no_token_id=no_token,
                         yes_price=yes_ask,
                         no_price=no_ask,
                         position_size=self.config.position_size_per_trade,
                         slippage_tolerance_bps=self.config.slippage_tolerance_bps
                     )
                     status = "Live Execution Sent"
        
        # Log
        self.trade_logger.log_opportunity(
            market_question=market_question,
            yes_ask=yes_ask,
            no_ask=no_ask,
            total_cost=total_cost,
            profit_bps=profit_bps,
            gas_gwei=await self.gas_monitor.get_latest_standard_gas(),
            status=status
        )
        
        # Telegram
        msg = (f"🚀 **True Arbitrage Opportunity**\n"
               f"Market: {market_question}\n"
               f"YES: {yes_ask} | NO: {no_ask}\n"
               f"Total Cost: {total_cost:.4f}\n"
               f"Profit: {profit_bps} bps")
        await self.telegram_bot.send_alert(msg)

    async def run_continuous_scan(self):
        """Hybrid Loop: Discovery + WS Subscription."""
        
        while True:
            try:
                # --- Phase 1: Market Discovery ---
                logger.info("[DISCOVERY] Fetching all active markets...")
                # Fetch up to 2000 markets using pagination
                all_markets = await self.gamma_client.fetch_all_active_markets(max_markets=2000)
                
                # Filter for useful markets (e.g. valid clobTokenIds)
                valid_markets = []
                token_ids_to_monitor = []
                
                for m in all_markets:
                    clob_tokens = m.get('clobTokenIds', [])
                    if isinstance(clob_tokens, str):
                        try:
                            import json
                            clob_tokens = json.loads(clob_tokens)
                        except: 
                            logger.warning(f"Could not parse clobTokenIds string for market {m.get('question', 'Unknown')}: {clob_tokens}")
                            continue
                        
                    if not clob_tokens or len(clob_tokens) != 2:
                        continue
                        
                    # --- QUALITY FILTER ---
                    # 1. Volume Check (Avoid dead markets)
                    vol = float(m.get('volumeNum', 0))
                    if vol < 1000:
                        continue
                        
                    # 2. Spread Check (Gamma Spread)
                    # Gamma spread is a decimal (0.01 = 1%). Avoid > 20% spread.
                    gamma_spread = m.get('spread')
                    if gamma_spread is not None:
                        try:
                            if float(gamma_spread) > 0.2:
                                # logger.debug(f"[SKIP] Wide spread {gamma_spread} for {m.get('question')}")
                                continue
                        except:
                            pass
                    # ----------------------
                    
                    yes_token = clob_tokens[0]
                    no_token = clob_tokens[1]
                    
                    market_id = m.get('conditionId')
                    question = m.get('question', 'Unknown')
                    
                    # Store mapping for both tokens
                    str_yes = str(yes_token)
                    str_no = str(no_token)
                    
                    self.token_map[str_yes] = (market_id, 'YES')
                    self.token_map[str_no] = (market_id, 'NO')
                    
                    # Init price tracking
                    if market_id not in self.market_prices:
                        self.market_prices[market_id] = {'YES': None, 'NO': None, 'question': question}

                    # Add to monitor list
                    valid_markets.append(m)
                    token_ids_to_monitor.append(str_yes)
                    token_ids_to_monitor.append(str_no)
                    
                    # For Telegram/Debug lookups
                    self.monitored_tokens[str_yes] = question
                    self.monitored_tokens[str_no] = question

                self.markets_scanned_count = len(valid_markets)
                logger.info(f"[DISCOVERY] Found {len(valid_markets)} valid markets. Subscribing...")
                
                # --- Phase 2: Subscribe ---
                if token_ids_to_monitor:
                    if self.ws_client.websocket and self.ws_client.connected:
                        # Re-subscribe if already connected
                        await self.ws_client.subscribe_to_markets(token_ids_to_monitor)
                    else:
                        # Start WS loop
                        asyncio.create_task(self.ws_client.subscribe_to_markets(token_ids_to_monitor))
                
                # Wait loop (Keep main task alive for Heartbeat & Rescan)
                # Rescan every 30 minutes to pick up new markets
                rescan_interval = 30 # minutes
                for _ in range(rescan_interval): 
                    # --- RUNTIME check for GHA ---
                    max_runtime = int(os.getenv("MAX_RUNTIME_MINUTES", "0"))
                    if max_runtime > 0:
                        elapsed_min = (datetime.now() - self.start_time).total_seconds() / 60
                        if elapsed_min > max_runtime:
                            logger.warning(f"[GHA] 🛑 Reached runtime limit ({max_runtime} min). Shutting down...")
                            return # Exit run_continuous_scan, forcing shutdown via finally block

                    await self._sleep(60) # 1 minute sleep
                    
                    # Heartbeat
                    if (datetime.now() - self.last_heartbeat_time).total_seconds() > 3600:
                         ws_connected = self.ws_client.connected if self.ws_client else False
                         await self.telegram_bot.send_alert(f"[HEARTBEAT] Bot Active. WS Connected: {ws_connected}")
                         self.last_heartbeat_time = datetime.now()

                    # Quality Watchdog: Warn if we haven't seen a liquid market in 2 minutes
                    if (datetime.now() - self.last_liquid_market_time).total_seconds() > 120:
                         logger.warning("[SANITY] ⚠️ WARNING: Only seeing illiquid markets. Check Gamma sorting!")

            except Exception as e:
                logger.error(f"Global Loop Error: {e}")
                await self._sleep(60)

    async def _sleep(self, seconds):
        if seconds > 0:
            await asyncio.sleep(seconds)

    async def shutdown(self):
        """Cleanup resources."""
        if self.session:
            await self.session.close()
            logger.info("[SHUTDOWN] Session closed.")

async def main():
    bot = PolySniperBot()
    try:
        await bot.initialize()
        await bot.run_continuous_scan()
    except KeyboardInterrupt:
        logger.info("[STOP] Bot stopped by user.")
    except Exception as e:
        logger.fatal(f"[CRITICAL] Bot crashed: {e}")
    finally:
        await bot.shutdown()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
