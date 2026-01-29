import aiohttp
import asyncio
import logging
from typing import Dict, Optional, Any

# Configure logging
logger = logging.getLogger(__name__)

class PolygonGasMonitor:
    """Monitor Polygon EIP-1559 gas fees in real-time."""
    
    def __init__(self, gas_station_url: str = "https://gasstation.polygon.technology/v2", session: Optional[aiohttp.ClientSession] = None):
        self.gas_station_url = gas_station_url
        self.session = session
        self.last_gas_data: Optional[Dict[str, Any]] = None
        
        # Log Spam Control
        self.last_high_gas_log = 0
        self.was_gas_high = False

    async def fetch_gas_prices(self) -> Optional[Dict[str, Any]]:
        """
        Fetch current Polygon gas prices from official Gas Station.
        """
        try:
            # Use provided session or create temporary
            if self.session:
                async with self.session.get(
                    self.gas_station_url,
                    timeout=aiohttp.ClientTimeout(total=5)
                ) as resp:
                    return await self._process_response(resp)
            else:
                async with aiohttp.ClientSession() as session:
                    async with session.get(
                        self.gas_station_url,
                        timeout=aiohttp.ClientTimeout(total=5)
                    ) as resp:
                        return await self._process_response(resp)
        
        except Exception as e:
            logger.error(f"Gas fetch error: {e}")
            return None

    async def _process_response(self, resp) -> Optional[Dict[str, Any]]:
        if resp.status != 200:
            logger.error(f"Gas fetch failed: {resp.status}")
            return None
        
        data = await resp.json()
        
        # Store last valid data
        self.last_gas_data = {
            'standard': {
                'maxFee': float(data['standard']['maxFee']),
                'maxPriorityFee': float(data['standard']['maxPriorityFee'])
            },
            'fast': {
                'maxFee': float(data['fast']['maxFee']),
                'maxPriorityFee': float(data['fast']['maxPriorityFee'])
            },
            'fastest': {
                # Fallback to fast if fastest is missing
                'maxFee': float(data.get('fastest', data['fast'])['maxFee']),
                'maxPriorityFee': float(data.get('fastest', data['fast'])['maxPriorityFee'])
            },
            'baseFee': float(data.get('estimatedBaseFee', data['standard']['maxFee']))
        }
        return self.last_gas_data

    async def is_gas_acceptable(self, threshold_gwei: float) -> bool:
        """
        Check if current standard maxFee is below the threshold.
        Controls log spam by only logging on state change or periodic reminders.
        """
        import time
        gas_data = await self.fetch_gas_prices()
        if not gas_data:
            logger.warning("Could not fetch gas prices, assuming unsafe.")
            return False
            
        current_standard_fee = gas_data['standard']['maxFee']
        is_acceptable = current_standard_fee < threshold_gwei
        
        current_time = time.time()
        
        if not is_acceptable:
            # Log if:
            # 1. First time seeing high gas (Status Changed)
            # 2. It's been > 60s since last log
            if not self.was_gas_high or (current_time - self.last_high_gas_log > 60):
                logger.info(f"Gas too high: {current_standard_fee:.1f} Gwei (Threshold: {threshold_gwei} Gwei)")
                self.last_high_gas_log = current_time
                self.was_gas_high = True
        else:
            # If gas WAS high but is now acceptable, log recovery
            if self.was_gas_high:
                logger.info(f"✅ Gas recovered: {current_standard_fee:.1f} Gwei")
                self.was_gas_high = False
            
        return is_acceptable

    async def get_latest_standard_gas(self) -> float:
        """Returns the last known standard gas fee, or 0.0 if unknown."""
        if self.last_gas_data and 'standard' in self.last_gas_data:
            return self.last_gas_data['standard']['maxFee']
        return 0.0

if __name__ == "__main__":
    # Simple verification script when run directly
    async def verify_gas():
        monitor = PolygonGasMonitor()
        print("Fetching gas prices...")
        prices = await monitor.fetch_gas_prices()
        
        if prices:
            print("\n[OK] Gas Data Fetched:")
            print(f"  Standard MaxFee: {prices['standard']['maxFee']:.2f} Gwei")
            print(f"  Fast MaxFee:     {prices['fast']['maxFee']:.2f} Gwei")
            
            threshold = 50.0
            is_ok = await monitor.is_gas_acceptable(threshold)
            print(f"\nIs gas acceptable (< {threshold} Gwei)? {is_ok}")
        else:
            print("\n[FAIL] Failed to fetch gas prices.")

    logging.basicConfig(level=logging.INFO)
    asyncio.run(verify_gas())
