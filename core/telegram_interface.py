import logging
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from web3 import Web3

from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from main import PolySniperBot

logger = logging.getLogger("PolySniper-Telegram")

class TelegramBot:
    """
    Async Telegram Bot Interface for PolySniper.
    """
    def __init__(self, bot_instance: 'PolySniperBot'):
        self.bot_instance = bot_instance
        self.token = bot_instance.config.telegram_bot_token
        self.chat_id = bot_instance.config.telegram_chat_id
        
        if not self.token:
            logger.warning("No Telegram Token provided. Telegram interface disabled.")
            self.app = None
            return

        self.app = ApplicationBuilder().token(self.token).build()
        
        # Initialize Web3 for balance checks
        self.w3 = Web3(Web3.HTTPProvider(bot_instance.config.polygon_rpc_url))
        
        # Register Handlers
        self.app.add_handler(CommandHandler("start", self.cmd_start))
        self.app.add_handler(CommandHandler("stop", self.cmd_stop))
        self.app.add_handler(CommandHandler("status", self.cmd_status))
        self.app.add_handler(CommandHandler("config", self.cmd_config))
        self.app.add_handler(CommandHandler("set_gas", self.cmd_set_gas))
        self.app.add_handler(CommandHandler("set_spread", self.cmd_set_spread))
        self.app.add_handler(CommandHandler("set_size", self.cmd_set_size))
        self.app.add_handler(CommandHandler("set_slippage", self.cmd_set_slippage))
        self.app.add_handler(CommandHandler("balance", self.cmd_balance))
        self.app.add_handler(CommandHandler("test_alert", self.cmd_test_alert))
        self.app.add_handler(CommandHandler("sample", self.cmd_sample))
        self.app.add_handler(CommandHandler("sample_top", self.cmd_sample_top))
        self.app.add_handler(CommandHandler("sample_best", self.cmd_sample_best))

    async def run(self):
        """Start the Telegram polling loop."""
        if not self.app:
            return
            
        logger.info("[TELEGRAM] Starting Telegram Bot...")
        try:
            # Drop pending updates to avoid processed backlog on startup
            await self.app.bot.delete_webhook(drop_pending_updates=True)
            
            # Correct Async Pattern for PTB v20+
            await self.app.initialize()
            await self.app.start()
            await self.app.updater.start_polling()
            
            logger.info("[TELEGRAM] Telegram Polling Started.")
            
        except Exception as e:
            logger.error(f"Failed to start Telegram Bot: {e}")

    async def send_alert(self, message: str):
        """Send a message to the configured chat."""
        if not self.app or not self.chat_id:
            return
        try:
            await self.app.bot.send_message(chat_id=self.chat_id, text=message)
        except Exception as e:
            logger.error(f"Failed to send Telegram alert: {e}")

    # --- Command Handlers ---

    async def cmd_start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        self.bot_instance.paused = False
        await update.message.reply_text("[ACTIVE] Bot Resumed. Scanning active.")
        logger.info("Bot resumed via Telegram.")

    async def cmd_stop(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        self.bot_instance.paused = True
        await update.message.reply_text("[PAUSED] Bot Paused. Scanning stopped.")
        logger.info("Bot paused via Telegram.")

    async def cmd_status(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        fees = await self.bot_instance.gas_monitor.fetch_gas_prices()
        current_gas = fees['standard']['maxFee'] if fees else "Unknown"
        ws_status = "Connected 🟢" if self.bot_instance.ws_client and self.bot_instance.ws_client.connected else "Disconnected 🔴"
        
        status_msg = (
            f"[STATUS] PolySniper Hybrid ⚡\n"
            f"- Mode: {'Live' if not self.bot_instance.dry_run else 'Dry Run'}\n"
            f"- State: {'Active' if not self.bot_instance.paused else 'Paused'}\n"
            f"- Gas: {current_gas} Gwei\n"
            f"- WS Status: {ws_status}\n"
            f"- Monitored: {self.bot_instance.markets_scanned_count} markets\n"
            f"- Errors: {self.bot_instance.error_count}\n"
        )
        await update.message.reply_text(status_msg)

    async def cmd_config(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        if self.bot_instance.config:
            c = self.bot_instance.config
            msg = (
                "🔧 **Current Configuration**\n"
                f"- Gas Threshold: {c.gas_threshold_gwei} Gwei\n"
                f"- Min Spread: {c.min_spread_bps} bps\n"
                f"- Position Size: ${c.position_size_per_trade}\n"
                f"- Slippage Tol: {c.slippage_tolerance_bps} bps\n"
                f"- Sim Slippage: {c.simulated_slippage_bps} bps\n"
                f"- Scanned Markets: {self.bot_instance.markets_scanned_count}"
            )
            await update.message.reply_text(msg, parse_mode='Markdown')

    async def cmd_set_gas(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        try:
            val = float(context.args[0])
            self.bot_instance.config.gas_threshold_gwei = val
            await update.message.reply_text(f"[OK] Gas Threshold updated to {val} Gwei")
        except (IndexError, ValueError):
            await update.message.reply_text("[ERROR] Usage: /set_gas <value>")

    async def cmd_set_spread(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        try:
            val = int(context.args[0])
            self.bot_instance.config.min_spread_bps = val
            await update.message.reply_text(f"[OK] Min Spread updated to {val} bps")
        except (IndexError, ValueError):
            await update.message.reply_text("[ERROR] Usage: /set_spread <value>")

    async def cmd_set_size(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        try:
            val = float(context.args[0])
            self.bot_instance.config.position_size_per_trade = val
            await update.message.reply_text(f"[OK] Position Size updated to ${val}")
        except (IndexError, ValueError):
            await update.message.reply_text("[ERROR] Usage: /set_size <amount_usd>")

    async def cmd_set_slippage(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        try:
            val = int(context.args[0])
            self.bot_instance.config.simulated_slippage_bps = val
            await update.message.reply_text(f"[OK] Simulated Slippage updated to {val} bps")
        except (IndexError, ValueError):
            await update.message.reply_text("[ERROR] Usage: /set_slippage <bps>")

    async def cmd_balance(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        addr = self.bot_instance.config.wallet_address
        if not addr:
            await update.message.reply_text("[WARN] No Wallet Address configured.")
            return

        try:
            # Run blocking web3 call in executor
            loop = asyncio.get_event_loop()
            balance_wei = await loop.run_in_executor(None, self.w3.eth.get_balance, addr)
            balance_pol = self.w3.from_wei(balance_wei, 'ether')
            
            msg = f"💳 **Wallet Balance**\nAddress: `{addr}`\nPOL: {balance_pol:.4f}"
            
            # Append Paper Stats if available
            if hasattr(self.bot_instance, 'paper_trader'):
                paper_stats = self.bot_instance.paper_trader.get_stats()
                msg += f"\n\n{paper_stats}"
            
            await update.message.reply_text(msg)
        except Exception as e:
            await update.message.reply_text(f"[ERROR] Failed to fetch balance: {e}")
            logger.error(f"Balance check error: {e}")

    async def cmd_test_alert(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await self.send_alert("🔔 TEST ALERT: This is a manual test message.")
        await update.message.reply_text("[OK] Test alert sent.")

    async def cmd_sample(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Fetch a random market sample from WS cache."""
        ws = self.bot_instance.ws_client
        if not ws or not ws.connected or not ws.orderbooks:
            await update.message.reply_text("[ERROR] WebSocket not connected or cache empty.")
            return

        import random
        # Pick random asset_id
        try:
            asset_id = random.choice(list(ws.orderbooks.keys()))
            data = ws.orderbooks[asset_id]
            question = self.bot_instance.monitored_tokens.get(asset_id, "Unknown Market")
            
            msg = (
                f"🔎 **Market Inspection**\n"
                f"Market: {question}\n"
                f"Ask: {data['best_ask']}\n"
                f"Bid: {data['best_bid']}\n"
                f"Spread: {data['spread_bps']} bps"
            )
            await update.message.reply_text(msg)
        except Exception as e:
            await update.message.reply_text(f"[ERROR] Sample failed: {e}")

    async def cmd_sample_top(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Fetch the confirmed highest volume market that has Live Data."""
        ws = self.bot_instance.ws_client
        if not ws or not ws.connected or not ws.orderbooks:
            await update.message.reply_text("[ERROR] WebSocket not connected or cache empty.")
            return

        try:
            # Iterate through the top 50 monitored tokens (which are sorted by Volume in Gamma)
            # Return the first one that has data in the WebSocket cache.
            found = False
            for token_id, question in list(self.bot_instance.monitored_tokens.items())[:50]:
                if token_id in ws.orderbooks:
                    data = ws.orderbooks[token_id]
                    # Check if it has actual prices, not just empty shell
                    if data.get('best_ask') and data.get('best_bid'):
                         msg = (f"🔝 **Top Active Market**\n"
                                f"Question: {question}\n"
                                f"Ask: {data.get('best_ask')} | Bid: {data.get('best_bid')}\n"
                                f"Spread: {data.get('spread_bps')} bps")
                         await update.message.reply_text(msg)
                         found = True
                         break
            
            if not found:
                 await update.message.reply_text("[INFO] Top 50 markets have no live price data yet.")
                 
        except Exception as e:
            await update.message.reply_text(f"[ERROR] Failed to sample top: {e}")

    async def cmd_sample_best(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Fetch the market with the tightest spread that is NOT a ghost."""
        ws = self.bot_instance.ws_client
        if not ws or not ws.connected or not ws.orderbooks:
            await update.message.reply_text("[ERROR] WebSocket not connected or cache empty.")
            return

        try:
            # Filter for valid markets (spread < 5000 bps)
            valid_items = [
                (tid, d) for tid, d in ws.orderbooks.items() 
                if d.get('spread_bps', 9999) < 5000 and d.get('best_bid', 0) > 0
            ]
            
            if not valid_items:
                await update.message.reply_text("[WARN] No markets found with spread < 50%")
                return

            # Find min spread among valid
            best_token = min(valid_items, key=lambda x: x[1]['spread_bps'])
            asset_id = best_token[0]
            data = best_token[1]
            question = self.bot_instance.monitored_tokens.get(asset_id, "Unknown Market")
            
            msg = (f"💎 **Tightest Valid Spread**\n"
                   f"Question: {question}\n"
                   f"Ask: {data.get('best_ask')} | Bid: {data.get('best_bid')}\n"
                   f"Spread: {data.get('spread_bps')} bps")
            await update.message.reply_text(msg)
        except Exception as e:
            await update.message.reply_text(f"[ERROR] Failed to find best spread: {e}")
