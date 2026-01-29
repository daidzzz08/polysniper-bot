import orjson
import time
import asyncio
from decimal import Decimal
from typing import Dict, Optional, Any, List, Tuple
from py_clob_client.client import ClobClient

class CLOBOrderbookParser:
    """Efficiently parse Polymarket CLOB orderbook data."""
    
    def __init__(self, clob_client: ClobClient):
        self.client = clob_client
    
    async def fetch_and_parse_orderbook(self, token_id: str) -> Optional[Dict[str, Any]]:
        """
        Fetch orderbook for a token and calculate synthetic spread.
        Uses asyncio.to_thread / run_in_executor to avoid blocking on sync client call.
        """
        try:
            # py-clob-client is synchronous, so wrap it to avoid blocking event loop
            loop = asyncio.get_event_loop()
            orderbook = await loop.run_in_executor(None, self.client.get_book, token_id)
            
            # Parse with orjson if it's a string
            if isinstance(orderbook, str):
                book_data = orjson.loads(orderbook)
            else:
                book_data = orderbook
            
            if not isinstance(book_data, dict):
                 return None

            # Extract prices
            yes_bids = book_data.get('bids', [])
            no_asks = book_data.get('asks', []) 
            
            if not yes_bids or not no_asks:
                return None
            
            # Calculate standard spread logic (Backup)
            yes_price = Decimal(str(yes_bids[0]['price']))
            no_price = Decimal(str(no_asks[0]['price']))
            sum_price = yes_price + no_price
            spread_bps = int((Decimal('1.00') - sum_price) * Decimal('10000'))
            
            return {
                'yes_price': float(yes_price),
                'no_price': float(no_price),
                'sum_price': float(sum_price),
                'spread_bps': spread_bps,
                'is_arbitrage': spread_bps > 50,
                'timestamp': time.time()
            }
        except Exception as e:
            return None

    def calculate_vwap_buy(self, asks: List[Dict], size_usd: float) -> Optional[Tuple[float, float]]:
        """
        Calculate the Volume Weighted Average Price (VWAP) to buy `size_usd`.
        
        Args:
            asks: List of dicts [{'price': '0.55', 'size': '100'}, ...] (Sorted asc)
            size_usd: Amount of USD we want to spend.
            
        Returns:
            Tuple[float, float]: (vwap_price, max_sweep_price)
            None: If insufficient liquidity to fill `size_usd`.
        """
        remaining_usd = float(size_usd)
        total_shares = 0.0
        max_sweep_price = 0.0
        
        for level in asks:
            try:
                price = float(level['price'])
                size = float(level['size']) 
                
                level_cost_usd = price * size
                max_sweep_price = price
                
                if level_cost_usd >= remaining_usd:
                    # Partial fill of this level
                    shares_bought = remaining_usd / price
                    total_shares += shares_bought
                    remaining_usd = 0
                    break
                else:
                    # Full fill of this level
                    total_shares += size
                    remaining_usd -= level_cost_usd
                    
            except (ValueError, KeyError, TypeError):
                continue
                
        if remaining_usd > 0.01: # allow small float error
            # DID NOT FILL
            return None
            
        if total_shares == 0:
            return None
            
        # VWAP = Total Spent / Total Shares
        vwap_price = size_usd / total_shares
        
        return vwap_price, max_sweep_price
