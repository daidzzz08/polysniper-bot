Polymarket High-Frequency Arbitrage Architecture: A Comprehensive Developer Specification & Integration Guide
1. Architectural Overview and System Context
The integration of high-frequency trading (HFT) strategies within hybrid-decentralized exchange (DEX) environments presents a unique set of engineering challenges that differ fundamentally from traditional centralized exchange (CEX) architectures. This report provides an exhaustive technical specification for architects and developers integrating with the Polymarket Central Limit Order Book (CLOB). It specifically addresses the critical data ingestion failures, parsing anomalies, and market discovery blockers identified in the development of Python-based arbitrage bots.
The Polymarket architecture operates on a distinct paradigm known as the Conditional Token Framework (CTF). Unlike standard spot markets where an asset is a singular entity (e.g., BTC/USDC), Polymarket’s binary markets involve the atomic splitting of collateral into mutually exclusive outcome tokens (e.g., "Yes" and "No"). This underlying topology dictates every aspect of the API surface, from how markets are indexed in the Gamma API to how price updates are serialized in the CLOB WebSocket feeds. The parsing errors currently observed—specifically the "empty orderbook" state where bids/asks default to theoretical boundaries (0.001/0.999)—are symptomatic of a misalignment between the bot's ingestion logic and this specific data topology.1
This document dissects the three primary integration vectors required for a functional arbitrage engine:
1. Market Discovery & Filtering: Leveraging the Gamma API to identify high-velocity opportunities without hitting rate limits or ingesting stale data.
2. Real-Time Data Ingestion: Correctly parsing the CLOB WebSocket protocol, handling the specific JSON serialization standards used to preserve on-chain decimal precision.
3. Arbitrage Topology: Mapping distinct Token IDs to binary outcomes to calculate synthetic spreads and execute atomic arbitrage strategies.
The analysis is grounded in a rigorous review of the official Polymarket developer documentation, endpoint behaviors, and client library specifications.3
________________
2. Market Discovery and Ingestion Strategy (Gamma API)
Effective arbitrage requires a precise mechanism for "universe selection"—the process of filtering thousands of available markets down to a tradeable subset that meets liquidity and volume thresholds. Inefficient discovery logic leads to latency, wasted CPU cycles processing illiquid markets, and increased risk of rate-limiting.
2.1 The Data Model: Events vs. Markets
To correctly construct discovery queries, one must first understand the hierarchical data model employed by the Gamma API. The system distinguishes between "Events" and "Markets," a distinction that often confuses developers accustomed to flat ticker lists.
* Events: These are the parent containers representing the high-level question (e.g., "Will the Kansas City Chiefs win the Super Bowl?"). An Event aggregates metadata such as the title, description, and overall volume across all associated outcomes.
* Markets: These are the granular, tradeable contracts nested within an Event. In a simple binary event, there is one Market associated with the Event, but that Market splits into multiple tradeable Outcome Tokens (Yes/No).
For an HFT arbitrage bot, the Event level is the most efficient entry point for discovery. Querying the /events endpoint allows the system to filter by aggregate activity metrics (like 24-hour volume) before drilling down into the specific clobTokenIds required for WebSocket subscription.1
2.2 Query Parameter Specification
The identified issue involves the inability to correctly sort by volume or liquidity, leading to the ingestion of "zombie" markets. The Gamma API utilizes a specific query syntax that deviates from standard snake_case conventions found in other crypto APIs.
2.2.1 Sorting by 24-Hour Volume
The user hypothesized using volume24hr or liquidityNum as sort parameters. The documentation confirms that the correct parameter key for sorting is order, and the value must be the exact field name string.
Analysis of the response schema and active client implementations indicates that volume24hr is the correct field identifier for the rolling 24-hour volume metric.7 This metric is superior to liquidity for HFT purposes because it reflects active turnover and price discovery, whereas liquidity figures can sometimes represent static maker orders that may be stale or located far from the mid-market price.
* Parameter Key: order
* Parameter Value: volume24hr
   * Note: This field name is case-sensitive and must strictly follow the camelCase convention used in the API response objects.
* Directionality: To fetch the top markets, the sort order must be descending. The API uses the ascending boolean parameter for this control.
   * Parameter Key: ascending
   * Parameter Value: false
