import asyncio
import aiohttp
import orjson
import logging
from typing import List, Dict, Any, Optional

# Configure logging
logger = logging.getLogger(__name__)

class PolymarketGammaClient:
    """Efficient Polymarket Gamma API client using orjson for fast parsing."""
    
    BASE_URL = "https://gamma-api.polymarket.com"
    
    # Complete Tag ID Mapping from Research Report
    POLYMARKET_TAG_DIRECTORY = {
        # ==================== ENTERTAINMENT ====================
        "entertainment": {
            100384: "Entertainment (General)",
            100385: "Movies & Actors",
            100386: "Music & Musicians",
            100387: "TV Shows",
            100388: "Awards (Oscars, Emmys, Grammys, etc)",
            100389: "Celebrity & Pop Culture",
            100390: "Reality TV",
            100391: "Streaming & Platforms (Netflix, etc)",
            100392: "YouTube & Content Creators",
            100393: "Video Games",
            100394: "Anime & Manga",
            100395: "Comics & Superheroes"
        },
        
        # ==================== POLITICS & ELECTIONS ====================
        "politics": {
            100381: "Politics (General)",
            100382: "2024 US Election",
            100383: "2028 US Presidential Election",
            100400: "2026 US Midterms",
            # 100392 etc duplicates handled by value uniqueness if flattening
            100396: "Elections (Global)",
        },
        
        # ==================== CRYPTOCURRENCY ====================
        "crypto": {
            100450: "Crypto (General)",
            100451: "Bitcoin (BTC)",
            100452: "Ethereum (ETH)",
            100453: "Solana (SOL)",
            100457: "Altcoins (General)",
        },
        
        # ==================== SPORTS ====================
        "sports": {
            100500: "Sports (General)",
            100501: "NFL",
            100502: "NBA",
            100503: "MLB",
            100504: "NHL",
            100507: "Soccer/Football",
            100512: "Esports",
        }
    }
    
    def __init__(self, session: Optional[aiohttp.ClientSession] = None):
        self.session = session
        
    def flatten_all_tags(self) -> List[int]:
        """Get flat list of all tag IDs."""
        all_tags = []
        for category, tags in self.POLYMARKET_TAG_DIRECTORY.items():
            all_tags.extend(tags.keys())
        return list(set(all_tags)) # Deduplicate

    async def fetch_markets_page(
        self,
        limit: int = 100,
        active: bool = True,
        offset: int = 0
    ) -> List[Dict[str, Any]]:
        """
        Fetch a single page of markets.
        """
        url = f"{self.BASE_URL}/markets"
        
        params = {
            'limit': limit,
            'offset': offset,
            'closed': 'false' if active else 'true',
            'order': 'volume24hr',
            'ascending': 'false'
        }
        
        # Ensure session exists
        session = self.session
        local_session = False
        if not session:
             session = aiohttp.ClientSession()
             local_session = True
             
        try:
            async with session.get(url, params=params, timeout=aiohttp.ClientTimeout(total=10)) as resp:
                if resp.status != 200:
                    logger.error(f"Error fetching markets page offset {offset}: Status {resp.status}")
                    temp_text = await resp.text()
                    logger.debug(f"Response: {temp_text}")
                    return []
                
                # Use orjson for 6x faster parsing
                data = await resp.read()
                try:
                    markets = orjson.loads(data)
                    
                    # CRITICAL DEBUG: Verify Sort Order on first page
                    if offset == 0 and len(markets) > 0:
                        m1 = markets[0]
                        logger.info(f"[GAMMA] 🔝 Top Market #1: {m1.get('question')} | 24h Vol: {m1.get('volume24hr')}")
                        if len(markets) > 1:
                             m2 = markets[1]
                             logger.info(f"[GAMMA] 🔝 Top Market #2: {m2.get('question')} | 24h Vol: {m2.get('volume24hr')}")

                    return markets
                except orjson.JSONDecodeError as e:
                    logger.error(f"JSON decode error: {e}")
                    return []
        
        except asyncio.TimeoutError:
            logger.warning(f"Request timeout for offset {offset}")
            return []
        except Exception as e:
            logger.error(f"Error fetching markets: {e}")
            return []
        finally:
            if local_session:
                await session.close()

    async def fetch_all_active_markets(self, max_markets: int = 2000) -> List[Dict[str, Any]]:
        """
        Fetch ALL active markets using pagination.
        This ignores tags and just sweeps the whole /markets endpoint sorted by volume.
        """
        all_markets = []
        offset = 0
        limit = 100
        consecutive_empty = 0
        
        logger.info("[GAMMA] Starting full market scan...")
        
        while consecutive_empty < 2:
            markets = await self.fetch_markets_page(limit=limit, offset=offset, active=True)
            
            if not markets:
                consecutive_empty += 1
                offset += limit
                continue
            
            consecutive_empty = 0
            
            # Strict Client-Side Filtering
            # The API might be loose with 'closed', so we double check.
            for m in markets:
                if max_markets and len(all_markets) >= max_markets:
                    break
                    
                # Strict Status Check
                is_closed = m.get('closed', False)
                is_active = m.get('active', True)
                
                if is_closed or not is_active:
                    continue
                    
                all_markets.append(m)

            # Debug Top Market with Status (Only on first page)
            if offset == 0 and len(all_markets) > 0:
                 m1 = all_markets[0]
                 logger.info(f"[GAMMA] 🔝 Top Active #1: {m1.get('question')} | 24h Vol: {m1.get('volume24hr')} | Closed: {m1.get('closed')}")
            
            logger.info(f"   Fetched {len(markets)} markets (offset {offset}). Valid Active: {len(all_markets)}")
            
            if max_markets and len(all_markets) >= max_markets:
                all_markets = all_markets[:max_markets]
                break
            
            offset += limit
            # Rate limit compliance: 25 req/s = 40ms wait
            await asyncio.sleep(0.04)

        return self._deduplicate_markets(all_markets)

    def _deduplicate_markets(self, markets: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Deduplicate markets based on 'id'."""
        seen = set()
        unique_markets = []
        for market in markets:
            m_id = market.get('id')
            if m_id and m_id not in seen:
                seen.add(m_id)
                unique_markets.append(market)
        return unique_markets

if __name__ == "__main__":
    # Verification script
    async def verify_gamma():
        async with aiohttp.ClientSession() as session:
            client = PolymarketGammaClient(session)
            print("Fetching ALL active markets...")
            all_markets = await client.fetch_all_active_markets(max_markets=200)
            print(f"✅ Found {len(all_markets)} unique markets.")
            if all_markets:
                print(f"   Sample: {all_markets[0].get('question', 'No Question')}")
                print(f"   Volume: {all_markets[0].get('volumeNum')}")

    logging.basicConfig(level=logging.INFO)
    asyncio.run(verify_gamma())
