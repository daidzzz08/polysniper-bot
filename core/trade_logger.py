import csv
import os
from datetime import datetime
import logging

logger = logging.getLogger("PolySniper")

class TradeLogger:
    """
    Logs trade opportunities and execution status to a CSV file.
    """
    
    def __init__(self, log_dir: str = "logs", filename: str = "opportunities.csv"):
        self.log_dir = log_dir
        self.filepath = os.path.join(log_dir, filename)
        self._initialize_csv()
        
    def _initialize_csv(self):
        """Ensures log directory exists and CSV has headers."""
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)
            
        file_exists = os.path.exists(self.filepath)
        
        if not file_exists:
            with open(self.filepath, mode='w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow([
                    "Timestamp", 
                    "Market", 
                    "YES_Ask", 
                    "NO_Ask", 
                    "Total_Cost",
                    "Profit_BPS", 
                    "Gas_Gwei", 
                    "Status"
                ])
            logger.info(f"Initialized trade log at {self.filepath}")

    def log_opportunity(self, 
                        market_question: str, 
                        yes_ask: float, 
                        no_ask: float, 
                        total_cost: float,
                        profit_bps: int, 
                        gas_gwei: float, 
                        status: str):
        """
        Appends a row to the trade log CSV.
        """
        try:
            timestamp = datetime.now().isoformat()
            
            with open(self.filepath, mode='a', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow([
                    timestamp,
                    market_question,
                    yes_ask,
                    no_ask,
                    total_cost,
                    profit_bps,
                    gas_gwei,
                    status
                ])
        except Exception as e:
            logger.error(f"Failed to log trade opportunity: {e}")