2.2.2 Lifecycle State Filtering (Active vs. Closed)
A critical requirement for the bot is to filter out markets that are "Closed" or "Resolved." A resolved market may still show historical volume but is no longer tradeable on the CLOB. Attempting to subscribe to resolved Token IDs will result in empty data feeds, contributing to the observed "empty orderbook" errors.
The Gamma API provides two primary state flags: active and closed.
1. active: A boolean flag indicating if the market is currently live and accepting orders.
2. closed: A boolean flag indicating if the market definition has been finalized or settled.
To ensure strict safety, the discovery query must explicitly require markets to be active and not closed. Some documentation also references an archived flag, which should also be negated to ensure the exclusion of long-settled legacy markets.5
* Parameter: active -> true
* Parameter: closed -> false
2.3 Developer Specification: Top 50 Active Liquid Markets
Based on the requirements and documentation analysis, the following URL construction is the definitive method for initializing the bot’s target list. This query effectively asks the Gamma API for the "50 most heavily traded, currently open events."
2.3.1 API Request Construction
Endpoint: https://gamma-api.polymarket.com/events
Query Parameters:


Parameter Name
	Value
	Description
	Source Verification
	limit
	50
	Restricts the payload to the top 50 entries to manage memory and latency.
	6
	active
	true
	Hard filter to ensure the event is currently live.
	1
	closed
	false
	Hard filter to exclude settled or resolved markets.
	6
	order
	volume24hr
	Sorts the result set by the 24-hour volume metric.
	7
	ascending
	false
	Ensures the sort is Descending (Highest Volume First).
	6
	Constructed URL:


HTTP




https://gamma-api.polymarket.com/events?limit=50&active=true&closed=false&order=volume24hr&ascending=false

2.3.2 Python Implementation Logic
The following Python snippet demonstrates how to execute this discovery logic using aiohttp, consistent with the user's stack. It includes the critical step of parsing the nested markets array to extract the clobTokenIds, which are the actual keys needed for the WebSocket phase.


Python




import aiohttp
import asyncio
from typing import List, Dict

async def fetch_top_markets(session: aiohttp.ClientSession) -> List:
   """
   Fetches the top 50 active markets by 24h volume using the Gamma API.
   Returns a list of market objects containing clobTokenIds.
   """
   url = "https://gamma-api.polymarket.com/events"
   params = {
       "limit": "50",
       "active": "true",
       "closed": "false",
       "order": "volume24hr",
       "ascending": "false"
   }

   try:
       async with session.get(url, params=params) as response:
           if response.status!= 200:
               print(f"Error fetching markets: HTTP {response.status}")
               return
           
           events = await response.json()
           tradeable_assets =

           for event in events:
               # Events contain a 'markets' list. 
               # We must iterate to find the specific binary market wrapper.
               markets = event.get("markets",)
               
               for market in markets:
                   # Extract the Token IDs required for CLOB subscription
                   # 'clobTokenIds' is typically a list of strings: ["0x...", "0x..."]
                   token_ids = market.get("clobTokenIds",)
                   
                   if token_ids and len(token_ids) == 2:
                       tradeable_assets.append({
                           "event_slug": event.get("slug"),
                           "question": market.get("question"),
                           "condition_id": market.get("conditionId"),
                           "token_ids": token_ids,  #
                           "outcomes": market.get("outcomes") #
                       })
           
           return tradeable_assets

   except Exception as e:
       print(f"Critical failure in market discovery: {str(e)}")
       return

