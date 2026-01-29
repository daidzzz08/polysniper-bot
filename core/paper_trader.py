import json
import os
import logging
from datetime import datetime
from typing import Dict, Any

logger = logging.getLogger("PolySniper")

class PaperTrader:
    """
    Simulates trades and tracks theoretical P&L including Gas estimates.
    """
    def __init__(self, initial_balance_usd: float = 1000.0, data_dir: str = "logs"):
        self.initial_balance = initial_balance_usd
        self.balance = initial_balance_usd
        self.trades_count = 0
        self.wins = 0
        self.total_gas_spent_usd = 0.0
        self.history = []
        
        self.data_path = os.path.join(data_dir, "paper_portfolio.json")
        self._load_state()

    def _load_state(self):
        """Load portfolio state from disk."""
        if os.path.exists(self.data_path):
            try:
                with open(self.data_path, 'r') as f:
                    data = json.load(f)
                    self.balance = data.get('balance', self.initial_balance)
                    self.trades_count = data.get('trades_count', 0)
                    self.wins = data.get('wins', 0)
                    self.total_gas_spent_usd = data.get('total_gas_spent_usd', 0.0)
                    self.history = data.get('history', [])
                    logger.info(f"[PAPER] Loaded Portfolio: ${self.balance:.2f} (Trades: {self.trades_count})")
            except Exception as e:
                logger.error(f"[PAPER] Failed to load state: {e}")

    def _save_state(self):
        """Save portfolio state to disk."""
        data = {
            'balance': self.balance,
            'trades_count': self.trades_count,
            'wins': self.wins,
            'total_gas_spent_usd': self.total_gas_spent_usd,
            'history': self.history[-50:] # Keep last 50 only in JSON for speed
        }
        try:
            with open(self.data_path, 'w') as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            logger.error(f"[PAPER] Failed to save state: {e}")

    def simulate_trade(self, 
                       market_question: str, 
                       yes_ask: float, 
                       no_ask: float, 
                       total_cost: float, 
                       position_size_usd: float = 20.0, 
                       gas_gwei: float = 50.0,
                       slippage_bps: int = 0):
        """
        Execute a simulated arbitrage trade with slippage.
        """
        # 1. Apply Slippage (Worsen the buy price)
        # Slippage of 50bps adds 0.0050 to the cost
        slippage_cost = slippage_bps / 10000.0
        adjusted_cost = total_cost + slippage_cost
        
        # 2. Calculate Quantity
        # We assume we spend the full position_size at the *adjusted* (worse) price.
        qty_tokens = position_size_usd / adjusted_cost

        
        # 2. Revenue (Redeem at $1.00)
        revenue_usd = qty_tokens * 1.00
        
        # 3. Gross Profit
        gross_profit = revenue_usd - position_size_usd
        
        # 4. Gas Cost Estimate
        # Assumption: 300,000 Gas Units for 3 txs (Approve output + Buy Yes + Buy No + Merge)
        # 1 Gwei = 1e-9 MATIC. 1 MATIC ~ $0.50 (Static Estimate for simplicity)
        est_gas_units = 300000
        matic_price_usd = 0.50 
        gas_cost_matic = (gas_gwei * 1e-9) * est_gas_units
        gas_cost_usd = gas_cost_matic * matic_price_usd
        
        # 5. Net Profit
        net_profit = gross_profit - gas_cost_usd
        
        # Update Balance
        self.balance += net_profit
        self.trades_count += 1
        self.total_gas_spent_usd += gas_cost_usd
        
        if net_profit > 0:
            self.wins += 1
            
        # Log Result
        trade_record = {
            'timestamp': datetime.now().isoformat(),
            'market': market_question,
            'cost_basis': total_cost,
            'gross_profit': gross_profit,
            'gas_usd': gas_cost_usd,
            'net_profit': net_profit,
            'balance_after': self.balance
        }
        self.history.append(trade_record)
        self._save_state()
        
        logger.info(f"[PAPER TRADE] 💰 Profit: ${net_profit:.2f} (Gross: ${gross_profit:.2f} - Gas: ${gas_cost_usd:.2f}) | Slip: {slippage_bps}bps | Cost: {adjusted_cost:.4f} | New Bal: ${self.balance:.2f}")
        return net_profit

    def get_stats(self) -> str:
        """Return formatted stats for Telegram."""
        roi = ((self.balance - self.initial_balance) / self.initial_balance) * 100
        win_rate = (self.wins / self.trades_count * 100) if self.trades_count > 0 else 0
        
        return (
             f"📜 **Paper Portfolio**\n"
             f"Balance: ${self.balance:.2f}\n"
             f"P&L: ${self.balance - self.initial_balance:+.2f} ({roi:+.1f}%)\n"
             f"Trades: {self.trades_count} (WR {win_rate:.0f}%)\n"
             f"Gas Spent: ${self.total_gas_spent_usd:.2f}"
        )
