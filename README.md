# PolySniper Bot 🎯

A high-performance arbitrage bot for Polymarket, designed to sniff out and execute risk-free spreads between YES/NO outcome tokens.

## ⚠️ Risk Warning
**USE AT YOUR OWN RISK.** This software is currently in **BETA**.
- **Real Funds:** Live trading involves real money.
- **Gas Fees:** High gas fees on Polygon can eat into profits.
- **API Limits:** Aggressive scanning may get you rate-limited by Polymarket.

---

## 🚀 Features
- **Fast Market Discovery:** Scans Entertainment and Politics markets via Gamma API.
- **Atomic Execution:** Places simultaneous YES and NO buy orders to lock in spreads.
- **Gas Protection:** Automatically pauses when Polygon gas fees exceed your threshold.
- **Dry Run Mode:** Safely test strategies without spending funds.
- **Trade Logging:** Records all detected opportunities to `logs/opportunities.csv`.

---

## 🛠️ Setup Guide

### 1. Prerequisites
- **Python 3.10+** installed.
- A **Polymarket Account** with funds (POL for gas, USDC for trading) on Polygon.
- **API Credentials** (CLOB API Key/Secret/Passphrase).

### 2. Installation
1.  **Clone the repository:**
    ```bash
    git clone <repo-url>
    cd PolySniper
    ```
2.  **Create a Virtual Environment:**
    ```powershell
    python -m venv venv
    venv\Scripts\activate
    ```
3.  **Install Dependencies:**
    ```powershell
    pip install -r requirements.txt
    ```

### 3. Configuration
1.  **Create `.env` file:**
    Copy the example template:
    ```powershell
    copy .env.example .env
    ```
2.  **Edit `.env`:**
    Open `.env` and fill in your details:
    ```ini
    # API Credentials (Get these from Polymarket Settings -> API)
    CLOB_API_KEY=your_0x_api_key_here
    CLOB_API_SECRET=your_api_secret
    CLOB_API_PASSPHRASE=your_passphrase
    
    # Trading Settings
    GAS_THRESHOLD_GWEI=50       # Max gas price to pay
    INITIAL_CAPITAL_USD=100     # Position sizing
    MIN_SPREAD_BPS=70           # Min profit margin (basis points)
    
    # Modes
    LIVE_TRADING=false          # Set to true to ENABLE REAL TRADING
    ```

---

## 🏃‍♂️ Usage

**Start the Bot:**
```powershell
venv\Scripts\activate
python main.py
```

**Logs:**
- **Console:** Real-time status updates.
- **File:** Detailed logs in `logs/polysniper.log`.
- **Trades:** CSV record of every opportunity in `logs/opportunities.csv`.

---

## 🧪 Testing (Dry Run)
By default, `LIVE_TRADING=false`. The bot will:
1.  Scan markets.
2.  Check orderbooks.
3.  Log "Would execute trade..." in the console.
4.  Write the opportunity to `logs/opportunities.csv`.

This is the safest way to verify configuration before risking real funds.