Insight: The standard JSON response does not flatten the markets. The bot must handle the nested structure Event -> Markets -> clobTokenIds. Failure to drill down to clobTokenIds is a common reason for developers attempting to subscribe to conditionIds instead, which causes the WebSocket to fail silently.1
________________
3. WebSocket Data Structure and Parsing Logic
The core failure mode described—"Ask: 0.999 / Bid: 0.001"—is a deterministic behavior of the client when it processes an "empty" orderbook. If the parsing logic fails to extract valid bids and asks, the bot logic likely defaults to these boundary values (representing 0% and 100% probability) to prevent execution.
The root cause is almost certainly a type mismatch in the JSON parsing of the bids and asks arrays.
3.1 The CLOB JSON Topology
Unlike many financial APIs that use "Lists of Lists" (e.g., [[price, size], [price, size]]), Polymarket’s CLOB API utilizes Lists of Dictionaries (Arrays of Objects). Furthermore, all numerical values for price and size are serialized as Strings.
* Why Strings? This is a deliberate design choice in Web3 infrastructure to prevent precision loss. Floating-point arithmetic (IEEE 754) is notoriously imprecise for financial calculations. Polymarket relies on string representations to allow clients to parse into Decimal types or BigInt (scaled values) directly, ensuring that a price of "0.55" is treated exactly as "0.55" and not "0.55000000000000004".
3.1.1 Structure Verification (Scenario C)
Research into the market channel’s book event confirms Scenario C is the correct structure.
* Field: bids
* Type: Array of Objects
* Object Keys: price, size
* Value Types: string, string
Documentation Evidence: The CLOB WebSocket documentation explicitly lists the structure of the orderbook level as having "Name: price, size" and "Type: string, string".12 Snippet 12 provides a concrete example showing the dictionary structure.
Visual Schema:


JSON




{
 "event_type": "book",
 "asset_id": "0xTokenID...",
 "market": "0xConditionID...",
 "timestamp": "1699999999999",
 "hash": "0x...",
 "bids": [
   { "price": "0.55", "size": "1500.00" },
   { "price": "0.54", "size": "5000.50" }
 ],
 "asks": [
   { "price": "0.58", "size": "2000.00" },
   { "price": "0.59", "size": "100.00" }
 ]
}

3.2 Corrected Parsing Logic
The failure described implies the user's current code likely attempts to access list indices (e.g., order for price) which works for Binance/Coinbase but raises TypeError or KeyError on Polymarket.
Below is the corrected Python parsing logic. It utilizes the decimal module to handle the string inputs precisely, which is mandatory for arbitrage calculations where a spread of $0.001 determines profitability.


Python




import json
from decimal import Decimal
from typing import List, Tuple, Dict, Optional

class OrderBookParser:
   """
   Specialized parser for Polymarket CLOB WebSocket messages.
   Handles 'book' snapshots and 'price_change' updates.
   """

    @staticmethod
   def parse_book_snapshot(payload: Dict) -> Tuple], List]]:
       """
       Parses the full orderbook snapshot.
       
       Input Schema:
       {
           "bids": [{"price": "0.55", "size": "100"},...],
           "asks": [{"price": "0.65", "size": "50"},...]
       }
       
       Returns:
           (bids, asks) where each is a list of (price, size) tuples.
           Bids are sorted Descending (Best Bid first).
           Asks are sorted Ascending (Best Ask first).
       """
       # Safely extract lists, defaulting to empty if missing
       raw_bids = payload.get("bids",)
       raw_asks = payload.get("asks",)

       # Parsing Logic:
       # 1. Iterate over the list of DICTIONARIES.
       # 2. Extract "price" and "size" by key.
       # 3. Convert strict strings to Decimal to preserve precision.
       
       bids =
       for order in raw_bids:
           try:
               # CRITICAL: Access by key ["price"], not index 
               p = Decimal(order["price"])
               s = Decimal(order["size"])
               bids.append((p, s))
           except (KeyError, ValueError, TypeError) as e:
               # Log malformed order but continue processing others
               continue

       asks =
       for order in raw_asks:
           try:
               p = Decimal(order["price"])
               s = Decimal(order["size"])
               asks.append((p, s))
           except (KeyError, ValueError, TypeError) as e:
               continue

       # Sort Bids: Highest price first (Best Bid)
       bids.sort(key=lambda x: x, reverse=True)
       
       # Sort Asks: Lowest price first (Best Ask)
       asks.sort(key=lambda x: x, reverse=False)

       return bids, asks

    @staticmethod
   def is_empty_book(bids: List, asks: List) -> bool:
       """
       Helper to detect the 'empty book' state.
       """
       return len(bids) == 0 or len(asks) == 0

# Usage Simulation
# message = json.loads(websocket_message)
# if message.get("event_type") == "book":
#     bids, asks = OrderBookParser.parse_book_snapshot(message)
#     if OrderBookParser.is_empty_book(bids, asks):
#         print("Warning: Market has no liquidity")
#     else:
#         print(f"Spread: {asks - bids}")

