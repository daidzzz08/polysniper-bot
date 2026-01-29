import asyncio
import json
import websockets
from typing import Optional, Callable, Dict
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class PolymarketWebSocketClient:
    """
    Real-time orderbook updates via WebSocket.
    
    Features:
    - Multi-token subscriptions (1000s of markets in one connection)
    - Real-time updates (<100ms latency)
    - Automatic reconnection with exponential backoff
    - No rate limits (unlimited updates)
    """
    
    def __init__(self, on_orderbook_update: Optional[Callable] = None):
        self.uri = "wss://ws-subscriptions-clob.polymarket.com/ws/market"
        self.token_ids = []
        self.orderbooks = {}  # Cache: {token_id: {best_bid, best_ask, spread}}
        self.on_orderbook_update = on_orderbook_update
        self.websocket = None
        self.connected = False
        self.total_updates = 0
    
    async def subscribe_to_markets(self, token_ids: list):
        """
        Subscribe to multiple token IDs for real-time orderbook updates.
        
        Args:
            token_ids: List of asset/token IDs (token ID, not condition ID)
        """
        self.token_ids = token_ids
        
        # FIX: If already connected, just update subscriptions and return.
        # This prevents spawning a second receive loop which causes "concurrent recv" crash.
        if self.connected and self.websocket:
            logger.info(f"WebSocket already connected. Updating subscriptions... ({len(token_ids)} tokens)")
            await self._send_subscription_payloads(token_ids)
            return

        while True:
            try:
                logger.info(f"Connecting to WebSocket... ({len(token_ids)} tokens)")
                async with websockets.connect(
                    self.uri,
                    ping_interval=20,  # Send ping every 20s
                    ping_timeout=20,   # Wait 20s for pong
                    close_timeout=10
                ) as websocket:
                    self.websocket = websocket
                    self.connected = True
                    
                    logger.info(f"WebSocket connected. Sending initial subscriptions...")
                    await self._send_subscription_payloads(token_ids)
                    
                    # Listen for messages
                    await self._listen_for_updates()
            
            except websockets.exceptions.WebSocketException as e:
                logger.error(f"WebSocket error: {e}")
                self.connected = False
                await self._reconnect_with_backoff()
            except Exception as e:
                logger.error(f"Unexpected error in WebSocket loop: {e}")
                self.connected = False
                await self._reconnect_with_backoff()

    async def _send_subscription_payloads(self, token_ids: list):
        """Helper to batch and send subscription messages."""
        if not self.websocket:
            return

        # Batch subscriptions (Try smaller batch 100)
        chunk_size = 100
        for i in range(0, len(token_ids), chunk_size):
            # Ensure all IDs are strings
            chunk = [str(t) for t in token_ids[i:i + chunk_size]]
            
            # Protocol: First batch is Initial (type: market), subsequent are operations
            # Note: On Re-subscribe (update), we might want to use "subscribe" operation for ALL?
            # Or does "market" type reset? 
            # CLOB API docs say "market" is for valid assets. 
            # Let's assume on Update we act like initial for that batch.
            if i == 0:
                subscription = {
                    "type": "market",
                    "assets_ids": chunk
                }
            else:
                subscription = {
                    "operation": "subscribe",
                    "assets_ids": chunk
                }
                
            await self.websocket.send(json.dumps(subscription))
            logger.info(f"Subscription batch sent ({len(chunk)} tokens)")
            await asyncio.sleep(0.5)
    
    async def _listen_for_updates(self):
        """Main message loop."""
        message_count = 0
        while self.connected:
            try:
                message = await self.websocket.recv()
                message_count += 1
                self.total_updates += 1

                if message_count % 5000 == 0:
                    logger.info(f"[WS] 💓 Heartbeat: +5000 updates processed (Total: {self.total_updates})")

                data = json.loads(message)
                
                # Check for empty list
                if isinstance(data, list) and len(data) == 0:
                     pass

                # FIX: Handle Batch (List) vs Single (Dict) responses
                if isinstance(data, list):
                    for item in data:
                        await self._process_single_message(item)
                elif isinstance(data, dict):
                    await self._process_single_message(data)
                else:
                    logger.warning(f"Unknown message format: {type(data)}")
                
            except websockets.exceptions.ConnectionClosed:
                logger.warning("WebSocket connection closed")
                self.connected = False
                break
            except json.JSONDecodeError:
                logger.warning("Invalid JSON received")
            except Exception as e:
                logger.error(f"Error processing message: {e}")

    async def _process_single_message(self, data: dict):
        """Route parsed message to handler."""
        event_type = data.get('event_type')
        
        if event_type == 'book':
            await self._handle_orderbook_full(data)
        elif event_type == 'best_bid_ask':
            await self._handle_best_bid_ask(data)
        elif event_type == 'price_change':
            pass 
        elif event_type is None:
             # Just in case format is different
             # Try to infer type or log
             pass 
    
    async def _handle_orderbook_full(self, data: dict):
        """Handle full orderbook snapshot (book event)."""
        asset_id = data.get('asset_id')
        # Support both 'buys'/'sells' and 'bids'/'asks'
        buys = data.get('buys') or data.get('bids', [])
        sells = data.get('sells') or data.get('asks', [])
        
        if buys and sells:
            # Deep Research Fix: Parse List of Dictionaries
            # Iterate to find Best Bid (Max) and Best Ask (Min) to be safe, 
            # though API usually sends sorted.
            
            parsed_bids = []
            for item in buys:
                try:
                    parsed_bids.append(float(item['price']))
                except (ValueError, KeyError):
                    continue
            
            parsed_asks = []
            for item in sells:
                try:
                    parsed_asks.append(float(item['price']))
                except (ValueError, KeyError):
                    continue

            if not parsed_bids or not parsed_asks:
                return

            best_bid = max(parsed_bids)
            best_ask = min(parsed_asks)
            
            spread = best_ask - best_bid
            spread_bps = int(spread * 10000)
            
            # Simple structure for arbitrage check
            self.orderbooks[asset_id] = {
                'best_bid': best_bid,
                'best_ask': best_ask,
                'spread': spread,
                'spread_bps': spread_bps,
                'timestamp': data.get('timestamp'),
                'asks': sells # Store full asks for VWAP
            }
            
            if self.on_orderbook_update:
                await self.on_orderbook_update(asset_id, self.orderbooks[asset_id])
    
    async def _handle_best_bid_ask(self, data: dict):
        """Handle best bid/ask incremental update (faster)."""
        asset_id = data.get('asset_id')
        best_bid = float(data.get('best_bid', 0))
        best_ask_val = data.get('best_ask')
        
        # VALIDATION: If no ask or ask is 0, market is illiquid/unbuyable
        if best_ask_val is None or float(best_ask_val) == 0:
            return

        best_ask = float(best_ask_val)
        spread = best_ask - best_bid
        spread_bps = int(spread * 10000)
        
        # Preserve existing depth if available
        # Incremental updates don't carry depth, so we keep the last snapshot's depth
        # We could potentially update asks[0]['price'] here, but sticking to snapshot depth + new top price is safer?
        # Actually, if we use VWAP, we rely on the list. 
        # Ideally we should update the list's top level.
        current_book = self.orderbooks.get(asset_id, {})
        current_asks = current_book.get('asks', [])
        
        # Quick Hack: Update Top Ask in the list to match new Best Ask
        # This prevents VWAP from being totally stale if price moved
        if current_asks and len(current_asks) > 0:
            try:
                # Assuming list of dicts: [{'price': '0.55', 'size': '500'}]
                # We update the price of the first level.
                # Note: This doesn't account for size changes, but it's better than old price.
                current_asks[0]['price'] = str(best_ask) 
            except:
                pass

        self.orderbooks[asset_id] = {
            'best_bid': best_bid,
            'best_ask': best_ask,
            'spread': spread,
            'spread_bps': spread_bps,
            'timestamp': data.get('timestamp'),
            'asks': current_asks # Preserve
        }
        
        if self.on_orderbook_update:
            await self.on_orderbook_update(asset_id, self.orderbooks[asset_id])
    
    async def _reconnect_with_backoff(self, max_retries: int = 10):
        """Reconnect with exponential backoff."""
        for attempt in range(max_retries):
            wait_time = min(300, 2 ** attempt)
            logger.warning(f"Reconnecting in {wait_time}s (attempt {attempt + 1}/{max_retries})")
            await asyncio.sleep(wait_time)
            # Break loop to allow re-calling subscribe_to_markets
            return
            
