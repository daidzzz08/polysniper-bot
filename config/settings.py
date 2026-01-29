import os
from dataclasses import dataclass
from typing import Optional
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

@dataclass
class BotConfig:
    """Bot runtime configuration."""
    
    # Capital management
    gas_threshold_gwei: float = 50.0
    min_spread_bps: int = 100
    capital_usd: float = 1000.0
    simulated_slippage_bps: int = 0
    slippage_tolerance_bps: int = 50
    position_size_per_trade: float = 20.04
    max_concurrent_positions: int = 4
    
    # API Endpoints
    gamma_api_url: str = "https://gamma-api.polymarket.com"
    gas_station_url: str = "https://gasstation.polygon.technology/v2"
    polygon_rpc_url: str = "https://polygon-rpc.com"
    wallet_address: Optional[str] = None
    
    # Market filters
    min_market_volume_usd: float = 500.0
    min_market_age_hours: float = 2
    max_market_age_days: float = 730  # 2 years (2028 election)
    
    # Arbitrage thresholds
    min_spread_bps: int = 70  # Minimum spread to trade
    max_spread_bps: int = 500  # Skip if spread too wide
    
    # Gas management
    gas_threshold_gwei: float = 50.0
    max_gas_price_gwei: float = 75.0
    
    # Execution
    max_execution_latency_ms: float = 5000.0
    order_timeout_seconds: float = 10.0
    
    # Risk
    max_daily_loss_usd: float = 10.0
    stop_loss_pct: float = 2.0
    max_position_holding_hours: float = 24.0
    
    # Scanning
    scan_interval_seconds: int = 30
    markets_to_monitor: int = 150
    
    # Trading windows (UTC)
    trading_start_hour: int = 23  # 11 PM
    trading_end_hour: int = 6     # 6 AM
    
    # Telegram
    telegram_bot_token: Optional[str] = None
    telegram_chat_id: Optional[str] = None
    
    @classmethod
    def from_env(cls):
        """Load configuration from environment variables."""
        return cls(
            capital_usd=float(os.getenv("INITIAL_CAPITAL_USD", "100")),
            position_size_per_trade=float(os.getenv("POSITION_SIZE_USD", "20")),
            simulated_slippage_bps=int(os.getenv("SIMULATED_SLIPPAGE_BPS", "0")),
            slippage_tolerance_bps=int(os.getenv("SLIPPAGE_TOLERANCE_BPS", "50")),
            gas_threshold_gwei=float(os.getenv("GAS_THRESHOLD_GWEI", "50")),
            min_spread_bps=int(os.getenv("MIN_SPREAD_BPS", "70")),
            max_daily_loss_usd=float(os.getenv("MAX_DAILY_LOSS_USD", "10")),

            telegram_bot_token=os.getenv("TELEGRAM_BOT_TOKEN"),
            telegram_chat_id=os.getenv("TELEGRAM_CHAT_ID"),
            wallet_address=os.getenv("WALLET_ADDRESS"),
        )