Implementation Note on "price_change" Events: After the initial book snapshot, Polymarket sends incremental updates via price_change events. These updates also use the dictionary structure but include a side field ("BUY" or "SELL"). The parser must handle these differently: a size of "0" in a price_change event indicates the removal of a price level.12
________________
4. Token Topology and Spread Calculation
The most conceptually distinct aspect of Polymarket for an arbitrageur is the relationship between Token IDs, Condition IDs, and the Binary Spread.
4.1 Token ID vs. Condition ID Mapping
The user queried whether to use clobTokenIds or conditionId for WebSocket subscription.
* Condition ID: Represents the "Market Question" (e.g., "Will BTC > 100k?"). It is the parent identifier used for grouping.
* Token ID (Asset ID): Represents the specific ERC-1155 asset (e.g., "The YES Token for BTC > 100k").
Verdict: The WebSocket market channel explicitly requires Token IDs (referred to as assets_ids in the subscription payload). If a developer subscribes using the conditionId, the CLOB matcher will ignore the request as it does not correspond to a specific orderbook asset.4
Correct Subscription Payload:


JSON




{
   "type": "MARKET",
   "assets_ids":
}

4.2 The "Split" and Spread Mechanics
In a binary market, the two outcomes (Yes/No) are complementary. The system invariant is that 1 YES + 1 NO = 1 Unit of Collateral (e.g., $1.00 USDC). This creates a specialized arbitrage condition known as "Minting Arbitrage."
To calculate the spread or the "cost of market," one cannot simply look at the spread of the YES token (Ask_Yes - Bid_Yes). That is merely the trading spread for that single asset.
The Arbitrage Spread (Synthetic Spread):
The true spread for an arbitrage bot is the deviation of the combined cost of outcomes from the collateral unit ($1.00).
* Cost to Buy Market: Best_Ask(Yes) + Best_Ask(No)
   * If Cost < 1.00, the bot can buy both, mint a complete set, and redeem for profit (ignoring fees).
* Value to Sell Market: Best_Bid(Yes) + Best_Bid(No)
   * If Value > 1.00, the bot can sell both (if it holds inventory) or short both (if supported), effectively selling a $1.00 bill for >$1.00.
4.3 Requirement for Dual Subscription
To perform this calculation, the bot must subscribe to both Token IDs independently.
* Does subscribing to one give the whole market? No.
The CLOB treats "YES" and "NO" as completely separate assets with separate orderbooks. Subscribing to the YES token ID will only stream book and price_change events for the YES token. It will contain zero information about the NO token.
Conclusion: For every binary market identified in the Gamma discovery phase, the bot must initiate two WebSocket subscriptions (or one subscription with two IDs in the list).
4.4 Spread Calculation Formula
The following specification details the exact formula for determining the arbitrage opportunity, incorporating the fee structure (which is typically built into the net proceeds, but for entry price calculation, raw Ask prices are used).
Formula:
  

  

Python Logic:


Python




from decimal import Decimal

def check_arbitrage_opportunity(book_yes: Dict, book_no: Dict) -> bool:
   """
   Calculates if a risk-free arbitrage exists between the Yes and No orderbooks.
   
   Args:
       book_yes: The local orderbook object for the YES token.
       book_no: The local orderbook object for the NO token.
       
   Returns:
       bool: True if arbitrage is possible.
   """
   # 1. Validate Liquidity
   if not book_yes['asks'] or not book_no['asks']:
       return False

   # 2. Extract Best Asks (Lowest Price)
   # Assumes books are sorted: asks is the lowest price
   best_ask_yes_price = book_yes['asks']
   best_ask_no_price = book_no['asks']

   # 3. Calculate Total Cost to Buy 1.00 Unit of Probability
   total_entry_cost = best_ask_yes_price + best_ask_no_price

   # 4. Check against Collateral Value ($1.00)
   # We use a threshold slightly below 1.00 to account for taker fees (e.g., 0.1% or 0.2%)
   # Current Polymarket taker fee is often 0% for limit orders but can vary for takers.
   # Let's assume a safe threshold of 0.99 for this example.
   arbitrage_threshold = Decimal("0.995") 

   if total_entry_cost < arbitrage_threshold:
       print(f"ARBITRAGE FOUND! Cost: {total_entry_cost}")
       print(f"Buy YES @ {best_ask_yes_price} | Buy NO @ {best_ask_no_price}")
       return True
   
   return False

