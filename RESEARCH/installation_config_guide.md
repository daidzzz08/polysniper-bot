# PolySniper Bot: Installation & Configuration Guide

## 1. System Requirements

**Python:** 3.10+
**OS:** Linux (Ubuntu 20.04+) or macOS
**Storage:** 100MB
**Memory:** 512MB (minimal), 1GB+ recommended
**Network:** Stable internet connection (1Mbps+)

---

## 2. Installation Steps

### 2.1 Clone Repository & Set Up Virtual Environment

```bash
# Clone the PolySniper repository
git clone https://github.com/your-repo/polysniper.git
cd polysniper

# Create Python virtual environment
python3.10 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Upgrade pip
pip install --upgrade pip
```

### 2.2 Install Dependencies

**File: `requirements.txt`**

```
# Core dependencies
aiohttp==3.9.1           # Async HTTP client
asyncio-contextmanager==1.0.0  # Async context support
web3==7.0.0              # Web3.py for Polygon RPC
py-clob-client==0.2.0    # Polymarket CLOB client
orjson==3.9.10           # Fast JSON parsing (6x faster)

# Gas monitoring & utilities
requests==2.31.0         # HTTP requests
python-dotenv==1.0.0     # Environment variables
pydantic==2.5.0          # Data validation

# Logging & monitoring
python-json-logger==2.0.7  # JSON logging for production

# Development (optional)
pytest==7.4.3
black==23.12.0
flake8==6.1.0
```

**Install:**

```bash
pip install -r requirements.txt
```

---

## 3. Configuration

### 3.1 Environment Variables

**File: `.env`** (Never commit this!)

```bash
# Polymarket CLOB API
CLOB_API_KEY=your_clob_api_key_here
CLOB_API_SECRET=your_clob_api_secret_here
CLOB_API_URL=https://clob.polymarket.com

# Polygon RPC (for gas monitoring)
POLYGON_RPC_URL=https://polygon-rpc.com

# Bot Configuration
INITIAL_CAPITAL_USD=100
GAS_THRESHOLD_GWEI=50
MIN_SPREAD_BPS=70
MAX_POSITION_SIZE_USD=25

# Trading Windows (UTC)
TRADING_START_HOUR=23  # 11 PM UTC (off-peak)
TRADING_END_HOUR=6     # 6 AM UTC

# Risk Management
MAX_DAILY_LOSS_USD=10
STOP_LOSS_PCT=2
MAX_POSITION_HOLDING_HOURS=24

# Logging
LOG_LEVEL=INFO
LOG_FILE=./logs/polysniper.log
```

**Load in Python:**

```python
import os
from dotenv import load_dotenv

load_dotenv()

CLOB_API_KEY = os.getenv("CLOB_API_KEY")
INITIAL_CAPITAL = float(os.getenv("INITIAL_CAPITAL_USD", "100"))
GAS_THRESHOLD = float(os.getenv("GAS_THRESHOLD_GWEI", "50"))
```

### 3.2 Bot Configuration Class

```python
from dataclasses import dataclass
from typing import Optional

@dataclass
class BotConfig:
    """Bot runtime configuration."""
    
    # Capital management
    capital_usd: float = 100.0
    position_size_per_trade: float = 25.0
    max_concurrent_positions: int = 4
    
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
    
    @classmethod
    def from_env(cls):
        """Load configuration from environment variables."""
        return cls(
            capital_usd=float(os.getenv("INITIAL_CAPITAL_USD", "100")),
            gas_threshold_gwei=float(os.getenv("GAS_THRESHOLD_GWEI", "50")),
            min_spread_bps=int(os.getenv("MIN_SPREAD_BPS", "70")),
            max_daily_loss_usd=float(os.getenv("MAX_DAILY_LOSS_USD", "10")),
        )
```

---

## 4. Running the Bot

### 4.1 Development Mode

```bash
# Set logging to DEBUG
export LOG_LEVEL=DEBUG

# Run bot
python -m polysniper.bot
```

### 4.2 Production Mode (with systemd)

**File: `/etc/systemd/system/polysniper.service`**

```ini
[Unit]
Description=PolySniper Arbitrage Bot
After=network.target

[Service]
Type=simple
User=polysniper
WorkingDirectory=/home/polysniper/polysniper
Environment="PATH=/home/polysniper/polysniper/venv/bin"
ExecStart=/home/polysniper/polysniper/venv/bin/python -m polysniper.bot
Restart=always
RestartSec=10

# Logging
StandardOutput=journal
StandardError=journal
SyslogIdentifier=polysniper

[Install]
WantedBy=multi-user.target
```

**Enable & start:**

```bash
sudo systemctl daemon-reload
sudo systemctl enable polysniper
sudo systemctl start polysniper
sudo systemctl status polysniper

# View logs
sudo journalctl -u polysniper -f
```

### 4.3 Docker Deployment

**File: `Dockerfile`**

```dockerfile
FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy bot code
COPY polysniper/ ./polysniper/
COPY .env ./

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Run bot
CMD ["python", "-m", "polysniper.bot"]
```

**Build & run:**

```bash
# Build image
docker build -t polysniper:latest .

# Run container
docker run -d \
  --name polysniper \
  --env-file .env \
  --restart always \
  --log-driver json-file \
  --log-opt max-size=10m \
  --log-opt max-file=3 \
  polysniper:latest

# Monitor
docker logs -f polysniper
```

