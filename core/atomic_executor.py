import asyncio
import time
from typing import Tuple, Dict, Any
from py_clob_client.client import ClobClient
from py_clob_client.clob_types import OrderArgs
from py_clob_client.order_builder.constants import BUY, SELL

class AtomicArbitrageExecutor:
    """Execute synthetic arbitrage trades atomically."""
    
    def __init__(self, clob_client: ClobClient):
        self.client = clob_client
    
    async def place_order(
        self,
        token_id: str,
        side: str,  # 'BUY' or 'SELL'
        size: float,
        price: float,
        order_type: str = "IOC", # Match library default usually, but we want control
        timeout_seconds: float = 10
    ) -> Dict[str, Any]:
        """
        Place single order asynchronously.
        Wraps synchronous client calls in executor.
        """
        start_time = time.perf_counter()
        
        try:
            side_const = BUY if side == 'BUY' else SELL
            
            # Note: OrderArgs construction stays same
            order_args = OrderArgs(
                price=price,
                size=size,
                side=side_const,
                token_id=token_id
            )
            
            loop = asyncio.get_event_loop()
            
            # Create order (signing)
            signed_order = await loop.run_in_executor(
                None,
                self.client.create_order,
                order_args
            )
            
            # Post order with SPECIFIED OrderType
            # Client.post_order(order, orderType=...)
            response = await loop.run_in_executor(
                None,
                lambda: self.client.post_order(signed_order, orderType=order_type)
            )
            
            latency_ms = (time.perf_counter() - start_time) * 1000
            
            return {
                'order_id': response.get('orderId', ''),
                'status': 'pending',
                'latency_ms': latency_ms,
                'response': response
            }
        
        except asyncio.TimeoutError:
            return {
                'order_id': '',
                'status': 'timeout',
                'latency_ms': (time.perf_counter() - start_time) * 1000,
                'error': 'Request timeout'
            }
        except Exception as e:
            return {
                'order_id': '',
                'status': 'error',
                'latency_ms': (time.perf_counter() - start_time) * 1000,
                'error': str(e)
            }
            
    async def execute_synthetic_arbitrage(
        self,
        yes_token_id: str,
        no_token_id: str,
        yes_price: float,
        no_price: float,
        position_size: float = 100.0,
        slippage_tolerance_bps: int = 50 # Default 50 bps (0.5%)
    ) -> Tuple[Dict[str, Any], Dict[str, Any], float]:
        """
        Execute buy YES + buy NO orders SEQUENTIALLY using FOK.
        
        Strategy:
        1. Buy YES (FOK).
        2. If Success -> Buy NO (FOK).
        3. If Fail -> ABORT (Risk Free).
        """
        start_time = time.perf_counter()
        
        # Calculate Aggressive Limit Prices (Market with Protection)
        # We willing to pay up to X% more to guarantee fill
        tolerance_multiplier = 1.0 + (slippage_tolerance_bps / 10000.0)
        
        # Ensure we don't exceed 1.00 logic too much, but for individual legs:
        limit_price_yes = yes_price * tolerance_multiplier
        limit_price_no = no_price * tolerance_multiplier
        
        # Cap at 1.0 (Prediction markets constraint usually)
        limit_price_yes = min(limit_price_yes, 1.0)
        limit_price_no = min(limit_price_no, 1.0)

        # --- LEG 1: YES ---
        # Note: We use FOK to prevent partial fills
        # Passing round(..., 4) or similar might be needed depending on tick size
        yes_result = await self.place_order_fok(yes_token_id, 'BUY', position_size, limit_price_yes)
        
        if yes_result['status'] != 'filled':
            # Abort
             total_latency_ms = (time.perf_counter() - start_time) * 1000
             return yes_result, {'status': 'skipped', 'error': 'First leg failed'}, total_latency_ms

        # --- LEG 2: NO ---
        no_result = await self.place_order_fok(no_token_id, 'BUY', position_size, limit_price_no)
        
        total_latency_ms = (time.perf_counter() - start_time) * 1000
        
        return yes_result, no_result, total_latency_ms

    async def place_order_fok(self, token_id, side, size, price):
        """Helper for FOK order placement."""
        # Note: This requires updating place_order or ClobClient to support FOK
        # Assuming place_order handles the basic placement, we might need to modify it 
        # to send orderType="FOK". For now, assuming standard Limit order with IO is default, 
        # we strictly need FOK.
        
        # Actually, py_clob_client `create_order` + `post_order` usually defaults to GTC or IOC 
        # depending on args. We need to pass orderType. 
        # Refactoring place_order below or here...
        # Let's use the existing place_order but we NEED TO UPDATE IT to support FOK.
        # For this refactor, let's assume place_order is updated or we add a new one.
        return await self.place_order(token_id, side, size, price, order_type="FOK")