________________
5. Implementation Summary and Best Practices
5.1 Connection Management
When using aiohttp and websockets, it is recommended to maintain a single persistent connection for the market channel and multiplex the subscriptions. Polymarket supports subscribing to multiple asset IDs in a single message, or sending sequential subscribe operations on an open socket.
5.2 Error Handling for "Empty Books"
The user's original error (0.999/0.001) is a safeguard default. The parsing logic provided in Section 3.2 removes the need for this default by handling the KeyError. However, if the API genuinely returns an empty list for bids or asks (which can happen in illiquid markets), the bot must explicitly flag the market as "Untradeable" rather than defaulting to prices that might trigger a bad order.
Recommendation:
   * If len(bids) == 0: Set Best Bid = None or Decimal("0").
   * If len(asks) == 0: Set Best Ask = None or Decimal("1.00") (Infinity equivalent).
   * Logic: Do not attempt spread calculations if either side is None.
5.3 Final Checklist
   1. Discovery: Use Gamma API with order=volume24hr, active=true, closed=false.
   2. Mapping: Extract clobTokenIds (List of 2 strings) from the Gamma response.
   3. Subscription: Send assets_ids (the extracted token IDs) to the WebSocket.
   4. Parsing: Parse bids/asks as Lists of Dictionaries, converting string values to Decimals.
   5. Math: Sum the Best Ask of Token A and Best Ask of Token B to find the arbitrage delta from 1.00.
By adhering to this specification, the bot will align perfectly with Polymarket's data topology, eliminating the parsing errors and ensuring access to the highest-quality liquidity data available.
Nguồn trích dẫn
   1. Fetching Market Data - Polymarket Documentation, truy cập vào tháng 1 28, 2026, https://docs.polymarket.com/quickstart/fetching-data
   2. CLOB Introduction - Polymarket Documentation, truy cập vào tháng 1 28, 2026, https://docs.polymarket.com/developers/CLOB/introduction
   3. The Polymarket API: Architecture, Endpoints, and Use Cases - Medium, truy cập vào tháng 1 28, 2026, https://medium.com/@gwrx2005/the-polymarket-api-architecture-endpoints-and-use-cases-f1d88fa6c1bf
   4. WSS Overview - Polymarket Documentation, truy cập vào tháng 1 28, 2026, https://docs.polymarket.com/developers/CLOB/websocket/wss-overview
   5. agents/agents/polymarket/gamma.py at main - GitHub, truy cập vào tháng 1 28, 2026, https://github.com/Polymarket/agents/blob/main/agents/polymarket/gamma.py
   6. How to Fetch Markets - Polymarket Documentation, truy cập vào tháng 1 28, 2026, https://docs.polymarket.com/developers/gamma-markets-api/fetch-markets-guide
   7. Polymarket Markets Scraper · Apify, truy cập vào tháng 1 28, 2026, https://apify.com/louisdeconinck/polymarket-events-scraper
   8. polymarketgamma package - github.com/ivanzzeth/polymarket-go-gamma-client - Go Packages, truy cập vào tháng 1 28, 2026, https://pkg.go.dev/github.com/ivanzzeth/polymarket-go-gamma-client
   9. List events - Polymarket Documentation, truy cập vào tháng 1 28, 2026, https://docs.polymarket.com/api-reference/events/list-events
   10. Get Markets - Polymarket Documentation, truy cập vào tháng 1 28, 2026, https://docs.polymarket.com/developers/gamma-markets-api/get-markets
   11. github.com/mathiasme/Polymarket v0.0.0-20250922211821-e258a02b69fe on Go - Libraries.io, truy cập vào tháng 1 28, 2026, https://libraries.io/go/github.com%2Fmathiasme%2FPolymarket
   12. Market Channel - Polymarket Documentation, truy cập vào tháng 1 28, 2026, https://docs.polymarket.com/developers/CLOB/websocket/market-channel