---

## 5. Monitoring & Debugging

### 5.1 Log File Location

```bash
# Real-time monitoring
tail -f ./logs/polysniper.log

# Search for errors
grep "ERROR" ./logs/polysniper.log

# Count trades
grep "Executing trade" ./logs/polysniper.log | wc -l
```

### 5.2 Health Check Endpoint (Optional)

```python
from aiohttp import web

async def health_check(request):
    """Endpoint for monitoring systems."""
    return web.json_response({
        'status': 'healthy',
        'trades_executed': bot.trades_executed,
        'daily_pnl': bot.daily_pnl_usd,
        'gas_threshold': bot.gas_threshold_gwei,
        'capital_remaining': bot.capital_usd - bot.open_position_usd
    })

# Register endpoint
app.router.add_get('/health', health_check)
```

### 5.3 Debugging Commands

```bash
# Check Polygon gas prices
curl https://gasstation.polygon.technology/v2

# Test CLOB API connectivity
curl -H "Authorization: Bearer YOUR_KEY" \
  https://clob.polymarket.com/markets

# Monitor bot process
ps aux | grep polysniper
htop -p $(pgrep -f polysniper)
```

---

## 6. Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'py_clob_client'"

**Solution:**
```bash
pip install --upgrade py-clob-client
python -c "from py_clob_client import ClobClient; print('OK')"
```

### Issue: "Gas price too high" (frequent skipped cycles)

**Solution:**
1. Increase `GAS_THRESHOLD_GWEI` in `.env` (e.g., 75 → 100)
2. Only trade during off-peak hours (11 PM–6 AM UTC)
3. Reduce `MIN_SPREAD_BPS` to 50 bps (more trades, lower per-trade profit)

### Issue: "No arbitrage opportunities found"

**Solution:**
1. Increase `markets_to_monitor` from 150 → 300
2. Lower `min_market_volume_usd` from 500 → 250
3. Verify entertainment/politics tags are correct (discover dynamically)

### Issue: "Orders timeout frequently"

**Solution:**
```python
# Increase timeout in config
order_timeout_seconds=15.0  # Was 10.0

# Check network latency
ping clob.polymarket.com
```

---

## 7. API Credentials Setup

### 7.1 Polymarket CLOB API

1. Sign up at https://polymarket.com
2. Go to Settings → API Keys
3. Create new key with permissions: `orders:read`, `orders:create`, `orders:cancel`
4. Copy key and secret to `.env`

### 7.2 Polygon RPC (Optional, for advanced features)

Use free tier:
- https://polygon-rpc.com (no auth required)
- https://rpc-amoy.polygon.technology (testnet)

Or premium:
- Alchemy: https://www.alchemy.com
- Infura: https://infura.io
- QuickNode: https://quicknode.com

---

## 8. Performance Optimization Tips

### 8.1 Network Optimization

```bash
# Increase open file limit (for concurrent connections)
ulimit -n 65536

# Enable TCP keepalive for long-running connections
sysctl -w net.ipv4.tcp_keepalive_time=60
```

### 8.2 Python Optimization

```python
# Use uvloop for faster asyncio (Unix only)
pip install uvloop

# Enable in bot startup
import uvloop
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
```

### 8.3 Database Optimization (for trade tracking)

```python
# Optional: Use SQLite for trade log
import sqlite3

conn = sqlite3.connect('trades.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS trades (
    id INTEGER PRIMARY KEY,
    timestamp REAL,
    market_id TEXT,
    yes_price REAL,
    no_price REAL,
    size REAL,
    pnl REAL
)
''')

conn.commit()
```

---

## 9. Maintenance

### 9.1 Daily Checklist

- ✅ Bot is running (`systemctl status polysniper`)
- ✅ Gas prices are reasonable (<60 Gwei)
- ✅ No error messages in logs
- ✅ Daily P&L is positive (or acceptable loss)
- ✅ Open positions reconciled

### 9.2 Weekly Checklist

- ✅ Review trade performance
- ✅ Update market categories (new entertainment/politics markets)
- ✅ Check Polymarket API changes
- ✅ Backup trade log

### 9.3 Monthly Checklist

- ✅ Review capital allocation
- ✅ Withdraw profits
- ✅ Update stop-loss thresholds
- ✅ Audit for unusual patterns

---

## 10. Security Best Practices

**CRITICAL: Never commit `.env` file!**

```bash
# Add to .gitignore
echo ".env" >> .gitignore
echo "*.log" >> .gitignore
echo "trades.db" >> .gitignore

# Use git-secrets to prevent accidental commits
brew install git-secrets
git secrets --install
```

**Secure API keys:**
```bash
# Use AWS Secrets Manager or HashiCorp Vault
# for production deployments
```

**Restrict file permissions:**
```bash
chmod 600 .env
chmod 700 ./logs
```

---

## 11. Uninstallation

```bash
# Stop bot
sudo systemctl stop polysniper
sudo systemctl disable polysniper

# Remove systemd service
sudo rm /etc/systemd/system/polysniper.service
sudo systemctl daemon-reload

# Remove bot files
rm -rf ~/polysniper
```

---

**Last Updated:** January 26, 2026
**Version:** 1.0.0