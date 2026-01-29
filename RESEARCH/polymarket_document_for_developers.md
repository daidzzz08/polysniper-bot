# Polymarket Documentation

## Docs

- [Create deposit addresses](https://docs.polymarket.com/api-reference/bridge/create-deposit-addresses.md): Generate unique deposit addresses for bridging assets to Polymarket.

**How it works:**
1. Request deposit addresses for your Polymarket wallet
2. Receive deposit addresses for each blockchain type (EVM, Solana, Bitcoin)
3. Send assets to the appropriate deposit address for your source chain
4. Assets are automatically bridged and swapped to USDC.e on Polygon
5. USDC.e is credited to your Polymarket wallet for trading

- [Get a quote](https://docs.polymarket.com/api-reference/bridge/get-a-quote.md): Get an estimated quote for a deposit or withdrawal, including output amounts, checkout time, and a detailed fee breakdown.

**Use Cases:**
- Preview fees and estimated output before executing a deposit or withdrawal
- Compare costs across different token/chain combinations
- Get the `quoteId` to reference this specific quote

**Notes:**
- Quotes are estimates and actual amounts may vary slightly due to market conditions
- See `/supported-assets` for a list of all supported chains and tokens

- [Get deposit status](https://docs.polymarket.com/api-reference/bridge/get-deposit-status.md): Get the transaction status for all deposits associated with a given deposit address.

**Usage:**
- Use the deposit address returned from the `/deposit` endpoint (EVM, SVM, or BTC address)
- Poll this endpoint to track the progress of your deposits

**Status Values:**
- `DEPOSIT_DETECTED`: Deposit detected but not yet processing
- `PROCESSING`: Transaction is being routed and swapped
- `ORIGIN_TX_CONFIRMED`: Origin transaction has been confirmed on source chain
- `SUBMITTED`: Transaction has been submitted to destination chain
- `COMPLETED`: Transaction completed successfully
- `FAILED`: Transaction encountered an error and did not complete

**Notes:**
- Transactions typically complete within a few minutes, but may take longer depending on network conditions
- An empty transactions array means no deposits have been made to this address yet

- [Get supported assets](https://docs.polymarket.com/api-reference/bridge/get-supported-assets.md): Retrieve all supported chains and tokens for deposits.

**USDC.e on Polygon:**
Polymarket uses USDC.e (Bridged USDC from Ethereum) on Polygon as the native collateral for all markets. When you deposit assets from other chains, they are automatically bridged and swapped to USDC.e on Polygon, which is then used as collateral for trading on Polymarket.

**Minimum Deposit Amounts:**
Each asset has a `minCheckoutUsd` field indicating the minimum deposit amount required in USD. Make sure your deposit meets this minimum to avoid transaction failures.

- [Get aggregated builder leaderboard](https://docs.polymarket.com/api-reference/builders/get-aggregated-builder-leaderboard.md): Returns aggregated builder rankings with one entry per builder showing total for the specified time period. Supports pagination.
- [Get daily builder volume time-series](https://docs.polymarket.com/api-reference/builders/get-daily-builder-volume-time-series.md): Returns daily time-series volume data with multiple entries per builder (one per day), each including a `dt` timestamp. No pagination.
- [Get comments by comment id](https://docs.polymarket.com/api-reference/comments/get-comments-by-comment-id.md)
- [Get comments by user address](https://docs.polymarket.com/api-reference/comments/get-comments-by-user-address.md)
- [List comments](https://docs.polymarket.com/api-reference/comments/list-comments.md)
- [Get closed positions for a user](https://docs.polymarket.com/api-reference/core/get-closed-positions-for-a-user.md): Fetches closed positions for a user(address)
- [Get current positions for a user](https://docs.polymarket.com/api-reference/core/get-current-positions-for-a-user.md): Returns positions filtered by user and optional filters.
- [Get top holders for markets](https://docs.polymarket.com/api-reference/core/get-top-holders-for-markets.md)
- [Get total value of a user's positions](https://docs.polymarket.com/api-reference/core/get-total-value-of-a-users-positions.md)
- [Get trader leaderboard rankings](https://docs.polymarket.com/api-reference/core/get-trader-leaderboard-rankings.md): Returns trader leaderboard rankings filtered by category, time period, and ordering.
- [Get trades for a user or markets](https://docs.polymarket.com/api-reference/core/get-trades-for-a-user-or-markets.md)
- [Get user activity](https://docs.polymarket.com/api-reference/core/get-user-activity.md): Returns on-chain activity for a user.
- [Data API Health check](https://docs.polymarket.com/api-reference/data-api-status/data-api-health-check.md)
- [Get event by id](https://docs.polymarket.com/api-reference/events/get-event-by-id.md)
- [Get event by slug](https://docs.polymarket.com/api-reference/events/get-event-by-slug.md)
- [Get event tags](https://docs.polymarket.com/api-reference/events/get-event-tags.md)
- [List events](https://docs.polymarket.com/api-reference/events/list-events.md)
- [Gamma API Health check](https://docs.polymarket.com/api-reference/gamma-status/gamma-api-health-check.md)
- [Get market by id](https://docs.polymarket.com/api-reference/markets/get-market-by-id.md)
- [Get market by slug](https://docs.polymarket.com/api-reference/markets/get-market-by-slug.md)
- [Get market tags by id](https://docs.polymarket.com/api-reference/markets/get-market-tags-by-id.md)
- [List markets](https://docs.polymarket.com/api-reference/markets/list-markets.md)
- [Get live volume for an event](https://docs.polymarket.com/api-reference/misc/get-live-volume-for-an-event.md)
- [Get open interest](https://docs.polymarket.com/api-reference/misc/get-open-interest.md)
- [Get total markets a user has traded](https://docs.polymarket.com/api-reference/misc/get-total-markets-a-user-has-traded.md)
- [Get multiple order books summaries by request](https://docs.polymarket.com/api-reference/orderbook/get-multiple-order-books-summaries-by-request.md): Retrieves order book summaries for specified tokens via POST request
- [Get order book summary](https://docs.polymarket.com/api-reference/orderbook/get-order-book-summary.md): Retrieves the order book summary for a specific token
- [Get market price](https://docs.polymarket.com/api-reference/pricing/get-market-price.md): Retrieves the market price for a specific token and side
- [Get midpoint price](https://docs.polymarket.com/api-reference/pricing/get-midpoint-price.md): Retrieves the midpoint price for a specific token
- [Get multiple market prices](https://docs.polymarket.com/api-reference/pricing/get-multiple-market-prices.md): Retrieves market prices for multiple tokens and sides
- [Get multiple market prices by request](https://docs.polymarket.com/api-reference/pricing/get-multiple-market-prices-by-request.md): Retrieves market prices for specified tokens and sides via POST request
- [Get price history for a traded token](https://docs.polymarket.com/api-reference/pricing/get-price-history-for-a-traded-token.md): Fetches historical price data for a specified market token
- [Get public profile by wallet address](https://docs.polymarket.com/api-reference/profiles/get-public-profile-by-wallet-address.md)
- [Search markets, events, and profiles](https://docs.polymarket.com/api-reference/search/search-markets-events-and-profiles.md)
- [Get series by id](https://docs.polymarket.com/api-reference/series/get-series-by-id.md)
- [List series](https://docs.polymarket.com/api-reference/series/list-series.md)
- [Get sports metadata information](https://docs.polymarket.com/api-reference/sports/get-sports-metadata-information.md): Retrieves metadata for various sports including images, resolution sources, ordering preferences, tags, and series information. This endpoint provides comprehensive sport configuration data used throughout the platform.
- [Get valid sports market types](https://docs.polymarket.com/api-reference/sports/get-valid-sports-market-types.md): Get a list of all valid sports market types available on the platform. Use these values when filtering markets by the sportsMarketTypes parameter.
- [List teams](https://docs.polymarket.com/api-reference/sports/list-teams.md)
- [Get bid-ask spreads](https://docs.polymarket.com/api-reference/spreads/get-bid-ask-spreads.md): Retrieves bid-ask spreads for multiple tokens
- [Get related tags (relationships) by tag id](https://docs.polymarket.com/api-reference/tags/get-related-tags-relationships-by-tag-id.md)
- [Get related tags (relationships) by tag slug](https://docs.polymarket.com/api-reference/tags/get-related-tags-relationships-by-tag-slug.md)
- [Get tag by id](https://docs.polymarket.com/api-reference/tags/get-tag-by-id.md)
- [Get tag by slug](https://docs.polymarket.com/api-reference/tags/get-tag-by-slug.md)
- [Get tags related to a tag id](https://docs.polymarket.com/api-reference/tags/get-tags-related-to-a-tag-id.md)
- [Get tags related to a tag slug](https://docs.polymarket.com/api-reference/tags/get-tags-related-to-a-tag-slug.md)
- [List tags](https://docs.polymarket.com/api-reference/tags/list-tags.md)
- [Polymarket Changelog](https://docs.polymarket.com/changelog/changelog.md): Welcome to the Polymarket Changelog. Here you will find any important changes to Polymarket, including but not limited to CLOB, API, UI and Mobile Applications.
- [Authentication](https://docs.polymarket.com/developers/CLOB/authentication.md): Understanding authentication using Polymarket's CLOB
- [Builder Methods](https://docs.polymarket.com/developers/CLOB/clients/methods-builder.md): These methods require builder API credentials and are only relevant for Builders Program order attribution.
- [L1 Methods](https://docs.polymarket.com/developers/CLOB/clients/methods-l1.md): These methods require a wallet signer (private key) but do not require user API credentials. Use these for initial setup.
- [L2 Methods](https://docs.polymarket.com/developers/CLOB/clients/methods-l2.md): These methods require user API credentials (L2 headers). Use these for placing trades and managing user's positions.
- [Methods Overview](https://docs.polymarket.com/developers/CLOB/clients/methods-overview.md): CLOB client methods require different levels of authentication. This reference is organized by what credentials you need to call each method. 
- [Public Methods](https://docs.polymarket.com/developers/CLOB/clients/methods-public.md): These methods can be called without a signer or user credentials. Use these for reading market data, prices, and order books.
- [Geographic Restrictions](https://docs.polymarket.com/developers/CLOB/geoblock.md): Check geographic restrictions before placing orders on Polymarket's CLOB
- [CLOB Introduction](https://docs.polymarket.com/developers/CLOB/introduction.md)
- [Cancel Orders(s)](https://docs.polymarket.com/developers/CLOB/orders/cancel-orders.md): Multiple endpoints to cancel a single order, multiple orders, all orders or all orders from a single market.
- [Check Order Reward Scoring](https://docs.polymarket.com/developers/CLOB/orders/check-scoring.md): Check if an order is eligble or scoring for Rewards purposes
- [Place Single Order](https://docs.polymarket.com/developers/CLOB/orders/create-order.md): Detailed instructions for creating, placing, and managing orders using Polymarket's CLOB API.
- [Place Multiple Orders (Batching)](https://docs.polymarket.com/developers/CLOB/orders/create-order-batch.md): Instructions for placing multiple orders(Batch)
- [Get Active Orders](https://docs.polymarket.com/developers/CLOB/orders/get-active-order.md)
- [Get Order](https://docs.polymarket.com/developers/CLOB/orders/get-order.md): Get information about an existing order
- [Onchain Order Info](https://docs.polymarket.com/developers/CLOB/orders/onchain-order-info.md)
- [Orders Overview](https://docs.polymarket.com/developers/CLOB/orders/orders.md): Detailed instructions for creating, placing, and managing orders using Polymarket's CLOB API.
- [Quickstart](https://docs.polymarket.com/developers/CLOB/quickstart.md): Initialize the CLOB and place your first order.
- [null](https://docs.polymarket.com/developers/CLOB/status.md)
- [Historical Timeseries Data](https://docs.polymarket.com/developers/CLOB/timeseries.md): Fetches historical price data for a specified market token.

- [Get Trades](https://docs.polymarket.com/developers/CLOB/trades/trades.md)
- [Trades Overview](https://docs.polymarket.com/developers/CLOB/trades/trades-overview.md)
- [Market Channel](https://docs.polymarket.com/developers/CLOB/websocket/market-channel.md)
- [User Channel](https://docs.polymarket.com/developers/CLOB/websocket/user-channel.md)
- [WSS Authentication](https://docs.polymarket.com/developers/CLOB/websocket/wss-auth.md)
- [WSS Overview](https://docs.polymarket.com/developers/CLOB/websocket/wss-overview.md): Overview and general information about the Polymarket Websocket
- [Deployment and Additional Information](https://docs.polymarket.com/developers/CTF/deployment-resources.md)
- [Merging Tokens](https://docs.polymarket.com/developers/CTF/merge.md)
- [Overview](https://docs.polymarket.com/developers/CTF/overview.md)
- [Reedeeming Tokens](https://docs.polymarket.com/developers/CTF/redeem.md)
- [Splitting USDC](https://docs.polymarket.com/developers/CTF/split.md)
- [RTDS Comments](https://docs.polymarket.com/developers/RTDS/RTDS-comments.md)
- [RTDS Crypto Prices](https://docs.polymarket.com/developers/RTDS/RTDS-crypto-prices.md)
- [Real Time Data Socket](https://docs.polymarket.com/developers/RTDS/RTDS-overview.md)
- [Builder Program Introduction](https://docs.polymarket.com/developers/builders/builder-intro.md): Learn about Polymarket's Builder Program and how to integrate
- [Builder Profile & Keys](https://docs.polymarket.com/developers/builders/builder-profile.md): Learn how to access your builder profile and obtain API credentials
- [Builder Tiers](https://docs.polymarket.com/developers/builders/builder-tiers.md): Permissionless integration with tiered rate limits, rewards, and revenue generating opportunities as you scale
- [Examples](https://docs.polymarket.com/developers/builders/examples.md): Complete Next.js applications demonstrating Polymarket builder integration
- [Order Attribution](https://docs.polymarket.com/developers/builders/order-attribution.md): Learn how to attribute orders to your builder account
- [Relayer Client](https://docs.polymarket.com/developers/builders/relayer-client.md): Use Polymarket's Polygon relayer to execute gasless transactions for your users
- [How to Fetch Markets](https://docs.polymarket.com/developers/gamma-markets-api/fetch-markets-guide.md)
- [Gamma Structure](https://docs.polymarket.com/developers/gamma-markets-api/gamma-structure.md)
- [null](https://docs.polymarket.com/developers/gamma-markets-api/overview.md)
- [Data Feeds](https://docs.polymarket.com/developers/market-makers/data-feeds.md): Real-time and historical data sources for market makers
- [Market Maker Introduction](https://docs.polymarket.com/developers/market-makers/introduction.md): Overview of market making on Polymarket and available tools for liquidity providers
- [Inventory Management](https://docs.polymarket.com/developers/market-makers/inventory.md): Split, merge, and redeem outcome tokens for market making
- [Liquidity Rewards](https://docs.polymarket.com/developers/market-makers/liquidity-rewards.md): Polymarket provides incentives aimed at catalyzing the supply and demand side of the marketplace. Specifically there is a public liquidity rewards program as well as one-off public pnl/volume competitions.
- [Maker Rebates Program](https://docs.polymarket.com/developers/market-makers/maker-rebates-program.md): Technical guide for handling taker fees and earning maker rebates on Polymarket
- [Setup](https://docs.polymarket.com/developers/market-makers/setup.md): One-time setup for market making on Polymarket: deposits, approvals, wallets, and API keys
- [Trading](https://docs.polymarket.com/developers/market-makers/trading.md): CLOB order entry and management for market makers
- [Overview](https://docs.polymarket.com/developers/misc-endpoints/bridge-overview.md): Bridge and swap assets to Polymarket
- [Overview](https://docs.polymarket.com/developers/neg-risk/overview.md)
- [null](https://docs.polymarket.com/developers/proxy-wallet.md)
- [Resolution](https://docs.polymarket.com/developers/resolution/UMA.md)
- [Message Format](https://docs.polymarket.com/developers/sports-websocket/message-format.md): Structure of sports result update messages
- [Overview](https://docs.polymarket.com/developers/sports-websocket/overview.md): Real-time sports results via WebSocket
- [Quickstart](https://docs.polymarket.com/developers/sports-websocket/quickstart.md): Connect to the Sports WebSocket and receive live updates
- [null](https://docs.polymarket.com/developers/subgraph/overview.md)
- [Does Polymarket have an API?](https://docs.polymarket.com/polymarket-learn/FAQ/does-polymarket-have-an-api.md): Getting data from Polymarket
- [How To Use Embeds](https://docs.polymarket.com/polymarket-learn/FAQ/embeds.md): Adding market embeds to your Substack or website.
- [Geographic Restrictions](https://docs.polymarket.com/polymarket-learn/FAQ/geoblocking.md): Countries and regions where Polymarket is restricted
- [How Do I Export My Key?](https://docs.polymarket.com/polymarket-learn/FAQ/how-to-export-private-key.md): Exporting your private key on Magic.Link
- [Is My Money Safe?](https://docs.polymarket.com/polymarket-learn/FAQ/is-my-money-safe.md): Yes. Polymarket is non-custodial, so you're in control of your funds.
- [Is Polymarket The House?](https://docs.polymarket.com/polymarket-learn/FAQ/is-polymarket-the-house.md): No, Polymarket is not the house. All trades happen peer-to-peer (p2p).
- [Polymarket vs. Polling](https://docs.polymarket.com/polymarket-learn/FAQ/polling.md): How is Polymarket better than traditional / legacy polling?
- [Recover Missing Deposit](https://docs.polymarket.com/polymarket-learn/FAQ/recover-missing-deposit.md): If you deposited the wrong cryptocurrency on Ethereum or Polygon, use these tools to recover those funds.
- [Can I Sell Early?](https://docs.polymarket.com/polymarket-learn/FAQ/sell-early.md)
- [How Do I Contact Support?](https://docs.polymarket.com/polymarket-learn/FAQ/support.md): Polymarket offers technical support through our website chat feature, and through Discord.
- [Does Polymarket Have a Token?](https://docs.polymarket.com/polymarket-learn/FAQ/wen-token.md)
- [What is a Prediction Market?](https://docs.polymarket.com/polymarket-learn/FAQ/what-are-prediction-markets.md): How people collectively forecast the future.
- [Why Crypto?](https://docs.polymarket.com/polymarket-learn/FAQ/why-do-i-need-crypto.md): Why Polymarket uses crypto and blockchain technology to create the world’s largest Prediction market.
- [Deposit with Coinbase](https://docs.polymarket.com/polymarket-learn/deposits/coinbase.md): How to buy and deposit USDC to your Polymarket account using Coinbase.
- [How to Withdraw](https://docs.polymarket.com/polymarket-learn/deposits/how-to-withdraw.md): How to withdraw your cash balance from Polymarket.
- [Large Cross Chain Deposits](https://docs.polymarket.com/polymarket-learn/deposits/large-cross-chain-deposits.md)
- [Deposit Using Your Card](https://docs.polymarket.com/polymarket-learn/deposits/moonpay.md): Use MoonPay to deposit cash using your Visa, Mastercard, or bank account.
- [Deposit by Transfering Crypto](https://docs.polymarket.com/polymarket-learn/deposits/supported-tokens.md): Learn what Tokens and Chains are supported for deposit.
- [Deposit USDC on Ethereum](https://docs.polymarket.com/polymarket-learn/deposits/usdc-on-eth.md): How to deposit USDC on the Ethereum Network to your Polymarket account.
- [How to Deposit](https://docs.polymarket.com/polymarket-learn/get-started/how-to-deposit.md): How to add cash to your balance on Polymarket.
- [How to Sign-Up](https://docs.polymarket.com/polymarket-learn/get-started/how-to-signup.md): How to create a Polymarket account.
- [Making Your First Trade](https://docs.polymarket.com/polymarket-learn/get-started/making-your-first-trade.md): How to buy shares.
- [What is Polymarket?](https://docs.polymarket.com/polymarket-learn/get-started/what-is-polymarket.md)
- [How Are Markets Disputed?](https://docs.polymarket.com/polymarket-learn/markets/dispute.md)
- [How Are Markets Clarified?](https://docs.polymarket.com/polymarket-learn/markets/how-are-markets-clarified.md): How are markets on Polymarket clarified?
- [How Are Markets Created?](https://docs.polymarket.com/polymarket-learn/markets/how-are-markets-created.md): Markets are created by the markets team with input from users and the community.
- [How Are Prediction Markets Resolved?](https://docs.polymarket.com/polymarket-learn/markets/how-are-markets-resolved.md): Markets are resolved by the UMA Optimistic Oracle, a smart-contract based optimistic oracle.
- [Trading Fees](https://docs.polymarket.com/polymarket-learn/trading/fees.md)
- [Holding Rewards](https://docs.polymarket.com/polymarket-learn/trading/holding-rewards.md)
- [How Are Prices Calculated?](https://docs.polymarket.com/polymarket-learn/trading/how-are-prices-calculated.md): The prices probabilities displayed on Polymarket are the midpoint of the bid-ask spread in the orderbook.
- [Limit Orders](https://docs.polymarket.com/polymarket-learn/trading/limit-orders.md): What are limit orders and how to make them.
- [Liquidity Rewards](https://docs.polymarket.com/polymarket-learn/trading/liquidity-rewards.md): Learn how to earn rewards merely by placing trades on Polymarket
- [Maker Rebates Program](https://docs.polymarket.com/polymarket-learn/trading/maker-rebates-program.md)
- [Market Orders](https://docs.polymarket.com/polymarket-learn/trading/market-orders.md): How to buy shares.
- [Does Polymarket Have Trading Limits?](https://docs.polymarket.com/polymarket-learn/trading/no-limits.md)
- [Using the Order Book](https://docs.polymarket.com/polymarket-learn/trading/using-the-orderbook.md): Understanding the Order Book will help you become an advanced trader.
- [Fetching Market Data](https://docs.polymarket.com/quickstart/fetching-data.md): Fetch Polymarket data in minutes with no authentication required
- [Placing Your First Order](https://docs.polymarket.com/quickstart/first-order.md): Set up authentication and submit your first trade
- [API Rate Limits](https://docs.polymarket.com/quickstart/introduction/rate-limits.md)
- [Developer Quickstart](https://docs.polymarket.com/quickstart/overview.md): Get started building with Polymarket APIs
- [Endpoints](https://docs.polymarket.com/quickstart/reference/endpoints.md): All Polymarket API URLs and base endpoints
- [Glossary](https://docs.polymarket.com/quickstart/reference/glossary.md): Key terms and concepts for Polymarket developers
- [WSS Quickstart](https://docs.polymarket.com/quickstart/websocket/WSS-Quickstart.md)


## Optional

- [Polymarket](https://polymarket.com)
- [Discord Community](https://discord.gg/polymarket)
- [Twitter](https://x.com/polymarket)

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.polymarket.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Developer Quickstart

> Get started building with Polymarket APIs

Polymarket provides a suite of APIs and SDKs for building prediction market applications. This guide will help you understand what's available and where to find it.

***

## What Can You Build?

| If you want to...             | Start here                                                          |
| ----------------------------- | ------------------------------------------------------------------- |
| Fetch markets & prices        | [Fetching Market Data](/quickstart/fetching-data)                   |
| Place orders for yourself     | [Placing Your First Order](/quickstart/first-order)                 |
| Build a trading app for users | [Builders Program Introduction](/developers/builders/builder-intro) |
| Provide liquidity             | [Market Makers](/developers/market-makers/introduction)             |

***

## APIs at a Glance

### Markets & Data

<CardGroup cols={2}>
  <Card title="Gamma API" icon="database" href="/developers/gamma-markets-api/overview">
    **Market discovery & metadata**

    Fetch events, markets, categories, and resolution data. This is where you discover what's tradeable.

    `https://gamma-api.polymarket.com`
  </Card>

  <Card title="CLOB API" icon="book" href="/developers/CLOB/introduction">
    **Prices, orderbooks & trading**

    Get real-time prices, orderbook depth, and place orders. The core trading API.

    `https://clob.polymarket.com`
  </Card>

  <Card title="Data API" icon="chart-bar" href="/developers/misc-endpoints/data-api-get-positions">
    **Positions, activity & history**

    Query user positions, trade history, and portfolio data.

    `https://data-api.polymarket.com`
  </Card>

  <Card title="WebSocket" icon="bolt" href="/developers/CLOB/websocket/wss-overview">
    **Real-time updates**

    Subscribe to orderbook changes, price updates, and order status.

    `wss://ws-subscriptions-clob.polymarket.com`
  </Card>
</CardGroup>

### Additional Data Sources

<CardGroup cols={2}>
  <Card title="RTDS" icon="signal-stream" href="/developers/RTDS/RTDS-overview">
    **Low-latency data stream**

    Real-time crypto prices and comments. Optimized for market makers.
  </Card>

  <Card title="Subgraph" icon="diagram-project" href="/developers/subgraph/overview">
    **Onchain queries**

    Query blockchain state directly via GraphQL.
  </Card>
</CardGroup>

### Trading Infrastructure

<CardGroup cols={2}>
  <Card title="CTF Operations" icon="arrows-split-up-and-left" href="/developers/CTF/overview">
    **Token split/merge/redeem**

    Convert between USDC and outcome tokens. Essential for inventory management.
  </Card>

  <Card title="Relayer Client" icon="gas-pump" href="/developers/builders/relayer-client">
    **Gasless transactions**

    Builders can offer gasfree transactions via Polymarket's relayer.
  </Card>
</CardGroup>

***

## SDKs & Libraries

<CardGroup cols={2}>
  <Card title="CLOB Client (TypeScript)" icon="npm" href="https://github.com/Polymarket/clob-client">
    `npm install @polymarket/clob-client`
  </Card>

  <Card title="CLOB Client (Python)" icon="python" href="https://github.com/Polymarket/py-clob-client">
    `pip install py-clob-client`
  </Card>
</CardGroup>

For builders routing orders for users:

<CardGroup cols={2}>
  <Card title="Relayer Client" icon="bolt" href="https://github.com/Polymarket/builder-relayer-client">
    Gasless wallet operations
  </Card>

  <Card title="Signing SDK" icon="key" href="https://github.com/Polymarket/builder-signing-sdk">
    Builder authentication headers
  </Card>
</CardGroup>

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.polymarket.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Fetching Market Data

> Fetch Polymarket data in minutes with no authentication required

Get market data with zero setup. No API key, no authentication, no wallet required.

***

## Understanding the Data Model

Before fetching data, understand how Polymarket structures its markets:

<Steps>
  <Step title="Event">
    The top-level object representing a question like "Will X happen?"
  </Step>

  <Step title="Market">
    Each event contains one or more markets. Each market is a specific tradable binary outcome.
  </Step>

  <Step title="Outcomes & Prices">
    Markets have `outcomes` and `outcomePrices` arrays that map 1:1. These prices represent implied probabilities.
  </Step>
</Steps>

```json  theme={null}
{
  "outcomes": "[\"Yes\", \"No\"]",
  "outcomePrices": "[\"0.20\", \"0.80\"]"
}
// Index 0: "Yes" → 0.20 (20% probability)
// Index 1: "No" → 0.80 (80% probability)
```

***

## Fetch Active Events

List all currently active events on Polymarket:

```bash  theme={null}
curl "https://gamma-api.polymarket.com/events?active=true&closed=false&limit=5"
```

<Accordion title="Example Response">
  ```json  theme={null}
  [
    {
      "id": "123456",
      "slug": "will-bitcoin-reach-100k-by-2025",
      "title": "Will Bitcoin reach $100k by 2025?",
      "active": true,
      "closed": false,
      "tags": [
        { "id": "21", "label": "Crypto", "slug": "crypto" }
      ],
      "markets": [
        {
          "id": "789",
          "question": "Will Bitcoin reach $100k by 2025?",
          "clobTokenIds": ["TOKEN_YES_ID", "TOKEN_NO_ID"],
          "outcomes": "[\"Yes\", \"No\"]",
          "outcomePrices": "[\"0.65\", \"0.35\"]"
        }
      ]
    }
  ]
  ```
</Accordion>

<Tip>
  Always use `active=true&closed=false` to filter for live, tradable events.
</Tip>

***

## Market Discovery Best Practices

### For Sports Events

Use the `/sports` endpoint to discover leagues, then query by `series_id`:

```bash  theme={null}
# Get all supported sports leagues
curl "https://gamma-api.polymarket.com/sports"

# Get events for a specific league (e.g., NBA series_id=10345)
curl "https://gamma-api.polymarket.com/events?series_id=10345&active=true&closed=false"

# Filter to just game bets (not futures) using tag_id=100639
curl "https://gamma-api.polymarket.com/events?series_id=10345&tag_id=100639&active=true&closed=false&order=startTime&ascending=true"
```

<Note>
  `/sports` only returns automated leagues. For others (UFC, Boxing, F1, Golf, Chess), use tag IDs via `/events?tag_id=<tag_id>`.
</Note>

### For Non-Sports Topics

Use `/tags` to discover all available categories, then filter events:

```bash  theme={null}
# Get all available tags
curl "https://gamma-api.polymarket.com/tags?limit=100"

# Query events by topic
curl "https://gamma-api.polymarket.com/events?tag_id=2&active=true&closed=false"
```

<Tip>
  Each event response includes a `tags` array, useful for discovering categories from live data and building your own tag mapping.
</Tip>

***

## Get Market Details

Once you have an event, get details for a specific market using its ID or slug:

```bash  theme={null}
curl "https://gamma-api.polymarket.com/markets?slug=will-bitcoin-reach-100k-by-2025"
```

The response includes `clobTokenIds`, you'll need these to fetch prices and place orders.

***

## Get Current Price

Query the CLOB for the current price of any token:

```bash  theme={null}
curl "https://clob.polymarket.com/price?token_id=YOUR_TOKEN_ID&side=buy"
```

<Accordion title="Example Response">
  ```json  theme={null}
  {
    "price": "0.65"
  }
  ```
</Accordion>

***

## Get Orderbook Depth

See all bids and asks for a market:

```bash  theme={null}
curl "https://clob.polymarket.com/book?token_id=YOUR_TOKEN_ID"
```

<Accordion title="Example Response">
  ```json  theme={null}
  {
    "market": "0x...",
    "asset_id": "YOUR_TOKEN_ID",
    "bids": [
      { "price": "0.64", "size": "500" },
      { "price": "0.63", "size": "1200" }
    ],
    "asks": [
      { "price": "0.66", "size": "300" },
      { "price": "0.67", "size": "800" }
    ]
  }
  ```
</Accordion>

***

## More Data APIs

<CardGroup cols={2}>
  <Card title="Gamma API" icon="database" href="/developers/gamma-markets-api/overview">
    Deep dive into market discovery
  </Card>

  <Card title="Data API" icon="table" href="/developers/misc-endpoints/data-api-get-positions">
    Positions, activity, and holders data
  </Card>

  <Card title="WebSocket" icon="bolt" href="/developers/CLOB/websocket/wss-overview">
    Real-time orderbook updates
  </Card>

  <Card title="RTDS" icon="signal-stream" href="/developers/RTDS/RTDS-overview">
    Real-time data streaming service
  </Card>
</CardGroup>

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.polymarket.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Placing Your First Order

> Set up authentication and submit your first trade

This guide walks you through placing an order on Polymarket using your own wallet.

***

## Installation

<CodeGroup>
  ```bash TypeScript theme={null}
  npm install @polymarket/clob-client ethers@5
  ```

  ```bash Python theme={null}
  pip install py-clob-client
  ```
</CodeGroup>

***

## Step 1: Initialize Client with Private Key

<CodeGroup>
  ```typescript TypeScript theme={null}
  import { ClobClient } from "@polymarket/clob-client";
  import { Wallet } from "ethers"; // v5.8.0

  const HOST = "https://clob.polymarket.com";
  const CHAIN_ID = 137; // Polygon mainnet
  const signer = new Wallet(process.env.PRIVATE_KEY);

  const client = new ClobClient(HOST, CHAIN_ID, signer);
  ```

  ```python Python theme={null}
  from py_clob_client.client import ClobClient
  import os

  host = "https://clob.polymarket.com"
  chain_id = 137  # Polygon mainnet
  private_key = os.getenv("PRIVATE_KEY")

  client = ClobClient(host, key=private_key, chain_id=chain_id)
  ```
</CodeGroup>

***

## Step 2: Derive User API Credentials

Your private key is used once to derive API credentials. These credentials authenticate all subsequent requests.

<CodeGroup>
  ```typescript TypeScript theme={null}
  // Get existing API key, or create one if none exists
  const userApiCreds = await client.createOrDeriveApiKey();

  console.log("API Key:", userApiCreds.apiKey);
  console.log("Secret:", userApiCreds.secret);
  console.log("Passphrase:", userApiCreds.passphrase);
  ```

  ```python Python theme={null}
  # Get existing API key, or create one if none exists
  user_api_creds = client.create_or_derive_api_creds()

  print("API Key:", user_api_creds["apiKey"])
  print("Secret:", user_api_creds["secret"])
  print("Passphrase:", user_api_creds["passphrase"])
  ```
</CodeGroup>

***

## Step 3: Configure Signature Type and Funder

Before reinitializing the client, determine your **signature type** and **funder address**:

| How do you want to trade?                                                                 | Type         | Value | Funder Address            |
| ----------------------------------------------------------------------------------------- | ------------ | ----- | ------------------------- |
| I want to use an EOA wallet. It holds USDCe and position tokens, and I'll pay my own gas. | EOA          | `0`   | Your EOA wallet address   |
| I want to trade through my Polymarket.com account (Magic Link email/Google login).        | POLY\_PROXY  | `1`   | Your proxy wallet address |
| I want to trade through my Polymarket.com account (browser wallet connection).            | GNOSIS\_SAFE | `2`   | Your proxy wallet address |

<Note>
  If you have a Polymarket.com account, your funds are in a proxy wallet (visible in the profile dropdown). Use type 1 or 2. Type 0 is for standalone EOA wallets only.
</Note>

***

## Step 4: Reinitialize with Full Authentication

<CodeGroup>
  ```typescript TypeScript theme={null}
  // Choose based on your wallet type (see table above)
  const SIGNATURE_TYPE = 0; // EOA example
  const FUNDER_ADDRESS = signer.address; // For EOA, funder is your wallet

  const client = new ClobClient(
    HOST,
    CHAIN_ID,
    signer,
    userApiCreds,
    SIGNATURE_TYPE,
    FUNDER_ADDRESS
  );
  ```

  ```python Python theme={null}
  # Choose based on your wallet type (see table above)
  signature_type = 0  # EOA example
  funder_address = "YOUR_WALLET_ADDRESS"  # For EOA, funder is your wallet

  client = ClobClient(
      host,
      key=private_key,
      chain_id=chain_id,
      creds=user_api_creds,
      signature_type=signature_type,
      funder=funder_address
  )
  ```
</CodeGroup>

<Warning>
  **Do not use Builder API credentials in place of User API credentials!** Builder credentials are for order attribution, not user authentication. See [Builder Order Attribution](/developers/builders/order-attribution).
</Warning>

***

## Step 5: Place an Order

Now you're ready to trade! First, get a token ID from the [Gamma API](/developers/gamma-markets-api/get-markets).

<CodeGroup>
  ```typescript TypeScript theme={null}
  import { Side, OrderType } from "@polymarket/clob-client";

  // Get market info first
  const market = await client.getMarket("TOKEN_ID");

  const response = await client.createAndPostOrder(
    {
      tokenID: "TOKEN_ID",
      price: 0.50,        // Price per share ($0.50)
      size: 10,           // Number of shares
      side: Side.BUY,     // BUY or SELL
    },
    {
      tickSize: market.tickSize,
      negRisk: market.negRisk,    // true for multi-outcome events
    },
    OrderType.GTC  // Good-Til-Cancelled
  );

  console.log("Order ID:", response.orderID);
  console.log("Status:", response.status);
  ```

  ```python Python theme={null}
  from py_clob_client.clob_types import OrderArgs, OrderType
  from py_clob_client.order_builder.constants import BUY

  # Get market info first
  market = client.get_market("TOKEN_ID")

  response = client.create_and_post_order(
      OrderArgs(
          token_id="TOKEN_ID",
          price=0.50,       # Price per share ($0.50)
          size=10,          # Number of shares
          side=BUY,         # BUY or SELL
      ),
      options={
          "tick_size": market["tickSize"],
          "neg_risk": market["negRisk"],    # True for multi-outcome events
      },
      order_type=OrderType.GTC  # Good-Til-Cancelled
  )

  print("Order ID:", response["orderID"])
  print("Status:", response["status"])
  ```
</CodeGroup>

***

## Step 6: Check Your Orders

<CodeGroup>
  ```typescript TypeScript theme={null}
  // View all open orders
  const openOrders = await client.getOpenOrders();
  console.log(`You have ${openOrders.length} open orders`);

  // View your trade history
  const trades = await client.getTrades();
  console.log(`You've made ${trades.length} trades`);

  // Cancel an order
  await client.cancelOrder(response.orderID);
  ```

  ```python Python theme={null}
  # View all open orders
  open_orders = trading_client.get_open_orders()
  print(f"You have {len(open_orders)} open orders")

  # View your trade history
  trades = trading_client.get_trades()
  print(f"You've made {len(trades)} trades")

  # Cancel an order
  trading_client.cancel_order(response["orderID"])
  ```
</CodeGroup>

***

## Troubleshooting

<AccordionGroup>
  <Accordion title="Invalid Signature / L2 Auth Not Available">
    Wrong private key, signature type, or funder address for the derived User API credentials.

    Double check the following values when creating User API credentials via `createOrDeriveApiKey()`:

    * Do not use Builder API credentials in place of User API credentials
    * Check `signatureType` matches your account type (0, 1, or 2)
    * Ensure `funder` is correct for your wallet type
  </Accordion>

  <Accordion title="Unauthorized / Invalid API Key">
    Wrong API key, secret, or passphrase.

    Re-derive credentials with `createOrDeriveApiKey()` and update your config.
  </Accordion>

  <Accordion title="Not Enough Balance / Allowance">
    Either not enough USDCe / position tokens in your funder address, or you lack approvals to spend your tokens.

    * Deposit USDCe to your funder address.
    * Ensure you have more USDCe than what's committed in open orders.
    * Check that you've set all necessary token approvals.
  </Accordion>

  <Accordion title="Blocked by Cloudflare / Geoblock">
    You're trying to place a trade from a restricted region.

    See [Geographic Restrictions](/developers/CLOB/geoblock) for details.
  </Accordion>
</AccordionGroup>

***

## Adding Builder API Credentials

If you're building an app that routes orders for your users, you can add builder credentials to get attribution on the [Builder Leaderboard](https://builders.polymarket.com/):

```typescript TypeScript theme={null}
import { BuilderConfig, BuilderApiKeyCreds } from "@polymarket/builder-signing-sdk";

const builderCreds: BuilderApiKeyCreds = {
  key: process.env.POLY_BUILDER_API_KEY!,
  secret: process.env.POLY_BUILDER_SECRET!,
  passphrase: process.env.POLY_BUILDER_PASSPHRASE!,
};

const builderConfig = new BuilderConfig({ localBuilderCreds: builderCreds });

// Add builderConfig as the last parameter
const client = new ClobClient(
  HOST, 
  CHAIN_ID, 
  signer, 
  userApiCreds, 
  signatureType, 
  funderAddress,
  undefined, 
  false, 
  builderConfig
);
```

<Info>
  Builder credentials are **separate** from user credentials. You use your builder
  credentials to tag orders, but each user still needs their own L2 credentials to trade.
</Info>

<Card title="Full Builder Guide" icon="hammer" href="/developers/builders/order-attribution">
  Complete documentation for order attribution and gasless transactions
</Card>

Skip to main content
Polymarket Documentation home pagedark logo

Search...
Ctrl K

Ask AI
Main Site

User Guide
For Developers
Changelog
Polymarket
Discord Community
Twitter
Developer Quickstart
Developer Quickstart
Fetching Market Data
Placing Your First Order
Glossary
API Rate Limits
Endpoints
Market Makers
Market Maker Introduction
Setup
Trading
Liquidity Rewards
Maker Rebates Program
Data Feeds
Inventory Management
Polymarket Builders Program
Builder Program Introduction
Builder Tiers
Builder Profile & Keys
Order Attribution
Relayer Client
Examples
Central Limit Order Book
CLOB Introduction
Status
Quickstart
Authentication
Geographic Restrictions

Client

REST API

Historical Timeseries Data

Order Management

Trades
Websocket
WSS Overview
WSS Quickstart
WSS Authentication
User Channel
Market Channel

Sports Websocket
Real Time Data Stream
RTDS Overview
RTDS Crypto Prices
RTDS Comments
Gamma Structure
Overview
Gamma Structure
Fetching Markets
Gamma Endpoints

Gamma Status

Sports

Tags

Events

Markets

Series

Comments

Profiles

Search
Data-API

Data API Status

Core

Misc

Builders
Bridge & Swap
Overview

Bridge
Subgraph
Overview
Resolution
Resolution
Conditional Token Frameworks
Overview
Splitting USDC
Merging Tokens
Reedeeming Tokens
Deployment and Additional Information
Proxy Wallets
Proxy wallet
Negative Risk
Overview

On this page
Markets & Events
Trading
Order Types
Market Types
Wallets
Token Operations (CTF)
Infrastructure
Developer Quickstart
Glossary
Key terms and concepts for Polymarket developers

​
Markets & Events
Term	Definition
Event	A collection of related markets grouped under a common topic. Example: “2024 US Presidential Election” contains markets for each candidate.
Market	A single tradeable outcome within an event. Each market has a Yes and No side. Corresponds to a condition ID, question ID, and pair of token IDs.
Token	Represents a position in a specific outcome (Yes or No). Prices range from 0.00 to 1.00. Winning tokens redeem for $1 USDCe. Also called outcome token or referenced by token ID.
Token ID	The unique identifier for a specific outcome token. Required when placing orders or querying prices.
Condition ID	Onchain identifier for a market’s resolution condition. Used in CTF operations.
Question ID	Identifier linking a market to its resolution oracle (UMA).
Slug	Human-readable URL identifier for a market or event. Found in Polymarket URLs: polymarket.com/event/[slug]
​
Trading
Term	Definition
CLOB	Central Limit Order Book. Polymarket’s off-chain order matching system. Orders are matched here before onchain settlement.
Tick Size	The minimum price increment for a market. Usually 0.01 (1 cent) or 0.001 (0.1 cent).
Fill	When an order is matched and executed. Orders can be partially or fully filled.
​
Order Types
Term	Definition
GTC	Good-Til-Cancelled. An order that remains open until filled or manually cancelled.
GTD	Good-Til-Date. An order that expires at a specified time if not filled.
FOK	Fill-Or-Kill. An order that must be filled entirely and immediately, or it’s cancelled. No partial fills.
FAK	Fill-And-Kill. An order that fills as much as possible immediately, then cancels any remaining unfilled portion.
​
Market Types
Term	Definition
Binary Market	A market with exactly two outcomes: Yes and No. The prices always sum to approximately $1.
Negative Risk (NegRisk)	A multi-outcome event where only one outcome can resolve Yes. Requires negRisk: true in order parameters. Details
​
Wallets
Term	Definition
EOA	Externally Owned Account. A standard Ethereum wallet controlled by a private key.
Funder Address	The wallet address that holds funds and tokens for trading.
Signature Type	Identifies wallet type when trading. 0 = EOA, 1 = Magic Link proxy, 2 = Gnosis Safe proxy.
​
Token Operations (CTF)
Term	Definition
CTF	Conditional Token Framework. The onchain smart contracts that manage outcome tokens.
Split	Convert USDCe into a complete set of outcome tokens (one Yes + one No).
Merge	Convert a complete set of outcome tokens back into USDCe.
Redeem	After resolution, exchange winning tokens for $1 USDCe each.
​
Infrastructure
Term	Definition
Polygon	The blockchain network where Polymarket operates. Chain ID: 137.
USDCe	The stablecoin used as collateral on Polymarket. Bridged USDC on Polygon.
Placing Your First Order
API Rate Limits
Ask a question...

github
Powered by
Glossary - Polymarket Documentation

Skip to main content
Polymarket Documentation home pagedark logo

Search...
Ctrl K

Ask AI
Main Site

User Guide
For Developers
Changelog
Polymarket
Discord Community
Twitter
Developer Quickstart
Developer Quickstart
Fetching Market Data
Placing Your First Order
Glossary
API Rate Limits
Endpoints
Market Makers
Market Maker Introduction
Setup
Trading
Liquidity Rewards
Maker Rebates Program
Data Feeds
Inventory Management
Polymarket Builders Program
Builder Program Introduction
Builder Tiers
Builder Profile & Keys
Order Attribution
Relayer Client
Examples
Central Limit Order Book
CLOB Introduction
Status
Quickstart
Authentication
Geographic Restrictions

Client

REST API

Historical Timeseries Data

Order Management

Trades
Websocket
WSS Overview
WSS Quickstart
WSS Authentication
User Channel
Market Channel

Sports Websocket
Real Time Data Stream
RTDS Overview
RTDS Crypto Prices
RTDS Comments
Gamma Structure
Overview
Gamma Structure
Fetching Markets
Gamma Endpoints

Gamma Status

Sports

Tags

Events

Markets

Series

Comments

Profiles

Search
Data-API

Data API Status

Core

Misc

Builders
Bridge & Swap
Overview

Bridge
Subgraph
Overview
Resolution
Resolution
Conditional Token Frameworks
Overview
Splitting USDC
Merging Tokens
Reedeeming Tokens
Deployment and Additional Information
Proxy Wallets
Proxy wallet
Negative Risk
Overview

On this page
How Rate Limiting Works
General Rate Limits
Data API Rate Limits
GAMMA API Rate Limits
CLOB API Rate Limits
General CLOB Endpoints
CLOB Market Data
CLOB Ledger Endpoints
CLOB Markets & Pricing
CLOB Authentication
CLOB Trading Endpoints
Other API Rate Limits
Developer Quickstart
API Rate Limits
​
How Rate Limiting Works
All rate limits are enforced using Cloudflare’s throttling system. When you exceed the maximum configured rate for any endpoint, requests are throttled rather than immediately rejected. This means:
Throttling: Requests over the limit are delayed/queued rather than dropped
Burst Allowances: Some endpoints allow short bursts above the sustained rate
Time Windows: Limits reset based on sliding time windows (e.g., per 10 seconds, per minute)
​
General Rate Limits
Endpoint	Limit	Notes
General Rate Limiting	15000 requests / 10s	Throttle requests over the maximum configured rate
”OK” Endpoint	100 requests / 10s	Throttle requests over the maximum configured rate
​
Data API Rate Limits
Endpoint	Limit	Notes
Data API (General)	1000 requests / 10s	Throttle requests over the maximum configured rate
Data API /trades	200 requests / 10s	Throttle requests over the maximum configured rate
Data API /positions	150 requests / 10s	Throttle requests over the maximum configured rate
Data API /closed-positions	150 requests / 10s	Throttle requests over the maximum configured rate
Data API “OK” Endpoint	100 requests / 10s	Throttle requests over the maximum configured rate
​
GAMMA API Rate Limits
Endpoint	Limit	Notes
GAMMA (General)	4000 requests / 10s	Throttle requests over the maximum configured rate
GAMMA Get Comments	200 requests / 10s	Throttle requests over the maximum configured rate
GAMMA /events	500 requests / 10s	Throttle requests over the maximum configured rate
GAMMA /markets	300 requests / 10s	Throttle requests over the maximum configured rate
GAMMA /markets /events listing	900 requests / 10s	Throttle requests over the maximum configured rate
GAMMA Tags	200 requests / 10s	Throttle requests over the maximum configured rate
GAMMA Search	350 requests / 10s	Throttle requests over the maximum configured rate
​
CLOB API Rate Limits
​
General CLOB Endpoints
Endpoint	Limit	Notes
CLOB (General)	9000 requests / 10s	Throttle requests over the maximum configured rate
CLOB GET Balance Allowance	200 requests / 10s	Throttle requests over the maximum configured rate
CLOB UPDATE Balance Allowance	50 requests / 10s	Throttle requests over the maximum configured rate
​
CLOB Market Data
Endpoint	Limit	Notes
CLOB /book	1500 requests / 10s	Throttle requests over the maximum configured rate
CLOB /books	500 requests / 10s	Throttle requests over the maximum configured rate
CLOB /price	1500 requests / 10s	Throttle requests over the maximum configured rate
CLOB /prices	500 requests / 10s	Throttle requests over the maximum configured rate
CLOB /midprice	1500 requests / 10s	Throttle requests over the maximum configured rate
CLOB /midprices	500 requests / 10s	Throttle requests over the maximum configured rate
​
CLOB Ledger Endpoints
Endpoint	Limit	Notes
CLOB Ledger (/trades /orders /notifications /order)	900 requests / 10s	Throttle requests over the maximum configured rate
CLOB Ledger /data/orders	500 requests / 10s	Throttle requests over the maximum configured rate
CLOB Ledger /data/trades	500 requests / 10s	Throttle requests over the maximum configured rate
CLOB /notifications	125 requests / 10s	Throttle requests over the maximum configured rate
​
CLOB Markets & Pricing
Endpoint	Limit	Notes
CLOB Price History	1000 requests / 10s	Throttle requests over the maximum configured rate
CLOB Market Tick Size	200 requests / 10s	Throttle requests over the maximum configured rate
​
CLOB Authentication
Endpoint	Limit	Notes
CLOB API Keys	100 requests / 10s	Throttle requests over the maximum configured rate
​
CLOB Trading Endpoints
Endpoint	Limit	Notes
CLOB POST /order	3500 requests / 10s (500/s)	BURST - Throttle requests over the maximum configured rate
CLOB POST /order	36000 requests / 10 minutes (60/s)	Throttle requests over the maximum configured rate
CLOB DELETE /order	3000 requests / 10s (300/s)	BURST - Throttle requests over the maximum configured rate
CLOB DELETE /order	30000 requests / 10 minutes (50/s)	Throttle requests over the maximum configured rate
CLOB POST /orders	1000 requests / 10s (100/s)	BURST - Throttle requests over the maximum configured rate
CLOB POST /orders	15000 requests / 10 minutes (25/s)	Throttle requests over the maximum configured rate
CLOB DELETE /orders	1000 requests / 10s (100/s)	BURST - Throttle requests over the maximum configured rate
CLOB DELETE /orders	15000 requests / 10 minutes (25/s)	Throttle requests over the maximum configured rate
CLOB DELETE /cancel-all	250 requests / 10s (25/s)	BURST - Throttle requests over the maximum configured rate
CLOB DELETE /cancel-all	6000 requests / 10 minutes (10/s)	Throttle requests over the maximum configured rate
CLOB DELETE /cancel-market-orders	1000 requests / 10s (100/s)	BURST - Throttle requests over the maximum configured rate
CLOB DELETE /cancel-market-orders	1500 requests / 10 minutes (25/s)	Throttle requests over the maximum configured rate
​
Other API Rate Limits
Endpoint	Limit	Notes
RELAYER /submit	25 requests / 1 minute	Throttle requests over the maximum configured rate
User PNL API	200 requests / 10s	Throttle requests over the maximum configured rate
Glossary
Endpoints
Ask a question...

github
Powered by
API Rate Limits - Polymarket Documentation

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.polymarket.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Endpoints

> All Polymarket API URLs and base endpoints

All base URLs for Polymarket APIs. See individual API documentation for available routes and parameters.

***

## REST APIs

| API           | Base URL                           | Description                          |
| ------------- | ---------------------------------- | ------------------------------------ |
| **CLOB API**  | `https://clob.polymarket.com`      | Order management, prices, orderbooks |
| **Gamma API** | `https://gamma-api.polymarket.com` | Market discovery, metadata, events   |
| **Data API**  | `https://data-api.polymarket.com`  | User positions, activity, history    |

***

## WebSocket Endpoints

| Service            | URL                                              | Description                         |
| ------------------ | ------------------------------------------------ | ----------------------------------- |
| **CLOB WebSocket** | `wss://ws-subscriptions-clob.polymarket.com/ws/` | Orderbook updates, order status     |
| **RTDS**           | `wss://ws-live-data.polymarket.com`              | Low-latency crypto prices, comments |

***

## Quick Reference

### CLOB API

```
https://clob.polymarket.com
```

Common endpoints:

* `GET /price` — Get current price for a token
* `GET /book` — Get orderbook for a token
* `GET /midpoint` — Get midpoint price
* `POST /order` — Place an order (auth required)
* `DELETE /order` — Cancel an order (auth required)

[Full CLOB documentation →](/developers/CLOB/introduction)

### Gamma API

```
https://gamma-api.polymarket.com
```

Common endpoints:

* `GET /events` — List events
* `GET /markets` — List markets
* `GET /events/{id}` — Get event details

[Full Gamma documentation →](/developers/gamma-markets-api/overview)

### Data API

```
https://data-api.polymarket.com
```

Common endpoints:

* `GET /positions` — Get user positions
* `GET /activity` — Get user activity
* `GET /trades` — Get trade history

[Full Data API documentation →](/developers/misc-endpoints/data-api-get-positions)

### CLOB WebSocket

```
wss://ws-subscriptions-clob.polymarket.com/ws/
```

Channels:

* `market` — Orderbook and price updates (public)
* `user` — Order status updates (authenticated)

[Full WebSocket documentation →](/developers/CLOB/websocket/wss-overview)

### RTDS (Real-Time Data Stream)

```
wss://ws-live-data.polymarket.com
```

Channels:

* Crypto price feeds
* Comment streams

[Full RTDS documentation →](/developers/RTDS/RTDS-overview)

Skip to main content
Polymarket Documentation home pagedark logo

Search...
Ctrl K

Ask AI
Main Site

User Guide
For Developers
Changelog
Polymarket
Discord Community
Twitter
Developer Quickstart
Developer Quickstart
Fetching Market Data
Placing Your First Order
Glossary
API Rate Limits
Endpoints
Market Makers
Market Maker Introduction
Setup
Trading
Liquidity Rewards
Maker Rebates Program
Data Feeds
Inventory Management
Polymarket Builders Program
Builder Program Introduction
Builder Tiers
Builder Profile & Keys
Order Attribution
Relayer Client
Examples
Central Limit Order Book
CLOB Introduction
Status
Quickstart
Authentication
Geographic Restrictions

Client

REST API

Historical Timeseries Data

Order Management

Trades
Websocket
WSS Overview
WSS Quickstart
WSS Authentication
User Channel
Market Channel

Sports Websocket
Real Time Data Stream
RTDS Overview
RTDS Crypto Prices
RTDS Comments
Gamma Structure
Overview
Gamma Structure
Fetching Markets
Gamma Endpoints

Gamma Status

Sports

Tags

Events

Markets

Series

Comments

Profiles

Search
Data-API

Data API Status

Core

Misc

Builders
Bridge & Swap
Overview

Bridge
Subgraph
Overview
Resolution
Resolution
Conditional Token Frameworks
Overview
Splitting USDC
Merging Tokens
Reedeeming Tokens
Deployment and Additional Information
Proxy Wallets
Proxy wallet
Negative Risk
Overview

On this page
What is a Market Maker?
Getting Started
Available Tools
By Action Type
Quick Reference
Support
Market Makers
Market Maker Introduction
Overview of market making on Polymarket and available tools for liquidity providers

​
What is a Market Maker?
A Market Maker (MM) on Polymarket is a sophisticated trader who provides liquidity to prediction markets by continuously posting bid and ask orders. By “laying the spread,” market makers enable other users to trade efficiently while earning the spread as compensation for the risk they take.
Market makers are essential to Polymarket’s ecosystem:
Provide liquidity across all markets
Tighten spreads for better user experience
Enable price discovery through continuous quoting
Absorb trading flow from retail and institutional users
Not a Market Maker? If you’re building an application that routes orders for your users, see the Builders Program instead. Builders get access to gasless transactions via the Relayer Client and can earn grants through order attribution.
​
Getting Started
To become a market maker on Polymarket:
Complete setup - Deploy wallets, fund with USDCe, set token approvals
Connect to data feeds - WebSocket for orderbook, RTDS for low-latency data
Start quoting - Post orders via CLOB REST API
​
Available Tools
​
By Action Type
Setup
Deposits, token approvals, wallet deployment, API keys
Trading
CLOB order entry, order types, quoting best practices
Data Feeds
WebSocket, RTDS, Gamma API, on-chain data
Inventory Management
Split, merge, and redeem outcome tokens
Liquidity Rewards
Earn rewards for providing liquidity
Maker Rebates Program
Earn rebates for providing liquidity
​
Quick Reference
Action	Tool	Documentation
Deposit USDCe	Bridge API	Bridge Overview
Approve tokens	Relayer Client	Setup Guide
Post limit orders	CLOB REST API	CLOB Client
Monitor orderbook	WebSocket	WebSocket Overview
Low-latency data	RTDS	Data Feeds
Split USDCe to tokens	CTF / Relayer	Inventory
Merge tokens to USDCe	CTF / Relayer	Inventory
​
Support
For market maker onboarding and support, contact support@polymarket.com.
Endpoints
Setup
Ask a question...

github
Powered by
Market Maker Introduction - Polymarket Documentation

Skip to main content
Polymarket Documentation home pagedark logo

Search...
Ctrl K

Ask AI
Main Site

User Guide
For Developers
Changelog
Polymarket
Discord Community
Twitter
Developer Quickstart
Developer Quickstart
Fetching Market Data
Placing Your First Order
Glossary
API Rate Limits
Endpoints
Market Makers
Market Maker Introduction
Setup
Trading
Liquidity Rewards
Maker Rebates Program
Data Feeds
Inventory Management
Polymarket Builders Program
Builder Program Introduction
Builder Tiers
Builder Profile & Keys
Order Attribution
Relayer Client
Examples
Central Limit Order Book
CLOB Introduction
Status
Quickstart
Authentication
Geographic Restrictions

Client

REST API

Historical Timeseries Data

Order Management

Trades
Websocket
WSS Overview
WSS Quickstart
WSS Authentication
User Channel
Market Channel

Sports Websocket
Real Time Data Stream
RTDS Overview
RTDS Crypto Prices
RTDS Comments
Gamma Structure
Overview
Gamma Structure
Fetching Markets
Gamma Endpoints

Gamma Status

Sports

Tags

Events

Markets

Series

Comments

Profiles

Search
Data-API

Data API Status

Core

Misc

Builders
Bridge & Swap
Overview

Bridge
Subgraph
Overview
Resolution
Resolution
Conditional Token Frameworks
Overview
Splitting USDC
Merging Tokens
Reedeeming Tokens
Deployment and Additional Information
Proxy Wallets
Proxy wallet
Negative Risk
Overview

On this page
Overview
Deposit USDCe
Options
Using the Bridge API
Wallet Options
EOA (Externally Owned Account)
Safe Wallet (Recommended)
Token Approvals
Required Approvals
Contract Addresses (Polygon Mainnet)
Approve via Relayer Client
API Key Generation
Generate API Key
Using Credentials
Next Steps
Market Makers
Setup
One-time setup for market making on Polymarket: deposits, approvals, wallets, and API keys

​
Overview
Before you can start market making on Polymarket, you need to complete these one-time setup steps:
Deposit bridged USDCe to Polygon
Deploy a wallet (EOA or Safe)
Approve tokens for trading
Generate API credentials
​
Deposit USDCe
Market makers need USDCe on Polygon to fund their trading operations.
​
Options
Method	Best For	Documentation
Bridge API	Automated deposits from other chains	Bridge Overview
Direct Polygon transfer	Already have USDCe on Polygon	N/A
Cross-chain bridge	Large deposits from Ethereum	Large Deposits
​
Using the Bridge API
// Deposit USDCe from Ethereum to Polygon
const deposit = await fetch("https://clob.polymarket.com/deposit", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    chainId: "1",
    fromChain: "ethereum",
    toChain: "polygon",
    asset: "USDCe",
    amount: "100000000000" // $100,000 in USDCe (6 decimals)
  })
});
See Bridge Deposit for full API details.
​
Wallet Options
​
EOA (Externally Owned Account)
Standard Ethereum wallet. You pay for all onchain transactions (approvals, splits, merges, trade exedcution).
​
Safe Wallet (Recommended)
Gnosis Safe-based wallet deployed via Polymarket’s relayer. Benefits:
Gasless transactions - Polymarket pays gas fees for onchain operations
Contract wallet - Enables advanced features like batched transactions.
Deploy a Safe wallet using the Relayer Client:
import { RelayClient, RelayerTxType } from "@polymarket/builder-relayer-client";

const client = new RelayClient(
  "https://relayer-v2.polymarket.com/",
  137, // Polygon mainnet
  signer,
  builderConfig,
  RelayerTxType.SAFE
);

// Deploy the Safe wallet
const response = await client.deploy();
const result = await response.wait();
console.log("Safe Address:", result?.proxyAddress);
​
Token Approvals
Before trading, you must approve the exchange contracts to spend your tokens.
​
Required Approvals
Token	Spender	Purpose
USDCe	CTF Contract	Split USDCe into outcome tokens
CTF (outcome tokens)	CTF Exchange	Trade outcome tokens
CTF (outcome tokens)	Neg Risk CTF Exchange	Trade neg-risk market tokens
​
Contract Addresses (Polygon Mainnet)
const ADDRESSES = {
  USDCe: "0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174",
  CTF: "0x4d97dcd97ec945f40cf65f87097ace5ea0476045",
  CTF_EXCHANGE: "0x4bFb41d5B3570DeFd03C39a9A4D8dE6Bd8B8982E",
  NEG_RISK_CTF_EXCHANGE: "0xC5d563A36AE78145C45a50134d48A1215220f80a",
  NEG_RISK_ADAPTER: "0xd91E80cF2E7be2e162c6513ceD06f1dD0dA35296"
};
​
Approve via Relayer Client
import { ethers } from "ethers";
import { Interface } from "ethers/lib/utils";

const erc20Interface = new Interface([
  "function approve(address spender, uint256 amount) returns (bool)"
]);

// Approve USDCe for CTF contract
const approveTx = {
  to: ADDRESSES.USDCe,
  data: erc20Interface.encodeFunctionData("approve", [
    ADDRESSES.CTF,
    ethers.constants.MaxUint256
  ]),
  value: "0"
};

const response = await client.execute([approveTx], "Approve USDCe for CTF");
await response.wait();
See Relayer Client for complete examples.
​
API Key Generation
To place orders and access authenticated endpoints, you need L2 API credentials.
​
Generate API Key
import { ClobClient } from "@polymarket/clob-client";

const client = new ClobClient(
  "https://clob.polymarket.com",
  137,
  signer
);

// Derive API credentials from your wallet
const credentials = await client.deriveApiKey();
console.log("API Key:", credentials.key);
console.log("Secret:", credentials.secret);
console.log("Passphrase:", credentials.passphrase);
​
Using Credentials
Once you have credentials, initialize the client for authenticated operations:
const client = new ClobClient(
  "https://clob.polymarket.com",
  137,
  wallet,
  credentials
);
See CLOB Authentication for full details.
​
Next Steps
Once setup is complete:
Start Trading
Post limit orders and manage quotes
Market Maker Introduction
Trading
Ask a question...

github
Powered by
Setup - Polymarket Documentation

Skip to main content
Polymarket Documentation home pagedark logo

Search...
Ctrl K

Ask AI
Main Site

User Guide
For Developers
Changelog
Polymarket
Discord Community
Twitter
Developer Quickstart
Developer Quickstart
Fetching Market Data
Placing Your First Order
Glossary
API Rate Limits
Endpoints
Market Makers
Market Maker Introduction
Setup
Trading
Liquidity Rewards
Maker Rebates Program
Data Feeds
Inventory Management
Polymarket Builders Program
Builder Program Introduction
Builder Tiers
Builder Profile & Keys
Order Attribution
Relayer Client
Examples
Central Limit Order Book
CLOB Introduction
Status
Quickstart
Authentication
Geographic Restrictions

Client

REST API

Historical Timeseries Data

Order Management

Trades
Websocket
WSS Overview
WSS Quickstart
WSS Authentication
User Channel
Market Channel

Sports Websocket
Real Time Data Stream
RTDS Overview
RTDS Crypto Prices
RTDS Comments
Gamma Structure
Overview
Gamma Structure
Fetching Markets
Gamma Endpoints

Gamma Status

Sports

Tags

Events

Markets

Series

Comments

Profiles

Search
Data-API

Data API Status

Core

Misc

Builders
Bridge & Swap
Overview

Bridge
Subgraph
Overview
Resolution
Resolution
Conditional Token Frameworks
Overview
Splitting USDC
Merging Tokens
Reedeeming Tokens
Deployment and Additional Information
Proxy Wallets
Proxy wallet
Negative Risk
Overview

On this page
Overview
Order Entry
Posting Limit Orders
Batch Orders
Order Types
When to Use Each
Order Management
Cancel Orders
Get Active Orders
Best Practices
Quote Management
Latency Optimization
Risk Management
Tick Sizes
Fee Structure
Related Documentation
Market Makers
Trading
CLOB order entry and management for market makers

​
Overview
Market makers primarily interact with Polymarket through the CLOB (Central Limit Order Book) API to post and manage limit orders.
​
Order Entry
​
Posting Limit Orders
Use the CLOB client to create and post limit orders:
import { ClobClient, Side, OrderType } from "@polymarket/clob-client";

const client = new ClobClient(
  "https://clob.polymarket.com",
  137,
  wallet,
  credentials,
  signatureType,
  funder
);

// Post a bid (buy order)
const bidOrder = await client.createAndPostOrder({
  tokenID: "34097058504275310827233323421517291090691602969494795225921954353603704046623",
  side: Side.BUY,
  price: 0.48,
  size: 1000,
  orderType: OrderType.GTC
});

// Post an ask (sell order)
const askOrder = await client.createAndPostOrder({
  tokenID: "34097058504275310827233323421517291090691602969494795225921954353603704046623",
  side: Side.SELL,
  price: 0.52,
  size: 1000,
  orderType: OrderType.GTC
});
See Create Order for full documentation.
​
Batch Orders
For efficiency, post multiple orders in a single request:
const orders = await Promise.all([
  client.createOrder({ tokenID, side: Side.BUY, price: 0.48, size: 500 }),
  client.createOrder({ tokenID, side: Side.BUY, price: 0.47, size: 500 }),
  client.createOrder({ tokenID, side: Side.SELL, price: 0.52, size: 500 }),
  client.createOrder({ tokenID, side: Side.SELL, price: 0.53, size: 500 })
]);

const response = await client.postOrders(
  orders.map(order => ({ order, orderType: OrderType.GTC }))
);
See Post Orders Batch for details.
​
Order Types
Type	Behavior	MM Use Case
GTC (Good Till Cancelled)	Rests on book until filled or cancelled	Default for passive quoting
GTD (Good Till Date)	Auto-expires at specified time	Auto-expire before events
FOK (Fill or Kill)	Fill entirely immediately or cancel	Aggressive rebalancing (all or nothing)
FAK (Fill and Kill)	Fill available immediately, cancel rest	Partial rebalancing acceptable
​
When to Use Each
For passive market making (maker orders):
GTC - Standard quotes that sit on the book
GTD - Time-limited quotes (e.g., expire before market close)
For rebalancing (taker orders):
FOK - When you need exact size or nothing
FAK - When partial fills are acceptable
// GTD example: expire in 1 hour
const expiringOrder = await client.createOrder({
  tokenID,
  side: Side.BUY,
  price: 0.50,
  size: 1000,
  orderType: OrderType.GTD,
  expiration: Math.floor(Date.now() / 1000) + 3600 // 1 hour from now
});
​
Order Management
​
Cancel Orders
Cancel individual orders or all orders:
// Cancel single order
await client.cancelOrder(orderId);

// Cancel multiple orders in a single calls
await client.cancelOrders(orderIds: string[]);

// Cancel all orders for a market
await client.cancelMarketOrders(conditionId);

// Cancel all orders
await client.cancelAll();
See Cancel Orders for full documentation.
​
Get Active Orders
Monitor your open orders:
// Get active order
const order = await client.getOrder(orderId);

// Get active orders optionally filtered
const orders = await client.getOpenOrders({
  id?: string; // Order ID (hash)
  market?: string; // Market condition ID
  asset_id?: string; // Token ID
});
See Get Active Orders for details.
​
Best Practices
​
Quote Management
Two-sided quoting - Post both bids and asks to earn maximum liquidity rewards
Monitor inventory - Skew quotes based on your position
Cancel stale quotes - Remove orders when market conditions change
Use GTD for events - Auto-expire quotes before known events
​
Latency Optimization
Batch orders - Use postOrders() instead of multiple createAndPostOrder() calls
WebSocket for data - Use WebSocket feeds instead of polling REST endpoints
​
Risk Management
Size limits - Check token balances before quoting; don’t exceed inventory
Price guards - Validate against book midpoint; reject outlier prices
Kill switch - Use cancelAll() on error or position breach
Monitor fills - Subscribe to WebSocket user channel for real-time fill updates
​
Tick Sizes
Markets have different minimum price increments:
const tickSize = await client.getTickSize(tokenID);
// Returns: "0.1" | "0.01" | "0.001" | "0.0001"
Ensure your prices conform to the market’s tick size.
​
Fee Structure
Role	Fee
Maker	0 bps
Taker	0 bps
Current fees are 0% for both makers and takers. See CLOB Introduction for fee calculation details.
​
Related Documentation
CLOB Client Overview
Complete client method reference
L2 Methods
Authenticated order management methods
WebSocket Feeds
Real-time order and market data
Liquidity Rewards
Earn rewards for providing liquidity
Setup
Liquidity Rewards
Ask a question...

github
Powered by
Trading - Polymarket Documentation

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.polymarket.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Liquidity Rewards

> Polymarket provides incentives aimed at catalyzing the supply and demand side of the marketplace. Specifically there is a public liquidity rewards program as well as one-off public pnl/volume competitions.

## Overview

By posting resting limit orders, liquidity providers (makers) are automatically eligible for Polymarket's incentive program. The overall goal of this program is to catalyze a healthy, liquid marketplace. We can further define this as creating incentives that:

* Catalyze liquidity across all markets
* Encourage liquidity throughout a market's entire lifecycle
* Motivate passive, balanced quoting tight to a market's mid-point
* Encourages trading activity
* Discourages blatantly exploitative behaviors

This program is heavily inspired by dYdX's liquidity provider rewards which you can read more about [here](https://www.dydx.foundation/blog/liquidity-provider-rewards). In fact, the incentive methodology is essentially a copy of dYdX's successful methodology but with some adjustments including specific adaptations for binary contract markets with distinct books, no staking mechanic a slightly modified order utility-relative depth function and reward amounts isolated per market. Rewards are distributed directly to the maker's addresses daily at midnight UTC.

## Methodology

Polymarket liquidity providers will be rewarded based on a formula that rewards participation in markets (complementary consideration!), boosts two-sided depth (single-sided orders still score), and spread (vs. mid-market, adjusted for the size cutoff!). Each market still configure a max spread and min size cutoff within which orders are considered the average of rewards earned is determined by the relative share of each participant's Q<sub>n</sub> in market m.

| Variable       | Description                                                      |
| -------------- | ---------------------------------------------------------------- |
| \$             | order position scoring function                                  |
| v              | max spread from midpoint (in cents)                              |
| s              | spread from size-cutoff-adjusted midpoint                        |
| b              | in-game multiplier                                               |
| m              | market                                                           |
| m'             | market complement (i.e NO if m = YES)                            |
| n              | trader index                                                     |
| u              | sample index                                                     |
| c              | scaling factor (currently 3.0 on all markets)                    |
| Q<sub>ne</sub> | point total for book one for a sample                            |
| Q<sub>no</sub> | point total for book two for a sample                            |
| Spread%        | distance from midpoint (bps or relative) for order n in market m |
| BidSize        | share-denominated quantity of bid                                |
| AskSize        | share-denominated quantity of ask                                |

## Equations

**Equation 1:**

$S(v,s)= (\frac{v-s}{v})^2 \cdot b$

**Equation 2:**

$Q_{one}= S(v,Spread_{m_1}) \cdot BidSize_{m_1} + S(v,Spread_{m_2}) \cdot BidSize_{m_2} + \dots $
$ + S(v, Spread_{m^\prime_1}) \cdot AskSize_{m^\prime_1} + S(v, Spread_{m^\prime_2}) \cdot AskSize_{m^\prime_2}$

**Equation 3:**

$Q_{two}= S(v,Spread_{m_1}) \cdot AskSize_{m_1} + S(v,Spread_{m_2}) \cdot AskSize_{m_2} + \dots $
$ + S(v, Spread_{m^\prime_1}) \cdot BidSize_{m^\prime_1} + S(v, Spread_{m^\prime_2}) \cdot BidSize_{m^\prime_2}$

**Equation 4:**

**Equation 4a:**

If midpoint is in range \[0.10,0.90] allow single sided liq to score:

$Q_{\min} = \max(\min({Q_{one}, Q_{two}}), \max(Q_{one}/c, Q_{two}/c))$

**Equation 4b:**

If midpoint is in either range \[0,0.10) or (.90,1.0] require liq to be double sided to score:

$Q_{\min} = \min({Q_{one}, Q_{two}})$

**Equation 5:**

$Q_{normal} = \frac{Q_{min}}{\sum_{n=1}^{N}{(Q_{min})_n}}$

**Equation 6:**

$Q_{epoch} = \sum_{u=1}^{10,080}{(Q_{normal})_u}$

**Equation 7:**

$Q_{final}=\frac{Q_{epoch}}{\sum_{n=1}^{N}{(Q_{epoch})_n}}$

## Steps

1. Quadratic scoring rule for an order based on position between the adjusted midpoint and the minimum qualifying spread

2. Calculate first market side score. Assume a trader has the following open orders:

   * 100Q bid on m @0.49 (adjusted midpoint is 0.50 then spread of this order is 0.01 or 1c)
   * 200Q bid on m @0.48
   * 100Q ask on m' @0.51

   and assume an adjusted market midpoint of 0.50 and maxSpread config of 3c for both m and m'. Then the trader's score is:

   $$
   Q_{ne} = \left( \frac{(3-1)}{3} \right)^2 \cdot 100 + \left( \frac{(3-2)}{3} \right)^2 \cdot 200 + \left( \frac{(3-1)}{3} \right)^2 \cdot 100
   $$

   $Q_{ne}$ is calculated every minute using random sampling

3. Calculate second market side score. Assume a trader has the following open orders:

   * 100Q bid on m @0.485
   * 100Q bid on m' @0.48
   * 200Q ask on m' @0.505

   and assume an adjusted market midpoint of 0.50 and maxSpread config of 3c for both m and m'. Then the trader's score is:

   $$
   Q_{no} = \left( \frac{(3-1.5)}{3} \right)^2 \cdot 100 + \left( \frac{(3-2)}{3} \right)^2 \cdot 100 + \left( \frac{(3-.5)}{3} \right)^2 \cdot 200
   $$

   $Q_{no}$ is calculated every minute using random sampling

4. Boosts 2-sided liquidity by taking the minimum of $Q_{ne}$ and $Q_{no}$, and rewards 1-side liquidity at a reduced rate (divided by c)

   Calculated every minute

5. $Q_{normal}$ is the $Q_{min}$ of a market maker divided by the sum of all the $Q_{min}$ of other market makers in a given sample

6. $Q_{epoch}$ is the sum of all $Q_{normal}$ for a trader in a given epoch

7. $Q_{final}$ normalizes $Q_{epoch}$ by dividing it by the sum of all other market maker's $Q_{epoch}$ in a given epoch this value is multiplied by the rewards available for the market to get a trader's reward

<Tip>Both min\_incentive\_size and max\_incentive\_spread can be fetched alongside full market objects via both the CLOB API and Markets API. Reward allocations for an epoch can be fetched via the Markets API. </Tip>

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.polymarket.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Maker Rebates Program

> Technical guide for handling taker fees and earning maker rebates on Polymarket

Polymarket has enabled **taker fees** on **15-minute crypto markets**. These fees fund a **Maker Rebates** program that pays daily USDC rebates to liquidity providers.

## Fee Handling by Implementation Type

### Option 1: Official CLOB Clients (Recommended)

The official CLOB clients **automatically handle fees** for you. Update to the latest version:

<CardGroup cols={2}>
  <Card title="TypeScript Client" icon="js" href="https://github.com/Polymarket/clob-client">
    npm install @polymarket/clob-client\@latest
  </Card>

  <Card title="Python Client" icon="python" href="https://github.com/Polymarket/py-clob-client">
    pip install --upgrade py-clob-client
  </Card>
</CardGroup>

**What the client does automatically:**

1. Fetches the fee rate for the market's token ID
2. Includes `feeRateBps` in the order structure
3. Signs the order with the fee rate included

**You don't need to do anything extra**. Just update your client and your orders will work on fee-enabled markets.

***

### Option 2: REST API / Custom Implementations

If you're calling the REST API directly or building your own order signing, you must manually include the fee rate in your **signed order payload**.

#### Step 1: Fetch the Fee Rate

Query the fee rate for the token ID before creating your order:

```bash  theme={null}
GET https://clob.polymarket.com/fee-rate?token_id={token_id}
```

**Response:**

```json  theme={null}
{
  "fee_rate_bps": 1000
}
```

* **Fee-enabled markets** return a value like `1000`
* **Fee-free markets** return `0`

#### Step 2: Include in Your Signed Order

Add the `feeRateBps` field to your order object. This value is **part of the signed payload**, the CLOB validates your signature against it.

```json  theme={null}
{
  "salt": "12345",
  "maker": "0x...",
  "signer": "0x...",
  "taker": "0x...",
  "tokenId": "71321045679252212594626385532706912750332728571942532289631379312455583992563",
  "makerAmount": "50000000",
  "takerAmount": "100000000",
  "expiration": "0",
  "nonce": "0",
  "feeRateBps": "1000",
  "side": "0",
  "signatureType": 2,
  "signature": "0x..."
}
```

#### Step 3: Sign and Submit

1. Include `feeRateBps` in the order object **before signing**
2. Sign the complete order
3. POST to `/order` endpoint

<Note>
  **Important:** Always fetch `fee_rate_bps` dynamically, do not hardcode. The fee rate may vary by market or change over time. You only need to pass `feeRateBps`
</Note>

See the [Create Order documentation](/developers/CLOB/orders/create-order) for full signing details.

***

## Fee Behavior

Fees are calculated in USDC and vary based on the share price. The effective rate **peaks at 50%** probability and decreases symmetrically toward the extremes.

### Fee Table (100 shares)

| Price  | Trade Value | Fee (USDC) | Effective Rate |
| ------ | ----------- | ---------- | -------------- |
| \$0.10 | \$10        | \$0.02     | 0.20%          |
| \$0.20 | \$20        | \$0.13     | 0.64%          |
| \$0.30 | \$30        | \$0.33     | 1.10%          |
| \$0.40 | \$40        | \$0.58     | 1.44%          |
| \$0.50 | \$50        | \$0.78     | **1.56%**      |
| \$0.60 | \$60        | \$0.86     | 1.44%          |
| \$0.70 | \$70        | \$0.77     | 1.10%          |
| \$0.80 | \$80        | \$0.51     | 0.64%          |
| \$0.90 | \$90        | \$0.18     | 0.20%          |

The maximum effective fee rate is **1.56%** at 50% probability. Fees are the same for both buying and selling.

***

## Maker Rebates

### How Rebates Work

* **Eligibility:** Your orders must add liquidity (maker orders) and get filled
* **Calculation:** Proportional to your share of executed maker volume in each eligible market
* **Payment:** Daily in USDC, paid directly to your wallet

### Rebate Pool

The rebate pool for each market is funded by taker fees collected in that market. The payout percentage is subject to change:

| Period                                           | Maker Rebate |
| ------------------------------------------------ | ------------ |
| Jan 9 – Jan 11, 2026 (Until Sunday Midnight UTC) | 100%         |
| Jan 12 – Jan 18, 2026                            | 20%          |

The rebate percentage is at the sole discretion of Polymarket.

***

## Which Markets Have Fees?

Currently, only **15-minute crypto markets** have fees enabled. Query the fee-rate endpoint to check:

```bash  theme={null}
GET https://clob.polymarket.com/fee-rate?token_id={token_id}

# Fee-enabled: { "fee_rate_bps": 1000 }
# Fee-free:    { "fee_rate_bps": 0 }
```

***

## Related Documentation

<CardGroup cols={2}>
  <Card title="Maker Rebates Program" icon="coins" href="/polymarket-learn/trading/maker-rebates-program">
    User-facing overview with full fee tables
  </Card>

  <Card title="Create CLOB Order via REST API" icon="code" href="/developers/CLOB/orders/create-order">
    Full order structure and signing documentation
  </Card>
</CardGroup>


Skip to main content
Polymarket Documentation home pagedark logo

Search...
Ctrl K

Ask AI
Main Site

User Guide
For Developers
Changelog
Polymarket
Discord Community
Twitter
Developer Quickstart
Developer Quickstart
Fetching Market Data
Placing Your First Order
Glossary
API Rate Limits
Endpoints
Market Makers
Market Maker Introduction
Setup
Trading
Liquidity Rewards
Maker Rebates Program
Data Feeds
Inventory Management
Polymarket Builders Program
Builder Program Introduction
Builder Tiers
Builder Profile & Keys
Order Attribution
Relayer Client
Examples
Central Limit Order Book
CLOB Introduction
Status
Quickstart
Authentication
Geographic Restrictions

Client

REST API

Historical Timeseries Data

Order Management

Trades
Websocket
WSS Overview
WSS Quickstart
WSS Authentication
User Channel
Market Channel

Sports Websocket
Real Time Data Stream
RTDS Overview
RTDS Crypto Prices
RTDS Comments
Gamma Structure
Overview
Gamma Structure
Fetching Markets
Gamma Endpoints

Gamma Status

Sports

Tags

Events

Markets

Series

Comments

Profiles

Search
Data-API

Data API Status

Core

Misc

Builders
Bridge & Swap
Overview

Bridge
Subgraph
Overview
Resolution
Resolution
Conditional Token Frameworks
Overview
Splitting USDC
Merging Tokens
Reedeeming Tokens
Deployment and Additional Information
Proxy Wallets
Proxy wallet
Negative Risk
Overview

On this page
Overview
WebSocket Feeds
Connecting
Available Channels
User Channel (Authenticated)
Best Practices
Gamma API
Get Markets
Get Events
Key Fields for MMs
Onchain Data
Data Sources
RPC Providers
UMA Oracle
Related Documentation
Market Makers
Data Feeds
Real-time and historical data sources for market makers

​
Overview
Market makers need fast, reliable data to price markets and manage inventory. Polymarket provides several data feeds at different latency and detail levels.
Feed	Latency	Use Case	Access
WebSocket	~100ms	Standard MM operations	Public
Gamma API	~1s	Market metadata, indexing	Public
Onchain	Block time	Settlement, resolution	Public
​
WebSocket Feeds
The WebSocket API provides real-time market data with low latency. This is sufficient for most market making strategies.
​
Connecting
const ws = new WebSocket("wss://ws-subscriptions-clob.polymarket.com/ws/market");

ws.onopen = () => {
  // Subscribe to orderbook updates
  ws.send(JSON.stringify({
    type: "market",
    assets_ids: [tokenId]
  }));
};

ws.onmessage = (event) => {
  const data = JSON.parse(event.data);
  // Handle orderbook update
};
​
Available Channels
Channel	Message Types	Documentation
market	book, price_change, last_trade_price	Market Channel
user	Order fills, cancellations	User Channel
​
User Channel (Authenticated)
Monitor your order activity in real-time:
// Requires authentication
const userWs = new WebSocket("wss://ws-subscriptions-clob.polymarket.com/ws/user");

userWs.onopen = () => {
  userWs.send(JSON.stringify({
    type: "user",
    auth: {
      apiKey: "your-api-key",
      secret: "your-secret",
      passphrase: "your-passphrase"
    },
    markets: [conditionId] // Optional: filter to specific markets
  }));
};

userWs.onmessage = (event) => {
  const data = JSON.parse(event.data);
  // Handle order fills, cancellations, etc.
};
See WebSocket Authentication for auth details.
​
Best Practices
Reconnection logic - Implement automatic reconnection with exponential backoff
Heartbeats - Respond to ping messages to maintain connection
Local orderbook - Maintain a local copy and apply incremental updates
Sequence numbers - Track sequence to detect missed messages
See WebSocket Overview for complete documentation.
​
Gamma API
The Gamma API provides market metadata and indexing. Use it for:
Market titles, slugs, categories
Event/condition mapping
Volume and liquidity data
Outcome token metadata
​
Get Markets
const response = await fetch(
  "https://gamma-api.polymarket.com/markets?active=true"
);
const markets = await response.json();
​
Get Events
const response = await fetch(
  "https://gamma-api.polymarket.com/events?slug=us-presidential-election"
);
const event = await response.json();
​
Key Fields for MMs
Field	Description
conditionId	Unique market identifier
clobTokenIds	Outcome token IDs
outcomes	Outcome names
outcomePrices	Current outcome prices
volume	Trading volume
liquidity	Current liquidity
See Gamma API Overview for complete documentation.
​
Onchain Data
For settlement, resolution, and position tracking, market makers may query onchain data directly.
​
Data Sources
Data	Source	Use Case
Token balances	ERC1155 balanceOf	Position tracking
Resolution	UMA Oracle events	Pre-resolution risk modeling
Condition resolution	CTF contract	Post-resolution redemption
​
RPC Providers
Common providers for Polygon:
Alchemy
QuickNode
Infura
​
UMA Oracle
Markets are resolved via UMA’s Optimistic Oracle. Monitor resolution events for risk management.
See Resolution for details on the resolution process.
​
Related Documentation
WebSocket Overview
Complete WebSocket documentation
Gamma API
Market metadata and indexing
Resolution
UMA Oracle resolution process
Maker Rebates Program
Inventory Management
Ask a question...

github
Powered by
Data Feeds - Polymarket Documentation

Skip to main content
Polymarket Documentation home pagedark logo

Search...
Ctrl K

Ask AI
Main Site

User Guide
For Developers
Changelog
Polymarket
Discord Community
Twitter
Developer Quickstart
Developer Quickstart
Fetching Market Data
Placing Your First Order
Glossary
API Rate Limits
Endpoints
Market Makers
Market Maker Introduction
Setup
Trading
Liquidity Rewards
Maker Rebates Program
Data Feeds
Inventory Management
Polymarket Builders Program
Builder Program Introduction
Builder Tiers
Builder Profile & Keys
Order Attribution
Relayer Client
Examples
Central Limit Order Book
CLOB Introduction
Status
Quickstart
Authentication
Geographic Restrictions

Client

REST API

Historical Timeseries Data

Order Management

Trades
Websocket
WSS Overview
WSS Quickstart
WSS Authentication
User Channel
Market Channel

Sports Websocket
Real Time Data Stream
RTDS Overview
RTDS Crypto Prices
RTDS Comments
Gamma Structure
Overview
Gamma Structure
Fetching Markets
Gamma Endpoints

Gamma Status

Sports

Tags

Events

Markets

Series

Comments

Profiles

Search
Data-API

Data API Status

Core

Misc

Builders
Bridge & Swap
Overview

Bridge
Subgraph
Overview
Resolution
Resolution
Conditional Token Frameworks
Overview
Splitting USDC
Merging Tokens
Reedeeming Tokens
Deployment and Additional Information
Proxy Wallets
Proxy wallet
Negative Risk
Overview

On this page
Overview
Splitting USDCe into Tokens
Via Relayer Client (Recommended)
Result
Merging Tokens to USDCe
Via Relayer Client
Result
Redeeming After Resolution
Check Resolution Status
Redeem Winning Tokens
Payout
Negative Risk Markets
Inventory Strategies
Pre-market Preparation
During Trading
Post-Resolution
Batch Operations
Related Documentation
Market Makers
Inventory Management
Split, merge, and redeem outcome tokens for market making

​
Overview
Market makers need to manage their inventory of outcome tokens. This involves:
Splitting USDCe into YES/NO tokens to have inventory to quote
Merging tokens back to USDCe to reduce exposure
Redeeming winning tokens after market resolution
All these operations use the Conditional Token Framework (CTF) contract, typically via the Relayer Client for gasless execution.
These examples assume you have initialized a RelayClient. See Setup for client initialization.
​
Splitting USDCe into Tokens
Split 1 USDCe into 1 YES + 1 NO token. This creates inventory for quoting both sides.
​
Via Relayer Client (Recommended)
import { ethers } from "ethers";
import { Interface } from "ethers/lib/utils";
import { RelayClient, Transaction } from "@polymarket/builder-relayer-client";

const CTF_ADDRESS = "0x4d97dcd97ec945f40cf65f87097ace5ea0476045";
const USDCe_ADDRESS = "0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174";

const ctfInterface = new Interface([
  "function splitPosition(address collateralToken, bytes32 parentCollectionId, bytes32 conditionId, uint[] partition, uint amount)"
]);

// Split $1000 USDCe into YES/NO tokens
const amount = ethers.utils.parseUnits("1000", 6); // USDCe has 6 decimals

const splitTx: Transaction = {
  to: CTF_ADDRESS,
  data: ctfInterface.encodeFunctionData("splitPosition", [
    USDCe_ADDRESS,                                    // collateralToken
    ethers.constants.HashZero,                       // parentCollectionId (null for Polymarket)
    conditionId,                                     // conditionId from market
    [1, 2],                                          // partition: [YES, NO]
    amount
  ]),
  value: "0"
};

const response = await client.execute([splitTx], "Split USDCe into tokens");
const result = await response.wait();
console.log("Split completed:", result?.transactionHash);
​
Result
After splitting 1000 USDCe:
Receive 1000 YES tokens
Receive 1000 NO tokens
USDCe balance decreases by 1000
​
Merging Tokens to USDCe
Merge equal amounts of YES + NO tokens back into USDCe. Useful for:
Reducing inventory
Exiting a market
Converting profits to USDCe
​
Via Relayer Client
const ctfInterface = new Interface([
  "function mergePositions(address collateralToken, bytes32 parentCollectionId, bytes32 conditionId, uint[] partition, uint amount)"
]);

// Merge 500 YES + 500 NO back to 500 USDCe
const amount = ethers.utils.parseUnits("500", 6);

const mergeTx: Transaction = {
  to: CTF_ADDRESS,
  data: ctfInterface.encodeFunctionData("mergePositions", [
    USDCe_ADDRESS,
    ethers.constants.HashZero,
    conditionId,
    [1, 2],
    amount
  ]),
  value: "0"
};

const response = await client.execute([mergeTx], "Merge tokens to USDCe");
await response.wait();
​
Result
After merging 500 of each:
YES tokens decrease by 500
NO tokens decrease by 500
USDCe balance increases by 500
​
Redeeming After Resolution
After a market resolves, redeem winning tokens for USDCe.
​
Check Resolution Status
// Via CLOB API
const market = await clobClient.getMarket(conditionId);
if (market.closed) {
  // Market is resolved
  const winningToken = market.tokens.find(t => t.winner);
  console.log("Winning outcome:", winningToken?.outcome);
}
​
Redeem Winning Tokens
const ctfInterface = new Interface([
  "function redeemPositions(address collateralToken, bytes32 parentCollectionId, bytes32 conditionId, uint[] indexSets)"
]);

const redeemTx: Transaction = {
  to: CTF_ADDRESS,
  data: ctfInterface.encodeFunctionData("redeemPositions", [
    USDCe_ADDRESS,
    ethers.constants.HashZero,
    conditionId,
    [1, 2]  // Redeem both YES and NO (only winners pay out)
  ]),
  value: "0"
};

const response = await client.execute([redeemTx], "Redeem winning tokens");
await response.wait();
​
Payout
If YES wins: Each YES token redeems for $1 USDCe
If NO wins: Each NO token redeems for $1 USDCe
Losing tokens are worthless (redeem for $0)
​
Negative Risk Markets
Multi-outcome markets use the Negative Risk CTF Exchange. The split/merge process is similar but uses different contract addresses.
const NEG_RISK_ADAPTER = "0xd91E80cF2E7be2e162c6513ceD06f1dD0dA35296";
const NEG_RISK_CTF_EXCHANGE = "0xC5d563A36AE78145C45a50134d48A1215220f80a";
See Negative Risk Overview for details.
​
Inventory Strategies
​
Pre-market Preparation
Before quoting a market:
Check market metadata via Gamma API
Split sufficient USDCe to cover expected quoting size
Set token approvals if not already done
​
During Trading
Monitor inventory and adjust:
Skew quotes when inventory is imbalanced
Merge excess tokens to free up capital
Split more when inventory runs low
​
Post-Resolution
After market closes:
Cancel all open orders
Wait for resolution
Redeem winning tokens
Merge any remaining pairs
​
Batch Operations
For efficiency, batch multiple operations:
const transactions: Transaction[] = [
  // Split on Market A
  {
    to: CTF_ADDRESS,
    data: ctfInterface.encodeFunctionData("splitPosition", [
      USDCe_ADDRESS,
      ethers.constants.HashZero,
      conditionIdA,
      [1, 2],
      ethers.utils.parseUnits("1000", 6)
    ]),
    value: "0"
  },
  // Split on Market B
  {
    to: CTF_ADDRESS,
    data: ctfInterface.encodeFunctionData("splitPosition", [
      USDCe_ADDRESS,
      ethers.constants.HashZero,
      conditionIdB,
      [1, 2],
      ethers.utils.parseUnits("1000", 6)
    ]),
    value: "0"
  }
];

const response = await client.execute(transactions, "Batch inventory setup");
await response.wait();
​
Related Documentation
CTF Overview
Conditional Token Framework basics
Split Positions
Detailed split documentation
Merge Positions
Detailed merge documentation
Relayer Client
Gasless transaction execution
Data Feeds
Builder Program Introduction
Ask a question...

github
Powered by
Inventory Management - Polymarket Documentation

Skip to main content
Polymarket Documentation home pagedark logo

Search...
Ctrl K

Ask AI
Main Site

User Guide
For Developers
Changelog
Polymarket
Discord Community
Twitter
Developer Quickstart
Developer Quickstart
Fetching Market Data
Placing Your First Order
Glossary
API Rate Limits
Endpoints
Market Makers
Market Maker Introduction
Setup
Trading
Liquidity Rewards
Maker Rebates Program
Data Feeds
Inventory Management
Polymarket Builders Program
Builder Program Introduction
Builder Tiers
Builder Profile & Keys
Order Attribution
Relayer Client
Examples
Central Limit Order Book
CLOB Introduction
Status
Quickstart
Authentication
Geographic Restrictions

Client

REST API

Historical Timeseries Data

Order Management

Trades
Websocket
WSS Overview
WSS Quickstart
WSS Authentication
User Channel
Market Channel

Sports Websocket
Real Time Data Stream
RTDS Overview
RTDS Crypto Prices
RTDS Comments
Gamma Structure
Overview
Gamma Structure
Fetching Markets
Gamma Endpoints

Gamma Status

Sports

Tags

Events

Markets

Series

Comments

Profiles

Search
Data-API

Data API Status

Core

Misc

Builders
Bridge & Swap
Overview

Bridge
Subgraph
Overview
Resolution
Resolution
Conditional Token Frameworks
Overview
Splitting USDC
Merging Tokens
Reedeeming Tokens
Deployment and Additional Information
Proxy Wallets
Proxy wallet
Negative Risk
Overview

On this page
What is a Builder?
Program Benefits
Relayer Access
Trading Attribution
Getting Started
SDKs & Libraries
Polymarket Builders Program
Builder Program Introduction
Learn about Polymarket’s Builder Program and how to integrate

​
What is a Builder?
A “builder” is a person, group, or organization that routes orders from their users to Polymarket. If you’ve created a platform that allows users to trade on Polymarket via your system, this program is for you.
​
Program Benefits
Relayer Access
All onchain operations are gasless through our relayer
Order Attribution
Get credited for orders and compete for grants on the Builder Leaderboard
Fee Share
Earn a share of fees on routed orders
​
Relayer Access
We expose our relayer to builders, providing gasless transactions for users with Polymarket’s Proxy Wallets deployed via Relayer Client.
When transactions are routed through proxy wallets, Polymarket pays all gas fees for:
Deploying Gnosis Safe Wallets or Custom Proxy (Magic Link users) Wallets
Token approvals (USDC, outcome tokens)
CTF operations (split, merge, redeem)
Order execution (via CLOB API)
EOA wallets do not have relayer access. Users trading directly from an EOA pay their own gas fees.
​
Trading Attribution
Attach custom headers to orders to identify your builder account:
Orders attributed to your builder account
Compete on the Builder Leaderboard for grants
Track performance via the Data API
Leaderboard API: Get aggregated builder rankings for a time period
Volume API: Get daily time-series volume data for trend analysis
​
Getting Started
Get Builder Credentials: Generate API keys from your Builder Profile
Configure Order Attribution: Set up CLOB client to credit trades to your account (guide)
Enable Gasless Transactions: Use the Relayer for gas-free wallet deployment and trading (guide)
See Example Apps for complete Next.js reference implementations.
​
SDKs & Libraries
CLOB Client (TypeScript)
Place orders with builder attribution
CLOB Client (Python)
Place orders with builder attribution
Relayer Client (TypeScript)
Gasless onchain transactions for your users
Relayer Client (Python)
Gasless onchain transactions for your users
Signing SDK (TypeScript)
Sign builder authentication headers
Signing SDK (Python)
Sign builder authentication headers
Inventory Management
Builder Tiers
Ask a question...

github
Powered by
Builder Program Introduction - Polymarket Documentation

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.polymarket.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Builder Tiers

> Permissionless integration with tiered rate limits, rewards, and revenue generating opportunities as you scale

## Overview

Polymarket Builders lets anyone integrate without approval.
Tiers exist to manage rate limits while rewarding high performing integrations with weekly rewards, grants, and revenue sharing opportunities. Higher tiers also unlock engineering support, marketing promotion, and priority access.

## Feature Definitions

| Feature                     | Description                                                                     |
| --------------------------- | ------------------------------------------------------------------------------- |
| **Daily Relayer Txn Limit** | Maximum Relayer transactions per day for Safe/Proxy wallet operations           |
| **API Rate Limits**         | Rate limits for non-relayer endpoints (CLOB, Gamma, etc.)                       |
| **Subsidized Transactions** | Gas fees subsidized for Relayer and CLOB operations via Safe/Proxy wallets      |
| **Order Attribution**       | Orders tracked and attributed to your Builder profile                           |
| **RevShare Protocol**       | Infrastructure allowing Builders to charge fees on top of Polymarket's base fee |
| **Leaderboard Visibility**  | Visibility on the [Builder leaderboard](https://builders.polymarket.com/)       |
| **Weekly Rewards**          | Weekly USDC rewards program for visible builders based on volume                |
| **Grants**                  | Builder grants awarded based on innovation and exclusivity                      |
| **Telegram Channel**        | Private Builders channel for announcements and support                          |
| **Badge**                   | Verified Builder affiliate badge on your Builder profile                        |
| **Engineering Support**     | Direct access to engineering team                                               |
| **Marketing Support**       | Promotion via official Polymarket social accounts                               |
| **Weekly Rewards Boost**    | Multiplier on the weekly USDC rewards program for visible builders              |
| **Priority Access**         | Early access to new features and products                                       |
| **Market Suggestions**      | Ability to propose new prediction markets                                       |
| **Base Fee Split**          | Volume based fee split on Polymarket's base fee                                 |

## Tier Comparison

| Feature                     | Unverified |  Verified |  Partner  |
| --------------------------- | :--------: | :-------: | :-------: |
| **Daily Relayer Txn Limit** |   100/day  | 1,500/day | Unlimited |
| **API Rate Limits**         |  Standard  |  Standard |  Highest  |
| **Subsidized Transactions** |      ✅     |     ✅     |     ✅     |
| **Order Attribution**       |      ✅     |     ✅     |     ✅     |
| **RevShare Protocol**       |      ❌     |     ✅     |     ✅     |
| **Leaderboard Visibility**  |      ❌     |     ✅     |     ✅     |
| **Weekly Rewards**          |      ❌     |     ✅     |     ✅     |
| **Telegram Channel**        |      ❌     |     ✅     |     ✅     |
| **Badge**                   |      ❌     |     ✅     |     ✅     |
| **Engineering Support**     |      ❌     |  Standard |  Elevated |
| **Marketing Support**       |      ❌     |  Standard |  Elevated |
| **Grants**                  |      ❌     |     ❌     |     ✅     |
| **Weekly Reward Boosts**    |      ❌     |     ❌     |     ✅     |
| **Priority Access**         |      ❌     |     ❌     |     ✅     |
| **Market Suggestions**      |      ❌     |     ❌     |     ✅     |
| **Base Fee Split**          |      ❌     |     ❌     |     ✅     |

***

### Unverified

<Card title="100 transactions/day" icon="seedling">
  The default tier for all new builders. Create Builder API keys instantly from your Polymarket profile.
</Card>

**How to get started:**

1. Go to [polymarket.com/settings?tab=builder](https://polymarket.com/settings?tab=builder)
2. Create a builder profile and click **"+ Create New"** to generate builder API keys
3. Implement [builder signing](/developers/builders/order-attribution); required for Relayer access and CLOB order attribution

**Included:**

* Gasless trading on all CLOB orders through Safe/Proxy wallets
* Gas subsidized on all Relayer transactions through Safe/Proxy wallets up to daily limit
* Order attribution credit to your Builder profile
* Access to all client libraries and documentation

***

### Verified

<Card title="1,500 transactions/day" icon="badge-check">
  For builders who need higher throughput. Requires manual approval by Polymarket.
</Card>

**How to upgrade:**

Contact us with your Builder API Key, use case, expected volume, and relevant info (app, docs, X profile).

**Unlocks over Unverified:**

* 15x daily Relayer transaction limit
* RevShare Protocol Access
* Telegram channel
* Leaderboard visibility
* Eligible for Weekly Rewards Program
* Promotion and verified affiliate badge from @PolymarketBuild
* Grants eligibility

***

### Partner

<Card title="Unlimited transactions/day" icon="handshake">
  Enterprise tier for high-volume integrations and strategic partners.
</Card>

**How to apply:**

Reach out to discuss partnership opportunities.

**Unlocks over Verified:**

* Unlimited Relayer transactions
* Highest API rate limits
* Elevated engineering support
* Elevated and coordinated marketing support
* Ability to suggest markets
* Priority access to new features and products
* Multiplier on the Weekly Rewards Program
* Custom split agreement on Polymarket's base fee

***

## Contact

Ready to upgrade or have questions?

* [builder@polymarket.com](mailto:builder@polymarket.com)

***

## FAQ

<AccordionGroup>
  <Accordion title="How do I know if I'm verified?">
    Verification is displayed in your [Builder Profile](https://polymarket.com/settings?tab=builder) settings.
  </Accordion>

  <Accordion title="What happens if I exceed my daily limit?">
    Relayer requests beyond your daily limit will be rate-limited and return an error. Consider upgrading to Verified or Partner tier if you're hitting limits.
  </Accordion>

  <Accordion title="Can I get a temporary limit increase?">
    For special events or product launches, contact [builder@polymarket.com](mailto:builder@polymarket.com)
  </Accordion>
</AccordionGroup>

***

## Next Steps

<CardGroup cols={2}>
  <Card title="Get Your Builder Keys" icon="key" href="/developers/builders/builder-profile">
    Create Builder API credentials to get started
  </Card>

  <Card title="Use Your Builder Keys" icon="server" href="/developers/builders/relayer-client">
    Configure Builder API credentials to attribute orders
  </Card>
</CardGroup>


Skip to main content
Polymarket Documentation home pagedark logo

Search...
Ctrl K

Ask AI
Main Site

User Guide
For Developers
Changelog
Polymarket
Discord Community
Twitter
Developer Quickstart
Developer Quickstart
Fetching Market Data
Placing Your First Order
Glossary
API Rate Limits
Endpoints
Market Makers
Market Maker Introduction
Setup
Trading
Liquidity Rewards
Maker Rebates Program
Data Feeds
Inventory Management
Polymarket Builders Program
Builder Program Introduction
Builder Tiers
Builder Profile & Keys
Order Attribution
Relayer Client
Examples
Central Limit Order Book
CLOB Introduction
Status
Quickstart
Authentication
Geographic Restrictions

Client

REST API

Historical Timeseries Data

Order Management

Trades
Websocket
WSS Overview
WSS Quickstart
WSS Authentication
User Channel
Market Channel

Sports Websocket
Real Time Data Stream
RTDS Overview
RTDS Crypto Prices
RTDS Comments
Gamma Structure
Overview
Gamma Structure
Fetching Markets
Gamma Endpoints

Gamma Status

Sports

Tags

Events

Markets

Series

Comments

Profiles

Search
Data-API

Data API Status

Core

Misc

Builders
Bridge & Swap
Overview

Bridge
Subgraph
Overview
Resolution
Resolution
Conditional Token Frameworks
Overview
Splitting USDC
Merging Tokens
Reedeeming Tokens
Deployment and Additional Information
Proxy Wallets
Proxy wallet
Negative Risk
Overview

On this page
Accessing Your Builder Profile
Builder Profile Settings
Customize Your Builder Identity
View Your Builder Information
Builder API Keys
Creating API Keys
Managing API Keys
Next Steps
Polymarket Builders Program
Builder Profile & Keys
Learn how to access your builder profile and obtain API credentials

​
Accessing Your Builder Profile
Direct Link
Go to polymarket.com/settings?tab=builder
From Profile Menu
Click your profile image and Select “Builders”
​
Builder Profile Settings
Builder Settings Page
​
Customize Your Builder Identity
Profile Picture: Upload a custom image for the Builder Leaderboard
Builder Name: Set the name displayed publicly on the leaderboard
​
View Your Builder Information
Builder Address: Your unique builder address for identification
Creation Date: When your builder account was created
Current Tier: Your rate limit tier (Unverified or Verified)
​
Builder API Keys
Builder API keys are required to access the relayer and for CLOB order attribution.
​
Creating API Keys
In the Builder Keys section of your profile’s Builder Settings:
View existing API keys with their creation dates and status
Click ”+ Create New” to generate a new API key
Each API key includes:
Credential	Description
apiKey	Your builder API key identifier
secret	Secret key for signing requests
passphrase	Additional authentication passphrase
​
Managing API Keys
Multiple Keys: Create separate keys for different environments
Active Status: Keys show “ACTIVE” when operational
​
Next Steps
Order Attribution
Start attributing customer orders to your account
Builder Leaderboard
View your public profile and stats
Builder Tiers
Order Attribution
Ask a question...

github
Powered by
Builder Profile & Keys - Polymarket Documentation

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.polymarket.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Order Attribution

> Learn how to attribute orders to your builder account

## Overview

The [CLOB (Central Limit Order Book)](/developers/CLOB/introduction) is Polymarket's order matching system. Order attribution adds builder authentication headers when placing orders through the CLOB Client, enabling Polymarket to credit trades to your builder account. This allows you to:

* Track volume on the [Builder Leaderboard](https://builders.polymarket.com/)
* Compete for grants based on trading activity
* Monitor performance via the Data API

***

## Builder API Credentials

Each builder receives API credentials from their [Builder Profile](/developers/builders/builder-profile):

| Credential   | Description                          |
| ------------ | ------------------------------------ |
| `key`        | Your builder API key identifier      |
| `secret`     | Secret key for signing requests      |
| `passphrase` | Additional authentication passphrase |

<Warning>
  **Security Notice**: Your Builder API keys must be kept secure. Never expose them in client-side code.
</Warning>

***

## Signing Methods

<Tabs>
  <Tab title="Remote Signing (Recommended)">
    Remote signing keeps your credentials secure on a server you control.

    **How it works:**

    1. User signs an order payload
    2. Payload is sent to your builder signing server
    3. Your server adds builder authentication headers
    4. Complete order is sent to the CLOB

    ### Server Implementation

    Your signing server receives request details and returns the authentication headers. Use the `buildHmacSignature` function from the SDK:

    <CodeGroup>
      ```typescript TypeScript theme={null}
      import { 
        buildHmacSignature, 
        BuilderApiKeyCreds 
      } from "@polymarket/builder-signing-sdk";

      const BUILDER_CREDENTIALS: BuilderApiKeyCreds = {
        key: process.env.POLY_BUILDER_API_KEY!,
        secret: process.env.POLY_BUILDER_SECRET!,
        passphrase: process.env.POLY_BUILDER_PASSPHRASE!,
      };

      // POST /sign - receives { method, path, body } from the client SDK
      export async function handleSignRequest(request) {
        const { method, path, body } = await request.json();
        
        const timestamp = Date.now().toString();
        
        const signature = buildHmacSignature(
          BUILDER_CREDENTIALS.secret,
          parseInt(timestamp),
          method,
          path,
          body
        );

        return {
          POLY_BUILDER_SIGNATURE: signature,
          POLY_BUILDER_TIMESTAMP: timestamp,
          POLY_BUILDER_API_KEY: BUILDER_CREDENTIALS.key,
          POLY_BUILDER_PASSPHRASE: BUILDER_CREDENTIALS.passphrase,
        };
      }
      ```

      ```python Python theme={null}
      import os
      import time
      from py_builder_signing_sdk.signing.hmac import build_hmac_signature
      from py_builder_signing_sdk import BuilderApiKeyCreds

      BUILDER_CREDENTIALS = BuilderApiKeyCreds(
          key=os.environ["POLY_BUILDER_API_KEY"],
          secret=os.environ["POLY_BUILDER_SECRET"],
          passphrase=os.environ["POLY_BUILDER_PASSPHRASE"],
      )

      # POST /sign - receives { method, path, body } from the client SDK
      def handle_sign_request(method: str, path: str, body: str):
          timestamp = str(int(time.time()))
          
          signature = build_hmac_signature(
              BUILDER_CREDENTIALS.secret,
              timestamp,
              method,
              path,
              body
          )

          return {
              "POLY_BUILDER_SIGNATURE": signature,
              "POLY_BUILDER_TIMESTAMP": timestamp,
              "POLY_BUILDER_API_KEY": BUILDER_CREDENTIALS.key,
              "POLY_BUILDER_PASSPHRASE": BUILDER_CREDENTIALS.passphrase,
          }
      ```
    </CodeGroup>

    <Warning>
      Never commit credentials to version control. Use environment variables or a secrets manager.
    </Warning>

    ### Client Configuration

    Point your client to your signing server:

    <CodeGroup>
      ```typescript TypeScript theme={null}
      import { ClobClient } from "@polymarket/clob-client";
      import { BuilderConfig } from "@polymarket/builder-signing-sdk";

      // Point to your signing server
      const builderConfig = new BuilderConfig({
        remoteBuilderConfig: { 
          url: "https://your-server.com/sign"
        }
      });

      // Or with optional authorization token
      const builderConfigWithAuth = new BuilderConfig({
        remoteBuilderConfig: { 
          url: "https://your-server.com/sign", 
          token: "your-auth-token" 
        }
      });

      const client = new ClobClient(
        "https://clob.polymarket.com",
        137,
        signer, // ethers v5.x EOA signer
        creds, // User's API Credentials
        2, // signatureType for the Safe proxy wallet
        funderAddress, // Safe proxy wallet address
        undefined, 
        false,
        builderConfig
      );

      // Orders automatically use the signing server
      const order = await client.createOrder({
        price: 0.40,
        side: Side.BUY,
        size: 5,
        tokenID: "YOUR_TOKEN_ID"
      });

      const response = await client.postOrder(order);
      ```

      ```python Python theme={null}
      from py_clob_client.client import ClobClient
      from py_builder_signing_sdk import BuilderConfig, RemoteBuilderConfig

      # Point to your signing server
      builder_config = BuilderConfig(
          remote_builder_config=RemoteBuilderConfig(
              url="https://your-server.com/sign"
          )
      )

      # Or with optional authorization token
      builder_config_with_auth = BuilderConfig(
          remote_builder_config=RemoteBuilderConfig(
              url="https://your-server.com/sign",
              token="your-auth-token"
          )
      )

      client = ClobClient(
          host="https://clob.polymarket.com",
          chain_id=137,
          key=private_key,
          creds=creds,  # User's API Credentials
          signature_type=2,  # signatureType for the Safe proxy wallet
          funder=funder_address,  # Safe proxy wallet address
          builder_config=builder_config
      )

      # Orders automatically use the signing server
      order = client.create_order({
          "price": 0.40,
          "side": "BUY",
          "size": 5,
          "token_id": "YOUR_TOKEN_ID"
      })

      response = client.post_order(order)
      ```
    </CodeGroup>

    ### Troubleshooting

    <AccordionGroup>
      <Accordion title="Invalid Signature Errors">
        **Error:** Client receives invalid signature errors

        **Solution:**

        1. Verify the request body is passed correctly as JSON
        2. Check that `path`, `body`, and `method` match what the client sends
        3. Ensure your server and client use the same Builder API credentials
      </Accordion>

      <Accordion title="Missing Credentials">
        **Error:** `Builder credentials not configured` or undefined values

        **Solution:** Ensure your environment variables are set:

        * `POLY_BUILDER_API_KEY`
        * `POLY_BUILDER_SECRET`
        * `POLY_BUILDER_PASSPHRASE`
      </Accordion>
    </AccordionGroup>
  </Tab>

  <Tab title="Local Signing">
    Sign orders locally when you control the entire order placement flow.

    **How it works:**

    1. Your system creates and signs orders on behalf of users
    2. Your system uses Builder API credentials locally to add headers
    3. Complete signed order is sent directly to the CLOB

    <CodeGroup>
      ```typescript TypeScript theme={null}
      import { ClobClient } from "@polymarket/clob-client";
      import { BuilderConfig, BuilderApiKeyCreds } from "@polymarket/builder-signing-sdk";

      // Configure with local builder credentials
      const builderCreds: BuilderApiKeyCreds = {
        key: process.env.POLY_BUILDER_API_KEY!,
        secret: process.env.POLY_BUILDER_SECRET!,
        passphrase: process.env.POLY_BUILDER_PASSPHRASE!
      };

      const builderConfig = new BuilderConfig({
        localBuilderCreds: builderCreds
      });

      const client = new ClobClient(
        "https://clob.polymarket.com",
        137,
        signer, // ethers v5.x EOA signer
        creds, // User's API Credentials
        2, // signatureType for the Safe proxy wallet
        funderAddress, // Safe proxy wallet address
        undefined, 
        false,
        builderConfig
      );

      // Orders automatically include builder headers
      const order = await client.createOrder({
        price: 0.40,
        side: Side.BUY,
        size: 5,
        tokenID: "YOUR_TOKEN_ID"
      });

      const response = await client.postOrder(order);
      ```

      ```python Python theme={null}
      import os
      from py_clob_client.client import ClobClient
      from py_builder_signing_sdk import BuilderConfig, BuilderApiKeyCreds

      # Configure with local builder credentials
      builder_creds = BuilderApiKeyCreds(
          key=os.environ["POLY_BUILDER_API_KEY"],
          secret=os.environ["POLY_BUILDER_SECRET"],
          passphrase=os.environ["POLY_BUILDER_PASSPHRASE"]
      )

      builder_config = BuilderConfig(
          local_builder_creds=builder_creds
      )

      client = ClobClient(
          host="https://clob.polymarket.com",
          chain_id=137,
          key=private_key,
          creds=creds,  # User's API Credentials
          signature_type=2,  # signatureType for the Safe proxy wallet
          funder=funder_address,  # Safe proxy wallet address
          builder_config=builder_config
      )

      # Orders automatically include builder headers
      order = client.create_order({
          "price": 0.40,
          "side": "BUY",
          "size": 5,
          "token_id": "YOUR_TOKEN_ID"
      })

      response = client.post_order(order)
      ```
    </CodeGroup>

    <Warning>
      Never commit credentials to version control. Use environment variables or a secrets manager.
    </Warning>
  </Tab>
</Tabs>

***

## Authentication Headers

The SDK automatically generates and attaches these headers to each request:

| Header                    | Description                          |
| ------------------------- | ------------------------------------ |
| `POLY_BUILDER_API_KEY`    | Your builder API key                 |
| `POLY_BUILDER_TIMESTAMP`  | Unix timestamp of signature creation |
| `POLY_BUILDER_PASSPHRASE` | Your builder passphrase              |
| `POLY_BUILDER_SIGNATURE`  | HMAC signature of the request        |

<Info>
  With **local signing**, the SDK constructs and attaches these headers automatically. With **remote signing**, your server must return these headers (see Server Implementation above), and the SDK attaches them to the request.
</Info>

***

## Next Steps

<CardGroup cols={2}>
  <Card title="Relayer Client" icon="bolt" href="/developers/builders/relayer-client">
    Learn how to configure and use the Relay Client too!
  </Card>

  <Card title="CLOB Client Methods" icon="book" href="/developers/CLOB/clients/methods-overview">
    Explore the complete CLOB client reference
  </Card>
</CardGroup>


Skip to main content
Polymarket Documentation home pagedark logo

Search...
Ctrl K

Ask AI
Main Site

User Guide
For Developers
Changelog
Polymarket
Discord Community
Twitter
Developer Quickstart
Developer Quickstart
Fetching Market Data
Placing Your First Order
Glossary
API Rate Limits
Endpoints
Market Makers
Market Maker Introduction
Setup
Trading
Liquidity Rewards
Maker Rebates Program
Data Feeds
Inventory Management
Polymarket Builders Program
Builder Program Introduction
Builder Tiers
Builder Profile & Keys
Order Attribution
Relayer Client
Examples
Central Limit Order Book
CLOB Introduction
Status
Quickstart
Authentication
Geographic Restrictions

Client

REST API

Historical Timeseries Data

Order Management

Trades
Websocket
WSS Overview
WSS Quickstart
WSS Authentication
User Channel
Market Channel

Sports Websocket
Real Time Data Stream
RTDS Overview
RTDS Crypto Prices
RTDS Comments
Gamma Structure
Overview
Gamma Structure
Fetching Markets
Gamma Endpoints

Gamma Status

Sports

Tags

Events

Markets

Series

Comments

Profiles

Search
Data-API

Data API Status

Core

Misc

Builders
Bridge & Swap
Overview

Bridge
Subgraph
Overview
Resolution
Resolution
Conditional Token Frameworks
Overview
Splitting USDC
Merging Tokens
Reedeeming Tokens
Deployment and Additional Information
Proxy Wallets
Proxy wallet
Negative Risk
Overview

On this page
Overview
Builder API Credentials
Installation
Relayer Endpoint
Signing Methods
Server Implementation
Client Configuration
Authentication Headers
Wallet Types
Usage
Deploy a Wallet
Execute Transactions
Transaction Examples
Reference
Contracts & Approvals
Transaction States
TypeScript Types
Next Steps
Polymarket Builders Program
Relayer Client
Use Polymarket’s Polygon relayer to execute gasless transactions for your users

​
Overview
The Relayer Client routes onchain transactions through Polymarket’s infrastructure, providing gasless transactions for your users. Builder authentication is required to access the relayer.
Gasless Transactions
Polymarket pays all gas fees
Wallet Deployment
Deploy Safe or Proxy wallets
CTF Operations
Split, merge, and redeem positions
​
Builder API Credentials
Each builder receives API credentials from their Builder Profile:
Credential	Description
key	Your builder API key identifier
secret	Secret key for signing requests
passphrase	Additional authentication passphrase
Security Notice: Your Builder API keys must be kept secure. Never expose them in client-side code.
​
Installation

TypeScript

Python
npm install @polymarket/builder-relayer-client
​
Relayer Endpoint
All relayer requests are sent to Polymarket’s relayer service on Polygon:
https://relayer-v2.polymarket.com/
​
Signing Methods
Remote Signing (Recommended)
Local Signing
Remote signing keeps your credentials secure on a server you control.
How it works:
Client sends request details to your signing server
Your server generates the HMAC signature
Client attaches headers and sends to relayer
​
Server Implementation
Your signing server receives request details and returns the authentication headers:

TypeScript

Python
import { 
  buildHmacSignature, 
  BuilderApiKeyCreds 
} from "@polymarket/builder-signing-sdk";

const BUILDER_CREDENTIALS: BuilderApiKeyCreds = {
  key: process.env.POLY_BUILDER_API_KEY!,
  secret: process.env.POLY_BUILDER_SECRET!,
  passphrase: process.env.POLY_BUILDER_PASSPHRASE!,
};

// POST /sign - receives { method, path, body } from the client SDK
export async function handleSignRequest(request) {
  const { method, path, body } = await request.json();
  
  const timestamp = Date.now().toString();
  
  const signature = buildHmacSignature(
    BUILDER_CREDENTIALS.secret,
    parseInt(timestamp),
    method,
    path,
    body
  );

  return {
    POLY_BUILDER_SIGNATURE: signature,
    POLY_BUILDER_TIMESTAMP: timestamp,
    POLY_BUILDER_API_KEY: BUILDER_CREDENTIALS.key,
    POLY_BUILDER_PASSPHRASE: BUILDER_CREDENTIALS.passphrase,
  };
}
Never commit credentials to version control. Use environment variables or a secrets manager.
​
Client Configuration
Point your client to your signing server:

TypeScript

Python
import { createWalletClient, http, Hex } from "viem";
import { privateKeyToAccount } from "viem/accounts";
import { polygon } from "viem/chains";
import { RelayClient } from "@polymarket/builder-relayer-client";
import { BuilderConfig } from "@polymarket/builder-signing-sdk";

// Create wallet
const account = privateKeyToAccount(process.env.PRIVATE_KEY as Hex);
const wallet = createWalletClient({
  account,
  chain: polygon,
  transport: http(process.env.RPC_URL)
});

// Configure remote signing
const builderConfig = new BuilderConfig({
  remoteBuilderConfig: { 
    url: "https://your-server.com/sign" 
  }
});

const RELAYER_URL = "https://relayer-v2.polymarket.com/";
const CHAIN_ID = 137;

const client = new RelayClient(
  RELAYER_URL,
  CHAIN_ID,
  wallet,
  builderConfig
);
​
Authentication Headers
The SDK automatically generates and attaches these headers to each request:
Header	Description
POLY_BUILDER_API_KEY	Your builder API key
POLY_BUILDER_TIMESTAMP	Unix timestamp of signature creation
POLY_BUILDER_PASSPHRASE	Your builder passphrase
POLY_BUILDER_SIGNATURE	HMAC signature of the request
With local signing, the SDK constructs and attaches these headers automatically. With remote signing, your server must return these headers (see Server Implementation above), and the SDK attaches them to the request.
​
Wallet Types
Choose your wallet type before using the relayer:
Safe Wallets
Proxy Wallets
Gnosis Safe-based proxy wallets that require explicit deployment before use.
Best for: Most builder integrations
Deployment: Call client.deploy() before first transaction
Gas fees: Paid by Polymarket

TypeScript

Python
const client = new RelayClient(
  "https://relayer-v2.polymarket.com", 
  137,
  eoaSigner, 
  builderConfig, 
  RelayerTxType.SAFE  // Default
);

// Deploy before first use
const response = await client.deploy();
const result = await response.wait();
console.log("Safe Address:", result?.proxyAddress);
Wallet Comparison Table

​
Usage
​
Deploy a Wallet
For Safe wallets, deploy before executing transactions:

TypeScript

Python
const response = await client.deploy();
const result = await response.wait();

if (result) {
  console.log("Safe deployed successfully!");
  console.log("Transaction Hash:", result.transactionHash);
  console.log("Safe Address:", result.proxyAddress);
}
​
Execute Transactions
The execute method sends transactions through the relayer. Pass an array of transactions to batch multiple operations in a single call.

TypeScript

Python
interface Transaction {
  to: string;    // Target contract or wallet address
  data: string;  // Encoded function call (use "0x" for simple transfers)
  value: string; // Amount of MATIC to send (usually "0")
}

const response = await client.execute(transactions, "Description");
const result = await response.wait();

if (result) {
  console.log("Transaction confirmed:", result.transactionHash);
}
​
Transaction Examples
Transfer
Approve
Redeem Positions
Split Positions
Merge Positions
Batch Transactions
Transfer tokens to any address (e.g., withdrawals):

TypeScript

Python
import { encodeFunctionData, parseUnits } from "viem";

const transferTx = {
  to: "0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174", // USDCe
  data: encodeFunctionData({
    abi: [{
      name: "transfer",
      type: "function",
      inputs: [
        { name: "to", type: "address" },
        { name: "amount", type: "uint256" }
      ],
      outputs: [{ type: "bool" }]
    }],
    functionName: "transfer",
    args: [
      "0xRecipientAddressHere",
      parseUnits("100", 6) // 100 USDCe (6 decimals)
    ]
  }),
  value: "0"
};

const response = await client.execute([transferTx], "Transfer USDCe");
await response.wait();
​
Reference
​
Contracts & Approvals
Contract	Address	USDCe	Outcome Tokens
USDCe	0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174	—	—
CTF	0x4d97dcd97ec945f40cf65f87097ace5ea0476045	✅	—
CTF Exchange	0x4bFb41d5B3570DeFd03C39a9A4D8dE6Bd8B8982E	✅	✅
Neg Risk CTF Exchange	0xC5d563A36AE78145C45a50134d48A1215220f80a	✅	✅
Neg Risk Adapter	0xd91E80cF2E7be2e162c6513ceD06f1dD0dA35296	—	✅
​
Transaction States
State	Description
STATE_NEW	Transaction received by relayer
STATE_EXECUTED	Transaction executed onchain
STATE_MINED	Transaction included in a block
STATE_CONFIRMED	Transaction confirmed (final ✅)
STATE_FAILED	Transaction failed (terminal ❌)
STATE_INVALID	Transaction rejected as invalid (terminal ❌)
​
TypeScript Types
View Type Definitions

​
Next Steps
Order Attribution
Attribute orders to your builder account
Example Apps
Complete integration examples
Order Attribution
Examples
Ask a question...

github
Powered by
Relayer Client - Polymarket Documentation

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.polymarket.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Examples

> Complete Next.js applications demonstrating Polymarket builder integration

## Overview

These open-source demo applications show how to integrate Polymarket's CLOB Client and Builder Relayer Client for gasless trading with builder order attribution.

<CardGroup cols={3}>
  <Card title="Authentication" icon="user-check">
    Multiple wallet providers
  </Card>

  <Card title="Gasless Trading" icon="gas-pump">
    Safe & Proxy wallet support
  </Card>

  <Card title="Full Integration" icon="puzzle-piece">
    Orders, positions, CTF ops
  </Card>
</CardGroup>

***

## Safe Wallet Examples

Deploy Gnosis Safe wallets for your users:

<CardGroup cols={2}>
  <Card title="wagmi + Safe" icon="wallet" href="https://github.com/Polymarket/wagmi-safe-builder-example">
    MetaMask, Phantom, Rabby, and other browser wallets
  </Card>

  <Card title="Privy + Safe" icon="shield-check" href="https://github.com/Polymarket/privy-safe-builder-example">
    Privy embedded wallets
  </Card>

  <Card title="Magic Link + Safe" icon="wand-magic-sparkles" href="https://github.com/Polymarket/magic-safe-builder-example">
    Magic Link email/social authentication
  </Card>

  <Card title="Turnkey + Safe" icon="key" href="https://github.com/Polymarket/turnkey-safe-builder-example">
    Turnkey embedded wallets
  </Card>
</CardGroup>

## Proxy Wallet Examples

For existing Magic Link users from Polymarket.com:

<CardGroup cols={1}>
  <Card title="Magic Link + Proxy" icon="wand-magic-sparkles" href="https://github.com/Polymarket/magic-proxy-builder-example">
    Auto-deploying proxy wallets for Polymarket.com Magic users
  </Card>
</CardGroup>

***

## What Each Demo Covers

<Tabs>
  <Tab title="Authentication">
    * User sign-in via wallet provider
    * User API credential derivation (L2 auth)
    * Builder config with remote signing
    * Signature types for Safe vs Proxy wallets
  </Tab>

  <Tab title="Wallet Operations">
    * Safe wallet deployment via Relayer
    * Batch token approvals (USDC.e + outcome tokens)
    * CTF operations (split, merge, redeem)
    * Transaction monitoring
  </Tab>

  <Tab title="Trading">
    * CLOB client initialization
    * Order placement with builder attribution
    * Position and order management
    * Market discovery via Gamma API
  </Tab>
</Tabs>


Skip to main content
Polymarket Documentation home pagedark logo

Search...
Ctrl K

Ask AI
Main Site

User Guide
For Developers
Changelog
Polymarket
Discord Community
Twitter
Developer Quickstart
Developer Quickstart
Fetching Market Data
Placing Your First Order
Glossary
API Rate Limits
Endpoints
Market Makers
Market Maker Introduction
Setup
Trading
Liquidity Rewards
Maker Rebates Program
Data Feeds
Inventory Management
Polymarket Builders Program
Builder Program Introduction
Builder Tiers
Builder Profile & Keys
Order Attribution
Relayer Client
Examples
Central Limit Order Book
CLOB Introduction
Status
Quickstart
Authentication
Geographic Restrictions

Client

REST API

Historical Timeseries Data

Order Management

Trades
Websocket
WSS Overview
WSS Quickstart
WSS Authentication
User Channel
Market Channel

Sports Websocket
Real Time Data Stream
RTDS Overview
RTDS Crypto Prices
RTDS Comments
Gamma Structure
Overview
Gamma Structure
Fetching Markets
Gamma Endpoints

Gamma Status

Sports

Tags

Events

Markets

Series

Comments

Profiles

Search
Data-API

Data API Status

Core

Misc

Builders
Bridge & Swap
Overview

Bridge
Subgraph
Overview
Resolution
Resolution
Conditional Token Frameworks
Overview
Splitting USDC
Merging Tokens
Reedeeming Tokens
Deployment and Additional Information
Proxy Wallets
Proxy wallet
Negative Risk
Overview

On this page
System
API
Security
Fees
Schedule
Overview
Additional Resources
Central Limit Order Book
CLOB Introduction
Welcome to the Polymarket Order Book API! This documentation provides overviews, explanations, examples, and annotations to simplify interaction with the order book. The following sections detail the Polymarket Order Book and the API usage.
​
System
Polymarket’s Order Book, or CLOB (Central Limit Order Book), is hybrid-decentralized. It includes an operator for off-chain matching/ordering, with settlement executed on-chain, non-custodially, via signed order messages.
The exchange uses a custom Exchange contract facilitating atomic swaps between binary Outcome Tokens (CTF ERC1155 assets and ERC20 PToken assets) and collateral assets (ERC20), following signed limit orders. Designed for binary markets, the contract enables complementary tokens to match across a unified order book.
Orders are EIP712-signed structured data. Matched orders have one maker and one or more takers, with price improvements benefiting the taker. The operator handles off-chain order management and submits matched trades to the blockchain for on-chain execution.
​
API
The Polymarket Order Book API enables market makers and traders to programmatically manage market orders. Orders of any amount can be created, listed, fetched, or read from the market order books. Data includes all available markets, market prices, and order history via REST and WebSocket endpoints.
​
Security
Polymarket’s Exchange contract has been audited by Chainsecurity (View Audit).
The operator’s privileges are limited to order matching, non-censorship, and ensuring correct ordering. Operators can’t set prices or execute unauthorized trades. Users can cancel orders on-chain independently if trust issues arise.
​
Fees
​
Schedule
Subject to change
Volume Level	Maker Fee Base Rate (bps)	Taker Fee Base Rate (bps)
>0 USDC	0	0
​
Overview
Fees apply symmetrically in output assets (proceeds). This symmetry ensures fairness and market integrity. Fees are calculated differently depending on whether you are buying or selling:
Selling outcome tokens (base) for collateral (quote):
f
e
e
Q
u
o
t
e
=
b
a
s
e
R
a
t
e
×
min
⁡
(
p
r
i
c
e
,
1
−
p
r
i
c
e
)
×
s
i
z
e
feeQuote=baseRate×min(price,1−price)×size
Buying outcome tokens (base) with collateral (quote):
f
e
e
B
a
s
e
=
b
a
s
e
R
a
t
e
×
min
⁡
(
p
r
i
c
e
,
1
−
p
r
i
c
e
)
×
s
i
z
e
p
r
i
c
e
feeBase=baseRate×min(price,1−price)× 
price
size
​
 
​
Additional Resources
Exchange contract source code
Exchange contract documentation
Examples
Status
Ask a question...

github
Powered by
CLOB Introduction - Polymarket Documentation

Skip to main content
Polymarket Documentation home pagedark logo

Search...
Ctrl K

Ask AI
Main Site

User Guide
For Developers
Changelog
Polymarket
Discord Community
Twitter
Developer Quickstart
Developer Quickstart
Fetching Market Data
Placing Your First Order
Glossary
API Rate Limits
Endpoints
Market Makers
Market Maker Introduction
Setup
Trading
Liquidity Rewards
Maker Rebates Program
Data Feeds
Inventory Management
Polymarket Builders Program
Builder Program Introduction
Builder Tiers
Builder Profile & Keys
Order Attribution
Relayer Client
Examples
Central Limit Order Book
CLOB Introduction
Status
Quickstart
Authentication
Geographic Restrictions

Client

REST API

Historical Timeseries Data

Order Management

Trades
Websocket
WSS Overview
WSS Quickstart
WSS Authentication
User Channel
Market Channel

Sports Websocket
Real Time Data Stream
RTDS Overview
RTDS Crypto Prices
RTDS Comments
Gamma Structure
Overview
Gamma Structure
Fetching Markets
Gamma Endpoints

Gamma Status

Sports

Tags

Events

Markets

Series

Comments

Profiles

Search
Data-API

Data API Status

Core

Misc

Builders
Bridge & Swap
Overview

Bridge
Subgraph
Overview
Resolution
Resolution
Conditional Token Frameworks
Overview
Splitting USDC
Merging Tokens
Reedeeming Tokens
Deployment and Additional Information
Proxy Wallets
Proxy wallet
Negative Risk
Overview
Central Limit Order Book
Status
Check the status of the Polymarket Order Book:
Status Page
CLOB Introduction
Quickstart
Ask a question...

github
Powered by
Status - Polymarket Documentation

Skip to main content
Polymarket Documentation home pagedark logo

Search...
Ctrl K

Ask AI
Main Site

User Guide
For Developers
Changelog
Polymarket
Discord Community
Twitter
Developer Quickstart
Developer Quickstart
Fetching Market Data
Placing Your First Order
Glossary
API Rate Limits
Endpoints
Market Makers
Market Maker Introduction
Setup
Trading
Liquidity Rewards
Maker Rebates Program
Data Feeds
Inventory Management
Polymarket Builders Program
Builder Program Introduction
Builder Tiers
Builder Profile & Keys
Order Attribution
Relayer Client
Examples
Central Limit Order Book
CLOB Introduction
Status
Quickstart
Authentication
Geographic Restrictions

Client

REST API

Historical Timeseries Data

Order Management

Trades
Websocket
WSS Overview
WSS Quickstart
WSS Authentication
User Channel
Market Channel

Sports Websocket
Real Time Data Stream
RTDS Overview
RTDS Crypto Prices
RTDS Comments
Gamma Structure
Overview
Gamma Structure
Fetching Markets
Gamma Endpoints

Gamma Status

Sports

Tags

Events

Markets

Series

Comments

Profiles

Search
Data-API

Data API Status

Core

Misc

Builders
Bridge & Swap
Overview

Bridge
Subgraph
Overview
Resolution
Resolution
Conditional Token Frameworks
Overview
Splitting USDC
Merging Tokens
Reedeeming Tokens
Deployment and Additional Information
Proxy Wallets
Proxy wallet
Negative Risk
Overview

On this page
Installation
Quick Start
1. Setup Client
2. Place an Order
3. Check Your Orders
Complete Example
Troubleshooting
Next Steps
Central Limit Order Book
Quickstart
Initialize the CLOB and place your first order.

​
Installation

TypeScript

Python
npm install @polymarket/clob-client ethers
​
Quick Start
​
1. Setup Client

TypeScript

Python
import { ClobClient } from "@polymarket/clob-client";
import { Wallet } from "ethers"; // v5.8.0

const HOST = "https://clob.polymarket.com";
const CHAIN_ID = 137; // Polygon mainnet
const signer = new Wallet(process.env.PRIVATE_KEY);

// Create or derive user API credentials
const tempClient = new ClobClient(HOST, CHAIN_ID, signer);
const apiCreds = await tempClient.createOrDeriveApiKey();

// See 'Signature Types' note below
const signatureType = 0;

// Initialize trading client
const client = new ClobClient(
  HOST, 
  CHAIN_ID, 
  signer, 
  apiCreds, 
  signatureType
);
This quick start sets your EOA as the trading account. You’ll need to fund this wallet to trade and pay for gas on transactions. Gas-less transactions are only available by deploying a proxy wallet and using Polymarket’s Polygon relayer infrastructure.
Signature Types

​
2. Place an Order

TypeScript

Python
import { Side } from "@polymarket/clob-client";

// Place a limit order in one step
const response = await client.createAndPostOrder({
  tokenID: "YOUR_TOKEN_ID", // Get from Gamma API
  price: 0.65, // Price per share
  size: 10, // Number of shares
  side: Side.BUY, // or SELL
});

console.log(`Order placed! ID: ${response.orderID}`);
​
3. Check Your Orders

TypeScript

Python
// View all open orders
const openOrders = await client.getOpenOrders();
console.log(`You have ${openOrders.length} open orders`);

// View your trade history
const trades = await client.getTrades();
console.log(`You've made ${trades.length} trades`);
​
Complete Example

TypeScript

Python
import { ClobClient, Side } from "@polymarket/clob-client";
import { Wallet } from "ethers";

async function trade() {
  const HOST = "https://clob.polymarket.com";
  const CHAIN_ID = 137; // Polygon mainnet
  const signer = new Wallet(process.env.PRIVATE_KEY);

  const tempClient = new ClobClient(HOST, CHAIN_ID, signer);
  const apiCreds = await tempClient.createOrDeriveApiKey();

  const signatureType = 0;

  const client = new ClobClient(
    HOST,
    CHAIN_ID,
    signer,
    apiCreds,
    signatureType
  );

  const response = await client.createAndPostOrder({
    tokenID: "YOUR_TOKEN_ID",
    price: 0.65,
    size: 10,
    side: Side.BUY,
  });

  console.log(`Order placed! ID: ${response.orderID}`);
}

trade();
​
Troubleshooting
Error: L2_AUTH_NOT_AVAILABLE

Order rejected: insufficient balance

Order rejected: insufficient allowance

What's my funder address?

​
Next Steps
Full Example Implementations
Complete Next.js examples demonstrating integration of embedded wallets (Privy, Magic, Turnkey, wagmi) and the CLOB and Builder Relay clients
Understand CLOB Authentication
Deep dive into L1 and L2 authentication
Browse Client Methods
Explore the complete client reference
Find Markets to Trade
Use Gamma API to discover markets
Monitor with WebSocket
Get real-time order updates
Status
Authentication
Ask a question...

github
Powered by
Quickstart - Polymarket Documentation

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.polymarket.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Authentication

> Understanding authentication using Polymarket's CLOB

The CLOB uses two levels of authentication: **L1 (Private Key)** and **L2 (API Key)**.
Either can be accomplished using the CLOB client or REST API. Authentication is not
required to access client public methods and public endpoints.

## Authentication Levels

<CardGroup cols={2}>
  <Card title="L1 Authentication" icon="key" href="#l1-authentication">
    Use the private key of the user’s account to sign messages
  </Card>

  <Card title="L2 Authentication" icon="lock" href="#l2-authentication">
    Use API credentials (key, secret, passphrase) to authenticate requests to the CLOB
  </Card>
</CardGroup>

***

## L1 Authentication

### What is L1?

L1 authentication uses the wallet's private key to sign an EIP-712 message used in the
request header. It proves ownership and control over the private key. The private key
stays in control of the user and all trading activity remains non-custodial.

### What This Enables

Access to L1 methods that create or derive L2 authentication headers.

* Create user API credentials
* Derive existing user API credentials
* Sign/create user's orders locally

### CLOB Client

<Tabs>
  <Tab title="TypeScript">
    ```typescript  theme={null}
    import { ClobClient } from "@polymarket/clob-client";
    import { Wallet } from "ethers"; // v5.8.0

    const HOST = "https://clob.polymarket.com";
    const CHAIN_ID = 137; // Polygon mainnet
    const signer = new Wallet(process.env.PRIVATE_KEY);

    const client = new ClobClient(
      HOST,
      CHAIN_ID,
      signer // Signer enables L1 methods
    );

    // Gets API key, or else creates
    const apiCreds = await client.createOrDeriveApiKey();

    /*
    apiCreds = {
      "apiKey": "550e8400-e29b-41d4-a716-446655440000",
      "secret": "base64EncodedSecretString",
      "passphrase": "randomPassphraseString"
    }
    */
    ```
  </Tab>

  <Tab title="Python">
    ```python  theme={null}
    from py_clob_client.client import ClobClient
    import os

    host = "https://clob.polymarket.com"
    chain_id = 137 # Polygon mainnet
    private_key = os.getenv("PRIVATE_KEY")

    client = ClobClient(
        host=host,
        chain_id=chaind_id,
        key=private_key  # Signer enables L1 methods
    )

    # Gets API key, or else creates
    api_creds = await client.create_or_derive_api_key()

    # api_creds = {
    #     "apiKey": "550e8400-e29b-41d4-a716-446655440000",
    #     "secret": "base64EncodedSecretString",
    #     "passphrase": "randomPassphraseString"
    # }
    ```
  </Tab>
</Tabs>

<Warning>
  **Never commit private keys to version control.** Always use environment
  variables or secure key management systems.
</Warning>

***

### REST API

While we highly recommend using our provided clients to handle signing
and authentication, the following is for developers who choose NOT to
use our [Python](https://github.com/Polymarket/py-clob-client) or
[TypeScript](https://github.com/Polymarket/clob-client) clients.

When making direct REST API calls with L1 authentication, include these headers:

| Header           | Required? | Description            |
| ---------------- | --------- | ---------------------- |
| `POLY_ADDRESS`   | yes       | Polygon signer address |
| `POLY_SIGNATURE` | yes       | CLOB EIP 712 signature |
| `POLY_TIMESTAMP` | yes       | Current UNIX timestamp |
| `POLY_NONCE`     | yes       | Nonce. Default 0       |

The `POLY_SIGNATURE` is generated by signing the following EIP-712 struct.

<Accordion title="EIP-712 Signing Example">
  <CodeGroup>
    ```typescript Typescript theme={null}
    const domain = {
      name: "ClobAuthDomain",
      version: "1",
      chainId: chainId, // Polygon Chain ID 137
    };

    const types = {
      ClobAuth: [
        { name: "address", type: "address" },
        { name: "timestamp", type: "string" },
        { name: "nonce", type: "uint256" },
        { name: "message", type: "string" },
      ],
    };

    const value = {
      address: signingAddress, // The Signing address
      timestamp: ts,            // The CLOB API server timestamp
      nonce: nonce,             // The nonce used
      message: "This message attests that I control the given wallet",
    };

    const sig = await signer._signTypedData(domain, types, value);
    ```

    ```python Python theme={null}
    domain = {
        "name": "ClobAuthDomain",
        "version": "1",
        "chainId": chainId,  # Polygon Chain ID 137
    }

    types = {
        "ClobAuth": [
            {"name": "address", "type": "address"},
            {"name": "timestamp", "type": "string"},
            {"name": "nonce", "type": "uint256"},
            {"name": "message", "type": "string"},
        ]
    }

    value = {
        "address": signingAddress,  # The signing address
        "timestamp": ts,            # The CLOB API server timestamp
        "nonce": nonce,             # The nonce used
        "message": "This message attests that I control the given wallet",
    }

    sig = await signer._signTypedData(domain, types, value) 
    ```
  </CodeGroup>
</Accordion>

Reference implementations:

* [TypeScript](https://github.com/Polymarket/clob-client/blob/main/src/signing/eip712.ts)
* [Python](https://github.com/Polymarket/py-clob-client/blob/main/py_clob_client/signing/eip712.py)

***

**Create API Credentials**

Create new API credentials for user.

```bash  theme={null}
POST {clob-endpoint}/auth/api-key
```

**Derive API Credentials**

Derive API credentials for user.

```bash  theme={null}
GET {clob-endpoint}/auth/derive-api-key
```

**Response**

```json  theme={null}
{
  "apiKey": "550e8400-e29b-41d4-a716-446655440000",
  "secret": "base64EncodedSecretString",
  "passphrase": "randomPassphraseString"
}
```

**You'll need all three values for L2 authentication.**

***

## L2 Authentication

### What is L2?

The next level of authentication is called L2, and it consists of the
user's API credentials (apiKey, secret, passphrase) generated from L1
authentication. These are used solely to authenticate requests made to
the CLOB API. Requests are signed using HMAC-SHA256.

### What This Enables

Access to L2 methods such as posting signed/created orders, viewing open
orders, cancelling open orders, getting trades

* Cancel or get user's open orders
* Check user's balances and allowances
* Post user's signed orders

### CLOB Client

<Tabs>
  <Tab title="TypeScript">
    ```typescript  theme={null}
    import { ClobClient } from "@polymarket/clob-client";
    import { Wallet } from "ethers"; // v5.8.0

    const HOST = "https://clob.polymarket.com";
    const CHAIN_ID = 137; // Polygon mainnet
    const signer = new Wallet(process.env.PRIVATE_KEY);

    const client = new ClobClient(
      HOST,
      CHAIN_ID,
      signer,
      apiCreds, // Generated from L1 auth, API credentials enable L2 methods
      1, // signatureType explained below
      FUNDER // funder explained below
    );

    // Now you can trade!*
    const order = await client.createAndPostOrder(
      { tokenID: "123456", price: 0.65, size: 100, side: "BUY" },
      { tickSize: "0.01", negRisk: false }
    );
    ```
  </Tab>

  <Tab title="Python">
    ```python  theme={null}
    from py_clob_client.client import ClobClient
    import os

    host = "https://clob.polymarket.com"
    chain_id = 137 # Polygon mainnet
    private_key = os.getenv("PRIVATE_KEY")

    client = ClobClient(
        host="https://clob.polymarket.com",
        chain_id=137,
        key=os.getenv("PRIVATE_KEY"),
        creds=api_creds,  # Generated from L1 auth, API credentials enable L2 methods
        signature_type=1,  # signatureType explained below
        funder=os.getenv("FUNDER_ADDRESS") # funder explained below
    )

    # Now you can trade!*
    order = await client.create_and_post_order(
        {"token_id": "123456", "price": 0.65, "size": 100, "side": "BUY"},
        {"tick_size": "0.01", "neg_risk": False}
    )
    ```
  </Tab>
</Tabs>

<Info>
  Even with L2 authentication headers, methods that create user orders still require the user to sign the order payload.
</Info>

***

### REST API

While we highly recommend using our provided clients to handle signing
and authentication, the following is for developers who choose NOT to
use our [Python](https://github.com/Polymarket/py-clob-client) or
[TypeScript](https://github.com/Polymarket/clob-client) clients.

When making direct REST API calls with L2 authentication, include these headers:

| Header            | Required? | Description                   |
| ----------------- | --------- | ----------------------------- |
| `POLY_ADDRESS`    | yes       | Polygon signer address        |
| `POLY_SIGNATURE`  | yes       | HMAC signature for request    |
| `POLY_TIMESTAMP`  | yes       | Current UNIX timestamp        |
| `POLY_API_KEY`    | yes       | User's API `apiKey` value     |
| `POLY_PASSPHRASE` | yes       | User's API `passphrase` value |

The `POLY_SIGNATURE` for L2 is an HMAC-SHA256 signature created using the user's API credentials `secret` value.
Reference implementations can be found in the [Typescript](https://github.com/Polymarket/clob-client/blob/main/src/signing/hmac.ts)
and [Python](https://github.com/Polymarket/py-clob-client/blob/main/py_clob_client/signing/hmac.py) clients.

***

## Signature Types and Funder

When initializing the L2 client, you must specify your wallet **signatureType** and the **funder** address which holds the funds:

| Signature Type | Value | Description                                                                                                                                                                                  |
| -------------- | ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| EOA            | 0     | Standard Ethereum wallet (MetaMask). Funder is the EOA address and will need POL to pay gas on transactions.                                                                                 |
| POLY\_PROXY    | 1     | A custom proxy wallet only used with users who logged in via Magic Link email/Google. Using this requires the user to have exported their PK from Polymarket.com and imported into your app. |
| GNOSIS\_SAFE   | 2     | Gnosis Safe multisig proxy wallet (most common). Use this for any new or returning user who does not fit the other 2 types.                                                                  |

<Tip>
  The wallet addresses displayed to the user on Polymarket.com is the proxy wallet and should be used as the funder.
  These can be deterministically derived or you can deploy them on behalf of the user.
  These proxy wallets are automatically deployed for the user on their first login to Polymarket.com.
</Tip>

***

## Troubleshooting

<AccordionGroup>
  <Accordion title="Error: INVALID_SIGNATURE">
    Your wallet's private key is incorrect or improperly formatted.

    **Solution:**

    * Verify your private key is a valid hex string (starts with "0x")
    * Ensure you're using the correct key for the intended address
    * Check that the key has proper permissions
  </Accordion>

  <Accordion title="Error: NONCE_ALREADY_USED">
    The nonce you provided has already been used to create an API key.

    **Solution:**

    * Use `deriveApiKey()` with the same nonce to retrieve existing credentials
    * Or use a different nonce with `createApiKey()`
  </Accordion>

  <Accordion title="Error: Invalid Funder Address">
    Your funder address is incorrect or doesn't match your wallet.

    **Solution:** Check your Polymarket profile address at [polymarket.com/settings](https://polymarket.com/settings).

    If it does not exist or user has never logged into Polymarket.com, deploy it first before creating L2 authentication.
  </Accordion>

  <Accordion title="Lost API credentials but have nonce">
    ```typescript  theme={null}
    // Use deriveApiKey with the original nonce
    const recovered = await client.deriveApiKey(originalNonce);
    ```
  </Accordion>

  <Accordion title="Lost both credentials and nonce">
    Unfortunately, there's no way to recover lost API credentials without the nonce. You'll need to create new credentials:

    ```typescript  theme={null}
    // Create fresh credentials with a new nonce
    const newCreds = await client.createApiKey();
    // Save the nonce this time!
    ```
  </Accordion>
</AccordionGroup>

***

## See Client Methods

<CardGroup cols={2}>
  <Card title="Public Methods" icon="globe" href="/developers/CLOB/clients/methods-public">
    Access market data, orderbooks, and prices.
  </Card>

  <Card title="L1 Methods" icon="key" href="/developers/CLOB/clients/methods-l1">
    Private key authentication to create or derive API keys (L2 headers).
  </Card>

  <Card title="L2 Methods" icon="lock" href="/developers/CLOB/clients/methods-l2">
    Manage and close orders. Creating orders requires signer.
  </Card>

  <Card title="Builder Program Methods" icon="hammer" href="/developers/CLOB/clients/methods-builder">
    Builder-specific operations for those in the Builders Program.
  </Card>
</CardGroup>


Skip to main content
Polymarket Documentation home pagedark logo

Search...
Ctrl K

Ask AI
Main Site

User Guide
For Developers
Changelog
Polymarket
Discord Community
Twitter
Developer Quickstart
Developer Quickstart
Fetching Market Data
Placing Your First Order
Glossary
API Rate Limits
Endpoints
Market Makers
Market Maker Introduction
Setup
Trading
Liquidity Rewards
Maker Rebates Program
Data Feeds
Inventory Management
Polymarket Builders Program
Builder Program Introduction
Builder Tiers
Builder Profile & Keys
Order Attribution
Relayer Client
Examples
Central Limit Order Book
CLOB Introduction
Status
Quickstart
Authentication
Geographic Restrictions

Client

REST API

Historical Timeseries Data

Order Management

Trades
Websocket
WSS Overview
WSS Quickstart
WSS Authentication
User Channel
Market Channel

Sports Websocket
Real Time Data Stream
RTDS Overview
RTDS Crypto Prices
RTDS Comments
Gamma Structure
Overview
Gamma Structure
Fetching Markets
Gamma Endpoints

Gamma Status

Sports

Tags

Events

Markets

Series

Comments

Profiles

Search
Data-API

Data API Status

Core

Misc

Builders
Bridge & Swap
Overview

Bridge
Subgraph
Overview
Resolution
Resolution
Conditional Token Frameworks
Overview
Splitting USDC
Merging Tokens
Reedeeming Tokens
Deployment and Additional Information
Proxy Wallets
Proxy wallet
Negative Risk
Overview

On this page
Overview
Server Infrastructure
Geoblock Endpoint
Response
Blocked Countries
Blocked Regions
Usage Examples
Central Limit Order Book
Geographic Restrictions
Check geographic restrictions before placing orders on Polymarket’s CLOB

​
Overview
Polymarket restricts order placement from certain geographic locations due to regulatory requirements and compliance with international sanctions. Before placing orders, builders should verify the location.
Orders submitted from blocked regions will be rejected. Implement geoblock checks in your application to provide users with appropriate feedback before they attempt to trade.
​
Server Infrastructure
Primary Servers: eu-west-2
Closest Non-Georestricted Region: eu-west-1
​
Geoblock Endpoint
Check the geographic eligibility of the requesting IP address:
GET https://polymarket.com/api/geoblock
​
Response
{
  "blocked": boolean;
  "ip": string;
  "country": string;
  "region": string;
}
Field	Type	Description
blocked	boolean	Whether the user is blocked from placing orders
ip	string	Detected IP address
country	string	ISO 3166-1 alpha-2 country code
region	string	Region/state code
​
Blocked Countries
The following 33 countries are completely restricted from placing orders on Polymarket:
Country Code	Country Name
AU	Australia
BE	Belgium
BY	Belarus
BI	Burundi
CF	Central African Republic
CD	Congo (Kinshasa)
CU	Cuba
DE	Germany
ET	Ethiopia
FR	France
GB	United Kingdom
IR	Iran
IQ	Iraq
IT	Italy
KP	North Korea
LB	Lebanon
LY	Libya
MM	Myanmar
NI	Nicaragua
PL	Poland
RU	Russia
SG	Singapore
SO	Somalia
SS	South Sudan
SD	Sudan
SY	Syria
TH	Thailand
TW	Taiwan
UM	United States Minor Outlying Islands
US	United States
VE	Venezuela
YE	Yemen
ZW	Zimbabwe
​
Blocked Regions
In addition to fully blocked countries, the following specific regions within otherwise accessible countries are also restricted:
Country	Region	Region Code
Canada (CA)	Ontario	ON
Ukraine (UA)	Crimea	43
Ukraine (UA)	Donetsk	14
Ukraine (UA)	Luhansk	09
​
Usage Examples
TypeScript
Python
interface GeoblockResponse {
  blocked: boolean;
  ip: string;
  country: string;
  region: string;
}

async function checkGeoblock(): Promise<GeoblockResponse> {
  const response = await fetch("https://polymarket.com/api/geoblock");
  return response.json();
}

// Usage
const geo = await checkGeoblock();

if (geo.blocked) {
  console.log(`Trading not available in ${geo.country}`);
} else {
  console.log("Trading available");
}
Authentication
Methods Overview
Ask a question...

github
Powered by
Geographic Restrictions - Polymarket Documentation

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.polymarket.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Methods Overview

> CLOB client methods require different levels of authentication. This reference is organized by what credentials you need to call each method. 

<CardGroup cols={2}>
  <Card title="Public Methods" icon="globe" href="/developers/CLOB/clients/methods-public">
    Access market data, orderbooks, and prices.
  </Card>

  <Card title="L1 Methods" icon="key" href="/developers/CLOB/clients/methods-l1">
    Private key authentication to create or derive API keys (L2 headers).
  </Card>

  <Card title="L2 Methods" icon="lock" href="/developers/CLOB/clients/methods-l2">
    Manage and close orders. Creating orders requires signer.
  </Card>

  <Card title="Builder Program Methods" icon="hammer" href="/developers/CLOB/clients/methods-builder">
    Builder-specific operations for those in the Builders Program.
  </Card>
</CardGroup>

***

## Client Initialization by Use Case

<Tabs>
  <Tab title="Get Market Data">
    <CodeGroup>
      ```typescript TypeScript theme={null}
      // No signer or credentials needed
      const client = new ClobClient(
        "https://clob.polymarket.com", 
        137
      );

      // All public methods available
      const markets = await client.getMarkets();
      const book = await client.getOrderBook(tokenId);
      const price = await client.getPrice(tokenId, "BUY");
      ```

      ```python Python theme={null}
      # No signer or credentials needed
      client = new ClobClient(
          host="https://clob.polymarket.com", 
          chain_id=137
      )

      # All public methods available
      markets = client.get_markets()
      book = client.get_order_book()
      price = client.get_price()
      ```
    </CodeGroup>
  </Tab>

  <Tab title="Generate User API Credentials">
    <CodeGroup>
      ```typescript TypeScript theme={null}
      // Create client with signer
      const client = new ClobClient(
        "https://clob.polymarket.com", 
        137, 
        signer
      );

      // All public and L1 methods available
      const newCreds = createApiKey();
      const derivedCreds = deriveApiKey();
      const creds = createOrDeriveApiKey();
      ```

      ```python Python theme={null}
      # Create client with signer
      client = new ClobClient(
          host="https://clob.polymarket.com", 
          chain_id=137
          key="private_key"
        )

      # All public and L1 methods available
      new_creds = client.create_api_key()
      derived_creds = client.derive_api_key()
      creds = client.create_or_derive_api_key()
      ```
    </CodeGroup>
  </Tab>

  <Tab title="Create and Post Order">
    <CodeGroup>
      ```typescript TypeScript theme={null}
      // Create client with signer and creds
      const client = new ClobClient(
        "https://clob.polymarket.com", 
        137, 
        signer,
        creds,
        2, // Indicates Gnosis Safe proxy
        funder // Safe wallet address holding funds
      );

      // All public, L1, and L2 methods available
      const order = await client.createOrder({ /* ... */ });
      const result = await client.postOrder(order);
      const trades = await client.getTrades();
      ```

      ```python Python theme={null}
      # Create client with signer and creds
      const client = new ClobClient(
          host="https://clob.polymarket.com",
          chain_id=137,
          key="private_key",
          creds=creds,
          signature_type=2, // Indicates Gnosis Safe proxy
          funder="funder_address" // Safe wallet address holding funds
      )

      # All public, L1, and L2 methods available
      order = client.create_order({ /* ... */ })
      result = client.post_order(order)
      trades = client.get_trades()
      ```
    </CodeGroup>
  </Tab>

  <Tab title="Get Builders Orders">
    <CodeGroup>
      ```typescript TypeScript theme={null}
      // Create client with builder's authentication headers
      import { BuilderConfig, BuilderApiKeyCreds } from "@polymarket/builder-signing-sdk";

      const builderCreds: BuilderApiKeyCreds = {
        key: process.env.POLY_BUILDER_API_KEY!,
        secret: process.env.POLY_BUILDER_SECRET!,
        passphrase: process.env.POLY_BUILDER_PASSPHRASE!
      };

      const builderConfig: BuilderConfig = {
        localBuilderCreds: builderCreds
      };

      const client = new ClobClient(
        "https://clob.polymarket.com", 
        137, 
        signer,
        creds, // User's API credentials
        2,
        funder,
        undefined,
        false,
        builderConfig // Builder's API credentials
      );

      // You can call all methods including builder methods
      const builderTrades = await client.getBuilderTrades();
      ```

      ```python Python theme={null}
      # Create client with builder's authentication headers
      from py_clob_client.client import ClobClient
      from py_clob_client.clob_types import ApiCreds
      from py_builder_signing_sdk.config import BuilderConfig, BuilderApiKeyCreds

      builder_creds = BuilderApiKeyCreds(
          key="POLY_BUILDER_API_KEY",
          secret="POLY_BUILDER_SECRET,
          passphrase="POLY_BUILDER_PASSPHRASE"
      )

      builder_config = BuilderConfig(
          local_builder_creds=builder_creds
      )

      client = ClobClient(
          host="https://clob.polymarket.com",
          chain_id=137,
          key="private_key",
          creds=creds, # User's API credentials
          signature_type=2,
          funder=funder_address,
          builder_config=builder_config # Builder's API credentials
      )

      # You can call all methods including builder methods
      builder_trades = client.get_builder_trades()
      ```
    </CodeGroup>

    Learn more about the Builders Program and Relay Client here
  </Tab>
</Tabs>

***

## Resources

<CardGroup cols={2}>
  <Card title="TypeScript Client" icon="github" href="https://github.com/Polymarket/clob-client">
    Open source TypeScript client on GitHub
  </Card>

  <Card title="Python Client" icon="github" href="https://github.com/Polymarket/py-clob-client">
    Open source Python client for GitHub
  </Card>

  <Card title="TypeScript Examples" icon="code" href="https://github.com/Polymarket/clob-client/tree/main/examples">
    TypeScript client method examples
  </Card>

  <Card title="Python Examples" icon="python" href="https://github.com/Polymarket/py-clob-client/tree/main/examples">
    Python client method examples
  </Card>

  <Card title="CLOB Rest API Reference" icon="hammer" href="/api-reference/orderbook/get-order-book-summary">
    Complete REST endpoint documentation
  </Card>

  <Card title="Web Socket API" icon="hammer" href="/developers/CLOB/websocket/wss-overview">
    Real-time market data streaming
  </Card>
</CardGroup>


Skip to main content
Polymarket Documentation home pagedark logo

Search...
Ctrl K

Ask AI
Main Site

User Guide
For Developers
Changelog
Polymarket
Discord Community
Twitter
Developer Quickstart
Developer Quickstart
Fetching Market Data
Placing Your First Order
Glossary
API Rate Limits
Endpoints
Market Makers
Market Maker Introduction
Setup
Trading
Liquidity Rewards
Maker Rebates Program
Data Feeds
Inventory Management
Polymarket Builders Program
Builder Program Introduction
Builder Tiers
Builder Profile & Keys
Order Attribution
Relayer Client
Examples
Central Limit Order Book
CLOB Introduction
Status
Quickstart
Authentication
Geographic Restrictions

Client
Methods Overview
Public Methods
L1 Methods
L2 Methods
Builder Methods

REST API

Historical Timeseries Data

Order Management

Trades
Websocket
WSS Overview
WSS Quickstart
WSS Authentication
User Channel
Market Channel

Sports Websocket
Real Time Data Stream
RTDS Overview
RTDS Crypto Prices
RTDS Comments
Gamma Structure
Overview
Gamma Structure
Fetching Markets
Gamma Endpoints

Gamma Status

Sports

Tags

Events

Markets

Series

Comments

Profiles

Search
Data-API

Data API Status

Core

Misc

Builders
Bridge & Swap
Overview

Bridge
Subgraph
Overview
Resolution
Resolution
Conditional Token Frameworks
Overview
Splitting USDC
Merging Tokens
Reedeeming Tokens
Deployment and Additional Information
Proxy Wallets
Proxy wallet
Negative Risk
Overview

On this page
Client Initialization
Health Check
getOk()
Markets
getMarket()
getMarkets()
getSimplifiedMarkets()
getSamplingMarkets()
getSamplingSimplifiedMarkets()
Order Books and Prices
calculateMarketPrice()
getOrderBook()
getOrderBooks()
getPrice()
getPrices()
getMidpoint()
getMidpoints()
getSpread()
getSpreads()
getPricesHistory()
Trades
getLastTradePrice()
getLastTradesPrices()
getMarketTradesEvents
Market Parameters
getFeeRateBps()
getTickSize()
getNegRisk()
Time & Server Info
getServerTime()
See Also
Client
Public Methods
These methods can be called without a signer or user credentials. Use these for reading market data, prices, and order books.

​
Client Initialization
Public methods require the client to initialize with the host URL and Polygon chain ID.
TypeScript
Python
import { ClobClient } from "@polymarket/clob-client";

const client = new ClobClient(
  "https://clob.polymarket.com",
  137
);

// Ready to call public methods
const markets = await client.getMarkets();
​
Health Check
​
getOk()
Health check endpoint to verify the CLOB service is operational.
Signature
async getOk(): Promise<any>
​
Markets
​
getMarket()
Get details for a single market by condition ID.
Signature
async getMarket(conditionId: string): Promise<Market>
Response
interface MarketToken {
  outcome: string;
  price: number;
  token_id: string;
  winner: boolean;
}

interface Market {
  accepting_order_timestamp: string | null;
  accepting_orders: boolean;
  active: boolean;
  archived: boolean;
  closed: boolean;
  condition_id: string;
  description: string;
  enable_order_book: boolean;
  end_date_iso: string;
  fpmm: string;
  game_start_time: string;
  icon: string;
  image: string;
  is_50_50_outcome: boolean;
  maker_base_fee: number;
  market_slug: string;
  minimum_order_size: number;
  minimum_tick_size: number;
  neg_risk: boolean;
  neg_risk_market_id: string;
  neg_risk_request_id: string;
  notifications_enabled: boolean;
  question: string;
  question_id: string;
  rewards: {
    max_spread: number;
    min_size: number;
    rates: any | null;
  };
  seconds_delay: number;
  tags: string[];
  taker_base_fee: number;
  tokens: MarketToken[];
}
​
getMarkets()
Get details for multiple markets paginated.
Signature
async getMarkets(): Promise<PaginationPayload>
Response
interface PaginationPayload {
  limit: number;
  count: number;
  data: Market[];
}

interface Market {
  accepting_order_timestamp: string | null;
  accepting_orders: boolean;
  active: boolean;
  archived: boolean;
  closed: boolean;
  condition_id: string;
  description: string;
  enable_order_book: boolean;
  end_date_iso: string;
  fpmm: string;
  game_start_time: string;
  icon: string;
  image: string;
  is_50_50_outcome: boolean;
  maker_base_fee: number;
  market_slug: string;
  minimum_order_size: number;
  minimum_tick_size: number;
  neg_risk: boolean;
  neg_risk_market_id: string;
  neg_risk_request_id: string;
  notifications_enabled: boolean;
  question: string;
  question_id: string;
  rewards: {
    max_spread: number;
    min_size: number;
    rates: any | null;
  };
  seconds_delay: number;
  tags: string[];
  taker_base_fee: number;
  tokens: MarketToken[];
}

interface MarketToken {
  outcome: string;
  price: number;
  token_id: string;
  winner: boolean;
}
​
getSimplifiedMarkets()
Get simplified market data paginated for faster loading.
Signature
async getSimplifiedMarkets(): Promise<PaginationPayload>
Response
interface PaginationPayload {
  limit: number;
  count: number;
  data: SimplifiedMarket[];
}

interface SimplifiedMarket {
  accepting_orders: boolean;
  active: boolean;
  archived: boolean;
  closed: boolean;
  condition_id: string;
  rewards: {
    rates: any | null;
    min_size: number;
    max_spread: number;
  };
    tokens: SimplifiedToken[];
}

interface SimplifiedToken {
  outcome: string;
  price: number;
  token_id: string;
}
​
getSamplingMarkets()
Signature
async getSamplingMarkets(): Promise<PaginationPayload>
Response
interface PaginationPayload {
  limit: number;
  count: number;
  data: Market[];
}

interface Market {
  accepting_order_timestamp: string | null;
  accepting_orders: boolean;
  active: boolean;
  archived: boolean;
  closed: boolean;
  condition_id: string;
  description: string;
  enable_order_book: boolean;
  end_date_iso: string;
  fpmm: string;
  game_start_time: string;
  icon: string;
  image: string;
  is_50_50_outcome: boolean;
  maker_base_fee: number;
  market_slug: string;
  minimum_order_size: number;
  minimum_tick_size: number;
  neg_risk: boolean;
  neg_risk_market_id: string;
  neg_risk_request_id: string;
  notifications_enabled: boolean;
  question: string;
  question_id: string;
  rewards: {
    max_spread: number;
    min_size: number;
    rates: any | null;
  };
  seconds_delay: number;
  tags: string[];
  taker_base_fee: number;
  tokens: MarketToken[];
}

interface MarketToken {
  outcome: string;
  price: number;
  token_id: string;
  winner: boolean;
}
​
getSamplingSimplifiedMarkets()
Signature
async getSamplingSimplifiedMarkets(): Promise<PaginationPayload>
Response
interface PaginationPayload {
  limit: number;
  count: number;
  data: SimplifiedMarket[];
}

interface SimplifiedMarket {
  accepting_orders: boolean;
  active: boolean;
  archived: boolean;
  closed: boolean;
  condition_id: string;
  rewards: {
    rates: any | null;
    min_size: number;
    max_spread: number;
  };
    tokens: SimplifiedToken[];
}

interface SimplifiedToken {
  outcome: string;
  price: number;
  token_id: string;
}
​
Order Books and Prices
​
calculateMarketPrice()
Signature
async calculateMarketPrice(
  tokenID: string,
  side: Side,
  amount: number,
  orderType: OrderType = OrderType.FOK
): Promise<number>
Params
enum OrderType {
  GTC = "GTC",  // Good Till Cancelled
  FOK = "FOK",  // Fill or Kill
  GTD = "GTD",  // Good Till Date
  FAK = "FAK",  // Fill and Kill
}

enum Side {
  BUY = "BUY",
  SELL = "SELL",
}
Response
number // calculated market price
​
getOrderBook()
Get the order book for a specific token ID.
Signature
async getOrderBook(tokenID: string): Promise<OrderBookSummary>
Response
interface OrderBookSummary {
  market: string;
  asset_id: string;
  timestamp: string;
  bids: OrderSummary[];
  asks: OrderSummary[];
  min_order_size: string;
  tick_size: string;
  neg_risk: boolean;
  hash: string;
}

interface OrderSummary {
  price: string;
  size: string;
}
​
getOrderBooks()
Get order books for multiple token IDs.
Signature
async getOrderBooks(params: BookParams[]): Promise<OrderBookSummary[]>
Params
interface BookParams {
  token_id: string;
  side: Side;  // Side.BUY or Side.SELL
}
Response
OrderBookSummary[]
​
getPrice()
Get the current best price for buying or selling a token ID.
Signature
async getPrice(
  tokenID: string,
  side: "BUY" | "SELL"
): Promise<any>
Response
{
  price: string;
}
​
getPrices()
Get the current best prices for multiple token IDs.
Signature
async getPrices(params: BookParams[]): Promise<PricesResponse>
Params
interface BookParams {
  token_id: string;
  side: Side;  // Side.BUY or Side.SELL
}
Response
interface TokenPrices {
  BUY?: string;
  SELL?: string;
}

type PricesResponse = {
  [tokenId: string]: TokenPrices;
}
​
getMidpoint()
Get the midpoint price (average of best bid and best ask) for a token ID.
Signature
async getMidpoint(tokenID: string): Promise<any>
Response
{
  mid: string;
}
​
getMidpoints()
Get the midpoint prices (average of best bid and best ask) for multiple token IDs.
Signature
async getMidpoints(params: BookParams[]): Promise<any>
Params
interface BookParams {
  token_id: string;
  side: Side;  // Side is ignored
}
Response
{
  [tokenId: string]: string;
}
​
getSpread()
Get the spread (difference between best ask and best bid) for a token ID.
Signature
async getSpread(tokenID: string): Promise<SpreadResponse>
Response
interface SpreadResponse {
  spread: string;
}
​
getSpreads()
Get the spreads (difference between best ask and best bid) for multiple token IDs.
Signature
async getSpreads(params: BookParams[]): Promise<SpreadsResponse>
Params
interface BookParams {
  token_id: string;
  side: Side;
}
Response
type SpreadsResponse = {
  [tokenId: string]: string;
}
​
getPricesHistory()
Get historical price data for a token.
Signature
async getPricesHistory(params: PriceHistoryFilterParams): Promise<MarketPrice[]>
Params
interface PriceHistoryFilterParams {
  market: string; // tokenID
  startTs?: number;
  endTs?: number;
  fidelity?: number;
  interval: PriceHistoryInterval;
}

enum PriceHistoryInterval {
  MAX = "max",
  ONE_WEEK = "1w",
  ONE_DAY = "1d",
  SIX_HOURS = "6h",
  ONE_HOUR = "1h",
}
Response
interface MarketPrice {
  t: number;  // timestamp
  p: number;  // price
}
​
Trades
​
getLastTradePrice()
Get the price of the most recent trade for a token.
Signature
async getLastTradePrice(tokenID: string): Promise<LastTradePrice>
Response
interface LastTradePrice {
  price: string;
  side: string;
}
​
getLastTradesPrices()
Get the price of the most recent trade for a token.
Signature
async getLastTradesPrices(params: BookParams[]): Promise<LastTradePriceWithToken[]>
Params
interface BookParams {
  token_id: string;
  side: Side;
}
Response
interface LastTradePriceWithToken {
  price: string;
  side: string;
  token_id: string;
}
​
getMarketTradesEvents
Signature
async getMarketTradesEvents(conditionID: string): Promise<MarketTradeEvent[]>
Response
interface MarketTradeEvent {
  event_type: string;
  market: {
    condition_id: string;
    asset_id: string;
    question: string;
    icon: string;
    slug: string;
  };
  user: {
    address: string;
    username: string;
    profile_picture: string;
    optimized_profile_picture: string;
    pseudonym: string;
  };
  side: Side;
  size: string;
  fee_rate_bps: string;
  price: string;
  outcome: string;
  outcome_index: number;
  transaction_hash: string;
  timestamp: string;
}
​
Market Parameters
​
getFeeRateBps()
Get the fee rate in basis points for a token.
Signature
async getFeeRateBps(tokenID: string): Promise<number>
Response
number
​
getTickSize()
Get the tick size (minimum price increment) for a market.
Signature
async getTickSize(tokenID: string): Promise<TickSize>
Response
type TickSize = "0.1" | "0.01" | "0.001" | "0.0001";
​
getNegRisk()
Check if a market uses negative risk (binary complementary tokens).
Signature
async getNegRisk(tokenID: string): Promise<boolean>
Response
boolean
​
Time & Server Info
​
getServerTime()
Get the current server timestamp.
Signature
async getServerTime(): Promise<number>
Response
number // Unix timestamp in seconds
​
See Also
L1 Methods
Private key authentication to create or derive API keys (L2 headers).
L2 Methods
Manage and close orders. Creating orders requires signer.
CLOB Rest API Reference
Complete REST endpoint documentation
Web Socket API
Real-time market data streaming
Methods Overview
L1 Methods
Ask a question...

github
Powered by
Public Methods - Polymarket Documentation

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.polymarket.com/llms.txt
> Use this file to discover all available pages before exploring further.

# L1 Methods

> These methods require a wallet signer (private key) but do not require user API credentials. Use these for initial setup.

## Client Initialization

L1 methods require the client to initialize with a signer.

<Tabs>
  <Tab title="TypeScript">
    ```typescript  theme={null}
    import { ClobClient } from "@polymarket/clob-client";
    import { Wallet } from "ethers";

    const signer = new Wallet(process.env.PRIVATE_KEY);

    const client = new ClobClient(
      "https://clob.polymarket.com",
      137,
      signer // Signer required for L1 methods
    );

    // Ready to create user API credentials
    const apiKey = await client.createApiKey();
    ```
  </Tab>

  <Tab title="Python">
    ```python  theme={null}
    from py_clob_client.client import ClobClient
    import os

    private_key = os.getenv("PRIVATE_KEY")

    client = ClobClient(
        host="https://clob.polymarket.com",
        chain_id=137,
        key=private_key  # Signer required for L1 methods
    )

    # Ready to create user API credentials
    api_key = await client.create_api_key()
    ```
  </Tab>
</Tabs>

<Warning>
  **Security:** Never commit private keys to version control. Always use environment variables or secure key management systems.
</Warning>

***

## API Key Management

***

### createApiKey()

Creates a new API key (L2 credentials) for the wallet signer. This generates a new set of credentials that can be used for L2 authenticated requests.
Each wallet can only have one active API key at a time. Creating a new key invalidates the previous one.

```typescript Signature theme={null}
async createApiKey(nonce?: number): Promise<ApiKeyCreds>
```

```typescript Params theme={null}
`nonce` (optional): Custom nonce for deterministic key generation. If not provided, a default derivation is used.
```

```typescript Response theme={null}
interface ApiKeyCreds {
  apiKey: string;
  secret: string;
  passphrase: string;
}
```

***

### deriveApiKey()

Derives an existing API key (L2 credentials) using a specific nonce. If you've already created API credentials with a particular nonce, this method will return the same credentials again.

```typescript Signature theme={null}
async deriveApiKey(nonce?: number): Promise<ApiKeyCreds>
```

```typescript Params theme={null}
`nonce` (optional): Custom nonce for deterministic key generation. If not provided, a default derivation is used.
```

```typescript Response theme={null}
interface ApiKeyCreds {
  apiKey: string;
  secret: string;
  passphrase: string;
}
```

***

### createOrDeriveApiKey()

Convenience method that attempts to derive an API key with the default nonce, or creates a new one if it doesn't exist. This is the recommended method for initial setup if you're unsure if credentials already exist.

```typescript Signature theme={null}
async createOrDeriveApiKey(nonce?: number): Promise<ApiKeyCreds>
```

```typescript Params theme={null}
`nonce` (optional): Custom nonce for deterministic key generation. If not provided, a default derivation is used.
```

```typescript Response theme={null}
interface ApiKeyCreds {
  apiKey: string;
  secret: string;
  passphrase: string;
}
```

***

## Order Signing

### createOrder()

Create and sign a limit order locally without posting it to the CLOB.
Use this when you want to sign orders in advance or implement custom order submission logic.
Place order via L2 methods postOrder or postOrders.

```typescript Signature theme={null}
async createOrder(
  userOrder: UserOrder,
  options?: Partial<CreateOrderOptions>
): Promise<SignedOrder>
```

```typescript Params theme={null}
interface UserOrder {
  tokenID: string;
  price: number;
  size: number;
  side: Side;
  feeRateBps?: number;
  nonce?: number;
  expiration?: number;
  taker?: string;
}

interface CreateOrderOptions {
  tickSize: TickSize;
  negRisk?: boolean;
}
```

```typescript Response theme={null}
interface SignedOrder {
  salt: string;
  maker: string;
  signer: string;
  taker: string;
  tokenId: string;
  makerAmount: string;
  takerAmount: string;
  side: number;  // 0 = BUY, 1 = SELL
  expiration: string;
  nonce: string;
  feeRateBps: string;
  signatureType: number;
  signature: string;
}
```

***

### createMarketOrder()

Create and sign a market order locally without posting it to the CLOB.
Use this when you want to sign orders in advance or implement custom order submission logic.
Place orders via L2 methods postOrder or postOrders.

```typescript Signature theme={null}
async createMarketOrder(
  userMarketOrder: UserMarketOrder,
  options?: Partial<CreateOrderOptions>
): Promise<SignedOrder>
```

```typescript Params theme={null}
interface UserMarketOrder {
  tokenID: string;
  amount: number;  // BUY: dollar amount, SELL: number of shares
  side: Side;
  price?: number;  // Optional price limit
  feeRateBps?: number;
  nonce?: number;
  taker?: string;
  orderType?: OrderType.FOK | OrderType.FAK;
}
```

```typescript Response theme={null}
interface SignedOrder {
  salt: string;
  maker: string;
  signer: string;
  taker: string;
  tokenId: string;
  makerAmount: string;
  takerAmount: string;
  side: number;  // 0 = BUY, 1 = SELL
  expiration: string;
  nonce: string;
  feeRateBps: string;
  signatureType: number;
  signature: string;
}
```

***

## Troubleshooting

<AccordionGroup>
  <Accordion title="Error: INVALID_SIGNATURE">
    Your wallet's private key is incorrect or improperly formatted.

    **Solution:**

    * Verify your private key is a valid hex string (starts with "0x")
    * Ensure you're using the correct key for the intended address
    * Check that the key has proper permissions
  </Accordion>

  <Accordion title="Error: NONCE_ALREADY_USED">
    The nonce you provided has already been used to create an API key.

    **Solution:**

    * Use `deriveApiKey()` with the same nonce to retrieve existing credentials
    * Or use a different nonce with `createApiKey()`
  </Accordion>

  <Accordion title="Error: Invalid Funder Address">
    Your funder address is incorrect or doesn't match your wallet.

    **Solution:** Check your Polymarket profile address at [polymarket.com/settings](https://polymarket.com/settings).

    If it does not exist or user has never logged into Polymarket.com, deploy it first before creating L2 authentication.
  </Accordion>

  <Accordion title="Lost API credentials but have nonce">
    ```typescript  theme={null}
    // Use deriveApiKey with the original nonce
    const recovered = await client.deriveApiKey(originalNonce);
    ```
  </Accordion>

  <Accordion title="Lost both credentials and nonce">
    Unfortunately, there's no way to recover lost API credentials without the nonce. You'll need to create new credentials:

    ```typescript  theme={null}
    // Create fresh credentials with a new nonce
    const newCreds = await client.createApiKey();
    // Save the nonce this time!
    ```
  </Accordion>
</AccordionGroup>

***

## See Also

<CardGroup cols={2}>
  <Card title="Understand CLOB Authentication" icon="shield" href="/developers/CLOB/authentication">
    Deep dive into L1 and L2 authentication
  </Card>

  <Card title="CLOB Quickstart Guide" icon="hammer" href="/developers/CLOB/quickstart">
    Initialize the CLOB quickly and place your first order.
  </Card>

  <Card title="Public Methods" icon="globe" href="/developers/CLOB/clients/methods-l2">
    Access market data, orderbooks, and prices.
  </Card>

  <Card title="L2 Methods" icon="lock" href="/developers/CLOB/clients/methods-l2">
    Manage and close orders. Creating orders requires signer.
  </Card>
</CardGroup>


Skip to main content
Polymarket Documentation home pagedark logo

Search...
Ctrl K

Ask AI
Main Site

User Guide
For Developers
Changelog
Polymarket
Discord Community
Twitter
Developer Quickstart
Developer Quickstart
Fetching Market Data
Placing Your First Order
Glossary
API Rate Limits
Endpoints
Market Makers
Market Maker Introduction
Setup
Trading
Liquidity Rewards
Maker Rebates Program
Data Feeds
Inventory Management
Polymarket Builders Program
Builder Program Introduction
Builder Tiers
Builder Profile & Keys
Order Attribution
Relayer Client
Examples
Central Limit Order Book
CLOB Introduction
Status
Quickstart
Authentication
Geographic Restrictions

Client
Methods Overview
Public Methods
L1 Methods
L2 Methods
Builder Methods

REST API

Historical Timeseries Data

Order Management

Trades
Websocket
WSS Overview
WSS Quickstart
WSS Authentication
User Channel
Market Channel

Sports Websocket
Real Time Data Stream
RTDS Overview
RTDS Crypto Prices
RTDS Comments
Gamma Structure
Overview
Gamma Structure
Fetching Markets
Gamma Endpoints

Gamma Status

Sports

Tags

Events

Markets

Series

Comments

Profiles

Search
Data-API

Data API Status

Core

Misc

Builders
Bridge & Swap
Overview

Bridge
Subgraph
Overview
Resolution
Resolution
Conditional Token Frameworks
Overview
Splitting USDC
Merging Tokens
Reedeeming Tokens
Deployment and Additional Information
Proxy Wallets
Proxy wallet
Negative Risk
Overview

On this page
Client Initialization
Order Creation and Management
createAndPostOrder()
createAndPostMarketOrder()
postOrder()
postOrders()
cancelOrder()
cancelOrders()
cancelAll()
cancelMarketOrders()
Order and Trade Queries
getOrder()
getOpenOrders()
getTrades()
getTradesPaginated()
Balance and Allowances
getBalanceAllowance()
updateBalanceAllowance()
API Key Management (L2)
getApiKeys()
deleteApiKey()
Notifications
getNotifications()
dropNotifications()
See Also
Client
L2 Methods
These methods require user API credentials (L2 headers). Use these for placing trades and managing user’s positions.

​
Client Initialization
L2 methods require the client to initialize with the signer, signatureType, user API credentials, and funder.
TypeScript
Python
import { ClobClient } from "@polymarket/clob-client";
import { Wallet } from "ethers";

const signer = new Wallet(process.env.PRIVATE_KEY)

const apiCreds = {
  apiKey: process.env.API_KEY,
  secret: process.env.SECRET,
  passphrase: process.env.PASSPHRASE,
};

const client = new ClobClient(
  "https://clob.polymarket.com",
  137,
  signer,
  apiCreds,
  2, // Deployed Safe proxy wallet
  process.env.FUNDER_ADDRESS // Address of deployed Safe proxy wallet
);

// Ready to send authenticated requests to the CLOB API!
const order = await client.postOrder(signedOrder);
​
Order Creation and Management
​
createAndPostOrder()
A convenience method that creates, prompts signature, and posts an order in a single call. Use when you want to buy/sell at a specific price and can wait.
Signature
async createAndPostOrder(
  userOrder: UserOrder,
  options?: Partial<CreateOrderOptions>,
  orderType?: OrderType.GTC | OrderType.GTD, // Defaults to GTC
): Promise<OrderResponse>
Params
interface UserOrder {
  tokenID: string;
  price: number;
  size: number;
  side: Side;
  feeRateBps?: number;
  nonce?: number;
  expiration?: number;
  taker?: string;
}

type CreateOrderOptions = {
  tickSize: TickSize;
  negRisk?: boolean;
}

type TickSize = "0.1" | "0.01" | "0.001" | "0.0001";
Response
interface OrderResponse {
  success: boolean;
  errorMsg: string;
  orderID: string;
  transactionsHashes: string[];
  status: string;
  takingAmount: string;
  makingAmount: string;
}
​
createAndPostMarketOrder()
A convenience method that creates, prompts signature, and posts an order in a single call. Use when you want to buy/sell right now at whatever the market price is.
Signature
async createAndPostMarketOrder(
  userMarketOrder: UserMarketOrder,
  options?: Partial<CreateOrderOptions>,
  orderType?: OrderType.FOK | OrderType.FAK, // Defaults to FOK
): Promise<OrderResponse>
Params
interface UserMarketOrder {
  tokenID: string;
  amount: number;
  side: Side;
  price?: number;
  feeRateBps?: number;
  nonce?: number;
  taker?: string;
  orderType?: OrderType.FOK | OrderType.FAK;
}

type CreateOrderOptions = {
  tickSize: TickSize;
  negRisk?: boolean;
}

type TickSize = "0.1" | "0.01" | "0.001" | "0.0001";
Response
interface OrderResponse {
  success: boolean;
  errorMsg: string;
  orderID: string;
  transactionsHashes: string[];
  status: string;
  takingAmount: string;
  makingAmount: string;
}
​
postOrder()
Posts a pre-signed and created order to the CLOB.
Signature
async postOrder(
  order: SignedOrder,
  orderType?: OrderType, // Defaults to GTC
  postOnly?: boolean, // Defaults to false
): Promise<OrderResponse>
Params
order: SignedOrder  // Pre-signed order from createOrder() or createMarketOrder()
orderType?: OrderType  // Optional, defaults to GTC
postOnly?: boolean  // Optional, defaults to false
Response
interface OrderResponse {
  success: boolean;
  errorMsg: string;
  orderID: string;
  transactionsHashes: string[];
  status: string;
  takingAmount: string;
  makingAmount: string;
}
​
postOrders()
Posts up to 15 pre-signed and created orders in a single batch.
async postOrders(
  args: PostOrdersArgs[],
): Promise<OrderResponse[]>
Params
interface PostOrdersArgs {
  order: SignedOrder;
  orderType: OrderType;
  postOnly?: boolean; // Defaults to false
}
Response
OrderResponse[]  // Array of OrderResponse objects

interface OrderResponse {
  success: boolean;
  errorMsg: string;
  orderID: string;
  transactionsHashes: string[];
  status: string;
  takingAmount: string;
  makingAmount: string;
}
​
cancelOrder()
Cancels a single open order.
Signature
async cancelOrder(orderID: string): Promise<CancelOrdersResponse>
Response
interface CancelOrdersResponse {
  canceled: string[];
  not_canceled: Record<string, any>;
}
​
cancelOrders()
Cancels multiple orders in a single batch.
Signature
async cancelOrders(orderIDs: string[]): Promise<CancelOrdersResponse>
Params
orderIDs: string[];
Response
interface CancelOrdersResponse {
  canceled: string[];
  not_canceled: Record<string, any>;
}
​
cancelAll()
Cancels all open orders.
Signature
async cancelAll(): Promise<CancelResponse>
Response
interface CancelOrdersResponse {
  canceled: string[];
  not_canceled: Record<string, any>;
}
​
cancelMarketOrders()
Cancels all open orders for a specific market.
Signature
async cancelMarketOrders(
  payload: OrderMarketCancelParams
): Promise<CancelOrdersResponse>
Parameters
interface OrderMarketCancelParams {
  market?: string;
  asset_id?: string;
}
Response
interface CancelOrdersResponse {
  canceled: string[];
  not_canceled: Record<string, any>;
}
​
Order and Trade Queries
​
getOrder()
Get details for a specific order.
Signature
async getOrder(orderID: string): Promise<OpenOrder>
Response
interface OpenOrder {
  id: string;
  status: string;
  owner: string;
  maker_address: string;
  market: string;
  asset_id: string;
  side: string;
  original_size: string;
  size_matched: string;
  price: string;
  associate_trades: string[];
  outcome: string;
  created_at: number;
  expiration: string;
  order_type: string;
}
​
getOpenOrders()
Get all your open orders.
Signature
async getOpenOrders(
  params?: OpenOrderParams,
  only_first_page?: boolean,
): Promise<OpenOrdersResponse>
Params
interface OpenOrderParams {
  id?: string; // Order ID
  market?: string; // Market condition ID
  asset_id?: string; // Token ID
}

only_first_page?: boolean  // Defaults to false
Response
type OpenOrdersResponse = OpenOrder[];

interface OpenOrder {
  id: string;
  status: string;
  owner: string;
  maker_address: string;
  market: string;
  asset_id: string;
  side: string;
  original_size: string;
  size_matched: string;
  price: string;
  associate_trades: string[];
  outcome: string;
  created_at: number;
  expiration: string;
  order_type: string;
}
​
getTrades()
Get your trade history (filled orders).
Signature
async getTrades(
  params?: TradeParams,
  only_first_page?: boolean,
): Promise<Trade[]>
Params
interface TradeParams {
  id?: string;
  maker_address?: string;
  market?: string;
  asset_id?: string;
  before?: string;
  after?: string;
}

only_first_page?: boolean  // Defaults to false
Response
interface Trade {
  id: string;
  taker_order_id: string;
  market: string;
  asset_id: string;
  side: Side;
  size: string;
  fee_rate_bps: string;
  price: string;
  status: string;
  match_time: string;
  last_update: string;
  outcome: string;
  bucket_index: number;
  owner: string;
  maker_address: string;
  maker_orders: MakerOrder[];
  transaction_hash: string;
  trader_side: "TAKER" | "MAKER";
}

interface MakerOrder {
  order_id: string;
  owner: string;
  maker_address: string;
  matched_amount: string;
  price: string;
  fee_rate_bps: string;
  asset_id: string;
  outcome: string;
  side: Side;
}
​
getTradesPaginated()
Get trade history with pagination for large result sets.
Signature
async getTradesPaginated(
  params?: TradeParams,
): Promise<TradesPaginatedResponse>
Params
interface TradeParams {
  id?: string;
  maker_address?: string;
  market?: string;
  asset_id?: string;
  before?: string;
  after?: string;
}
Response
interface TradesPaginatedResponse {
  trades: Trade[];
  limit: number;
  count: number;
}
​
Balance and Allowances
​
getBalanceAllowance()
Get your balance and allowance for specific tokens.
Signature
async getBalanceAllowance(
  params?: BalanceAllowanceParams
): Promise<BalanceAllowanceResponse>
Params
interface BalanceAllowanceParams {
  asset_type: AssetType;
  token_id?: string;
}

enum AssetType {
  COLLATERAL = "COLLATERAL",
  CONDITIONAL = "CONDITIONAL",
}
Response
interface BalanceAllowanceResponse {
  balance: string;
  allowance: string;
}
​
updateBalanceAllowance()
Updates the cached balance and allowance for specific tokens.
Signature
async updateBalanceAllowance(
  params?: BalanceAllowanceParams
): Promise<void>
Params
interface BalanceAllowanceParams {
  asset_type: AssetType;
  token_id?: string;
}

enum AssetType {
  COLLATERAL = "COLLATERAL",
  CONDITIONAL = "CONDITIONAL",
}
​
API Key Management (L2)
​
getApiKeys()
Get all API keys associated with your account.
Signature
async getApiKeys(): Promise<ApiKeysResponse>
Response
interface ApiKeysResponse {
  apiKeys: ApiKeyCreds[];
}

interface ApiKeyCreds {
  key: string;
  secret: string;
  passphrase: string;
}
​
deleteApiKey()
Deletes (revokes) the currently authenticated API key.
TypeScript Signature:
async deleteApiKey(): Promise<any>
​
Notifications
​
getNotifications()
Retrieves all event notifications for the L2 authenticated user. Records are removed automatically after 48 hours or if manually removed via dropNotifications().
Signature
public async getNotifications(): Promise<Notification[]>
Response
interface Notification {
    id: number;           // Unique notification ID
    owner: string;        // User's L2 credential apiKey or empty string for global notifications
    payload: any;         // Type-specific payload data
    timestamp?: number;   // Unix timestamp
    type: number;         // Notification type (see type mapping below)
}
Notification Type Mapping
Name	Value	Description
Order Cancellation	1	User’s order was canceled
Order Fill	2	User’s order was filled (maker or taker)
Market Resolved	4	Market was resolved
​
dropNotifications()
Mark notifications as read/dismissed.
Signature
public async dropNotifications(params?: DropNotificationParams): Promise<void>
Params
interface DropNotificationParams {
    ids: string[];  // Array of notification IDs to mark as read
}
​
See Also
Understand CLOB Authentication
Deep dive into L1 and L2 authentication
Public Methods
Access market data, orderbooks, and prices.
L1 Methods
Private key authentication to create or derive API keys (L2 headers)
Web Socket API
Real-time market data streaming
L1 Methods
Builder Methods
Ask a question...

github
Powered by
L2 Methods - Polymarket Documentation

Skip to main content
Polymarket Documentation home pagedark logo

Search...
Ctrl K

Ask AI
Main Site

User Guide
For Developers
Changelog
Polymarket
Discord Community
Twitter
Developer Quickstart
Developer Quickstart
Fetching Market Data
Placing Your First Order
Glossary
API Rate Limits
Endpoints
Market Makers
Market Maker Introduction
Setup
Trading
Liquidity Rewards
Maker Rebates Program
Data Feeds
Inventory Management
Polymarket Builders Program
Builder Program Introduction
Builder Tiers
Builder Profile & Keys
Order Attribution
Relayer Client
Examples
Central Limit Order Book
CLOB Introduction
Status
Quickstart
Authentication
Geographic Restrictions

Client
Methods Overview
Public Methods
L1 Methods
L2 Methods
Builder Methods

REST API

Historical Timeseries Data

Order Management

Trades
Websocket
WSS Overview
WSS Quickstart
WSS Authentication
User Channel
Market Channel

Sports Websocket
Real Time Data Stream
RTDS Overview
RTDS Crypto Prices
RTDS Comments
Gamma Structure
Overview
Gamma Structure
Fetching Markets
Gamma Endpoints

Gamma Status

Sports

Tags

Events

Markets

Series

Comments

Profiles

Search
Data-API

Data API Status

Core

Misc

Builders
Bridge & Swap
Overview

Bridge
Subgraph
Overview
Resolution
Resolution
Conditional Token Frameworks
Overview
Splitting USDC
Merging Tokens
Reedeeming Tokens
Deployment and Additional Information
Proxy Wallets
Proxy wallet
Negative Risk
Overview

On this page
Client Initialization
Methods
getBuilderTrades()
revokeBuilderApiKey()
See Also
Client
Builder Methods
These methods require builder API credentials and are only relevant for Builders Program order attribution.

​
Client Initialization
Builder methods require the client to initialize with a separate authentication setup using builder configs acquired from Polymarket.com and the @polymarket/builder-signing-sdk package.
Local Builder Credentials
Remote Builder Signing

TypeScript

Python
import { ClobClient } from "@polymarket/clob-client";
import { BuilderConfig, BuilderApiKeyCreds } from "@polymarket/builder-signing-sdk";

const builderConfig = new BuilderConfig({
  localBuilderCreds: new BuilderApiKeyCreds({
    key: process.env.BUILDER_API_KEY,
    secret: process.env.BUILDER_SECRET,
    passphrase: process.env.BUILDER_PASS_PHRASE,
  }),
});

const clobClient = new ClobClient(
  "https://clob.polymarket.com",
  137,
  signer,
  apiCreds, // The user's API credentials generated from L1 authentication
  signatureType,
  funderAddress,
  undefined,
  false,
  builderConfig
);
More information on builder signing
​
Methods
​
getBuilderTrades()
Retrieves all trades attributed to your builder account. This method allows builders to track which trades were routed through your platform.
Signature
async getBuilderTrades(
  params?: TradeParams,
): Promise<BuilderTradesPaginatedResponse>
Params
interface TradeParams {
  id?: string;
  maker_address?: string;
  market?: string;
  asset_id?: string;
  before?: string;
  after?: string;
}
Response
interface BuilderTradesPaginatedResponse {
  trades: BuilderTrade[];
  next_cursor: string;
  limit: number;
  count: number;
}

interface BuilderTrade {
  id: string;
  tradeType: string;
  takerOrderHash: string;
  builder: string;
  market: string;
  assetId: string;
  side: string;
  size: string;
  sizeUsdc: string;
  price: string;
  status: string;
  outcome: string;
  outcomeIndex: number;
  owner: string;
  maker: string;
  transactionHash: string;
  matchTime: string;
  bucketIndex: number;
  fee: string;
  feeUsdc: string;
  err_msg?: string | null;
  createdAt: string | null;
  updatedAt: string | null;
}
​
revokeBuilderApiKey()
Revokes the builder API key used to authenticate the current request. After revocation, the key can no longer be used to make builder-authenticated requests.
Signature
async revokeBuilderApiKey(): Promise<any>
​
See Also
Builders Program Introduction
Learn the benefits, how to implement, and more.
Implement Builders Signing
Attribute orders to you, and pre-requisite to using the Relayer Client.
Relayer Client
The relayer executes other gasless transactions for your users, on your app.
Full Example Implementations
Complete Next.js examples integrated with embedded wallets (Privy, Magic, Turnkey, wagmi)
L2 Methods
Get order book summary
Ask a question...

github
Powered by
Builder Methods - Polymarket Documentation

Skip to main content
Polymarket Documentation home pagedark logo

Search...
Ctrl K

Ask AI
Main Site

User Guide
For Developers
Changelog
Polymarket
Discord Community
Twitter
Developer Quickstart
Developer Quickstart
Fetching Market Data
Placing Your First Order
Glossary
API Rate Limits
Endpoints
Market Makers
Market Maker Introduction
Setup
Trading
Liquidity Rewards
Maker Rebates Program
Data Feeds
Inventory Management
Polymarket Builders Program
Builder Program Introduction
Builder Tiers
Builder Profile & Keys
Order Attribution
Relayer Client
Examples
Central Limit Order Book
CLOB Introduction
Status
Quickstart
Authentication
Geographic Restrictions

Client
Methods Overview
Public Methods
L1 Methods
L2 Methods
Builder Methods

REST API

Orderbook
GET
Get order book summary
POST
Get multiple order books summaries by request

Pricing

Spreads

Historical Timeseries Data

Order Management

Trades
Websocket
WSS Overview
WSS Quickstart
WSS Authentication
User Channel
Market Channel

Sports Websocket
Real Time Data Stream
RTDS Overview
RTDS Crypto Prices
RTDS Comments
Gamma Structure
Overview
Gamma Structure
Fetching Markets
Gamma Endpoints

Gamma Status

Sports

Tags

Events

Markets

Series

Comments

Profiles

Search
Data-API

Data API Status

Core

Misc

Builders
Bridge & Swap
Overview

Bridge
Subgraph
Overview
Resolution
Resolution
Conditional Token Frameworks
Overview
Splitting USDC
Merging Tokens
Reedeeming Tokens
Deployment and Additional Information
Proxy Wallets
Proxy wallet
Negative Risk
Overview
Get order book summary

curl --request GET \
  --url https://clob.polymarket.com/book

200

400

404

500
{
  "market": "0x1b6f76e5b8587ee896c35847e12d11e75290a8c3934c5952e8a9d6e4c6f03cfa",
  "asset_id": "1234567890",
  "timestamp": "2023-10-01T12:00:00Z",
  "hash": "0xabc123def456...",
  "bids": [
    {
      "price": "1800.50",
      "size": "10.5"
    }
  ],
  "asks": [
    {
      "price": "1800.50",
      "size": "10.5"
    }
  ],
  "min_order_size": "0.001",
  "tick_size": "0.01",
  "neg_risk": false
}
Orderbook
Get order book summary
Retrieves the order book summary for a specific token

GET
/
book

Try it
Query Parameters
​
token_id
stringrequired
The unique identifier for the token

Response

200

application/json
Successful response

​
market
stringrequired
Market identifier

Example:
"0x1b6f76e5b8587ee896c35847e12d11e75290a8c3934c5952e8a9d6e4c6f03cfa"

​
asset_id
stringrequired
Asset identifier

Example:
"1234567890"

​
timestamp
string<date-time>required
Timestamp of the order book snapshot

Example:
"2023-10-01T12:00:00Z"

​
hash
stringrequired
Hash of the order book state

Example:
"0xabc123def456..."

​
bids
object[]required
Array of bid levels

Show child attributes

​
asks
object[]required
Array of ask levels

Show child attributes

​
min_order_size
stringrequired
Minimum order size for this market

Example:
"0.001"

​
tick_size
stringrequired
Minimum price increment

Example:
"0.01"

​
neg_risk
booleanrequired
Whether negative risk is enabled

Example:
false

Builder Methods
Get multiple order books summaries by request
Ask a question...

github
Powered by
Get order book summary - Polymarket Documentation

Skip to main content
Polymarket Documentation home pagedark logo

Search...
Ctrl K

Ask AI
Main Site

User Guide
For Developers
Changelog
Polymarket
Discord Community
Twitter
Developer Quickstart
Developer Quickstart
Fetching Market Data
Placing Your First Order
Glossary
API Rate Limits
Endpoints
Market Makers
Market Maker Introduction
Setup
Trading
Liquidity Rewards
Maker Rebates Program
Data Feeds
Inventory Management
Polymarket Builders Program
Builder Program Introduction
Builder Tiers
Builder Profile & Keys
Order Attribution
Relayer Client
Examples
Central Limit Order Book
CLOB Introduction
Status
Quickstart
Authentication
Geographic Restrictions

Client
Methods Overview
Public Methods
L1 Methods
L2 Methods
Builder Methods

REST API

Orderbook
GET
Get order book summary
POST
Get multiple order books summaries by request

Pricing

Spreads

Historical Timeseries Data

Order Management

Trades
Websocket
WSS Overview
WSS Quickstart
WSS Authentication
User Channel
Market Channel

Sports Websocket
Real Time Data Stream
RTDS Overview
RTDS Crypto Prices
RTDS Comments
Gamma Structure
Overview
Gamma Structure
Fetching Markets
Gamma Endpoints

Gamma Status

Sports

Tags

Events

Markets

Series

Comments

Profiles

Search
Data-API

Data API Status

Core

Misc

Builders
Bridge & Swap
Overview

Bridge
Subgraph
Overview
Resolution
Resolution
Conditional Token Frameworks
Overview
Splitting USDC
Merging Tokens
Reedeeming Tokens
Deployment and Additional Information
Proxy Wallets
Proxy wallet
Negative Risk
Overview
Get multiple order books summaries by request

curl --request POST \
  --url https://clob.polymarket.com/books \
  --header 'Content-Type: application/json' \
  --data '
[
  {
    "token_id": "1234567890"
  },
  {
    "token_id": "0987654321"
  }
]
'


[
  {
    "market": "0x1b6f76e5b8587ee896c35847e12d11e75290a8c3934c5952e8a9d6e4c6f03cfa",
    "asset_id": "1234567890",
    "timestamp": "2023-10-01T12:00:00Z",
    "hash": "0xabc123def456...",
    "bids": [
      {
        "price": "1800.50",
        "size": "10.5"
      }
    ],
    "asks": [
      {
        "price": "1800.50",
        "size": "10.5"
      }
    ],
    "min_order_size": "0.001",
    "tick_size": "0.01",
    "neg_risk": false
  }
]
Orderbook
Get multiple order books summaries by request
Retrieves order book summaries for specified tokens via POST request

POST
/
books

Try it
Body
application/json
Maximum array length: 500
​
token_id
stringrequired
The unique identifier for the token

Example:
"1234567890"

​
side
enum<string>
Optional side parameter for certain operations

Available options: BUY, SELL 
Example:
"BUY"

Response

200

application/json
Successful response

​
market
stringrequired
Market identifier

Example:
"0x1b6f76e5b8587ee896c35847e12d11e75290a8c3934c5952e8a9d6e4c6f03cfa"

​
asset_id
stringrequired
Asset identifier

Example:
"1234567890"

​
timestamp
string<date-time>required
Timestamp of the order book snapshot

Example:
"2023-10-01T12:00:00Z"

​
hash
stringrequired
Hash of the order book state

Example:
"0xabc123def456..."

​
bids
object[]required
Array of bid levels

Show child attributes

​
asks
object[]required
Array of ask levels

Show child attributes

​
min_order_size
stringrequired
Minimum order size for this market

Example:
"0.001"

​
tick_size
stringrequired
Minimum price increment

Example:
"0.01"

​
neg_risk
booleanrequired
Whether negative risk is enabled

Example:
false

Get order book summary
Get market price
Ask a question...

github
Powered by
Get multiple order books summaries by request - Polymarket Documentation

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.polymarket.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get market price

> Retrieves the market price for a specific token and side



## OpenAPI

````yaml api-reference/clob-subset-openapi.yaml get /price
openapi: 3.0.3
info:
  title: CLOB (Central Limit Order Book) API
  description: >-
    API for interacting with the Central Limit Order Book system, providing
    orderbook data, prices, midpoints, and spreads
  version: 1.0.0
  contact:
    name: CLOB API Team
  license:
    name: MIT
servers:
  - url: https://clob.polymarket.com/
    description: Production server
security: []
tags:
  - name: Orderbook
    description: Order book related operations
  - name: Pricing
    description: Price and midpoint operations
  - name: Spreads
    description: Spread calculation operations
paths:
  /price:
    get:
      tags:
        - Pricing
      summary: Get market price
      description: Retrieves the market price for a specific token and side
      parameters:
        - name: token_id
          in: query
          required: true
          schema:
            type: string
          description: The unique identifier for the token
          example: '1234567890'
        - name: side
          in: query
          required: true
          schema:
            type: string
            enum:
              - BUY
              - SELL
          description: The side of the market (BUY or SELL)
          example: BUY
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PriceResponse'
        '400':
          description: Bad request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
              examples:
                invalid_token:
                  value:
                    error: Invalid token id
                invalid_side:
                  value:
                    error: Invalid side
        '404':
          description: Order book not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
              example:
                error: No orderbook exists for the requested token id
        '500':
          description: Internal server error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
components:
  schemas:
    PriceResponse:
      type: object
      required:
        - price
      properties:
        price:
          type: string
          description: The market price (as string to maintain precision)
          example: '1800.50'
    Error:
      type: object
      required:
        - error
      properties:
        error:
          type: string
          description: Error message describing what went wrong
          example: Invalid token id

````

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.polymarket.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get multiple market prices

> Retrieves market prices for multiple tokens and sides



## OpenAPI

````yaml api-reference/clob-subset-openapi.yaml get /prices
openapi: 3.0.3
info:
  title: CLOB (Central Limit Order Book) API
  description: >-
    API for interacting with the Central Limit Order Book system, providing
    orderbook data, prices, midpoints, and spreads
  version: 1.0.0
  contact:
    name: CLOB API Team
  license:
    name: MIT
servers:
  - url: https://clob.polymarket.com/
    description: Production server
security: []
tags:
  - name: Orderbook
    description: Order book related operations
  - name: Pricing
    description: Price and midpoint operations
  - name: Spreads
    description: Spread calculation operations
paths:
  /prices:
    get:
      tags:
        - Pricing
      summary: Get multiple market prices
      description: Retrieves market prices for multiple tokens and sides
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PricesResponse'
        '400':
          description: Bad request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '500':
          description: Internal server error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
components:
  schemas:
    PricesResponse:
      type: object
      additionalProperties:
        type: object
        additionalProperties:
          type: string
      description: Map of token_id to side to price
      example:
        '1234567890':
          BUY: '1800.50'
          SELL: '1801.00'
        '0987654321':
          BUY: '50.25'
          SELL: '50.30'
    Error:
      type: object
      required:
        - error
      properties:
        error:
          type: string
          description: Error message describing what went wrong
          example: Invalid token id

````

Skip to main content
Polymarket Documentation home pagedark logo

Search...
Ctrl K

Ask AI
Main Site

User Guide
For Developers
Changelog
Polymarket
Discord Community
Twitter
Developer Quickstart
Developer Quickstart
Fetching Market Data
Placing Your First Order
Glossary
API Rate Limits
Endpoints
Market Makers
Market Maker Introduction
Setup
Trading
Liquidity Rewards
Maker Rebates Program
Data Feeds
Inventory Management
Polymarket Builders Program
Builder Program Introduction
Builder Tiers
Builder Profile & Keys
Order Attribution
Relayer Client
Examples
Central Limit Order Book
CLOB Introduction
Status
Quickstart
Authentication
Geographic Restrictions

Client
Methods Overview
Public Methods
L1 Methods
L2 Methods
Builder Methods

REST API

Orderbook
GET
Get order book summary
POST
Get multiple order books summaries by request

Pricing
GET
Get market price
GET
Get multiple market prices
POST
Get multiple market prices by request
GET
Get midpoint price
GET
Get price history for a traded token

Spreads

Historical Timeseries Data

Order Management

Trades
Websocket
WSS Overview
WSS Quickstart
WSS Authentication
User Channel
Market Channel

Sports Websocket
Real Time Data Stream
RTDS Overview
RTDS Crypto Prices
RTDS Comments
Gamma Structure
Overview
Gamma Structure
Fetching Markets
Gamma Endpoints

Gamma Status

Sports

Tags

Events

Markets

Series

Comments

Profiles

Search
Data-API

Data API Status

Core

Misc

Builders
Bridge & Swap
Overview

Bridge
Subgraph
Overview
Resolution
Resolution
Conditional Token Frameworks
Overview
Splitting USDC
Merging Tokens
Reedeeming Tokens
Deployment and Additional Information
Proxy Wallets
Proxy wallet
Negative Risk
Overview
Get multiple market prices by request

curl --request POST \
  --url https://clob.polymarket.com/prices \
  --header 'Content-Type: application/json' \
  --data '
[
  {
    "token_id": "1234567890",
    "side": "BUY"
  },
  {
    "token_id": "0987654321",
    "side": "SELL"
  }
]
'


{
  "1234567890": {
    "BUY": "1800.50",
    "SELL": "1801.00"
  },
  "0987654321": {
    "BUY": "50.25",
    "SELL": "50.30"
  }
}
Pricing
Get multiple market prices by request
Retrieves market prices for specified tokens and sides via POST request

POST
/
prices

Try it
Body
application/json
Maximum array length: 500
​
token_id
stringrequired
The unique identifier for the token

Example:
"1234567890"

​
side
enum<string>required
The side of the market (BUY or SELL)

Available options: BUY, SELL 
Example:
"BUY"

Response

200

application/json
Successful response

Map of token_id to side to price

​
{key}
object
Show child attributes

Get multiple market prices
Get midpoint price
Ask a question...

github
Powered by
Get multiple market prices by request - Polymarket Documentation

Skip to main content
Polymarket Documentation home pagedark logo

Search...
Ctrl K

Ask AI
Main Site

User Guide
For Developers
Changelog
Polymarket
Discord Community
Twitter
Developer Quickstart
Developer Quickstart
Fetching Market Data
Placing Your First Order
Glossary
API Rate Limits
Endpoints
Market Makers
Market Maker Introduction
Setup
Trading
Liquidity Rewards
Maker Rebates Program
Data Feeds
Inventory Management
Polymarket Builders Program
Builder Program Introduction
Builder Tiers
Builder Profile & Keys
Order Attribution
Relayer Client
Examples
Central Limit Order Book
CLOB Introduction
Status
Quickstart
Authentication
Geographic Restrictions

Client
Methods Overview
Public Methods
L1 Methods
L2 Methods
Builder Methods

REST API

Orderbook
GET
Get order book summary
POST
Get multiple order books summaries by request

Pricing
GET
Get market price
GET
Get multiple market prices
POST
Get multiple market prices by request
GET
Get midpoint price
GET
Get price history for a traded token

Spreads

Historical Timeseries Data

Order Management

Trades
Websocket
WSS Overview
WSS Quickstart
WSS Authentication
User Channel
Market Channel

Sports Websocket
Real Time Data Stream
RTDS Overview
RTDS Crypto Prices
RTDS Comments
Gamma Structure
Overview
Gamma Structure
Fetching Markets
Gamma Endpoints

Gamma Status

Sports

Tags

Events

Markets

Series

Comments

Profiles

Search
Data-API

Data API Status

Core

Misc

Builders
Bridge & Swap
Overview

Bridge
Subgraph
Overview
Resolution
Resolution
Conditional Token Frameworks
Overview
Splitting USDC
Merging Tokens
Reedeeming Tokens
Deployment and Additional Information
Proxy Wallets
Proxy wallet
Negative Risk
Overview
Get midpoint price

curl --request GET \
  --url https://clob.polymarket.com/midpoint

200

400

404

500
{
  "mid": "1800.75"
}
Pricing
Get midpoint price
Retrieves the midpoint price for a specific token

GET
/
midpoint

Try it
Query Parameters
​
token_id
stringrequired
The unique identifier for the token

Response

200

application/json
Successful response

​
mid
stringrequired
The midpoint price (as string to maintain precision)

Example:
"1800.75"

Get multiple market prices by request
Get price history for a traded token
Ask a question...

github
Powered by
Get midpoint price - Polymarket Documentation

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.polymarket.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get price history for a traded token

> Fetches historical price data for a specified market token



## OpenAPI

````yaml api-reference/clob-subset-openapi.yaml get /prices-history
openapi: 3.0.3
info:
  title: CLOB (Central Limit Order Book) API
  description: >-
    API for interacting with the Central Limit Order Book system, providing
    orderbook data, prices, midpoints, and spreads
  version: 1.0.0
  contact:
    name: CLOB API Team
  license:
    name: MIT
servers:
  - url: https://clob.polymarket.com/
    description: Production server
security: []
tags:
  - name: Orderbook
    description: Order book related operations
  - name: Pricing
    description: Price and midpoint operations
  - name: Spreads
    description: Spread calculation operations
paths:
  /prices-history:
    get:
      tags:
        - Pricing
      summary: Get price history for a traded token
      description: Fetches historical price data for a specified market token
      parameters:
        - name: market
          in: query
          required: true
          schema:
            type: string
          description: The CLOB token ID for which to fetch price history
          example: '1234567890'
        - name: startTs
          in: query
          required: false
          schema:
            type: number
          description: The start time, a Unix timestamp in UTC
          example: 1697875200
        - name: endTs
          in: query
          required: false
          schema:
            type: number
          description: The end time, a Unix timestamp in UTC
          example: 1697961600
        - name: interval
          in: query
          required: false
          schema:
            type: string
            enum:
              - 1m
              - 1w
              - 1d
              - 6h
              - 1h
              - max
          description: >-
            A string representing a duration ending at the current time.
            Mutually exclusive with startTs and endTs
          example: 1d
        - name: fidelity
          in: query
          required: false
          schema:
            type: number
          description: The resolution of the data, in minutes
          example: 60
      responses:
        '200':
          description: A list of timestamp/price pairs
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PriceHistoryResponse'
        '400':
          description: Bad request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '404':
          description: Market not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '500':
          description: Internal server error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
components:
  schemas:
    PriceHistoryResponse:
      type: object
      required:
        - history
      properties:
        history:
          type: array
          items:
            type: object
            required:
              - t
              - p
            properties:
              t:
                type: number
                description: UTC timestamp
                example: 1697875200
              p:
                type: number
                description: Price
                example: 1800.75
    Error:
      type: object
      required:
        - error
      properties:
        error:
          type: string
          description: Error message describing what went wrong
          example: Invalid token id

````


Skip to main content
Polymarket Documentation home pagedark logo

Search...
Ctrl K

Ask AI
Main Site

User Guide
For Developers
Changelog
Polymarket
Discord Community
Twitter
Developer Quickstart
Developer Quickstart
Fetching Market Data
Placing Your First Order
Glossary
API Rate Limits
Endpoints
Market Makers
Market Maker Introduction
Setup
Trading
Liquidity Rewards
Maker Rebates Program
Data Feeds
Inventory Management
Polymarket Builders Program
Builder Program Introduction
Builder Tiers
Builder Profile & Keys
Order Attribution
Relayer Client
Examples
Central Limit Order Book
CLOB Introduction
Status
Quickstart
Authentication
Geographic Restrictions

Client
Methods Overview
Public Methods
L1 Methods
L2 Methods
Builder Methods

REST API

Orderbook
GET
Get order book summary
POST
Get multiple order books summaries by request

Pricing
GET
Get market price
GET
Get multiple market prices
POST
Get multiple market prices by request
GET
Get midpoint price
GET
Get price history for a traded token

Spreads
POST
Get bid-ask spreads

Historical Timeseries Data

Order Management

Trades
Websocket
WSS Overview
WSS Quickstart
WSS Authentication
User Channel
Market Channel

Sports Websocket
Real Time Data Stream
RTDS Overview
RTDS Crypto Prices
RTDS Comments
Gamma Structure
Overview
Gamma Structure
Fetching Markets
Gamma Endpoints

Gamma Status

Sports

Tags

Events

Markets

Series

Comments

Profiles

Search
Data-API

Data API Status

Core

Misc

Builders
Bridge & Swap
Overview

Bridge
Subgraph
Overview
Resolution
Resolution
Conditional Token Frameworks
Overview
Splitting USDC
Merging Tokens
Reedeeming Tokens
Deployment and Additional Information
Proxy Wallets
Proxy wallet
Negative Risk
Overview
Get bid-ask spreads

curl --request POST \
  --url https://clob.polymarket.com/spreads \
  --header 'Content-Type: application/json' \
  --data '
[
  {
    "token_id": "1234567890"
  },
  {
    "token_id": "0987654321"
  }
]
'


{
  "1234567890": "0.50",
  "0987654321": "0.05"
}
Spreads
Get bid-ask spreads
Retrieves bid-ask spreads for multiple tokens

POST
/
spreads

Try it
Body
application/json
Maximum array length: 500
​
token_id
stringrequired
The unique identifier for the token

Example:
"1234567890"

​
side
enum<string>
Optional side parameter for certain operations

Available options: BUY, SELL 
Example:
"BUY"

Response

200

application/json
Successful response

Map of token_id to spread value

​
{key}
string
Get price history for a traded token
Historical Timeseries Data
Ask a question...

github
Powered by
Get bid-ask spreads - Polymarket Documentation

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.polymarket.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Historical Timeseries Data

> Fetches historical price data for a specified market token.


The CLOB provides detailed price history for each traded token.

**HTTP REQUEST**

`GET /<clob-endpoint>/prices-history`

<Tip>We also have a Interactive Notebook to visualize the data from this endpoint available [here](https://colab.research.google.com/drive/1s4TCOR4K7fRP7EwAH1YmOactMakx24Cs?usp=sharing#scrollTo=mYCJBcfB9Zu4).</Tip>


## OpenAPI

````yaml GET /prices-history
openapi: 3.0.3
info:
  title: CLOB (Central Limit Order Book) API
  description: >-
    API for interacting with the Central Limit Order Book system, providing
    orderbook data, prices, midpoints, and spreads
  version: 1.0.0
  contact:
    name: CLOB API Team
  license:
    name: MIT
servers:
  - url: https://clob.polymarket.com/
    description: Production server
security: []
tags:
  - name: Orderbook
    description: Order book related operations
  - name: Pricing
    description: Price and midpoint operations
  - name: Spreads
    description: Spread calculation operations
paths:
  /prices-history:
    get:
      tags:
        - Pricing
      summary: Get price history for a traded token
      description: Fetches historical price data for a specified market token
      parameters:
        - name: market
          in: query
          required: true
          schema:
            type: string
          description: The CLOB token ID for which to fetch price history
          example: '1234567890'
        - name: startTs
          in: query
          required: false
          schema:
            type: number
          description: The start time, a Unix timestamp in UTC
          example: 1697875200
        - name: endTs
          in: query
          required: false
          schema:
            type: number
          description: The end time, a Unix timestamp in UTC
          example: 1697961600
        - name: interval
          in: query
          required: false
          schema:
            type: string
            enum:
              - 1m
              - 1w
              - 1d
              - 6h
              - 1h
              - max
          description: >-
            A string representing a duration ending at the current time.
            Mutually exclusive with startTs and endTs
          example: 1d
        - name: fidelity
          in: query
          required: false
          schema:
            type: number
          description: The resolution of the data, in minutes
          example: 60
      responses:
        '200':
          description: A list of timestamp/price pairs
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PriceHistoryResponse'
        '400':
          description: Bad request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '404':
          description: Market not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '500':
          description: Internal server error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
components:
  schemas:
    PriceHistoryResponse:
      type: object
      required:
        - history
      properties:
        history:
          type: array
          items:
            type: object
            required:
              - t
              - p
            properties:
              t:
                type: number
                description: UTC timestamp
                example: 1697875200
              p:
                type: number
                description: Price
                example: 1800.75
    Error:
      type: object
      required:
        - error
      properties:
        error:
          type: string
          description: Error message describing what went wrong
          example: Invalid token id

````

Skip to main content
Polymarket Documentation home pagedark logo

Search...
Ctrl K

Ask AI
Main Site

User Guide
For Developers
Changelog
Polymarket
Discord Community
Twitter
Developer Quickstart
Developer Quickstart
Fetching Market Data
Placing Your First Order
Glossary
API Rate Limits
Endpoints
Market Makers
Market Maker Introduction
Setup
Trading
Liquidity Rewards
Maker Rebates Program
Data Feeds
Inventory Management
Polymarket Builders Program
Builder Program Introduction
Builder Tiers
Builder Profile & Keys
Order Attribution
Relayer Client
Examples
Central Limit Order Book
CLOB Introduction
Status
Quickstart
Authentication
Geographic Restrictions

Client
Methods Overview
Public Methods
L1 Methods
L2 Methods
Builder Methods

REST API

Orderbook
GET
Get order book summary
POST
Get multiple order books summaries by request

Pricing
GET
Get market price
GET
Get multiple market prices
POST
Get multiple market prices by request
GET
Get midpoint price
GET
Get price history for a traded token

Spreads
POST
Get bid-ask spreads

Historical Timeseries Data
GET
Historical Timeseries Data

Order Management
Orders Overview
Place Single Order
Place Multiple Orders (Batching)
Get Order
Get Active Orders
Check Order Reward Scoring
Cancel Orders(s)
Onchain Order Info

Trades
Websocket
WSS Overview
WSS Quickstart
WSS Authentication
User Channel
Market Channel

Sports Websocket
Real Time Data Stream
RTDS Overview
RTDS Crypto Prices
RTDS Comments
Gamma Structure
Overview
Gamma Structure
Fetching Markets
Gamma Endpoints

Gamma Status

Sports

Tags

Events

Markets

Series

Comments

Profiles

Search
Data-API

Data API Status

Core

Misc

Builders
Bridge & Swap
Overview

Bridge
Subgraph
Overview
Resolution
Resolution
Conditional Token Frameworks
Overview
Splitting USDC
Merging Tokens
Reedeeming Tokens
Deployment and Additional Information
Proxy Wallets
Proxy wallet
Negative Risk
Overview

On this page
Allowances
Signature Types
Validity Checks
Order Management
Orders Overview
Detailed instructions for creating, placing, and managing orders using Polymarket’s CLOB API.

All orders are expressed as limit orders (can be marketable). The underlying order primitive must be in the form expected and executable by the on-chain binary limit order protocol contract. Preparing such an order is quite involved (structuring, hashing, signing), thus Polymarket suggests using the open source typescript, python and golang libraries.
​
Allowances
To place an order, allowances must be set by the funder address for the specified maker asset for the Exchange contract. When buying, this means the funder must have set a USDC allowance greater than or equal to the spending amount. When selling, the funder must have set an allowance for the conditional token that is greater than or equal to the selling amount. This allows the Exchange contract to execute settlement according to the signed order instructions created by a user and matched by the operator.
​
Signature Types
Polymarket’s CLOB supports 3 signature types. Orders must identify what signature type they use. The available typescript and python clients abstract the complexity of signing and preparing orders with the following signature types by allowing a funder address and signer type to be specified on initialization. The supported signature types are:
Type	ID	Description
EOA	0	EIP712 signature signed by an EOA
POLY_PROXY	1	EIP712 signatures signed by a signer associated with funding Polymarket proxy wallet
POLY_GNOSIS_SAFE	2	EIP712 signatures signed by a signer associated with funding Polymarket gnosis safe wallet
​
Validity Checks
Orders are continually monitored to make sure they remain valid. Specifically, this includes continually tracking underlying balances, allowances and on-chain order cancellations. Any maker that is caught intentionally abusing these checks (which are essentially real time) will be blacklisted.
Additionally, there are rails on order placement in a market. Specifically, you can only place orders that sum to less than or equal to your available balance for each market. For example if you have 500 USDC in your funding wallet, you can place one order to buy 1000 YES in marketA @ $.50, then any additional buy orders to that market will be rejected since your entire balance is reserved for the first (and only) buy order. More explicitly the max size you can place for an order is:
maxOrderSize
=
underlyingAssetBalance
−
∑
(
orderSize
−
orderFillAmount
)
maxOrderSize=underlyingAssetBalance−∑(orderSize−orderFillAmount)
Historical Timeseries Data
Place Single Order
Ask a question...

github
Powered by
Orders Overview - Polymarket Documentation

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.polymarket.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Place Single Order

> Detailed instructions for creating, placing, and managing orders using Polymarket's CLOB API.

# Create and Place an Order

<Tip> This endpoint requires a L2 Header </Tip>

Create and place an order using the Polymarket CLOB API clients. All orders are represented as "limit" orders, but "market" orders are also supported. To place a market order, simply ensure your price is marketable against current resting limit orders, which are executed on input at the best price.

**HTTP REQUEST**

`POST /<clob-endpoint>/order`

### Request Payload Parameters

| Name      | Required | Type    | Description                                                                                  |
| --------- | -------- | ------- | -------------------------------------------------------------------------------------------- |
| order     | yes      | Order   | signed object                                                                                |
| owner     | yes      | string  | api key of order owner                                                                       |
| orderType | yes      | string  | order type ("FOK", "GTC", "GTD")                                                             |
| postOnly  | no       | boolean | if `true`, the order will only rest on the book and not match immediately (default: `false`) |

### Post-only orders

* postOnly submits a limit order that will not match resting liquidity upon entry.
* If a postOnly order would cross the spread (i.e., it is marketable), it will be rejected rather than executed.
* postOnly cannot be combined with market order types (e.g., FOK or FAK). If `postOnly = true` is sent with a market order type, the order will be rejected.

An `order` object is the form:

| Name          | Required | Type    | Description                                        |
| ------------- | -------- | ------- | -------------------------------------------------- |
| salt          | yes      | integer | random salt used to create unique order            |
| maker         | yes      | string  | maker address (funder)                             |
| signer        | yes      | string  | signing address                                    |
| taker         | yes      | string  | taker address (operator)                           |
| tokenId       | yes      | string  | ERC1155 token ID of conditional token being traded |
| makerAmount   | yes      | string  | maximum amount maker is willing to spend           |
| takerAmount   | yes      | string  | minimum amount taker will pay the maker in return  |
| expiration    | yes      | string  | unix expiration timestamp                          |
| nonce         | yes      | string  | maker's exchange nonce of the order is associated  |
| feeRateBps    | yes      | string  | fee rate basis points as required by the operator  |
| side          | yes      | string  | buy or sell enum index                             |
| signatureType | yes      | integer | signature type enum index                          |
| signature     | yes      | string  | hex encoded signature                              |

### Order types

* **FOK**: A Fill-Or-Kill order is an market order to buy (in dollars) or sell (in shares) shares that must be executed immediately in its entirety; otherwise, the entire order will be cancelled.
* **FAK**: A Fill-And-Kill order is a market order to buy (in dollars) or sell (in shares) that will be executed immediately for as many shares as are available; any portion not filled at once is cancelled.
* **GTC**: A Good-Til-Cancelled order is a limit order that is active until it is fulfilled or cancelled.
* **GTD**: A Good-Til-Date order is a type of order that is active until its specified date (UTC seconds timestamp), unless it has already been fulfilled or cancelled. There is a security threshold of one minute. If the order needs to expire in 90 seconds the correct expiration value is: now + 1 minute + 30 seconds

### Response Format

| Name        | Type      | Description                                                                                                                        |
| ----------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| success     | boolean   | boolean indicating if server-side err (`success = false`) -> server-side error                                                     |
| errorMsg    | string    | error message in case of unsuccessful placement (in case `success = false`, e.g. `client-side error`, the reason is in `errorMsg`) |
| orderId     | string    | id of order                                                                                                                        |
| orderHashes | string\[] | hash of settlement transaction order was marketable and triggered a match                                                          |

### Insert Error Messages

If the `errorMsg` field of the response object from placement is not an empty string, the order was not able to be immediately placed. This might be because of a delay or because of a failure. If the `success` is not `true`, then there was an issue placing the order. The following `errorMessages` are possible:

#### Error

| Error                                | Success | Message                                                                                 | Description                                                           |
| ------------------------------------ | ------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| INVALID\_ORDER\_MIN\_TICK\_SIZE      | yes     | order is invalid. Price breaks minimum tick size rules                                  | order price isn't accurate to correct tick sizing                     |
| INVALID\_ORDER\_MIN\_SIZE            | yes     | order is invalid. Size lower than the minimum                                           | order size must meet min size threshold requirement                   |
| INVALID\_ORDER\_DUPLICATED           | yes     | order is invalid. Duplicated. Same order has already been placed, can't be placed again |                                                                       |
| INVALID\_ORDER\_NOT\_ENOUGH\_BALANCE | yes     | not enough balance / allowance                                                          | funder address doesn't have sufficient balance or allowance for order |
| INVALID\_ORDER\_EXPIRATION           | yes     | invalid expiration                                                                      | expiration field expresses a time before now                          |
| INVALID\_ORDER\_ERROR                | yes     | could not insert order                                                                  | system error while inserting order                                    |
| INVALID\_POST\_ONLY\_ORDER\_TYPE     | yes     | invalid post-only order: only GTC and GTD order types are allowed                       | post only flag attached to a market order                             |
| INVALID\_POST\_ONLY\_ORDER           | yes     | invalid post-only order: order crosses book                                             | post only order would match                                           |
| EXECUTION\_ERROR                     | yes     | could not run the execution                                                             | system error while attempting to execute trade                        |
| ORDER\_DELAYED                       | no      | order match delayed due to market conditions                                            | order placement delayed                                               |
| DELAYING\_ORDER\_ERROR               | yes     | error delaying the order                                                                | system error while delaying order                                     |
| FOK\_ORDER\_NOT\_FILLED\_ERROR       | yes     | order couldn't be fully filled, FOK orders are fully filled/killed                      | FOK order not fully filled so can't be placed                         |
| MARKET\_NOT\_READY                   | no      | the market is not yet ready to process new orders                                       | system not accepting orders for market yet                            |

### Insert Statuses

When placing an order, a status field is included. The status field provides additional information regarding the order's state as a result of the placement. Possible values include:

#### Status

| Status    | Description                                                  |
| --------- | ------------------------------------------------------------ |
| matched   | order placed and matched with an existing resting order      |
| live      | order placed and resting on the book                         |
| delayed   | order marketable, but subject to matching delay              |
| unmatched | order marketable, but failure delaying, placement successful |

<RequestExample>
  ```python Python theme={null}
  from py_clob_client.client import ClobClient
  from py_clob_client.clob_types import OrderArgs, OrderType
  from py_clob_client.order_builder.constants import BUY

  host: str = "https://clob.polymarket.com"
  key: str = "" #This is your Private Key. Export from reveal.polymarket.com or from your Web3 Application
  chain_id: int = 137 #No need to adjust this
  POLYMARKET_PROXY_ADDRESS: str = '' #This is the address you deposit/send USDC to to FUND your Polymarket account.

  #Select from the following 3 initialization options to matches your login method, and remove any unused lines so only one client is initialized.


  ### Initialization of a client using a Polymarket Proxy associated with an Email/Magic account. If you login with your email use this example.
  client = ClobClient(host, key=key, chain_id=chain_id, signature_type=1, funder=POLYMARKET_PROXY_ADDRESS)

  ### Initialization of a client using a Polymarket Proxy associated with a Browser Wallet(Metamask, Coinbase Wallet, etc)
  client = ClobClient(host, key=key, chain_id=chain_id, signature_type=2, funder=POLYMARKET_PROXY_ADDRESS)

  ### Initialization of a client that trades directly from an EOA. 
  client = ClobClient(host, key=key, chain_id=chain_id)

  ## Create and sign a limit order buying 100 YES tokens for 0.50c each
  #Refer to the Markets API documentation to locate a tokenID: https://docs.polymarket.com/developers/gamma-markets-api/get-markets

  client.set_api_creds(client.create_or_derive_api_creds()) 

  order_args = OrderArgs(
      price=0.01,
      size=5.0,
      side=BUY,
      token_id="", #Token ID you want to purchase goes here. 
  )
  signed_order = client.create_order(order_args)

  ## GTC(Good-Till-Cancelled) Order
  resp = client.post_order(signed_order, OrderType.GTC)
  print(resp)
  ```

  ```javascript typescript theme={null}
  // GTC Order example
  //
  import { Side, OrderType } from "@polymarket/clob-client";

  async function main() {
    // Create a buy order for 100 YES for 0.50c
    // YES: 71321045679252212594626385532706912750332728571942532289631379312455583992563
    const order = await clobClient.createOrder({
      tokenID:
        "71321045679252212594626385532706912750332728571942532289631379312455583992563",
      price: 0.5,
      side: Side.BUY,
      size: 100,
      feeRateBps: 0,
      nonce: 1,
    });
    console.log("Created Order", order);

    // Send it to the server

    // GTC Order
    const resp = await clobClient.postOrder(order, OrderType.GTC);
    console.log(resp);
  }

  main();
  // GTD Order example
  //
  import { Side, OrderType } from "@polymarket/clob-client";

  async function main() {
    // Create a buy order for 100 YES for 0.50c that expires in 1 minute
    // YES: 71321045679252212594626385532706912750332728571942532289631379312455583992563

    // There is a 1 minute of security threshold for the expiration field.
    // If we need the order to expire in 30 seconds the correct expiration value is:
    // now + 1 miute + 30 seconds
    const oneMinute = 60 * 1000;
    const seconds = 30 * 1000;
    const expiration = parseInt(
      ((new Date().getTime() + oneMinute + seconds) / 1000).toString()
    );

    const order = await clobClient.createOrder({
      tokenID:
        "71321045679252212594626385532706912750332728571942532289631379312455583992563",
      price: 0.5,
      side: Side.BUY,
      size: 100,
      feeRateBps: 0,
      nonce: 1,
      // There is a 1 minute of security threshold for the expiration field.
      // If we need the order to expire in 30 seconds the correct expiration value is:
      // now + 1 miute + 30 seconds
      expiration: expiration,
    });
    console.log("Created Order", order);

    // Send it to the server

    // GTD Order
    const resp = await clobClient.postOrder(order, OrderType.GTD);
    console.log(resp);
  }

  main();
  // FOK BUY Order example
  //
  import { Side, OrderType } from "@polymarket/clob-client";

  async function main() {
    // Create a market buy order for $100
    // YES: 71321045679252212594626385532706912750332728571942532289631379312455583992563

    const marketOrder = await clobClient.createMarketOrder({
      side: Side.BUY,
      tokenID:
        "71321045679252212594626385532706912750332728571942532289631379312455583992563",
      amount: 100, // $$$
      feeRateBps: 0,
      nonce: 0,
      price: 0.5,
    });
    console.log("Created Order", order);

    // Send it to the server
    // FOK Order
    const resp = await clobClient.postOrder(order, OrderType.FOK);
    console.log(resp);
  }

  main();
  // FOK SELL Order example
  //
  import { Side, OrderType } from "@polymarket/clob-client";

  async function main() {
    // Create a market sell order for 100 shares
    // YES: 71321045679252212594626385532706912750332728571942532289631379312455583992563

    const marketOrder = await clobClient.createMarketOrder({
      side: Side.SELL,
      tokenID:
        "71321045679252212594626385532706912750332728571942532289631379312455583992563",
      amount: 100, // shares
      feeRateBps: 0,
      nonce: 0,
      price: 0.5,
    });
    console.log("Created Order", order);

    // Send it to the server
    // FOK Order
    const resp = await clobClient.postOrder(order, OrderType.FOK);
    console.log(resp);
  }

  main();
  ```
</RequestExample>


Skip to main content
Polymarket Documentation home pagedark logo

Search...
Ctrl K

Ask AI
Main Site

User Guide
For Developers
Changelog
Polymarket
Discord Community
Twitter
Developer Quickstart
Developer Quickstart
Fetching Market Data
Placing Your First Order
Glossary
API Rate Limits
Endpoints
Market Makers
Market Maker Introduction
Setup
Trading
Liquidity Rewards
Maker Rebates Program
Data Feeds
Inventory Management
Polymarket Builders Program
Builder Program Introduction
Builder Tiers
Builder Profile & Keys
Order Attribution
Relayer Client
Examples
Central Limit Order Book
CLOB Introduction
Status
Quickstart
Authentication
Geographic Restrictions

Client
Methods Overview
Public Methods
L1 Methods
L2 Methods
Builder Methods

REST API

Orderbook
GET
Get order book summary
POST
Get multiple order books summaries by request

Pricing
GET
Get market price
GET
Get multiple market prices
POST
Get multiple market prices by request
GET
Get midpoint price
GET
Get price history for a traded token

Spreads
POST
Get bid-ask spreads

Historical Timeseries Data
GET
Historical Timeseries Data

Order Management
Orders Overview
Place Single Order
Place Multiple Orders (Batching)
Get Order
Get Active Orders
Check Order Reward Scoring
Cancel Orders(s)
Onchain Order Info

Trades
Websocket
WSS Overview
WSS Quickstart
WSS Authentication
User Channel
Market Channel

Sports Websocket
Real Time Data Stream
RTDS Overview
RTDS Crypto Prices
RTDS Comments
Gamma Structure
Overview
Gamma Structure
Fetching Markets
Gamma Endpoints

Gamma Status

Sports

Tags

Events

Markets

Series

Comments

Profiles

Search
Data-API

Data API Status

Core

Misc

Builders
Bridge & Swap
Overview

Bridge
Subgraph
Overview
Resolution
Resolution
Conditional Token Frameworks
Overview
Splitting USDC
Merging Tokens
Reedeeming Tokens
Deployment and Additional Information
Proxy Wallets
Proxy wallet
Negative Risk
Overview

Python

typescript

Example Payload
from py_clob_client.client import ClobClient
from py_clob_client.clob_types import OrderArgs, OrderType, PostOrdersArgs
from py_clob_client.order_builder.constants import BUY


host: str = "https://clob.polymarket.com"
key: str = "" ##This is your Private Key. Export from https://reveal.magic.link/polymarket or from your Web3 Application
chain_id: int = 137 #No need to adjust this
POLYMARKET_PROXY_ADDRESS: str = '' #This is the address listed below your profile picture when using the Polymarket site.

#Select from the following 3 initialization options to matches your login method, and remove any unused lines so only one client is initialized.


### Initialization of a client using a Polymarket Proxy associated with an Email/Magic account. If you login with your email use this example.
client = ClobClient(host, key=key, chain_id=chain_id, signature_type=1, funder=POLYMARKET_PROXY_ADDRESS)

### Initialization of a client using a Polymarket Proxy associated with a Browser Wallet(Metamask, Coinbase Wallet, etc)
client = ClobClient(host, key=key, chain_id=chain_id, signature_type=2, funder=POLYMARKET_PROXY_ADDRESS)

### Initialization of a client that trades directly from an EOA. 
client = ClobClient(host, key=key, chain_id=chain_id)

## Create and sign a limit order buying 100 YES tokens for 0.50c each
#Refer to the Markets API documentation to locate a tokenID: https://docs.polymarket.com/developers/gamma-markets-api/get-markets

client.set_api_creds(client.create_or_derive_api_creds()) 

resp = client.post_orders([
    PostOrdersArgs(
        # Create and sign a limit order buying 100 YES tokens for 0.50 each
        order=client.create_order(OrderArgs(
            price=0.01,
            size=5,
            side=BUY,
            token_id="88613172803544318200496156596909968959424174365708473463931555296257475886634",
        )),
        orderType=OrderType.GTC,  # Good 'Til Cancelled
    ),
    PostOrdersArgs(
        # Create and sign a limit order selling 200 NO tokens for 0.25 each
        order=client.create_order(OrderArgs(
            price=0.01,
            size=5,
            side=BUY,
            token_id="93025177978745967226369398316375153283719303181694312089956059680730874301533",
        )),
        orderType=OrderType.GTC,  # Good 'Til Cancelled
    )
])
print(resp)
print("Done!")
Order Management
Place Multiple Orders (Batching)
Instructions for placing multiple orders(Batch)

This endpoint requires a L2 Header
Polymarket’s CLOB supports batch orders, allowing you to place up to 15 orders in a single request. Before using this feature, make sure you’re comfortable placing a single order first. You can find the documentation for that here.
HTTP REQUEST
POST /<clob-endpoint>/orders
​
Request Payload Parameters
Name	Required	Type	Description
PostOrder	yes	PostOrders[]	list of signed order objects (Signed Order + Order Type + Owner)
A PostOrder object is the form:
Name	Required	Type	Description
order	yes	order	See below table for details on crafting this object
orderType	yes	string	order type (“FOK”, “GTC”, “GTD”, “FAK”)
owner	yes	string	api key of order owner
postOnly	no	boolean	if true, the order will only rest on the book and not match immediately (default: false)
An order object is the form:
Name	Required	Type	Description
salt	yes	integer	random salt used to create unique order
maker	yes	string	maker address (funder)
signer	yes	string	signing address
taker	yes	string	taker address (operator)
tokenId	yes	string	ERC1155 token ID of conditional token being traded
makerAmount	yes	string	maximum amount maker is willing to spend
takerAmount	yes	string	minimum amount taker will pay the maker in return
expiration	yes	string	unix expiration timestamp
nonce	yes	string	maker’s exchange nonce of the order is associated
feeRateBps	yes	string	fee rate basis points as required by the operator
side	yes	string	buy or sell enum index
signatureType	yes	integer	signature type enum index
signature	yes	string	hex encoded signature
​
Order types
FOK: A Fill-Or-Kill order is an market order to buy (in dollars) or sell (in shares) shares that must be executed immediately in its entirety; otherwise, the entire order will be cancelled.
FAK: A Fill-And-Kill order is a market order to buy (in dollars) or sell (in shares) that will be executed immediately for as many shares as are available; any portion not filled at once is cancelled.
GTC: A Good-Til-Cancelled order is a limit order that is active until it is fulfilled or cancelled.
GTD: A Good-Til-Date order is a type of order that is active until its specified date (UTC seconds timestamp), unless it has already been fulfilled or cancelled. There is a security threshold of one minute. If the order needs to expire in 90 seconds the correct expiration value is: now + 1 minute + 30 seconds
​
Response Format
Name	Type	Description
success	boolean	boolean indicating if server-side err (success = false) -> server-side error
errorMsg	string	error message in case of unsuccessful placement (in case success = false, e.g. client-side error, the reason is in errorMsg)
orderId	string	id of order
orderHashes	string[]	hash of settlement transaction order was marketable and triggered a match
​
Insert Error Messages
If the errorMsg field of the response object from placement is not an empty string, the order was not able to be immediately placed. This might be because of a delay or because of a failure. If the success is not true, then there was an issue placing the order. The following errorMessages are possible:
​
Error
Error	Success	Message	Description
INVALID_ORDER_MIN_TICK_SIZE	yes	order is invalid. Price breaks minimum tick size rules	order price isn’t accurate to correct tick sizing
INVALID_ORDER_MIN_SIZE	yes	order is invalid. Size lower than the minimum	order size must meet min size threshold requirement
INVALID_ORDER_DUPLICATED	yes	order is invalid. Duplicated. Same order has already been placed, can’t be placed again	
INVALID_ORDER_NOT_ENOUGH_BALANCE	yes	not enough balance / allowance	funder address doesn’t have sufficient balance or allowance for order
INVALID_ORDER_EXPIRATION	yes	invalid expiration	expiration field expresses a time before now
INVALID_ORDER_ERROR	yes	could not insert order	system error while inserting order
INVALID_POST_ONLY_ORDER_TYPE	yes	invalid post-only order: only GTC and GTD order types are allowed	post only flag attached to a market order
INVALID_POST_ONLY_ORDER	yes	invalid post-only order: order crosses book	post only order would match
EXECUTION_ERROR	yes	could not run the execution	system error while attempting to execute trade
ORDER_DELAYED	no	order match delayed due to market conditions	order placement delayed
DELAYING_ORDER_ERROR	yes	error delaying the order	system error while delaying order
FOK_ORDER_NOT_FILLED_ERROR	yes	order couldn’t be fully filled, FOK orders are fully filled/killed	FOK order not fully filled so can’t be placed
MARKET_NOT_READY	no	the market is not yet ready to process new orders	system not accepting orders for market yet
​
Insert Statuses
When placing an order, a status field is included. The status field provides additional information regarding the order’s state as a result of the placement. Possible values include:
​
Status
Status	Description
matched	order placed and matched with an existing resting order
live	order placed and resting on the book
delayed	order marketable, but subject to matching delay
unmatched	order marketable, but failure delaying, placement successful
Place Single Order
Get Order
Ask a question...

github
Powered by
Place Multiple Orders (Batching) - Polymarket Documentation

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.polymarket.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Order

> Get information about an existing order

<Tip>This endpoint requires a L2 Header. </Tip>

Get single order by id.

**HTTP REQUEST**

`GET /<clob-endpoint>/data/order/<order_hash>`

### Request Parameters

| Name | Required | Type   | Description                          |
| ---- | -------- | ------ | ------------------------------------ |
| id   | no       | string | id of order to get information about |

### Response Format

| Name  | Type      | Description        |
| ----- | --------- | ------------------ |
| order | OpenOrder | order if it exists |

An `OpenOrder` object is of the form:

| Name              | Type      | Description                                                    |
| ----------------- | --------- | -------------------------------------------------------------- |
| associate\_trades | string\[] | any Trade id the order has been partially included in          |
| id                | string    | order id                                                       |
| status            | string    | order current status                                           |
| market            | string    | market id (condition id)                                       |
| original\_size    | string    | original order size at placement                               |
| outcome           | string    | human readable outcome the order is for                        |
| maker\_address    | string    | maker address (funder)                                         |
| owner             | string    | api key                                                        |
| price             | string    | price                                                          |
| side              | string    | buy or sell                                                    |
| size\_matched     | string    | size of order that has been matched/filled                     |
| asset\_id         | string    | token id                                                       |
| expiration        | string    | unix timestamp when the order expired, 0 if it does not expire |
| type              | string    | order type (GTC, FOK, GTD)                                     |
| created\_at       | string    | unix timestamp when the order was created                      |

<RequestExample>
  ```python Python theme={null}
  order = clob_client.get_order("0xb816482a5187a3d3db49cbaf6fe3ddf24f53e6c712b5a4bf5e01d0ec7b11dabc")
  print(order)
  ```

  ```javascript Typescript theme={null}
  async function main() {
    const order = await clobClient.getOrder(
      "0xb816482a5187a3d3db49cbaf6fe3ddf24f53e6c712b5a4bf5e01d0ec7b11dabc"
    );
    console.log(order);
  }

  main();

  ```
</RequestExample>


Skip to main content
Polymarket Documentation home pagedark logo

Search...
Ctrl K

Ask AI
Main Site

User Guide
For Developers
Changelog
Polymarket
Discord Community
Twitter
Developer Quickstart
Developer Quickstart
Fetching Market Data
Placing Your First Order
Glossary
API Rate Limits
Endpoints
Market Makers
Market Maker Introduction
Setup
Trading
Liquidity Rewards
Maker Rebates Program
Data Feeds
Inventory Management
Polymarket Builders Program
Builder Program Introduction
Builder Tiers
Builder Profile & Keys
Order Attribution
Relayer Client
Examples
Central Limit Order Book
CLOB Introduction
Status
Quickstart
Authentication
Geographic Restrictions

Client
Methods Overview
Public Methods
L1 Methods
L2 Methods
Builder Methods

REST API

Orderbook
GET
Get order book summary
POST
Get multiple order books summaries by request

Pricing
GET
Get market price
GET
Get multiple market prices
POST
Get multiple market prices by request
GET
Get midpoint price
GET
Get price history for a traded token

Spreads
POST
Get bid-ask spreads

Historical Timeseries Data
GET
Historical Timeseries Data

Order Management
Orders Overview
Place Single Order
Place Multiple Orders (Batching)
Get Order
Get Active Orders
Check Order Reward Scoring
Cancel Orders(s)
Onchain Order Info

Trades
Websocket
WSS Overview
WSS Quickstart
WSS Authentication
User Channel
Market Channel

Sports Websocket
Real Time Data Stream
RTDS Overview
RTDS Crypto Prices
RTDS Comments
Gamma Structure
Overview
Gamma Structure
Fetching Markets
Gamma Endpoints

Gamma Status

Sports

Tags

Events

Markets

Series

Comments

Profiles

Search
Data-API

Data API Status

Core

Misc

Builders
Bridge & Swap
Overview

Bridge
Subgraph
Overview
Resolution
Resolution
Conditional Token Frameworks
Overview
Splitting USDC
Merging Tokens
Reedeeming Tokens
Deployment and Additional Information
Proxy Wallets
Proxy wallet
Negative Risk
Overview

Python

Typescript
from py_clob_client.clob_types import OpenOrderParams

resp = client.get_orders(
    OpenOrderParams(
        market="0xbd31dc8a20211944f6b70f31557f1001557b59905b7738480ca09bd4532f84af",
    )
)
print(resp)
print("Done!")
Order Management
Get Active Orders
This endpoint requires a L2 Header.
Get active order(s) for a specific market.
HTTP REQUEST
GET /<clob-endpoint>/data/orders
​
Request Parameters
Name	Required	Type	Description
id	no	string	id of order to get information about
market	no	string	condition id of market
asset_id	no	string	id of the asset/token
​
Response Format
Name	Type	Description
null	OpenOrder[]	list of open orders filtered by the query parameters
Get Order
Check Order Reward Scoring
Ask a question...

github
Powered by
Get Active Orders - Polymarket Documentation

Skip to main content
Polymarket Documentation home pagedark logo

Search...
Ctrl K

Ask AI
Main Site

User Guide
For Developers
Changelog
Polymarket
Discord Community
Twitter
Developer Quickstart
Developer Quickstart
Fetching Market Data
Placing Your First Order
Glossary
API Rate Limits
Endpoints
Market Makers
Market Maker Introduction
Setup
Trading
Liquidity Rewards
Maker Rebates Program
Data Feeds
Inventory Management
Polymarket Builders Program
Builder Program Introduction
Builder Tiers
Builder Profile & Keys
Order Attribution
Relayer Client
Examples
Central Limit Order Book
CLOB Introduction
Status
Quickstart
Authentication
Geographic Restrictions

Client
Methods Overview
Public Methods
L1 Methods
L2 Methods
Builder Methods

REST API

Orderbook
GET
Get order book summary
POST
Get multiple order books summaries by request

Pricing
GET
Get market price
GET
Get multiple market prices
POST
Get multiple market prices by request
GET
Get midpoint price
GET
Get price history for a traded token

Spreads
POST
Get bid-ask spreads

Historical Timeseries Data
GET
Historical Timeseries Data

Order Management
Orders Overview
Place Single Order
Place Multiple Orders (Batching)
Get Order
Get Active Orders
Check Order Reward Scoring
Cancel Orders(s)
Onchain Order Info

Trades
Websocket
WSS Overview
WSS Quickstart
WSS Authentication
User Channel
Market Channel

Sports Websocket
Real Time Data Stream
RTDS Overview
RTDS Crypto Prices
RTDS Comments
Gamma Structure
Overview
Gamma Structure
Fetching Markets
Gamma Endpoints

Gamma Status

Sports

Tags

Events

Markets

Series

Comments

Profiles

Search
Data-API

Data API Status

Core

Misc

Builders
Bridge & Swap
Overview

Bridge
Subgraph
Overview
Resolution
Resolution
Conditional Token Frameworks
Overview
Splitting USDC
Merging Tokens
Reedeeming Tokens
Deployment and Additional Information
Proxy Wallets
Proxy wallet
Negative Risk
Overview

Python

Typescript
scoring = client.is_order_scoring(
    OrderScoringParams(
        orderId="0x..."
    )
)
print(scoring)

scoring = client.are_orders_scoring(
    OrdersScoringParams(
        orderIds=["0x..."]
    )
)
print(scoring)
Order Management
Check Order Reward Scoring
Check if an order is eligble or scoring for Rewards purposes

This endpoint requires a L2 Header.
Returns a boolean value where it is indicated if an order is scoring or not.
HTTP REQUEST
GET /<clob-endpoint>/order-scoring?order_id={...}
​
Request Parameters
Name	Required	Type	Description
orderId	yes	string	id of order to get information about
​
Response Format
Name	Type	Description
null	OrdersScoring	order scoring data
An OrdersScoring object is of the form:
Name	Type	Description
scoring	boolean	indicates if the order is scoring or not
​
Check if some orders are scoring
This endpoint requires a L2 Header.
Returns to a dictionary with boolean value where it is indicated if an order is scoring or not.
HTTP REQUEST
POST /<clob-endpoint>/orders-scoring
​
Request Parameters
Name	Required	Type	Description
orderIds	yes	string[]	ids of the orders to get information about
​
Response Format
Name	Type	Description
null	OrdersScoring	orders scoring data
An OrdersScoring object is a dictionary that indicates the order by if it score.
Get Active Orders
Cancel Orders(s)
Ask a question...

github
Powered by
Check Order Reward Scoring - Polymarket Documentation

Skip to main content
Polymarket Documentation home pagedark logo

Search...
Ctrl K

Ask AI
Main Site

User Guide
For Developers
Changelog
Polymarket
Discord Community
Twitter
Developer Quickstart
Developer Quickstart
Fetching Market Data
Placing Your First Order
Glossary
API Rate Limits
Endpoints
Market Makers
Market Maker Introduction
Setup
Trading
Liquidity Rewards
Maker Rebates Program
Data Feeds
Inventory Management
Polymarket Builders Program
Builder Program Introduction
Builder Tiers
Builder Profile & Keys
Order Attribution
Relayer Client
Examples
Central Limit Order Book
CLOB Introduction
Status
Quickstart
Authentication
Geographic Restrictions

Client
Methods Overview
Public Methods
L1 Methods
L2 Methods
Builder Methods

REST API

Orderbook
GET
Get order book summary
POST
Get multiple order books summaries by request

Pricing
GET
Get market price
GET
Get multiple market prices
POST
Get multiple market prices by request
GET
Get midpoint price
GET
Get price history for a traded token

Spreads
POST
Get bid-ask spreads

Historical Timeseries Data
GET
Historical Timeseries Data

Order Management
Orders Overview
Place Single Order
Place Multiple Orders (Batching)
Get Order
Get Active Orders
Check Order Reward Scoring
Cancel Orders(s)
Onchain Order Info

Trades
Websocket
WSS Overview
WSS Quickstart
WSS Authentication
User Channel
Market Channel

Sports Websocket
Real Time Data Stream
RTDS Overview
RTDS Crypto Prices
RTDS Comments
Gamma Structure
Overview
Gamma Structure
Fetching Markets
Gamma Endpoints

Gamma Status

Sports

Tags

Events

Markets

Series

Comments

Profiles

Search
Data-API

Data API Status

Core

Misc

Builders
Bridge & Swap
Overview

Bridge
Subgraph
Overview
Resolution
Resolution
Conditional Token Frameworks
Overview
Splitting USDC
Merging Tokens
Reedeeming Tokens
Deployment and Additional Information
Proxy Wallets
Proxy wallet
Negative Risk
Overview

On this page
Cancel an single Order
Request Payload Parameters
Response Format
Cancel Multiple Orders
Request Payload Parameters
Response Format
Cancel ALL Orders
Response Format
Cancel orders from market
Request Payload Parameters
Response Format
Order Management
Cancel Orders(s)
Multiple endpoints to cancel a single order, multiple orders, all orders or all orders from a single market.

​
Cancel an single Order
This endpoint requires a L2 Header.
Cancel an order.
HTTP REQUEST
DELETE /<clob-endpoint>/order
​
Request Payload Parameters
Name	Required	Type	Description
orderID	yes	string	ID of order to cancel
​
Response Format
Name	Type	Description
canceled	string[]	list of canceled orders
not_canceled		a order id -> reason map that explains why that order couldn’t be canceled

Python

Typescript
resp = client.cancel(order_id="0x38a73eed1e6d177545e9ab027abddfb7e08dbe975fa777123b1752d203d6ac88")
print(resp)
​
Cancel Multiple Orders
This endpoint requires a L2 Header.
HTTP REQUEST
DELETE /<clob-endpoint>/orders
​
Request Payload Parameters
Name	Required	Type	Description
null	yes	string[]	IDs of the orders to cancel
​
Response Format
Name	Type	Description
canceled	string[]	list of canceled orders
not_canceled		a order id -> reason map that explains why that order couldn’t be canceled

Python

Typescript
resp = client.cancel_orders(["0x38a73eed1e6d177545e9ab027abddfb7e08dbe975fa777123b1752d203d6ac88", "0xaaaa..."])
print(resp)
​
Cancel ALL Orders
This endpoint requires a L2 Header.
Cancel all open orders posted by a user.
HTTP REQUEST
DELETE /<clob-endpoint>/cancel-all
​
Response Format
Name	Type	Description
canceled	string[]	list of canceled orders
not_canceled		a order id -> reason map that explains why that order couldn’t be canceled

Python

Typescript
resp = client.cancel_all()
print(resp)
print("Done!")
​
Cancel orders from market
This endpoint requires a L2 Header.
Cancel orders from market.
HTTP REQUEST
DELETE /<clob-endpoint>/cancel-market-orders
​
Request Payload Parameters
Name	Required	Type	Description
market	no	string	condition id of the market
asset_id	no	string	id of the asset/token
​
Response Format
Name	Type	Description
canceled	string[]	list of canceled orders
not_canceled		a order id -> reason map that explains why that order couldn’t be canceled

Python

Typescript
resp = client.cancel_market_orders(market="0xbd31dc8a20211944f6b70f31557f1001557b59905b7738480ca09bd4532f84af", asset_id="52114319501245915516055106046884209969926127482827954674443846427813813222426")
print(resp)

Check Order Reward Scoring
Onchain Order Info
Ask a question...

github
Powered by
Cancel Orders(s) - Polymarket Documentation

Skip to main content
Polymarket Documentation home pagedark logo

Search...
Ctrl K

Ask AI
Main Site

User Guide
For Developers
Changelog
Polymarket
Discord Community
Twitter
Developer Quickstart
Developer Quickstart
Fetching Market Data
Placing Your First Order
Glossary
API Rate Limits
Endpoints
Market Makers
Market Maker Introduction
Setup
Trading
Liquidity Rewards
Maker Rebates Program
Data Feeds
Inventory Management
Polymarket Builders Program
Builder Program Introduction
Builder Tiers
Builder Profile & Keys
Order Attribution
Relayer Client
Examples
Central Limit Order Book
CLOB Introduction
Status
Quickstart
Authentication
Geographic Restrictions

Client
Methods Overview
Public Methods
L1 Methods
L2 Methods
Builder Methods

REST API

Orderbook
GET
Get order book summary
POST
Get multiple order books summaries by request

Pricing
GET
Get market price
GET
Get multiple market prices
POST
Get multiple market prices by request
GET
Get midpoint price
GET
Get price history for a traded token

Spreads
POST
Get bid-ask spreads

Historical Timeseries Data
GET
Historical Timeseries Data

Order Management
Orders Overview
Place Single Order
Place Multiple Orders (Batching)
Get Order
Get Active Orders
Check Order Reward Scoring
Cancel Orders(s)
Onchain Order Info

Trades
Websocket
WSS Overview
WSS Quickstart
WSS Authentication
User Channel
Market Channel

Sports Websocket
Real Time Data Stream
RTDS Overview
RTDS Crypto Prices
RTDS Comments
Gamma Structure
Overview
Gamma Structure
Fetching Markets
Gamma Endpoints

Gamma Status

Sports

Tags

Events

Markets

Series

Comments

Profiles

Search
Data-API

Data API Status

Core

Misc

Builders
Bridge & Swap
Overview

Bridge
Subgraph
Overview
Resolution
Resolution
Conditional Token Frameworks
Overview
Splitting USDC
Merging Tokens
Reedeeming Tokens
Deployment and Additional Information
Proxy Wallets
Proxy wallet
Negative Risk
Overview

On this page
How do I interpret the OrderFilled onchain event?
Order Management
Onchain Order Info
​
How do I interpret the OrderFilled onchain event?
Given an OrderFilled event:
orderHash: a unique hash for the Order being filled
maker: the user generating the order and the source of funds for the order
taker: the user filling the order OR the Exchange contract if the order fills multiple limit orders
makerAssetId: id of the asset that is given out. If 0, indicates that the Order is a BUY, giving USDC in exchange for Outcome tokens. Else, indicates that the Order is a SELL, giving Outcome tokens in exchange for USDC.
takerAssetId: id of the asset that is received. If 0, indicates that the Order is a SELL, receiving USDC in exchange for Outcome tokens. Else, indicates that the Order is a BUY, receiving Outcome tokens in exchange for USDC.
makerAmountFilled: the amount of the asset that is given out.
takerAmountFilled: the amount of the asset that is received.
fee: the fees paid by the order maker
Cancel Orders(s)
Trades Overview
Ask a question...

github
Powered by
Onchain Order Info - Polymarket Documentation

Skip to main content
Polymarket Documentation home pagedark logo

Search...
Ctrl K

Ask AI
Main Site

User Guide
For Developers
Changelog
Polymarket
Discord Community
Twitter
Developer Quickstart
Developer Quickstart
Fetching Market Data
Placing Your First Order
Glossary
API Rate Limits
Endpoints
Market Makers
Market Maker Introduction
Setup
Trading
Liquidity Rewards
Maker Rebates Program
Data Feeds
Inventory Management
Polymarket Builders Program
Builder Program Introduction
Builder Tiers
Builder Profile & Keys
Order Attribution
Relayer Client
Examples
Central Limit Order Book
CLOB Introduction
Status
Quickstart
Authentication
Geographic Restrictions

Client
Methods Overview
Public Methods
L1 Methods
L2 Methods
Builder Methods

REST API

Orderbook
GET
Get order book summary
POST
Get multiple order books summaries by request

Pricing
GET
Get market price
GET
Get multiple market prices
POST
Get multiple market prices by request
GET
Get midpoint price
GET
Get price history for a traded token

Spreads
POST
Get bid-ask spreads

Historical Timeseries Data
GET
Historical Timeseries Data

Order Management
Orders Overview
Place Single Order
Place Multiple Orders (Batching)
Get Order
Get Active Orders
Check Order Reward Scoring
Cancel Orders(s)
Onchain Order Info

Trades
Trades Overview
Get Trades
Websocket
WSS Overview
WSS Quickstart
WSS Authentication
User Channel
Market Channel

Sports Websocket
Real Time Data Stream
RTDS Overview
RTDS Crypto Prices
RTDS Comments
Gamma Structure
Overview
Gamma Structure
Fetching Markets
Gamma Endpoints

Gamma Status

Sports

Tags

Events

Markets

Series

Comments

Profiles

Search
Data-API

Data API Status

Core

Misc

Builders
Bridge & Swap
Overview

Bridge
Subgraph
Overview
Resolution
Resolution
Conditional Token Frameworks
Overview
Splitting USDC
Merging Tokens
Reedeeming Tokens
Deployment and Additional Information
Proxy Wallets
Proxy wallet
Negative Risk
Overview

On this page
Overview
Statuses
Trades
Trades Overview
​
Overview
All historical trades can be fetched via the Polymarket CLOB REST API. A trade is initiated by a “taker” who creates a marketable limit order. This limit order can be matched against one or more resting limit orders on the associated book. A trade can be in various states as described below. Note: in some cases (due to gas limitations) the execution of a “trade” must be broken into multiple transactions which case separate trade entities will be returned. To associate trade entities, there is a bucket_index field and a match_time field. Trades that have been broken into multiple trade objects can be reconciled by combining trade objects with the same market_order_id, match_time and incrementing bucket_index’s into a top level “trade” client side.
​
Statuses
Status	Terminal?	Description
MATCHED	no	trade has been matched and sent to the executor service by the operator, the executor service submits the trade as a transaction to the Exchange contract
MINED	no	trade is observed to be mined into the chain, no finality threshold established
CONFIRMED	yes	trade has achieved strong probabilistic finality and was successful
RETRYING	no	trade transaction has failed (revert or reorg) and is being retried/resubmitted by the operator
FAILED	yes	trade has failed and is not being retried
Onchain Order Info
Get Trades
Ask a question...

github
Powered by
Trades Overview - Polymarket Documentation

Skip to main content
Polymarket Documentation home pagedark logo

Search...
Ctrl K

Ask AI
Main Site

User Guide
For Developers
Changelog
Polymarket
Discord Community
Twitter
Developer Quickstart
Developer Quickstart
Fetching Market Data
Placing Your First Order
Glossary
API Rate Limits
Endpoints
Market Makers
Market Maker Introduction
Setup
Trading
Liquidity Rewards
Maker Rebates Program
Data Feeds
Inventory Management
Polymarket Builders Program
Builder Program Introduction
Builder Tiers
Builder Profile & Keys
Order Attribution
Relayer Client
Examples
Central Limit Order Book
CLOB Introduction
Status
Quickstart
Authentication
Geographic Restrictions

Client
Methods Overview
Public Methods
L1 Methods
L2 Methods
Builder Methods

REST API

Orderbook
GET
Get order book summary
POST
Get multiple order books summaries by request

Pricing
GET
Get market price
GET
Get multiple market prices
POST
Get multiple market prices by request
GET
Get midpoint price
GET
Get price history for a traded token

Spreads
POST
Get bid-ask spreads

Historical Timeseries Data
GET
Historical Timeseries Data

Order Management
Orders Overview
Place Single Order
Place Multiple Orders (Batching)
Get Order
Get Active Orders
Check Order Reward Scoring
Cancel Orders(s)
Onchain Order Info

Trades
Trades Overview
Get Trades
Websocket
WSS Overview
WSS Quickstart
WSS Authentication
User Channel
Market Channel

Sports Websocket
Real Time Data Stream
RTDS Overview
RTDS Crypto Prices
RTDS Comments
Gamma Structure
Overview
Gamma Structure
Fetching Markets
Gamma Endpoints

Gamma Status

Sports

Tags

Events

Markets

Series

Comments

Profiles

Search
Data-API

Data API Status

Core

Misc

Builders
Bridge & Swap
Overview

Bridge
Subgraph
Overview
Resolution
Resolution
Conditional Token Frameworks
Overview
Splitting USDC
Merging Tokens
Reedeeming Tokens
Deployment and Additional Information
Proxy Wallets
Proxy wallet
Negative Risk
Overview

Python

Typescript
from py_clob_client.clob_types import TradeParams

resp = client.get_trades(
    TradeParams(
        maker_address=client.get_address(),
        market="0xbd31dc8a20211944f6b70f31557f1001557b59905b7738480ca09bd4532f84af",
    ),
)
print(resp)
print("Done!")
Trades
Get Trades
This endpoint requires a L2 Header.
Get trades for the authenticated user based on the provided filters.
HTTP REQUEST
GET /<clob-endpoint>/data/trades
​
Request Parameters
Name	Required	Type	Description
id	no	string	id of trade to fetch
taker	no	string	address to get trades for where it is included as a taker
maker	no	string	address to get trades for where it is included as a maker
market	no	string	market for which to get the trades (condition ID)
before	no	string	unix timestamp representing the cutoff up to which trades that happened before then can be included
after	no	string	unix timestamp representing the cutoff for which trades that happened after can be included
​
Response Format
Name	Type	Description
null	Trade[]	list of trades filtered by query parameters
A Trade object is of the form:
Name	Type	Description
id	string	trade id
taker_order_id	string	hash of taker order (market order) that catalyzed the trade
market	string	market id (condition id)
asset_id	string	asset id (token id) of taker order (market order)
side	string	buy or sell
size	string	size
fee_rate_bps	string	the fees paid for the taker order expressed in basic points
price	string	limit price of taker order
status	string	trade status (see above)
match_time	string	time at which the trade was matched
last_update	string	timestamp of last status update
outcome	string	human readable outcome of the trade
maker_address	string	funder address of the taker of the trade
owner	string	api key of taker of the trade
transaction_hash	string	hash of the transaction where the trade was executed
bucket_index	integer	index of bucket for trade in case trade is executed in multiple transactions
maker_orders	MakerOrder[]	list of the maker trades the taker trade was filled against
type	string	side of the trade: TAKER or MAKER
A MakerOrder object is of the form:
Name	Type	Description
order_id	string	id of maker order
maker_address	string	maker address of the order
owner	string	api key of the owner of the order
matched_amount	string	size of maker order consumed with this trade
fee_rate_bps	string	the fees paid for the taker order expressed in basic points
price	string	price of maker order
asset_id	string	token/asset id
outcome	string	human readable outcome of the maker order
side	string	the side of the maker order. Can be buy or sell
Trades Overview
WSS Overview
Ask a question...

github
Powered by
Get Trades - Polymarket Documentation

Skip to main content
Polymarket Documentation home pagedark logo

Search...
Ctrl K

Ask AI
Main Site

User Guide
For Developers
Changelog
Polymarket
Discord Community
Twitter
Developer Quickstart
Developer Quickstart
Fetching Market Data
Placing Your First Order
Glossary
API Rate Limits
Endpoints
Market Makers
Market Maker Introduction
Setup
Trading
Liquidity Rewards
Maker Rebates Program
Data Feeds
Inventory Management
Polymarket Builders Program
Builder Program Introduction
Builder Tiers
Builder Profile & Keys
Order Attribution
Relayer Client
Examples
Central Limit Order Book
CLOB Introduction
Status
Quickstart
Authentication
Geographic Restrictions

Client
Methods Overview
Public Methods
L1 Methods
L2 Methods
Builder Methods

REST API

Orderbook
GET
Get order book summary
POST
Get multiple order books summaries by request

Pricing
GET
Get market price
GET
Get multiple market prices
POST
Get multiple market prices by request
GET
Get midpoint price
GET
Get price history for a traded token

Spreads
POST
Get bid-ask spreads

Historical Timeseries Data
GET
Historical Timeseries Data

Order Management
Orders Overview
Place Single Order
Place Multiple Orders (Batching)
Get Order
Get Active Orders
Check Order Reward Scoring
Cancel Orders(s)
Onchain Order Info

Trades
Trades Overview
Get Trades
Websocket
WSS Overview
WSS Quickstart
WSS Authentication
User Channel
Market Channel

Sports Websocket
Real Time Data Stream
RTDS Overview
RTDS Crypto Prices
RTDS Comments
Gamma Structure
Overview
Gamma Structure
Fetching Markets
Gamma Endpoints

Gamma Status

Sports

Tags

Events

Markets

Series

Comments

Profiles

Search
Data-API

Data API Status

Core

Misc

Builders
Bridge & Swap
Overview

Bridge
Subgraph
Overview
Resolution
Resolution
Conditional Token Frameworks
Overview
Splitting USDC
Merging Tokens
Reedeeming Tokens
Deployment and Additional Information
Proxy Wallets
Proxy wallet
Negative Risk
Overview

On this page
Overview
Subscription
Subscribe to more assets
Websocket
WSS Overview
Overview and general information about the Polymarket Websocket

​
Overview
The Polymarket CLOB API provides websocket (wss) channels through which clients can get pushed updates. These endpoints allow clients to maintain almost real-time views of their orders, their trades and markets in general. There are two available channels user and market.
​
Subscription
To subscribe send a message including the following authentication and intent information upon opening the connection.
Field	Type	Description
auth	Auth	see next page for auth information
markets	string[]	array of markets (condition IDs) to receive events for (for user channel)
assets_ids	string[]	array of asset ids (token IDs) to receive events for (for market channel)
type	string	id of channel to subscribe to (USER or MARKET)
custom_feature_enabled	bool	enabling / disabling custom features
Where the auth field is of type Auth which has the form described in the WSS Authentication section below.
​
Subscribe to more assets
Once connected, the client can subscribe and unsubscribe to asset_ids by sending the following message:
Field	Type	Description
assets_ids	string[]	array of asset ids (token IDs) to receive events for (for market channel)
markets	string[]	array of market ids (condition IDs) to receive events for (for user channel)
operation	string	”subscribe” or “unsubscribe”
custom_feature_enabled	bool	enabling / disabling custom features
Get Trades
WSS Quickstart
Ask a question...

github
Powered by
WSS Overview - Polymarket Documentation

Skip to main content
Polymarket Documentation home pagedark logo

Search...
Ctrl K

Ask AI
Main Site

User Guide
For Developers
Changelog
Polymarket
Discord Community
Twitter
Developer Quickstart
Developer Quickstart
Fetching Market Data
Placing Your First Order
Glossary
API Rate Limits
Endpoints
Market Makers
Market Maker Introduction
Setup
Trading
Liquidity Rewards
Maker Rebates Program
Data Feeds
Inventory Management
Polymarket Builders Program
Builder Program Introduction
Builder Tiers
Builder Profile & Keys
Order Attribution
Relayer Client
Examples
Central Limit Order Book
CLOB Introduction
Status
Quickstart
Authentication
Geographic Restrictions

Client
Methods Overview
Public Methods
L1 Methods
L2 Methods
Builder Methods

REST API

Orderbook
GET
Get order book summary
POST
Get multiple order books summaries by request

Pricing
GET
Get market price
GET
Get multiple market prices
POST
Get multiple market prices by request
GET
Get midpoint price
GET
Get price history for a traded token

Spreads
POST
Get bid-ask spreads

Historical Timeseries Data
GET
Historical Timeseries Data

Order Management
Orders Overview
Place Single Order
Place Multiple Orders (Batching)
Get Order
Get Active Orders
Check Order Reward Scoring
Cancel Orders(s)
Onchain Order Info

Trades
Trades Overview
Get Trades
Websocket
WSS Overview
WSS Quickstart
WSS Authentication
User Channel
Market Channel

Sports Websocket
Real Time Data Stream
RTDS Overview
RTDS Crypto Prices
RTDS Comments
Gamma Structure
Overview
Gamma Structure
Fetching Markets
Gamma Endpoints

Gamma Status

Sports

Tags

Events

Markets

Series

Comments

Profiles

Search
Data-API

Data API Status

Core

Misc

Builders
Bridge & Swap
Overview

Bridge
Subgraph
Overview
Resolution
Resolution
Conditional Token Frameworks
Overview
Splitting USDC
Merging Tokens
Reedeeming Tokens
Deployment and Additional Information
Proxy Wallets
Proxy wallet
Negative Risk
Overview

On this page
Getting your API Keys
Using those keys to connect to the Market or User Websocket
Websocket
WSS Quickstart
The following code samples and explanation will show you how to subscribe to the Marker and User channels of the Websocket. You’ll need your API keys to do this so we’ll start with that.
​
Getting your API Keys

DeriveAPIKeys-Python

DeriveAPIKeys-TS
from py_clob_client.client import ClobClient

host: str = "https://clob.polymarket.com"
key: str = "" #This is your Private Key. If using email login export from https://reveal.magic.link/polymarket otherwise export from your Web3 Application
chain_id: int = 137 #No need to adjust this
POLYMARKET_PROXY_ADDRESS: str = '' #This is the address you deposit/send USDC to to FUND your Polymarket account.

#Select from the following 3 initialization options to matches your login method, and remove any unused lines so only one client is initialized.

### Initialization of a client using a Polymarket Proxy associated with an Email/Magic account. If you login with your email use this example.
client = ClobClient(host, key=key, chain_id=chain_id, signature_type=1, funder=POLYMARKET_PROXY_ADDRESS)

### Initialization of a client using a Polymarket Proxy associated with a Browser Wallet(Metamask, Coinbase Wallet, etc)
client = ClobClient(host, key=key, chain_id=chain_id, signature_type=2, funder=POLYMARKET_PROXY_ADDRESS)

### Initialization of a client that trades directly from an EOA. 
client = ClobClient(host, key=key, chain_id=chain_id)

print( client.derive_api_key() )

See all 20 lines
​
Using those keys to connect to the Market or User Websocket

WSS-Connection
from websocket import WebSocketApp
import json
import time
import threading

MARKET_CHANNEL = "market"
USER_CHANNEL = "user"


class WebSocketOrderBook:
    def __init__(self, channel_type, url, data, auth, message_callback, verbose):
        self.channel_type = channel_type
        self.url = url
        self.data = data
        self.auth = auth
        self.message_callback = message_callback
        self.verbose = verbose
        furl = url + "/ws/" + channel_type
        self.ws = WebSocketApp(
            furl,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close,
            on_open=self.on_open,
        )
        self.orderbooks = {}

    def on_message(self, ws, message):
        print(message)
        pass

    def on_error(self, ws, error):
        print("Error: ", error)
        exit(1)

    def on_close(self, ws, close_status_code, close_msg):
        print("closing")
        exit(0)

    def on_open(self, ws):
        if self.channel_type == MARKET_CHANNEL:
            ws.send(json.dumps({"assets_ids": self.data, "type": MARKET_CHANNEL}))
        elif self.channel_type == USER_CHANNEL and self.auth:
            ws.send(
                json.dumps(
                    {"markets": self.data, "type": USER_CHANNEL, "auth": self.auth}
                )
            )
        else:
            exit(1)

        thr = threading.Thread(target=self.ping, args=(ws,))
        thr.start()


    def subscribe_to_tokens_ids(self, assets_ids):
        if self.channel_type == MARKET_CHANNEL:
            self.ws.send(json.dumps({"assets_ids": assets_ids, "operation": "subscribe"}))

    def unsubscribe_to_tokens_ids(self, assets_ids):
        if self.channel_type == MARKET_CHANNEL:
            self.ws.send(json.dumps({"assets_ids": assets_ids, "operation": "unsubscribe"}))


    def ping(self, ws):
        while True:
            ws.send("PING")
            time.sleep(10)

    def run(self):
        self.ws.run_forever()


if __name__ == "__main__":
    url = "wss://ws-subscriptions-clob.polymarket.com"
    #Complete these by exporting them from your initialized client. 
    api_key = ""
    api_secret = ""
    api_passphrase = ""

    asset_ids = [
        "109681959945973300464568698402968596289258214226684818748321941747028805721376",
    ]
    condition_ids = [] # no really need to filter by this one

    auth = {"apiKey": api_key, "secret": api_secret, "passphrase": api_passphrase}

    market_connection = WebSocketOrderBook(
        MARKET_CHANNEL, url, asset_ids, auth, None, True
    )
    user_connection = WebSocketOrderBook(
        USER_CHANNEL, url, condition_ids, auth, None, True
    )

    market_connection.subscribe_to_tokens_ids(["123"])
    # market_connection.unsubscribe_to_tokens_ids(["123"])

    market_connection.run()
    # user_connection.run()
See all 99 lines
WSS Overview
WSS Authentication
Ask a question...

github
Powered by
WSS Quickstart - Polymarket Documentation

Skip to main content
Polymarket Documentation home pagedark logo

Search...
Ctrl K

Ask AI
Main Site

User Guide
For Developers
Changelog
Polymarket
Discord Community
Twitter
Developer Quickstart
Developer Quickstart
Fetching Market Data
Placing Your First Order
Glossary
API Rate Limits
Endpoints
Market Makers
Market Maker Introduction
Setup
Trading
Liquidity Rewards
Maker Rebates Program
Data Feeds
Inventory Management
Polymarket Builders Program
Builder Program Introduction
Builder Tiers
Builder Profile & Keys
Order Attribution
Relayer Client
Examples
Central Limit Order Book
CLOB Introduction
Status
Quickstart
Authentication
Geographic Restrictions

Client
Methods Overview
Public Methods
L1 Methods
L2 Methods
Builder Methods

REST API

Orderbook
GET
Get order book summary
POST
Get multiple order books summaries by request

Pricing
GET
Get market price
GET
Get multiple market prices
POST
Get multiple market prices by request
GET
Get midpoint price
GET
Get price history for a traded token

Spreads
POST
Get bid-ask spreads

Historical Timeseries Data
GET
Historical Timeseries Data

Order Management
Orders Overview
Place Single Order
Place Multiple Orders (Batching)
Get Order
Get Active Orders
Check Order Reward Scoring
Cancel Orders(s)
Onchain Order Info

Trades
Trades Overview
Get Trades
Websocket
WSS Overview
WSS Quickstart
WSS Authentication
User Channel
Market Channel

Sports Websocket
Real Time Data Stream
RTDS Overview
RTDS Crypto Prices
RTDS Comments
Gamma Structure
Overview
Gamma Structure
Fetching Markets
Gamma Endpoints

Gamma Status

Sports

Tags

Events

Markets

Series

Comments

Profiles

Search
Data-API

Data API Status

Core

Misc

Builders
Bridge & Swap
Overview

Bridge
Subgraph
Overview
Resolution
Resolution
Conditional Token Frameworks
Overview
Splitting USDC
Merging Tokens
Reedeeming Tokens
Deployment and Additional Information
Proxy Wallets
Proxy wallet
Negative Risk
Overview
Websocket
WSS Authentication
Only connections to user channel require authentication.
Field	Optional	Description
apikey	yes	Polygon account’s CLOB api key
secret	yes	Polygon account’s CLOB api secret
passphrase	yes	Polygon account’s CLOB api passphrase
WSS Quickstart
User Channel
Ask a question...

github
Powered by
WSS Authentication - Polymarket Documentation

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.polymarket.com/llms.txt
> Use this file to discover all available pages before exploring further.

# User Channel

Authenticated channel for updates related to user activities (orders, trades), filtered for authenticated user by apikey.

**SUBSCRIBE**

`<wss-channel> user`

## Trade Message

Emitted when:

* when a market order is matched ("MATCHED")
* when a limit order for the user is included in a trade ("MATCHED")
* subsequent status changes for trade ("MINED", "CONFIRMED", "RETRYING", "FAILED")

### Structure

| Name             | Type          | Description                                 |
| ---------------- | ------------- | ------------------------------------------- |
| asset\_id        | string        | asset id (token ID) of order (market order) |
| event\_type      | string        | "trade"                                     |
| id               | string        | trade id                                    |
| last\_update     | string        | time of last update to trade                |
| maker\_orders    | MakerOrder\[] | array of maker order details                |
| market           | string        | market identifier (condition ID)            |
| matchtime        | string        | time trade was matched                      |
| outcome          | string        | outcome                                     |
| owner            | string        | api key of event owner                      |
| price            | string        | price                                       |
| side             | string        | BUY/SELL                                    |
| size             | string        | size                                        |
| status           | string        | trade status                                |
| taker\_order\_id | string        | id of taker order                           |
| timestamp        | string        | time of event                               |
| trade\_owner     | string        | api key of trade owner                      |
| type             | string        | "TRADE"                                     |

Where a `MakerOrder` object is of the form:

| Name            | Type   | Description                            |
| --------------- | ------ | -------------------------------------- |
| asset\_id       | string | asset of the maker order               |
| matched\_amount | string | amount of maker order matched in trade |
| order\_id       | string | maker order ID                         |
| outcome         | string | outcome                                |
| owner           | string | owner of maker order                   |
| price           | string | price of maker order                   |

```json Response theme={null}
{
  "asset_id": "52114319501245915516055106046884209969926127482827954674443846427813813222426",
  "event_type": "trade",
  "id": "28c4d2eb-bbea-40e7-a9f0-b2fdb56b2c2e",
  "last_update": "1672290701",
  "maker_orders": [
    {
      "asset_id": "52114319501245915516055106046884209969926127482827954674443846427813813222426",
      "matched_amount": "10",
      "order_id": "0xff354cd7ca7539dfa9c28d90943ab5779a4eac34b9b37a757d7b32bdfb11790b",
      "outcome": "YES",
      "owner": "9180014b-33c8-9240-a14b-bdca11c0a465",
      "price": "0.57"
    }
  ],
  "market": "0xbd31dc8a20211944f6b70f31557f1001557b59905b7738480ca09bd4532f84af",
  "matchtime": "1672290701",
  "outcome": "YES",
  "owner": "9180014b-33c8-9240-a14b-bdca11c0a465",
  "price": "0.57",
  "side": "BUY",
  "size": "10",
  "status": "MATCHED",
  "taker_order_id": "0x06bc63e346ed4ceddce9efd6b3af37c8f8f440c92fe7da6b2d0f9e4ccbc50c42",
  "timestamp": "1672290701",
  "trade_owner": "9180014b-33c8-9240-a14b-bdca11c0a465",
  "type": "TRADE"
}
```

## Order Message

Emitted when:

* When an order is placed (PLACEMENT)
* When an order is updated (some of it is matched) (UPDATE)
* When an order is canceled (CANCELLATION)

### Structure

| Name              | Type      | Description                                                         |
| ----------------- | --------- | ------------------------------------------------------------------- |
| asset\_id         | string    | asset ID (token ID) of order                                        |
| associate\_trades | string\[] | array of ids referencing trades that the order has been included in |
| event\_type       | string    | "order"                                                             |
| id                | string    | order id                                                            |
| market            | string    | condition ID of market                                              |
| order\_owner      | string    | owner of order                                                      |
| original\_size    | string    | original order size                                                 |
| outcome           | string    | outcome                                                             |
| owner             | string    | owner of orders                                                     |
| price             | string    | price of order                                                      |
| side              | string    | BUY/SELL                                                            |
| size\_matched     | string    | size of order that has been matched                                 |
| timestamp         | string    | time of event                                                       |
| type              | string    | PLACEMENT/UPDATE/CANCELLATION                                       |

```json Response theme={null}
{
  "asset_id": "52114319501245915516055106046884209969926127482827954674443846427813813222426",
  "associate_trades": null,
  "event_type": "order",
  "id": "0xff354cd7ca7539dfa9c28d90943ab5779a4eac34b9b37a757d7b32bdfb11790b",
  "market": "0xbd31dc8a20211944f6b70f31557f1001557b59905b7738480ca09bd4532f84af",
  "order_owner": "9180014b-33c8-9240-a14b-bdca11c0a465",
  "original_size": "10",
  "outcome": "YES",
  "owner": "9180014b-33c8-9240-a14b-bdca11c0a465",
  "price": "0.57",
  "side": "SELL",
  "size_matched": "0",
  "timestamp": "1672290687",
  "type": "PLACEMENT"
}
```


> ## Documentation Index
> Fetch the complete documentation index at: https://docs.polymarket.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Market Channel

Public channel for updates related to market updates (level 2 price data).

**SUBSCRIBE**

`<wss-channel> market`

## book Message

Emitted When:

* First subscribed to a market
* When there is a trade that affects the book

### Structure

| Name        | Type            | Description                                                                 |
| ----------- | --------------- | --------------------------------------------------------------------------- |
| event\_type | string          | "book"                                                                      |
| asset\_id   | string          | asset ID (token ID)                                                         |
| market      | string          | condition ID of market                                                      |
| timestamp   | string          | unix timestamp the current book generation in milliseconds (1/1,000 second) |
| hash        | string          | hash summary of the orderbook content                                       |
| buys        | OrderSummary\[] | list of type (size, price) aggregate book levels for buys                   |
| sells       | OrderSummary\[] | list of type (size, price) aggregate book levels for sells                  |

Where a `OrderSummary` object is of the form:

| Name  | Type   | Description                        |
| ----- | ------ | ---------------------------------- |
| price | string | price of the orderbook level       |
| size  | string | size available at that price level |

```json Response theme={null}
{
  "event_type": "book",
  "asset_id": "65818619657568813474341868652308942079804919287380422192892211131408793125422",
  "market": "0xbd31dc8a20211944f6b70f31557f1001557b59905b7738480ca09bd4532f84af",
  "bids": [
    { "price": ".48", "size": "30" },
    { "price": ".49", "size": "20" },
    { "price": ".50", "size": "15" }
  ],
  "asks": [
    { "price": ".52", "size": "25" },
    { "price": ".53", "size": "60" },
    { "price": ".54", "size": "10" }
  ],
  "timestamp": "123456789000",
  "hash": "0x0...."
}
```

## price\_change Message

<div style={{backgroundColor: '#fff3cd', border: '1px solid #ffeaa7', borderRadius: '4px', padding: '12px', marginBottom: '16px'}}>
  <strong>⚠️ Breaking Change Notice:</strong> The price\_change message schema will be updated on September 15, 2025 at 11 PM UTC. Please see the [migration guide](/developers/CLOB/websocket/market-channel-migration-guide) for details.
</div>

Emitted When:

* A new order is placed
* An order is cancelled

### Structure

| Name           | Type           | Description                    |
| -------------- | -------------- | ------------------------------ |
| event\_type    | string         | "price\_change"                |
| market         | string         | condition ID of market         |
| price\_changes | PriceChange\[] | array of price change objects  |
| timestamp      | string         | unix timestamp in milliseconds |

Where a `PriceChange` object is of the form:

| Name      | Type   | Description                        |
| --------- | ------ | ---------------------------------- |
| asset\_id | string | asset ID (token ID)                |
| price     | string | price level affected               |
| size      | string | new aggregate size for price level |
| side      | string | "BUY" or "SELL"                    |
| hash      | string | hash of the order                  |
| best\_bid | string | current best bid price             |
| best\_ask | string | current best ask price             |

```json Response theme={null}
{
    "market": "0x5f65177b394277fd294cd75650044e32ba009a95022d88a0c1d565897d72f8f1",
    "price_changes": [
        {
            "asset_id": "71321045679252212594626385532706912750332728571942532289631379312455583992563",
            "price": "0.5",
            "size": "200",
            "side": "BUY",
            "hash": "56621a121a47ed9333273e21c83b660cff37ae50",
            "best_bid": "0.5",
            "best_ask": "1"
        },
        {
            "asset_id": "52114319501245915516055106046884209969926127482827954674443846427813813222426",
            "price": "0.5",
            "size": "200",
            "side": "SELL",
            "hash": "1895759e4df7a796bf4f1c5a5950b748306923e2",
            "best_bid": "0",
            "best_ask": "0.5"
        }
    ],
    "timestamp": "1757908892351",
    "event_type": "price_change"
}
```

## tick\_size\_change Message

Emitted When:

* The minimum tick size of the market changes. This happens when the book's price reaches the limits: price > 0.96 or price \< 0.04

### Structure

| Name            | Type   | Description                |
| --------------- | ------ | -------------------------- |
| event\_type     | string | "price\_change"            |
| asset\_id       | string | asset ID (token ID)        |
| market          | string | condition ID of market     |
| old\_tick\_size | string | previous minimum tick size |
| new\_tick\_size | string | current minimum tick size  |
| side            | string | buy/sell                   |
| timestamp       | string | time of event              |

```json Response theme={null}
{
"event_type": "tick_size_change",
"asset_id": "65818619657568813474341868652308942079804919287380422192892211131408793125422",\
"market": "0xbd31dc8a20211944f6b70f31557f1001557b59905b7738480ca09bd4532f84af",
"old_tick_size": "0.01",
"new_tick_size": "0.001",
"timestamp": "100000000"
}
```

## last\_trade\_price Message

Emitted When:

* When a maker and taker order is matched creating a trade event.

```json Response theme={null}
{
"asset_id":"114122071509644379678018727908709560226618148003371446110114509806601493071694",
"event_type":"last_trade_price",
"fee_rate_bps":"0",
"market":"0x6a67b9d828d53862160e470329ffea5246f338ecfffdf2cab45211ec578b0347",
"price":"0.456",
"side":"BUY",
"size":"219.217767",
"timestamp":"1750428146322"
}
```

## best\_bid\_ask Message

Emitted When:

* The best bid and ask prices for a market change.

(This message is behind the `custom_feature_enabled` flag)

### Structure

| Name        | Type   | Description                     |
| ----------- | ------ | ------------------------------- |
| event\_type | string | "best\_bid\_ask"                |
| market      | string | condition ID of market          |
| asset\_id   | string | asset ID (token ID)             |
| best\_bid   | string | current best bid price          |
| best\_ask   | string | current best ask price          |
| spread      | string | spread between best bid and ask |
| timestamp   | string | unix timestamp in milliseconds  |

### Example

```json Response theme={null}
{
  "event_type": "best_bid_ask",
  "market": "0x0005c0d312de0be897668695bae9f32b624b4a1ae8b140c49f08447fcc74f442",
  "asset_id": "85354956062430465315924116860125388538595433819574542752031640332592237464430",
  "best_bid": "0.73",
  "best_ask": "0.77",
  "spread": "0.04",
  "timestamp": "1766789469958"
}
```

## new\_market Message

Emitted When:

* A new market is created.

(This message is behind the `custom_feature_enabled` flag)

### Structure

| Name           | Type      | Description                    |
| -------------- | --------- | ------------------------------ |
| id             | string    | market ID                      |
| question       | string    | market question                |
| market         | string    | condition ID of market         |
| slug           | string    | market slug                    |
| description    | string    | market description             |
| assets\_ids    | string\[] | list of asset IDs              |
| outcomes       | string\[] | list of outcomes               |
| event\_message | object    | event message object           |
| timestamp      | string    | unix timestamp in milliseconds |
| event\_type    | string    | "new\_market"                  |

Where a `EventMessage` object is of the form:

| Name        | Type   | Description               |
| ----------- | ------ | ------------------------- |
| id          | string | event message ID          |
| ticker      | string | event message ticker      |
| slug        | string | event message slug        |
| title       | string | event message title       |
| description | string | event message description |

### Example

```json Response theme={null}
{
    "id": "1031769",
    "question": "Will NVIDIA (NVDA) close above $240 end of January?",
    "market": "0x311d0c4b6671ab54af4970c06fcf58662516f5168997bdda209ec3db5aa6b0c1",
    "slug": "nvda-above-240-on-january-30-2026",
    "description": "This market will resolve to \"Yes\" if the official closing price for NVIDIA (NVDA) on the final trading day of January 2026 is higher than the listed price. Otherwise, this market will resolve to \"No\".\n\nIf the final trading day of the month is shortened (for example, due to a market-holiday schedule), the official closing price published for that shortened session will still be used for resolution.\n\nIf no official closing price is published for that session (for example, due to a trading halt into the close, system issue, or other disruption), the market will use the last valid on-exchange trade price of the regular session as the effective closing price.\n\nThe resolution source for this market is Yahoo Finance — specifically, the NVIDIA (NVDA) \"Close\" prices available at https://finance.yahoo.com/quote/NVDA/history, published under \"Historical Prices.\"\n\nIn the event of a stock split, reverse stock split, or similar corporate action affecting the listed company during the listed time frame, this market will resolve based on split-adjusted prices as displayed on Yahoo Finance.",
    "assets_ids": [
        "76043073756653678226373981964075571318267289248134717369284518995922789326425",
        "31690934263385727664202099278545688007799199447969475608906331829650099442770"
    ],
    "outcomes": [
        "Yes",
        "No"
    ],
    "event_message": {
        "id": "125819",
        "ticker": "nvda-above-in-january-2026",
        "slug": "nvda-above-in-january-2026",
        "title": "Will NVIDIA (NVDA) close above ___ end of January?",
        "description": "This market will resolve to \"Yes\" if the official closing price for NVIDIA (NVDA) on the final trading day of January 2026 is higher than the listed price. Otherwise, this market will resolve to \"No\".\n\nIf the final trading day of the month is shortened (for example, due to a market-holiday schedule), the official closing price published for that shortened session will still be used for resolution.\n\nIf no official closing price is published for that session (for example, due to a trading halt into the close, system issue, or other disruption), the market will use the last valid on-exchange trade price of the regular session as the effective closing price.\n\nThe resolution source for this market is Yahoo Finance — specifically, the NVIDIA (NVDA) \"Close\" prices available at https://finance.yahoo.com/quote/NVDA/history, published under \"Historical Prices.\"\n\nIn the event of a stock split, reverse stock split, or similar corporate action affecting the listed company during the listed time frame, this market will resolve based on split-adjusted prices as displayed on Yahoo Finance."
    },
    "timestamp": "1766790415550",
    "event_type": "new_market"
}
```

## market\_resolved Message

Emitted When:

* A market is resolved.

(This message is behind the `custom_feature_enabled` flag)

### Structure

| Name               | Type      | Description                    |
| ------------------ | --------- | ------------------------------ |
| id                 | string    | market ID                      |
| question           | string    | market question                |
| market             | string    | condition ID of market         |
| slug               | string    | market slug                    |
| description        | string    | market description             |
| assets\_ids        | string\[] | list of asset IDs              |
| outcomes           | string\[] | list of outcomes               |
| winning\_asset\_id | string    | winning asset ID               |
| winning\_outcome   | string    | winning outcome                |
| event\_message     | object    | event message object           |
| timestamp          | string    | unix timestamp in milliseconds |
| event\_type        | string    | "market\_resolved"             |

Where a `EventMessage` object is of the form:

| Name        | Type   | Description               |
| ----------- | ------ | ------------------------- |
| id          | string | event message ID          |
| ticker      | string | event message ticker      |
| slug        | string | event message slug        |
| title       | string | event message title       |
| description | string | event message description |

### Example

```json Response theme={null}
{
    "id": "1031769",
    "question": "Will NVIDIA (NVDA) close above $240 end of January?",
    "market": "0x311d0c4b6671ab54af4970c06fcf58662516f5168997bdda209ec3db5aa6b0c1",
    "slug": "nvda-above-240-on-january-30-2026",
    "description": "This market will resolve to \"Yes\" if the official closing price for NVIDIA (NVDA) on the final trading day of January 2026 is higher than the listed price. Otherwise, this market will resolve to \"No\".\n\nIf the final trading day of the month is shortened (for example, due to a market-holiday schedule), the official closing price published for that shortened session will still be used for resolution.\n\nIf no official closing price is published for that session (for example, due to a trading halt into the close, system issue, or other disruption), the market will use the last valid on-exchange trade price of the regular session as the effective closing price.\n\nThe resolution source for this market is Yahoo Finance — specifically, the NVIDIA (NVDA) \"Close\" prices available at https://finance.yahoo.com/quote/NVDA/history, published under \"Historical Prices.\"\n\nIn the event of a stock split, reverse stock split, or similar corporate action affecting the listed company during the listed time frame, this market will resolve based on split-adjusted prices as displayed on Yahoo Finance.",
    "assets_ids": [
        "76043073756653678226373981964075571318267289248134717369284518995922789326425",
        "31690934263385727664202099278545688007799199447969475608906331829650099442770"
    ],
    "winning_asset_id": "76043073756653678226373981964075571318267289248134717369284518995922789326425",
    "winning_outcome": "Yes",
    "event_message": {
        "id": "125819",
        "ticker": "nvda-above-in-january-2026",
        "slug": "nvda-above-in-january-2026",
        "title": "Will NVIDIA (NVDA) close above ___ end of January?",
        "description": "This market will resolve to \"Yes\" if the official closing price for NVIDIA (NVDA) on the final trading day of January 2026 is higher than the listed price. Otherwise, this market will resolve to \"No\".\n\nIf the final trading day of the month is shortened (for example, due to a market-holiday schedule), the official closing price published for that shortened session will still be used for resolution.\n\nIf no official closing price is published for that session (for example, due to a trading halt into the close, system issue, or other disruption), the market will use the last valid on-exchange trade price of the regular session as the effective closing price.\n\nThe resolution source for this market is Yahoo Finance — specifically, the NVIDIA (NVDA) \"Close\" prices available at https://finance.yahoo.com/quote/NVDA/history, published under \"Historical Prices.\"\n\nIn the event of a stock split, reverse stock split, or similar corporate action affecting the listed company during the listed time frame, this market will resolve based on split-adjusted prices as displayed on Yahoo Finance."
    },
    "timestamp": "1766790415550",
    "event_type": "new_market"
}
```


Skip to main content
Polymarket Documentation home pagedark logo

Search...
Ctrl K

Ask AI
Main Site

User Guide
For Developers
Changelog
Polymarket
Discord Community
Twitter
Developer Quickstart
Developer Quickstart
Fetching Market Data
Placing Your First Order
Glossary
API Rate Limits
Endpoints
Market Makers
Market Maker Introduction
Setup
Trading
Liquidity Rewards
Maker Rebates Program
Data Feeds
Inventory Management
Polymarket Builders Program
Builder Program Introduction
Builder Tiers
Builder Profile & Keys
Order Attribution
Relayer Client
Examples
Central Limit Order Book
CLOB Introduction
Status
Quickstart
Authentication
Geographic Restrictions

Client
Methods Overview
Public Methods
L1 Methods
L2 Methods
Builder Methods

REST API

Orderbook
GET
Get order book summary
POST
Get multiple order books summaries by request

Pricing
GET
Get market price
GET
Get multiple market prices
POST
Get multiple market prices by request
GET
Get midpoint price
GET
Get price history for a traded token

Spreads
POST
Get bid-ask spreads

Historical Timeseries Data
GET
Historical Timeseries Data

Order Management
Orders Overview
Place Single Order
Place Multiple Orders (Batching)
Get Order
Get Active Orders
Check Order Reward Scoring
Cancel Orders(s)
Onchain Order Info

Trades
Trades Overview
Get Trades
Websocket
WSS Overview
WSS Quickstart
WSS Authentication
User Channel
Market Channel

Sports Websocket
Overview
Message Format
Quickstart
Real Time Data Stream
RTDS Overview
RTDS Crypto Prices
RTDS Comments
Gamma Structure
Overview
Gamma Structure
Fetching Markets
Gamma Endpoints

Gamma Status

Sports

Tags

Events

Markets

Series

Comments

Profiles

Search
Data-API

Data API Status

Core

Misc

Builders
Bridge & Swap
Overview

Bridge
Subgraph
Overview
Resolution
Resolution
Conditional Token Frameworks
Overview
Splitting USDC
Merging Tokens
Reedeeming Tokens
Deployment and Additional Information
Proxy Wallets
Proxy wallet
Negative Risk
Overview

On this page
How It Works
Connection Management
Automatic Ping/Pong Heartbeat
Connection Health
Session Affinity
Next Steps
Sports Websocket
Overview
Real-time sports results via WebSocket

The Polymarket Sports WebSocket API provides real-time sports results updates. Clients connect to receive live match data including scores, periods, and game status as events happen.
Endpoint:
wss://sports-api.polymarket.com/ws
No authentication is required. This is a public broadcast channel that streams updates for all active sports events.
​
How It Works
Once connected, clients automatically receive JSON messages whenever a sports event updates. There is no subscription message required—simply connect and start receiving data.
​
Connection Management
​
Automatic Ping/Pong Heartbeat
The server sends PING messages at regular intervals. Clients must respond with PONG to maintain the connection.
Parameter	Default	Description
PING Interval	5 seconds	How often the server sends PING messages
PONG Timeout	10 seconds	How long the server waits for a PONG response
If your client doesn’t respond to PING within 10 seconds, the connection will be closed automatically.
​
Connection Health
Server sends PING → Client must respond with PONG
No response within timeout → Connection terminated
Clients should implement automatic reconnection with exponential backoff
​
Session Affinity
The server uses cookie-based session affinity (sports-results cookie) to ensure clients maintain connection to the same backend instance. This is handled automatically by the browser.
​
Next Steps
Message Format
Understand the structure of sports update messages
Quickstart
Implementation examples in JavaScript and TypeScript
Market Channel
Message Format
Ask a question...

github
Powered by
Overview - Polymarket Documentation

Skip to main content
Polymarket Documentation home pagedark logo

Search...
Ctrl K

Ask AI
Main Site

User Guide
For Developers
Changelog
Polymarket
Discord Community
Twitter
Developer Quickstart
Developer Quickstart
Fetching Market Data
Placing Your First Order
Glossary
API Rate Limits
Endpoints
Market Makers
Market Maker Introduction
Setup
Trading
Liquidity Rewards
Maker Rebates Program
Data Feeds
Inventory Management
Polymarket Builders Program
Builder Program Introduction
Builder Tiers
Builder Profile & Keys
Order Attribution
Relayer Client
Examples
Central Limit Order Book
CLOB Introduction
Status
Quickstart
Authentication
Geographic Restrictions

Client
Methods Overview
Public Methods
L1 Methods
L2 Methods
Builder Methods

REST API

Orderbook
GET
Get order book summary
POST
Get multiple order books summaries by request

Pricing
GET
Get market price
GET
Get multiple market prices
POST
Get multiple market prices by request
GET
Get midpoint price
GET
Get price history for a traded token

Spreads
POST
Get bid-ask spreads

Historical Timeseries Data
GET
Historical Timeseries Data

Order Management
Orders Overview
Place Single Order
Place Multiple Orders (Batching)
Get Order
Get Active Orders
Check Order Reward Scoring
Cancel Orders(s)
Onchain Order Info

Trades
Trades Overview
Get Trades
Websocket
WSS Overview
WSS Quickstart
WSS Authentication
User Channel
Market Channel

Sports Websocket
Overview
Message Format
Quickstart
Real Time Data Stream
RTDS Overview
RTDS Crypto Prices
RTDS Comments
Gamma Structure
Overview
Gamma Structure
Fetching Markets
Gamma Endpoints

Gamma Status

Sports

Tags

Events

Markets

Series

Comments

Profiles

Search
Data-API

Data API Status

Core

Misc

Builders
Bridge & Swap
Overview

Bridge
Subgraph
Overview
Resolution
Resolution
Conditional Token Frameworks
Overview
Splitting USDC
Merging Tokens
Reedeeming Tokens
Deployment and Additional Information
Proxy Wallets
Proxy wallet
Negative Risk
Overview

On this page
sport_result Message
Structure
Example Messages
Slug Format
Period Values
Handling Updates
Sports Websocket
Message Format
Structure of sports result update messages

Once connected to the Sports WebSocket, clients receive JSON messages whenever a sports event updates. Messages are broadcast to all connected clients automatically.
​
sport_result Message
Emitted when:
A match goes live
The score changes
The period changes (e.g., halftime, overtime)
A match ends
Possession changes (NFL and CFB only)
​
Structure
​
gameId
number
Unique identifier for the game
​
leagueAbbreviation
string
League identifier (e.g., "nfl", "nba", "cs2")
​
homeTeam
string
Home team name or abbreviation
​
awayTeam
string
Away team name or abbreviation
​
status
string
Game status (e.g., "InProgress", "finished")
​
live
boolean
true if the match is currently in progress
​
ended
boolean
true if the match has concluded
​
score
string
Current score (format varies by sport)
​
period
string
Current period (e.g., "Q4", "2H", "2/3")
​
elapsed
string
Time elapsed in current period (e.g., "05:09")
​
finishedTimestamp
string
Timestamp when the match ended (only present when ended: true)
​
turn
string
Team abbreviation with possession (NFL/CFB only)
The turn field is only present for NFL and CFB games and indicates which team currently has the ball.
​
Example Messages
NFL (in progress):
{
  "gameId": 19439,
  "leagueAbbreviation": "nfl",
  "homeTeam": "LAC",
  "awayTeam": "BUF",
  "status": "InProgress",
  "score": "3-16",
  "period": "Q4",
  "elapsed": "5:18",
  "live": true,
  "ended": false,
  "turn": "lac"
}
Esports - CS2 (finished):
{
  "gameId": 1317359,
  "leagueAbbreviation": "cs2",
  "homeTeam": "ARCRED",
  "awayTeam": "The glecs",
  "status": "finished",
  "score": "000-000|2-0|Bo3",
  "period": "2/3",
  "live": false,
  "ended": true
}
​
Slug Format
The slug field follows a consistent naming convention:
{league}-{team1}-{team2}-{date}
Examples:
nfl-buf-kc-2025-01-26 — NFL: Buffalo Bills vs Kansas City Chiefs
nba-lal-bos-2025-02-15 — NBA: LA Lakers vs Boston Celtics
mlb-nyy-bos-2025-04-01 — MLB: NY Yankees vs Boston Red Sox
​
Period Values
Period	Description
1H	First half
2H	Second half
1Q, 2Q, 3Q, 4Q	Quarters (NFL, NBA)
HT	Halftime
FT	Full time (match ended in regulation)
FT OT	Full time with overtime
FT NR	Full time, no result (draw or canceled)
End 1, End 2, etc.	End of inning (MLB)
1/3, 2/3, 3/3	Map number in Bo3 series (Esports)
1/5, 2/5, etc.	Map number in Bo5 series (Esports)
​
Handling Updates
When processing messages, use the gameId field as the unique identifier to update your local state:
// Update or insert based on gameId
setSportsData(prev => {
  const existing = prev.find(item => item.gameId === data.gameId);
  if (existing) {
    return prev.map(item => 
      item.gameId === data.gameId ? data : item
    );
  }
  return [...prev, data];
});
Overview
Quickstart
Ask a question...

github
Powered by
Message Format - Polymarket Documentation

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.polymarket.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Quickstart

> Connect to the Sports WebSocket and receive live updates

Connect to the Sports WebSocket to receive real-time sports results. No authentication required—just connect and handle incoming messages.

## Endpoint

```
wss://sports-api.polymarket.com/ws
```

***

## JavaScript Example

<CodeGroup>
  ```javascript JavaScript theme={null}
  const ws = new WebSocket('wss://sports-api.polymarket.com/ws');

  ws.onopen = () => {
    console.log('Connected to Sports WebSocket');
  };

  ws.onmessage = (event) => {
    // Respond to server PING
    if (event.data === 'ping') {
      ws.send('pong');
      return;
    }

    // Parse and handle sports updates
    const data = JSON.parse(event.data);
    console.log('Update:', data.slug, data.score, data.period);
  };

  ws.onclose = () => {
    console.log('Disconnected');
    // Reconnect after 1 second
    setTimeout(() => location.reload(), 1000);
  };

  ws.onerror = (error) => {
    console.error('WebSocket error:', error);
  };
  ```

  ```typescript React Hook theme={null}
  import { useEffect, useRef, useState } from 'react';

  interface SportsUpdate {
    slug: string;
    live: boolean;
    ended: boolean;
    score: string;
    period: string;
    elapsed: string;
    last_update: string;
    finished_timestamp?: string;
    turn?: string;
  }

  export function useSportsWebSocket() {
    const [updates, setUpdates] = useState<Map<string, SportsUpdate>>(new Map());
    const wsRef = useRef<WebSocket | null>(null);

    useEffect(() => {
      const ws = new WebSocket('wss://sports-api.polymarket.com/ws');
      wsRef.current = ws;

      ws.onmessage = (event) => {
        if (event.data === 'ping') {
          ws.send('pong');
          return;
        }
        const data: SportsUpdate = JSON.parse(event.data);
        setUpdates(prev => new Map(prev).set(data.slug, data));
      };

      ws.onclose = () => setTimeout(() => location.reload(), 1000);

      return () => ws.close();
    }, []);

    return Array.from(updates.values());
  }
  ```
</CodeGroup>

***

## Critical: PING/PONG Handling

The server sends PING messages every 5 seconds. Your client **must** respond with PONG to stay connected.

```javascript  theme={null}
// CORRECT - Handle PING messages
ws.onmessage = (event) => {
  if (event.data === 'ping') {
    ws.send('pong');  // Respond immediately
    return;
  }
  // Handle other messages...
  const data = JSON.parse(event.data);
  handleUpdate(data);
};
```

```javascript  theme={null}
// WRONG - Ignoring PING messages will disconnect you
ws.onmessage = (event) => {
  const data = JSON.parse(event.data);  // Fails on "ping" string!
  handleUpdate(data);
};
```

<Warning>
  If you don't respond to PING within 10 seconds, your connection will be terminated.
</Warning>

***

## Connection State Management

Always check connection state before sending:

```javascript  theme={null}
if (ws.readyState === WebSocket.OPEN) {
  ws.send('pong');
} else {
  console.warn('WebSocket not connected');
}
```

***

## Browser Tab Visibility

Connections may drop when browser tabs become inactive. Handle visibility changes:

```javascript  theme={null}
document.addEventListener('visibilitychange', () => {
  if (!document.hidden && ws.readyState !== WebSocket.OPEN) {
    console.log('Tab became visible, reconnecting...');
    connect();
  }
});
```

***

## Troubleshooting

<AccordionGroup>
  <Accordion title="Connection drops after exactly 10 seconds">
    Your PING/PONG handler isn't working correctly.

    **Check:**

    * You're responding to `"ping"` string messages (not JSON)
    * You're sending `"pong"` as a string response
    * No errors are preventing the PONG from being sent

    ```javascript  theme={null}
    // Debug PING/PONG handling
    ws.onmessage = (event) => {
      console.log('Received:', event.data);
      if (event.data === 'ping') {
        console.log('Sending PONG response');
        ws.send('pong');
        return;
      }
      // Handle JSON messages...
    };
    ```
  </Accordion>

  <Accordion title="Connection keeps dropping frequently">
    This may be network instability or main thread blocking.

    **Solutions:**

    * Implement exponential backoff for reconnection
    * Ensure your message handler doesn't block the main thread
    * Check network stability

    ```javascript  theme={null}
    handleReconnect() {
      this.reconnectDelay = Math.min(this.reconnectDelay * 2, 30000);
      setTimeout(() => this.connect(), this.reconnectDelay);
    }
    ```
  </Accordion>

  <Accordion title="Messages not updating UI">
    Ensure you're updating state correctly based on the `slug` identifier.

    ```javascript  theme={null}
    // Use slug as unique key
    setSportsData(prev => {
      const index = prev.findIndex(item => item.slug === data.slug);
      if (index >= 0) {
        const updated = [...prev];
        updated[index] = data;
        return updated;
      }
      return [...prev, data];
    });
    ```
  </Accordion>

  <Accordion title="Memory leaks with multiple connections">
    Clean up properly when disconnecting:

    ```javascript  theme={null}
    const cleanup = () => {
      if (reconnectTimeout) {
        clearTimeout(reconnectTimeout);
      }
      if (ws) {
        ws.close();
        ws = null;
      }
    };

    // React: cleanup in useEffect return
    // Vanilla: call on page unload
    window.addEventListener('beforeunload', cleanup);
    ```
  </Accordion>
</AccordionGroup>

***

## Debugging Tips

Enable verbose logging to diagnose connection issues:

```javascript  theme={null}
ws.onopen = () => console.log('[connected]');
ws.onclose = (e) => console.log('[closed]', e.code, e.reason);
ws.onerror = (e) => console.error('[error]', e);
ws.onmessage = (e) => console.log('[message]', e.data);
```

Monitor connection state:

```javascript  theme={null}
setInterval(() => {
  const states = ['CONNECTING', 'OPEN', 'CLOSING', 'CLOSED'];
  console.log('WebSocket state:', states[ws.readyState]);
}, 5000);
```


> ## Documentation Index
> Fetch the complete documentation index at: https://docs.polymarket.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Real Time Data Socket

## Overview

The Polymarket Real-Time Data Socket (RTDS) is a WebSocket-based streaming service that provides real-time updates for **comments** and **crypto prices**.

<Card title="TypeScript client" icon="github" href="https://github.com/Polymarket/real-time-data-client">
  Official RTDS TypeScript client (`real-time-data-client`).
</Card>

### Connection Details

* **WebSocket URL**: `wss://ws-live-data.polymarket.com`
* **Protocol**: WebSocket
* **Data Format**: JSON

### Authentication

Some user-specific streams may require `gamma_auth`:

* `address`: User wallet address

### Connection Management

The WebSocket connection supports:

* **Dynamic Subscriptions**: Without disconnecting from the socket users can add, remove and modify topics and filters they are subscribed to.
* **Ping/Pong**: You should send PING messages (every 5 seconds ideally) to maintain connection

## Available Subscription Types

<Note>Only the subscription types documented below are supported.</Note>

The RTDS currently supports the following subscription types:

1. **[Crypto Prices](/developers/RTDS/RTDS-crypto-prices)** - Real-time cryptocurrency price updates
2. **[Comments](/developers/RTDS/RTDS-comments)** - Comment-related events including reactions

## Message Structure

All messages received from the WebSocket follow this structure:

```json  theme={null}
{
  "topic": "string",
  "type": "string", 
  "timestamp": "number",
  "payload": "object"
}
```

* `topic`: The subscription topic (e.g., "crypto\_prices", "comments")
* `type`: The message type/event (e.g., "update", "reaction\_created")
* `timestamp`: Unix timestamp in milliseconds
* `payload`: Event-specific data object

## Subscription Management

### Subscribe to Topics

To subscribe to data streams, send a JSON message with this structure:

```json  theme={null}
{
  "action": "subscribe",
  "subscriptions": [
    {
      "topic": "topic_name",
      "type": "message_type",
      "filters": "optional_filter_string",
      "gamma_auth": {
        "address": "wallet_address"
      }
    }
  ]
}
```

### Unsubscribe from Topics

To unsubscribe from data streams, send a similar message with `"action": "unsubscribe"`.

## Error Handling

* Connection errors will trigger automatic reconnection attempts
* Invalid subscription messages may result in connection closure
* Authentication failures will prevent successful subscription to protected topics


Skip to main content
Polymarket Documentation home pagedark logo

Search...
Ctrl K

Ask AI
Main Site

User Guide
For Developers
Changelog
Polymarket
Discord Community
Twitter
Developer Quickstart
Developer Quickstart
Fetching Market Data
Placing Your First Order
Glossary
API Rate Limits
Endpoints
Market Makers
Market Maker Introduction
Setup
Trading
Liquidity Rewards
Maker Rebates Program
Data Feeds
Inventory Management
Polymarket Builders Program
Builder Program Introduction
Builder Tiers
Builder Profile & Keys
Order Attribution
Relayer Client
Examples
Central Limit Order Book
CLOB Introduction
Status
Quickstart
Authentication
Geographic Restrictions

Client
Methods Overview
Public Methods
L1 Methods
L2 Methods
Builder Methods

REST API

Orderbook
GET
Get order book summary
POST
Get multiple order books summaries by request

Pricing
GET
Get market price
GET
Get multiple market prices
POST
Get multiple market prices by request
GET
Get midpoint price
GET
Get price history for a traded token

Spreads
POST
Get bid-ask spreads

Historical Timeseries Data
GET
Historical Timeseries Data

Order Management
Orders Overview
Place Single Order
Place Multiple Orders (Batching)
Get Order
Get Active Orders
Check Order Reward Scoring
Cancel Orders(s)
Onchain Order Info

Trades
Trades Overview
Get Trades
Websocket
WSS Overview
WSS Quickstart
WSS Authentication
User Channel
Market Channel

Sports Websocket
Overview
Message Format
Quickstart
Real Time Data Stream
RTDS Overview
RTDS Crypto Prices
RTDS Comments
Gamma Structure
Overview
Gamma Structure
Fetching Markets
Gamma Endpoints

Gamma Status

Sports

Tags

Events

Markets

Series

Comments

Profiles

Search
Data-API

Data API Status

Core

Misc

Builders
Bridge & Swap
Overview

Bridge
Subgraph
Overview
Resolution
Resolution
Conditional Token Frameworks
Overview
Splitting USDC
Merging Tokens
Reedeeming Tokens
Deployment and Additional Information
Proxy Wallets
Proxy wallet
Negative Risk
Overview

On this page
Overview
Binance Source (crypto_prices)
Subscription Details
Subscription Message
With Symbol Filter
Chainlink Source (crypto_prices_chainlink)
Subscription Details
Subscription Message
With Symbol Filter
Message Format
Binance Source Message Format
Chainlink Source Message Format
Payload Fields
Example Messages
Binance Source Examples
Solana Price Update (Binance)
Bitcoin Price Update (Binance)
Chainlink Source Examples
Ethereum Price Update (Chainlink)
Bitcoin Price Update (Chainlink)
Supported Symbols
Binance Source Symbols
Chainlink Source Symbols
Notes
General
Real Time Data Stream
RTDS Crypto Prices
TypeScript client
Official RTDS TypeScript client (real-time-data-client).
​
Overview
The crypto prices subscription provides real-time updates for cryptocurrency price data from two different sources:
Binance Source (crypto_prices): Real-time price data from Binance exchange
Chainlink Source (crypto_prices_chainlink): Price data from Chainlink oracle networks
Both streams deliver current market prices for various cryptocurrency trading pairs, but use different symbol formats and subscription structures.
​
Binance Source (crypto_prices)
​
Subscription Details
Topic: crypto_prices
Type: update
Authentication: Not required
Filters: Optional (specific symbols can be filtered)
Symbol Format: Lowercase concatenated pairs (e.g., solusdt, btcusdt)
​
Subscription Message
{
  "action": "subscribe",
  "subscriptions": [
    {
      "topic": "crypto_prices",
      "type": "update"
    }
  ]
}
​
With Symbol Filter
To subscribe to specific cryptocurrency symbols, include a filters parameter:
{
  "action": "subscribe", 
  "subscriptions": [
    {
      "topic": "crypto_prices",
      "type": "update",
      "filters": "solusdt,btcusdt,ethusdt"
    }
  ]
}
​
Chainlink Source (crypto_prices_chainlink)
​
Subscription Details
Topic: crypto_prices_chainlink
Type: * (all types)
Authentication: Not required
Filters: Optional (JSON object with symbol specification)
Symbol Format: Slash-separated pairs (e.g., eth/usd, btc/usd)
​
Subscription Message
{
  "action": "subscribe",
  "subscriptions": [
    {
      "topic": "crypto_prices_chainlink",
      "type": "*",
      "filters": ""
    }
  ]
}
​
With Symbol Filter
To subscribe to specific cryptocurrency symbols, include a JSON filters parameter:
{
  "action": "subscribe",
  "subscriptions": [
    {
      "topic": "crypto_prices_chainlink",
      "type": "*",
      "filters": "{\"symbol\":\"eth/usd\"}"
    }
  ]
}
​
Message Format
​
Binance Source Message Format
When subscribed to Binance crypto prices (crypto_prices), you’ll receive messages with the following structure:
{
  "topic": "crypto_prices",
  "type": "update", 
  "timestamp": 1753314064237,
  "payload": {
    "symbol": "solusdt",
    "timestamp": 1753314064213,
    "value": 189.55
  }
}
​
Chainlink Source Message Format
When subscribed to Chainlink crypto prices (crypto_prices_chainlink), you’ll receive messages with the following structure:
{
  "topic": "crypto_prices_chainlink",
  "type": "update", 
  "timestamp": 1753314064237,
  "payload": {
    "symbol": "eth/usd",
    "timestamp": 1753314064213,
    "value": 3456.78
  }
}
​
Payload Fields
Field	Type	Description
symbol	string	Trading pair symbol
Binance: lowercase concatenated (e.g., “solusdt”, “btcusdt”)
Chainlink: slash-separated (e.g., “eth/usd”, “btc/usd”)
timestamp	number	Price timestamp in Unix milliseconds
value	number	Current price value in the quote currency
​
Example Messages
​
Binance Source Examples
​
Solana Price Update (Binance)
{
  "topic": "crypto_prices",
  "type": "update",
  "timestamp": 1753314064237,
  "payload": {
    "symbol": "solusdt", 
    "timestamp": 1753314064213,
    "value": 189.55
  }
}
​
Bitcoin Price Update (Binance)
{
  "topic": "crypto_prices",
  "type": "update", 
  "timestamp": 1753314088421,
  "payload": {
    "symbol": "btcusdt",
    "timestamp": 1753314088395,
    "value": 67234.50
  }
}
​
Chainlink Source Examples
​
Ethereum Price Update (Chainlink)
{
  "topic": "crypto_prices_chainlink",
  "type": "update",
  "timestamp": 1753314064237,
  "payload": {
    "symbol": "eth/usd", 
    "timestamp": 1753314064213,
    "value": 3456.78
  }
}
​
Bitcoin Price Update (Chainlink)
{
  "topic": "crypto_prices_chainlink",
  "type": "update", 
  "timestamp": 1753314088421,
  "payload": {
    "symbol": "btc/usd",
    "timestamp": 1753314088395,
    "value": 67234.50
  }
}
​
Supported Symbols
​
Binance Source Symbols
The Binance source supports various cryptocurrency trading pairs using lowercase concatenated format:
btcusdt - Bitcoin to USDT
ethusdt - Ethereum to USDT
solusdt - Solana to USDT
xrpusdt - XRP to USDT
​
Chainlink Source Symbols
The Chainlink source supports cryptocurrency trading pairs using slash-separated format:
btc/usd - Bitcoin to USD
eth/usd - Ethereum to USD
sol/usd - Solana to USD
xrp/usd - XRP to USD
​
Notes
​
General
Price updates are sent as market prices change
The timestamp in the payload represents when the price was recorded
The outer timestamp represents when the message was sent via WebSocket
No authentication is required for crypto price data
RTDS Overview
RTDS Comments
Ask a question...

github
Powered by
RTDS Crypto Prices - Polymarket Documentation

Skip to main content
Polymarket Documentation home pagedark logo

Search...
Ctrl K

Ask AI
Main Site

User Guide
For Developers
Changelog
Polymarket
Discord Community
Twitter
Developer Quickstart
Developer Quickstart
Fetching Market Data
Placing Your First Order
Glossary
API Rate Limits
Endpoints
Market Makers
Market Maker Introduction
Setup
Trading
Liquidity Rewards
Maker Rebates Program
Data Feeds
Inventory Management
Polymarket Builders Program
Builder Program Introduction
Builder Tiers
Builder Profile & Keys
Order Attribution
Relayer Client
Examples
Central Limit Order Book
CLOB Introduction
Status
Quickstart
Authentication
Geographic Restrictions

Client
Methods Overview
Public Methods
L1 Methods
L2 Methods
Builder Methods

REST API

Orderbook
GET
Get order book summary
POST
Get multiple order books summaries by request

Pricing
GET
Get market price
GET
Get multiple market prices
POST
Get multiple market prices by request
GET
Get midpoint price
GET
Get price history for a traded token

Spreads
POST
Get bid-ask spreads

Historical Timeseries Data
GET
Historical Timeseries Data

Order Management
Orders Overview
Place Single Order
Place Multiple Orders (Batching)
Get Order
Get Active Orders
Check Order Reward Scoring
Cancel Orders(s)
Onchain Order Info

Trades
Trades Overview
Get Trades
Websocket
WSS Overview
WSS Quickstart
WSS Authentication
User Channel
Market Channel

Sports Websocket
Overview
Message Format
Quickstart
Real Time Data Stream
RTDS Overview
RTDS Crypto Prices
RTDS Comments
Gamma Structure
Overview
Gamma Structure
Fetching Markets
Gamma Endpoints

Gamma Status

Sports

Tags

Events

Markets

Series

Comments

Profiles

Search
Data-API

Data API Status

Core

Misc

Builders
Bridge & Swap
Overview

Bridge
Subgraph
Overview
Resolution
Resolution
Conditional Token Frameworks
Overview
Splitting USDC
Merging Tokens
Reedeeming Tokens
Deployment and Additional Information
Proxy Wallets
Proxy wallet
Negative Risk
Overview

On this page
Overview
Subscription Details
Subscription Message
Message Format
Message Types
comment_created
comment_removed
reaction_created
reaction_removed
Payload Fields
Profile Object Fields
Parent Entity Types
Example Messages
New Comment Created
Reply to Existing Comment
Comment Hierarchy
Use Cases
Content
Notes
Real Time Data Stream
RTDS Comments
TypeScript client
Official RTDS TypeScript client (real-time-data-client).
​
Overview
The comments subscription provides real-time updates for comment-related events on the Polymarket platform. This includes new comments being created, as well as other comment interactions like reactions and replies.
​
Subscription Details
Topic: comments
Type: comment_created (and potentially other comment event types like reaction_created)
Authentication: May require Gamma authentication for user-specific data
Filters: Optional (can filter by specific comment IDs, users, or events)
​
Subscription Message
{
  "action": "subscribe",
  "subscriptions": [
    {
      "topic": "comments", 
      "type": "comment_created"
    }
  ]
}
​
Message Format
When subscribed to comments, you’ll receive messages with the following structure:
{
  "topic": "comments",
  "type": "comment_created",
  "timestamp": 1753454975808,
  "payload": {
    "body": "do you know what the term encircle means? it means to surround from all sides, Russia has present on only 1 side, that's the opposite of an encirclement",
    "createdAt": "2025-07-25T14:49:35.801298Z",
    "id": "1763355",
    "parentCommentID": "1763325",
    "parentEntityID": 18396,
    "parentEntityType": "Event",
    "profile": {
      "baseAddress": "0xce533188d53a16ed580fd5121dedf166d3482677",
      "displayUsernamePublic": true,
      "name": "salted.caramel",
      "proxyWallet": "0x4ca749dcfa93c87e5ee23e2d21ff4422c7a4c1ee",
      "pseudonym": "Adored-Disparity"
    },
    "reactionCount": 0,
    "replyAddress": "0x0bda5d16f76cd1d3485bcc7a44bc6fa7db004cdd",
    "reportCount": 0,
    "userAddress": "0xce533188d53a16ed580fd5121dedf166d3482677"
  }
}
​
Message Types
​
comment_created
Triggered when a user creates a new comment on an event or in reply to another comment.
​
comment_removed
Triggered when a comment is removed or deleted.
​
reaction_created
Triggered when a user adds a reaction to an existing comment.
​
reaction_removed
Triggered when a reaction is removed from a comment.
​
Payload Fields
Field	Type	Description
body	string	The text content of the comment
createdAt	string	ISO 8601 timestamp when the comment was created
id	string	Unique identifier for this comment
parentCommentID	string	ID of the parent comment if this is a reply (null for top-level comments)
parentEntityID	number	ID of the parent entity (event, market, etc.)
parentEntityType	string	Type of parent entity (e.g., “Event”, “Market”)
profile	object	Profile information of the user who created the comment
reactionCount	number	Current number of reactions on this comment
replyAddress	string	Polygon address for replies (may be different from userAddress)
reportCount	number	Current number of reports on this comment
userAddress	string	Polygon address of the user who created the comment
​
Profile Object Fields
Field	Type	Description
baseAddress	string	User profile address
displayUsernamePublic	boolean	Whether the username should be displayed publicly
name	string	User’s display name
proxyWallet	string	Proxy wallet address used for transactions
pseudonym	string	Generated pseudonym for the user
​
Parent Entity Types
The following parent entity types are supported:
Event - Comments on prediction events
Market - Comments on specific markets
Additional entity types may be available
​
Example Messages
​
New Comment Created
{
  "topic": "comments",
  "type": "comment_created",
  "timestamp": 1753454975808,
  "payload": {
    "body": "do you know what the term encircle means? it means to surround from all sides, Russia has present on only 1 side, that's the opposite of an encirclement",
    "createdAt": "2025-07-25T14:49:35.801298Z",
    "id": "1763355",
    "parentCommentID": "1763325",
    "parentEntityID": 18396,
    "parentEntityType": "Event",
    "profile": {
      "baseAddress": "0xce533188d53a16ed580fd5121dedf166d3482677",
      "displayUsernamePublic": true,
      "name": "salted.caramel",
      "proxyWallet": "0x4ca749dcfa93c87e5ee23e2d21ff4422c7a4c1ee",
      "pseudonym": "Adored-Disparity"
    },
    "reactionCount": 0,
    "replyAddress": "0x0bda5d16f76cd1d3485bcc7a44bc6fa7db004cdd",
    "reportCount": 0,
    "userAddress": "0xce533188d53a16ed580fd5121dedf166d3482677"
  }
}
​
Reply to Existing Comment
{
  "topic": "comments",
  "type": "comment_created",
  "timestamp": 1753454985123,
  "payload": {
    "body": "That's a good point about the definition of encirclement.",
    "createdAt": "2025-07-25T14:49:45.120000Z",
    "id": "1763356",
    "parentCommentID": "1763355",
    "parentEntityID": 18396,
    "parentEntityType": "Event",
    "profile": {
      "baseAddress": "0x1234567890abcdef1234567890abcdef12345678",
      "displayUsernamePublic": true,
      "name": "trader",
      "proxyWallet": "0x9876543210fedcba9876543210fedcba98765432",
      "pseudonym": "Bright-Analysis"
    },
    "reactionCount": 0,
    "replyAddress": "0x0bda5d16f76cd1d3485bcc7a44bc6fa7db004cdd",
    "reportCount": 0,
    "userAddress": "0x1234567890abcdef1234567890abcdef12345678"
  }
}
​
Comment Hierarchy
Comments support nested threading:
Top-level comments: parentCommentID is null or empty
Reply comments: parentCommentID contains the ID of the parent comment
All comments are associated with a parentEntityID and parentEntityType
​
Use Cases
Real-time comment feed displays
Discussion thread monitoring
Community sentiment analysis
​
Content
Comments include reactionCount and reportCount
Comment body contains the full text content
​
Notes
The createdAt timestamp uses ISO 8601 format with timezone information
The outer timestamp field represents when the WebSocket message was sent
User profiles include both primary addresses and proxy wallet addresses
RTDS Crypto Prices
Overview
Ask a question...

github
Powered by
RTDS Comments - Polymarket Documentation

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.polymarket.com/llms.txt
> Use this file to discover all available pages before exploring further.

# null

All market data necessary for market resolution is available on-chain (ie ancillaryData in UMA 00 request), but Polymarket also provides a hosted service, Gamma, that indexes this data and provides additional market metadata (ie categorization, indexed volume, etc). This service is made available through a REST API. For public users, this resource read only and can be used to fetch useful information about markets for things like non-profit research projects, alternative trading interfaces, automated trading systems etc.

# Endpoint

[https://gamma-api.polymarket.com](https://gamma-api.polymarket.com)


Skip to main content
Polymarket Documentation home pagedark logo

Search...
Ctrl K

Ask AI
Main Site

User Guide
For Developers
Changelog
Polymarket
Discord Community
Twitter
Developer Quickstart
Developer Quickstart
Fetching Market Data
Placing Your First Order
Glossary
API Rate Limits
Endpoints
Market Makers
Market Maker Introduction
Setup
Trading
Liquidity Rewards
Maker Rebates Program
Data Feeds
Inventory Management
Polymarket Builders Program
Builder Program Introduction
Builder Tiers
Builder Profile & Keys
Order Attribution
Relayer Client
Examples
Central Limit Order Book
CLOB Introduction
Status
Quickstart
Authentication
Geographic Restrictions

Client
Methods Overview
Public Methods
L1 Methods
L2 Methods
Builder Methods

REST API

Orderbook
GET
Get order book summary
POST
Get multiple order books summaries by request

Pricing
GET
Get market price
GET
Get multiple market prices
POST
Get multiple market prices by request
GET
Get midpoint price
GET
Get price history for a traded token

Spreads
POST
Get bid-ask spreads

Historical Timeseries Data
GET
Historical Timeseries Data

Order Management
Orders Overview
Place Single Order
Place Multiple Orders (Batching)
Get Order
Get Active Orders
Check Order Reward Scoring
Cancel Orders(s)
Onchain Order Info

Trades
Trades Overview
Get Trades
Websocket
WSS Overview
WSS Quickstart
WSS Authentication
User Channel
Market Channel

Sports Websocket
Overview
Message Format
Quickstart
Real Time Data Stream
RTDS Overview
RTDS Crypto Prices
RTDS Comments
Gamma Structure
Overview
Gamma Structure
Fetching Markets
Gamma Endpoints

Gamma Status

Sports

Tags

Events

Markets

Series

Comments

Profiles

Search
Data-API

Data API Status

Core

Misc

Builders
Bridge & Swap
Overview

Bridge
Subgraph
Overview
Resolution
Resolution
Conditional Token Frameworks
Overview
Splitting USDC
Merging Tokens
Reedeeming Tokens
Deployment and Additional Information
Proxy Wallets
Proxy wallet
Negative Risk
Overview

On this page
Detail
Example
Gamma Structure
Gamma Structure
Gamma provides some organizational models. These include events, and markets. The most fundamental element is always markets and the other models simply provide additional organization.
​
Detail
Market
Contains data related to a market that is traded on. Maps onto a pair of clob token ids, a market address, a question id and a condition id
Event
Contains a set of markets
Variants:
Event with 1 market (i.e., resulting in an SMP)
Event with 2 or more markets (i.e., resulting in an GMP)
​
Example
[Event] Where will Barron Trump attend College?
[Market] Will Barron attend Georgetown?
[Market] Will Barron attend NYU?
[Market] Will Barron attend UPenn?
[Market] Will Barron attend Harvard?
[Market] Will Barron attend another college?
Overview
Fetching Markets
Ask a question...

github
Powered by
Gamma Structure - Polymarket Documentation

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.polymarket.com/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Fetch Markets

<Tip>Both the getEvents and getMarkets are paginated. See [pagination section](#pagination) for details.</Tip>
This guide covers the three recommended approaches for fetching market data from the Gamma API, each optimized for different use cases.

## Overview

There are three main strategies for retrieving market data:

1. **By Slug** - Best for fetching specific individual markets or events
2. **By Tags** - Ideal for filtering markets by category or sport
3. **Via Events Endpoint** - Most efficient for retrieving all active markets

***

## 1. Fetch by Slug

**Use Case:** When you need to retrieve a specific market or event that you already know about.

Individual markets and events are best fetched using their unique slug identifier. The slug can be found directly in the Polymarket frontend URL.

### How to Extract the Slug

From any Polymarket URL, the slug is the path segment after `/event/` or `/market/`:

```
https://polymarket.com/event/fed-decision-in-october?tid=1758818660485
                            ↑
                  Slug: fed-decision-in-october
```

### API Endpoints

**For Events:** [GET /events/slug/{slug}](/api-reference/events/list-events)

**For Markets:** [GET /markets/slug/{slug}](/api-reference/markets/list-markets)

### Examples

```bash  theme={null}
curl "https://gamma-api.polymarket.com/events/slug/fed-decision-in-october"
```

***

## 2. Fetch by Tags

**Use Case:** When you want to filter markets by category, sport, or topic.

Tags provide a powerful way to categorize and filter markets. You can discover available tags and then use them to filter your market requests.

### Discover Available Tags

**General Tags:** [GET /tags](/api-reference/tags/list-tags)

**Sports Tags & Metadata:** [GET /sports](/api-reference/sports/get-sports-metadata-information)

The `/sports` endpoint returns comprehensive metadata for sports including tag IDs, images, resolution sources, and series information.

### Using Tags in Market Requests

Once you have tag IDs, you can use them with the `tag_id` parameter in both markets and events endpoints.

**Markets with Tags:** [GET /markets](/api-reference/markets/list-markets)

**Events with Tags:** [GET /events](/api-reference/events/list-events)

```bash  theme={null}
curl "https://gamma-api.polymarket.com/events?tag_id=100381&limit=1&closed=false"

```

### Additional Tag Filtering

You can also:

* Use `related_tags=true` to include related tag markets
* Exclude specific tags with `exclude_tag_id`

***

## 3. Fetch All Active Markets

**Use Case:** When you need to retrieve all available active markets, typically for broader analysis or market discovery.

The most efficient approach is to use the `/events` endpoint and work backwards, as events contain their associated markets.

**Events Endpoint:** [GET /events](/api-reference/events/list-events)

**Markets Endpoint:** [GET /markets](/api-reference/markets/list-markets)

### Key Parameters

* `order=id` - Order by event ID
* `ascending=false` - Get newest events first
* `closed=false` - Only active markets
* `limit` - Control response size
* `offset` - For pagination

### Examples

```bash  theme={null}
curl "https://gamma-api.polymarket.com/events?order=id&ascending=false&closed=false&limit=100"
```

This approach gives you all active markets ordered from newest to oldest, allowing you to systematically process all available trading opportunities.

### Pagination

For large datasets, use pagination with `limit` and `offset` parameters:

* `limit=50` - Return 50 results per page
* `offset=0` - Start from the beginning (increment by limit for subsequent pages)

**Pagination Examples:**

```bash  theme={null}
# Page 1: First 50 results (offset=0)
curl "https://gamma-api.polymarket.com/events?order=id&ascending=false&closed=false&limit=50&offset=0"
```

```bash  theme={null}
# Page 2: Next 50 results (offset=50)
curl "https://gamma-api.polymarket.com/events?order=id&ascending=false&closed=false&limit=50&offset=50"
```

```bash  theme={null}
# Page 3: Next 50 results (offset=100)
curl "https://gamma-api.polymarket.com/events?order=id&ascending=false&closed=false&limit=50&offset=100"
```

```bash  theme={null}
# Paginating through markets with tag filtering
curl "https://gamma-api.polymarket.com/markets?tag_id=100381&closed=false&limit=25&offset=0"
```

```bash  theme={null}
# Next page of markets with tag filtering
curl "https://gamma-api.polymarket.com/markets?tag_id=100381&closed=false&limit=25&offset=25"
```

***

## Best Practices

1. **For Individual Markets:** Always use the slug method for best performance
2. **For Category Browsing:** Use tag filtering to reduce API calls
3. **For Complete Market Discovery:** Use the events endpoint with pagination
4. **Always Include `closed=false`:** Unless you specifically need historical data
5. **Implement Rate Limiting:** Respect API limits for production applications

## Related Endpoints

* [Get Markets](/developers/gamma-markets-api/get-markets) - Full markets endpoint documentation
* [Get Events](/developers/gamma-markets-api/get-events) - Full events endpoint documentation
* [Search Markets](/developers/gamma-markets-api/get-public-search) - Search functionality


Skip to main content
Polymarket Documentation home pagedark logo

Search...
Ctrl K

Ask AI
Main Site

User Guide
For Developers
Changelog
Polymarket
Discord Community
Twitter
Developer Quickstart
Developer Quickstart
Fetching Market Data
Placing Your First Order
Glossary
API Rate Limits
Endpoints
Market Makers
Market Maker Introduction
Setup
Trading
Liquidity Rewards
Maker Rebates Program
Data Feeds
Inventory Management
Polymarket Builders Program
Builder Program Introduction
Builder Tiers
Builder Profile & Keys
Order Attribution
Relayer Client
Examples
Central Limit Order Book
CLOB Introduction
Status
Quickstart
Authentication
Geographic Restrictions

Client
Methods Overview
Public Methods
L1 Methods
L2 Methods
Builder Methods

REST API

Orderbook
GET
Get order book summary
POST
Get multiple order books summaries by request

Pricing
GET
Get market price
GET
Get multiple market prices
POST
Get multiple market prices by request
GET
Get midpoint price
GET
Get price history for a traded token

Spreads
POST
Get bid-ask spreads

Historical Timeseries Data
GET
Historical Timeseries Data

Order Management
Orders Overview
Place Single Order
Place Multiple Orders (Batching)
Get Order
Get Active Orders
Check Order Reward Scoring
Cancel Orders(s)
Onchain Order Info

Trades
Trades Overview
Get Trades
Websocket
WSS Overview
WSS Quickstart
WSS Authentication
User Channel
Market Channel

Sports Websocket
Overview
Message Format
Quickstart
Real Time Data Stream
RTDS Overview
RTDS Crypto Prices
RTDS Comments
Gamma Structure
Overview
Gamma Structure
Fetching Markets
Gamma Endpoints

Gamma Status
GET
Gamma API Health check

Sports

Tags

Events

Markets

Series

Comments

Profiles

Search
Data-API

Data API Status

Core

Misc

Builders
Bridge & Swap
Overview

Bridge
Subgraph
Overview
Resolution
Resolution
Conditional Token Frameworks
Overview
Splitting USDC
Merging Tokens
Reedeeming Tokens
Deployment and Additional Information
Proxy Wallets
Proxy wallet
Negative Risk
Overview
Gamma API Health check

curl --request GET \
  --url https://gamma-api.polymarket.com/status

200
"OK"
Gamma Status
Gamma API Health check
GET
/
status

Try it
Response
200 - text/plain
OK

The response is of type string.

Example:
"OK"

Fetching Markets
List teams
Ask a question...

github
Powered by
Gamma API Health check - Polymarket Documentation
Skip to main content
Polymarket Documentation home pagedark logo

Search...
Ctrl K

Ask AI
Main Site

User Guide
For Developers
Changelog
Polymarket
Discord Community
Twitter
Developer Quickstart
Developer Quickstart
Fetching Market Data
Placing Your First Order
Glossary
API Rate Limits
Endpoints
Market Makers
Market Maker Introduction
Setup
Trading
Liquidity Rewards
Maker Rebates Program
Data Feeds
Inventory Management
Polymarket Builders Program
Builder Program Introduction
Builder Tiers
Builder Profile & Keys
Order Attribution
Relayer Client
Examples
Central Limit Order Book
CLOB Introduction
Status
Quickstart
Authentication
Geographic Restrictions

Client
Methods Overview
Public Methods
L1 Methods
L2 Methods
Builder Methods

REST API

Orderbook
GET
Get order book summary
POST
Get multiple order books summaries by request

Pricing
GET
Get market price
GET
Get multiple market prices
POST
Get multiple market prices by request
GET
Get midpoint price
GET
Get price history for a traded token

Spreads
POST
Get bid-ask spreads

Historical Timeseries Data
GET
Historical Timeseries Data

Order Management
Orders Overview
Place Single Order
Place Multiple Orders (Batching)
Get Order
Get Active Orders
Check Order Reward Scoring
Cancel Orders(s)
Onchain Order Info

Trades
Trades Overview
Get Trades
Websocket
WSS Overview
WSS Quickstart
WSS Authentication
User Channel
Market Channel

Sports Websocket
Overview
Message Format
Quickstart
Real Time Data Stream
RTDS Overview
RTDS Crypto Prices
RTDS Comments
Gamma Structure
Overview
Gamma Structure
Fetching Markets
Gamma Endpoints

Gamma Status
GET
Gamma API Health check

Sports
GET
List teams
GET
Get sports metadata information
GET
Get valid sports market types

Tags

Events

Markets

Series

Comments

Profiles

Search
Data-API

Data API Status

Core

Misc

Builders
Bridge & Swap
Overview

Bridge
Subgraph
Overview
Resolution
Resolution
Conditional Token Frameworks
Overview
Splitting USDC
Merging Tokens
Reedeeming Tokens
Deployment and Additional Information
Proxy Wallets
Proxy wallet
Negative Risk
Overview
List teams

curl --request GET \
  --url https://gamma-api.polymarket.com/teams

200
[
  {
    "id": 123,
    "name": "<string>",
    "league": "<string>",
    "record": "<string>",
    "logo": "<string>",
    "abbreviation": "<string>",
    "alias": "<string>",
    "createdAt": "2023-11-07T05:31:56Z",
    "updatedAt": "2023-11-07T05:31:56Z"
  }
]
Sports
List teams
GET
/
teams

Try it
Query Parameters
​
limit
integer
Required range: x >= 0
​
offset
integer
Required range: x >= 0
​
order
string
Comma-separated list of fields to order by

​
ascending
boolean
​
league
string[]
​
name
string[]
​
abbreviation
string[]
Response
200 - application/json
List of teams

​
id
integer
​
name
string | null
​
league
string | null
​
record
string | null
​
logo
string | null
​
abbreviation
string | null
​
alias
string | null
​
createdAt
string<date-time> | null
​
updatedAt
string<date-time> | null
Gamma API Health check
Get sports metadata information
Ask a question...

github
Powered by
List teams - Polymarket Documentation

Skip to main content
Polymarket Documentation home pagedark logo

Search...
Ctrl K

Ask AI
Main Site

User Guide
For Developers
Changelog
Polymarket
Discord Community
Twitter
Developer Quickstart
Developer Quickstart
Fetching Market Data
Placing Your First Order
Glossary
API Rate Limits
Endpoints
Market Makers
Market Maker Introduction
Setup
Trading
Liquidity Rewards
Maker Rebates Program
Data Feeds
Inventory Management
Polymarket Builders Program
Builder Program Introduction
Builder Tiers
Builder Profile & Keys
Order Attribution
Relayer Client
Examples
Central Limit Order Book
CLOB Introduction
Status
Quickstart
Authentication
Geographic Restrictions

Client
Methods Overview
Public Methods
L1 Methods
L2 Methods
Builder Methods

REST API

Orderbook
GET
Get order book summary
POST
Get multiple order books summaries by request

Pricing
GET
Get market price
GET
Get multiple market prices
POST
Get multiple market prices by request
GET
Get midpoint price
GET
Get price history for a traded token

Spreads
POST
Get bid-ask spreads

Historical Timeseries Data
GET
Historical Timeseries Data

Order Management
Orders Overview
Place Single Order
Place Multiple Orders (Batching)
Get Order
Get Active Orders
Check Order Reward Scoring
Cancel Orders(s)
Onchain Order Info

Trades
Trades Overview
Get Trades
Websocket
WSS Overview
WSS Quickstart
WSS Authentication
User Channel
Market Channel

Sports Websocket
Overview
Message Format
Quickstart
Real Time Data Stream
RTDS Overview
RTDS Crypto Prices
RTDS Comments
Gamma Structure
Overview
Gamma Structure
Fetching Markets
Gamma Endpoints

Gamma Status
GET
Gamma API Health check

Sports
GET
List teams
GET
Get sports metadata information
GET
Get valid sports market types

Tags

Events

Markets

Series

Comments

Profiles

Search
Data-API

Data API Status

Core

Misc

Builders
Bridge & Swap
Overview

Bridge
Subgraph
Overview
Resolution
Resolution
Conditional Token Frameworks
Overview
Splitting USDC
Merging Tokens
Reedeeming Tokens
Deployment and Additional Information
Proxy Wallets
Proxy wallet
Negative Risk
Overview
Get sports metadata information

curl --request GET \
  --url https://gamma-api.polymarket.com/sports

200
[
  {
    "sport": "<string>",
    "image": "<string>",
    "resolution": "<string>",
    "ordering": "<string>",
    "tags": "<string>",
    "series": "<string>"
  }
]
Sports
Get sports metadata information
Retrieves metadata for various sports including images, resolution sources, ordering preferences, tags, and series information. This endpoint provides comprehensive sport configuration data used throughout the platform.

GET
/
sports

Try it
Response
200 - application/json
List of sports metadata objects containing sport configuration details, visual assets, and related identifiers

​
sport
string
The sport identifier or abbreviation

​
image
string<uri>
URL to the sport's logo or image asset

​
resolution
string<uri>
URL to the official resolution source for the sport (e.g., league website)

​
ordering
string
Preferred ordering for sport display, typically "home" or "away"

​
tags
string
Comma-separated list of tag IDs associated with the sport for categorization and filtering

​
series
string
Series identifier linking the sport to a specific tournament or season series

List teams
Get valid sports market types
Ask a question...

github
Powered by
Get sports metadata information - Polymarket Documentation

Skip to main content
Polymarket Documentation home pagedark logo

Search...
Ctrl K

Ask AI
Main Site

User Guide
For Developers
Changelog
Polymarket
Discord Community
Twitter
Developer Quickstart
Developer Quickstart
Fetching Market Data
Placing Your First Order
Glossary
API Rate Limits
Endpoints
Market Makers
Market Maker Introduction
Setup
Trading
Liquidity Rewards
Maker Rebates Program
Data Feeds
Inventory Management
Polymarket Builders Program
Builder Program Introduction
Builder Tiers
Builder Profile & Keys
Order Attribution
Relayer Client
Examples
Central Limit Order Book
CLOB Introduction
Status
Quickstart
Authentication
Geographic Restrictions

Client
Methods Overview
Public Methods
L1 Methods
L2 Methods
Builder Methods

REST API

Orderbook
GET
Get order book summary
POST
Get multiple order books summaries by request

Pricing
GET
Get market price
GET
Get multiple market prices
POST
Get multiple market prices by request
GET
Get midpoint price
GET
Get price history for a traded token

Spreads
POST
Get bid-ask spreads

Historical Timeseries Data
GET
Historical Timeseries Data

Order Management
Orders Overview
Place Single Order
Place Multiple Orders (Batching)
Get Order
Get Active Orders
Check Order Reward Scoring
Cancel Orders(s)
Onchain Order Info

Trades
Trades Overview
Get Trades
Websocket
WSS Overview
WSS Quickstart
WSS Authentication
User Channel
Market Channel

Sports Websocket
Overview
Message Format
Quickstart
Real Time Data Stream
RTDS Overview
RTDS Crypto Prices
RTDS Comments
Gamma Structure
Overview
Gamma Structure
Fetching Markets
Gamma Endpoints

Gamma Status
GET
Gamma API Health check

Sports
GET
List teams
GET
Get sports metadata information
GET
Get valid sports market types

Tags

Events

Markets

Series

Comments

Profiles

Search
Data-API

Data API Status

Core

Misc

Builders
Bridge & Swap
Overview

Bridge
Subgraph
Overview
Resolution
Resolution
Conditional Token Frameworks
Overview
Splitting USDC
Merging Tokens
Reedeeming Tokens
Deployment and Additional Information
Proxy Wallets
Proxy wallet
Negative Risk
Overview
Get valid sports market types

curl --request GET \
  --url https://gamma-api.polymarket.com/sports/market-types

200
{
  "marketTypes": [
    "<string>"
  ]
}
Sports
Get valid sports market types
Get a list of all valid sports market types available on the platform. Use these values when filtering markets by the sportsMarketTypes parameter.

GET
/
sports
/
market-types

Try it
Response
200 - application/json
List of valid sports market types

​
marketTypes
string[]
List of all valid sports market types

Get sports metadata information
List tags
Ask a question...

github
Powered by
Get valid sports market types - Polymarket Documentation

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.polymarket.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List tags



## OpenAPI

````yaml api-reference/gamma-openapi.json get /tags
openapi: 3.0.3
info:
  title: Markets API
  version: 1.0.0
  description: REST API specification for public endpoints used by the Markets service.
servers:
  - url: https://gamma-api.polymarket.com
    description: Polymarket Gamma API Production Server
security: []
tags:
  - name: Gamma Status
    description: Gamma API status and health check
  - name: Sports
    description: Sports-related endpoints including teams and game data
  - name: Tags
    description: Tag management and related tag operations
  - name: Events
    description: Event management and event-related operations
  - name: Markets
    description: Market data and market-related operations
  - name: Comments
    description: Comment system and user interactions
  - name: Series
    description: Series management and related operations
  - name: Profiles
    description: User profile management
  - name: Search
    description: Search functionality across different entity types
paths:
  /tags:
    get:
      tags:
        - Tags
      summary: List tags
      operationId: listTags
      parameters:
        - $ref: '#/components/parameters/limit'
        - $ref: '#/components/parameters/offset'
        - $ref: '#/components/parameters/order'
        - $ref: '#/components/parameters/ascending'
        - name: include_template
          in: query
          schema:
            type: boolean
        - name: is_carousel
          in: query
          schema:
            type: boolean
      responses:
        '200':
          description: List of tags
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Tag'
components:
  parameters:
    limit:
      name: limit
      in: query
      schema:
        type: integer
        minimum: 0
    offset:
      name: offset
      in: query
      schema:
        type: integer
        minimum: 0
    order:
      name: order
      in: query
      schema:
        type: string
      description: Comma-separated list of fields to order by
    ascending:
      name: ascending
      in: query
      schema:
        type: boolean
  schemas:
    Tag:
      type: object
      properties:
        id:
          type: string
        label:
          type: string
          nullable: true
        slug:
          type: string
          nullable: true
        forceShow:
          type: boolean
          nullable: true
        publishedAt:
          type: string
          nullable: true
        createdBy:
          type: integer
          nullable: true
        updatedBy:
          type: integer
          nullable: true
        createdAt:
          type: string
          format: date-time
          nullable: true
        updatedAt:
          type: string
          format: date-time
          nullable: true
        forceHide:
          type: boolean
          nullable: true
        isCarousel:
          type: boolean
          nullable: true

````

Skip to main content
Polymarket Documentation home pagedark logo

Search...
Ctrl K

Ask AI
Main Site

User Guide
For Developers
Changelog
Polymarket
Discord Community
Twitter
Developer Quickstart
Developer Quickstart
Fetching Market Data
Placing Your First Order
Glossary
API Rate Limits
Endpoints
Market Makers
Market Maker Introduction
Setup
Trading
Liquidity Rewards
Maker Rebates Program
Data Feeds
Inventory Management
Polymarket Builders Program
Builder Program Introduction
Builder Tiers
Builder Profile & Keys
Order Attribution
Relayer Client
Examples
Central Limit Order Book
CLOB Introduction
Status
Quickstart
Authentication
Geographic Restrictions

Client
Methods Overview
Public Methods
L1 Methods
L2 Methods
Builder Methods

REST API

Orderbook
GET
Get order book summary
POST
Get multiple order books summaries by request

Pricing
GET
Get market price
GET
Get multiple market prices
POST
Get multiple market prices by request
GET
Get midpoint price
GET
Get price history for a traded token

Spreads
POST
Get bid-ask spreads

Historical Timeseries Data
GET
Historical Timeseries Data

Order Management
Orders Overview
Place Single Order
Place Multiple Orders (Batching)
Get Order
Get Active Orders
Check Order Reward Scoring
Cancel Orders(s)
Onchain Order Info

Trades
Trades Overview
Get Trades
Websocket
WSS Overview
WSS Quickstart
WSS Authentication
User Channel
Market Channel

Sports Websocket
Overview
Message Format
Quickstart
Real Time Data Stream
RTDS Overview
RTDS Crypto Prices
RTDS Comments
Gamma Structure
Overview
Gamma Structure
Fetching Markets
Gamma Endpoints

Gamma Status
GET
Gamma API Health check

Sports
GET
List teams
GET
Get sports metadata information
GET
Get valid sports market types

Tags
GET
List tags
GET
Get tag by id
GET
Get tag by slug
GET
Get related tags (relationships) by tag id
GET
Get related tags (relationships) by tag slug
GET
Get tags related to a tag id
GET
Get tags related to a tag slug

Events

Markets

Series

Comments

Profiles

Search
Data-API

Data API Status

Core

Misc

Builders
Bridge & Swap
Overview

Bridge
Subgraph
Overview
Resolution
Resolution
Conditional Token Frameworks
Overview
Splitting USDC
Merging Tokens
Reedeeming Tokens
Deployment and Additional Information
Proxy Wallets
Proxy wallet
Negative Risk
Overview
Get tag by id

curl --request GET \
  --url https://gamma-api.polymarket.com/tags/{id}

200
{
  "id": "<string>",
  "label": "<string>",
  "slug": "<string>",
  "forceShow": true,
  "publishedAt": "<string>",
  "createdBy": 123,
  "updatedBy": 123,
  "createdAt": "2023-11-07T05:31:56Z",
  "updatedAt": "2023-11-07T05:31:56Z",
  "forceHide": true,
  "isCarousel": true
}
Tags
Get tag by id
GET
/
tags
/
{id}

Try it
Path Parameters
​
id
integerrequired
Query Parameters
​
include_template
boolean
Response

200

application/json
Tag

​
id
string
​
label
string | null
​
slug
string | null
​
forceShow
boolean | null
​
publishedAt
string | null
​
createdBy
integer | null
​
updatedBy
integer | null
​
createdAt
string<date-time> | null
​
updatedAt
string<date-time> | null
​
forceHide
boolean | null
​
isCarousel
boolean | null
List tags
Get tag by slug
Ask a question...

github
Powered by
Get tag by id - Polymarket Documentation

Skip to main content
Polymarket Documentation home pagedark logo

Search...
Ctrl K

Ask AI
Main Site

User Guide
For Developers
Changelog
Polymarket
Discord Community
Twitter
Developer Quickstart
Developer Quickstart
Fetching Market Data
Placing Your First Order
Glossary
API Rate Limits
Endpoints
Market Makers
Market Maker Introduction
Setup
Trading
Liquidity Rewards
Maker Rebates Program
Data Feeds
Inventory Management
Polymarket Builders Program
Builder Program Introduction
Builder Tiers
Builder Profile & Keys
Order Attribution
Relayer Client
Examples
Central Limit Order Book
CLOB Introduction
Status
Quickstart
Authentication
Geographic Restrictions

Client
Methods Overview
Public Methods
L1 Methods
L2 Methods
Builder Methods

REST API

Orderbook
GET
Get order book summary
POST
Get multiple order books summaries by request

Pricing
GET
Get market price
GET
Get multiple market prices
POST
Get multiple market prices by request
GET
Get midpoint price
GET
Get price history for a traded token

Spreads
POST
Get bid-ask spreads

Historical Timeseries Data
GET
Historical Timeseries Data

Order Management
Orders Overview
Place Single Order
Place Multiple Orders (Batching)
Get Order
Get Active Orders
Check Order Reward Scoring
Cancel Orders(s)
Onchain Order Info

Trades
Trades Overview
Get Trades
Websocket
WSS Overview
WSS Quickstart
WSS Authentication
User Channel
Market Channel

Sports Websocket
Overview
Message Format
Quickstart
Real Time Data Stream
RTDS Overview
RTDS Crypto Prices
RTDS Comments
Gamma Structure
Overview
Gamma Structure
Fetching Markets
Gamma Endpoints

Gamma Status
GET
Gamma API Health check

Sports
GET
List teams
GET
Get sports metadata information
GET
Get valid sports market types

Tags
GET
List tags
GET
Get tag by id
GET
Get tag by slug
GET
Get related tags (relationships) by tag id
GET
Get related tags (relationships) by tag slug
GET
Get tags related to a tag id
GET
Get tags related to a tag slug

Events

Markets

Series

Comments

Profiles

Search
Data-API

Data API Status

Core

Misc

Builders
Bridge & Swap
Overview

Bridge
Subgraph
Overview
Resolution
Resolution
Conditional Token Frameworks
Overview
Splitting USDC
Merging Tokens
Reedeeming Tokens
Deployment and Additional Information
Proxy Wallets
Proxy wallet
Negative Risk
Overview
Get tag by slug

curl --request GET \
  --url https://gamma-api.polymarket.com/tags/slug/{slug}

200
{
  "id": "<string>",
  "label": "<string>",
  "slug": "<string>",
  "forceShow": true,
  "publishedAt": "<string>",
  "createdBy": 123,
  "updatedBy": 123,
  "createdAt": "2023-11-07T05:31:56Z",
  "updatedAt": "2023-11-07T05:31:56Z",
  "forceHide": true,
  "isCarousel": true
}
Tags
Get tag by slug
GET
/
tags
/
slug
/
{slug}

Try it
Path Parameters
​
slug
stringrequired
Query Parameters
​
include_template
boolean
Response

200

application/json
Tag

​
id
string
​
label
string | null
​
slug
string | null
​
forceShow
boolean | null
​
publishedAt
string | null
​
createdBy
integer | null
​
updatedBy
integer | null
​
createdAt
string<date-time> | null
​
updatedAt
string<date-time> | null
​
forceHide
boolean | null
​
isCarousel
boolean | null
Get tag by id
Get related tags (relationships) by tag id
Ask a question...

github
Powered by
Get tag by slug - Polymarket Documentation

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.polymarket.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get related tags (relationships) by tag id



## OpenAPI

````yaml api-reference/gamma-openapi.json get /tags/{id}/related-tags
openapi: 3.0.3
info:
  title: Markets API
  version: 1.0.0
  description: REST API specification for public endpoints used by the Markets service.
servers:
  - url: https://gamma-api.polymarket.com
    description: Polymarket Gamma API Production Server
security: []
tags:
  - name: Gamma Status
    description: Gamma API status and health check
  - name: Sports
    description: Sports-related endpoints including teams and game data
  - name: Tags
    description: Tag management and related tag operations
  - name: Events
    description: Event management and event-related operations
  - name: Markets
    description: Market data and market-related operations
  - name: Comments
    description: Comment system and user interactions
  - name: Series
    description: Series management and related operations
  - name: Profiles
    description: User profile management
  - name: Search
    description: Search functionality across different entity types
paths:
  /tags/{id}/related-tags:
    get:
      tags:
        - Tags
      summary: Get related tags (relationships) by tag id
      operationId: getRelatedTagsById
      parameters:
        - $ref: '#/components/parameters/pathId'
        - name: omit_empty
          in: query
          schema:
            type: boolean
        - name: status
          in: query
          schema:
            type: string
            enum:
              - active
              - closed
              - all
      responses:
        '200':
          description: Related tag relationships
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/RelatedTag'
components:
  parameters:
    pathId:
      name: id
      in: path
      required: true
      schema:
        type: integer
  schemas:
    RelatedTag:
      type: object
      properties:
        id:
          type: string
        tagID:
          type: integer
          nullable: true
        relatedTagID:
          type: integer
          nullable: true
        rank:
          type: integer
          nullable: true

````

Skip to main content
Polymarket Documentation home pagedark logo

Search...
Ctrl K

Ask AI
Main Site

User Guide
For Developers
Changelog
Polymarket
Discord Community
Twitter
Developer Quickstart
Developer Quickstart
Fetching Market Data
Placing Your First Order
Glossary
API Rate Limits
Endpoints
Market Makers
Market Maker Introduction
Setup
Trading
Liquidity Rewards
Maker Rebates Program
Data Feeds
Inventory Management
Polymarket Builders Program
Builder Program Introduction
Builder Tiers
Builder Profile & Keys
Order Attribution
Relayer Client
Examples
Central Limit Order Book
CLOB Introduction
Status
Quickstart
Authentication
Geographic Restrictions

Client
Methods Overview
Public Methods
L1 Methods
L2 Methods
Builder Methods

REST API

Orderbook
GET
Get order book summary
POST
Get multiple order books summaries by request

Pricing
GET
Get market price
GET
Get multiple market prices
POST
Get multiple market prices by request
GET
Get midpoint price
GET
Get price history for a traded token

Spreads
POST
Get bid-ask spreads

Historical Timeseries Data
GET
Historical Timeseries Data

Order Management
Orders Overview
Place Single Order
Place Multiple Orders (Batching)
Get Order
Get Active Orders
Check Order Reward Scoring
Cancel Orders(s)
Onchain Order Info

Trades
Trades Overview
Get Trades
Websocket
WSS Overview
WSS Quickstart
WSS Authentication
User Channel
Market Channel

Sports Websocket
Overview
Message Format
Quickstart
Real Time Data Stream
RTDS Overview
RTDS Crypto Prices
RTDS Comments
Gamma Structure
Overview
Gamma Structure
Fetching Markets
Gamma Endpoints

Gamma Status
GET
Gamma API Health check

Sports
GET
List teams
GET
Get sports metadata information
GET
Get valid sports market types

Tags
GET
List tags
GET
Get tag by id
GET
Get tag by slug
GET
Get related tags (relationships) by tag id
GET
Get related tags (relationships) by tag slug
GET
Get tags related to a tag id
GET
Get tags related to a tag slug

Events

Markets

Series

Comments

Profiles

Search
Data-API

Data API Status

Core

Misc

Builders
Bridge & Swap
Overview

Bridge
Subgraph
Overview
Resolution
Resolution
Conditional Token Frameworks
Overview
Splitting USDC
Merging Tokens
Reedeeming Tokens
Deployment and Additional Information
Proxy Wallets
Proxy wallet
Negative Risk
Overview
Get related tags (relationships) by tag slug

curl --request GET \
  --url https://gamma-api.polymarket.com/tags/slug/{slug}/related-tags

200
[
  {
    "id": "<string>",
    "tagID": 123,
    "relatedTagID": 123,
    "rank": 123
  }
]
Tags
Get related tags (relationships) by tag slug
GET
/
tags
/
slug
/
{slug}
/
related-tags

Try it
Path Parameters
​
slug
stringrequired
Query Parameters
​
omit_empty
boolean
​
status
enum<string>
Available options: active, closed, all 
Response
200 - application/json
Related tag relationships

​
id
string
​
tagID
integer | null
​
relatedTagID
integer | null
​
rank
integer | null
Get related tags (relationships) by tag id
Get tags related to a tag id
Ask a question...

github
Powered by
Get related tags (relationships) by tag slug - Polymarket Documentation

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.polymarket.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get tags related to a tag id



## OpenAPI

````yaml api-reference/gamma-openapi.json get /tags/{id}/related-tags/tags
openapi: 3.0.3
info:
  title: Markets API
  version: 1.0.0
  description: REST API specification for public endpoints used by the Markets service.
servers:
  - url: https://gamma-api.polymarket.com
    description: Polymarket Gamma API Production Server
security: []
tags:
  - name: Gamma Status
    description: Gamma API status and health check
  - name: Sports
    description: Sports-related endpoints including teams and game data
  - name: Tags
    description: Tag management and related tag operations
  - name: Events
    description: Event management and event-related operations
  - name: Markets
    description: Market data and market-related operations
  - name: Comments
    description: Comment system and user interactions
  - name: Series
    description: Series management and related operations
  - name: Profiles
    description: User profile management
  - name: Search
    description: Search functionality across different entity types
paths:
  /tags/{id}/related-tags/tags:
    get:
      tags:
        - Tags
      summary: Get tags related to a tag id
      operationId: getTagsRelatedToATagById
      parameters:
        - $ref: '#/components/parameters/pathId'
        - name: omit_empty
          in: query
          schema:
            type: boolean
        - name: status
          in: query
          schema:
            type: string
            enum:
              - active
              - closed
              - all
      responses:
        '200':
          description: Related tags
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Tag'
components:
  parameters:
    pathId:
      name: id
      in: path
      required: true
      schema:
        type: integer
  schemas:
    Tag:
      type: object
      properties:
        id:
          type: string
        label:
          type: string
          nullable: true
        slug:
          type: string
          nullable: true
        forceShow:
          type: boolean
          nullable: true
        publishedAt:
          type: string
          nullable: true
        createdBy:
          type: integer
          nullable: true
        updatedBy:
          type: integer
          nullable: true
        createdAt:
          type: string
          format: date-time
          nullable: true
        updatedAt:
          type: string
          format: date-time
          nullable: true
        forceHide:
          type: boolean
          nullable: true
        isCarousel:
          type: boolean
          nullable: true

````

Skip to main content
Polymarket Documentation home pagedark logo

Search...
Ctrl K

Ask AI
Main Site

User Guide
For Developers
Changelog
Polymarket
Discord Community
Twitter
Developer Quickstart
Developer Quickstart
Fetching Market Data
Placing Your First Order
Glossary
API Rate Limits
Endpoints
Market Makers
Market Maker Introduction
Setup
Trading
Liquidity Rewards
Maker Rebates Program
Data Feeds
Inventory Management
Polymarket Builders Program
Builder Program Introduction
Builder Tiers
Builder Profile & Keys
Order Attribution
Relayer Client
Examples
Central Limit Order Book
CLOB Introduction
Status
Quickstart
Authentication
Geographic Restrictions

Client
Methods Overview
Public Methods
L1 Methods
L2 Methods
Builder Methods

REST API

Orderbook
GET
Get order book summary
POST
Get multiple order books summaries by request

Pricing
GET
Get market price
GET
Get multiple market prices
POST
Get multiple market prices by request
GET
Get midpoint price
GET
Get price history for a traded token

Spreads
POST
Get bid-ask spreads

Historical Timeseries Data
GET
Historical Timeseries Data

Order Management
Orders Overview
Place Single Order
Place Multiple Orders (Batching)
Get Order
Get Active Orders
Check Order Reward Scoring
Cancel Orders(s)
Onchain Order Info

Trades
Trades Overview
Get Trades
Websocket
WSS Overview
WSS Quickstart
WSS Authentication
User Channel
Market Channel

Sports Websocket
Overview
Message Format
Quickstart
Real Time Data Stream
RTDS Overview
RTDS Crypto Prices
RTDS Comments
Gamma Structure
Overview
Gamma Structure
Fetching Markets
Gamma Endpoints

Gamma Status
GET
Gamma API Health check

Sports
GET
List teams
GET
Get sports metadata information
GET
Get valid sports market types

Tags
GET
List tags
GET
Get tag by id
GET
Get tag by slug
GET
Get related tags (relationships) by tag id
GET
Get related tags (relationships) by tag slug
GET
Get tags related to a tag id
GET
Get tags related to a tag slug

Events

Markets

Series

Comments

Profiles

Search
Data-API

Data API Status

Core

Misc

Builders
Bridge & Swap
Overview

Bridge
Subgraph
Overview
Resolution
Resolution
Conditional Token Frameworks
Overview
Splitting USDC
Merging Tokens
Reedeeming Tokens
Deployment and Additional Information
Proxy Wallets
Proxy wallet
Negative Risk
Overview
Get tags related to a tag slug

curl --request GET \
  --url https://gamma-api.polymarket.com/tags/slug/{slug}/related-tags/tags

200
[
  {
    "id": "<string>",
    "label": "<string>",
    "slug": "<string>",
    "forceShow": true,
    "publishedAt": "<string>",
    "createdBy": 123,
    "updatedBy": 123,
    "createdAt": "2023-11-07T05:31:56Z",
    "updatedAt": "2023-11-07T05:31:56Z",
    "forceHide": true,
    "isCarousel": true
  }
]
Tags
Get tags related to a tag slug
GET
/
tags
/
slug
/
{slug}
/
related-tags
/
tags

Try it
Path Parameters
​
slug
stringrequired
Query Parameters
​
omit_empty
boolean
​
status
enum<string>
Available options: active, closed, all 
Response
200 - application/json
Related tags

​
id
string
​
label
string | null
​
slug
string | null
​
forceShow
boolean | null
​
publishedAt
string | null
​
createdBy
integer | null
​
updatedBy
integer | null
​
createdAt
string<date-time> | null
​
updatedAt
string<date-time> | null
​
forceHide
boolean | null
​
isCarousel
boolean | null
Get tags related to a tag id
List events
Ask a question...

github
Powered by
Get tags related to a tag slug - Polymarket Documentation

Skip to main content
Polymarket Documentation home pagedark logo

Search...
Ctrl K

Ask AI
Main Site

User Guide
For Developers
Changelog
Polymarket
Discord Community
Twitter
Developer Quickstart
Developer Quickstart
Fetching Market Data
Placing Your First Order
Glossary
API Rate Limits
Endpoints
Market Makers
Market Maker Introduction
Setup
Trading
Liquidity Rewards
Maker Rebates Program
Data Feeds
Inventory Management
Polymarket Builders Program
Builder Program Introduction
Builder Tiers
Builder Profile & Keys
Order Attribution
Relayer Client
Examples
Central Limit Order Book
CLOB Introduction
Status
Quickstart
Authentication
Geographic Restrictions

Client
Methods Overview
Public Methods
L1 Methods
L2 Methods
Builder Methods

REST API

Orderbook
GET
Get order book summary
POST
Get multiple order books summaries by request

Pricing
GET
Get market price
GET
Get multiple market prices
POST
Get multiple market prices by request
GET
Get midpoint price
GET
Get price history for a traded token

Spreads
POST
Get bid-ask spreads

Historical Timeseries Data
GET
Historical Timeseries Data

Order Management
Orders Overview
Place Single Order
Place Multiple Orders (Batching)
Get Order
Get Active Orders
Check Order Reward Scoring
Cancel Orders(s)
Onchain Order Info

Trades
Trades Overview
Get Trades
Websocket
WSS Overview
WSS Quickstart
WSS Authentication
User Channel
Market Channel

Sports Websocket
Overview
Message Format
Quickstart
Real Time Data Stream
RTDS Overview
RTDS Crypto Prices
RTDS Comments
Gamma Structure
Overview
Gamma Structure
Fetching Markets
Gamma Endpoints

Gamma Status
GET
Gamma API Health check

Sports
GET
List teams
GET
Get sports metadata information
GET
Get valid sports market types

Tags
GET
List tags
GET
Get tag by id
GET
Get tag by slug
GET
Get related tags (relationships) by tag id
GET
Get related tags (relationships) by tag slug
GET
Get tags related to a tag id
GET
Get tags related to a tag slug

Events
GET
List events
GET
Get event by id
GET
Get event tags
GET
Get event by slug

Markets

Series

Comments

Profiles

Search
Data-API

Data API Status

Core

Misc

Builders
Bridge & Swap
Overview

Bridge
Subgraph
Overview
Resolution
Resolution
Conditional Token Frameworks
Overview
Splitting USDC
Merging Tokens
Reedeeming Tokens
Deployment and Additional Information
Proxy Wallets
Proxy wallet
Negative Risk
Overview
List events

curl --request GET \
  --url https://gamma-api.polymarket.com/events

200
[
  {
    "id": "<string>",
    "ticker": "<string>",
    "slug": "<string>",
    "title": "<string>",
    "subtitle": "<string>",
    "description": "<string>",
    "resolutionSource": "<string>",
    "startDate": "2023-11-07T05:31:56Z",
    "creationDate": "2023-11-07T05:31:56Z",
    "endDate": "2023-11-07T05:31:56Z",
    "image": "<string>",
    "icon": "<string>",
    "active": true,
    "closed": true,
    "archived": true,
    "new": true,
    "featured": true,
    "restricted": true,
    "liquidity": 123,
    "volume": 123,
    "openInterest": 123,
    "sortBy": "<string>",
    "category": "<string>",
    "subcategory": "<string>",
    "isTemplate": true,
    "templateVariables": "<string>",
    "published_at": "<string>",
    "createdBy": "<string>",
    "updatedBy": "<string>",
    "createdAt": "2023-11-07T05:31:56Z",
    "updatedAt": "2023-11-07T05:31:56Z",
    "commentsEnabled": true,
    "competitive": 123,
    "volume24hr": 123,
    "volume1wk": 123,
    "volume1mo": 123,
    "volume1yr": 123,
    "featuredImage": "<string>",
    "disqusThread": "<string>",
    "parentEvent": "<string>",
    "enableOrderBook": true,
    "liquidityAmm": 123,
    "liquidityClob": 123,
    "negRisk": true,
    "negRiskMarketID": "<string>",
    "negRiskFeeBips": 123,
    "commentCount": 123,
    "imageOptimized": {
      "id": "<string>",
      "imageUrlSource": "<string>",
      "imageUrlOptimized": "<string>",
      "imageSizeKbSource": 123,
      "imageSizeKbOptimized": 123,
      "imageOptimizedComplete": true,
      "imageOptimizedLastUpdated": "<string>",
      "relID": 123,
      "field": "<string>",
      "relname": "<string>"
    },
    "iconOptimized": {
      "id": "<string>",
      "imageUrlSource": "<string>",
      "imageUrlOptimized": "<string>",
      "imageSizeKbSource": 123,
      "imageSizeKbOptimized": 123,
      "imageOptimizedComplete": true,
      "imageOptimizedLastUpdated": "<string>",
      "relID": 123,
      "field": "<string>",
      "relname": "<string>"
    },
    "featuredImageOptimized": {
      "id": "<string>",
      "imageUrlSource": "<string>",
      "imageUrlOptimized": "<string>",
      "imageSizeKbSource": 123,
      "imageSizeKbOptimized": 123,
      "imageOptimizedComplete": true,
      "imageOptimizedLastUpdated": "<string>",
      "relID": 123,
      "field": "<string>",
      "relname": "<string>"
    },
    "subEvents": [
      "<string>"
    ],
    "markets": [
      {
        "id": "<string>",
        "question": "<string>",
        "conditionId": "<string>",
        "slug": "<string>",
        "twitterCardImage": "<string>",
        "resolutionSource": "<string>",
        "endDate": "2023-11-07T05:31:56Z",
        "category": "<string>",
        "ammType": "<string>",
        "liquidity": "<string>",
        "sponsorName": "<string>",
        "sponsorImage": "<string>",
        "startDate": "2023-11-07T05:31:56Z",
        "xAxisValue": "<string>",
        "yAxisValue": "<string>",
        "denominationToken": "<string>",
        "fee": "<string>",
        "image": "<string>",
        "icon": "<string>",
        "lowerBound": "<string>",
        "upperBound": "<string>",
        "description": "<string>",
        "outcomes": "<string>",
        "outcomePrices": "<string>",
        "volume": "<string>",
        "active": true,
        "marketType": "<string>",
        "formatType": "<string>",
        "lowerBoundDate": "<string>",
        "upperBoundDate": "<string>",
        "closed": true,
        "marketMakerAddress": "<string>",
        "createdBy": 123,
        "updatedBy": 123,
        "createdAt": "2023-11-07T05:31:56Z",
        "updatedAt": "2023-11-07T05:31:56Z",
        "closedTime": "<string>",
        "wideFormat": true,
        "new": true,
        "mailchimpTag": "<string>",
        "featured": true,
        "archived": true,
        "resolvedBy": "<string>",
        "restricted": true,
        "marketGroup": 123,
        "groupItemTitle": "<string>",
        "groupItemThreshold": "<string>",
        "questionID": "<string>",
        "umaEndDate": "<string>",
        "enableOrderBook": true,
        "orderPriceMinTickSize": 123,
        "orderMinSize": 123,
        "umaResolutionStatus": "<string>",
        "curationOrder": 123,
        "volumeNum": 123,
        "liquidityNum": 123,
        "endDateIso": "<string>",
        "startDateIso": "<string>",
        "umaEndDateIso": "<string>",
        "hasReviewedDates": true,
        "readyForCron": true,
        "commentsEnabled": true,
        "volume24hr": 123,
        "volume1wk": 123,
        "volume1mo": 123,
        "volume1yr": 123,
        "gameStartTime": "<string>",
        "secondsDelay": 123,
        "clobTokenIds": "<string>",
        "disqusThread": "<string>",
        "shortOutcomes": "<string>",
        "teamAID": "<string>",
        "teamBID": "<string>",
        "umaBond": "<string>",
        "umaReward": "<string>",
        "fpmmLive": true,
        "volume24hrAmm": 123,
        "volume1wkAmm": 123,
        "volume1moAmm": 123,
        "volume1yrAmm": 123,
        "volume24hrClob": 123,
        "volume1wkClob": 123,
        "volume1moClob": 123,
        "volume1yrClob": 123,
        "volumeAmm": 123,
        "volumeClob": 123,
        "liquidityAmm": 123,
        "liquidityClob": 123,
        "makerBaseFee": 123,
        "takerBaseFee": 123,
        "customLiveness": 123,
        "acceptingOrders": true,
        "notificationsEnabled": true,
        "score": 123,
        "imageOptimized": {
          "id": "<string>",
          "imageUrlSource": "<string>",
          "imageUrlOptimized": "<string>",
          "imageSizeKbSource": 123,
          "imageSizeKbOptimized": 123,
          "imageOptimizedComplete": true,
          "imageOptimizedLastUpdated": "<string>",
          "relID": 123,
          "field": "<string>",
          "relname": "<string>"
        },
        "iconOptimized": {
          "id": "<string>",
          "imageUrlSource": "<string>",
          "imageUrlOptimized": "<string>",
          "imageSizeKbSource": 123,
          "imageSizeKbOptimized": 123,
          "imageOptimizedComplete": true,
          "imageOptimizedLastUpdated": "<string>",
          "relID": 123,
          "field": "<string>",
          "relname": "<string>"
        },
        "events": "<array>",
        "categories": [
          {
            "id": "<string>",
            "label": "<string>",
            "parentCategory": "<string>",
            "slug": "<string>",
            "publishedAt": "<string>",
            "createdBy": "<string>",
            "updatedBy": "<string>",
            "createdAt": "2023-11-07T05:31:56Z",
            "updatedAt": "2023-11-07T05:31:56Z"
          }
        ],
        "tags": [
          {
            "id": "<string>",
            "label": "<string>",
            "slug": "<string>",
            "forceShow": true,
            "publishedAt": "<string>",
            "createdBy": 123,
            "updatedBy": 123,
            "createdAt": "2023-11-07T05:31:56Z",
            "updatedAt": "2023-11-07T05:31:56Z",
            "forceHide": true,
            "isCarousel": true
          }
        ],
        "creator": "<string>",
        "ready": true,
        "funded": true,
        "pastSlugs": "<string>",
        "readyTimestamp": "2023-11-07T05:31:56Z",
        "fundedTimestamp": "2023-11-07T05:31:56Z",
        "acceptingOrdersTimestamp": "2023-11-07T05:31:56Z",
        "competitive": 123,
        "rewardsMinSize": 123,
        "rewardsMaxSpread": 123,
        "spread": 123,
        "automaticallyResolved": true,
        "oneDayPriceChange": 123,
        "oneHourPriceChange": 123,
        "oneWeekPriceChange": 123,
        "oneMonthPriceChange": 123,
        "oneYearPriceChange": 123,
        "lastTradePrice": 123,
        "bestBid": 123,
        "bestAsk": 123,
        "automaticallyActive": true,
        "clearBookOnStart": true,
        "chartColor": "<string>",
        "seriesColor": "<string>",
        "showGmpSeries": true,
        "showGmpOutcome": true,
        "manualActivation": true,
        "negRiskOther": true,
        "gameId": "<string>",
        "groupItemRange": "<string>",
        "sportsMarketType": "<string>",
        "line": 123,
        "umaResolutionStatuses": "<string>",
        "pendingDeployment": true,
        "deploying": true,
        "deployingTimestamp": "2023-11-07T05:31:56Z",
        "scheduledDeploymentTimestamp": "2023-11-07T05:31:56Z",
        "rfqEnabled": true,
        "eventStartTime": "2023-11-07T05:31:56Z"
      }
    ],
    "series": [
      {
        "id": "<string>",
        "ticker": "<string>",
        "slug": "<string>",
        "title": "<string>",
        "subtitle": "<string>",
        "seriesType": "<string>",
        "recurrence": "<string>",
        "description": "<string>",
        "image": "<string>",
        "icon": "<string>",
        "layout": "<string>",
        "active": true,
        "closed": true,
        "archived": true,
        "new": true,
        "featured": true,
        "restricted": true,
        "isTemplate": true,
        "templateVariables": true,
        "publishedAt": "<string>",
        "createdBy": "<string>",
        "updatedBy": "<string>",
        "createdAt": "2023-11-07T05:31:56Z",
        "updatedAt": "2023-11-07T05:31:56Z",
        "commentsEnabled": true,
        "competitive": "<string>",
        "volume24hr": 123,
        "volume": 123,
        "liquidity": 123,
        "startDate": "2023-11-07T05:31:56Z",
        "pythTokenID": "<string>",
        "cgAssetName": "<string>",
        "score": 123,
        "events": "<array>",
        "collections": [
          {
            "id": "<string>",
            "ticker": "<string>",
            "slug": "<string>",
            "title": "<string>",
            "subtitle": "<string>",
            "collectionType": "<string>",
            "description": "<string>",
            "tags": "<string>",
            "image": "<string>",
            "icon": "<string>",
            "headerImage": "<string>",
            "layout": "<string>",
            "active": true,
            "closed": true,
            "archived": true,
            "new": true,
            "featured": true,
            "restricted": true,
            "isTemplate": true,
            "templateVariables": "<string>",
            "publishedAt": "<string>",
            "createdBy": "<string>",
            "updatedBy": "<string>",
            "createdAt": "2023-11-07T05:31:56Z",
            "updatedAt": "2023-11-07T05:31:56Z",
            "commentsEnabled": true,
            "imageOptimized": {
              "id": "<string>",
              "imageUrlSource": "<string>",
              "imageUrlOptimized": "<string>",
              "imageSizeKbSource": 123,
              "imageSizeKbOptimized": 123,
              "imageOptimizedComplete": true,
              "imageOptimizedLastUpdated": "<string>",
              "relID": 123,
              "field": "<string>",
              "relname": "<string>"
            },
            "iconOptimized": {
              "id": "<string>",
              "imageUrlSource": "<string>",
              "imageUrlOptimized": "<string>",
              "imageSizeKbSource": 123,
              "imageSizeKbOptimized": 123,
              "imageOptimizedComplete": true,
              "imageOptimizedLastUpdated": "<string>",
              "relID": 123,
              "field": "<string>",
              "relname": "<string>"
            },
            "headerImageOptimized": {
              "id": "<string>",
              "imageUrlSource": "<string>",
              "imageUrlOptimized": "<string>",
              "imageSizeKbSource": 123,
              "imageSizeKbOptimized": 123,
              "imageOptimizedComplete": true,
              "imageOptimizedLastUpdated": "<string>",
              "relID": 123,
              "field": "<string>",
              "relname": "<string>"
            }
          }
        ],
        "categories": [
          {
            "id": "<string>",
            "label": "<string>",
            "parentCategory": "<string>",
            "slug": "<string>",
            "publishedAt": "<string>",
            "createdBy": "<string>",
            "updatedBy": "<string>",
            "createdAt": "2023-11-07T05:31:56Z",
            "updatedAt": "2023-11-07T05:31:56Z"
          }
        ],
        "tags": [
          {
            "id": "<string>",
            "label": "<string>",
            "slug": "<string>",
            "forceShow": true,
            "publishedAt": "<string>",
            "createdBy": 123,
            "updatedBy": 123,
            "createdAt": "2023-11-07T05:31:56Z",
            "updatedAt": "2023-11-07T05:31:56Z",
            "forceHide": true,
            "isCarousel": true
          }
        ],
        "commentCount": 123,
        "chats": [
          {
            "id": "<string>",
            "channelId": "<string>",
            "channelName": "<string>",
            "channelImage": "<string>",
            "live": true,
            "startTime": "2023-11-07T05:31:56Z",
            "endTime": "2023-11-07T05:31:56Z"
          }
        ]
      }
    ],
    "categories": [
      {
        "id": "<string>",
        "label": "<string>",
        "parentCategory": "<string>",
        "slug": "<string>",
        "publishedAt": "<string>",
        "createdBy": "<string>",
        "updatedBy": "<string>",
        "createdAt": "2023-11-07T05:31:56Z",
        "updatedAt": "2023-11-07T05:31:56Z"
      }
    ],
    "collections": [
      {
        "id": "<string>",
        "ticker": "<string>",
        "slug": "<string>",
        "title": "<string>",
        "subtitle": "<string>",
        "collectionType": "<string>",
        "description": "<string>",
        "tags": "<string>",
        "image": "<string>",
        "icon": "<string>",
        "headerImage": "<string>",
        "layout": "<string>",
        "active": true,
        "closed": true,
        "archived": true,
        "new": true,
        "featured": true,
        "restricted": true,
        "isTemplate": true,
        "templateVariables": "<string>",
        "publishedAt": "<string>",
        "createdBy": "<string>",
        "updatedBy": "<string>",
        "createdAt": "2023-11-07T05:31:56Z",
        "updatedAt": "2023-11-07T05:31:56Z",
        "commentsEnabled": true,
        "imageOptimized": {
          "id": "<string>",
          "imageUrlSource": "<string>",
          "imageUrlOptimized": "<string>",
          "imageSizeKbSource": 123,
          "imageSizeKbOptimized": 123,
          "imageOptimizedComplete": true,
          "imageOptimizedLastUpdated": "<string>",
          "relID": 123,
          "field": "<string>",
          "relname": "<string>"
        },
        "iconOptimized": {
          "id": "<string>",
          "imageUrlSource": "<string>",
          "imageUrlOptimized": "<string>",
          "imageSizeKbSource": 123,
          "imageSizeKbOptimized": 123,
          "imageOptimizedComplete": true,
          "imageOptimizedLastUpdated": "<string>",
          "relID": 123,
          "field": "<string>",
          "relname": "<string>"
        },
        "headerImageOptimized": {
          "id": "<string>",
          "imageUrlSource": "<string>",
          "imageUrlOptimized": "<string>",
          "imageSizeKbSource": 123,
          "imageSizeKbOptimized": 123,
          "imageOptimizedComplete": true,
          "imageOptimizedLastUpdated": "<string>",
          "relID": 123,
          "field": "<string>",
          "relname": "<string>"
        }
      }
    ],
    "tags": [
      {
        "id": "<string>",
        "label": "<string>",
        "slug": "<string>",
        "forceShow": true,
        "publishedAt": "<string>",
        "createdBy": 123,
        "updatedBy": 123,
        "createdAt": "2023-11-07T05:31:56Z",
        "updatedAt": "2023-11-07T05:31:56Z",
        "forceHide": true,
        "isCarousel": true
      }
    ],
    "cyom": true,
    "closedTime": "2023-11-07T05:31:56Z",
    "showAllOutcomes": true,
    "showMarketImages": true,
    "automaticallyResolved": true,
    "enableNegRisk": true,
    "automaticallyActive": true,
    "eventDate": "<string>",
    "startTime": "2023-11-07T05:31:56Z",
    "eventWeek": 123,
    "seriesSlug": "<string>",
    "score": "<string>",
    "elapsed": "<string>",
    "period": "<string>",
    "live": true,
    "ended": true,
    "finishedTimestamp": "2023-11-07T05:31:56Z",
    "gmpChartMode": "<string>",
    "eventCreators": [
      {
        "id": "<string>",
        "creatorName": "<string>",
        "creatorHandle": "<string>",
        "creatorUrl": "<string>",
        "creatorImage": "<string>",
        "createdAt": "2023-11-07T05:31:56Z",
        "updatedAt": "2023-11-07T05:31:56Z"
      }
    ],
    "tweetCount": 123,
    "chats": [
      {
        "id": "<string>",
        "channelId": "<string>",
        "channelName": "<string>",
        "channelImage": "<string>",
        "live": true,
        "startTime": "2023-11-07T05:31:56Z",
        "endTime": "2023-11-07T05:31:56Z"
      }
    ],
    "featuredOrder": 123,
    "estimateValue": true,
    "cantEstimate": true,
    "estimatedValue": "<string>",
    "templates": [
      {
        "id": "<string>",
        "eventTitle": "<string>",
        "eventSlug": "<string>",
        "eventImage": "<string>",
        "marketTitle": "<string>",
        "description": "<string>",
        "resolutionSource": "<string>",
        "negRisk": true,
        "sortBy": "<string>",
        "showMarketImages": true,
        "seriesSlug": "<string>",
        "outcomes": "<string>"
      }
    ],
    "spreadsMainLine": 123,
    "totalsMainLine": 123,
    "carouselMap": "<string>",
    "pendingDeployment": true,
    "deploying": true,
    "deployingTimestamp": "2023-11-07T05:31:56Z",
    "scheduledDeploymentTimestamp": "2023-11-07T05:31:56Z",
    "gameStatus": "<string>"
  }
]
Events
List events
GET
/
events

Try it
Query Parameters
​
limit
integer
Required range: x >= 0
​
offset
integer
Required range: x >= 0
​
order
string
Comma-separated list of fields to order by

​
ascending
boolean
​
id
integer[]
​
tag_id
integer
​
exclude_tag_id
integer[]
​
slug
string[]
​
tag_slug
string
​
related_tags
boolean
​
active
boolean
​
archived
boolean
​
featured
boolean
​
cyom
boolean
​
include_chat
boolean
​
include_template
boolean
​
recurrence
string
​
closed
boolean
​
liquidity_min
number
​
liquidity_max
number
​
volume_min
number
​
volume_max
number
​
start_date_min
string<date-time>
​
start_date_max
string<date-time>
​
end_date_min
string<date-time>
​
end_date_max
string<date-time>
Response
200 - application/json
List of events

​
id
string
​
ticker
string | null
​
slug
string | null
​
title
string | null
​
subtitle
string | null
​
description
string | null
​
resolutionSource
string | null
​
startDate
string<date-time> | null
​
creationDate
string<date-time> | null
​
endDate
string<date-time> | null
​
image
string | null
​
icon
string | null
​
active
boolean | null
​
closed
boolean | null
​
archived
boolean | null
​
new
boolean | null
​
featured
boolean | null
​
restricted
boolean | null
​
liquidity
number | null
​
volume
number | null
​
openInterest
number | null
​
sortBy
string | null
​
category
string | null
​
subcategory
string | null
​
isTemplate
boolean | null
​
templateVariables
string | null
​
published_at
string | null
​
createdBy
string | null
​
updatedBy
string | null
​
createdAt
string<date-time> | null
​
updatedAt
string<date-time> | null
​
commentsEnabled
boolean | null
​
competitive
number | null
​
volume24hr
number | null
​
volume1wk
number | null
​
volume1mo
number | null
​
volume1yr
number | null
​
featuredImage
string | null
​
disqusThread
string | null
​
parentEvent
string | null
​
enableOrderBook
boolean | null
​
liquidityAmm
number | null
​
liquidityClob
number | null
​
negRisk
boolean | null
​
negRiskMarketID
string | null
​
negRiskFeeBips
integer | null
​
commentCount
integer | null
​
imageOptimized
object
Show child attributes

​
iconOptimized
object
Show child attributes

​
featuredImageOptimized
object
Show child attributes

​
subEvents
string[] | null
​
markets
object[]
Show child attributes

​
series
object[]
Show child attributes

​
categories
object[]
Show child attributes

​
collections
object[]
Show child attributes

​
tags
object[]
Show child attributes

​
cyom
boolean | null
​
closedTime
string<date-time> | null
​
showAllOutcomes
boolean | null
​
showMarketImages
boolean | null
​
automaticallyResolved
boolean | null
​
enableNegRisk
boolean | null
​
automaticallyActive
boolean | null
​
eventDate
string | null
​
startTime
string<date-time> | null
​
eventWeek
integer | null
​
seriesSlug
string | null
​
score
string | null
​
elapsed
string | null
​
period
string | null
​
live
boolean | null
​
ended
boolean | null
​
finishedTimestamp
string<date-time> | null
​
gmpChartMode
string | null
​
eventCreators
object[]
Show child attributes

​
tweetCount
integer | null
​
chats
object[]
Show child attributes

​
featuredOrder
integer | null
​
estimateValue
boolean | null
​
cantEstimate
boolean | null
​
estimatedValue
string | null
​
templates
object[]
Show child attributes

​
spreadsMainLine
number | null
​
totalsMainLine
number | null
​
carouselMap
string | null
​
pendingDeployment
boolean | null
​
deploying
boolean | null
​
deployingTimestamp
string<date-time> | null
​
scheduledDeploymentTimestamp
string<date-time> | null
​
gameStatus
string | null
Get tags related to a tag slug
Get event by id
Ask a question...

github
Powered by
List events - Polymarket Documentation

Skip to main content
Polymarket Documentation home pagedark logo

Search...
Ctrl K

Ask AI
Main Site

User Guide
For Developers
Changelog
Polymarket
Discord Community
Twitter
Developer Quickstart
Developer Quickstart
Fetching Market Data
Placing Your First Order
Glossary
API Rate Limits
Endpoints
Market Makers
Market Maker Introduction
Setup
Trading
Liquidity Rewards
Maker Rebates Program
Data Feeds
Inventory Management
Polymarket Builders Program
Builder Program Introduction
Builder Tiers
Builder Profile & Keys
Order Attribution
Relayer Client
Examples
Central Limit Order Book
CLOB Introduction
Status
Quickstart
Authentication
Geographic Restrictions

Client
Methods Overview
Public Methods
L1 Methods
L2 Methods
Builder Methods

REST API

Orderbook
GET
Get order book summary
POST
Get multiple order books summaries by request

Pricing
GET
Get market price
GET
Get multiple market prices
POST
Get multiple market prices by request
GET
Get midpoint price
GET
Get price history for a traded token

Spreads
POST
Get bid-ask spreads

Historical Timeseries Data
GET
Historical Timeseries Data

Order Management
Orders Overview
Place Single Order
Place Multiple Orders (Batching)
Get Order
Get Active Orders
Check Order Reward Scoring
Cancel Orders(s)
Onchain Order Info

Trades
Trades Overview
Get Trades
Websocket
WSS Overview
WSS Quickstart
WSS Authentication
User Channel
Market Channel

Sports Websocket
Overview
Message Format
Quickstart
Real Time Data Stream
RTDS Overview
RTDS Crypto Prices
RTDS Comments
Gamma Structure
Overview
Gamma Structure
Fetching Markets
Gamma Endpoints

Gamma Status
GET
Gamma API Health check

Sports
GET
List teams
GET
Get sports metadata information
GET
Get valid sports market types

Tags
GET
List tags
GET
Get tag by id
GET
Get tag by slug
GET
Get related tags (relationships) by tag id
GET
Get related tags (relationships) by tag slug
GET
Get tags related to a tag id
GET
Get tags related to a tag slug

Events
GET
List events
GET
Get event by id
GET
Get event tags
GET
Get event by slug

Markets

Series

Comments

Profiles

Search
Data-API

Data API Status

Core

Misc

Builders
Bridge & Swap
Overview

Bridge
Subgraph
Overview
Resolution
Resolution
Conditional Token Frameworks
Overview
Splitting USDC
Merging Tokens
Reedeeming Tokens
Deployment and Additional Information
Proxy Wallets
Proxy wallet
Negative Risk
Overview
Get event by id

curl --request GET \
  --url https://gamma-api.polymarket.com/events/{id}

200
{
  "id": "<string>",
  "ticker": "<string>",
  "slug": "<string>",
  "title": "<string>",
  "subtitle": "<string>",
  "description": "<string>",
  "resolutionSource": "<string>",
  "startDate": "2023-11-07T05:31:56Z",
  "creationDate": "2023-11-07T05:31:56Z",
  "endDate": "2023-11-07T05:31:56Z",
  "image": "<string>",
  "icon": "<string>",
  "active": true,
  "closed": true,
  "archived": true,
  "new": true,
  "featured": true,
  "restricted": true,
  "liquidity": 123,
  "volume": 123,
  "openInterest": 123,
  "sortBy": "<string>",
  "category": "<string>",
  "subcategory": "<string>",
  "isTemplate": true,
  "templateVariables": "<string>",
  "published_at": "<string>",
  "createdBy": "<string>",
  "updatedBy": "<string>",
  "createdAt": "2023-11-07T05:31:56Z",
  "updatedAt": "2023-11-07T05:31:56Z",
  "commentsEnabled": true,
  "competitive": 123,
  "volume24hr": 123,
  "volume1wk": 123,
  "volume1mo": 123,
  "volume1yr": 123,
  "featuredImage": "<string>",
  "disqusThread": "<string>",
  "parentEvent": "<string>",
  "enableOrderBook": true,
  "liquidityAmm": 123,
  "liquidityClob": 123,
  "negRisk": true,
  "negRiskMarketID": "<string>",
  "negRiskFeeBips": 123,
  "commentCount": 123,
  "imageOptimized": {
    "id": "<string>",
    "imageUrlSource": "<string>",
    "imageUrlOptimized": "<string>",
    "imageSizeKbSource": 123,
    "imageSizeKbOptimized": 123,
    "imageOptimizedComplete": true,
    "imageOptimizedLastUpdated": "<string>",
    "relID": 123,
    "field": "<string>",
    "relname": "<string>"
  },
  "iconOptimized": {
    "id": "<string>",
    "imageUrlSource": "<string>",
    "imageUrlOptimized": "<string>",
    "imageSizeKbSource": 123,
    "imageSizeKbOptimized": 123,
    "imageOptimizedComplete": true,
    "imageOptimizedLastUpdated": "<string>",
    "relID": 123,
    "field": "<string>",
    "relname": "<string>"
  },
  "featuredImageOptimized": {
    "id": "<string>",
    "imageUrlSource": "<string>",
    "imageUrlOptimized": "<string>",
    "imageSizeKbSource": 123,
    "imageSizeKbOptimized": 123,
    "imageOptimizedComplete": true,
    "imageOptimizedLastUpdated": "<string>",
    "relID": 123,
    "field": "<string>",
    "relname": "<string>"
  },
  "subEvents": [
    "<string>"
  ],
  "markets": [
    {
      "id": "<string>",
      "question": "<string>",
      "conditionId": "<string>",
      "slug": "<string>",
      "twitterCardImage": "<string>",
      "resolutionSource": "<string>",
      "endDate": "2023-11-07T05:31:56Z",
      "category": "<string>",
      "ammType": "<string>",
      "liquidity": "<string>",
      "sponsorName": "<string>",
      "sponsorImage": "<string>",
      "startDate": "2023-11-07T05:31:56Z",
      "xAxisValue": "<string>",
      "yAxisValue": "<string>",
      "denominationToken": "<string>",
      "fee": "<string>",
      "image": "<string>",
      "icon": "<string>",
      "lowerBound": "<string>",
      "upperBound": "<string>",
      "description": "<string>",
      "outcomes": "<string>",
      "outcomePrices": "<string>",
      "volume": "<string>",
      "active": true,
      "marketType": "<string>",
      "formatType": "<string>",
      "lowerBoundDate": "<string>",
      "upperBoundDate": "<string>",
      "closed": true,
      "marketMakerAddress": "<string>",
      "createdBy": 123,
      "updatedBy": 123,
      "createdAt": "2023-11-07T05:31:56Z",
      "updatedAt": "2023-11-07T05:31:56Z",
      "closedTime": "<string>",
      "wideFormat": true,
      "new": true,
      "mailchimpTag": "<string>",
      "featured": true,
      "archived": true,
      "resolvedBy": "<string>",
      "restricted": true,
      "marketGroup": 123,
      "groupItemTitle": "<string>",
      "groupItemThreshold": "<string>",
      "questionID": "<string>",
      "umaEndDate": "<string>",
      "enableOrderBook": true,
      "orderPriceMinTickSize": 123,
      "orderMinSize": 123,
      "umaResolutionStatus": "<string>",
      "curationOrder": 123,
      "volumeNum": 123,
      "liquidityNum": 123,
      "endDateIso": "<string>",
      "startDateIso": "<string>",
      "umaEndDateIso": "<string>",
      "hasReviewedDates": true,
      "readyForCron": true,
      "commentsEnabled": true,
      "volume24hr": 123,
      "volume1wk": 123,
      "volume1mo": 123,
      "volume1yr": 123,
      "gameStartTime": "<string>",
      "secondsDelay": 123,
      "clobTokenIds": "<string>",
      "disqusThread": "<string>",
      "shortOutcomes": "<string>",
      "teamAID": "<string>",
      "teamBID": "<string>",
      "umaBond": "<string>",
      "umaReward": "<string>",
      "fpmmLive": true,
      "volume24hrAmm": 123,
      "volume1wkAmm": 123,
      "volume1moAmm": 123,
      "volume1yrAmm": 123,
      "volume24hrClob": 123,
      "volume1wkClob": 123,
      "volume1moClob": 123,
      "volume1yrClob": 123,
      "volumeAmm": 123,
      "volumeClob": 123,
      "liquidityAmm": 123,
      "liquidityClob": 123,
      "makerBaseFee": 123,
      "takerBaseFee": 123,
      "customLiveness": 123,
      "acceptingOrders": true,
      "notificationsEnabled": true,
      "score": 123,
      "imageOptimized": {
        "id": "<string>",
        "imageUrlSource": "<string>",
        "imageUrlOptimized": "<string>",
        "imageSizeKbSource": 123,
        "imageSizeKbOptimized": 123,
        "imageOptimizedComplete": true,
        "imageOptimizedLastUpdated": "<string>",
        "relID": 123,
        "field": "<string>",
        "relname": "<string>"
      },
      "iconOptimized": {
        "id": "<string>",
        "imageUrlSource": "<string>",
        "imageUrlOptimized": "<string>",
        "imageSizeKbSource": 123,
        "imageSizeKbOptimized": 123,
        "imageOptimizedComplete": true,
        "imageOptimizedLastUpdated": "<string>",
        "relID": 123,
        "field": "<string>",
        "relname": "<string>"
      },
      "events": "<array>",
      "categories": [
        {
          "id": "<string>",
          "label": "<string>",
          "parentCategory": "<string>",
          "slug": "<string>",
          "publishedAt": "<string>",
          "createdBy": "<string>",
          "updatedBy": "<string>",
          "createdAt": "2023-11-07T05:31:56Z",
          "updatedAt": "2023-11-07T05:31:56Z"
        }
      ],
      "tags": [
        {
          "id": "<string>",
          "label": "<string>",
          "slug": "<string>",
          "forceShow": true,
          "publishedAt": "<string>",
          "createdBy": 123,
          "updatedBy": 123,
          "createdAt": "2023-11-07T05:31:56Z",
          "updatedAt": "2023-11-07T05:31:56Z",
          "forceHide": true,
          "isCarousel": true
        }
      ],
      "creator": "<string>",
      "ready": true,
      "funded": true,
      "pastSlugs": "<string>",
      "readyTimestamp": "2023-11-07T05:31:56Z",
      "fundedTimestamp": "2023-11-07T05:31:56Z",
      "acceptingOrdersTimestamp": "2023-11-07T05:31:56Z",
      "competitive": 123,
      "rewardsMinSize": 123,
      "rewardsMaxSpread": 123,
      "spread": 123,
      "automaticallyResolved": true,
      "oneDayPriceChange": 123,
      "oneHourPriceChange": 123,
      "oneWeekPriceChange": 123,
      "oneMonthPriceChange": 123,
      "oneYearPriceChange": 123,
      "lastTradePrice": 123,
      "bestBid": 123,
      "bestAsk": 123,
      "automaticallyActive": true,
      "clearBookOnStart": true,
      "chartColor": "<string>",
      "seriesColor": "<string>",
      "showGmpSeries": true,
      "showGmpOutcome": true,
      "manualActivation": true,
      "negRiskOther": true,
      "gameId": "<string>",
      "groupItemRange": "<string>",
      "sportsMarketType": "<string>",
      "line": 123,
      "umaResolutionStatuses": "<string>",
      "pendingDeployment": true,
      "deploying": true,
      "deployingTimestamp": "2023-11-07T05:31:56Z",
      "scheduledDeploymentTimestamp": "2023-11-07T05:31:56Z",
      "rfqEnabled": true,
      "eventStartTime": "2023-11-07T05:31:56Z"
    }
  ],
  "series": [
    {
      "id": "<string>",
      "ticker": "<string>",
      "slug": "<string>",
      "title": "<string>",
      "subtitle": "<string>",
      "seriesType": "<string>",
      "recurrence": "<string>",
      "description": "<string>",
      "image": "<string>",
      "icon": "<string>",
      "layout": "<string>",
      "active": true,
      "closed": true,
      "archived": true,
      "new": true,
      "featured": true,
      "restricted": true,
      "isTemplate": true,
      "templateVariables": true,
      "publishedAt": "<string>",
      "createdBy": "<string>",
      "updatedBy": "<string>",
      "createdAt": "2023-11-07T05:31:56Z",
      "updatedAt": "2023-11-07T05:31:56Z",
      "commentsEnabled": true,
      "competitive": "<string>",
      "volume24hr": 123,
      "volume": 123,
      "liquidity": 123,
      "startDate": "2023-11-07T05:31:56Z",
      "pythTokenID": "<string>",
      "cgAssetName": "<string>",
      "score": 123,
      "events": "<array>",
      "collections": [
        {
          "id": "<string>",
          "ticker": "<string>",
          "slug": "<string>",
          "title": "<string>",
          "subtitle": "<string>",
          "collectionType": "<string>",
          "description": "<string>",
          "tags": "<string>",
          "image": "<string>",
          "icon": "<string>",
          "headerImage": "<string>",
          "layout": "<string>",
          "active": true,
          "closed": true,
          "archived": true,
          "new": true,
          "featured": true,
          "restricted": true,
          "isTemplate": true,
          "templateVariables": "<string>",
          "publishedAt": "<string>",
          "createdBy": "<string>",
          "updatedBy": "<string>",
          "createdAt": "2023-11-07T05:31:56Z",
          "updatedAt": "2023-11-07T05:31:56Z",
          "commentsEnabled": true,
          "imageOptimized": {
            "id": "<string>",
            "imageUrlSource": "<string>",
            "imageUrlOptimized": "<string>",
            "imageSizeKbSource": 123,
            "imageSizeKbOptimized": 123,
            "imageOptimizedComplete": true,
            "imageOptimizedLastUpdated": "<string>",
            "relID": 123,
            "field": "<string>",
            "relname": "<string>"
          },
          "iconOptimized": {
            "id": "<string>",
            "imageUrlSource": "<string>",
            "imageUrlOptimized": "<string>",
            "imageSizeKbSource": 123,
            "imageSizeKbOptimized": 123,
            "imageOptimizedComplete": true,
            "imageOptimizedLastUpdated": "<string>",
            "relID": 123,
            "field": "<string>",
            "relname": "<string>"
          },
          "headerImageOptimized": {
            "id": "<string>",
            "imageUrlSource": "<string>",
            "imageUrlOptimized": "<string>",
            "imageSizeKbSource": 123,
            "imageSizeKbOptimized": 123,
            "imageOptimizedComplete": true,
            "imageOptimizedLastUpdated": "<string>",
            "relID": 123,
            "field": "<string>",
            "relname": "<string>"
          }
        }
      ],
      "categories": [
        {
          "id": "<string>",
          "label": "<string>",
          "parentCategory": "<string>",
          "slug": "<string>",
          "publishedAt": "<string>",
          "createdBy": "<string>",
          "updatedBy": "<string>",
          "createdAt": "2023-11-07T05:31:56Z",
          "updatedAt": "2023-11-07T05:31:56Z"
        }
      ],
      "tags": [
        {
          "id": "<string>",
          "label": "<string>",
          "slug": "<string>",
          "forceShow": true,
          "publishedAt": "<string>",
          "createdBy": 123,
          "updatedBy": 123,
          "createdAt": "2023-11-07T05:31:56Z",
          "updatedAt": "2023-11-07T05:31:56Z",
          "forceHide": true,
          "isCarousel": true
        }
      ],
      "commentCount": 123,
      "chats": [
        {
          "id": "<string>",
          "channelId": "<string>",
          "channelName": "<string>",
          "channelImage": "<string>",
          "live": true,
          "startTime": "2023-11-07T05:31:56Z",
          "endTime": "2023-11-07T05:31:56Z"
        }
      ]
    }
  ],
  "categories": [
    {
      "id": "<string>",
      "label": "<string>",
      "parentCategory": "<string>",
      "slug": "<string>",
      "publishedAt": "<string>",
      "createdBy": "<string>",
      "updatedBy": "<string>",
      "createdAt": "2023-11-07T05:31:56Z",
      "updatedAt": "2023-11-07T05:31:56Z"
    }
  ],
  "collections": [
    {
      "id": "<string>",
      "ticker": "<string>",
      "slug": "<string>",
      "title": "<string>",
      "subtitle": "<string>",
      "collectionType": "<string>",
      "description": "<string>",
      "tags": "<string>",
      "image": "<string>",
      "icon": "<string>",
      "headerImage": "<string>",
      "layout": "<string>",
      "active": true,
      "closed": true,
      "archived": true,
      "new": true,
      "featured": true,
      "restricted": true,
      "isTemplate": true,
      "templateVariables": "<string>",
      "publishedAt": "<string>",
      "createdBy": "<string>",
      "updatedBy": "<string>",
      "createdAt": "2023-11-07T05:31:56Z",
      "updatedAt": "2023-11-07T05:31:56Z",
      "commentsEnabled": true,
      "imageOptimized": {
        "id": "<string>",
        "imageUrlSource": "<string>",
        "imageUrlOptimized": "<string>",
        "imageSizeKbSource": 123,
        "imageSizeKbOptimized": 123,
        "imageOptimizedComplete": true,
        "imageOptimizedLastUpdated": "<string>",
        "relID": 123,
        "field": "<string>",
        "relname": "<string>"
      },
      "iconOptimized": {
        "id": "<string>",
        "imageUrlSource": "<string>",
        "imageUrlOptimized": "<string>",
        "imageSizeKbSource": 123,
        "imageSizeKbOptimized": 123,
        "imageOptimizedComplete": true,
        "imageOptimizedLastUpdated": "<string>",
        "relID": 123,
        "field": "<string>",
        "relname": "<string>"
      },
      "headerImageOptimized": {
        "id": "<string>",
        "imageUrlSource": "<string>",
        "imageUrlOptimized": "<string>",
        "imageSizeKbSource": 123,
        "imageSizeKbOptimized": 123,
        "imageOptimizedComplete": true,
        "imageOptimizedLastUpdated": "<string>",
        "relID": 123,
        "field": "<string>",
        "relname": "<string>"
      }
    }
  ],
  "tags": [
    {
      "id": "<string>",
      "label": "<string>",
      "slug": "<string>",
      "forceShow": true,
      "publishedAt": "<string>",
      "createdBy": 123,
      "updatedBy": 123,
      "createdAt": "2023-11-07T05:31:56Z",
      "updatedAt": "2023-11-07T05:31:56Z",
      "forceHide": true,
      "isCarousel": true
    }
  ],
  "cyom": true,
  "closedTime": "2023-11-07T05:31:56Z",
  "showAllOutcomes": true,
  "showMarketImages": true,
  "automaticallyResolved": true,
  "enableNegRisk": true,
  "automaticallyActive": true,
  "eventDate": "<string>",
  "startTime": "2023-11-07T05:31:56Z",
  "eventWeek": 123,
  "seriesSlug": "<string>",
  "score": "<string>",
  "elapsed": "<string>",
  "period": "<string>",
  "live": true,
  "ended": true,
  "finishedTimestamp": "2023-11-07T05:31:56Z",
  "gmpChartMode": "<string>",
  "eventCreators": [
    {
      "id": "<string>",
      "creatorName": "<string>",
      "creatorHandle": "<string>",
      "creatorUrl": "<string>",
      "creatorImage": "<string>",
      "createdAt": "2023-11-07T05:31:56Z",
      "updatedAt": "2023-11-07T05:31:56Z"
    }
  ],
  "tweetCount": 123,
  "chats": [
    {
      "id": "<string>",
      "channelId": "<string>",
      "channelName": "<string>",
      "channelImage": "<string>",
      "live": true,
      "startTime": "2023-11-07T05:31:56Z",
      "endTime": "2023-11-07T05:31:56Z"
    }
  ],
  "featuredOrder": 123,
  "estimateValue": true,
  "cantEstimate": true,
  "estimatedValue": "<string>",
  "templates": [
    {
      "id": "<string>",
      "eventTitle": "<string>",
      "eventSlug": "<string>",
      "eventImage": "<string>",
      "marketTitle": "<string>",
      "description": "<string>",
      "resolutionSource": "<string>",
      "negRisk": true,
      "sortBy": "<string>",
      "showMarketImages": true,
      "seriesSlug": "<string>",
      "outcomes": "<string>"
    }
  ],
  "spreadsMainLine": 123,
  "totalsMainLine": 123,
  "carouselMap": "<string>",
  "pendingDeployment": true,
  "deploying": true,
  "deployingTimestamp": "2023-11-07T05:31:56Z",
  "scheduledDeploymentTimestamp": "2023-11-07T05:31:56Z",
  "gameStatus": "<string>"
}
Events
Get event by id
GET
/
events
/
{id}

Try it
Path Parameters
​
id
integerrequired
Query Parameters
​
include_chat
boolean
​
include_template
boolean
Response

200

application/json
Event

​
id
string
​
ticker
string | null
​
slug
string | null
​
title
string | null
​
subtitle
string | null
​
description
string | null
​
resolutionSource
string | null
​
startDate
string<date-time> | null
​
creationDate
string<date-time> | null
​
endDate
string<date-time> | null
​
image
string | null
​
icon
string | null
​
active
boolean | null
​
closed
boolean | null
​
archived
boolean | null
​
new
boolean | null
​
featured
boolean | null
​
restricted
boolean | null
​
liquidity
number | null
​
volume
number | null
​
openInterest
number | null
​
sortBy
string | null
​
category
string | null
​
subcategory
string | null
​
isTemplate
boolean | null
​
templateVariables
string | null
​
published_at
string | null
​
createdBy
string | null
​
updatedBy
string | null
​
createdAt
string<date-time> | null
​
updatedAt
string<date-time> | null
​
commentsEnabled
boolean | null
​
competitive
number | null
​
volume24hr
number | null
​
volume1wk
number | null
​
volume1mo
number | null
​
volume1yr
number | null
​
featuredImage
string | null
​
disqusThread
string | null
​
parentEvent
string | null
​
enableOrderBook
boolean | null
​
liquidityAmm
number | null
​
liquidityClob
number | null
​
negRisk
boolean | null
​
negRiskMarketID
string | null
​
negRiskFeeBips
integer | null
​
commentCount
integer | null
​
imageOptimized
object
Show child attributes

​
iconOptimized
object
Show child attributes

​
featuredImageOptimized
object
Show child attributes

​
subEvents
string[] | null
​
markets
object[]
Show child attributes

​
series
object[]
Show child attributes

​
categories
object[]
Show child attributes

​
collections
object[]
Show child attributes

​
tags
object[]
Show child attributes

​
cyom
boolean | null
​
closedTime
string<date-time> | null
​
showAllOutcomes
boolean | null
​
showMarketImages
boolean | null
​
automaticallyResolved
boolean | null
​
enableNegRisk
boolean | null
​
automaticallyActive
boolean | null
​
eventDate
string | null
​
startTime
string<date-time> | null
​
eventWeek
integer | null
​
seriesSlug
string | null
​
score
string | null
​
elapsed
string | null
​
period
string | null
​
live
boolean | null
​
ended
boolean | null
​
finishedTimestamp
string<date-time> | null
​
gmpChartMode
string | null
​
eventCreators
object[]
Show child attributes

​
tweetCount
integer | null
​
chats
object[]
Show child attributes

​
featuredOrder
integer | null
​
estimateValue
boolean | null
​
cantEstimate
boolean | null
​
estimatedValue
string | null
​
templates
object[]
Show child attributes

​
spreadsMainLine
number | null
​
totalsMainLine
number | null
​
carouselMap
string | null
​
pendingDeployment
boolean | null
​
deploying
boolean | null
​
deployingTimestamp
string<date-time> | null
​
scheduledDeploymentTimestamp
string<date-time> | null
​
gameStatus
string | null
List events
Get event tags
Ask a question...

github
Powered by
Get event by id - Polymarket Documentation

Skip to main content
Polymarket Documentation home pagedark logo

Search...
Ctrl K

Ask AI
Main Site

User Guide
For Developers
Changelog
Polymarket
Discord Community
Twitter
Developer Quickstart
Developer Quickstart
Fetching Market Data
Placing Your First Order
Glossary
API Rate Limits
Endpoints
Market Makers
Market Maker Introduction
Setup
Trading
Liquidity Rewards
Maker Rebates Program
Data Feeds
Inventory Management
Polymarket Builders Program
Builder Program Introduction
Builder Tiers
Builder Profile & Keys
Order Attribution
Relayer Client
Examples
Central Limit Order Book
CLOB Introduction
Status
Quickstart
Authentication
Geographic Restrictions

Client
Methods Overview
Public Methods
L1 Methods
L2 Methods
Builder Methods

REST API

Orderbook
GET
Get order book summary
POST
Get multiple order books summaries by request

Pricing
GET
Get market price
GET
Get multiple market prices
POST
Get multiple market prices by request
GET
Get midpoint price
GET
Get price history for a traded token

Spreads
POST
Get bid-ask spreads

Historical Timeseries Data
GET
Historical Timeseries Data

Order Management
Orders Overview
Place Single Order
Place Multiple Orders (Batching)
Get Order
Get Active Orders
Check Order Reward Scoring
Cancel Orders(s)
Onchain Order Info

Trades
Trades Overview
Get Trades
Websocket
WSS Overview
WSS Quickstart
WSS Authentication
User Channel
Market Channel

Sports Websocket
Overview
Message Format
Quickstart
Real Time Data Stream
RTDS Overview
RTDS Crypto Prices
RTDS Comments
Gamma Structure
Overview
Gamma Structure
Fetching Markets
Gamma Endpoints

Gamma Status
GET
Gamma API Health check

Sports
GET
List teams
GET
Get sports metadata information
GET
Get valid sports market types

Tags
GET
List tags
GET
Get tag by id
GET
Get tag by slug
GET
Get related tags (relationships) by tag id
GET
Get related tags (relationships) by tag slug
GET
Get tags related to a tag id
GET
Get tags related to a tag slug

Events
GET
List events
GET
Get event by id
GET
Get event tags
GET
Get event by slug

Markets

Series

Comments

Profiles

Search
Data-API

Data API Status

Core

Misc

Builders
Bridge & Swap
Overview

Bridge
Subgraph
Overview
Resolution
Resolution
Conditional Token Frameworks
Overview
Splitting USDC
Merging Tokens
Reedeeming Tokens
Deployment and Additional Information
Proxy Wallets
Proxy wallet
Negative Risk
Overview
Get event tags

curl --request GET \
  --url https://gamma-api.polymarket.com/events/{id}/tags

200
[
  {
    "id": "<string>",
    "label": "<string>",
    "slug": "<string>",
    "forceShow": true,
    "publishedAt": "<string>",
    "createdBy": 123,
    "updatedBy": 123,
    "createdAt": "2023-11-07T05:31:56Z",
    "updatedAt": "2023-11-07T05:31:56Z",
    "forceHide": true,
    "isCarousel": true
  }
]
Events
Get event tags
GET
/
events
/
{id}
/
tags

Try it
Path Parameters
​
id
integerrequired
Response

200

application/json
Tags attached to the event

​
id
string
​
label
string | null
​
slug
string | null
​
forceShow
boolean | null
​
publishedAt
string | null
​
createdBy
integer | null
​
updatedBy
integer | null
​
createdAt
string<date-time> | null
​
updatedAt
string<date-time> | null
​
forceHide
boolean | null
​
isCarousel
boolean | null
Get event by id
Get event by slug
Ask a question...

github
Powered by
Get event tags - Polymarket Documentation

Skip to main content
Polymarket Documentation home pagedark logo

Search...
Ctrl K

Ask AI
Main Site

User Guide
For Developers
Changelog
Polymarket
Discord Community
Twitter
Developer Quickstart
Developer Quickstart
Fetching Market Data
Placing Your First Order
Glossary
API Rate Limits
Endpoints
Market Makers
Market Maker Introduction
Setup
Trading
Liquidity Rewards
Maker Rebates Program
Data Feeds
Inventory Management
Polymarket Builders Program
Builder Program Introduction
Builder Tiers
Builder Profile & Keys
Order Attribution
Relayer Client
Examples
Central Limit Order Book
CLOB Introduction
Status
Quickstart
Authentication
Geographic Restrictions

Client
Methods Overview
Public Methods
L1 Methods
L2 Methods
Builder Methods

REST API

Orderbook
GET
Get order book summary
POST
Get multiple order books summaries by request

Pricing
GET
Get market price
GET
Get multiple market prices
POST
Get multiple market prices by request
GET
Get midpoint price
GET
Get price history for a traded token

Spreads
POST
Get bid-ask spreads

Historical Timeseries Data
GET
Historical Timeseries Data

Order Management
Orders Overview
Place Single Order
Place Multiple Orders (Batching)
Get Order
Get Active Orders
Check Order Reward Scoring
Cancel Orders(s)
Onchain Order Info

Trades
Trades Overview
Get Trades
Websocket
WSS Overview
WSS Quickstart
WSS Authentication
User Channel
Market Channel

Sports Websocket
Overview
Message Format
Quickstart
Real Time Data Stream
RTDS Overview
RTDS Crypto Prices
RTDS Comments
Gamma Structure
Overview
Gamma Structure
Fetching Markets
Gamma Endpoints

Gamma Status
GET
Gamma API Health check

Sports
GET
List teams
GET
Get sports metadata information
GET
Get valid sports market types

Tags
GET
List tags
GET
Get tag by id
GET
Get tag by slug
GET
Get related tags (relationships) by tag id
GET
Get related tags (relationships) by tag slug
GET
Get tags related to a tag id
GET
Get tags related to a tag slug

Events
GET
List events
GET
Get event by id
GET
Get event tags
GET
Get event by slug

Markets

Series

Comments

Profiles

Search
Data-API

Data API Status

Core

Misc

Builders
Bridge & Swap
Overview

Bridge
Subgraph
Overview
Resolution
Resolution
Conditional Token Frameworks
Overview
Splitting USDC
Merging Tokens
Reedeeming Tokens
Deployment and Additional Information
Proxy Wallets
Proxy wallet
Negative Risk
Overview
Get event by slug

curl --request GET \
  --url https://gamma-api.polymarket.com/events/slug/{slug}

200
{
  "id": "<string>",
  "ticker": "<string>",
  "slug": "<string>",
  "title": "<string>",
  "subtitle": "<string>",
  "description": "<string>",
  "resolutionSource": "<string>",
  "startDate": "2023-11-07T05:31:56Z",
  "creationDate": "2023-11-07T05:31:56Z",
  "endDate": "2023-11-07T05:31:56Z",
  "image": "<string>",
  "icon": "<string>",
  "active": true,
  "closed": true,
  "archived": true,
  "new": true,
  "featured": true,
  "restricted": true,
  "liquidity": 123,
  "volume": 123,
  "openInterest": 123,
  "sortBy": "<string>",
  "category": "<string>",
  "subcategory": "<string>",
  "isTemplate": true,
  "templateVariables": "<string>",
  "published_at": "<string>",
  "createdBy": "<string>",
  "updatedBy": "<string>",
  "createdAt": "2023-11-07T05:31:56Z",
  "updatedAt": "2023-11-07T05:31:56Z",
  "commentsEnabled": true,
  "competitive": 123,
  "volume24hr": 123,
  "volume1wk": 123,
  "volume1mo": 123,
  "volume1yr": 123,
  "featuredImage": "<string>",
  "disqusThread": "<string>",
  "parentEvent": "<string>",
  "enableOrderBook": true,
  "liquidityAmm": 123,
  "liquidityClob": 123,
  "negRisk": true,
  "negRiskMarketID": "<string>",
  "negRiskFeeBips": 123,
  "commentCount": 123,
  "imageOptimized": {
    "id": "<string>",
    "imageUrlSource": "<string>",
    "imageUrlOptimized": "<string>",
    "imageSizeKbSource": 123,
    "imageSizeKbOptimized": 123,
    "imageOptimizedComplete": true,
    "imageOptimizedLastUpdated": "<string>",
    "relID": 123,
    "field": "<string>",
    "relname": "<string>"
  },
  "iconOptimized": {
    "id": "<string>",
    "imageUrlSource": "<string>",
    "imageUrlOptimized": "<string>",
    "imageSizeKbSource": 123,
    "imageSizeKbOptimized": 123,
    "imageOptimizedComplete": true,
    "imageOptimizedLastUpdated": "<string>",
    "relID": 123,
    "field": "<string>",
    "relname": "<string>"
  },
  "featuredImageOptimized": {
    "id": "<string>",
    "imageUrlSource": "<string>",
    "imageUrlOptimized": "<string>",
    "imageSizeKbSource": 123,
    "imageSizeKbOptimized": 123,
    "imageOptimizedComplete": true,
    "imageOptimizedLastUpdated": "<string>",
    "relID": 123,
    "field": "<string>",
    "relname": "<string>"
  },
  "subEvents": [
    "<string>"
  ],
  "markets": [
    {
      "id": "<string>",
      "question": "<string>",
      "conditionId": "<string>",
      "slug": "<string>",
      "twitterCardImage": "<string>",
      "resolutionSource": "<string>",
      "endDate": "2023-11-07T05:31:56Z",
      "category": "<string>",
      "ammType": "<string>",
      "liquidity": "<string>",
      "sponsorName": "<string>",
      "sponsorImage": "<string>",
      "startDate": "2023-11-07T05:31:56Z",
      "xAxisValue": "<string>",
      "yAxisValue": "<string>",
      "denominationToken": "<string>",
      "fee": "<string>",
      "image": "<string>",
      "icon": "<string>",
      "lowerBound": "<string>",
      "upperBound": "<string>",
      "description": "<string>",
      "outcomes": "<string>",
      "outcomePrices": "<string>",
      "volume": "<string>",
      "active": true,
      "marketType": "<string>",
      "formatType": "<string>",
      "lowerBoundDate": "<string>",
      "upperBoundDate": "<string>",
      "closed": true,
      "marketMakerAddress": "<string>",
      "createdBy": 123,
      "updatedBy": 123,
      "createdAt": "2023-11-07T05:31:56Z",
      "updatedAt": "2023-11-07T05:31:56Z",
      "closedTime": "<string>",
      "wideFormat": true,
      "new": true,
      "mailchimpTag": "<string>",
      "featured": true,
      "archived": true,
      "resolvedBy": "<string>",
      "restricted": true,
      "marketGroup": 123,
      "groupItemTitle": "<string>",
      "groupItemThreshold": "<string>",
      "questionID": "<string>",
      "umaEndDate": "<string>",
      "enableOrderBook": true,
      "orderPriceMinTickSize": 123,
      "orderMinSize": 123,
      "umaResolutionStatus": "<string>",
      "curationOrder": 123,
      "volumeNum": 123,
      "liquidityNum": 123,
      "endDateIso": "<string>",
      "startDateIso": "<string>",
      "umaEndDateIso": "<string>",
      "hasReviewedDates": true,
      "readyForCron": true,
      "commentsEnabled": true,
      "volume24hr": 123,
      "volume1wk": 123,
      "volume1mo": 123,
      "volume1yr": 123,
      "gameStartTime": "<string>",
      "secondsDelay": 123,
      "clobTokenIds": "<string>",
      "disqusThread": "<string>",
      "shortOutcomes": "<string>",
      "teamAID": "<string>",
      "teamBID": "<string>",
      "umaBond": "<string>",
      "umaReward": "<string>",
      "fpmmLive": true,
      "volume24hrAmm": 123,
      "volume1wkAmm": 123,
      "volume1moAmm": 123,
      "volume1yrAmm": 123,
      "volume24hrClob": 123,
      "volume1wkClob": 123,
      "volume1moClob": 123,
      "volume1yrClob": 123,
      "volumeAmm": 123,
      "volumeClob": 123,
      "liquidityAmm": 123,
      "liquidityClob": 123,
      "makerBaseFee": 123,
      "takerBaseFee": 123,
      "customLiveness": 123,
      "acceptingOrders": true,
      "notificationsEnabled": true,
      "score": 123,
      "imageOptimized": {
        "id": "<string>",
        "imageUrlSource": "<string>",
        "imageUrlOptimized": "<string>",
        "imageSizeKbSource": 123,
        "imageSizeKbOptimized": 123,
        "imageOptimizedComplete": true,
        "imageOptimizedLastUpdated": "<string>",
        "relID": 123,
        "field": "<string>",
        "relname": "<string>"
      },
      "iconOptimized": {
        "id": "<string>",
        "imageUrlSource": "<string>",
        "imageUrlOptimized": "<string>",
        "imageSizeKbSource": 123,
        "imageSizeKbOptimized": 123,
        "imageOptimizedComplete": true,
        "imageOptimizedLastUpdated": "<string>",
        "relID": 123,
        "field": "<string>",
        "relname": "<string>"
      },
      "events": "<array>",
      "categories": [
        {
          "id": "<string>",
          "label": "<string>",
          "parentCategory": "<string>",
          "slug": "<string>",
          "publishedAt": "<string>",
          "createdBy": "<string>",
          "updatedBy": "<string>",
          "createdAt": "2023-11-07T05:31:56Z",
          "updatedAt": "2023-11-07T05:31:56Z"
        }
      ],
      "tags": [
        {
          "id": "<string>",
          "label": "<string>",
          "slug": "<string>",
          "forceShow": true,
          "publishedAt": "<string>",
          "createdBy": 123,
          "updatedBy": 123,
          "createdAt": "2023-11-07T05:31:56Z",
          "updatedAt": "2023-11-07T05:31:56Z",
          "forceHide": true,
          "isCarousel": true
        }
      ],
      "creator": "<string>",
      "ready": true,
      "funded": true,
      "pastSlugs": "<string>",
      "readyTimestamp": "2023-11-07T05:31:56Z",
      "fundedTimestamp": "2023-11-07T05:31:56Z",
      "acceptingOrdersTimestamp": "2023-11-07T05:31:56Z",
      "competitive": 123,
      "rewardsMinSize": 123,
      "rewardsMaxSpread": 123,
      "spread": 123,
      "automaticallyResolved": true,
      "oneDayPriceChange": 123,
      "oneHourPriceChange": 123,
      "oneWeekPriceChange": 123,
      "oneMonthPriceChange": 123,
      "oneYearPriceChange": 123,
      "lastTradePrice": 123,
      "bestBid": 123,
      "bestAsk": 123,
      "automaticallyActive": true,
      "clearBookOnStart": true,
      "chartColor": "<string>",
      "seriesColor": "<string>",
      "showGmpSeries": true,
      "showGmpOutcome": true,
      "manualActivation": true,
      "negRiskOther": true,
      "gameId": "<string>",
      "groupItemRange": "<string>",
      "sportsMarketType": "<string>",
      "line": 123,
      "umaResolutionStatuses": "<string>",
      "pendingDeployment": true,
      "deploying": true,
      "deployingTimestamp": "2023-11-07T05:31:56Z",
      "scheduledDeploymentTimestamp": "2023-11-07T05:31:56Z",
      "rfqEnabled": true,
      "eventStartTime": "2023-11-07T05:31:56Z"
    }
  ],
  "series": [
    {
      "id": "<string>",
      "ticker": "<string>",
      "slug": "<string>",
      "title": "<string>",
      "subtitle": "<string>",
      "seriesType": "<string>",
      "recurrence": "<string>",
      "description": "<string>",
      "image": "<string>",
      "icon": "<string>",
      "layout": "<string>",
      "active": true,
      "closed": true,
      "archived": true,
      "new": true,
      "featured": true,
      "restricted": true,
      "isTemplate": true,
      "templateVariables": true,
      "publishedAt": "<string>",
      "createdBy": "<string>",
      "updatedBy": "<string>",
      "createdAt": "2023-11-07T05:31:56Z",
      "updatedAt": "2023-11-07T05:31:56Z",
      "commentsEnabled": true,
      "competitive": "<string>",
      "volume24hr": 123,
      "volume": 123,
      "liquidity": 123,
      "startDate": "2023-11-07T05:31:56Z",
      "pythTokenID": "<string>",
      "cgAssetName": "<string>",
      "score": 123,
      "events": "<array>",
      "collections": [
        {
          "id": "<string>",
          "ticker": "<string>",
          "slug": "<string>",
          "title": "<string>",
          "subtitle": "<string>",
          "collectionType": "<string>",
          "description": "<string>",
          "tags": "<string>",
          "image": "<string>",
          "icon": "<string>",
          "headerImage": "<string>",
          "layout": "<string>",
          "active": true,
          "closed": true,
          "archived": true,
          "new": true,
          "featured": true,
          "restricted": true,
          "isTemplate": true,
          "templateVariables": "<string>",
          "publishedAt": "<string>",
          "createdBy": "<string>",
          "updatedBy": "<string>",
          "createdAt": "2023-11-07T05:31:56Z",
          "updatedAt": "2023-11-07T05:31:56Z",
          "commentsEnabled": true,
          "imageOptimized": {
            "id": "<string>",
            "imageUrlSource": "<string>",
            "imageUrlOptimized": "<string>",
            "imageSizeKbSource": 123,
            "imageSizeKbOptimized": 123,
            "imageOptimizedComplete": true,
            "imageOptimizedLastUpdated": "<string>",
            "relID": 123,
            "field": "<string>",
            "relname": "<string>"
          },
          "iconOptimized": {
            "id": "<string>",
            "imageUrlSource": "<string>",
            "imageUrlOptimized": "<string>",
            "imageSizeKbSource": 123,
            "imageSizeKbOptimized": 123,
            "imageOptimizedComplete": true,
            "imageOptimizedLastUpdated": "<string>",
            "relID": 123,
            "field": "<string>",
            "relname": "<string>"
          },
          "headerImageOptimized": {
            "id": "<string>",
            "imageUrlSource": "<string>",
            "imageUrlOptimized": "<string>",
            "imageSizeKbSource": 123,
            "imageSizeKbOptimized": 123,
            "imageOptimizedComplete": true,
            "imageOptimizedLastUpdated": "<string>",
            "relID": 123,
            "field": "<string>",
            "relname": "<string>"
          }
        }
      ],
      "categories": [
        {
          "id": "<string>",
          "label": "<string>",
          "parentCategory": "<string>",
          "slug": "<string>",
          "publishedAt": "<string>",
          "createdBy": "<string>",
          "updatedBy": "<string>",
          "createdAt": "2023-11-07T05:31:56Z",
          "updatedAt": "2023-11-07T05:31:56Z"
        }
      ],
      "tags": [
        {
          "id": "<string>",
          "label": "<string>",
          "slug": "<string>",
          "forceShow": true,
          "publishedAt": "<string>",
          "createdBy": 123,
          "updatedBy": 123,
          "createdAt": "2023-11-07T05:31:56Z",
          "updatedAt": "2023-11-07T05:31:56Z",
          "forceHide": true,
          "isCarousel": true
        }
      ],
      "commentCount": 123,
      "chats": [
        {
          "id": "<string>",
          "channelId": "<string>",
          "channelName": "<string>",
          "channelImage": "<string>",
          "live": true,
          "startTime": "2023-11-07T05:31:56Z",
          "endTime": "2023-11-07T05:31:56Z"
        }
      ]
    }
  ],
  "categories": [
    {
      "id": "<string>",
      "label": "<string>",
      "parentCategory": "<string>",
      "slug": "<string>",
      "publishedAt": "<string>",
      "createdBy": "<string>",
      "updatedBy": "<string>",
      "createdAt": "2023-11-07T05:31:56Z",
      "updatedAt": "2023-11-07T05:31:56Z"
    }
  ],
  "collections": [
    {
      "id": "<string>",
      "ticker": "<string>",
      "slug": "<string>",
      "title": "<string>",
      "subtitle": "<string>",
      "collectionType": "<string>",
      "description": "<string>",
      "tags": "<string>",
      "image": "<string>",
      "icon": "<string>",
      "headerImage": "<string>",
      "layout": "<string>",
      "active": true,
      "closed": true,
      "archived": true,
      "new": true,
      "featured": true,
      "restricted": true,
      "isTemplate": true,
      "templateVariables": "<string>",
      "publishedAt": "<string>",
      "createdBy": "<string>",
      "updatedBy": "<string>",
      "createdAt": "2023-11-07T05:31:56Z",
      "updatedAt": "2023-11-07T05:31:56Z",
      "commentsEnabled": true,
      "imageOptimized": {
        "id": "<string>",
        "imageUrlSource": "<string>",
        "imageUrlOptimized": "<string>",
        "imageSizeKbSource": 123,
        "imageSizeKbOptimized": 123,
        "imageOptimizedComplete": true,
        "imageOptimizedLastUpdated": "<string>",
        "relID": 123,
        "field": "<string>",
        "relname": "<string>"
      },
      "iconOptimized": {
        "id": "<string>",
        "imageUrlSource": "<string>",
        "imageUrlOptimized": "<string>",
        "imageSizeKbSource": 123,
        "imageSizeKbOptimized": 123,
        "imageOptimizedComplete": true,
        "imageOptimizedLastUpdated": "<string>",
        "relID": 123,
        "field": "<string>",
        "relname": "<string>"
      },
      "headerImageOptimized": {
        "id": "<string>",
        "imageUrlSource": "<string>",
        "imageUrlOptimized": "<string>",
        "imageSizeKbSource": 123,
        "imageSizeKbOptimized": 123,
        "imageOptimizedComplete": true,
        "imageOptimizedLastUpdated": "<string>",
        "relID": 123,
        "field": "<string>",
        "relname": "<string>"
      }
    }
  ],
  "tags": [
    {
      "id": "<string>",
      "label": "<string>",
      "slug": "<string>",
      "forceShow": true,
      "publishedAt": "<string>",
      "createdBy": 123,
      "updatedBy": 123,
      "createdAt": "2023-11-07T05:31:56Z",
      "updatedAt": "2023-11-07T05:31:56Z",
      "forceHide": true,
      "isCarousel": true
    }
  ],
  "cyom": true,
  "closedTime": "2023-11-07T05:31:56Z",
  "showAllOutcomes": true,
  "showMarketImages": true,
  "automaticallyResolved": true,
  "enableNegRisk": true,
  "automaticallyActive": true,
  "eventDate": "<string>",
  "startTime": "2023-11-07T05:31:56Z",
  "eventWeek": 123,
  "seriesSlug": "<string>",
  "score": "<string>",
  "elapsed": "<string>",
  "period": "<string>",
  "live": true,
  "ended": true,
  "finishedTimestamp": "2023-11-07T05:31:56Z",
  "gmpChartMode": "<string>",
  "eventCreators": [
    {
      "id": "<string>",
      "creatorName": "<string>",
      "creatorHandle": "<string>",
      "creatorUrl": "<string>",
      "creatorImage": "<string>",
      "createdAt": "2023-11-07T05:31:56Z",
      "updatedAt": "2023-11-07T05:31:56Z"
    }
  ],
  "tweetCount": 123,
  "chats": [
    {
      "id": "<string>",
      "channelId": "<string>",
      "channelName": "<string>",
      "channelImage": "<string>",
      "live": true,
      "startTime": "2023-11-07T05:31:56Z",
      "endTime": "2023-11-07T05:31:56Z"
    }
  ],
  "featuredOrder": 123,
  "estimateValue": true,
  "cantEstimate": true,
  "estimatedValue": "<string>",
  "templates": [
    {
      "id": "<string>",
      "eventTitle": "<string>",
      "eventSlug": "<string>",
      "eventImage": "<string>",
      "marketTitle": "<string>",
      "description": "<string>",
      "resolutionSource": "<string>",
      "negRisk": true,
      "sortBy": "<string>",
      "showMarketImages": true,
      "seriesSlug": "<string>",
      "outcomes": "<string>"
    }
  ],
  "spreadsMainLine": 123,
  "totalsMainLine": 123,
  "carouselMap": "<string>",
  "pendingDeployment": true,
  "deploying": true,
  "deployingTimestamp": "2023-11-07T05:31:56Z",
  "scheduledDeploymentTimestamp": "2023-11-07T05:31:56Z",
  "gameStatus": "<string>"
}
Events
Get event by slug
GET
/
events
/
slug
/
{slug}

Try it
Path Parameters
​
slug
stringrequired
Query Parameters
​
include_chat
boolean
​
include_template
boolean
Response

200

application/json
Event

​
id
string
​
ticker
string | null
​
slug
string | null
​
title
string | null
​
subtitle
string | null
​
description
string | null
​
resolutionSource
string | null
​
startDate
string<date-time> | null
​
creationDate
string<date-time> | null
​
endDate
string<date-time> | null
​
image
string | null
​
icon
string | null
​
active
boolean | null
​
closed
boolean | null
​
archived
boolean | null
​
new
boolean | null
​
featured
boolean | null
​
restricted
boolean | null
​
liquidity
number | null
​
volume
number | null
​
openInterest
number | null
​
sortBy
string | null
​
category
string | null
​
subcategory
string | null
​
isTemplate
boolean | null
​
templateVariables
string | null
​
published_at
string | null
​
createdBy
string | null
​
updatedBy
string | null
​
createdAt
string<date-time> | null
​
updatedAt
string<date-time> | null
​
commentsEnabled
boolean | null
​
competitive
number | null
​
volume24hr
number | null
​
volume1wk
number | null
​
volume1mo
number | null
​
volume1yr
number | null
​
featuredImage
string | null
​
disqusThread
string | null
​
parentEvent
string | null
​
enableOrderBook
boolean | null
​
liquidityAmm
number | null
​
liquidityClob
number | null
​
negRisk
boolean | null
​
negRiskMarketID
string | null
​
negRiskFeeBips
integer | null
​
commentCount
integer | null
​
imageOptimized
object
Show child attributes

​
iconOptimized
object
Show child attributes

​
featuredImageOptimized
object
Show child attributes

​
subEvents
string[] | null
​
markets
object[]
Show child attributes

​
series
object[]
Show child attributes

​
categories
object[]
Show child attributes

​
collections
object[]
Show child attributes

​
tags
object[]
Show child attributes

​
cyom
boolean | null
​
closedTime
string<date-time> | null
​
showAllOutcomes
boolean | null
​
showMarketImages
boolean | null
​
automaticallyResolved
boolean | null
​
enableNegRisk
boolean | null
​
automaticallyActive
boolean | null
​
eventDate
string | null
​
startTime
string<date-time> | null
​
eventWeek
integer | null
​
seriesSlug
string | null
​
score
string | null
​
elapsed
string | null
​
period
string | null
​
live
boolean | null
​
ended
boolean | null
​
finishedTimestamp
string<date-time> | null
​
gmpChartMode
string | null
​
eventCreators
object[]
Show child attributes

​
tweetCount
integer | null
​
chats
object[]
Show child attributes

​
featuredOrder
integer | null
​
estimateValue
boolean | null
​
cantEstimate
boolean | null
​
estimatedValue
string | null
​
templates
object[]
Show child attributes

​
spreadsMainLine
number | null
​
totalsMainLine
number | null
​
carouselMap
string | null
​
pendingDeployment
boolean | null
​
deploying
boolean | null
​
deployingTimestamp
string<date-time> | null
​
scheduledDeploymentTimestamp
string<date-time> | null
​
gameStatus
string | null
Get event tags
List markets
Ask a question...

github
Powered by
Get event by slug - Polymarket Documentation


Skip to main content
Polymarket Documentation home pagedark logo

Search...
Ctrl K

Ask AI
Main Site

User Guide
For Developers
Changelog
Polymarket
Discord Community
Twitter
Developer Quickstart
Developer Quickstart
Fetching Market Data
Placing Your First Order
Glossary
API Rate Limits
Endpoints
Market Makers
Market Maker Introduction
Setup
Trading
Liquidity Rewards
Maker Rebates Program
Data Feeds
Inventory Management
Polymarket Builders Program
Builder Program Introduction
Builder Tiers
Builder Profile & Keys
Order Attribution
Relayer Client
Examples
Central Limit Order Book
CLOB Introduction
Status
Quickstart
Authentication
Geographic Restrictions

Client
Methods Overview
Public Methods
L1 Methods
L2 Methods
Builder Methods

REST API

Orderbook
GET
Get order book summary
POST
Get multiple order books summaries by request

Pricing
GET
Get market price
GET
Get multiple market prices
POST
Get multiple market prices by request
GET
Get midpoint price
GET
Get price history for a traded token

Spreads
POST
Get bid-ask spreads

Historical Timeseries Data
GET
Historical Timeseries Data

Order Management
Orders Overview
Place Single Order
Place Multiple Orders (Batching)
Get Order
Get Active Orders
Check Order Reward Scoring
Cancel Orders(s)
Onchain Order Info

Trades
Trades Overview
Get Trades
Websocket
WSS Overview
WSS Quickstart
WSS Authentication
User Channel
Market Channel

Sports Websocket
Overview
Message Format
Quickstart
Real Time Data Stream
RTDS Overview
RTDS Crypto Prices
RTDS Comments
Gamma Structure
Overview
Gamma Structure
Fetching Markets
Gamma Endpoints

Gamma Status
GET
Gamma API Health check

Sports
GET
List teams
GET
Get sports metadata information
GET
Get valid sports market types

Tags
GET
List tags
GET
Get tag by id
GET
Get tag by slug
GET
Get related tags (relationships) by tag id
GET
Get related tags (relationships) by tag slug
GET
Get tags related to a tag id
GET
Get tags related to a tag slug

Events
GET
List events
GET
Get event by id
GET
Get event tags
GET
Get event by slug

Markets
GET
List markets
GET
Get market by id
GET
Get market tags by id
GET
Get market by slug

Series

Comments

Profiles

Search
Data-API

Data API Status

Core

Misc

Builders
Bridge & Swap
Overview

Bridge
Subgraph
Overview
Resolution
Resolution
Conditional Token Frameworks
Overview
Splitting USDC
Merging Tokens
Reedeeming Tokens
Deployment and Additional Information
Proxy Wallets
Proxy wallet
Negative Risk
Overview
List markets

curl --request GET \
  --url https://gamma-api.polymarket.com/markets

200
[
  {
    "id": "<string>",
    "question": "<string>",
    "conditionId": "<string>",
    "slug": "<string>",
    "twitterCardImage": "<string>",
    "resolutionSource": "<string>",
    "endDate": "2023-11-07T05:31:56Z",
    "category": "<string>",
    "ammType": "<string>",
    "liquidity": "<string>",
    "sponsorName": "<string>",
    "sponsorImage": "<string>",
    "startDate": "2023-11-07T05:31:56Z",
    "xAxisValue": "<string>",
    "yAxisValue": "<string>",
    "denominationToken": "<string>",
    "fee": "<string>",
    "image": "<string>",
    "icon": "<string>",
    "lowerBound": "<string>",
    "upperBound": "<string>",
    "description": "<string>",
    "outcomes": "<string>",
    "outcomePrices": "<string>",
    "volume": "<string>",
    "active": true,
    "marketType": "<string>",
    "formatType": "<string>",
    "lowerBoundDate": "<string>",
    "upperBoundDate": "<string>",
    "closed": true,
    "marketMakerAddress": "<string>",
    "createdBy": 123,
    "updatedBy": 123,
    "createdAt": "2023-11-07T05:31:56Z",
    "updatedAt": "2023-11-07T05:31:56Z",
    "closedTime": "<string>",
    "wideFormat": true,
    "new": true,
    "mailchimpTag": "<string>",
    "featured": true,
    "archived": true,
    "resolvedBy": "<string>",
    "restricted": true,
    "marketGroup": 123,
    "groupItemTitle": "<string>",
    "groupItemThreshold": "<string>",
    "questionID": "<string>",
    "umaEndDate": "<string>",
    "enableOrderBook": true,
    "orderPriceMinTickSize": 123,
    "orderMinSize": 123,
    "umaResolutionStatus": "<string>",
    "curationOrder": 123,
    "volumeNum": 123,
    "liquidityNum": 123,
    "endDateIso": "<string>",
    "startDateIso": "<string>",
    "umaEndDateIso": "<string>",
    "hasReviewedDates": true,
    "readyForCron": true,
    "commentsEnabled": true,
    "volume24hr": 123,
    "volume1wk": 123,
    "volume1mo": 123,
    "volume1yr": 123,
    "gameStartTime": "<string>",
    "secondsDelay": 123,
    "clobTokenIds": "<string>",
    "disqusThread": "<string>",
    "shortOutcomes": "<string>",
    "teamAID": "<string>",
    "teamBID": "<string>",
    "umaBond": "<string>",
    "umaReward": "<string>",
    "fpmmLive": true,
    "volume24hrAmm": 123,
    "volume1wkAmm": 123,
    "volume1moAmm": 123,
    "volume1yrAmm": 123,
    "volume24hrClob": 123,
    "volume1wkClob": 123,
    "volume1moClob": 123,
    "volume1yrClob": 123,
    "volumeAmm": 123,
    "volumeClob": 123,
    "liquidityAmm": 123,
    "liquidityClob": 123,
    "makerBaseFee": 123,
    "takerBaseFee": 123,
    "customLiveness": 123,
    "acceptingOrders": true,
    "notificationsEnabled": true,
    "score": 123,
    "imageOptimized": {
      "id": "<string>",
      "imageUrlSource": "<string>",
      "imageUrlOptimized": "<string>",
      "imageSizeKbSource": 123,
      "imageSizeKbOptimized": 123,
      "imageOptimizedComplete": true,
      "imageOptimizedLastUpdated": "<string>",
      "relID": 123,
      "field": "<string>",
      "relname": "<string>"
    },
    "iconOptimized": {
      "id": "<string>",
      "imageUrlSource": "<string>",
      "imageUrlOptimized": "<string>",
      "imageSizeKbSource": 123,
      "imageSizeKbOptimized": 123,
      "imageOptimizedComplete": true,
      "imageOptimizedLastUpdated": "<string>",
      "relID": 123,
      "field": "<string>",
      "relname": "<string>"
    },
    "events": [
      {
        "id": "<string>",
        "ticker": "<string>",
        "slug": "<string>",
        "title": "<string>",
        "subtitle": "<string>",
        "description": "<string>",
        "resolutionSource": "<string>",
        "startDate": "2023-11-07T05:31:56Z",
        "creationDate": "2023-11-07T05:31:56Z",
        "endDate": "2023-11-07T05:31:56Z",
        "image": "<string>",
        "icon": "<string>",
        "active": true,
        "closed": true,
        "archived": true,
        "new": true,
        "featured": true,
        "restricted": true,
        "liquidity": 123,
        "volume": 123,
        "openInterest": 123,
        "sortBy": "<string>",
        "category": "<string>",
        "subcategory": "<string>",
        "isTemplate": true,
        "templateVariables": "<string>",
        "published_at": "<string>",
        "createdBy": "<string>",
        "updatedBy": "<string>",
        "createdAt": "2023-11-07T05:31:56Z",
        "updatedAt": "2023-11-07T05:31:56Z",
        "commentsEnabled": true,
        "competitive": 123,
        "volume24hr": 123,
        "volume1wk": 123,
        "volume1mo": 123,
        "volume1yr": 123,
        "featuredImage": "<string>",
        "disqusThread": "<string>",
        "parentEvent": "<string>",
        "enableOrderBook": true,
        "liquidityAmm": 123,
        "liquidityClob": 123,
        "negRisk": true,
        "negRiskMarketID": "<string>",
        "negRiskFeeBips": 123,
        "commentCount": 123,
        "imageOptimized": {
          "id": "<string>",
          "imageUrlSource": "<string>",
          "imageUrlOptimized": "<string>",
          "imageSizeKbSource": 123,
          "imageSizeKbOptimized": 123,
          "imageOptimizedComplete": true,
          "imageOptimizedLastUpdated": "<string>",
          "relID": 123,
          "field": "<string>",
          "relname": "<string>"
        },
        "iconOptimized": {
          "id": "<string>",
          "imageUrlSource": "<string>",
          "imageUrlOptimized": "<string>",
          "imageSizeKbSource": 123,
          "imageSizeKbOptimized": 123,
          "imageOptimizedComplete": true,
          "imageOptimizedLastUpdated": "<string>",
          "relID": 123,
          "field": "<string>",
          "relname": "<string>"
        },
        "featuredImageOptimized": {
          "id": "<string>",
          "imageUrlSource": "<string>",
          "imageUrlOptimized": "<string>",
          "imageSizeKbSource": 123,
          "imageSizeKbOptimized": 123,
          "imageOptimizedComplete": true,
          "imageOptimizedLastUpdated": "<string>",
          "relID": 123,
          "field": "<string>",
          "relname": "<string>"
        },
        "subEvents": [
          "<string>"
        ],
        "markets": "<array>",
        "series": [
          {
            "id": "<string>",
            "ticker": "<string>",
            "slug": "<string>",
            "title": "<string>",
            "subtitle": "<string>",
            "seriesType": "<string>",
            "recurrence": "<string>",
            "description": "<string>",
            "image": "<string>",
            "icon": "<string>",
            "layout": "<string>",
            "active": true,
            "closed": true,
            "archived": true,
            "new": true,
            "featured": true,
            "restricted": true,
            "isTemplate": true,
            "templateVariables": true,
            "publishedAt": "<string>",
            "createdBy": "<string>",
            "updatedBy": "<string>",
            "createdAt": "2023-11-07T05:31:56Z",
            "updatedAt": "2023-11-07T05:31:56Z",
            "commentsEnabled": true,
            "competitive": "<string>",
            "volume24hr": 123,
            "volume": 123,
            "liquidity": 123,
            "startDate": "2023-11-07T05:31:56Z",
            "pythTokenID": "<string>",
            "cgAssetName": "<string>",
            "score": 123,
            "events": "<array>",
            "collections": [
              {
                "id": "<string>",
                "ticker": "<string>",
                "slug": "<string>",
                "title": "<string>",
                "subtitle": "<string>",
                "collectionType": "<string>",
                "description": "<string>",
                "tags": "<string>",
                "image": "<string>",
                "icon": "<string>",
                "headerImage": "<string>",
                "layout": "<string>",
                "active": true,
                "closed": true,
                "archived": true,
                "new": true,
                "featured": true,
                "restricted": true,
                "isTemplate": true,
                "templateVariables": "<string>",
                "publishedAt": "<string>",
                "createdBy": "<string>",
                "updatedBy": "<string>",
                "createdAt": "2023-11-07T05:31:56Z",
                "updatedAt": "2023-11-07T05:31:56Z",
                "commentsEnabled": true,
                "imageOptimized": {
                  "id": "<string>",
                  "imageUrlSource": "<string>",
                  "imageUrlOptimized": "<string>",
                  "imageSizeKbSource": 123,
                  "imageSizeKbOptimized": 123,
                  "imageOptimizedComplete": true,
                  "imageOptimizedLastUpdated": "<string>",
                  "relID": 123,
                  "field": "<string>",
                  "relname": "<string>"
                },
                "iconOptimized": {
                  "id": "<string>",
                  "imageUrlSource": "<string>",
                  "imageUrlOptimized": "<string>",
                  "imageSizeKbSource": 123,
                  "imageSizeKbOptimized": 123,
                  "imageOptimizedComplete": true,
                  "imageOptimizedLastUpdated": "<string>",
                  "relID": 123,
                  "field": "<string>",
                  "relname": "<string>"
                },
                "headerImageOptimized": {
                  "id": "<string>",
                  "imageUrlSource": "<string>",
                  "imageUrlOptimized": "<string>",
                  "imageSizeKbSource": 123,
                  "imageSizeKbOptimized": 123,
                  "imageOptimizedComplete": true,
                  "imageOptimizedLastUpdated": "<string>",
                  "relID": 123,
                  "field": "<string>",
                  "relname": "<string>"
                }
              }
            ],
            "categories": [
              {
                "id": "<string>",
                "label": "<string>",
                "parentCategory": "<string>",
                "slug": "<string>",
                "publishedAt": "<string>",
                "createdBy": "<string>",
                "updatedBy": "<string>",
                "createdAt": "2023-11-07T05:31:56Z",
                "updatedAt": "2023-11-07T05:31:56Z"
              }
            ],
            "tags": [
              {
                "id": "<string>",
                "label": "<string>",
                "slug": "<string>",
                "forceShow": true,
                "publishedAt": "<string>",
                "createdBy": 123,
                "updatedBy": 123,
                "createdAt": "2023-11-07T05:31:56Z",
                "updatedAt": "2023-11-07T05:31:56Z",
                "forceHide": true,
                "isCarousel": true
              }
            ],
            "commentCount": 123,
            "chats": [
              {
                "id": "<string>",
                "channelId": "<string>",
                "channelName": "<string>",
                "channelImage": "<string>",
                "live": true,
                "startTime": "2023-11-07T05:31:56Z",
                "endTime": "2023-11-07T05:31:56Z"
              }
            ]
          }
        ],
        "categories": [
          {
            "id": "<string>",
            "label": "<string>",
            "parentCategory": "<string>",
            "slug": "<string>",
            "publishedAt": "<string>",
            "createdBy": "<string>",
            "updatedBy": "<string>",
            "createdAt": "2023-11-07T05:31:56Z",
            "updatedAt": "2023-11-07T05:31:56Z"
          }
        ],
        "collections": [
          {
            "id": "<string>",
            "ticker": "<string>",
            "slug": "<string>",
            "title": "<string>",
            "subtitle": "<string>",
            "collectionType": "<string>",
            "description": "<string>",
            "tags": "<string>",
            "image": "<string>",
            "icon": "<string>",
            "headerImage": "<string>",
            "layout": "<string>",
            "active": true,
            "closed": true,
            "archived": true,
            "new": true,
            "featured": true,
            "restricted": true,
            "isTemplate": true,
            "templateVariables": "<string>",
            "publishedAt": "<string>",
            "createdBy": "<string>",
            "updatedBy": "<string>",
            "createdAt": "2023-11-07T05:31:56Z",
            "updatedAt": "2023-11-07T05:31:56Z",
            "commentsEnabled": true,
            "imageOptimized": {
              "id": "<string>",
              "imageUrlSource": "<string>",
              "imageUrlOptimized": "<string>",
              "imageSizeKbSource": 123,
              "imageSizeKbOptimized": 123,
              "imageOptimizedComplete": true,
              "imageOptimizedLastUpdated": "<string>",
              "relID": 123,
              "field": "<string>",
              "relname": "<string>"
            },
            "iconOptimized": {
              "id": "<string>",
              "imageUrlSource": "<string>",
              "imageUrlOptimized": "<string>",
              "imageSizeKbSource": 123,
              "imageSizeKbOptimized": 123,
              "imageOptimizedComplete": true,
              "imageOptimizedLastUpdated": "<string>",
              "relID": 123,
              "field": "<string>",
              "relname": "<string>"
            },
            "headerImageOptimized": {
              "id": "<string>",
              "imageUrlSource": "<string>",
              "imageUrlOptimized": "<string>",
              "imageSizeKbSource": 123,
              "imageSizeKbOptimized": 123,
              "imageOptimizedComplete": true,
              "imageOptimizedLastUpdated": "<string>",
              "relID": 123,
              "field": "<string>",
              "relname": "<string>"
            }
          }
        ],
        "tags": [
          {
            "id": "<string>",
            "label": "<string>",
            "slug": "<string>",
            "forceShow": true,
            "publishedAt": "<string>",
            "createdBy": 123,
            "updatedBy": 123,
            "createdAt": "2023-11-07T05:31:56Z",
            "updatedAt": "2023-11-07T05:31:56Z",
            "forceHide": true,
            "isCarousel": true
          }
        ],
        "cyom": true,
        "closedTime": "2023-11-07T05:31:56Z",
        "showAllOutcomes": true,
        "showMarketImages": true,
        "automaticallyResolved": true,
        "enableNegRisk": true,
        "automaticallyActive": true,
        "eventDate": "<string>",
        "startTime": "2023-11-07T05:31:56Z",
        "eventWeek": 123,
        "seriesSlug": "<string>",
        "score": "<string>",
        "elapsed": "<string>",
        "period": "<string>",
        "live": true,
        "ended": true,
        "finishedTimestamp": "2023-11-07T05:31:56Z",
        "gmpChartMode": "<string>",
        "eventCreators": [
          {
            "id": "<string>",
            "creatorName": "<string>",
            "creatorHandle": "<string>",
            "creatorUrl": "<string>",
            "creatorImage": "<string>",
            "createdAt": "2023-11-07T05:31:56Z",
            "updatedAt": "2023-11-07T05:31:56Z"
          }
        ],
        "tweetCount": 123,
        "chats": [
          {
            "id": "<string>",
            "channelId": "<string>",
            "channelName": "<string>",
            "channelImage": "<string>",
            "live": true,
            "startTime": "2023-11-07T05:31:56Z",
            "endTime": "2023-11-07T05:31:56Z"
          }
        ],
        "featuredOrder": 123,
        "estimateValue": true,
        "cantEstimate": true,
        "estimatedValue": "<string>",
        "templates": [
          {
            "id": "<string>",
            "eventTitle": "<string>",
            "eventSlug": "<string>",
            "eventImage": "<string>",
            "marketTitle": "<string>",
            "description": "<string>",
            "resolutionSource": "<string>",
            "negRisk": true,
            "sortBy": "<string>",
            "showMarketImages": true,
            "seriesSlug": "<string>",
            "outcomes": "<string>"
          }
        ],
        "spreadsMainLine": 123,
        "totalsMainLine": 123,
        "carouselMap": "<string>",
        "pendingDeployment": true,
        "deploying": true,
        "deployingTimestamp": "2023-11-07T05:31:56Z",
        "scheduledDeploymentTimestamp": "2023-11-07T05:31:56Z",
        "gameStatus": "<string>"
      }
    ],
    "categories": [
      {
        "id": "<string>",
        "label": "<string>",
        "parentCategory": "<string>",
        "slug": "<string>",
        "publishedAt": "<string>",
        "createdBy": "<string>",
        "updatedBy": "<string>",
        "createdAt": "2023-11-07T05:31:56Z",
        "updatedAt": "2023-11-07T05:31:56Z"
      }
    ],
    "tags": [
      {
        "id": "<string>",
        "label": "<string>",
        "slug": "<string>",
        "forceShow": true,
        "publishedAt": "<string>",
        "createdBy": 123,
        "updatedBy": 123,
        "createdAt": "2023-11-07T05:31:56Z",
        "updatedAt": "2023-11-07T05:31:56Z",
        "forceHide": true,
        "isCarousel": true
      }
    ],
    "creator": "<string>",
    "ready": true,
    "funded": true,
    "pastSlugs": "<string>",
    "readyTimestamp": "2023-11-07T05:31:56Z",
    "fundedTimestamp": "2023-11-07T05:31:56Z",
    "acceptingOrdersTimestamp": "2023-11-07T05:31:56Z",
    "competitive": 123,
    "rewardsMinSize": 123,
    "rewardsMaxSpread": 123,
    "spread": 123,
    "automaticallyResolved": true,
    "oneDayPriceChange": 123,
    "oneHourPriceChange": 123,
    "oneWeekPriceChange": 123,
    "oneMonthPriceChange": 123,
    "oneYearPriceChange": 123,
    "lastTradePrice": 123,
    "bestBid": 123,
    "bestAsk": 123,
    "automaticallyActive": true,
    "clearBookOnStart": true,
    "chartColor": "<string>",
    "seriesColor": "<string>",
    "showGmpSeries": true,
    "showGmpOutcome": true,
    "manualActivation": true,
    "negRiskOther": true,
    "gameId": "<string>",
    "groupItemRange": "<string>",
    "sportsMarketType": "<string>",
    "line": 123,
    "umaResolutionStatuses": "<string>",
    "pendingDeployment": true,
    "deploying": true,
    "deployingTimestamp": "2023-11-07T05:31:56Z",
    "scheduledDeploymentTimestamp": "2023-11-07T05:31:56Z",
    "rfqEnabled": true,
    "eventStartTime": "2023-11-07T05:31:56Z"
  }
]
Markets
List markets
GET
/
markets

Try it
Query Parameters
​
limit
integer
Required range: x >= 0
​
offset
integer
Required range: x >= 0
​
order
string
Comma-separated list of fields to order by

​
ascending
boolean
​
id
integer[]
​
slug
string[]
​
clob_token_ids
string[]
​
condition_ids
string[]
​
market_maker_address
string[]
​
liquidity_num_min
number
​
liquidity_num_max
number
​
volume_num_min
number
​
volume_num_max
number
​
start_date_min
string<date-time>
​
start_date_max
string<date-time>
​
end_date_min
string<date-time>
​
end_date_max
string<date-time>
​
tag_id
integer
​
related_tags
boolean
​
cyom
boolean
​
uma_resolution_status
string
​
game_id
string
​
sports_market_types
string[]
​
rewards_min_size
number
​
question_ids
string[]
​
include_tag
boolean
​
closed
boolean
Response
200 - application/json
List of markets

​
id
string
​
question
string | null
​
conditionId
string
​
slug
string | null
​
twitterCardImage
string | null
​
resolutionSource
string | null
​
endDate
string<date-time> | null
​
category
string | null
​
ammType
string | null
​
liquidity
string | null
​
sponsorName
string | null
​
sponsorImage
string | null
​
startDate
string<date-time> | null
​
xAxisValue
string | null
​
yAxisValue
string | null
​
denominationToken
string | null
​
fee
string | null
​
image
string | null
​
icon
string | null
​
lowerBound
string | null
​
upperBound
string | null
​
description
string | null
​
outcomes
string | null
​
outcomePrices
string | null
​
volume
string | null
​
active
boolean | null
​
marketType
string | null
​
formatType
string | null
​
lowerBoundDate
string | null
​
upperBoundDate
string | null
​
closed
boolean | null
​
marketMakerAddress
string
​
createdBy
integer | null
​
updatedBy
integer | null
​
createdAt
string<date-time> | null
​
updatedAt
string<date-time> | null
​
closedTime
string | null
​
wideFormat
boolean | null
​
new
boolean | null
​
mailchimpTag
string | null
​
featured
boolean | null
​
archived
boolean | null
​
resolvedBy
string | null
​
restricted
boolean | null
​
marketGroup
integer | null
​
groupItemTitle
string | null
​
groupItemThreshold
string | null
​
questionID
string | null
​
umaEndDate
string | null
​
enableOrderBook
boolean | null
​
orderPriceMinTickSize
number | null
​
orderMinSize
number | null
​
umaResolutionStatus
string | null
​
curationOrder
integer | null
​
volumeNum
number | null
​
liquidityNum
number | null
​
endDateIso
string | null
​
startDateIso
string | null
​
umaEndDateIso
string | null
​
hasReviewedDates
boolean | null
​
readyForCron
boolean | null
​
commentsEnabled
boolean | null
​
volume24hr
number | null
​
volume1wk
number | null
​
volume1mo
number | null
​
volume1yr
number | null
​
gameStartTime
string | null
​
secondsDelay
integer | null
​
clobTokenIds
string | null
​
disqusThread
string | null
​
shortOutcomes
string | null
​
teamAID
string | null
​
teamBID
string | null
​
umaBond
string | null
​
umaReward
string | null
​
fpmmLive
boolean | null
​
volume24hrAmm
number | null
​
volume1wkAmm
number | null
​
volume1moAmm
number | null
​
volume1yrAmm
number | null
​
volume24hrClob
number | null
​
volume1wkClob
number | null
​
volume1moClob
number | null
​
volume1yrClob
number | null
​
volumeAmm
number | null
​
volumeClob
number | null
​
liquidityAmm
number | null
​
liquidityClob
number | null
​
makerBaseFee
integer | null
​
takerBaseFee
integer | null
​
customLiveness
integer | null
​
acceptingOrders
boolean | null
​
notificationsEnabled
boolean | null
​
score
integer | null
​
imageOptimized
object
Show child attributes

​
iconOptimized
object
Show child attributes

​
events
object[]
Show child attributes

​
categories
object[]
Show child attributes

​
tags
object[]
Show child attributes

​
creator
string | null
​
ready
boolean | null
​
funded
boolean | null
​
pastSlugs
string | null
​
readyTimestamp
string<date-time> | null
​
fundedTimestamp
string<date-time> | null
​
acceptingOrdersTimestamp
string<date-time> | null
​
competitive
number | null
​
rewardsMinSize
number | null
​
rewardsMaxSpread
number | null
​
spread
number | null
​
automaticallyResolved
boolean | null
​
oneDayPriceChange
number | null
​
oneHourPriceChange
number | null
​
oneWeekPriceChange
number | null
​
oneMonthPriceChange
number | null
​
oneYearPriceChange
number | null
​
lastTradePrice
number | null
​
bestBid
number | null
​
bestAsk
number | null
​
automaticallyActive
boolean | null
​
clearBookOnStart
boolean | null
​
chartColor
string | null
​
seriesColor
string | null
​
showGmpSeries
boolean | null
​
showGmpOutcome
boolean | null
​
manualActivation
boolean | null
​
negRiskOther
boolean | null
​
gameId
string | null
​
groupItemRange
string | null
​
sportsMarketType
string | null
​
line
number | null
​
umaResolutionStatuses
string | null
​
pendingDeployment
boolean | null
​
deploying
boolean | null
​
deployingTimestamp
string<date-time> | null
​
scheduledDeploymentTimestamp
string<date-time> | null
​
rfqEnabled
boolean | null
​
eventStartTime
string<date-time> | null
Get event by slug
Get market by id
Ask a question...

github
Powered by
List markets - Polymarket Documentation

Skip to main content
Polymarket Documentation home pagedark logo

Search...
Ctrl K

Ask AI
Main Site

User Guide
For Developers
Changelog
Polymarket
Discord Community
Twitter
Developer Quickstart
Developer Quickstart
Fetching Market Data
Placing Your First Order
Glossary
API Rate Limits
Endpoints
Market Makers
Market Maker Introduction
Setup
Trading
Liquidity Rewards
Maker Rebates Program
Data Feeds
Inventory Management
Polymarket Builders Program
Builder Program Introduction
Builder Tiers
Builder Profile & Keys
Order Attribution
Relayer Client
Examples
Central Limit Order Book
CLOB Introduction
Status
Quickstart
Authentication
Geographic Restrictions

Client
Methods Overview
Public Methods
L1 Methods
L2 Methods
Builder Methods

REST API

Orderbook
GET
Get order book summary
POST
Get multiple order books summaries by request

Pricing
GET
Get market price
GET
Get multiple market prices
POST
Get multiple market prices by request
GET
Get midpoint price
GET
Get price history for a traded token

Spreads
POST
Get bid-ask spreads

Historical Timeseries Data
GET
Historical Timeseries Data

Order Management
Orders Overview
Place Single Order
Place Multiple Orders (Batching)
Get Order
Get Active Orders
Check Order Reward Scoring
Cancel Orders(s)
Onchain Order Info

Trades
Trades Overview
Get Trades
Websocket
WSS Overview
WSS Quickstart
WSS Authentication
User Channel
Market Channel

Sports Websocket
Overview
Message Format
Quickstart
Real Time Data Stream
RTDS Overview
RTDS Crypto Prices
RTDS Comments
Gamma Structure
Overview
Gamma Structure
Fetching Markets
Gamma Endpoints

Gamma Status
GET
Gamma API Health check

Sports
GET
List teams
GET
Get sports metadata information
GET
Get valid sports market types

Tags
GET
List tags
GET
Get tag by id
GET
Get tag by slug
GET
Get related tags (relationships) by tag id
GET
Get related tags (relationships) by tag slug
GET
Get tags related to a tag id
GET
Get tags related to a tag slug

Events
GET
List events
GET
Get event by id
GET
Get event tags
GET
Get event by slug

Markets
GET
List markets
GET
Get market by id
GET
Get market tags by id
GET
Get market by slug

Series

Comments

Profiles

Search
Data-API

Data API Status

Core

Misc

Builders
Bridge & Swap
Overview

Bridge
Subgraph
Overview
Resolution
Resolution
Conditional Token Frameworks
Overview
Splitting USDC
Merging Tokens
Reedeeming Tokens
Deployment and Additional Information
Proxy Wallets
Proxy wallet
Negative Risk
Overview
Get market by id

curl --request GET \
  --url https://gamma-api.polymarket.com/markets/{id}

200
{
  "id": "<string>",
  "question": "<string>",
  "conditionId": "<string>",
  "slug": "<string>",
  "twitterCardImage": "<string>",
  "resolutionSource": "<string>",
  "endDate": "2023-11-07T05:31:56Z",
  "category": "<string>",
  "ammType": "<string>",
  "liquidity": "<string>",
  "sponsorName": "<string>",
  "sponsorImage": "<string>",
  "startDate": "2023-11-07T05:31:56Z",
  "xAxisValue": "<string>",
  "yAxisValue": "<string>",
  "denominationToken": "<string>",
  "fee": "<string>",
  "image": "<string>",
  "icon": "<string>",
  "lowerBound": "<string>",
  "upperBound": "<string>",
  "description": "<string>",
  "outcomes": "<string>",
  "outcomePrices": "<string>",
  "volume": "<string>",
  "active": true,
  "marketType": "<string>",
  "formatType": "<string>",
  "lowerBoundDate": "<string>",
  "upperBoundDate": "<string>",
  "closed": true,
  "marketMakerAddress": "<string>",
  "createdBy": 123,
  "updatedBy": 123,
  "createdAt": "2023-11-07T05:31:56Z",
  "updatedAt": "2023-11-07T05:31:56Z",
  "closedTime": "<string>",
  "wideFormat": true,
  "new": true,
  "mailchimpTag": "<string>",
  "featured": true,
  "archived": true,
  "resolvedBy": "<string>",
  "restricted": true,
  "marketGroup": 123,
  "groupItemTitle": "<string>",
  "groupItemThreshold": "<string>",
  "questionID": "<string>",
  "umaEndDate": "<string>",
  "enableOrderBook": true,
  "orderPriceMinTickSize": 123,
  "orderMinSize": 123,
  "umaResolutionStatus": "<string>",
  "curationOrder": 123,
  "volumeNum": 123,
  "liquidityNum": 123,
  "endDateIso": "<string>",
  "startDateIso": "<string>",
  "umaEndDateIso": "<string>",
  "hasReviewedDates": true,
  "readyForCron": true,
  "commentsEnabled": true,
  "volume24hr": 123,
  "volume1wk": 123,
  "volume1mo": 123,
  "volume1yr": 123,
  "gameStartTime": "<string>",
  "secondsDelay": 123,
  "clobTokenIds": "<string>",
  "disqusThread": "<string>",
  "shortOutcomes": "<string>",
  "teamAID": "<string>",
  "teamBID": "<string>",
  "umaBond": "<string>",
  "umaReward": "<string>",
  "fpmmLive": true,
  "volume24hrAmm": 123,
  "volume1wkAmm": 123,
  "volume1moAmm": 123,
  "volume1yrAmm": 123,
  "volume24hrClob": 123,
  "volume1wkClob": 123,
  "volume1moClob": 123,
  "volume1yrClob": 123,
  "volumeAmm": 123,
  "volumeClob": 123,
  "liquidityAmm": 123,
  "liquidityClob": 123,
  "makerBaseFee": 123,
  "takerBaseFee": 123,
  "customLiveness": 123,
  "acceptingOrders": true,
  "notificationsEnabled": true,
  "score": 123,
  "imageOptimized": {
    "id": "<string>",
    "imageUrlSource": "<string>",
    "imageUrlOptimized": "<string>",
    "imageSizeKbSource": 123,
    "imageSizeKbOptimized": 123,
    "imageOptimizedComplete": true,
    "imageOptimizedLastUpdated": "<string>",
    "relID": 123,
    "field": "<string>",
    "relname": "<string>"
  },
  "iconOptimized": {
    "id": "<string>",
    "imageUrlSource": "<string>",
    "imageUrlOptimized": "<string>",
    "imageSizeKbSource": 123,
    "imageSizeKbOptimized": 123,
    "imageOptimizedComplete": true,
    "imageOptimizedLastUpdated": "<string>",
    "relID": 123,
    "field": "<string>",
    "relname": "<string>"
  },
  "events": [
    {
      "id": "<string>",
      "ticker": "<string>",
      "slug": "<string>",
      "title": "<string>",
      "subtitle": "<string>",
      "description": "<string>",
      "resolutionSource": "<string>",
      "startDate": "2023-11-07T05:31:56Z",
      "creationDate": "2023-11-07T05:31:56Z",
      "endDate": "2023-11-07T05:31:56Z",
      "image": "<string>",
      "icon": "<string>",
      "active": true,
      "closed": true,
      "archived": true,
      "new": true,
      "featured": true,
      "restricted": true,
      "liquidity": 123,
      "volume": 123,
      "openInterest": 123,
      "sortBy": "<string>",
      "category": "<string>",
      "subcategory": "<string>",
      "isTemplate": true,
      "templateVariables": "<string>",
      "published_at": "<string>",
      "createdBy": "<string>",
      "updatedBy": "<string>",
      "createdAt": "2023-11-07T05:31:56Z",
      "updatedAt": "2023-11-07T05:31:56Z",
      "commentsEnabled": true,
      "competitive": 123,
      "volume24hr": 123,
      "volume1wk": 123,
      "volume1mo": 123,
      "volume1yr": 123,
      "featuredImage": "<string>",
      "disqusThread": "<string>",
      "parentEvent": "<string>",
      "enableOrderBook": true,
      "liquidityAmm": 123,
      "liquidityClob": 123,
      "negRisk": true,
      "negRiskMarketID": "<string>",
      "negRiskFeeBips": 123,
      "commentCount": 123,
      "imageOptimized": {
        "id": "<string>",
        "imageUrlSource": "<string>",
        "imageUrlOptimized": "<string>",
        "imageSizeKbSource": 123,
        "imageSizeKbOptimized": 123,
        "imageOptimizedComplete": true,
        "imageOptimizedLastUpdated": "<string>",
        "relID": 123,
        "field": "<string>",
        "relname": "<string>"
      },
      "iconOptimized": {
        "id": "<string>",
        "imageUrlSource": "<string>",
        "imageUrlOptimized": "<string>",
        "imageSizeKbSource": 123,
        "imageSizeKbOptimized": 123,
        "imageOptimizedComplete": true,
        "imageOptimizedLastUpdated": "<string>",
        "relID": 123,
        "field": "<string>",
        "relname": "<string>"
      },
      "featuredImageOptimized": {
        "id": "<string>",
        "imageUrlSource": "<string>",
        "imageUrlOptimized": "<string>",
        "imageSizeKbSource": 123,
        "imageSizeKbOptimized": 123,
        "imageOptimizedComplete": true,
        "imageOptimizedLastUpdated": "<string>",
        "relID": 123,
        "field": "<string>",
        "relname": "<string>"
      },
      "subEvents": [
        "<string>"
      ],
      "markets": "<array>",
      "series": [
        {
          "id": "<string>",
          "ticker": "<string>",
          "slug": "<string>",
          "title": "<string>",
          "subtitle": "<string>",
          "seriesType": "<string>",
          "recurrence": "<string>",
          "description": "<string>",
          "image": "<string>",
          "icon": "<string>",
          "layout": "<string>",
          "active": true,
          "closed": true,
          "archived": true,
          "new": true,
          "featured": true,
          "restricted": true,
          "isTemplate": true,
          "templateVariables": true,
          "publishedAt": "<string>",
          "createdBy": "<string>",
          "updatedBy": "<string>",
          "createdAt": "2023-11-07T05:31:56Z",
          "updatedAt": "2023-11-07T05:31:56Z",
          "commentsEnabled": true,
          "competitive": "<string>",
          "volume24hr": 123,
          "volume": 123,
          "liquidity": 123,
          "startDate": "2023-11-07T05:31:56Z",
          "pythTokenID": "<string>",
          "cgAssetName": "<string>",
          "score": 123,
          "events": "<array>",
          "collections": [
            {
              "id": "<string>",
              "ticker": "<string>",
              "slug": "<string>",
              "title": "<string>",
              "subtitle": "<string>",
              "collectionType": "<string>",
              "description": "<string>",
              "tags": "<string>",
              "image": "<string>",
              "icon": "<string>",
              "headerImage": "<string>",
              "layout": "<string>",
              "active": true,
              "closed": true,
              "archived": true,
              "new": true,
              "featured": true,
              "restricted": true,
              "isTemplate": true,
              "templateVariables": "<string>",
              "publishedAt": "<string>",
              "createdBy": "<string>",
              "updatedBy": "<string>",
              "createdAt": "2023-11-07T05:31:56Z",
              "updatedAt": "2023-11-07T05:31:56Z",
              "commentsEnabled": true,
              "imageOptimized": {
                "id": "<string>",
                "imageUrlSource": "<string>",
                "imageUrlOptimized": "<string>",
                "imageSizeKbSource": 123,
                "imageSizeKbOptimized": 123,
                "imageOptimizedComplete": true,
                "imageOptimizedLastUpdated": "<string>",
                "relID": 123,
                "field": "<string>",
                "relname": "<string>"
              },
              "iconOptimized": {
                "id": "<string>",
                "imageUrlSource": "<string>",
                "imageUrlOptimized": "<string>",
                "imageSizeKbSource": 123,
                "imageSizeKbOptimized": 123,
                "imageOptimizedComplete": true,
                "imageOptimizedLastUpdated": "<string>",
                "relID": 123,
                "field": "<string>",
                "relname": "<string>"
              },
              "headerImageOptimized": {
                "id": "<string>",
                "imageUrlSource": "<string>",
                "imageUrlOptimized": "<string>",
                "imageSizeKbSource": 123,
                "imageSizeKbOptimized": 123,
                "imageOptimizedComplete": true,
                "imageOptimizedLastUpdated": "<string>",
                "relID": 123,
                "field": "<string>",
                "relname": "<string>"
              }
            }
          ],
          "categories": [
            {
              "id": "<string>",
              "label": "<string>",
              "parentCategory": "<string>",
              "slug": "<string>",
              "publishedAt": "<string>",
              "createdBy": "<string>",
              "updatedBy": "<string>",
              "createdAt": "2023-11-07T05:31:56Z",
              "updatedAt": "2023-11-07T05:31:56Z"
            }
          ],
          "tags": [
            {
              "id": "<string>",
              "label": "<string>",
              "slug": "<string>",
              "forceShow": true,
              "publishedAt": "<string>",
              "createdBy": 123,
              "updatedBy": 123,
              "createdAt": "2023-11-07T05:31:56Z",
              "updatedAt": "2023-11-07T05:31:56Z",
              "forceHide": true,
              "isCarousel": true
            }
          ],
          "commentCount": 123,
          "chats": [
            {
              "id": "<string>",
              "channelId": "<string>",
              "channelName": "<string>",
              "channelImage": "<string>",
              "live": true,
              "startTime": "2023-11-07T05:31:56Z",
              "endTime": "2023-11-07T05:31:56Z"
            }
          ]
        }
      ],
      "categories": [
        {
          "id": "<string>",
          "label": "<string>",
          "parentCategory": "<string>",
          "slug": "<string>",
          "publishedAt": "<string>",
          "createdBy": "<string>",
          "updatedBy": "<string>",
          "createdAt": "2023-11-07T05:31:56Z",
          "updatedAt": "2023-11-07T05:31:56Z"
        }
      ],
      "collections": [
        {
          "id": "<string>",
          "ticker": "<string>",
          "slug": "<string>",
          "title": "<string>",
          "subtitle": "<string>",
          "collectionType": "<string>",
          "description": "<string>",
          "tags": "<string>",
          "image": "<string>",
          "icon": "<string>",
          "headerImage": "<string>",
          "layout": "<string>",
          "active": true,
          "closed": true,
          "archived": true,
          "new": true,
          "featured": true,
          "restricted": true,
          "isTemplate": true,
          "templateVariables": "<string>",
          "publishedAt": "<string>",
          "createdBy": "<string>",
          "updatedBy": "<string>",
          "createdAt": "2023-11-07T05:31:56Z",
          "updatedAt": "2023-11-07T05:31:56Z",
          "commentsEnabled": true,
          "imageOptimized": {
            "id": "<string>",
            "imageUrlSource": "<string>",
            "imageUrlOptimized": "<string>",
            "imageSizeKbSource": 123,
            "imageSizeKbOptimized": 123,
            "imageOptimizedComplete": true,
            "imageOptimizedLastUpdated": "<string>",
            "relID": 123,
            "field": "<string>",
            "relname": "<string>"
          },
          "iconOptimized": {
            "id": "<string>",
            "imageUrlSource": "<string>",
            "imageUrlOptimized": "<string>",
            "imageSizeKbSource": 123,
            "imageSizeKbOptimized": 123,
            "imageOptimizedComplete": true,
            "imageOptimizedLastUpdated": "<string>",
            "relID": 123,
            "field": "<string>",
            "relname": "<string>"
          },
          "headerImageOptimized": {
            "id": "<string>",
            "imageUrlSource": "<string>",
            "imageUrlOptimized": "<string>",
            "imageSizeKbSource": 123,
            "imageSizeKbOptimized": 123,
            "imageOptimizedComplete": true,
            "imageOptimizedLastUpdated": "<string>",
            "relID": 123,
            "field": "<string>",
            "relname": "<string>"
          }
        }
      ],
      "tags": [
        {
          "id": "<string>",
          "label": "<string>",
          "slug": "<string>",
          "forceShow": true,
          "publishedAt": "<string>",
          "createdBy": 123,
          "updatedBy": 123,
          "createdAt": "2023-11-07T05:31:56Z",
          "updatedAt": "2023-11-07T05:31:56Z",
          "forceHide": true,
          "isCarousel": true
        }
      ],
      "cyom": true,
      "closedTime": "2023-11-07T05:31:56Z",
      "showAllOutcomes": true,
      "showMarketImages": true,
      "automaticallyResolved": true,
      "enableNegRisk": true,
      "automaticallyActive": true,
      "eventDate": "<string>",
      "startTime": "2023-11-07T05:31:56Z",
      "eventWeek": 123,
      "seriesSlug": "<string>",
      "score": "<string>",
      "elapsed": "<string>",
      "period": "<string>",
      "live": true,
      "ended": true,
      "finishedTimestamp": "2023-11-07T05:31:56Z",
      "gmpChartMode": "<string>",
      "eventCreators": [
        {
          "id": "<string>",
          "creatorName": "<string>",
          "creatorHandle": "<string>",
          "creatorUrl": "<string>",
          "creatorImage": "<string>",
          "createdAt": "2023-11-07T05:31:56Z",
          "updatedAt": "2023-11-07T05:31:56Z"
        }
      ],
      "tweetCount": 123,
      "chats": [
        {
          "id": "<string>",
          "channelId": "<string>",
          "channelName": "<string>",
          "channelImage": "<string>",
          "live": true,
          "startTime": "2023-11-07T05:31:56Z",
          "endTime": "2023-11-07T05:31:56Z"
        }
      ],
      "featuredOrder": 123,
      "estimateValue": true,
      "cantEstimate": true,
      "estimatedValue": "<string>",
      "templates": [
        {
          "id": "<string>",
          "eventTitle": "<string>",
          "eventSlug": "<string>",
          "eventImage": "<string>",
          "marketTitle": "<string>",
          "description": "<string>",
          "resolutionSource": "<string>",
          "negRisk": true,
          "sortBy": "<string>",
          "showMarketImages": true,
          "seriesSlug": "<string>",
          "outcomes": "<string>"
        }
      ],
      "spreadsMainLine": 123,
      "totalsMainLine": 123,
      "carouselMap": "<string>",
      "pendingDeployment": true,
      "deploying": true,
      "deployingTimestamp": "2023-11-07T05:31:56Z",
      "scheduledDeploymentTimestamp": "2023-11-07T05:31:56Z",
      "gameStatus": "<string>"
    }
  ],
  "categories": [
    {
      "id": "<string>",
      "label": "<string>",
      "parentCategory": "<string>",
      "slug": "<string>",
      "publishedAt": "<string>",
      "createdBy": "<string>",
      "updatedBy": "<string>",
      "createdAt": "2023-11-07T05:31:56Z",
      "updatedAt": "2023-11-07T05:31:56Z"
    }
  ],
  "tags": [
    {
      "id": "<string>",
      "label": "<string>",
      "slug": "<string>",
      "forceShow": true,
      "publishedAt": "<string>",
      "createdBy": 123,
      "updatedBy": 123,
      "createdAt": "2023-11-07T05:31:56Z",
      "updatedAt": "2023-11-07T05:31:56Z",
      "forceHide": true,
      "isCarousel": true
    }
  ],
  "creator": "<string>",
  "ready": true,
  "funded": true,
  "pastSlugs": "<string>",
  "readyTimestamp": "2023-11-07T05:31:56Z",
  "fundedTimestamp": "2023-11-07T05:31:56Z",
  "acceptingOrdersTimestamp": "2023-11-07T05:31:56Z",
  "competitive": 123,
  "rewardsMinSize": 123,
  "rewardsMaxSpread": 123,
  "spread": 123,
  "automaticallyResolved": true,
  "oneDayPriceChange": 123,
  "oneHourPriceChange": 123,
  "oneWeekPriceChange": 123,
  "oneMonthPriceChange": 123,
  "oneYearPriceChange": 123,
  "lastTradePrice": 123,
  "bestBid": 123,
  "bestAsk": 123,
  "automaticallyActive": true,
  "clearBookOnStart": true,
  "chartColor": "<string>",
  "seriesColor": "<string>",
  "showGmpSeries": true,
  "showGmpOutcome": true,
  "manualActivation": true,
  "negRiskOther": true,
  "gameId": "<string>",
  "groupItemRange": "<string>",
  "sportsMarketType": "<string>",
  "line": 123,
  "umaResolutionStatuses": "<string>",
  "pendingDeployment": true,
  "deploying": true,
  "deployingTimestamp": "2023-11-07T05:31:56Z",
  "scheduledDeploymentTimestamp": "2023-11-07T05:31:56Z",
  "rfqEnabled": true,
  "eventStartTime": "2023-11-07T05:31:56Z"
}
Markets
Get market by id
GET
/
markets
/
{id}

Try it
Path Parameters
​
id
integerrequired
Query Parameters
​
include_tag
boolean
Response

200

application/json
Market

​
id
string
​
question
string | null
​
conditionId
string
​
slug
string | null
​
twitterCardImage
string | null
​
resolutionSource
string | null
​
endDate
string<date-time> | null
​
category
string | null
​
ammType
string | null
​
liquidity
string | null
​
sponsorName
string | null
​
sponsorImage
string | null
​
startDate
string<date-time> | null
​
xAxisValue
string | null
​
yAxisValue
string | null
​
denominationToken
string | null
​
fee
string | null
​
image
string | null
​
icon
string | null
​
lowerBound
string | null
​
upperBound
string | null
​
description
string | null
​
outcomes
string | null
​
outcomePrices
string | null
​
volume
string | null
​
active
boolean | null
​
marketType
string | null
​
formatType
string | null
​
lowerBoundDate
string | null
​
upperBoundDate
string | null
​
closed
boolean | null
​
marketMakerAddress
string
​
createdBy
integer | null
​
updatedBy
integer | null
​
createdAt
string<date-time> | null
​
updatedAt
string<date-time> | null
​
closedTime
string | null
​
wideFormat
boolean | null
​
new
boolean | null
​
mailchimpTag
string | null
​
featured
boolean | null
​
archived
boolean | null
​
resolvedBy
string | null
​
restricted
boolean | null
​
marketGroup
integer | null
​
groupItemTitle
string | null
​
groupItemThreshold
string | null
​
questionID
string | null
​
umaEndDate
string | null
​
enableOrderBook
boolean | null
​
orderPriceMinTickSize
number | null
​
orderMinSize
number | null
​
umaResolutionStatus
string | null
​
curationOrder
integer | null
​
volumeNum
number | null
​
liquidityNum
number | null
​
endDateIso
string | null
​
startDateIso
string | null
​
umaEndDateIso
string | null
​
hasReviewedDates
boolean | null
​
readyForCron
boolean | null
​
commentsEnabled
boolean | null
​
volume24hr
number | null
​
volume1wk
number | null
​
volume1mo
number | null
​
volume1yr
number | null
​
gameStartTime
string | null
​
secondsDelay
integer | null
​
clobTokenIds
string | null
​
disqusThread
string | null
​
shortOutcomes
string | null
​
teamAID
string | null
​
teamBID
string | null
​
umaBond
string | null
​
umaReward
string | null
​
fpmmLive
boolean | null
​
volume24hrAmm
number | null
​
volume1wkAmm
number | null
​
volume1moAmm
number | null
​
volume1yrAmm
number | null
​
volume24hrClob
number | null
​
volume1wkClob
number | null
​
volume1moClob
number | null
​
volume1yrClob
number | null
​
volumeAmm
number | null
​
volumeClob
number | null
​
liquidityAmm
number | null
​
liquidityClob
number | null
​
makerBaseFee
integer | null
​
takerBaseFee
integer | null
​
customLiveness
integer | null
​
acceptingOrders
boolean | null
​
notificationsEnabled
boolean | null
​
score
integer | null
​
imageOptimized
object
Show child attributes

​
iconOptimized
object
Show child attributes

​
events
object[]
Show child attributes

​
categories
object[]
Show child attributes

​
tags
object[]
Show child attributes

​
creator
string | null
​
ready
boolean | null
​
funded
boolean | null
​
pastSlugs
string | null
​
readyTimestamp
string<date-time> | null
​
fundedTimestamp
string<date-time> | null
​
acceptingOrdersTimestamp
string<date-time> | null
​
competitive
number | null
​
rewardsMinSize
number | null
​
rewardsMaxSpread
number | null
​
spread
number | null
​
automaticallyResolved
boolean | null
​
oneDayPriceChange
number | null
​
oneHourPriceChange
number | null
​
oneWeekPriceChange
number | null
​
oneMonthPriceChange
number | null
​
oneYearPriceChange
number | null
​
lastTradePrice
number | null
​
bestBid
number | null
​
bestAsk
number | null
​
automaticallyActive
boolean | null
​
clearBookOnStart
boolean | null
​
chartColor
string | null
​
seriesColor
string | null
​
showGmpSeries
boolean | null
​
showGmpOutcome
boolean | null
​
manualActivation
boolean | null
​
negRiskOther
boolean | null
​
gameId
string | null
​
groupItemRange
string | null
​
sportsMarketType
string | null
​
line
number | null
​
umaResolutionStatuses
string | null
​
pendingDeployment
boolean | null
​
deploying
boolean | null
​
deployingTimestamp
string<date-time> | null
​
scheduledDeploymentTimestamp
string<date-time> | null
​
rfqEnabled
boolean | null
​
eventStartTime
string<date-time> | null
List markets
Get market tags by id
Ask a question...

github
Powered by
Get market by id - Polymarket Documentation

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.polymarket.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get market tags by id



## OpenAPI

````yaml api-reference/gamma-openapi.json get /markets/{id}/tags
openapi: 3.0.3
info:
  title: Markets API
  version: 1.0.0
  description: REST API specification for public endpoints used by the Markets service.
servers:
  - url: https://gamma-api.polymarket.com
    description: Polymarket Gamma API Production Server
security: []
tags:
  - name: Gamma Status
    description: Gamma API status and health check
  - name: Sports
    description: Sports-related endpoints including teams and game data
  - name: Tags
    description: Tag management and related tag operations
  - name: Events
    description: Event management and event-related operations
  - name: Markets
    description: Market data and market-related operations
  - name: Comments
    description: Comment system and user interactions
  - name: Series
    description: Series management and related operations
  - name: Profiles
    description: User profile management
  - name: Search
    description: Search functionality across different entity types
paths:
  /markets/{id}/tags:
    get:
      tags:
        - Markets
        - Tags
      summary: Get market tags by id
      operationId: getMarketTags
      parameters:
        - $ref: '#/components/parameters/pathId'
      responses:
        '200':
          description: Tags attached to the market
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Tag'
        '404':
          description: Not found
components:
  parameters:
    pathId:
      name: id
      in: path
      required: true
      schema:
        type: integer
  schemas:
    Tag:
      type: object
      properties:
        id:
          type: string
        label:
          type: string
          nullable: true
        slug:
          type: string
          nullable: true
        forceShow:
          type: boolean
          nullable: true
        publishedAt:
          type: string
          nullable: true
        createdBy:
          type: integer
          nullable: true
        updatedBy:
          type: integer
          nullable: true
        createdAt:
          type: string
          format: date-time
          nullable: true
        updatedAt:
          type: string
          format: date-time
          nullable: true
        forceHide:
          type: boolean
          nullable: true
        isCarousel:
          type: boolean
          nullable: true

````

Skip to main content
Polymarket Documentation home pagedark logo

Search...
Ctrl K

Ask AI
Main Site

User Guide
For Developers
Changelog
Polymarket
Discord Community
Twitter
Developer Quickstart
Developer Quickstart
Fetching Market Data
Placing Your First Order
Glossary
API Rate Limits
Endpoints
Market Makers
Market Maker Introduction
Setup
Trading
Liquidity Rewards
Maker Rebates Program
Data Feeds
Inventory Management
Polymarket Builders Program
Builder Program Introduction
Builder Tiers
Builder Profile & Keys
Order Attribution
Relayer Client
Examples
Central Limit Order Book
CLOB Introduction
Status
Quickstart
Authentication
Geographic Restrictions

Client
Methods Overview
Public Methods
L1 Methods
L2 Methods
Builder Methods

REST API

Orderbook
GET
Get order book summary
POST
Get multiple order books summaries by request

Pricing
GET
Get market price
GET
Get multiple market prices
POST
Get multiple market prices by request
GET
Get midpoint price
GET
Get price history for a traded token

Spreads
POST
Get bid-ask spreads

Historical Timeseries Data
GET
Historical Timeseries Data

Order Management
Orders Overview
Place Single Order
Place Multiple Orders (Batching)
Get Order
Get Active Orders
Check Order Reward Scoring
Cancel Orders(s)
Onchain Order Info

Trades
Trades Overview
Get Trades
Websocket
WSS Overview
WSS Quickstart
WSS Authentication
User Channel
Market Channel

Sports Websocket
Overview
Message Format
Quickstart
Real Time Data Stream
RTDS Overview
RTDS Crypto Prices
RTDS Comments
Gamma Structure
Overview
Gamma Structure
Fetching Markets
Gamma Endpoints

Gamma Status
GET
Gamma API Health check

Sports
GET
List teams
GET
Get sports metadata information
GET
Get valid sports market types

Tags
GET
List tags
GET
Get tag by id
GET
Get tag by slug
GET
Get related tags (relationships) by tag id
GET
Get related tags (relationships) by tag slug
GET
Get tags related to a tag id
GET
Get tags related to a tag slug

Events
GET
List events
GET
Get event by id
GET
Get event tags
GET
Get event by slug

Markets
GET
List markets
GET
Get market by id
GET
Get market tags by id
GET
Get market by slug

Series

Comments

Profiles

Search
Data-API

Data API Status

Core

Misc

Builders
Bridge & Swap
Overview

Bridge
Subgraph
Overview
Resolution
Resolution
Conditional Token Frameworks
Overview
Splitting USDC
Merging Tokens
Reedeeming Tokens
Deployment and Additional Information
Proxy Wallets
Proxy wallet
Negative Risk
Overview
Get market by slug

curl --request GET \
  --url https://gamma-api.polymarket.com/markets/slug/{slug}

200
{
  "id": "<string>",
  "question": "<string>",
  "conditionId": "<string>",
  "slug": "<string>",
  "twitterCardImage": "<string>",
  "resolutionSource": "<string>",
  "endDate": "2023-11-07T05:31:56Z",
  "category": "<string>",
  "ammType": "<string>",
  "liquidity": "<string>",
  "sponsorName": "<string>",
  "sponsorImage": "<string>",
  "startDate": "2023-11-07T05:31:56Z",
  "xAxisValue": "<string>",
  "yAxisValue": "<string>",
  "denominationToken": "<string>",
  "fee": "<string>",
  "image": "<string>",
  "icon": "<string>",
  "lowerBound": "<string>",
  "upperBound": "<string>",
  "description": "<string>",
  "outcomes": "<string>",
  "outcomePrices": "<string>",
  "volume": "<string>",
  "active": true,
  "marketType": "<string>",
  "formatType": "<string>",
  "lowerBoundDate": "<string>",
  "upperBoundDate": "<string>",
  "closed": true,
  "marketMakerAddress": "<string>",
  "createdBy": 123,
  "updatedBy": 123,
  "createdAt": "2023-11-07T05:31:56Z",
  "updatedAt": "2023-11-07T05:31:56Z",
  "closedTime": "<string>",
  "wideFormat": true,
  "new": true,
  "mailchimpTag": "<string>",
  "featured": true,
  "archived": true,
  "resolvedBy": "<string>",
  "restricted": true,
  "marketGroup": 123,
  "groupItemTitle": "<string>",
  "groupItemThreshold": "<string>",
  "questionID": "<string>",
  "umaEndDate": "<string>",
  "enableOrderBook": true,
  "orderPriceMinTickSize": 123,
  "orderMinSize": 123,
  "umaResolutionStatus": "<string>",
  "curationOrder": 123,
  "volumeNum": 123,
  "liquidityNum": 123,
  "endDateIso": "<string>",
  "startDateIso": "<string>",
  "umaEndDateIso": "<string>",
  "hasReviewedDates": true,
  "readyForCron": true,
  "commentsEnabled": true,
  "volume24hr": 123,
  "volume1wk": 123,
  "volume1mo": 123,
  "volume1yr": 123,
  "gameStartTime": "<string>",
  "secondsDelay": 123,
  "clobTokenIds": "<string>",
  "disqusThread": "<string>",
  "shortOutcomes": "<string>",
  "teamAID": "<string>",
  "teamBID": "<string>",
  "umaBond": "<string>",
  "umaReward": "<string>",
  "fpmmLive": true,
  "volume24hrAmm": 123,
  "volume1wkAmm": 123,
  "volume1moAmm": 123,
  "volume1yrAmm": 123,
  "volume24hrClob": 123,
  "volume1wkClob": 123,
  "volume1moClob": 123,
  "volume1yrClob": 123,
  "volumeAmm": 123,
  "volumeClob": 123,
  "liquidityAmm": 123,
  "liquidityClob": 123,
  "makerBaseFee": 123,
  "takerBaseFee": 123,
  "customLiveness": 123,
  "acceptingOrders": true,
  "notificationsEnabled": true,
  "score": 123,
  "imageOptimized": {
    "id": "<string>",
    "imageUrlSource": "<string>",
    "imageUrlOptimized": "<string>",
    "imageSizeKbSource": 123,
    "imageSizeKbOptimized": 123,
    "imageOptimizedComplete": true,
    "imageOptimizedLastUpdated": "<string>",
    "relID": 123,
    "field": "<string>",
    "relname": "<string>"
  },
  "iconOptimized": {
    "id": "<string>",
    "imageUrlSource": "<string>",
    "imageUrlOptimized": "<string>",
    "imageSizeKbSource": 123,
    "imageSizeKbOptimized": 123,
    "imageOptimizedComplete": true,
    "imageOptimizedLastUpdated": "<string>",
    "relID": 123,
    "field": "<string>",
    "relname": "<string>"
  },
  "events": [
    {
      "id": "<string>",
      "ticker": "<string>",
      "slug": "<string>",
      "title": "<string>",
      "subtitle": "<string>",
      "description": "<string>",
      "resolutionSource": "<string>",
      "startDate": "2023-11-07T05:31:56Z",
      "creationDate": "2023-11-07T05:31:56Z",
      "endDate": "2023-11-07T05:31:56Z",
      "image": "<string>",
      "icon": "<string>",
      "active": true,
      "closed": true,
      "archived": true,
      "new": true,
      "featured": true,
      "restricted": true,
      "liquidity": 123,
      "volume": 123,
      "openInterest": 123,
      "sortBy": "<string>",
      "category": "<string>",
      "subcategory": "<string>",
      "isTemplate": true,
      "templateVariables": "<string>",
      "published_at": "<string>",
      "createdBy": "<string>",
      "updatedBy": "<string>",
      "createdAt": "2023-11-07T05:31:56Z",
      "updatedAt": "2023-11-07T05:31:56Z",
      "commentsEnabled": true,
      "competitive": 123,
      "volume24hr": 123,
      "volume1wk": 123,
      "volume1mo": 123,
      "volume1yr": 123,
      "featuredImage": "<string>",
      "disqusThread": "<string>",
      "parentEvent": "<string>",
      "enableOrderBook": true,
      "liquidityAmm": 123,
      "liquidityClob": 123,
      "negRisk": true,
      "negRiskMarketID": "<string>",
      "negRiskFeeBips": 123,
      "commentCount": 123,
      "imageOptimized": {
        "id": "<string>",
        "imageUrlSource": "<string>",
        "imageUrlOptimized": "<string>",
        "imageSizeKbSource": 123,
        "imageSizeKbOptimized": 123,
        "imageOptimizedComplete": true,
        "imageOptimizedLastUpdated": "<string>",
        "relID": 123,
        "field": "<string>",
        "relname": "<string>"
      },
      "iconOptimized": {
        "id": "<string>",
        "imageUrlSource": "<string>",
        "imageUrlOptimized": "<string>",
        "imageSizeKbSource": 123,
        "imageSizeKbOptimized": 123,
        "imageOptimizedComplete": true,
        "imageOptimizedLastUpdated": "<string>",
        "relID": 123,
        "field": "<string>",
        "relname": "<string>"
      },
      "featuredImageOptimized": {
        "id": "<string>",
        "imageUrlSource": "<string>",
        "imageUrlOptimized": "<string>",
        "imageSizeKbSource": 123,
        "imageSizeKbOptimized": 123,
        "imageOptimizedComplete": true,
        "imageOptimizedLastUpdated": "<string>",
        "relID": 123,
        "field": "<string>",
        "relname": "<string>"
      },
      "subEvents": [
        "<string>"
      ],
      "markets": "<array>",
      "series": [
        {
          "id": "<string>",
          "ticker": "<string>",
          "slug": "<string>",
          "title": "<string>",
          "subtitle": "<string>",
          "seriesType": "<string>",
          "recurrence": "<string>",
          "description": "<string>",
          "image": "<string>",
          "icon": "<string>",
          "layout": "<string>",
          "active": true,
          "closed": true,
          "archived": true,
          "new": true,
          "featured": true,
          "restricted": true,
          "isTemplate": true,
          "templateVariables": true,
          "publishedAt": "<string>",
          "createdBy": "<string>",
          "updatedBy": "<string>",
          "createdAt": "2023-11-07T05:31:56Z",
          "updatedAt": "2023-11-07T05:31:56Z",
          "commentsEnabled": true,
          "competitive": "<string>",
          "volume24hr": 123,
          "volume": 123,
          "liquidity": 123,
          "startDate": "2023-11-07T05:31:56Z",
          "pythTokenID": "<string>",
          "cgAssetName": "<string>",
          "score": 123,
          "events": "<array>",
          "collections": [
            {
              "id": "<string>",
              "ticker": "<string>",
              "slug": "<string>",
              "title": "<string>",
              "subtitle": "<string>",
              "collectionType": "<string>",
              "description": "<string>",
              "tags": "<string>",
              "image": "<string>",
              "icon": "<string>",
              "headerImage": "<string>",
              "layout": "<string>",
              "active": true,
              "closed": true,
              "archived": true,
              "new": true,
              "featured": true,
              "restricted": true,
              "isTemplate": true,
              "templateVariables": "<string>",
              "publishedAt": "<string>",
              "createdBy": "<string>",
              "updatedBy": "<string>",
              "createdAt": "2023-11-07T05:31:56Z",
              "updatedAt": "2023-11-07T05:31:56Z",
              "commentsEnabled": true,
              "imageOptimized": {
                "id": "<string>",
                "imageUrlSource": "<string>",
                "imageUrlOptimized": "<string>",
                "imageSizeKbSource": 123,
                "imageSizeKbOptimized": 123,
                "imageOptimizedComplete": true,
                "imageOptimizedLastUpdated": "<string>",
                "relID": 123,
                "field": "<string>",
                "relname": "<string>"
              },
              "iconOptimized": {
                "id": "<string>",
                "imageUrlSource": "<string>",
                "imageUrlOptimized": "<string>",
                "imageSizeKbSource": 123,
                "imageSizeKbOptimized": 123,
                "imageOptimizedComplete": true,
                "imageOptimizedLastUpdated": "<string>",
                "relID": 123,
                "field": "<string>",
                "relname": "<string>"
              },
              "headerImageOptimized": {
                "id": "<string>",
                "imageUrlSource": "<string>",
                "imageUrlOptimized": "<string>",
                "imageSizeKbSource": 123,
                "imageSizeKbOptimized": 123,
                "imageOptimizedComplete": true,
                "imageOptimizedLastUpdated": "<string>",
                "relID": 123,
                "field": "<string>",
                "relname": "<string>"
              }
            }
          ],
          "categories": [
            {
              "id": "<string>",
              "label": "<string>",
              "parentCategory": "<string>",
              "slug": "<string>",
              "publishedAt": "<string>",
              "createdBy": "<string>",
              "updatedBy": "<string>",
              "createdAt": "2023-11-07T05:31:56Z",
              "updatedAt": "2023-11-07T05:31:56Z"
            }
          ],
          "tags": [
            {
              "id": "<string>",
              "label": "<string>",
              "slug": "<string>",
              "forceShow": true,
              "publishedAt": "<string>",
              "createdBy": 123,
              "updatedBy": 123,
              "createdAt": "2023-11-07T05:31:56Z",
              "updatedAt": "2023-11-07T05:31:56Z",
              "forceHide": true,
              "isCarousel": true
            }
          ],
          "commentCount": 123,
          "chats": [
            {
              "id": "<string>",
              "channelId": "<string>",
              "channelName": "<string>",
              "channelImage": "<string>",
              "live": true,
              "startTime": "2023-11-07T05:31:56Z",
              "endTime": "2023-11-07T05:31:56Z"
            }
          ]
        }
      ],
      "categories": [
        {
          "id": "<string>",
          "label": "<string>",
          "parentCategory": "<string>",
          "slug": "<string>",
          "publishedAt": "<string>",
          "createdBy": "<string>",
          "updatedBy": "<string>",
          "createdAt": "2023-11-07T05:31:56Z",
          "updatedAt": "2023-11-07T05:31:56Z"
        }
      ],
      "collections": [
        {
          "id": "<string>",
          "ticker": "<string>",
          "slug": "<string>",
          "title": "<string>",
          "subtitle": "<string>",
          "collectionType": "<string>",
          "description": "<string>",
          "tags": "<string>",
          "image": "<string>",
          "icon": "<string>",
          "headerImage": "<string>",
          "layout": "<string>",
          "active": true,
          "closed": true,
          "archived": true,
          "new": true,
          "featured": true,
          "restricted": true,
          "isTemplate": true,
          "templateVariables": "<string>",
          "publishedAt": "<string>",
          "createdBy": "<string>",
          "updatedBy": "<string>",
          "createdAt": "2023-11-07T05:31:56Z",
          "updatedAt": "2023-11-07T05:31:56Z",
          "commentsEnabled": true,
          "imageOptimized": {
            "id": "<string>",
            "imageUrlSource": "<string>",
            "imageUrlOptimized": "<string>",
            "imageSizeKbSource": 123,
            "imageSizeKbOptimized": 123,
            "imageOptimizedComplete": true,
            "imageOptimizedLastUpdated": "<string>",
            "relID": 123,
            "field": "<string>",
            "relname": "<string>"
          },
          "iconOptimized": {
            "id": "<string>",
            "imageUrlSource": "<string>",
            "imageUrlOptimized": "<string>",
            "imageSizeKbSource": 123,
            "imageSizeKbOptimized": 123,
            "imageOptimizedComplete": true,
            "imageOptimizedLastUpdated": "<string>",
            "relID": 123,
            "field": "<string>",
            "relname": "<string>"
          },
          "headerImageOptimized": {
            "id": "<string>",
            "imageUrlSource": "<string>",
            "imageUrlOptimized": "<string>",
            "imageSizeKbSource": 123,
            "imageSizeKbOptimized": 123,
            "imageOptimizedComplete": true,
            "imageOptimizedLastUpdated": "<string>",
            "relID": 123,
            "field": "<string>",
            "relname": "<string>"
          }
        }
      ],
      "tags": [
        {
          "id": "<string>",
          "label": "<string>",
          "slug": "<string>",
          "forceShow": true,
          "publishedAt": "<string>",
          "createdBy": 123,
          "updatedBy": 123,
          "createdAt": "2023-11-07T05:31:56Z",
          "updatedAt": "2023-11-07T05:31:56Z",
          "forceHide": true,
          "isCarousel": true
        }
      ],
      "cyom": true,
      "closedTime": "2023-11-07T05:31:56Z",
      "showAllOutcomes": true,
      "showMarketImages": true,
      "automaticallyResolved": true,
      "enableNegRisk": true,
      "automaticallyActive": true,
      "eventDate": "<string>",
      "startTime": "2023-11-07T05:31:56Z",
      "eventWeek": 123,
      "seriesSlug": "<string>",
      "score": "<string>",
      "elapsed": "<string>",
      "period": "<string>",
      "live": true,
      "ended": true,
      "finishedTimestamp": "2023-11-07T05:31:56Z",
      "gmpChartMode": "<string>",
      "eventCreators": [
        {
          "id": "<string>",
          "creatorName": "<string>",
          "creatorHandle": "<string>",
          "creatorUrl": "<string>",
          "creatorImage": "<string>",
          "createdAt": "2023-11-07T05:31:56Z",
          "updatedAt": "2023-11-07T05:31:56Z"
        }
      ],
      "tweetCount": 123,
      "chats": [
        {
          "id": "<string>",
          "channelId": "<string>",
          "channelName": "<string>",
          "channelImage": "<string>",
          "live": true,
          "startTime": "2023-11-07T05:31:56Z",
          "endTime": "2023-11-07T05:31:56Z"
        }
      ],
      "featuredOrder": 123,
      "estimateValue": true,
      "cantEstimate": true,
      "estimatedValue": "<string>",
      "templates": [
        {
          "id": "<string>",
          "eventTitle": "<string>",
          "eventSlug": "<string>",
          "eventImage": "<string>",
          "marketTitle": "<string>",
          "description": "<string>",
          "resolutionSource": "<string>",
          "negRisk": true,
          "sortBy": "<string>",
          "showMarketImages": true,
          "seriesSlug": "<string>",
          "outcomes": "<string>"
        }
      ],
      "spreadsMainLine": 123,
      "totalsMainLine": 123,
      "carouselMap": "<string>",
      "pendingDeployment": true,
      "deploying": true,
      "deployingTimestamp": "2023-11-07T05:31:56Z",
      "scheduledDeploymentTimestamp": "2023-11-07T05:31:56Z",
      "gameStatus": "<string>"
    }
  ],
  "categories": [
    {
      "id": "<string>",
      "label": "<string>",
      "parentCategory": "<string>",
      "slug": "<string>",
      "publishedAt": "<string>",
      "createdBy": "<string>",
      "updatedBy": "<string>",
      "createdAt": "2023-11-07T05:31:56Z",
      "updatedAt": "2023-11-07T05:31:56Z"
    }
  ],
  "tags": [
    {
      "id": "<string>",
      "label": "<string>",
      "slug": "<string>",
      "forceShow": true,
      "publishedAt": "<string>",
      "createdBy": 123,
      "updatedBy": 123,
      "createdAt": "2023-11-07T05:31:56Z",
      "updatedAt": "2023-11-07T05:31:56Z",
      "forceHide": true,
      "isCarousel": true
    }
  ],
  "creator": "<string>",
  "ready": true,
  "funded": true,
  "pastSlugs": "<string>",
  "readyTimestamp": "2023-11-07T05:31:56Z",
  "fundedTimestamp": "2023-11-07T05:31:56Z",
  "acceptingOrdersTimestamp": "2023-11-07T05:31:56Z",
  "competitive": 123,
  "rewardsMinSize": 123,
  "rewardsMaxSpread": 123,
  "spread": 123,
  "automaticallyResolved": true,
  "oneDayPriceChange": 123,
  "oneHourPriceChange": 123,
  "oneWeekPriceChange": 123,
  "oneMonthPriceChange": 123,
  "oneYearPriceChange": 123,
  "lastTradePrice": 123,
  "bestBid": 123,
  "bestAsk": 123,
  "automaticallyActive": true,
  "clearBookOnStart": true,
  "chartColor": "<string>",
  "seriesColor": "<string>",
  "showGmpSeries": true,
  "showGmpOutcome": true,
  "manualActivation": true,
  "negRiskOther": true,
  "gameId": "<string>",
  "groupItemRange": "<string>",
  "sportsMarketType": "<string>",
  "line": 123,
  "umaResolutionStatuses": "<string>",
  "pendingDeployment": true,
  "deploying": true,
  "deployingTimestamp": "2023-11-07T05:31:56Z",
  "scheduledDeploymentTimestamp": "2023-11-07T05:31:56Z",
  "rfqEnabled": true,
  "eventStartTime": "2023-11-07T05:31:56Z"
}
Markets
Get market by slug
GET
/
markets
/
slug
/
{slug}

Try it
Path Parameters
​
slug
stringrequired
Query Parameters
​
include_tag
boolean
Response

200

application/json
Market

​
id
string
​
question
string | null
​
conditionId
string
​
slug
string | null
​
twitterCardImage
string | null
​
resolutionSource
string | null
​
endDate
string<date-time> | null
​
category
string | null
​
ammType
string | null
​
liquidity
string | null
​
sponsorName
string | null
​
sponsorImage
string | null
​
startDate
string<date-time> | null
​
xAxisValue
string | null
​
yAxisValue
string | null
​
denominationToken
string | null
​
fee
string | null
​
image
string | null
​
icon
string | null
​
lowerBound
string | null
​
upperBound
string | null
​
description
string | null
​
outcomes
string | null
​
outcomePrices
string | null
​
volume
string | null
​
active
boolean | null
​
marketType
string | null
​
formatType
string | null
​
lowerBoundDate
string | null
​
upperBoundDate
string | null
​
closed
boolean | null
​
marketMakerAddress
string
​
createdBy
integer | null
​
updatedBy
integer | null
​
createdAt
string<date-time> | null
​
updatedAt
string<date-time> | null
​
closedTime
string | null
​
wideFormat
boolean | null
​
new
boolean | null
​
mailchimpTag
string | null
​
featured
boolean | null
​
archived
boolean | null
​
resolvedBy
string | null
​
restricted
boolean | null
​
marketGroup
integer | null
​
groupItemTitle
string | null
​
groupItemThreshold
string | null
​
questionID
string | null
​
umaEndDate
string | null
​
enableOrderBook
boolean | null
​
orderPriceMinTickSize
number | null
​
orderMinSize
number | null
​
umaResolutionStatus
string | null
​
curationOrder
integer | null
​
volumeNum
number | null
​
liquidityNum
number | null
​
endDateIso
string | null
​
startDateIso
string | null
​
umaEndDateIso
string | null
​
hasReviewedDates
boolean | null
​
readyForCron
boolean | null
​
commentsEnabled
boolean | null
​
volume24hr
number | null
​
volume1wk
number | null
​
volume1mo
number | null
​
volume1yr
number | null
​
gameStartTime
string | null
​
secondsDelay
integer | null
​
clobTokenIds
string | null
​
disqusThread
string | null
​
shortOutcomes
string | null
​
teamAID
string | null
​
teamBID
string | null
​
umaBond
string | null
​
umaReward
string | null
​
fpmmLive
boolean | null
​
volume24hrAmm
number | null
​
volume1wkAmm
number | null
​
volume1moAmm
number | null
​
volume1yrAmm
number | null
​
volume24hrClob
number | null
​
volume1wkClob
number | null
​
volume1moClob
number | null
​
volume1yrClob
number | null
​
volumeAmm
number | null
​
volumeClob
number | null
​
liquidityAmm
number | null
​
liquidityClob
number | null
​
makerBaseFee
integer | null
​
takerBaseFee
integer | null
​
customLiveness
integer | null
​
acceptingOrders
boolean | null
​
notificationsEnabled
boolean | null
​
score
integer | null
​
imageOptimized
object
Show child attributes

​
iconOptimized
object
Show child attributes

​
events
object[]
Show child attributes

​
categories
object[]
Show child attributes

​
tags
object[]
Show child attributes

​
creator
string | null
​
ready
boolean | null
​
funded
boolean | null
​
pastSlugs
string | null
​
readyTimestamp
string<date-time> | null
​
fundedTimestamp
string<date-time> | null
​
acceptingOrdersTimestamp
string<date-time> | null
​
competitive
number | null
​
rewardsMinSize
number | null
​
rewardsMaxSpread
number | null
​
spread
number | null
​
automaticallyResolved
boolean | null
​
oneDayPriceChange
number | null
​
oneHourPriceChange
number | null
​
oneWeekPriceChange
number | null
​
oneMonthPriceChange
number | null
​
oneYearPriceChange
number | null
​
lastTradePrice
number | null
​
bestBid
number | null
​
bestAsk
number | null
​
automaticallyActive
boolean | null
​
clearBookOnStart
boolean | null
​
chartColor
string | null
​
seriesColor
string | null
​
showGmpSeries
boolean | null
​
showGmpOutcome
boolean | null
​
manualActivation
boolean | null
​
negRiskOther
boolean | null
​
gameId
string | null
​
groupItemRange
string | null
​
sportsMarketType
string | null
​
line
number | null
​
umaResolutionStatuses
string | null
​
pendingDeployment
boolean | null
​
deploying
boolean | null
​
deployingTimestamp
string<date-time> | null
​
scheduledDeploymentTimestamp
string<date-time> | null
​
rfqEnabled
boolean | null
​
eventStartTime
string<date-time> | null
Get market tags by id
List series
Ask a question...

github
Powered by
Get market by slug - Polymarket Documentation

Skip to main content
Polymarket Documentation home pagedark logo

Search...
Ctrl K

Ask AI
Main Site

User Guide
For Developers
Changelog
Polymarket
Discord Community
Twitter
Developer Quickstart
Developer Quickstart
Fetching Market Data
Placing Your First Order
Glossary
API Rate Limits
Endpoints
Market Makers
Market Maker Introduction
Setup
Trading
Liquidity Rewards
Maker Rebates Program
Data Feeds
Inventory Management
Polymarket Builders Program
Builder Program Introduction
Builder Tiers
Builder Profile & Keys
Order Attribution
Relayer Client
Examples
Central Limit Order Book
CLOB Introduction
Status
Quickstart
Authentication
Geographic Restrictions

Client
Methods Overview
Public Methods
L1 Methods
L2 Methods
Builder Methods

REST API

Orderbook
GET
Get order book summary
POST
Get multiple order books summaries by request

Pricing
GET
Get market price
GET
Get multiple market prices
POST
Get multiple market prices by request
GET
Get midpoint price
GET
Get price history for a traded token

Spreads
POST
Get bid-ask spreads

Historical Timeseries Data
GET
Historical Timeseries Data

Order Management
Orders Overview
Place Single Order
Place Multiple Orders (Batching)
Get Order
Get Active Orders
Check Order Reward Scoring
Cancel Orders(s)
Onchain Order Info

Trades
Trades Overview
Get Trades
Websocket
WSS Overview
WSS Quickstart
WSS Authentication
User Channel
Market Channel

Sports Websocket
Overview
Message Format
Quickstart
Real Time Data Stream
RTDS Overview
RTDS Crypto Prices
RTDS Comments
Gamma Structure
Overview
Gamma Structure
Fetching Markets
Gamma Endpoints

Gamma Status
GET
Gamma API Health check

Sports
GET
List teams
GET
Get sports metadata information
GET
Get valid sports market types

Tags
GET
List tags
GET
Get tag by id
GET
Get tag by slug
GET
Get related tags (relationships) by tag id
GET
Get related tags (relationships) by tag slug
GET
Get tags related to a tag id
GET
Get tags related to a tag slug

Events
GET
List events
GET
Get event by id
GET
Get event tags
GET
Get event by slug

Markets
GET
List markets
GET
Get market by id
GET
Get market tags by id
GET
Get market by slug

Series
GET
List series
GET
Get series by id

Comments

Profiles

Search
Data-API

Data API Status

Core

Misc

Builders
Bridge & Swap
Overview

Bridge
Subgraph
Overview
Resolution
Resolution
Conditional Token Frameworks
Overview
Splitting USDC
Merging Tokens
Reedeeming Tokens
Deployment and Additional Information
Proxy Wallets
Proxy wallet
Negative Risk
Overview
List series

curl --request GET \
  --url https://gamma-api.polymarket.com/series

200
[
  {
    "id": "<string>",
    "ticker": "<string>",
    "slug": "<string>",
    "title": "<string>",
    "subtitle": "<string>",
    "seriesType": "<string>",
    "recurrence": "<string>",
    "description": "<string>",
    "image": "<string>",
    "icon": "<string>",
    "layout": "<string>",
    "active": true,
    "closed": true,
    "archived": true,
    "new": true,
    "featured": true,
    "restricted": true,
    "isTemplate": true,
    "templateVariables": true,
    "publishedAt": "<string>",
    "createdBy": "<string>",
    "updatedBy": "<string>",
    "createdAt": "2023-11-07T05:31:56Z",
    "updatedAt": "2023-11-07T05:31:56Z",
    "commentsEnabled": true,
    "competitive": "<string>",
    "volume24hr": 123,
    "volume": 123,
    "liquidity": 123,
    "startDate": "2023-11-07T05:31:56Z",
    "pythTokenID": "<string>",
    "cgAssetName": "<string>",
    "score": 123,
    "events": [
      {
        "id": "<string>",
        "ticker": "<string>",
        "slug": "<string>",
        "title": "<string>",
        "subtitle": "<string>",
        "description": "<string>",
        "resolutionSource": "<string>",
        "startDate": "2023-11-07T05:31:56Z",
        "creationDate": "2023-11-07T05:31:56Z",
        "endDate": "2023-11-07T05:31:56Z",
        "image": "<string>",
        "icon": "<string>",
        "active": true,
        "closed": true,
        "archived": true,
        "new": true,
        "featured": true,
        "restricted": true,
        "liquidity": 123,
        "volume": 123,
        "openInterest": 123,
        "sortBy": "<string>",
        "category": "<string>",
        "subcategory": "<string>",
        "isTemplate": true,
        "templateVariables": "<string>",
        "published_at": "<string>",
        "createdBy": "<string>",
        "updatedBy": "<string>",
        "createdAt": "2023-11-07T05:31:56Z",
        "updatedAt": "2023-11-07T05:31:56Z",
        "commentsEnabled": true,
        "competitive": 123,
        "volume24hr": 123,
        "volume1wk": 123,
        "volume1mo": 123,
        "volume1yr": 123,
        "featuredImage": "<string>",
        "disqusThread": "<string>",
        "parentEvent": "<string>",
        "enableOrderBook": true,
        "liquidityAmm": 123,
        "liquidityClob": 123,
        "negRisk": true,
        "negRiskMarketID": "<string>",
        "negRiskFeeBips": 123,
        "commentCount": 123,
        "imageOptimized": {
          "id": "<string>",
          "imageUrlSource": "<string>",
          "imageUrlOptimized": "<string>",
          "imageSizeKbSource": 123,
          "imageSizeKbOptimized": 123,
          "imageOptimizedComplete": true,
          "imageOptimizedLastUpdated": "<string>",
          "relID": 123,
          "field": "<string>",
          "relname": "<string>"
        },
        "iconOptimized": {
          "id": "<string>",
          "imageUrlSource": "<string>",
          "imageUrlOptimized": "<string>",
          "imageSizeKbSource": 123,
          "imageSizeKbOptimized": 123,
          "imageOptimizedComplete": true,
          "imageOptimizedLastUpdated": "<string>",
          "relID": 123,
          "field": "<string>",
          "relname": "<string>"
        },
        "featuredImageOptimized": {
          "id": "<string>",
          "imageUrlSource": "<string>",
          "imageUrlOptimized": "<string>",
          "imageSizeKbSource": 123,
          "imageSizeKbOptimized": 123,
          "imageOptimizedComplete": true,
          "imageOptimizedLastUpdated": "<string>",
          "relID": 123,
          "field": "<string>",
          "relname": "<string>"
        },
        "subEvents": [
          "<string>"
        ],
        "markets": [
          {
            "id": "<string>",
            "question": "<string>",
            "conditionId": "<string>",
            "slug": "<string>",
            "twitterCardImage": "<string>",
            "resolutionSource": "<string>",
            "endDate": "2023-11-07T05:31:56Z",
            "category": "<string>",
            "ammType": "<string>",
            "liquidity": "<string>",
            "sponsorName": "<string>",
            "sponsorImage": "<string>",
            "startDate": "2023-11-07T05:31:56Z",
            "xAxisValue": "<string>",
            "yAxisValue": "<string>",
            "denominationToken": "<string>",
            "fee": "<string>",
            "image": "<string>",
            "icon": "<string>",
            "lowerBound": "<string>",
            "upperBound": "<string>",
            "description": "<string>",
            "outcomes": "<string>",
            "outcomePrices": "<string>",
            "volume": "<string>",
            "active": true,
            "marketType": "<string>",
            "formatType": "<string>",
            "lowerBoundDate": "<string>",
            "upperBoundDate": "<string>",
            "closed": true,
            "marketMakerAddress": "<string>",
            "createdBy": 123,
            "updatedBy": 123,
            "createdAt": "2023-11-07T05:31:56Z",
            "updatedAt": "2023-11-07T05:31:56Z",
            "closedTime": "<string>",
            "wideFormat": true,
            "new": true,
            "mailchimpTag": "<string>",
            "featured": true,
            "archived": true,
            "resolvedBy": "<string>",
            "restricted": true,
            "marketGroup": 123,
            "groupItemTitle": "<string>",
            "groupItemThreshold": "<string>",
            "questionID": "<string>",
            "umaEndDate": "<string>",
            "enableOrderBook": true,
            "orderPriceMinTickSize": 123,
            "orderMinSize": 123,
            "umaResolutionStatus": "<string>",
            "curationOrder": 123,
            "volumeNum": 123,
            "liquidityNum": 123,
            "endDateIso": "<string>",
            "startDateIso": "<string>",
            "umaEndDateIso": "<string>",
            "hasReviewedDates": true,
            "readyForCron": true,
            "commentsEnabled": true,
            "volume24hr": 123,
            "volume1wk": 123,
            "volume1mo": 123,
            "volume1yr": 123,
            "gameStartTime": "<string>",
            "secondsDelay": 123,
            "clobTokenIds": "<string>",
            "disqusThread": "<string>",
            "shortOutcomes": "<string>",
            "teamAID": "<string>",
            "teamBID": "<string>",
            "umaBond": "<string>",
            "umaReward": "<string>",
            "fpmmLive": true,
            "volume24hrAmm": 123,
            "volume1wkAmm": 123,
            "volume1moAmm": 123,
            "volume1yrAmm": 123,
            "volume24hrClob": 123,
            "volume1wkClob": 123,
            "volume1moClob": 123,
            "volume1yrClob": 123,
            "volumeAmm": 123,
            "volumeClob": 123,
            "liquidityAmm": 123,
            "liquidityClob": 123,
            "makerBaseFee": 123,
            "takerBaseFee": 123,
            "customLiveness": 123,
            "acceptingOrders": true,
            "notificationsEnabled": true,
            "score": 123,
            "imageOptimized": {
              "id": "<string>",
              "imageUrlSource": "<string>",
              "imageUrlOptimized": "<string>",
              "imageSizeKbSource": 123,
              "imageSizeKbOptimized": 123,
              "imageOptimizedComplete": true,
              "imageOptimizedLastUpdated": "<string>",
              "relID": 123,
              "field": "<string>",
              "relname": "<string>"
            },
            "iconOptimized": {
              "id": "<string>",
              "imageUrlSource": "<string>",
              "imageUrlOptimized": "<string>",
              "imageSizeKbSource": 123,
              "imageSizeKbOptimized": 123,
              "imageOptimizedComplete": true,
              "imageOptimizedLastUpdated": "<string>",
              "relID": 123,
              "field": "<string>",
              "relname": "<string>"
            },
            "events": "<array>",
            "categories": [
              {
                "id": "<string>",
                "label": "<string>",
                "parentCategory": "<string>",
                "slug": "<string>",
                "publishedAt": "<string>",
                "createdBy": "<string>",
                "updatedBy": "<string>",
                "createdAt": "2023-11-07T05:31:56Z",
                "updatedAt": "2023-11-07T05:31:56Z"
              }
            ],
            "tags": [
              {
                "id": "<string>",
                "label": "<string>",
                "slug": "<string>",
                "forceShow": true,
                "publishedAt": "<string>",
                "createdBy": 123,
                "updatedBy": 123,
                "createdAt": "2023-11-07T05:31:56Z",
                "updatedAt": "2023-11-07T05:31:56Z",
                "forceHide": true,
                "isCarousel": true
              }
            ],
            "creator": "<string>",
            "ready": true,
            "funded": true,
            "pastSlugs": "<string>",
            "readyTimestamp": "2023-11-07T05:31:56Z",
            "fundedTimestamp": "2023-11-07T05:31:56Z",
            "acceptingOrdersTimestamp": "2023-11-07T05:31:56Z",
            "competitive": 123,
            "rewardsMinSize": 123,
            "rewardsMaxSpread": 123,
            "spread": 123,
            "automaticallyResolved": true,
            "oneDayPriceChange": 123,
            "oneHourPriceChange": 123,
            "oneWeekPriceChange": 123,
            "oneMonthPriceChange": 123,
            "oneYearPriceChange": 123,
            "lastTradePrice": 123,
            "bestBid": 123,
            "bestAsk": 123,
            "automaticallyActive": true,
            "clearBookOnStart": true,
            "chartColor": "<string>",
            "seriesColor": "<string>",
            "showGmpSeries": true,
            "showGmpOutcome": true,
            "manualActivation": true,
            "negRiskOther": true,
            "gameId": "<string>",
            "groupItemRange": "<string>",
            "sportsMarketType": "<string>",
            "line": 123,
            "umaResolutionStatuses": "<string>",
            "pendingDeployment": true,
            "deploying": true,
            "deployingTimestamp": "2023-11-07T05:31:56Z",
            "scheduledDeploymentTimestamp": "2023-11-07T05:31:56Z",
            "rfqEnabled": true,
            "eventStartTime": "2023-11-07T05:31:56Z"
          }
        ],
        "series": "<array>",
        "categories": [
          {
            "id": "<string>",
            "label": "<string>",
            "parentCategory": "<string>",
            "slug": "<string>",
            "publishedAt": "<string>",
            "createdBy": "<string>",
            "updatedBy": "<string>",
            "createdAt": "2023-11-07T05:31:56Z",
            "updatedAt": "2023-11-07T05:31:56Z"
          }
        ],
        "collections": [
          {
            "id": "<string>",
            "ticker": "<string>",
            "slug": "<string>",
            "title": "<string>",
            "subtitle": "<string>",
            "collectionType": "<string>",
            "description": "<string>",
            "tags": "<string>",
            "image": "<string>",
            "icon": "<string>",
            "headerImage": "<string>",
            "layout": "<string>",
            "active": true,
            "closed": true,
            "archived": true,
            "new": true,
            "featured": true,
            "restricted": true,
            "isTemplate": true,
            "templateVariables": "<string>",
            "publishedAt": "<string>",
            "createdBy": "<string>",
            "updatedBy": "<string>",
            "createdAt": "2023-11-07T05:31:56Z",
            "updatedAt": "2023-11-07T05:31:56Z",
            "commentsEnabled": true,
            "imageOptimized": {
              "id": "<string>",
              "imageUrlSource": "<string>",
              "imageUrlOptimized": "<string>",
              "imageSizeKbSource": 123,
              "imageSizeKbOptimized": 123,
              "imageOptimizedComplete": true,
              "imageOptimizedLastUpdated": "<string>",
              "relID": 123,
              "field": "<string>",
              "relname": "<string>"
            },
            "iconOptimized": {
              "id": "<string>",
              "imageUrlSource": "<string>",
              "imageUrlOptimized": "<string>",
              "imageSizeKbSource": 123,
              "imageSizeKbOptimized": 123,
              "imageOptimizedComplete": true,
              "imageOptimizedLastUpdated": "<string>",
              "relID": 123,
              "field": "<string>",
              "relname": "<string>"
            },
            "headerImageOptimized": {
              "id": "<string>",
              "imageUrlSource": "<string>",
              "imageUrlOptimized": "<string>",
              "imageSizeKbSource": 123,
              "imageSizeKbOptimized": 123,
              "imageOptimizedComplete": true,
              "imageOptimizedLastUpdated": "<string>",
              "relID": 123,
              "field": "<string>",
              "relname": "<string>"
            }
          }
        ],
        "tags": [
          {
            "id": "<string>",
            "label": "<string>",
            "slug": "<string>",
            "forceShow": true,
            "publishedAt": "<string>",
            "createdBy": 123,
            "updatedBy": 123,
            "createdAt": "2023-11-07T05:31:56Z",
            "updatedAt": "2023-11-07T05:31:56Z",
            "forceHide": true,
            "isCarousel": true
          }
        ],
        "cyom": true,
        "closedTime": "2023-11-07T05:31:56Z",
        "showAllOutcomes": true,
        "showMarketImages": true,
        "automaticallyResolved": true,
        "enableNegRisk": true,
        "automaticallyActive": true,
        "eventDate": "<string>",
        "startTime": "2023-11-07T05:31:56Z",
        "eventWeek": 123,
        "seriesSlug": "<string>",
        "score": "<string>",
        "elapsed": "<string>",
        "period": "<string>",
        "live": true,
        "ended": true,
        "finishedTimestamp": "2023-11-07T05:31:56Z",
        "gmpChartMode": "<string>",
        "eventCreators": [
          {
            "id": "<string>",
            "creatorName": "<string>",
            "creatorHandle": "<string>",
            "creatorUrl": "<string>",
            "creatorImage": "<string>",
            "createdAt": "2023-11-07T05:31:56Z",
            "updatedAt": "2023-11-07T05:31:56Z"
          }
        ],
        "tweetCount": 123,
        "chats": [
          {
            "id": "<string>",
            "channelId": "<string>",
            "channelName": "<string>",
            "channelImage": "<string>",
            "live": true,
            "startTime": "2023-11-07T05:31:56Z",
            "endTime": "2023-11-07T05:31:56Z"
          }
        ],
        "featuredOrder": 123,
        "estimateValue": true,
        "cantEstimate": true,
        "estimatedValue": "<string>",
        "templates": [
          {
            "id": "<string>",
            "eventTitle": "<string>",
            "eventSlug": "<string>",
            "eventImage": "<string>",
            "marketTitle": "<string>",
            "description": "<string>",
            "resolutionSource": "<string>",
            "negRisk": true,
            "sortBy": "<string>",
            "showMarketImages": true,
            "seriesSlug": "<string>",
            "outcomes": "<string>"
          }
        ],
        "spreadsMainLine": 123,
        "totalsMainLine": 123,
        "carouselMap": "<string>",
        "pendingDeployment": true,
        "deploying": true,
        "deployingTimestamp": "2023-11-07T05:31:56Z",
        "scheduledDeploymentTimestamp": "2023-11-07T05:31:56Z",
        "gameStatus": "<string>"
      }
    ],
    "collections": [
      {
        "id": "<string>",
        "ticker": "<string>",
        "slug": "<string>",
        "title": "<string>",
        "subtitle": "<string>",
        "collectionType": "<string>",
        "description": "<string>",
        "tags": "<string>",
        "image": "<string>",
        "icon": "<string>",
        "headerImage": "<string>",
        "layout": "<string>",
        "active": true,
        "closed": true,
        "archived": true,
        "new": true,
        "featured": true,
        "restricted": true,
        "isTemplate": true,
        "templateVariables": "<string>",
        "publishedAt": "<string>",
        "createdBy": "<string>",
        "updatedBy": "<string>",
        "createdAt": "2023-11-07T05:31:56Z",
        "updatedAt": "2023-11-07T05:31:56Z",
        "commentsEnabled": true,
        "imageOptimized": {
          "id": "<string>",
          "imageUrlSource": "<string>",
          "imageUrlOptimized": "<string>",
          "imageSizeKbSource": 123,
          "imageSizeKbOptimized": 123,
          "imageOptimizedComplete": true,
          "imageOptimizedLastUpdated": "<string>",
          "relID": 123,
          "field": "<string>",
          "relname": "<string>"
        },
        "iconOptimized": {
          "id": "<string>",
          "imageUrlSource": "<string>",
          "imageUrlOptimized": "<string>",
          "imageSizeKbSource": 123,
          "imageSizeKbOptimized": 123,
          "imageOptimizedComplete": true,
          "imageOptimizedLastUpdated": "<string>",
          "relID": 123,
          "field": "<string>",
          "relname": "<string>"
        },
        "headerImageOptimized": {
          "id": "<string>",
          "imageUrlSource": "<string>",
          "imageUrlOptimized": "<string>",
          "imageSizeKbSource": 123,
          "imageSizeKbOptimized": 123,
          "imageOptimizedComplete": true,
          "imageOptimizedLastUpdated": "<string>",
          "relID": 123,
          "field": "<string>",
          "relname": "<string>"
        }
      }
    ],
    "categories": [
      {
        "id": "<string>",
        "label": "<string>",
        "parentCategory": "<string>",
        "slug": "<string>",
        "publishedAt": "<string>",
        "createdBy": "<string>",
        "updatedBy": "<string>",
        "createdAt": "2023-11-07T05:31:56Z",
        "updatedAt": "2023-11-07T05:31:56Z"
      }
    ],
    "tags": [
      {
        "id": "<string>",
        "label": "<string>",
        "slug": "<string>",
        "forceShow": true,
        "publishedAt": "<string>",
        "createdBy": 123,
        "updatedBy": 123,
        "createdAt": "2023-11-07T05:31:56Z",
        "updatedAt": "2023-11-07T05:31:56Z",
        "forceHide": true,
        "isCarousel": true
      }
    ],
    "commentCount": 123,
    "chats": [
      {
        "id": "<string>",
        "channelId": "<string>",
        "channelName": "<string>",
        "channelImage": "<string>",
        "live": true,
        "startTime": "2023-11-07T05:31:56Z",
        "endTime": "2023-11-07T05:31:56Z"
      }
    ]
  }
]
Series
List series
GET
/
series

Try it
Query Parameters
​
limit
integer
Required range: x >= 0
​
offset
integer
Required range: x >= 0
​
order
string
Comma-separated list of fields to order by

​
ascending
boolean
​
slug
string[]
​
categories_ids
integer[]
​
categories_labels
string[]
​
closed
boolean
​
include_chat
boolean
​
recurrence
string
Response
200 - application/json
List of series

​
id
string
​
ticker
string | null
​
slug
string | null
​
title
string | null
​
subtitle
string | null
​
seriesType
string | null
​
recurrence
string | null
​
description
string | null
​
image
string | null
​
icon
string | null
​
layout
string | null
​
active
boolean | null
​
closed
boolean | null
​
archived
boolean | null
​
new
boolean | null
​
featured
boolean | null
​
restricted
boolean | null
​
isTemplate
boolean | null
​
templateVariables
boolean | null
​
publishedAt
string | null
​
createdBy
string | null
​
updatedBy
string | null
​
createdAt
string<date-time> | null
​
updatedAt
string<date-time> | null
​
commentsEnabled
boolean | null
​
competitive
string | null
​
volume24hr
number | null
​
volume
number | null
​
liquidity
number | null
​
startDate
string<date-time> | null
​
pythTokenID
string | null
​
cgAssetName
string | null
​
score
integer | null
​
events
object[]
Show child attributes

​
collections
object[]
Show child attributes

​
categories
object[]
Show child attributes

​
tags
object[]
Show child attributes

​
commentCount
integer | null
​
chats
object[]
Show child attributes

Get market by slug
Get series by id
Ask a question...

github
Powered by
List series - Polymarket Documentation

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.polymarket.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get series by id



## OpenAPI

````yaml api-reference/gamma-openapi.json get /series/{id}
openapi: 3.0.3
info:
  title: Markets API
  version: 1.0.0
  description: REST API specification for public endpoints used by the Markets service.
servers:
  - url: https://gamma-api.polymarket.com
    description: Polymarket Gamma API Production Server
security: []
tags:
  - name: Gamma Status
    description: Gamma API status and health check
  - name: Sports
    description: Sports-related endpoints including teams and game data
  - name: Tags
    description: Tag management and related tag operations
  - name: Events
    description: Event management and event-related operations
  - name: Markets
    description: Market data and market-related operations
  - name: Comments
    description: Comment system and user interactions
  - name: Series
    description: Series management and related operations
  - name: Profiles
    description: User profile management
  - name: Search
    description: Search functionality across different entity types
paths:
  /series/{id}:
    get:
      tags:
        - Series
      summary: Get series by id
      operationId: getSeries
      parameters:
        - $ref: '#/components/parameters/pathId'
        - name: include_chat
          in: query
          schema:
            type: boolean
      responses:
        '200':
          description: Series
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Series'
        '404':
          description: Not found
components:
  parameters:
    pathId:
      name: id
      in: path
      required: true
      schema:
        type: integer
  schemas:
    Series:
      type: object
      properties:
        id:
          type: string
        ticker:
          type: string
          nullable: true
        slug:
          type: string
          nullable: true
        title:
          type: string
          nullable: true
        subtitle:
          type: string
          nullable: true
        seriesType:
          type: string
          nullable: true
        recurrence:
          type: string
          nullable: true
        description:
          type: string
          nullable: true
        image:
          type: string
          nullable: true
        icon:
          type: string
          nullable: true
        layout:
          type: string
          nullable: true
        active:
          type: boolean
          nullable: true
        closed:
          type: boolean
          nullable: true
        archived:
          type: boolean
          nullable: true
        new:
          type: boolean
          nullable: true
        featured:
          type: boolean
          nullable: true
        restricted:
          type: boolean
          nullable: true
        isTemplate:
          type: boolean
          nullable: true
        templateVariables:
          type: boolean
          nullable: true
        publishedAt:
          type: string
          nullable: true
        createdBy:
          type: string
          nullable: true
        updatedBy:
          type: string
          nullable: true
        createdAt:
          type: string
          format: date-time
          nullable: true
        updatedAt:
          type: string
          format: date-time
          nullable: true
        commentsEnabled:
          type: boolean
          nullable: true
        competitive:
          type: string
          nullable: true
        volume24hr:
          type: number
          nullable: true
        volume:
          type: number
          nullable: true
        liquidity:
          type: number
          nullable: true
        startDate:
          type: string
          format: date-time
          nullable: true
        pythTokenID:
          type: string
          nullable: true
        cgAssetName:
          type: string
          nullable: true
        score:
          type: integer
          nullable: true
        events:
          type: array
          items:
            $ref: '#/components/schemas/Event'
        collections:
          type: array
          items:
            $ref: '#/components/schemas/Collection'
        categories:
          type: array
          items:
            $ref: '#/components/schemas/Category'
        tags:
          type: array
          items:
            $ref: '#/components/schemas/Tag'
        commentCount:
          type: integer
          nullable: true
        chats:
          type: array
          items:
            $ref: '#/components/schemas/Chat'
    Event:
      type: object
      properties:
        id:
          type: string
        ticker:
          type: string
          nullable: true
        slug:
          type: string
          nullable: true
        title:
          type: string
          nullable: true
        subtitle:
          type: string
          nullable: true
        description:
          type: string
          nullable: true
        resolutionSource:
          type: string
          nullable: true
        startDate:
          type: string
          format: date-time
          nullable: true
        creationDate:
          type: string
          format: date-time
          nullable: true
        endDate:
          type: string
          format: date-time
          nullable: true
        image:
          type: string
          nullable: true
        icon:
          type: string
          nullable: true
        active:
          type: boolean
          nullable: true
        closed:
          type: boolean
          nullable: true
        archived:
          type: boolean
          nullable: true
        new:
          type: boolean
          nullable: true
        featured:
          type: boolean
          nullable: true
        restricted:
          type: boolean
          nullable: true
        liquidity:
          type: number
          nullable: true
        volume:
          type: number
          nullable: true
        openInterest:
          type: number
          nullable: true
        sortBy:
          type: string
          nullable: true
        category:
          type: string
          nullable: true
        subcategory:
          type: string
          nullable: true
        isTemplate:
          type: boolean
          nullable: true
        templateVariables:
          type: string
          nullable: true
        published_at:
          type: string
          nullable: true
        createdBy:
          type: string
          nullable: true
        updatedBy:
          type: string
          nullable: true
        createdAt:
          type: string
          format: date-time
          nullable: true
        updatedAt:
          type: string
          format: date-time
          nullable: true
        commentsEnabled:
          type: boolean
          nullable: true
        competitive:
          type: number
          nullable: true
        volume24hr:
          type: number
          nullable: true
        volume1wk:
          type: number
          nullable: true
        volume1mo:
          type: number
          nullable: true
        volume1yr:
          type: number
          nullable: true
        featuredImage:
          type: string
          nullable: true
        disqusThread:
          type: string
          nullable: true
        parentEvent:
          type: string
          nullable: true
        enableOrderBook:
          type: boolean
          nullable: true
        liquidityAmm:
          type: number
          nullable: true
        liquidityClob:
          type: number
          nullable: true
        negRisk:
          type: boolean
          nullable: true
        negRiskMarketID:
          type: string
          nullable: true
        negRiskFeeBips:
          type: integer
          nullable: true
        commentCount:
          type: integer
          nullable: true
        imageOptimized:
          $ref: '#/components/schemas/ImageOptimization'
        iconOptimized:
          $ref: '#/components/schemas/ImageOptimization'
        featuredImageOptimized:
          $ref: '#/components/schemas/ImageOptimization'
        subEvents:
          type: array
          items:
            type: string
          nullable: true
        markets:
          type: array
          items:
            $ref: '#/components/schemas/Market'
        series:
          type: array
          items:
            $ref: '#/components/schemas/Series'
        categories:
          type: array
          items:
            $ref: '#/components/schemas/Category'
        collections:
          type: array
          items:
            $ref: '#/components/schemas/Collection'
        tags:
          type: array
          items:
            $ref: '#/components/schemas/Tag'
        cyom:
          type: boolean
          nullable: true
        closedTime:
          type: string
          format: date-time
          nullable: true
        showAllOutcomes:
          type: boolean
          nullable: true
        showMarketImages:
          type: boolean
          nullable: true
        automaticallyResolved:
          type: boolean
          nullable: true
        enableNegRisk:
          type: boolean
          nullable: true
        automaticallyActive:
          type: boolean
          nullable: true
        eventDate:
          type: string
          nullable: true
        startTime:
          type: string
          format: date-time
          nullable: true
        eventWeek:
          type: integer
          nullable: true
        seriesSlug:
          type: string
          nullable: true
        score:
          type: string
          nullable: true
        elapsed:
          type: string
          nullable: true
        period:
          type: string
          nullable: true
        live:
          type: boolean
          nullable: true
        ended:
          type: boolean
          nullable: true
        finishedTimestamp:
          type: string
          format: date-time
          nullable: true
        gmpChartMode:
          type: string
          nullable: true
        eventCreators:
          type: array
          items:
            $ref: '#/components/schemas/EventCreator'
        tweetCount:
          type: integer
          nullable: true
        chats:
          type: array
          items:
            $ref: '#/components/schemas/Chat'
        featuredOrder:
          type: integer
          nullable: true
        estimateValue:
          type: boolean
          nullable: true
        cantEstimate:
          type: boolean
          nullable: true
        estimatedValue:
          type: string
          nullable: true
        templates:
          type: array
          items:
            $ref: '#/components/schemas/Template'
        spreadsMainLine:
          type: number
          nullable: true
        totalsMainLine:
          type: number
          nullable: true
        carouselMap:
          type: string
          nullable: true
        pendingDeployment:
          type: boolean
          nullable: true
        deploying:
          type: boolean
          nullable: true
        deployingTimestamp:
          type: string
          format: date-time
          nullable: true
        scheduledDeploymentTimestamp:
          type: string
          format: date-time
          nullable: true
        gameStatus:
          type: string
          nullable: true
    Collection:
      type: object
      properties:
        id:
          type: string
        ticker:
          type: string
          nullable: true
        slug:
          type: string
          nullable: true
        title:
          type: string
          nullable: true
        subtitle:
          type: string
          nullable: true
        collectionType:
          type: string
          nullable: true
        description:
          type: string
          nullable: true
        tags:
          type: string
          nullable: true
        image:
          type: string
          nullable: true
        icon:
          type: string
          nullable: true
        headerImage:
          type: string
          nullable: true
        layout:
          type: string
          nullable: true
        active:
          type: boolean
          nullable: true
        closed:
          type: boolean
          nullable: true
        archived:
          type: boolean
          nullable: true
        new:
          type: boolean
          nullable: true
        featured:
          type: boolean
          nullable: true
        restricted:
          type: boolean
          nullable: true
        isTemplate:
          type: boolean
          nullable: true
        templateVariables:
          type: string
          nullable: true
        publishedAt:
          type: string
          nullable: true
        createdBy:
          type: string
          nullable: true
        updatedBy:
          type: string
          nullable: true
        createdAt:
          type: string
          format: date-time
          nullable: true
        updatedAt:
          type: string
          format: date-time
          nullable: true
        commentsEnabled:
          type: boolean
          nullable: true
        imageOptimized:
          $ref: '#/components/schemas/ImageOptimization'
        iconOptimized:
          $ref: '#/components/schemas/ImageOptimization'
        headerImageOptimized:
          $ref: '#/components/schemas/ImageOptimization'
    Category:
      type: object
      properties:
        id:
          type: string
        label:
          type: string
          nullable: true
        parentCategory:
          type: string
          nullable: true
        slug:
          type: string
          nullable: true
        publishedAt:
          type: string
          nullable: true
        createdBy:
          type: string
          nullable: true
        updatedBy:
          type: string
          nullable: true
        createdAt:
          type: string
          format: date-time
          nullable: true
        updatedAt:
          type: string
          format: date-time
          nullable: true
    Tag:
      type: object
      properties:
        id:
          type: string
        label:
          type: string
          nullable: true
        slug:
          type: string
          nullable: true
        forceShow:
          type: boolean
          nullable: true
        publishedAt:
          type: string
          nullable: true
        createdBy:
          type: integer
          nullable: true
        updatedBy:
          type: integer
          nullable: true
        createdAt:
          type: string
          format: date-time
          nullable: true
        updatedAt:
          type: string
          format: date-time
          nullable: true
        forceHide:
          type: boolean
          nullable: true
        isCarousel:
          type: boolean
          nullable: true
    Chat:
      type: object
      properties:
        id:
          type: string
        channelId:
          type: string
          nullable: true
        channelName:
          type: string
          nullable: true
        channelImage:
          type: string
          nullable: true
        live:
          type: boolean
          nullable: true
        startTime:
          type: string
          format: date-time
          nullable: true
        endTime:
          type: string
          format: date-time
          nullable: true
    ImageOptimization:
      type: object
      properties:
        id:
          type: string
        imageUrlSource:
          type: string
          nullable: true
        imageUrlOptimized:
          type: string
          nullable: true
        imageSizeKbSource:
          type: number
          nullable: true
        imageSizeKbOptimized:
          type: number
          nullable: true
        imageOptimizedComplete:
          type: boolean
          nullable: true
        imageOptimizedLastUpdated:
          type: string
          nullable: true
        relID:
          type: integer
          nullable: true
        field:
          type: string
          nullable: true
        relname:
          type: string
          nullable: true
    Market:
      type: object
      properties:
        id:
          type: string
        question:
          type: string
          nullable: true
        conditionId:
          type: string
        slug:
          type: string
          nullable: true
        twitterCardImage:
          type: string
          nullable: true
        resolutionSource:
          type: string
          nullable: true
        endDate:
          type: string
          format: date-time
          nullable: true
        category:
          type: string
          nullable: true
        ammType:
          type: string
          nullable: true
        liquidity:
          type: string
          nullable: true
        sponsorName:
          type: string
          nullable: true
        sponsorImage:
          type: string
          nullable: true
        startDate:
          type: string
          format: date-time
          nullable: true
        xAxisValue:
          type: string
          nullable: true
        yAxisValue:
          type: string
          nullable: true
        denominationToken:
          type: string
          nullable: true
        fee:
          type: string
          nullable: true
        image:
          type: string
          nullable: true
        icon:
          type: string
          nullable: true
        lowerBound:
          type: string
          nullable: true
        upperBound:
          type: string
          nullable: true
        description:
          type: string
          nullable: true
        outcomes:
          type: string
          nullable: true
        outcomePrices:
          type: string
          nullable: true
        volume:
          type: string
          nullable: true
        active:
          type: boolean
          nullable: true
        marketType:
          type: string
          nullable: true
        formatType:
          type: string
          nullable: true
        lowerBoundDate:
          type: string
          nullable: true
        upperBoundDate:
          type: string
          nullable: true
        closed:
          type: boolean
          nullable: true
        marketMakerAddress:
          type: string
        createdBy:
          type: integer
          nullable: true
        updatedBy:
          type: integer
          nullable: true
        createdAt:
          type: string
          format: date-time
          nullable: true
        updatedAt:
          type: string
          format: date-time
          nullable: true
        closedTime:
          type: string
          nullable: true
        wideFormat:
          type: boolean
          nullable: true
        new:
          type: boolean
          nullable: true
        mailchimpTag:
          type: string
          nullable: true
        featured:
          type: boolean
          nullable: true
        archived:
          type: boolean
          nullable: true
        resolvedBy:
          type: string
          nullable: true
        restricted:
          type: boolean
          nullable: true
        marketGroup:
          type: integer
          nullable: true
        groupItemTitle:
          type: string
          nullable: true
        groupItemThreshold:
          type: string
          nullable: true
        questionID:
          type: string
          nullable: true
        umaEndDate:
          type: string
          nullable: true
        enableOrderBook:
          type: boolean
          nullable: true
        orderPriceMinTickSize:
          type: number
          nullable: true
        orderMinSize:
          type: number
          nullable: true
        umaResolutionStatus:
          type: string
          nullable: true
        curationOrder:
          type: integer
          nullable: true
        volumeNum:
          type: number
          nullable: true
        liquidityNum:
          type: number
          nullable: true
        endDateIso:
          type: string
          nullable: true
        startDateIso:
          type: string
          nullable: true
        umaEndDateIso:
          type: string
          nullable: true
        hasReviewedDates:
          type: boolean
          nullable: true
        readyForCron:
          type: boolean
          nullable: true
        commentsEnabled:
          type: boolean
          nullable: true
        volume24hr:
          type: number
          nullable: true
        volume1wk:
          type: number
          nullable: true
        volume1mo:
          type: number
          nullable: true
        volume1yr:
          type: number
          nullable: true
        gameStartTime:
          type: string
          nullable: true
        secondsDelay:
          type: integer
          nullable: true
        clobTokenIds:
          type: string
          nullable: true
        disqusThread:
          type: string
          nullable: true
        shortOutcomes:
          type: string
          nullable: true
        teamAID:
          type: string
          nullable: true
        teamBID:
          type: string
          nullable: true
        umaBond:
          type: string
          nullable: true
        umaReward:
          type: string
          nullable: true
        fpmmLive:
          type: boolean
          nullable: true
        volume24hrAmm:
          type: number
          nullable: true
        volume1wkAmm:
          type: number
          nullable: true
        volume1moAmm:
          type: number
          nullable: true
        volume1yrAmm:
          type: number
          nullable: true
        volume24hrClob:
          type: number
          nullable: true
        volume1wkClob:
          type: number
          nullable: true
        volume1moClob:
          type: number
          nullable: true
        volume1yrClob:
          type: number
          nullable: true
        volumeAmm:
          type: number
          nullable: true
        volumeClob:
          type: number
          nullable: true
        liquidityAmm:
          type: number
          nullable: true
        liquidityClob:
          type: number
          nullable: true
        makerBaseFee:
          type: integer
          nullable: true
        takerBaseFee:
          type: integer
          nullable: true
        customLiveness:
          type: integer
          nullable: true
        acceptingOrders:
          type: boolean
          nullable: true
        notificationsEnabled:
          type: boolean
          nullable: true
        score:
          type: integer
          nullable: true
        imageOptimized:
          $ref: '#/components/schemas/ImageOptimization'
        iconOptimized:
          $ref: '#/components/schemas/ImageOptimization'
        events:
          type: array
          items:
            $ref: '#/components/schemas/Event'
        categories:
          type: array
          items:
            $ref: '#/components/schemas/Category'
        tags:
          type: array
          items:
            $ref: '#/components/schemas/Tag'
        creator:
          type: string
          nullable: true
        ready:
          type: boolean
          nullable: true
        funded:
          type: boolean
          nullable: true
        pastSlugs:
          type: string
          nullable: true
        readyTimestamp:
          type: string
          format: date-time
          nullable: true
        fundedTimestamp:
          type: string
          format: date-time
          nullable: true
        acceptingOrdersTimestamp:
          type: string
          format: date-time
          nullable: true
        competitive:
          type: number
          nullable: true
        rewardsMinSize:
          type: number
          nullable: true
        rewardsMaxSpread:
          type: number
          nullable: true
        spread:
          type: number
          nullable: true
        automaticallyResolved:
          type: boolean
          nullable: true
        oneDayPriceChange:
          type: number
          nullable: true
        oneHourPriceChange:
          type: number
          nullable: true
        oneWeekPriceChange:
          type: number
          nullable: true
        oneMonthPriceChange:
          type: number
          nullable: true
        oneYearPriceChange:
          type: number
          nullable: true
        lastTradePrice:
          type: number
          nullable: true
        bestBid:
          type: number
          nullable: true
        bestAsk:
          type: number
          nullable: true
        automaticallyActive:
          type: boolean
          nullable: true
        clearBookOnStart:
          type: boolean
          nullable: true
        chartColor:
          type: string
          nullable: true
        seriesColor:
          type: string
          nullable: true
        showGmpSeries:
          type: boolean
          nullable: true
        showGmpOutcome:
          type: boolean
          nullable: true
        manualActivation:
          type: boolean
          nullable: true
        negRiskOther:
          type: boolean
          nullable: true
        gameId:
          type: string
          nullable: true
        groupItemRange:
          type: string
          nullable: true
        sportsMarketType:
          type: string
          nullable: true
        line:
          type: number
          nullable: true
        umaResolutionStatuses:
          type: string
          nullable: true
        pendingDeployment:
          type: boolean
          nullable: true
        deploying:
          type: boolean
          nullable: true
        deployingTimestamp:
          type: string
          format: date-time
          nullable: true
        scheduledDeploymentTimestamp:
          type: string
          format: date-time
          nullable: true
        rfqEnabled:
          type: boolean
          nullable: true
        eventStartTime:
          type: string
          format: date-time
          nullable: true
    EventCreator:
      type: object
      properties:
        id:
          type: string
        creatorName:
          type: string
          nullable: true
        creatorHandle:
          type: string
          nullable: true
        creatorUrl:
          type: string
          nullable: true
        creatorImage:
          type: string
          nullable: true
        createdAt:
          type: string
          format: date-time
          nullable: true
        updatedAt:
          type: string
          format: date-time
          nullable: true
    Template:
      type: object
      properties:
        id:
          type: string
        eventTitle:
          type: string
          nullable: true
        eventSlug:
          type: string
          nullable: true
        eventImage:
          type: string
          nullable: true
        marketTitle:
          type: string
          nullable: true
        description:
          type: string
          nullable: true
        resolutionSource:
          type: string
          nullable: true
        negRisk:
          type: boolean
          nullable: true
        sortBy:
          type: string
          nullable: true
        showMarketImages:
          type: boolean
          nullable: true
        seriesSlug:
          type: string
          nullable: true
        outcomes:
          type: string
          nullable: true

````

Skip to main content
Polymarket Documentation home pagedark logo

Search...
Ctrl K

Ask AI
Main Site

User Guide
For Developers
Changelog
Polymarket
Discord Community
Twitter
Developer Quickstart
Developer Quickstart
Fetching Market Data
Placing Your First Order
Glossary
API Rate Limits
Endpoints
Market Makers
Market Maker Introduction
Setup
Trading
Liquidity Rewards
Maker Rebates Program
Data Feeds
Inventory Management
Polymarket Builders Program
Builder Program Introduction
Builder Tiers
Builder Profile & Keys
Order Attribution
Relayer Client
Examples
Central Limit Order Book
CLOB Introduction
Status
Quickstart
Authentication
Geographic Restrictions

Client
Methods Overview
Public Methods
L1 Methods
L2 Methods
Builder Methods

REST API

Orderbook
GET
Get order book summary
POST
Get multiple order books summaries by request

Pricing
GET
Get market price
GET
Get multiple market prices
POST
Get multiple market prices by request
GET
Get midpoint price
GET
Get price history for a traded token

Spreads
POST
Get bid-ask spreads

Historical Timeseries Data
GET
Historical Timeseries Data

Order Management
Orders Overview
Place Single Order
Place Multiple Orders (Batching)
Get Order
Get Active Orders
Check Order Reward Scoring
Cancel Orders(s)
Onchain Order Info

Trades
Trades Overview
Get Trades
Websocket
WSS Overview
WSS Quickstart
WSS Authentication
User Channel
Market Channel

Sports Websocket
Overview
Message Format
Quickstart
Real Time Data Stream
RTDS Overview
RTDS Crypto Prices
RTDS Comments
Gamma Structure
Overview
Gamma Structure
Fetching Markets
Gamma Endpoints

Gamma Status
GET
Gamma API Health check

Sports
GET
List teams
GET
Get sports metadata information
GET
Get valid sports market types

Tags
GET
List tags
GET
Get tag by id
GET
Get tag by slug
GET
Get related tags (relationships) by tag id
GET
Get related tags (relationships) by tag slug
GET
Get tags related to a tag id
GET
Get tags related to a tag slug

Events
GET
List events
GET
Get event by id
GET
Get event tags
GET
Get event by slug

Markets
GET
List markets
GET
Get market by id
GET
Get market tags by id
GET
Get market by slug

Series
GET
List series
GET
Get series by id

Comments
GET
List comments
GET
Get comments by comment id
GET
Get comments by user address

Profiles

Search
Data-API

Data API Status

Core

Misc

Builders
Bridge & Swap
Overview

Bridge
Subgraph
Overview
Resolution
Resolution
Conditional Token Frameworks
Overview
Splitting USDC
Merging Tokens
Reedeeming Tokens
Deployment and Additional Information
Proxy Wallets
Proxy wallet
Negative Risk
Overview
List comments

curl --request GET \
  --url https://gamma-api.polymarket.com/comments

200
[
  {
    "id": "<string>",
    "body": "<string>",
    "parentEntityType": "<string>",
    "parentEntityID": 123,
    "parentCommentID": "<string>",
    "userAddress": "<string>",
    "replyAddress": "<string>",
    "createdAt": "2023-11-07T05:31:56Z",
    "updatedAt": "2023-11-07T05:31:56Z",
    "profile": {
      "name": "<string>",
      "pseudonym": "<string>",
      "displayUsernamePublic": true,
      "bio": "<string>",
      "isMod": true,
      "isCreator": true,
      "proxyWallet": "<string>",
      "baseAddress": "<string>",
      "profileImage": "<string>",
      "profileImageOptimized": {
        "id": "<string>",
        "imageUrlSource": "<string>",
        "imageUrlOptimized": "<string>",
        "imageSizeKbSource": 123,
        "imageSizeKbOptimized": 123,
        "imageOptimizedComplete": true,
        "imageOptimizedLastUpdated": "<string>",
        "relID": 123,
        "field": "<string>",
        "relname": "<string>"
      },
      "positions": [
        {
          "tokenId": "<string>",
          "positionSize": "<string>"
        }
      ]
    },
    "reactions": [
      {
        "id": "<string>",
        "commentID": 123,
        "reactionType": "<string>",
        "icon": "<string>",
        "userAddress": "<string>",
        "createdAt": "2023-11-07T05:31:56Z",
        "profile": {
          "name": "<string>",
          "pseudonym": "<string>",
          "displayUsernamePublic": true,
          "bio": "<string>",
          "isMod": true,
          "isCreator": true,
          "proxyWallet": "<string>",
          "baseAddress": "<string>",
          "profileImage": "<string>",
          "profileImageOptimized": {
            "id": "<string>",
            "imageUrlSource": "<string>",
            "imageUrlOptimized": "<string>",
            "imageSizeKbSource": 123,
            "imageSizeKbOptimized": 123,
            "imageOptimizedComplete": true,
            "imageOptimizedLastUpdated": "<string>",
            "relID": 123,
            "field": "<string>",
            "relname": "<string>"
          },
          "positions": [
            {
              "tokenId": "<string>",
              "positionSize": "<string>"
            }
          ]
        }
      }
    ],
    "reportCount": 123,
    "reactionCount": 123
  }
]
Comments
List comments
GET
/
comments

Try it
Query Parameters
​
limit
integer
Required range: x >= 0
​
offset
integer
Required range: x >= 0
​
order
string
Comma-separated list of fields to order by

​
ascending
boolean
​
parent_entity_type
enum<string>
Available options: Event, Series, market 
​
parent_entity_id
integer
​
get_positions
boolean
​
holders_only
boolean
Response
200 - application/json
List of comments

​
id
string
​
body
string | null
​
parentEntityType
string | null
​
parentEntityID
integer | null
​
parentCommentID
string | null
​
userAddress
string | null
​
replyAddress
string | null
​
createdAt
string<date-time> | null
​
updatedAt
string<date-time> | null
​
profile
object
Show child attributes

​
reactions
object[]
Show child attributes

​
reportCount
integer | null
​
reactionCount
integer | null
Get series by id
Get comments by comment id
Ask a question...

github
Powered by
List comments - Polymarket Documentation

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.polymarket.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get comments by comment id



## OpenAPI

````yaml api-reference/gamma-openapi.json get /comments/{id}
openapi: 3.0.3
info:
  title: Markets API
  version: 1.0.0
  description: REST API specification for public endpoints used by the Markets service.
servers:
  - url: https://gamma-api.polymarket.com
    description: Polymarket Gamma API Production Server
security: []
tags:
  - name: Gamma Status
    description: Gamma API status and health check
  - name: Sports
    description: Sports-related endpoints including teams and game data
  - name: Tags
    description: Tag management and related tag operations
  - name: Events
    description: Event management and event-related operations
  - name: Markets
    description: Market data and market-related operations
  - name: Comments
    description: Comment system and user interactions
  - name: Series
    description: Series management and related operations
  - name: Profiles
    description: User profile management
  - name: Search
    description: Search functionality across different entity types
paths:
  /comments/{id}:
    get:
      tags:
        - Comments
      summary: Get comments by comment id
      operationId: getCommentsById
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: integer
        - name: get_positions
          in: query
          schema:
            type: boolean
      responses:
        '200':
          description: Comments
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Comment'
components:
  schemas:
    Comment:
      type: object
      properties:
        id:
          type: string
        body:
          type: string
          nullable: true
        parentEntityType:
          type: string
          nullable: true
        parentEntityID:
          type: integer
          nullable: true
        parentCommentID:
          type: string
          nullable: true
        userAddress:
          type: string
          nullable: true
        replyAddress:
          type: string
          nullable: true
        createdAt:
          type: string
          format: date-time
          nullable: true
        updatedAt:
          type: string
          format: date-time
          nullable: true
        profile:
          $ref: '#/components/schemas/CommentProfile'
        reactions:
          type: array
          items:
            $ref: '#/components/schemas/Reaction'
        reportCount:
          type: integer
          nullable: true
        reactionCount:
          type: integer
          nullable: true
    CommentProfile:
      type: object
      properties:
        name:
          type: string
          nullable: true
        pseudonym:
          type: string
          nullable: true
        displayUsernamePublic:
          type: boolean
          nullable: true
        bio:
          type: string
          nullable: true
        isMod:
          type: boolean
          nullable: true
        isCreator:
          type: boolean
          nullable: true
        proxyWallet:
          type: string
          nullable: true
        baseAddress:
          type: string
          nullable: true
        profileImage:
          type: string
          nullable: true
        profileImageOptimized:
          $ref: '#/components/schemas/ImageOptimization'
        positions:
          type: array
          items:
            $ref: '#/components/schemas/CommentPosition'
    Reaction:
      type: object
      properties:
        id:
          type: string
        commentID:
          type: integer
          nullable: true
        reactionType:
          type: string
          nullable: true
        icon:
          type: string
          nullable: true
        userAddress:
          type: string
          nullable: true
        createdAt:
          type: string
          format: date-time
          nullable: true
        profile:
          $ref: '#/components/schemas/CommentProfile'
    ImageOptimization:
      type: object
      properties:
        id:
          type: string
        imageUrlSource:
          type: string
          nullable: true
        imageUrlOptimized:
          type: string
          nullable: true
        imageSizeKbSource:
          type: number
          nullable: true
        imageSizeKbOptimized:
          type: number
          nullable: true
        imageOptimizedComplete:
          type: boolean
          nullable: true
        imageOptimizedLastUpdated:
          type: string
          nullable: true
        relID:
          type: integer
          nullable: true
        field:
          type: string
          nullable: true
        relname:
          type: string
          nullable: true
    CommentPosition:
      type: object
      properties:
        tokenId:
          type: string
          nullable: true
        positionSize:
          type: string
          nullable: true

````

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.polymarket.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get comments by user address



## OpenAPI

````yaml api-reference/gamma-openapi.json get /comments/user_address/{user_address}
openapi: 3.0.3
info:
  title: Markets API
  version: 1.0.0
  description: REST API specification for public endpoints used by the Markets service.
servers:
  - url: https://gamma-api.polymarket.com
    description: Polymarket Gamma API Production Server
security: []
tags:
  - name: Gamma Status
    description: Gamma API status and health check
  - name: Sports
    description: Sports-related endpoints including teams and game data
  - name: Tags
    description: Tag management and related tag operations
  - name: Events
    description: Event management and event-related operations
  - name: Markets
    description: Market data and market-related operations
  - name: Comments
    description: Comment system and user interactions
  - name: Series
    description: Series management and related operations
  - name: Profiles
    description: User profile management
  - name: Search
    description: Search functionality across different entity types
paths:
  /comments/user_address/{user_address}:
    get:
      tags:
        - Comments
        - Profiles
      summary: Get comments by user address
      operationId: getCommentsByUserAddress
      parameters:
        - name: user_address
          in: path
          required: true
          schema:
            type: string
        - $ref: '#/components/parameters/limit'
        - $ref: '#/components/parameters/offset'
        - $ref: '#/components/parameters/order'
        - $ref: '#/components/parameters/ascending'
      responses:
        '200':
          description: Comments
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Comment'
components:
  parameters:
    limit:
      name: limit
      in: query
      schema:
        type: integer
        minimum: 0
    offset:
      name: offset
      in: query
      schema:
        type: integer
        minimum: 0
    order:
      name: order
      in: query
      schema:
        type: string
      description: Comma-separated list of fields to order by
    ascending:
      name: ascending
      in: query
      schema:
        type: boolean
  schemas:
    Comment:
      type: object
      properties:
        id:
          type: string
        body:
          type: string
          nullable: true
        parentEntityType:
          type: string
          nullable: true
        parentEntityID:
          type: integer
          nullable: true
        parentCommentID:
          type: string
          nullable: true
        userAddress:
          type: string
          nullable: true
        replyAddress:
          type: string
          nullable: true
        createdAt:
          type: string
          format: date-time
          nullable: true
        updatedAt:
          type: string
          format: date-time
          nullable: true
        profile:
          $ref: '#/components/schemas/CommentProfile'
        reactions:
          type: array
          items:
            $ref: '#/components/schemas/Reaction'
        reportCount:
          type: integer
          nullable: true
        reactionCount:
          type: integer
          nullable: true
    CommentProfile:
      type: object
      properties:
        name:
          type: string
          nullable: true
        pseudonym:
          type: string
          nullable: true
        displayUsernamePublic:
          type: boolean
          nullable: true
        bio:
          type: string
          nullable: true
        isMod:
          type: boolean
          nullable: true
        isCreator:
          type: boolean
          nullable: true
        proxyWallet:
          type: string
          nullable: true
        baseAddress:
          type: string
          nullable: true
        profileImage:
          type: string
          nullable: true
        profileImageOptimized:
          $ref: '#/components/schemas/ImageOptimization'
        positions:
          type: array
          items:
            $ref: '#/components/schemas/CommentPosition'
    Reaction:
      type: object
      properties:
        id:
          type: string
        commentID:
          type: integer
          nullable: true
        reactionType:
          type: string
          nullable: true
        icon:
          type: string
          nullable: true
        userAddress:
          type: string
          nullable: true
        createdAt:
          type: string
          format: date-time
          nullable: true
        profile:
          $ref: '#/components/schemas/CommentProfile'
    ImageOptimization:
      type: object
      properties:
        id:
          type: string
        imageUrlSource:
          type: string
          nullable: true
        imageUrlOptimized:
          type: string
          nullable: true
        imageSizeKbSource:
          type: number
          nullable: true
        imageSizeKbOptimized:
          type: number
          nullable: true
        imageOptimizedComplete:
          type: boolean
          nullable: true
        imageOptimizedLastUpdated:
          type: string
          nullable: true
        relID:
          type: integer
          nullable: true
        field:
          type: string
          nullable: true
        relname:
          type: string
          nullable: true
    CommentPosition:
      type: object
      properties:
        tokenId:
          type: string
          nullable: true
        positionSize:
          type: string
          nullable: true

````

Skip to main content
Polymarket Documentation home pagedark logo

Search...
Ctrl K

Ask AI
Main Site

User Guide
For Developers
Changelog
Polymarket
Discord Community
Twitter
Developer Quickstart
Developer Quickstart
Fetching Market Data
Placing Your First Order
Glossary
API Rate Limits
Endpoints
Market Makers
Market Maker Introduction
Setup
Trading
Liquidity Rewards
Maker Rebates Program
Data Feeds
Inventory Management
Polymarket Builders Program
Builder Program Introduction
Builder Tiers
Builder Profile & Keys
Order Attribution
Relayer Client
Examples
Central Limit Order Book
CLOB Introduction
Status
Quickstart
Authentication
Geographic Restrictions

Client
Methods Overview
Public Methods
L1 Methods
L2 Methods
Builder Methods

REST API

Orderbook
GET
Get order book summary
POST
Get multiple order books summaries by request

Pricing
GET
Get market price
GET
Get multiple market prices
POST
Get multiple market prices by request
GET
Get midpoint price
GET
Get price history for a traded token

Spreads
POST
Get bid-ask spreads

Historical Timeseries Data
GET
Historical Timeseries Data

Order Management
Orders Overview
Place Single Order
Place Multiple Orders (Batching)
Get Order
Get Active Orders
Check Order Reward Scoring
Cancel Orders(s)
Onchain Order Info

Trades
Trades Overview
Get Trades
Websocket
WSS Overview
WSS Quickstart
WSS Authentication
User Channel
Market Channel

Sports Websocket
Overview
Message Format
Quickstart
Real Time Data Stream
RTDS Overview
RTDS Crypto Prices
RTDS Comments
Gamma Structure
Overview
Gamma Structure
Fetching Markets
Gamma Endpoints

Gamma Status
GET
Gamma API Health check

Sports
GET
List teams
GET
Get sports metadata information
GET
Get valid sports market types

Tags
GET
List tags
GET
Get tag by id
GET
Get tag by slug
GET
Get related tags (relationships) by tag id
GET
Get related tags (relationships) by tag slug
GET
Get tags related to a tag id
GET
Get tags related to a tag slug

Events
GET
List events
GET
Get event by id
GET
Get event tags
GET
Get event by slug

Markets
GET
List markets
GET
Get market by id
GET
Get market tags by id
GET
Get market by slug

Series
GET
List series
GET
Get series by id

Comments
GET
List comments
GET
Get comments by comment id
GET
Get comments by user address

Profiles
GET
Get public profile by wallet address

Search
Data-API

Data API Status

Core

Misc

Builders
Bridge & Swap
Overview

Bridge
Subgraph
Overview
Resolution
Resolution
Conditional Token Frameworks
Overview
Splitting USDC
Merging Tokens
Reedeeming Tokens
Deployment and Additional Information
Proxy Wallets
Proxy wallet
Negative Risk
Overview
Get public profile by wallet address

curl --request GET \
  --url https://gamma-api.polymarket.com/public-profile

200

400

404
{
  "createdAt": "2023-11-07T05:31:56Z",
  "proxyWallet": "<string>",
  "profileImage": "<string>",
  "displayUsernamePublic": true,
  "bio": "<string>",
  "pseudonym": "<string>",
  "name": "<string>",
  "users": [
    {
      "id": "<string>",
      "creator": true,
      "mod": true
    }
  ],
  "xUsername": "<string>",
  "verifiedBadge": true
}
Profiles
Get public profile by wallet address
GET
/
public-profile

Try it
Query Parameters
​
address
stringrequired
The wallet address (proxy wallet or user address)

Response

200

application/json
Public profile information

​
createdAt
string<date-time> | null
ISO 8601 timestamp of when the profile was created

​
proxyWallet
string | null
The proxy wallet address

​
profileImage
string<uri> | null
URL to the profile image

​
displayUsernamePublic
boolean | null
Whether the username is displayed publicly

​
bio
string | null
Profile bio

​
pseudonym
string | null
Auto-generated pseudonym

​
name
string | null
User-chosen display name

​
users
object[] | null
Array of associated user objects

Show child attributes

​
xUsername
string | null
X (Twitter) username

​
verifiedBadge
boolean | null
Whether the profile has a verified badge

Get comments by user address
Search markets, events, and profiles
Ask a question...

github
Powered by
Get public profile by wallet address - Polymarket Documentation

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.polymarket.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Search markets, events, and profiles



## OpenAPI

````yaml api-reference/gamma-openapi.json get /public-search
openapi: 3.0.3
info:
  title: Markets API
  version: 1.0.0
  description: REST API specification for public endpoints used by the Markets service.
servers:
  - url: https://gamma-api.polymarket.com
    description: Polymarket Gamma API Production Server
security: []
tags:
  - name: Gamma Status
    description: Gamma API status and health check
  - name: Sports
    description: Sports-related endpoints including teams and game data
  - name: Tags
    description: Tag management and related tag operations
  - name: Events
    description: Event management and event-related operations
  - name: Markets
    description: Market data and market-related operations
  - name: Comments
    description: Comment system and user interactions
  - name: Series
    description: Series management and related operations
  - name: Profiles
    description: User profile management
  - name: Search
    description: Search functionality across different entity types
paths:
  /public-search:
    get:
      tags:
        - Search
      summary: Search markets, events, and profiles
      operationId: publicSearch
      parameters:
        - name: q
          in: query
          required: true
          schema:
            type: string
        - name: cache
          in: query
          schema:
            type: boolean
        - name: events_status
          in: query
          schema:
            type: string
        - name: limit_per_type
          in: query
          schema:
            type: integer
        - name: page
          in: query
          schema:
            type: integer
        - name: events_tag
          in: query
          schema:
            type: array
            items:
              type: string
        - name: keep_closed_markets
          in: query
          schema:
            type: integer
        - name: sort
          in: query
          schema:
            type: string
        - name: ascending
          in: query
          schema:
            type: boolean
        - name: search_tags
          in: query
          schema:
            type: boolean
        - name: search_profiles
          in: query
          schema:
            type: boolean
        - name: recurrence
          in: query
          schema:
            type: string
        - name: exclude_tag_id
          in: query
          schema:
            type: array
            items:
              type: integer
        - name: optimized
          in: query
          schema:
            type: boolean
      responses:
        '200':
          description: Search results
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Search'
components:
  schemas:
    Search:
      type: object
      properties:
        events:
          type: array
          items:
            $ref: '#/components/schemas/Event'
          nullable: true
        tags:
          type: array
          items:
            $ref: '#/components/schemas/SearchTag'
          nullable: true
        profiles:
          type: array
          items:
            $ref: '#/components/schemas/Profile'
          nullable: true
        pagination:
          $ref: '#/components/schemas/Pagination'
    Event:
      type: object
      properties:
        id:
          type: string
        ticker:
          type: string
          nullable: true
        slug:
          type: string
          nullable: true
        title:
          type: string
          nullable: true
        subtitle:
          type: string
          nullable: true
        description:
          type: string
          nullable: true
        resolutionSource:
          type: string
          nullable: true
        startDate:
          type: string
          format: date-time
          nullable: true
        creationDate:
          type: string
          format: date-time
          nullable: true
        endDate:
          type: string
          format: date-time
          nullable: true
        image:
          type: string
          nullable: true
        icon:
          type: string
          nullable: true
        active:
          type: boolean
          nullable: true
        closed:
          type: boolean
          nullable: true
        archived:
          type: boolean
          nullable: true
        new:
          type: boolean
          nullable: true
        featured:
          type: boolean
          nullable: true
        restricted:
          type: boolean
          nullable: true
        liquidity:
          type: number
          nullable: true
        volume:
          type: number
          nullable: true
        openInterest:
          type: number
          nullable: true
        sortBy:
          type: string
          nullable: true
        category:
          type: string
          nullable: true
        subcategory:
          type: string
          nullable: true
        isTemplate:
          type: boolean
          nullable: true
        templateVariables:
          type: string
          nullable: true
        published_at:
          type: string
          nullable: true
        createdBy:
          type: string
          nullable: true
        updatedBy:
          type: string
          nullable: true
        createdAt:
          type: string
          format: date-time
          nullable: true
        updatedAt:
          type: string
          format: date-time
          nullable: true
        commentsEnabled:
          type: boolean
          nullable: true
        competitive:
          type: number
          nullable: true
        volume24hr:
          type: number
          nullable: true
        volume1wk:
          type: number
          nullable: true
        volume1mo:
          type: number
          nullable: true
        volume1yr:
          type: number
          nullable: true
        featuredImage:
          type: string
          nullable: true
        disqusThread:
          type: string
          nullable: true
        parentEvent:
          type: string
          nullable: true
        enableOrderBook:
          type: boolean
          nullable: true
        liquidityAmm:
          type: number
          nullable: true
        liquidityClob:
          type: number
          nullable: true
        negRisk:
          type: boolean
          nullable: true
        negRiskMarketID:
          type: string
          nullable: true
        negRiskFeeBips:
          type: integer
          nullable: true
        commentCount:
          type: integer
          nullable: true
        imageOptimized:
          $ref: '#/components/schemas/ImageOptimization'
        iconOptimized:
          $ref: '#/components/schemas/ImageOptimization'
        featuredImageOptimized:
          $ref: '#/components/schemas/ImageOptimization'
        subEvents:
          type: array
          items:
            type: string
          nullable: true
        markets:
          type: array
          items:
            $ref: '#/components/schemas/Market'
        series:
          type: array
          items:
            $ref: '#/components/schemas/Series'
        categories:
          type: array
          items:
            $ref: '#/components/schemas/Category'
        collections:
          type: array
          items:
            $ref: '#/components/schemas/Collection'
        tags:
          type: array
          items:
            $ref: '#/components/schemas/Tag'
        cyom:
          type: boolean
          nullable: true
        closedTime:
          type: string
          format: date-time
          nullable: true
        showAllOutcomes:
          type: boolean
          nullable: true
        showMarketImages:
          type: boolean
          nullable: true
        automaticallyResolved:
          type: boolean
          nullable: true
        enableNegRisk:
          type: boolean
          nullable: true
        automaticallyActive:
          type: boolean
          nullable: true
        eventDate:
          type: string
          nullable: true
        startTime:
          type: string
          format: date-time
          nullable: true
        eventWeek:
          type: integer
          nullable: true
        seriesSlug:
          type: string
          nullable: true
        score:
          type: string
          nullable: true
        elapsed:
          type: string
          nullable: true
        period:
          type: string
          nullable: true
        live:
          type: boolean
          nullable: true
        ended:
          type: boolean
          nullable: true
        finishedTimestamp:
          type: string
          format: date-time
          nullable: true
        gmpChartMode:
          type: string
          nullable: true
        eventCreators:
          type: array
          items:
            $ref: '#/components/schemas/EventCreator'
        tweetCount:
          type: integer
          nullable: true
        chats:
          type: array
          items:
            $ref: '#/components/schemas/Chat'
        featuredOrder:
          type: integer
          nullable: true
        estimateValue:
          type: boolean
          nullable: true
        cantEstimate:
          type: boolean
          nullable: true
        estimatedValue:
          type: string
          nullable: true
        templates:
          type: array
          items:
            $ref: '#/components/schemas/Template'
        spreadsMainLine:
          type: number
          nullable: true
        totalsMainLine:
          type: number
          nullable: true
        carouselMap:
          type: string
          nullable: true
        pendingDeployment:
          type: boolean
          nullable: true
        deploying:
          type: boolean
          nullable: true
        deployingTimestamp:
          type: string
          format: date-time
          nullable: true
        scheduledDeploymentTimestamp:
          type: string
          format: date-time
          nullable: true
        gameStatus:
          type: string
          nullable: true
    SearchTag:
      type: object
      properties:
        id:
          type: string
        label:
          type: string
        slug:
          type: string
        event_count:
          type: integer
    Profile:
      type: object
      properties:
        id:
          type: string
        name:
          type: string
          nullable: true
        user:
          type: integer
          nullable: true
        referral:
          type: string
          nullable: true
        createdBy:
          type: integer
          nullable: true
        updatedBy:
          type: integer
          nullable: true
        createdAt:
          type: string
          format: date-time
          nullable: true
        updatedAt:
          type: string
          format: date-time
          nullable: true
        utmSource:
          type: string
          nullable: true
        utmMedium:
          type: string
          nullable: true
        utmCampaign:
          type: string
          nullable: true
        utmContent:
          type: string
          nullable: true
        utmTerm:
          type: string
          nullable: true
        walletActivated:
          type: boolean
          nullable: true
        pseudonym:
          type: string
          nullable: true
        displayUsernamePublic:
          type: boolean
          nullable: true
        profileImage:
          type: string
          nullable: true
        bio:
          type: string
          nullable: true
        proxyWallet:
          type: string
          nullable: true
        profileImageOptimized:
          $ref: '#/components/schemas/ImageOptimization'
        isCloseOnly:
          type: boolean
          nullable: true
        isCertReq:
          type: boolean
          nullable: true
        certReqDate:
          type: string
          format: date-time
          nullable: true
    Pagination:
      type: object
      properties:
        hasMore:
          type: boolean
        totalResults:
          type: integer
    ImageOptimization:
      type: object
      properties:
        id:
          type: string
        imageUrlSource:
          type: string
          nullable: true
        imageUrlOptimized:
          type: string
          nullable: true
        imageSizeKbSource:
          type: number
          nullable: true
        imageSizeKbOptimized:
          type: number
          nullable: true
        imageOptimizedComplete:
          type: boolean
          nullable: true
        imageOptimizedLastUpdated:
          type: string
          nullable: true
        relID:
          type: integer
          nullable: true
        field:
          type: string
          nullable: true
        relname:
          type: string
          nullable: true
    Market:
      type: object
      properties:
        id:
          type: string
        question:
          type: string
          nullable: true
        conditionId:
          type: string
        slug:
          type: string
          nullable: true
        twitterCardImage:
          type: string
          nullable: true
        resolutionSource:
          type: string
          nullable: true
        endDate:
          type: string
          format: date-time
          nullable: true
        category:
          type: string
          nullable: true
        ammType:
          type: string
          nullable: true
        liquidity:
          type: string
          nullable: true
        sponsorName:
          type: string
          nullable: true
        sponsorImage:
          type: string
          nullable: true
        startDate:
          type: string
          format: date-time
          nullable: true
        xAxisValue:
          type: string
          nullable: true
        yAxisValue:
          type: string
          nullable: true
        denominationToken:
          type: string
          nullable: true
        fee:
          type: string
          nullable: true
        image:
          type: string
          nullable: true
        icon:
          type: string
          nullable: true
        lowerBound:
          type: string
          nullable: true
        upperBound:
          type: string
          nullable: true
        description:
          type: string
          nullable: true
        outcomes:
          type: string
          nullable: true
        outcomePrices:
          type: string
          nullable: true
        volume:
          type: string
          nullable: true
        active:
          type: boolean
          nullable: true
        marketType:
          type: string
          nullable: true
        formatType:
          type: string
          nullable: true
        lowerBoundDate:
          type: string
          nullable: true
        upperBoundDate:
          type: string
          nullable: true
        closed:
          type: boolean
          nullable: true
        marketMakerAddress:
          type: string
        createdBy:
          type: integer
          nullable: true
        updatedBy:
          type: integer
          nullable: true
        createdAt:
          type: string
          format: date-time
          nullable: true
        updatedAt:
          type: string
          format: date-time
          nullable: true
        closedTime:
          type: string
          nullable: true
        wideFormat:
          type: boolean
          nullable: true
        new:
          type: boolean
          nullable: true
        mailchimpTag:
          type: string
          nullable: true
        featured:
          type: boolean
          nullable: true
        archived:
          type: boolean
          nullable: true
        resolvedBy:
          type: string
          nullable: true
        restricted:
          type: boolean
          nullable: true
        marketGroup:
          type: integer
          nullable: true
        groupItemTitle:
          type: string
          nullable: true
        groupItemThreshold:
          type: string
          nullable: true
        questionID:
          type: string
          nullable: true
        umaEndDate:
          type: string
          nullable: true
        enableOrderBook:
          type: boolean
          nullable: true
        orderPriceMinTickSize:
          type: number
          nullable: true
        orderMinSize:
          type: number
          nullable: true
        umaResolutionStatus:
          type: string
          nullable: true
        curationOrder:
          type: integer
          nullable: true
        volumeNum:
          type: number
          nullable: true
        liquidityNum:
          type: number
          nullable: true
        endDateIso:
          type: string
          nullable: true
        startDateIso:
          type: string
          nullable: true
        umaEndDateIso:
          type: string
          nullable: true
        hasReviewedDates:
          type: boolean
          nullable: true
        readyForCron:
          type: boolean
          nullable: true
        commentsEnabled:
          type: boolean
          nullable: true
        volume24hr:
          type: number
          nullable: true
        volume1wk:
          type: number
          nullable: true
        volume1mo:
          type: number
          nullable: true
        volume1yr:
          type: number
          nullable: true
        gameStartTime:
          type: string
          nullable: true
        secondsDelay:
          type: integer
          nullable: true
        clobTokenIds:
          type: string
          nullable: true
        disqusThread:
          type: string
          nullable: true
        shortOutcomes:
          type: string
          nullable: true
        teamAID:
          type: string
          nullable: true
        teamBID:
          type: string
          nullable: true
        umaBond:
          type: string
          nullable: true
        umaReward:
          type: string
          nullable: true
        fpmmLive:
          type: boolean
          nullable: true
        volume24hrAmm:
          type: number
          nullable: true
        volume1wkAmm:
          type: number
          nullable: true
        volume1moAmm:
          type: number
          nullable: true
        volume1yrAmm:
          type: number
          nullable: true
        volume24hrClob:
          type: number
          nullable: true
        volume1wkClob:
          type: number
          nullable: true
        volume1moClob:
          type: number
          nullable: true
        volume1yrClob:
          type: number
          nullable: true
        volumeAmm:
          type: number
          nullable: true
        volumeClob:
          type: number
          nullable: true
        liquidityAmm:
          type: number
          nullable: true
        liquidityClob:
          type: number
          nullable: true
        makerBaseFee:
          type: integer
          nullable: true
        takerBaseFee:
          type: integer
          nullable: true
        customLiveness:
          type: integer
          nullable: true
        acceptingOrders:
          type: boolean
          nullable: true
        notificationsEnabled:
          type: boolean
          nullable: true
        score:
          type: integer
          nullable: true
        imageOptimized:
          $ref: '#/components/schemas/ImageOptimization'
        iconOptimized:
          $ref: '#/components/schemas/ImageOptimization'
        events:
          type: array
          items:
            $ref: '#/components/schemas/Event'
        categories:
          type: array
          items:
            $ref: '#/components/schemas/Category'
        tags:
          type: array
          items:
            $ref: '#/components/schemas/Tag'
        creator:
          type: string
          nullable: true
        ready:
          type: boolean
          nullable: true
        funded:
          type: boolean
          nullable: true
        pastSlugs:
          type: string
          nullable: true
        readyTimestamp:
          type: string
          format: date-time
          nullable: true
        fundedTimestamp:
          type: string
          format: date-time
          nullable: true
        acceptingOrdersTimestamp:
          type: string
          format: date-time
          nullable: true
        competitive:
          type: number
          nullable: true
        rewardsMinSize:
          type: number
          nullable: true
        rewardsMaxSpread:
          type: number
          nullable: true
        spread:
          type: number
          nullable: true
        automaticallyResolved:
          type: boolean
          nullable: true
        oneDayPriceChange:
          type: number
          nullable: true
        oneHourPriceChange:
          type: number
          nullable: true
        oneWeekPriceChange:
          type: number
          nullable: true
        oneMonthPriceChange:
          type: number
          nullable: true
        oneYearPriceChange:
          type: number
          nullable: true
        lastTradePrice:
          type: number
          nullable: true
        bestBid:
          type: number
          nullable: true
        bestAsk:
          type: number
          nullable: true
        automaticallyActive:
          type: boolean
          nullable: true
        clearBookOnStart:
          type: boolean
          nullable: true
        chartColor:
          type: string
          nullable: true
        seriesColor:
          type: string
          nullable: true
        showGmpSeries:
          type: boolean
          nullable: true
        showGmpOutcome:
          type: boolean
          nullable: true
        manualActivation:
          type: boolean
          nullable: true
        negRiskOther:
          type: boolean
          nullable: true
        gameId:
          type: string
          nullable: true
        groupItemRange:
          type: string
          nullable: true
        sportsMarketType:
          type: string
          nullable: true
        line:
          type: number
          nullable: true
        umaResolutionStatuses:
          type: string
          nullable: true
        pendingDeployment:
          type: boolean
          nullable: true
        deploying:
          type: boolean
          nullable: true
        deployingTimestamp:
          type: string
          format: date-time
          nullable: true
        scheduledDeploymentTimestamp:
          type: string
          format: date-time
          nullable: true
        rfqEnabled:
          type: boolean
          nullable: true
        eventStartTime:
          type: string
          format: date-time
          nullable: true
    Series:
      type: object
      properties:
        id:
          type: string
        ticker:
          type: string
          nullable: true
        slug:
          type: string
          nullable: true
        title:
          type: string
          nullable: true
        subtitle:
          type: string
          nullable: true
        seriesType:
          type: string
          nullable: true
        recurrence:
          type: string
          nullable: true
        description:
          type: string
          nullable: true
        image:
          type: string
          nullable: true
        icon:
          type: string
          nullable: true
        layout:
          type: string
          nullable: true
        active:
          type: boolean
          nullable: true
        closed:
          type: boolean
          nullable: true
        archived:
          type: boolean
          nullable: true
        new:
          type: boolean
          nullable: true
        featured:
          type: boolean
          nullable: true
        restricted:
          type: boolean
          nullable: true
        isTemplate:
          type: boolean
          nullable: true
        templateVariables:
          type: boolean
          nullable: true
        publishedAt:
          type: string
          nullable: true
        createdBy:
          type: string
          nullable: true
        updatedBy:
          type: string
          nullable: true
        createdAt:
          type: string
          format: date-time
          nullable: true
        updatedAt:
          type: string
          format: date-time
          nullable: true
        commentsEnabled:
          type: boolean
          nullable: true
        competitive:
          type: string
          nullable: true
        volume24hr:
          type: number
          nullable: true
        volume:
          type: number
          nullable: true
        liquidity:
          type: number
          nullable: true
        startDate:
          type: string
          format: date-time
          nullable: true
        pythTokenID:
          type: string
          nullable: true
        cgAssetName:
          type: string
          nullable: true
        score:
          type: integer
          nullable: true
        events:
          type: array
          items:
            $ref: '#/components/schemas/Event'
        collections:
          type: array
          items:
            $ref: '#/components/schemas/Collection'
        categories:
          type: array
          items:
            $ref: '#/components/schemas/Category'
        tags:
          type: array
          items:
            $ref: '#/components/schemas/Tag'
        commentCount:
          type: integer
          nullable: true
        chats:
          type: array
          items:
            $ref: '#/components/schemas/Chat'
    Category:
      type: object
      properties:
        id:
          type: string
        label:
          type: string
          nullable: true
        parentCategory:
          type: string
          nullable: true
        slug:
          type: string
          nullable: true
        publishedAt:
          type: string
          nullable: true
        createdBy:
          type: string
          nullable: true
        updatedBy:
          type: string
          nullable: true
        createdAt:
          type: string
          format: date-time
          nullable: true
        updatedAt:
          type: string
          format: date-time
          nullable: true
    Collection:
      type: object
      properties:
        id:
          type: string
        ticker:
          type: string
          nullable: true
        slug:
          type: string
          nullable: true
        title:
          type: string
          nullable: true
        subtitle:
          type: string
          nullable: true
        collectionType:
          type: string
          nullable: true
        description:
          type: string
          nullable: true
        tags:
          type: string
          nullable: true
        image:
          type: string
          nullable: true
        icon:
          type: string
          nullable: true
        headerImage:
          type: string
          nullable: true
        layout:
          type: string
          nullable: true
        active:
          type: boolean
          nullable: true
        closed:
          type: boolean
          nullable: true
        archived:
          type: boolean
          nullable: true
        new:
          type: boolean
          nullable: true
        featured:
          type: boolean
          nullable: true
        restricted:
          type: boolean
          nullable: true
        isTemplate:
          type: boolean
          nullable: true
        templateVariables:
          type: string
          nullable: true
        publishedAt:
          type: string
          nullable: true
        createdBy:
          type: string
          nullable: true
        updatedBy:
          type: string
          nullable: true
        createdAt:
          type: string
          format: date-time
          nullable: true
        updatedAt:
          type: string
          format: date-time
          nullable: true
        commentsEnabled:
          type: boolean
          nullable: true
        imageOptimized:
          $ref: '#/components/schemas/ImageOptimization'
        iconOptimized:
          $ref: '#/components/schemas/ImageOptimization'
        headerImageOptimized:
          $ref: '#/components/schemas/ImageOptimization'
    Tag:
      type: object
      properties:
        id:
          type: string
        label:
          type: string
          nullable: true
        slug:
          type: string
          nullable: true
        forceShow:
          type: boolean
          nullable: true
        publishedAt:
          type: string
          nullable: true
        createdBy:
          type: integer
          nullable: true
        updatedBy:
          type: integer
          nullable: true
        createdAt:
          type: string
          format: date-time
          nullable: true
        updatedAt:
          type: string
          format: date-time
          nullable: true
        forceHide:
          type: boolean
          nullable: true
        isCarousel:
          type: boolean
          nullable: true
    EventCreator:
      type: object
      properties:
        id:
          type: string
        creatorName:
          type: string
          nullable: true
        creatorHandle:
          type: string
          nullable: true
        creatorUrl:
          type: string
          nullable: true
        creatorImage:
          type: string
          nullable: true
        createdAt:
          type: string
          format: date-time
          nullable: true
        updatedAt:
          type: string
          format: date-time
          nullable: true
    Chat:
      type: object
      properties:
        id:
          type: string
        channelId:
          type: string
          nullable: true
        channelName:
          type: string
          nullable: true
        channelImage:
          type: string
          nullable: true
        live:
          type: boolean
          nullable: true
        startTime:
          type: string
          format: date-time
          nullable: true
        endTime:
          type: string
          format: date-time
          nullable: true
    Template:
      type: object
      properties:
        id:
          type: string
        eventTitle:
          type: string
          nullable: true
        eventSlug:
          type: string
          nullable: true
        eventImage:
          type: string
          nullable: true
        marketTitle:
          type: string
          nullable: true
        description:
          type: string
          nullable: true
        resolutionSource:
          type: string
          nullable: true
        negRisk:
          type: boolean
          nullable: true
        sortBy:
          type: string
          nullable: true
        showMarketImages:
          type: boolean
          nullable: true
        seriesSlug:
          type: string
          nullable: true
        outcomes:
          type: string
          nullable: true

````

Skip to main content
Polymarket Documentation home pagedark logo

Search...
Ctrl K

Ask AI
Main Site

User Guide
For Developers
Changelog
Polymarket
Discord Community
Twitter
Developer Quickstart
Developer Quickstart
Fetching Market Data
Placing Your First Order
Glossary
API Rate Limits
Endpoints
Market Makers
Market Maker Introduction
Setup
Trading
Liquidity Rewards
Maker Rebates Program
Data Feeds
Inventory Management
Polymarket Builders Program
Builder Program Introduction
Builder Tiers
Builder Profile & Keys
Order Attribution
Relayer Client
Examples
Central Limit Order Book
CLOB Introduction
Status
Quickstart
Authentication
Geographic Restrictions

Client
Methods Overview
Public Methods
L1 Methods
L2 Methods
Builder Methods

REST API

Orderbook
GET
Get order book summary
POST
Get multiple order books summaries by request

Pricing
GET
Get market price
GET
Get multiple market prices
POST
Get multiple market prices by request
GET
Get midpoint price
GET
Get price history for a traded token

Spreads
POST
Get bid-ask spreads

Historical Timeseries Data
GET
Historical Timeseries Data

Order Management
Orders Overview
Place Single Order
Place Multiple Orders (Batching)
Get Order
Get Active Orders
Check Order Reward Scoring
Cancel Orders(s)
Onchain Order Info

Trades
Trades Overview
Get Trades
Websocket
WSS Overview
WSS Quickstart
WSS Authentication
User Channel
Market Channel

Sports Websocket
Overview
Message Format
Quickstart
Real Time Data Stream
RTDS Overview
RTDS Crypto Prices
RTDS Comments
Gamma Structure
Overview
Gamma Structure
Fetching Markets
Gamma Endpoints

Gamma Status
GET
Gamma API Health check

Sports
GET
List teams
GET
Get sports metadata information
GET
Get valid sports market types

Tags
GET
List tags
GET
Get tag by id
GET
Get tag by slug
GET
Get related tags (relationships) by tag id
GET
Get related tags (relationships) by tag slug
GET
Get tags related to a tag id
GET
Get tags related to a tag slug

Events
GET
List events
GET
Get event by id
GET
Get event tags
GET
Get event by slug

Markets
GET
List markets
GET
Get market by id
GET
Get market tags by id
GET
Get market by slug

Series
GET
List series
GET
Get series by id

Comments
GET
List comments
GET
Get comments by comment id
GET
Get comments by user address

Profiles
GET
Get public profile by wallet address

Search
GET
Search markets, events, and profiles
Data-API

Data API Status
GET
Data API Health check

Core

Misc

Builders
Bridge & Swap
Overview

Bridge
Subgraph
Overview
Resolution
Resolution
Conditional Token Frameworks
Overview
Splitting USDC
Merging Tokens
Reedeeming Tokens
Deployment and Additional Information
Proxy Wallets
Proxy wallet
Negative Risk
Overview
Data API Health check

curl --request GET \
  --url https://data-api.polymarket.com/

200
{
  "data": "OK"
}
Data API Status
Data API Health check
GET

Try it
Response
200 - application/json
OK

​
data
string
Example:
"OK"

Search markets, events, and profiles
Get current positions for a user
Ask a question...

github
Powered by
Data API Health check - Polymarket Documentation

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.polymarket.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get current positions for a user

> Returns positions filtered by user and optional filters.



## OpenAPI

````yaml api-reference/data-api-openapi.yaml get /positions
openapi: 3.0.3
info:
  title: Polymarket Data API
  version: 1.0.0
  description: >
    HTTP API for Polymarket data. This specification documents all public
    routes.
servers:
  - url: https://data-api.polymarket.com
    description: Relative server (same host)
security: []
tags:
  - name: Data API Status
    description: Data API health check
  - name: Core
  - name: Builders
  - name: Misc
paths:
  /positions:
    get:
      tags:
        - Core
      summary: Get current positions for a user
      description: Returns positions filtered by user and optional filters.
      parameters:
        - in: query
          name: user
          required: true
          schema:
            $ref: '#/components/schemas/Address'
          description: User address (required)
        - in: query
          name: market
          style: form
          explode: false
          schema:
            type: array
            items:
              $ref: '#/components/schemas/Hash64'
          description: >-
            Comma-separated list of condition IDs. Mutually exclusive with
            eventId.
        - in: query
          name: eventId
          style: form
          explode: false
          schema:
            type: array
            items:
              type: integer
              minimum: 1
          description: Comma-separated list of event IDs. Mutually exclusive with market.
        - in: query
          name: sizeThreshold
          schema:
            type: number
            default: 1
            minimum: 0
        - in: query
          name: redeemable
          schema:
            type: boolean
            default: false
        - in: query
          name: mergeable
          schema:
            type: boolean
            default: false
        - in: query
          name: limit
          schema:
            type: integer
            default: 100
            minimum: 0
            maximum: 500
        - in: query
          name: offset
          schema:
            type: integer
            default: 0
            minimum: 0
            maximum: 10000
        - in: query
          name: sortBy
          schema:
            type: string
            enum:
              - CURRENT
              - INITIAL
              - TOKENS
              - CASHPNL
              - PERCENTPNL
              - TITLE
              - RESOLVING
              - PRICE
              - AVGPRICE
            default: TOKENS
        - in: query
          name: sortDirection
          schema:
            type: string
            enum:
              - ASC
              - DESC
            default: DESC
        - in: query
          name: title
          schema:
            type: string
            maxLength: 100
      responses:
        '200':
          description: Success
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Position'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '401':
          description: Unauthorized
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '500':
          description: Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
components:
  schemas:
    Address:
      type: string
      description: User Profile Address (0x-prefixed, 40 hex chars)
      pattern: ^0x[a-fA-F0-9]{40}$
      example: '0x56687bf447db6ffa42ffe2204a05edaa20f55839'
    Hash64:
      type: string
      description: 0x-prefixed 64-hex string
      pattern: ^0x[a-fA-F0-9]{64}$
      example: '0xdd22472e552920b8438158ea7238bfadfa4f736aa4cee91a6b86c39ead110917'
    Position:
      type: object
      properties:
        proxyWallet:
          $ref: '#/components/schemas/Address'
        asset:
          type: string
        conditionId:
          $ref: '#/components/schemas/Hash64'
        size:
          type: number
        avgPrice:
          type: number
        initialValue:
          type: number
        currentValue:
          type: number
        cashPnl:
          type: number
        percentPnl:
          type: number
        totalBought:
          type: number
        realizedPnl:
          type: number
        percentRealizedPnl:
          type: number
        curPrice:
          type: number
        redeemable:
          type: boolean
        mergeable:
          type: boolean
        title:
          type: string
        slug:
          type: string
        icon:
          type: string
        eventSlug:
          type: string
        outcome:
          type: string
        outcomeIndex:
          type: integer
        oppositeOutcome:
          type: string
        oppositeAsset:
          type: string
        endDate:
          type: string
        negativeRisk:
          type: boolean
    ErrorResponse:
      type: object
      properties:
        error:
          type: string
      required:
        - error

````

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.polymarket.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get trades for a user or markets



## OpenAPI

````yaml api-reference/data-api-openapi.yaml get /trades
openapi: 3.0.3
info:
  title: Polymarket Data API
  version: 1.0.0
  description: >
    HTTP API for Polymarket data. This specification documents all public
    routes.
servers:
  - url: https://data-api.polymarket.com
    description: Relative server (same host)
security: []
tags:
  - name: Data API Status
    description: Data API health check
  - name: Core
  - name: Builders
  - name: Misc
paths:
  /trades:
    get:
      tags:
        - Core
      summary: Get trades for a user or markets
      parameters:
        - in: query
          name: limit
          schema:
            type: integer
            default: 100
            minimum: 0
            maximum: 10000
        - in: query
          name: offset
          schema:
            type: integer
            default: 0
            minimum: 0
            maximum: 10000
        - in: query
          name: takerOnly
          schema:
            type: boolean
            default: true
        - in: query
          name: filterType
          schema:
            type: string
            enum:
              - CASH
              - TOKENS
          description: Must be provided together with filterAmount.
        - in: query
          name: filterAmount
          schema:
            type: number
            minimum: 0
          description: Must be provided together with filterType.
        - in: query
          name: market
          style: form
          explode: false
          schema:
            type: array
            items:
              $ref: '#/components/schemas/Hash64'
          description: >-
            Comma-separated list of condition IDs. Mutually exclusive with
            eventId.
        - in: query
          name: eventId
          style: form
          explode: false
          schema:
            type: array
            items:
              type: integer
              minimum: 1
          description: Comma-separated list of event IDs. Mutually exclusive with market.
        - in: query
          name: user
          schema:
            $ref: '#/components/schemas/Address'
        - in: query
          name: side
          schema:
            type: string
            enum:
              - BUY
              - SELL
      responses:
        '200':
          description: Success
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Trade'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '401':
          description: Unauthorized
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '500':
          description: Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
components:
  schemas:
    Hash64:
      type: string
      description: 0x-prefixed 64-hex string
      pattern: ^0x[a-fA-F0-9]{64}$
      example: '0xdd22472e552920b8438158ea7238bfadfa4f736aa4cee91a6b86c39ead110917'
    Address:
      type: string
      description: User Profile Address (0x-prefixed, 40 hex chars)
      pattern: ^0x[a-fA-F0-9]{40}$
      example: '0x56687bf447db6ffa42ffe2204a05edaa20f55839'
    Trade:
      type: object
      properties:
        proxyWallet:
          $ref: '#/components/schemas/Address'
        side:
          type: string
          enum:
            - BUY
            - SELL
        asset:
          type: string
        conditionId:
          $ref: '#/components/schemas/Hash64'
        size:
          type: number
        price:
          type: number
        timestamp:
          type: integer
          format: int64
        title:
          type: string
        slug:
          type: string
        icon:
          type: string
        eventSlug:
          type: string
        outcome:
          type: string
        outcomeIndex:
          type: integer
        name:
          type: string
        pseudonym:
          type: string
        bio:
          type: string
        profileImage:
          type: string
        profileImageOptimized:
          type: string
        transactionHash:
          type: string
    ErrorResponse:
      type: object
      properties:
        error:
          type: string
      required:
        - error

````

Skip to main content
Polymarket Documentation home pagedark logo

Search...
Ctrl K

Ask AI
Main Site

User Guide
For Developers
Changelog
Polymarket
Discord Community
Twitter
Developer Quickstart
Developer Quickstart
Fetching Market Data
Placing Your First Order
Glossary
API Rate Limits
Endpoints
Market Makers
Market Maker Introduction
Setup
Trading
Liquidity Rewards
Maker Rebates Program
Data Feeds
Inventory Management
Polymarket Builders Program
Builder Program Introduction
Builder Tiers
Builder Profile & Keys
Order Attribution
Relayer Client
Examples
Central Limit Order Book
CLOB Introduction
Status
Quickstart
Authentication
Geographic Restrictions

Client
Methods Overview
Public Methods
L1 Methods
L2 Methods
Builder Methods

REST API

Orderbook
GET
Get order book summary
POST
Get multiple order books summaries by request

Pricing
GET
Get market price
GET
Get multiple market prices
POST
Get multiple market prices by request
GET
Get midpoint price
GET
Get price history for a traded token

Spreads
POST
Get bid-ask spreads

Historical Timeseries Data
GET
Historical Timeseries Data

Order Management
Orders Overview
Place Single Order
Place Multiple Orders (Batching)
Get Order
Get Active Orders
Check Order Reward Scoring
Cancel Orders(s)
Onchain Order Info

Trades
Trades Overview
Get Trades
Websocket
WSS Overview
WSS Quickstart
WSS Authentication
User Channel
Market Channel

Sports Websocket
Overview
Message Format
Quickstart
Real Time Data Stream
RTDS Overview
RTDS Crypto Prices
RTDS Comments
Gamma Structure
Overview
Gamma Structure
Fetching Markets
Gamma Endpoints

Gamma Status
GET
Gamma API Health check

Sports
GET
List teams
GET
Get sports metadata information
GET
Get valid sports market types

Tags
GET
List tags
GET
Get tag by id
GET
Get tag by slug
GET
Get related tags (relationships) by tag id
GET
Get related tags (relationships) by tag slug
GET
Get tags related to a tag id
GET
Get tags related to a tag slug

Events
GET
List events
GET
Get event by id
GET
Get event tags
GET
Get event by slug

Markets
GET
List markets
GET
Get market by id
GET
Get market tags by id
GET
Get market by slug

Series
GET
List series
GET
Get series by id

Comments
GET
List comments
GET
Get comments by comment id
GET
Get comments by user address

Profiles
GET
Get public profile by wallet address

Search
GET
Search markets, events, and profiles
Data-API

Data API Status
GET
Data API Health check

Core
GET
Get current positions for a user
GET
Get trades for a user or markets
GET
Get user activity
GET
Get top holders for markets
GET
Get total value of a user's positions
GET
Get closed positions for a user
GET
Get trader leaderboard rankings

Misc

Builders
Bridge & Swap
Overview

Bridge
Subgraph
Overview
Resolution
Resolution
Conditional Token Frameworks
Overview
Splitting USDC
Merging Tokens
Reedeeming Tokens
Deployment and Additional Information
Proxy Wallets
Proxy wallet
Negative Risk
Overview
Get user activity

curl --request GET \
  --url 'https://data-api.polymarket.com/activity?limit=100&sortBy=TIMESTAMP&sortDirection=DESC'

200

400

401

500
[
  {
    "proxyWallet": "0x56687bf447db6ffa42ffe2204a05edaa20f55839",
    "timestamp": 123,
    "conditionId": "0xdd22472e552920b8438158ea7238bfadfa4f736aa4cee91a6b86c39ead110917",
    "type": "TRADE",
    "size": 123,
    "usdcSize": 123,
    "transactionHash": "<string>",
    "price": 123,
    "asset": "<string>",
    "side": "BUY",
    "outcomeIndex": 123,
    "title": "<string>",
    "slug": "<string>",
    "icon": "<string>",
    "eventSlug": "<string>",
    "outcome": "<string>",
    "name": "<string>",
    "pseudonym": "<string>",
    "bio": "<string>",
    "profileImage": "<string>",
    "profileImageOptimized": "<string>"
  }
]
Core
Get user activity
Returns on-chain activity for a user.

GET
/
activity

Try it
Query Parameters
​
limit
integerdefault:100
Required range: 0 <= x <= 500
​
offset
integerdefault:0
Required range: 0 <= x <= 10000
​
user
stringrequired
User Profile Address (0x-prefixed, 40 hex chars)

Example:
"0x56687bf447db6ffa42ffe2204a05edaa20f55839"

​
market
string[]
Comma-separated list of condition IDs. Mutually exclusive with eventId.

0x-prefixed 64-hex string

​
eventId
integer[]
Comma-separated list of event IDs. Mutually exclusive with market.

Required range: x >= 1
​
type
enum<string>[]
Available options: TRADE, SPLIT, MERGE, REDEEM, REWARD, CONVERSION, MAKER_REBATE 
​
start
integer
Required range: x >= 0
​
end
integer
Required range: x >= 0
​
sortBy
enum<string>default:TIMESTAMP
Available options: TIMESTAMP, TOKENS, CASH 
​
sortDirection
enum<string>default:DESC
Available options: ASC, DESC 
​
side
enum<string>
Available options: BUY, SELL 
Response

200

application/json
Success

​
proxyWallet
string
User Profile Address (0x-prefixed, 40 hex chars)

Example:
"0x56687bf447db6ffa42ffe2204a05edaa20f55839"

​
timestamp
integer<int64>
​
conditionId
string
0x-prefixed 64-hex string

Example:
"0xdd22472e552920b8438158ea7238bfadfa4f736aa4cee91a6b86c39ead110917"

​
type
enum<string>
Available options: TRADE, SPLIT, MERGE, REDEEM, REWARD, CONVERSION, MAKER_REBATE 
​
size
number
​
usdcSize
number
​
transactionHash
string
​
price
number
​
asset
string
​
side
enum<string>
Available options: BUY, SELL 
​
outcomeIndex
integer
​
title
string
​
slug
string
​
icon
string
​
eventSlug
string
​
outcome
string
​
name
string
​
pseudonym
string
​
bio
string
​
profileImage
string
​
profileImageOptimized
string
Get trades for a user or markets
Get top holders for markets
Ask a question...

github
Powered by
Get user activity - Polymarket Documentation

Skip to main content
Polymarket Documentation home pagedark logo

Search...
Ctrl K

Ask AI
Main Site

User Guide
For Developers
Changelog
Polymarket
Discord Community
Twitter
Developer Quickstart
Developer Quickstart
Fetching Market Data
Placing Your First Order
Glossary
API Rate Limits
Endpoints
Market Makers
Market Maker Introduction
Setup
Trading
Liquidity Rewards
Maker Rebates Program
Data Feeds
Inventory Management
Polymarket Builders Program
Builder Program Introduction
Builder Tiers
Builder Profile & Keys
Order Attribution
Relayer Client
Examples
Central Limit Order Book
CLOB Introduction
Status
Quickstart
Authentication
Geographic Restrictions

Client
Methods Overview
Public Methods
L1 Methods
L2 Methods
Builder Methods

REST API

Orderbook
GET
Get order book summary
POST
Get multiple order books summaries by request

Pricing
GET
Get market price
GET
Get multiple market prices
POST
Get multiple market prices by request
GET
Get midpoint price
GET
Get price history for a traded token

Spreads
POST
Get bid-ask spreads

Historical Timeseries Data
GET
Historical Timeseries Data

Order Management
Orders Overview
Place Single Order
Place Multiple Orders (Batching)
Get Order
Get Active Orders
Check Order Reward Scoring
Cancel Orders(s)
Onchain Order Info

Trades
Trades Overview
Get Trades
Websocket
WSS Overview
WSS Quickstart
WSS Authentication
User Channel
Market Channel

Sports Websocket
Overview
Message Format
Quickstart
Real Time Data Stream
RTDS Overview
RTDS Crypto Prices
RTDS Comments
Gamma Structure
Overview
Gamma Structure
Fetching Markets
Gamma Endpoints

Gamma Status
GET
Gamma API Health check

Sports
GET
List teams
GET
Get sports metadata information
GET
Get valid sports market types

Tags
GET
List tags
GET
Get tag by id
GET
Get tag by slug
GET
Get related tags (relationships) by tag id
GET
Get related tags (relationships) by tag slug
GET
Get tags related to a tag id
GET
Get tags related to a tag slug

Events
GET
List events
GET
Get event by id
GET
Get event tags
GET
Get event by slug

Markets
GET
List markets
GET
Get market by id
GET
Get market tags by id
GET
Get market by slug

Series
GET
List series
GET
Get series by id

Comments
GET
List comments
GET
Get comments by comment id
GET
Get comments by user address

Profiles
GET
Get public profile by wallet address

Search
GET
Search markets, events, and profiles
Data-API

Data API Status
GET
Data API Health check

Core
GET
Get current positions for a user
GET
Get trades for a user or markets
GET
Get user activity
GET
Get top holders for markets
GET
Get total value of a user's positions
GET
Get closed positions for a user
GET
Get trader leaderboard rankings

Misc

Builders
Bridge & Swap
Overview

Bridge
Subgraph
Overview
Resolution
Resolution
Conditional Token Frameworks
Overview
Splitting USDC
Merging Tokens
Reedeeming Tokens
Deployment and Additional Information
Proxy Wallets
Proxy wallet
Negative Risk
Overview
Get top holders for markets

curl --request GET \
  --url 'https://data-api.polymarket.com/holders?limit=20&minBalance=1'

200

400

401

500
[
  {
    "token": "<string>",
    "holders": [
      {
        "proxyWallet": "0x56687bf447db6ffa42ffe2204a05edaa20f55839",
        "bio": "<string>",
        "asset": "<string>",
        "pseudonym": "<string>",
        "amount": 123,
        "displayUsernamePublic": true,
        "outcomeIndex": 123,
        "name": "<string>",
        "profileImage": "<string>",
        "profileImageOptimized": "<string>"
      }
    ]
  }
]
Core
Get top holders for markets
GET
/
holders

Try it
Query Parameters
​
limit
integerdefault:20
Maximum number of holders to return per token. Capped at 20.

Required range: 0 <= x <= 20
​
market
string[]required
Comma-separated list of condition IDs.

0x-prefixed 64-hex string

​
minBalance
integerdefault:1
Required range: 0 <= x <= 999999
Response

200

application/json
Success

​
token
string
​
holders
object[]
Show child attributes

Get user activity
Get total value of a user's positions
Ask a question...

github
Powered by
Get top holders for markets - Polymarket Documentation

Skip to main content
Polymarket Documentation home pagedark logo

Search...
Ctrl K

Ask AI
Main Site

User Guide
For Developers
Changelog
Polymarket
Discord Community
Twitter
Developer Quickstart
Developer Quickstart
Fetching Market Data
Placing Your First Order
Glossary
API Rate Limits
Endpoints
Market Makers
Market Maker Introduction
Setup
Trading
Liquidity Rewards
Maker Rebates Program
Data Feeds
Inventory Management
Polymarket Builders Program
Builder Program Introduction
Builder Tiers
Builder Profile & Keys
Order Attribution
Relayer Client
Examples
Central Limit Order Book
CLOB Introduction
Status
Quickstart
Authentication
Geographic Restrictions

Client
Methods Overview
Public Methods
L1 Methods
L2 Methods
Builder Methods

REST API

Orderbook
GET
Get order book summary
POST
Get multiple order books summaries by request

Pricing
GET
Get market price
GET
Get multiple market prices
POST
Get multiple market prices by request
GET
Get midpoint price
GET
Get price history for a traded token

Spreads
POST
Get bid-ask spreads

Historical Timeseries Data
GET
Historical Timeseries Data

Order Management
Orders Overview
Place Single Order
Place Multiple Orders (Batching)
Get Order
Get Active Orders
Check Order Reward Scoring
Cancel Orders(s)
Onchain Order Info

Trades
Trades Overview
Get Trades
Websocket
WSS Overview
WSS Quickstart
WSS Authentication
User Channel
Market Channel

Sports Websocket
Overview
Message Format
Quickstart
Real Time Data Stream
RTDS Overview
RTDS Crypto Prices
RTDS Comments
Gamma Structure
Overview
Gamma Structure
Fetching Markets
Gamma Endpoints

Gamma Status
GET
Gamma API Health check

Sports
GET
List teams
GET
Get sports metadata information
GET
Get valid sports market types

Tags
GET
List tags
GET
Get tag by id
GET
Get tag by slug
GET
Get related tags (relationships) by tag id
GET
Get related tags (relationships) by tag slug
GET
Get tags related to a tag id
GET
Get tags related to a tag slug

Events
GET
List events
GET
Get event by id
GET
Get event tags
GET
Get event by slug

Markets
GET
List markets
GET
Get market by id
GET
Get market tags by id
GET
Get market by slug

Series
GET
List series
GET
Get series by id

Comments
GET
List comments
GET
Get comments by comment id
GET
Get comments by user address

Profiles
GET
Get public profile by wallet address

Search
GET
Search markets, events, and profiles
Data-API

Data API Status
GET
Data API Health check

Core
GET
Get current positions for a user
GET
Get trades for a user or markets
GET
Get user activity
GET
Get top holders for markets
GET
Get total value of a user's positions
GET
Get closed positions for a user
GET
Get trader leaderboard rankings

Misc

Builders
Bridge & Swap
Overview

Bridge
Subgraph
Overview
Resolution
Resolution
Conditional Token Frameworks
Overview
Splitting USDC
Merging Tokens
Reedeeming Tokens
Deployment and Additional Information
Proxy Wallets
Proxy wallet
Negative Risk
Overview
Get total value of a user's positions

curl --request GET \
  --url https://data-api.polymarket.com/value

200

400

500
[
  {
    "user": "0x56687bf447db6ffa42ffe2204a05edaa20f55839",
    "value": 123
  }
]
Core
Get total value of a user's positions
GET
/
value

Try it
Query Parameters
​
user
stringrequired
User Profile Address (0x-prefixed, 40 hex chars)

Example:
"0x56687bf447db6ffa42ffe2204a05edaa20f55839"

​
market
string[]
0x-prefixed 64-hex string

Response

200

application/json
Success

​
user
string
User Profile Address (0x-prefixed, 40 hex chars)

Example:
"0x56687bf447db6ffa42ffe2204a05edaa20f55839"

​
value
number
Get top holders for markets
Get closed positions for a user
Ask a question...

github
Powered by
Get total value of a user's positions - Polymarket Documentation

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.polymarket.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get closed positions for a user

> Fetches closed positions for a user(address)



## OpenAPI

````yaml api-reference/data-api-openapi.yaml get /closed-positions
openapi: 3.0.3
info:
  title: Polymarket Data API
  version: 1.0.0
  description: >
    HTTP API for Polymarket data. This specification documents all public
    routes.
servers:
  - url: https://data-api.polymarket.com
    description: Relative server (same host)
security: []
tags:
  - name: Data API Status
    description: Data API health check
  - name: Core
  - name: Builders
  - name: Misc
paths:
  /closed-positions:
    get:
      tags:
        - Core
      summary: Get closed positions for a user
      description: Fetches closed positions for a user(address)
      parameters:
        - in: query
          name: user
          required: true
          schema:
            $ref: '#/components/schemas/Address'
          description: The address of the user in question
        - in: query
          name: market
          style: form
          explode: false
          schema:
            type: array
            items:
              $ref: '#/components/schemas/Hash64'
          description: >-
            The conditionId of the market in question. Supports multiple csv
            separated values. Cannot be used with the eventId param.
        - in: query
          name: title
          schema:
            type: string
            maxLength: 100
          description: Filter by market title
        - in: query
          name: eventId
          style: form
          explode: false
          schema:
            type: array
            items:
              type: integer
              minimum: 1
          description: >-
            The event id of the event in question. Supports multiple csv
            separated values. Returns positions for all markets for those event
            ids. Cannot be used with the market param.
        - in: query
          name: limit
          schema:
            type: integer
            default: 10
            minimum: 0
            maximum: 50
          description: The max number of positions to return
        - in: query
          name: offset
          schema:
            type: integer
            default: 0
            minimum: 0
            maximum: 100000
          description: The starting index for pagination
        - in: query
          name: sortBy
          schema:
            type: string
            enum:
              - REALIZEDPNL
              - TITLE
              - PRICE
              - AVGPRICE
              - TIMESTAMP
            default: REALIZEDPNL
          description: The sort criteria
        - in: query
          name: sortDirection
          schema:
            type: string
            enum:
              - ASC
              - DESC
            default: DESC
          description: The sort direction
      responses:
        '200':
          description: Success
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/ClosedPosition'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '401':
          description: Unauthorized
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '500':
          description: Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
components:
  schemas:
    Address:
      type: string
      description: User Profile Address (0x-prefixed, 40 hex chars)
      pattern: ^0x[a-fA-F0-9]{40}$
      example: '0x56687bf447db6ffa42ffe2204a05edaa20f55839'
    Hash64:
      type: string
      description: 0x-prefixed 64-hex string
      pattern: ^0x[a-fA-F0-9]{64}$
      example: '0xdd22472e552920b8438158ea7238bfadfa4f736aa4cee91a6b86c39ead110917'
    ClosedPosition:
      type: object
      properties:
        proxyWallet:
          $ref: '#/components/schemas/Address'
        asset:
          type: string
        conditionId:
          $ref: '#/components/schemas/Hash64'
        avgPrice:
          type: number
        totalBought:
          type: number
        realizedPnl:
          type: number
        curPrice:
          type: number
        timestamp:
          type: integer
          format: int64
        title:
          type: string
        slug:
          type: string
        icon:
          type: string
        eventSlug:
          type: string
        outcome:
          type: string
        outcomeIndex:
          type: integer
        oppositeOutcome:
          type: string
        oppositeAsset:
          type: string
        endDate:
          type: string
    ErrorResponse:
      type: object
      properties:
        error:
          type: string
      required:
        - error

````

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.polymarket.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get trader leaderboard rankings

> Returns trader leaderboard rankings filtered by category, time period, and ordering.



## OpenAPI

````yaml api-reference/data-api-openapi.yaml get /v1/leaderboard
openapi: 3.0.3
info:
  title: Polymarket Data API
  version: 1.0.0
  description: >
    HTTP API for Polymarket data. This specification documents all public
    routes.
servers:
  - url: https://data-api.polymarket.com
    description: Relative server (same host)
security: []
tags:
  - name: Data API Status
    description: Data API health check
  - name: Core
  - name: Builders
  - name: Misc
paths:
  /v1/leaderboard:
    get:
      tags:
        - Core
      summary: Get trader leaderboard rankings
      description: >-
        Returns trader leaderboard rankings filtered by category, time period,
        and ordering.
      parameters:
        - in: query
          name: category
          schema:
            type: string
            enum:
              - OVERALL
              - POLITICS
              - SPORTS
              - CRYPTO
              - CULTURE
              - MENTIONS
              - WEATHER
              - ECONOMICS
              - TECH
              - FINANCE
            default: OVERALL
          description: Market category for the leaderboard
        - in: query
          name: timePeriod
          schema:
            type: string
            enum:
              - DAY
              - WEEK
              - MONTH
              - ALL
            default: DAY
          description: Time period for leaderboard results
        - in: query
          name: orderBy
          schema:
            type: string
            enum:
              - PNL
              - VOL
            default: PNL
          description: Leaderboard ordering criteria
        - in: query
          name: limit
          schema:
            type: integer
            default: 25
            minimum: 1
            maximum: 50
          description: Max number of leaderboard traders to return
        - in: query
          name: offset
          schema:
            type: integer
            default: 0
            minimum: 0
            maximum: 1000
          description: Starting index for pagination
        - in: query
          name: user
          schema:
            $ref: '#/components/schemas/Address'
          description: Limit leaderboard to a single user by address
        - in: query
          name: userName
          schema:
            type: string
          description: Limit leaderboard to a single username
      responses:
        '200':
          description: Success
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/TraderLeaderboardEntry'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '500':
          description: Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
components:
  schemas:
    Address:
      type: string
      description: User Profile Address (0x-prefixed, 40 hex chars)
      pattern: ^0x[a-fA-F0-9]{40}$
      example: '0x56687bf447db6ffa42ffe2204a05edaa20f55839'
    TraderLeaderboardEntry:
      type: object
      properties:
        rank:
          type: string
          description: The rank position of the trader
        proxyWallet:
          $ref: '#/components/schemas/Address'
        userName:
          type: string
          description: The trader's username
        vol:
          type: number
          description: Trading volume for this trader
        pnl:
          type: number
          description: Profit and loss for this trader
        profileImage:
          type: string
          description: URL to the trader's profile image
        xUsername:
          type: string
          description: The trader's X (Twitter) username
        verifiedBadge:
          type: boolean
          description: Whether the trader has a verified badge
    ErrorResponse:
      type: object
      properties:
        error:
          type: string
      required:
        - error

````

Skip to main content
Polymarket Documentation home pagedark logo

Search...
Ctrl K

Ask AI
Main Site

User Guide
For Developers
Changelog
Polymarket
Discord Community
Twitter
Developer Quickstart
Developer Quickstart
Fetching Market Data
Placing Your First Order
Glossary
API Rate Limits
Endpoints
Market Makers
Market Maker Introduction
Setup
Trading
Liquidity Rewards
Maker Rebates Program
Data Feeds
Inventory Management
Polymarket Builders Program
Builder Program Introduction
Builder Tiers
Builder Profile & Keys
Order Attribution
Relayer Client
Examples
Central Limit Order Book
CLOB Introduction
Status
Quickstart
Authentication
Geographic Restrictions

Client
Methods Overview
Public Methods
L1 Methods
L2 Methods
Builder Methods

REST API

Orderbook
GET
Get order book summary
POST
Get multiple order books summaries by request

Pricing
GET
Get market price
GET
Get multiple market prices
POST
Get multiple market prices by request
GET
Get midpoint price
GET
Get price history for a traded token

Spreads
POST
Get bid-ask spreads

Historical Timeseries Data
GET
Historical Timeseries Data

Order Management
Orders Overview
Place Single Order
Place Multiple Orders (Batching)
Get Order
Get Active Orders
Check Order Reward Scoring
Cancel Orders(s)
Onchain Order Info

Trades
Trades Overview
Get Trades
Websocket
WSS Overview
WSS Quickstart
WSS Authentication
User Channel
Market Channel

Sports Websocket
Overview
Message Format
Quickstart
Real Time Data Stream
RTDS Overview
RTDS Crypto Prices
RTDS Comments
Gamma Structure
Overview
Gamma Structure
Fetching Markets
Gamma Endpoints

Gamma Status
GET
Gamma API Health check

Sports
GET
List teams
GET
Get sports metadata information
GET
Get valid sports market types

Tags
GET
List tags
GET
Get tag by id
GET
Get tag by slug
GET
Get related tags (relationships) by tag id
GET
Get related tags (relationships) by tag slug
GET
Get tags related to a tag id
GET
Get tags related to a tag slug

Events
GET
List events
GET
Get event by id
GET
Get event tags
GET
Get event by slug

Markets
GET
List markets
GET
Get market by id
GET
Get market tags by id
GET
Get market by slug

Series
GET
List series
GET
Get series by id

Comments
GET
List comments
GET
Get comments by comment id
GET
Get comments by user address

Profiles
GET
Get public profile by wallet address

Search
GET
Search markets, events, and profiles
Data-API

Data API Status
GET
Data API Health check

Core
GET
Get current positions for a user
GET
Get trades for a user or markets
GET
Get user activity
GET
Get top holders for markets
GET
Get total value of a user's positions
GET
Get closed positions for a user
GET
Get trader leaderboard rankings

Misc
GET
Get total markets a user has traded
GET
Get open interest
GET
Get live volume for an event

Builders
Bridge & Swap
Overview

Bridge
Subgraph
Overview
Resolution
Resolution
Conditional Token Frameworks
Overview
Splitting USDC
Merging Tokens
Reedeeming Tokens
Deployment and Additional Information
Proxy Wallets
Proxy wallet
Negative Risk
Overview
Get total markets a user has traded

curl --request GET \
  --url https://data-api.polymarket.com/traded

200

400

401

500
{
  "user": "0x56687bf447db6ffa42ffe2204a05edaa20f55839",
  "traded": 123
}
Misc
Get total markets a user has traded
GET
/
traded

Try it
Query Parameters
​
user
stringrequired
User Profile Address (0x-prefixed, 40 hex chars)

Example:
"0x56687bf447db6ffa42ffe2204a05edaa20f55839"

Response

200

application/json
Success

​
user
string
User Profile Address (0x-prefixed, 40 hex chars)

Example:
"0x56687bf447db6ffa42ffe2204a05edaa20f55839"

​
traded
integer
Get trader leaderboard rankings
Get open interest
Ask a question...

github
Powered by
Get total markets a user has traded - Polymarket Documentation

Skip to main content
Polymarket Documentation home pagedark logo

Search...
Ctrl K

Ask AI
Main Site

User Guide
For Developers
Changelog
Polymarket
Discord Community
Twitter
Developer Quickstart
Developer Quickstart
Fetching Market Data
Placing Your First Order
Glossary
API Rate Limits
Endpoints
Market Makers
Market Maker Introduction
Setup
Trading
Liquidity Rewards
Maker Rebates Program
Data Feeds
Inventory Management
Polymarket Builders Program
Builder Program Introduction
Builder Tiers
Builder Profile & Keys
Order Attribution
Relayer Client
Examples
Central Limit Order Book
CLOB Introduction
Status
Quickstart
Authentication
Geographic Restrictions

Client
Methods Overview
Public Methods
L1 Methods
L2 Methods
Builder Methods

REST API

Orderbook
GET
Get order book summary
POST
Get multiple order books summaries by request

Pricing
GET
Get market price
GET
Get multiple market prices
POST
Get multiple market prices by request
GET
Get midpoint price
GET
Get price history for a traded token

Spreads
POST
Get bid-ask spreads

Historical Timeseries Data
GET
Historical Timeseries Data

Order Management
Orders Overview
Place Single Order
Place Multiple Orders (Batching)
Get Order
Get Active Orders
Check Order Reward Scoring
Cancel Orders(s)
Onchain Order Info

Trades
Trades Overview
Get Trades
Websocket
WSS Overview
WSS Quickstart
WSS Authentication
User Channel
Market Channel

Sports Websocket
Overview
Message Format
Quickstart
Real Time Data Stream
RTDS Overview
RTDS Crypto Prices
RTDS Comments
Gamma Structure
Overview
Gamma Structure
Fetching Markets
Gamma Endpoints

Gamma Status
GET
Gamma API Health check

Sports
GET
List teams
GET
Get sports metadata information
GET
Get valid sports market types

Tags
GET
List tags
GET
Get tag by id
GET
Get tag by slug
GET
Get related tags (relationships) by tag id
GET
Get related tags (relationships) by tag slug
GET
Get tags related to a tag id
GET
Get tags related to a tag slug

Events
GET
List events
GET
Get event by id
GET
Get event tags
GET
Get event by slug

Markets
GET
List markets
GET
Get market by id
GET
Get market tags by id
GET
Get market by slug

Series
GET
List series
GET
Get series by id

Comments
GET
List comments
GET
Get comments by comment id
GET
Get comments by user address

Profiles
GET
Get public profile by wallet address

Search
GET
Search markets, events, and profiles
Data-API

Data API Status
GET
Data API Health check

Core
GET
Get current positions for a user
GET
Get trades for a user or markets
GET
Get user activity
GET
Get top holders for markets
GET
Get total value of a user's positions
GET
Get closed positions for a user
GET
Get trader leaderboard rankings

Misc
GET
Get total markets a user has traded
GET
Get open interest
GET
Get live volume for an event

Builders
Bridge & Swap
Overview

Bridge
Subgraph
Overview
Resolution
Resolution
Conditional Token Frameworks
Overview
Splitting USDC
Merging Tokens
Reedeeming Tokens
Deployment and Additional Information
Proxy Wallets
Proxy wallet
Negative Risk
Overview
Get open interest

curl --request GET \
  --url https://data-api.polymarket.com/oi

200

400

500
[
  {
    "market": "0xdd22472e552920b8438158ea7238bfadfa4f736aa4cee91a6b86c39ead110917",
    "value": 123
  }
]
Misc
Get open interest
GET
/
oi

Try it
Query Parameters
​
market
string[]
0x-prefixed 64-hex string

Response

200

application/json
Success

​
market
string
0x-prefixed 64-hex string

Example:
"0xdd22472e552920b8438158ea7238bfadfa4f736aa4cee91a6b86c39ead110917"

​
value
number
Get total markets a user has traded
Get live volume for an event
Ask a question...

github
Powered by
Get open interest - Polymarket Documentation

Skip to main content
Polymarket Documentation home pagedark logo

Search...
Ctrl K

Ask AI
Main Site

User Guide
For Developers
Changelog
Polymarket
Discord Community
Twitter
Developer Quickstart
Developer Quickstart
Fetching Market Data
Placing Your First Order
Glossary
API Rate Limits
Endpoints
Market Makers
Market Maker Introduction
Setup
Trading
Liquidity Rewards
Maker Rebates Program
Data Feeds
Inventory Management
Polymarket Builders Program
Builder Program Introduction
Builder Tiers
Builder Profile & Keys
Order Attribution
Relayer Client
Examples
Central Limit Order Book
CLOB Introduction
Status
Quickstart
Authentication
Geographic Restrictions

Client
Methods Overview
Public Methods
L1 Methods
L2 Methods
Builder Methods

REST API

Orderbook
GET
Get order book summary
POST
Get multiple order books summaries by request

Pricing
GET
Get market price
GET
Get multiple market prices
POST
Get multiple market prices by request
GET
Get midpoint price
GET
Get price history for a traded token

Spreads
POST
Get bid-ask spreads

Historical Timeseries Data
GET
Historical Timeseries Data

Order Management
Orders Overview
Place Single Order
Place Multiple Orders (Batching)
Get Order
Get Active Orders
Check Order Reward Scoring
Cancel Orders(s)
Onchain Order Info

Trades
Trades Overview
Get Trades
Websocket
WSS Overview
WSS Quickstart
WSS Authentication
User Channel
Market Channel

Sports Websocket
Overview
Message Format
Quickstart
Real Time Data Stream
RTDS Overview
RTDS Crypto Prices
RTDS Comments
Gamma Structure
Overview
Gamma Structure
Fetching Markets
Gamma Endpoints

Gamma Status
GET
Gamma API Health check

Sports
GET
List teams
GET
Get sports metadata information
GET
Get valid sports market types

Tags
GET
List tags
GET
Get tag by id
GET
Get tag by slug
GET
Get related tags (relationships) by tag id
GET
Get related tags (relationships) by tag slug
GET
Get tags related to a tag id
GET
Get tags related to a tag slug

Events
GET
List events
GET
Get event by id
GET
Get event tags
GET
Get event by slug

Markets
GET
List markets
GET
Get market by id
GET
Get market tags by id
GET
Get market by slug

Series
GET
List series
GET
Get series by id

Comments
GET
List comments
GET
Get comments by comment id
GET
Get comments by user address

Profiles
GET
Get public profile by wallet address

Search
GET
Search markets, events, and profiles
Data-API

Data API Status
GET
Data API Health check

Core
GET
Get current positions for a user
GET
Get trades for a user or markets
GET
Get user activity
GET
Get top holders for markets
GET
Get total value of a user's positions
GET
Get closed positions for a user
GET
Get trader leaderboard rankings

Misc
GET
Get total markets a user has traded
GET
Get open interest
GET
Get live volume for an event

Builders
Bridge & Swap
Overview

Bridge
Subgraph
Overview
Resolution
Resolution
Conditional Token Frameworks
Overview
Splitting USDC
Merging Tokens
Reedeeming Tokens
Deployment and Additional Information
Proxy Wallets
Proxy wallet
Negative Risk
Overview
Get live volume for an event

curl --request GET \
  --url https://data-api.polymarket.com/live-volume

200

400

500
[
  {
    "total": 123,
    "markets": [
      {
        "market": "0xdd22472e552920b8438158ea7238bfadfa4f736aa4cee91a6b86c39ead110917",
        "value": 123
      }
    ]
  }
]
Misc
Get live volume for an event
GET
/
live-volume

Try it
Query Parameters
​
id
integerrequired
Required range: x >= 1
Response

200

application/json
Success

​
total
number
​
markets
object[]
Show child attributes

Get open interest
Get aggregated builder leaderboard
Ask a question...

github
Powered by
Get live volume for an event - Polymarket Documentation

Skip to main content
Polymarket Documentation home pagedark logo

Search...
Ctrl K

Ask AI
Main Site

User Guide
For Developers
Changelog
Polymarket
Discord Community
Twitter
Developer Quickstart
Developer Quickstart
Fetching Market Data
Placing Your First Order
Glossary
API Rate Limits
Endpoints
Market Makers
Market Maker Introduction
Setup
Trading
Liquidity Rewards
Maker Rebates Program
Data Feeds
Inventory Management
Polymarket Builders Program
Builder Program Introduction
Builder Tiers
Builder Profile & Keys
Order Attribution
Relayer Client
Examples
Central Limit Order Book
CLOB Introduction
Status
Quickstart
Authentication
Geographic Restrictions

Client
Methods Overview
Public Methods
L1 Methods
L2 Methods
Builder Methods

REST API

Orderbook
GET
Get order book summary
POST
Get multiple order books summaries by request

Pricing
GET
Get market price
GET
Get multiple market prices
POST
Get multiple market prices by request
GET
Get midpoint price
GET
Get price history for a traded token

Spreads
POST
Get bid-ask spreads

Historical Timeseries Data
GET
Historical Timeseries Data

Order Management
Orders Overview
Place Single Order
Place Multiple Orders (Batching)
Get Order
Get Active Orders
Check Order Reward Scoring
Cancel Orders(s)
Onchain Order Info

Trades
Trades Overview
Get Trades
Websocket
WSS Overview
WSS Quickstart
WSS Authentication
User Channel
Market Channel

Sports Websocket
Overview
Message Format
Quickstart
Real Time Data Stream
RTDS Overview
RTDS Crypto Prices
RTDS Comments
Gamma Structure
Overview
Gamma Structure
Fetching Markets
Gamma Endpoints

Gamma Status
GET
Gamma API Health check

Sports
GET
List teams
GET
Get sports metadata information
GET
Get valid sports market types

Tags
GET
List tags
GET
Get tag by id
GET
Get tag by slug
GET
Get related tags (relationships) by tag id
GET
Get related tags (relationships) by tag slug
GET
Get tags related to a tag id
GET
Get tags related to a tag slug

Events
GET
List events
GET
Get event by id
GET
Get event tags
GET
Get event by slug

Markets
GET
List markets
GET
Get market by id
GET
Get market tags by id
GET
Get market by slug

Series
GET
List series
GET
Get series by id

Comments
GET
List comments
GET
Get comments by comment id
GET
Get comments by user address

Profiles
GET
Get public profile by wallet address

Search
GET
Search markets, events, and profiles
Data-API

Data API Status
GET
Data API Health check

Core
GET
Get current positions for a user
GET
Get trades for a user or markets
GET
Get user activity
GET
Get top holders for markets
GET
Get total value of a user's positions
GET
Get closed positions for a user
GET
Get trader leaderboard rankings

Misc
GET
Get total markets a user has traded
GET
Get open interest
GET
Get live volume for an event

Builders
GET
Get aggregated builder leaderboard
GET
Get daily builder volume time-series
Bridge & Swap
Overview

Bridge
Subgraph
Overview
Resolution
Resolution
Conditional Token Frameworks
Overview
Splitting USDC
Merging Tokens
Reedeeming Tokens
Deployment and Additional Information
Proxy Wallets
Proxy wallet
Negative Risk
Overview
Get aggregated builder leaderboard

curl --request GET \
  --url 'https://data-api.polymarket.com/v1/builders/leaderboard?timePeriod=DAY&limit=25'

200

400

500
[
  {
    "rank": "<string>",
    "builder": "<string>",
    "volume": 123,
    "activeUsers": 123,
    "verified": true,
    "builderLogo": "<string>"
  }
]
Builders
Get aggregated builder leaderboard
Returns aggregated builder rankings with one entry per builder showing total for the specified time period. Supports pagination.

GET
/
v1
/
builders
/
leaderboard

Try it
Query Parameters
​
timePeriod
enum<string>default:DAY
The time period to aggregate results over.

Available options: DAY, WEEK, MONTH, ALL 
​
limit
integerdefault:25
Maximum number of builders to return

Required range: 0 <= x <= 50
​
offset
integerdefault:0
Starting index for pagination

Required range: 0 <= x <= 1000
Response

200

application/json
Success

​
rank
string
The rank position of the builder

​
builder
string
The builder name or identifier

​
volume
number
Total trading volume attributed to this builder

​
activeUsers
integer
Number of active users for this builder

​
verified
boolean
Whether the builder is verified

​
builderLogo
string
URL to the builder's logo image

Get live volume for an event
Get daily builder volume time-series
Ask a question...

github
Powered by
Get aggregated builder leaderboard - Polymarket Documentation

Skip to main content
Polymarket Documentation home pagedark logo

Search...
Ctrl K

Ask AI
Main Site

User Guide
For Developers
Changelog
Polymarket
Discord Community
Twitter
Developer Quickstart
Developer Quickstart
Fetching Market Data
Placing Your First Order
Glossary
API Rate Limits
Endpoints
Market Makers
Market Maker Introduction
Setup
Trading
Liquidity Rewards
Maker Rebates Program
Data Feeds
Inventory Management
Polymarket Builders Program
Builder Program Introduction
Builder Tiers
Builder Profile & Keys
Order Attribution
Relayer Client
Examples
Central Limit Order Book
CLOB Introduction
Status
Quickstart
Authentication
Geographic Restrictions

Client
Methods Overview
Public Methods
L1 Methods
L2 Methods
Builder Methods

REST API

Orderbook
GET
Get order book summary
POST
Get multiple order books summaries by request

Pricing
GET
Get market price
GET
Get multiple market prices
POST
Get multiple market prices by request
GET
Get midpoint price
GET
Get price history for a traded token

Spreads
POST
Get bid-ask spreads

Historical Timeseries Data
GET
Historical Timeseries Data

Order Management
Orders Overview
Place Single Order
Place Multiple Orders (Batching)
Get Order
Get Active Orders
Check Order Reward Scoring
Cancel Orders(s)
Onchain Order Info

Trades
Trades Overview
Get Trades
Websocket
WSS Overview
WSS Quickstart
WSS Authentication
User Channel
Market Channel

Sports Websocket
Overview
Message Format
Quickstart
Real Time Data Stream
RTDS Overview
RTDS Crypto Prices
RTDS Comments
Gamma Structure
Overview
Gamma Structure
Fetching Markets
Gamma Endpoints

Gamma Status
GET
Gamma API Health check

Sports
GET
List teams
GET
Get sports metadata information
GET
Get valid sports market types

Tags
GET
List tags
GET
Get tag by id
GET
Get tag by slug
GET
Get related tags (relationships) by tag id
GET
Get related tags (relationships) by tag slug
GET
Get tags related to a tag id
GET
Get tags related to a tag slug

Events
GET
List events
GET
Get event by id
GET
Get event tags
GET
Get event by slug

Markets
GET
List markets
GET
Get market by id
GET
Get market tags by id
GET
Get market by slug

Series
GET
List series
GET
Get series by id

Comments
GET
List comments
GET
Get comments by comment id
GET
Get comments by user address

Profiles
GET
Get public profile by wallet address

Search
GET
Search markets, events, and profiles
Data-API

Data API Status
GET
Data API Health check

Core
GET
Get current positions for a user
GET
Get trades for a user or markets
GET
Get user activity
GET
Get top holders for markets
GET
Get total value of a user's positions
GET
Get closed positions for a user
GET
Get trader leaderboard rankings

Misc
GET
Get total markets a user has traded
GET
Get open interest
GET
Get live volume for an event

Builders
GET
Get aggregated builder leaderboard
GET
Get daily builder volume time-series
Bridge & Swap
Overview

Bridge
Subgraph
Overview
Resolution
Resolution
Conditional Token Frameworks
Overview
Splitting USDC
Merging Tokens
Reedeeming Tokens
Deployment and Additional Information
Proxy Wallets
Proxy wallet
Negative Risk
Overview
Get daily builder volume time-series

curl --request GET \
  --url 'https://data-api.polymarket.com/v1/builders/volume?timePeriod=DAY'

200

400

500
[
  {
    "dt": "2025-11-15T00:00:00Z",
    "builder": "<string>",
    "builderLogo": "<string>",
    "verified": true,
    "volume": 123,
    "activeUsers": 123,
    "rank": "<string>"
  }
]
Builders
Get daily builder volume time-series
Returns daily time-series volume data with multiple entries per builder (one per day), each including a dt timestamp. No pagination.

GET
/
v1
/
builders
/
volume

Try it
Query Parameters
​
timePeriod
enum<string>default:DAY
The time period to fetch daily records for.

Available options: DAY, WEEK, MONTH, ALL 
Response

200

application/json
Success - Returns array of daily volume records

​
dt
string<date-time>
The timestamp for this volume entry in ISO 8601 format

Example:
"2025-11-15T00:00:00Z"

​
builder
string
The builder name or identifier

​
builderLogo
string
URL to the builder's logo image

​
verified
boolean
Whether the builder is verified

​
volume
number
Trading volume for this builder on this date

​
activeUsers
integer
Number of active users for this builder on this date

​
rank
string
The rank position of the builder on this date

Get aggregated builder leaderboard
Overview
Ask a question...

github
Powered by
Get daily builder volume time-series - Polymarket Documentation

Skip to main content
Polymarket Documentation home pagedark logo

Search...
Ctrl K

Ask AI
Main Site

User Guide
For Developers
Changelog
Polymarket
Discord Community
Twitter
Developer Quickstart
Developer Quickstart
Fetching Market Data
Placing Your First Order
Glossary
API Rate Limits
Endpoints
Market Makers
Market Maker Introduction
Setup
Trading
Liquidity Rewards
Maker Rebates Program
Data Feeds
Inventory Management
Polymarket Builders Program
Builder Program Introduction
Builder Tiers
Builder Profile & Keys
Order Attribution
Relayer Client
Examples
Central Limit Order Book
CLOB Introduction
Status
Quickstart
Authentication
Geographic Restrictions

Client
Methods Overview
Public Methods
L1 Methods
L2 Methods
Builder Methods

REST API

Orderbook
GET
Get order book summary
POST
Get multiple order books summaries by request

Pricing
GET
Get market price
GET
Get multiple market prices
POST
Get multiple market prices by request
GET
Get midpoint price
GET
Get price history for a traded token

Spreads
POST
Get bid-ask spreads

Historical Timeseries Data
GET
Historical Timeseries Data

Order Management
Orders Overview
Place Single Order
Place Multiple Orders (Batching)
Get Order
Get Active Orders
Check Order Reward Scoring
Cancel Orders(s)
Onchain Order Info

Trades
Trades Overview
Get Trades
Websocket
WSS Overview
WSS Quickstart
WSS Authentication
User Channel
Market Channel

Sports Websocket
Overview
Message Format
Quickstart
Real Time Data Stream
RTDS Overview
RTDS Crypto Prices
RTDS Comments
Gamma Structure
Overview
Gamma Structure
Fetching Markets
Gamma Endpoints

Gamma Status
GET
Gamma API Health check

Sports
GET
List teams
GET
Get sports metadata information
GET
Get valid sports market types

Tags
GET
List tags
GET
Get tag by id
GET
Get tag by slug
GET
Get related tags (relationships) by tag id
GET
Get related tags (relationships) by tag slug
GET
Get tags related to a tag id
GET
Get tags related to a tag slug

Events
GET
List events
GET
Get event by id
GET
Get event tags
GET
Get event by slug

Markets
GET
List markets
GET
Get market by id
GET
Get market tags by id
GET
Get market by slug

Series
GET
List series
GET
Get series by id

Comments
GET
List comments
GET
Get comments by comment id
GET
Get comments by user address

Profiles
GET
Get public profile by wallet address

Search
GET
Search markets, events, and profiles
Data-API

Data API Status
GET
Data API Health check

Core
GET
Get current positions for a user
GET
Get trades for a user or markets
GET
Get user activity
GET
Get top holders for markets
GET
Get total value of a user's positions
GET
Get closed positions for a user
GET
Get trader leaderboard rankings

Misc
GET
Get total markets a user has traded
GET
Get open interest
GET
Get live volume for an event

Builders
GET
Get aggregated builder leaderboard
GET
Get daily builder volume time-series
Bridge & Swap
Overview

Bridge
Subgraph
Overview
Resolution
Resolution
Conditional Token Frameworks
Overview
Splitting USDC
Merging Tokens
Reedeeming Tokens
Deployment and Additional Information
Proxy Wallets
Proxy wallet
Negative Risk
Overview

On this page
Overview
USDC.e on Polygon
Base URL
Key Features
Endpoints
Bridge & Swap
Overview
Bridge and swap assets to Polymarket

​
Overview
The Polymarket Bridge API enables seamless deposits between multiple blockchains and Polymarket.
​
USDC.e on Polygon
Polymarket uses USDC.e (Bridged USDC) on Polygon as collateral for all trading activities. USDC.e is the bridged version of USDC from Ethereum, and it serves as the native currency for placing orders and settling trades on Polymarket.
When you deposit assets to Polymarket:
You can deposit from various supported chains (Ethereum, Solana, Arbitrum, Base, etc.)
Your assets are automatically bridged/swapped to USDC.e on Polygon
USDC.e is credited to your Polymarket wallet
You can now trade on any Polymarket market
​
Base URL
https://bridge.polymarket.com
​
Key Features
Multi-chain deposits: Bridge assets from EVM chains (Ethereum, Arbitrum, Base, etc.), Solana, and Bitcoin
Automatic conversion: Assets are automatically bridged/swapped to USDC.e on Polygon
Simple addressing: One deposit address per blockchain type (EVM, SVM, BTC)
​
Endpoints
POST /deposit - Create unique deposit addresses for bridging assets
GET /supported-assets - Get all supported chains and tokens
GET /status/{address} - Get deposit status for a given deposit address
Get daily builder volume time-series
Create deposit addresses
Ask a question...

github
Powered by
Overview - Polymarket Documentation

Skip to main content
Polymarket Documentation home pagedark logo

Search...
Ctrl K

Ask AI
Main Site

User Guide
For Developers
Changelog
Polymarket
Discord Community
Twitter
Developer Quickstart
Developer Quickstart
Fetching Market Data
Placing Your First Order
Glossary
API Rate Limits
Endpoints
Market Makers
Market Maker Introduction
Setup
Trading
Liquidity Rewards
Maker Rebates Program
Data Feeds
Inventory Management
Polymarket Builders Program
Builder Program Introduction
Builder Tiers
Builder Profile & Keys
Order Attribution
Relayer Client
Examples
Central Limit Order Book
CLOB Introduction
Status
Quickstart
Authentication
Geographic Restrictions

Client
Methods Overview
Public Methods
L1 Methods
L2 Methods
Builder Methods

REST API

Orderbook
GET
Get order book summary
POST
Get multiple order books summaries by request

Pricing
GET
Get market price
GET
Get multiple market prices
POST
Get multiple market prices by request
GET
Get midpoint price
GET
Get price history for a traded token

Spreads
POST
Get bid-ask spreads

Historical Timeseries Data
GET
Historical Timeseries Data

Order Management
Orders Overview
Place Single Order
Place Multiple Orders (Batching)
Get Order
Get Active Orders
Check Order Reward Scoring
Cancel Orders(s)
Onchain Order Info

Trades
Trades Overview
Get Trades
Websocket
WSS Overview
WSS Quickstart
WSS Authentication
User Channel
Market Channel

Sports Websocket
Overview
Message Format
Quickstart
Real Time Data Stream
RTDS Overview
RTDS Crypto Prices
RTDS Comments
Gamma Structure
Overview
Gamma Structure
Fetching Markets
Gamma Endpoints

Gamma Status
GET
Gamma API Health check

Sports
GET
List teams
GET
Get sports metadata information
GET
Get valid sports market types

Tags
GET
List tags
GET
Get tag by id
GET
Get tag by slug
GET
Get related tags (relationships) by tag id
GET
Get related tags (relationships) by tag slug
GET
Get tags related to a tag id
GET
Get tags related to a tag slug

Events
GET
List events
GET
Get event by id
GET
Get event tags
GET
Get event by slug

Markets
GET
List markets
GET
Get market by id
GET
Get market tags by id
GET
Get market by slug

Series
GET
List series
GET
Get series by id

Comments
GET
List comments
GET
Get comments by comment id
GET
Get comments by user address

Profiles
GET
Get public profile by wallet address

Search
GET
Search markets, events, and profiles
Data-API

Data API Status
GET
Data API Health check

Core
GET
Get current positions for a user
GET
Get trades for a user or markets
GET
Get user activity
GET
Get top holders for markets
GET
Get total value of a user's positions
GET
Get closed positions for a user
GET
Get trader leaderboard rankings

Misc
GET
Get total markets a user has traded
GET
Get open interest
GET
Get live volume for an event

Builders
GET
Get aggregated builder leaderboard
GET
Get daily builder volume time-series
Bridge & Swap
Overview

Bridge
POST
Create deposit addresses
GET
Get supported assets
GET
Get deposit status
POST
Get a quote
Subgraph
Overview
Resolution
Resolution
Conditional Token Frameworks
Overview
Splitting USDC
Merging Tokens
Reedeeming Tokens
Deployment and Additional Information
Proxy Wallets
Proxy wallet
Negative Risk
Overview
Create deposit addresses

curl --request POST \
  --url https://bridge.polymarket.com/deposit \
  --header 'Content-Type: application/json' \
  --data '
{
  "address": "0x56687bf447db6ffa42ffe2204a05edaa20f55839"
}
'

201

400

500
{
  "address": {
    "evm": "0x23566f8b2E82aDfCf01846E54899d110e97AC053",
    "svm": "CrvTBvzryYxBHbWu2TiQpcqD5M7Le7iBKzVmEj3f36Jb",
    "btc": "bc1q8eau83qffxcj8ht4hsjdza3lha9r3egfqysj3g"
  },
  "note": "Only certain chains and tokens are supported. See /supported-assets for details."
}
Bridge
Create deposit addresses
Generate unique deposit addresses for bridging assets to Polymarket.

How it works:

Request deposit addresses for your Polymarket wallet
Receive deposit addresses for each blockchain type (EVM, Solana, Bitcoin)
Send assets to the appropriate deposit address for your source chain
Assets are automatically bridged and swapped to USDC.e on Polygon
USDC.e is credited to your Polymarket wallet for trading
POST
/
deposit

Try it
Body
application/json
​
address
stringrequired
Your Polymarket wallet address

Example:
"0x56687bf447db6ffa42ffe2204a05edaa20f55839"

Response

201

application/json
Deposit addresses created successfully

​
address
object
Deposit addresses for different blockchain networks

Show child attributes

​
note
string
Additional information about supported chains

Example:
"Only certain chains and tokens are supported. See /supported-assets for details."

Overview
Get supported assets
Ask a question...

github
Powered by
Create deposit addresses - Polymarket Documentation

Skip to main content
Polymarket Documentation home pagedark logo

Search...
Ctrl K

Ask AI
Main Site

User Guide
For Developers
Changelog
Polymarket
Discord Community
Twitter
Developer Quickstart
Developer Quickstart
Fetching Market Data
Placing Your First Order
Glossary
API Rate Limits
Endpoints
Market Makers
Market Maker Introduction
Setup
Trading
Liquidity Rewards
Maker Rebates Program
Data Feeds
Inventory Management
Polymarket Builders Program
Builder Program Introduction
Builder Tiers
Builder Profile & Keys
Order Attribution
Relayer Client
Examples
Central Limit Order Book
CLOB Introduction
Status
Quickstart
Authentication
Geographic Restrictions

Client
Methods Overview
Public Methods
L1 Methods
L2 Methods
Builder Methods

REST API

Orderbook
GET
Get order book summary
POST
Get multiple order books summaries by request

Pricing
GET
Get market price
GET
Get multiple market prices
POST
Get multiple market prices by request
GET
Get midpoint price
GET
Get price history for a traded token

Spreads
POST
Get bid-ask spreads

Historical Timeseries Data
GET
Historical Timeseries Data

Order Management
Orders Overview
Place Single Order
Place Multiple Orders (Batching)
Get Order
Get Active Orders
Check Order Reward Scoring
Cancel Orders(s)
Onchain Order Info

Trades
Trades Overview
Get Trades
Websocket
WSS Overview
WSS Quickstart
WSS Authentication
User Channel
Market Channel

Sports Websocket
Overview
Message Format
Quickstart
Real Time Data Stream
RTDS Overview
RTDS Crypto Prices
RTDS Comments
Gamma Structure
Overview
Gamma Structure
Fetching Markets
Gamma Endpoints

Gamma Status
GET
Gamma API Health check

Sports
GET
List teams
GET
Get sports metadata information
GET
Get valid sports market types

Tags
GET
List tags
GET
Get tag by id
GET
Get tag by slug
GET
Get related tags (relationships) by tag id
GET
Get related tags (relationships) by tag slug
GET
Get tags related to a tag id
GET
Get tags related to a tag slug

Events
GET
List events
GET
Get event by id
GET
Get event tags
GET
Get event by slug

Markets
GET
List markets
GET
Get market by id
GET
Get market tags by id
GET
Get market by slug

Series
GET
List series
GET
Get series by id

Comments
GET
List comments
GET
Get comments by comment id
GET
Get comments by user address

Profiles
GET
Get public profile by wallet address

Search
GET
Search markets, events, and profiles
Data-API

Data API Status
GET
Data API Health check

Core
GET
Get current positions for a user
GET
Get trades for a user or markets
GET
Get user activity
GET
Get top holders for markets
GET
Get total value of a user's positions
GET
Get closed positions for a user
GET
Get trader leaderboard rankings

Misc
GET
Get total markets a user has traded
GET
Get open interest
GET
Get live volume for an event

Builders
GET
Get aggregated builder leaderboard
GET
Get daily builder volume time-series
Bridge & Swap
Overview

Bridge
POST
Create deposit addresses
GET
Get supported assets
GET
Get deposit status
POST
Get a quote
Subgraph
Overview
Resolution
Resolution
Conditional Token Frameworks
Overview
Splitting USDC
Merging Tokens
Reedeeming Tokens
Deployment and Additional Information
Proxy Wallets
Proxy wallet
Negative Risk
Overview
Get supported assets

curl --request GET \
  --url https://bridge.polymarket.com/supported-assets

200

500
{
  "supportedAssets": [
    {
      "chainId": "1",
      "chainName": "Ethereum",
      "token": {
        "name": "USD Coin",
        "symbol": "USDC",
        "address": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
        "decimals": 6
      },
      "minCheckoutUsd": 45
    }
  ]
}
Bridge
Get supported assets
Retrieve all supported chains and tokens for deposits.

USDC.e on Polygon: Polymarket uses USDC.e (Bridged USDC from Ethereum) on Polygon as the native collateral for all markets. When you deposit assets from other chains, they are automatically bridged and swapped to USDC.e on Polygon, which is then used as collateral for trading on Polymarket.

Minimum Deposit Amounts: Each asset has a minCheckoutUsd field indicating the minimum deposit amount required in USD. Make sure your deposit meets this minimum to avoid transaction failures.

GET
/
supported-assets

Try it
Response

200

application/json
Successfully retrieved supported assets

​
supportedAssets
object[]
List of supported assets with minimum deposit amounts

Show child attributes

Create deposit addresses
Get deposit status
Ask a question...

github
Powered by
Get supported assets - Polymarket Documentation

Skip to main content
Polymarket Documentation home pagedark logo

Search...
Ctrl K

Ask AI
Main Site

User Guide
For Developers
Changelog
Polymarket
Discord Community
Twitter
Developer Quickstart
Developer Quickstart
Fetching Market Data
Placing Your First Order
Glossary
API Rate Limits
Endpoints
Market Makers
Market Maker Introduction
Setup
Trading
Liquidity Rewards
Maker Rebates Program
Data Feeds
Inventory Management
Polymarket Builders Program
Builder Program Introduction
Builder Tiers
Builder Profile & Keys
Order Attribution
Relayer Client
Examples
Central Limit Order Book
CLOB Introduction
Status
Quickstart
Authentication
Geographic Restrictions

Client
Methods Overview
Public Methods
L1 Methods
L2 Methods
Builder Methods

REST API

Orderbook
GET
Get order book summary
POST
Get multiple order books summaries by request

Pricing
GET
Get market price
GET
Get multiple market prices
POST
Get multiple market prices by request
GET
Get midpoint price
GET
Get price history for a traded token

Spreads
POST
Get bid-ask spreads

Historical Timeseries Data
GET
Historical Timeseries Data

Order Management
Orders Overview
Place Single Order
Place Multiple Orders (Batching)
Get Order
Get Active Orders
Check Order Reward Scoring
Cancel Orders(s)
Onchain Order Info

Trades
Trades Overview
Get Trades
Websocket
WSS Overview
WSS Quickstart
WSS Authentication
User Channel
Market Channel

Sports Websocket
Overview
Message Format
Quickstart
Real Time Data Stream
RTDS Overview
RTDS Crypto Prices
RTDS Comments
Gamma Structure
Overview
Gamma Structure
Fetching Markets
Gamma Endpoints

Gamma Status
GET
Gamma API Health check

Sports
GET
List teams
GET
Get sports metadata information
GET
Get valid sports market types

Tags
GET
List tags
GET
Get tag by id
GET
Get tag by slug
GET
Get related tags (relationships) by tag id
GET
Get related tags (relationships) by tag slug
GET
Get tags related to a tag id
GET
Get tags related to a tag slug

Events
GET
List events
GET
Get event by id
GET
Get event tags
GET
Get event by slug

Markets
GET
List markets
GET
Get market by id
GET
Get market tags by id
GET
Get market by slug

Series
GET
List series
GET
Get series by id

Comments
GET
List comments
GET
Get comments by comment id
GET
Get comments by user address

Profiles
GET
Get public profile by wallet address

Search
GET
Search markets, events, and profiles
Data-API

Data API Status
GET
Data API Health check

Core
GET
Get current positions for a user
GET
Get trades for a user or markets
GET
Get user activity
GET
Get top holders for markets
GET
Get total value of a user's positions
GET
Get closed positions for a user
GET
Get trader leaderboard rankings

Misc
GET
Get total markets a user has traded
GET
Get open interest
GET
Get live volume for an event

Builders
GET
Get aggregated builder leaderboard
GET
Get daily builder volume time-series
Bridge & Swap
Overview

Bridge
POST
Create deposit addresses
GET
Get supported assets
GET
Get deposit status
POST
Get a quote
Subgraph
Overview
Resolution
Resolution
Conditional Token Frameworks
Overview
Splitting USDC
Merging Tokens
Reedeeming Tokens
Deployment and Additional Information
Proxy Wallets
Proxy wallet
Negative Risk
Overview
Get deposit status

curl --request GET \
  --url https://bridge.polymarket.com/status/{address}

200

400

500
{
  "transactions": [
    {
      "fromChainId": "1151111081099710",
      "fromTokenAddress": "11111111111111111111111111111111",
      "fromAmountBaseUnit": "13566635",
      "toChainId": "137",
      "toTokenAddress": "0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174",
      "status": "DEPOSIT_DETECTED"
    },
    {
      "fromChainId": "1151111081099710",
      "fromTokenAddress": "11111111111111111111111111111111",
      "fromAmountBaseUnit": "13400000",
      "toChainId": "137",
      "toTokenAddress": "0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174",
      "createdTimeMs": 1757646914535,
      "status": "PROCESSING"
    },
    {
      "fromChainId": "1151111081099710",
      "fromTokenAddress": "11111111111111111111111111111111",
      "fromAmountBaseUnit": "13500152",
      "toChainId": "137",
      "toTokenAddress": "0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174",
      "txHash": "3atr19NAiNCYt24RHM1WnzZp47RXskpTDzspJoCBBaMFwUB8fk37hFkxz35P5UEnnmWz21rb2t5wJ8pq3EE2XnxU",
      "createdTimeMs": 1757531217339,
      "status": "COMPLETED"
    }
  ]
}
Bridge
Get deposit status
Get the transaction status for all deposits associated with a given deposit address.

Usage:

Use the deposit address returned from the /deposit endpoint (EVM, SVM, or BTC address)
Poll this endpoint to track the progress of your deposits
Status Values:

DEPOSIT_DETECTED: Deposit detected but not yet processing
PROCESSING: Transaction is being routed and swapped
ORIGIN_TX_CONFIRMED: Origin transaction has been confirmed on source chain
SUBMITTED: Transaction has been submitted to destination chain
COMPLETED: Transaction completed successfully
FAILED: Transaction encountered an error and did not complete
Notes:

Transactions typically complete within a few minutes, but may take longer depending on network conditions
An empty transactions array means no deposits have been made to this address yet
GET
/
status
/
{address}

Try it
Path Parameters
​
address
stringrequired
The deposit address to query (EVM, SVM, or BTC address from the /deposit response)

Response

200

application/json
Successfully retrieved transaction status

​
transactions
object[]
List of transactions for the given address

Show child attributes

Get supported assets
Get a quote
Ask a question...

github
Powered by
Get deposit status - Polymarket Documentation

Skip to main content
Polymarket Documentation home pagedark logo

Search...
Ctrl K

Ask AI
Main Site

User Guide
For Developers
Changelog
Polymarket
Discord Community
Twitter
Developer Quickstart
Developer Quickstart
Fetching Market Data
Placing Your First Order
Glossary
API Rate Limits
Endpoints
Market Makers
Market Maker Introduction
Setup
Trading
Liquidity Rewards
Maker Rebates Program
Data Feeds
Inventory Management
Polymarket Builders Program
Builder Program Introduction
Builder Tiers
Builder Profile & Keys
Order Attribution
Relayer Client
Examples
Central Limit Order Book
CLOB Introduction
Status
Quickstart
Authentication
Geographic Restrictions

Client
Methods Overview
Public Methods
L1 Methods
L2 Methods
Builder Methods

REST API

Orderbook
GET
Get order book summary
POST
Get multiple order books summaries by request

Pricing
GET
Get market price
GET
Get multiple market prices
POST
Get multiple market prices by request
GET
Get midpoint price
GET
Get price history for a traded token

Spreads
POST
Get bid-ask spreads

Historical Timeseries Data
GET
Historical Timeseries Data

Order Management
Orders Overview
Place Single Order
Place Multiple Orders (Batching)
Get Order
Get Active Orders
Check Order Reward Scoring
Cancel Orders(s)
Onchain Order Info

Trades
Trades Overview
Get Trades
Websocket
WSS Overview
WSS Quickstart
WSS Authentication
User Channel
Market Channel

Sports Websocket
Overview
Message Format
Quickstart
Real Time Data Stream
RTDS Overview
RTDS Crypto Prices
RTDS Comments
Gamma Structure
Overview
Gamma Structure
Fetching Markets
Gamma Endpoints

Gamma Status
GET
Gamma API Health check

Sports
GET
List teams
GET
Get sports metadata information
GET
Get valid sports market types

Tags
GET
List tags
GET
Get tag by id
GET
Get tag by slug
GET
Get related tags (relationships) by tag id
GET
Get related tags (relationships) by tag slug
GET
Get tags related to a tag id
GET
Get tags related to a tag slug

Events
GET
List events
GET
Get event by id
GET
Get event tags
GET
Get event by slug

Markets
GET
List markets
GET
Get market by id
GET
Get market tags by id
GET
Get market by slug

Series
GET
List series
GET
Get series by id

Comments
GET
List comments
GET
Get comments by comment id
GET
Get comments by user address

Profiles
GET
Get public profile by wallet address

Search
GET
Search markets, events, and profiles
Data-API

Data API Status
GET
Data API Health check

Core
GET
Get current positions for a user
GET
Get trades for a user or markets
GET
Get user activity
GET
Get top holders for markets
GET
Get total value of a user's positions
GET
Get closed positions for a user
GET
Get trader leaderboard rankings

Misc
GET
Get total markets a user has traded
GET
Get open interest
GET
Get live volume for an event

Builders
GET
Get aggregated builder leaderboard
GET
Get daily builder volume time-series
Bridge & Swap
Overview

Bridge
POST
Create deposit addresses
GET
Get supported assets
GET
Get deposit status
POST
Get a quote
Subgraph
Overview
Resolution
Resolution
Conditional Token Frameworks
Overview
Splitting USDC
Merging Tokens
Reedeeming Tokens
Deployment and Additional Information
Proxy Wallets
Proxy wallet
Negative Risk
Overview
Get a quote

curl --request POST \
  --url https://bridge.polymarket.com/quote \
  --header 'Content-Type: application/json' \
  --data '
{
  "fromAmountBaseUnit": "10000000",
  "fromChainId": "137",
  "fromTokenAddress": "0x3c499c542cEF5E3811e1192ce70d8cC03d5c3359",
  "recipientAddress": "0x17eC161f126e82A8ba337f4022d574DBEaFef575",
  "toChainId": "137",
  "toTokenAddress": "0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174"
}
'


{
  "estCheckoutTimeMs": 25000,
  "estFeeBreakdown": {
    "appFeeLabel": "Fun.xyz fee",
    "appFeePercent": 0,
    "appFeeUsd": 0,
    "fillCostPercent": 0,
    "fillCostUsd": 0,
    "gasUsd": 0.003854,
    "maxSlippage": 0,
    "minReceived": 14.488305,
    "swapImpact": 0,
    "swapImpactUsd": 0,
    "totalImpact": 0,
    "totalImpactUsd": 0
  },
  "estInputUsd": 14.488305,
  "estOutputUsd": 14.488305,
  "estToTokenBaseUnit": "14491203",
  "quoteId": "0x00c34ba467184b0146406d62b0e60aaa24ed52460bd456222b6155a0d9de0ad5"
}
Bridge
Get a quote
Get an estimated quote for a deposit or withdrawal, including output amounts, checkout time, and a detailed fee breakdown.

Use Cases:

Preview fees and estimated output before executing a deposit or withdrawal
Compare costs across different token/chain combinations
Get the quoteId to reference this specific quote
Notes:

Quotes are estimates and actual amounts may vary slightly due to market conditions
See /supported-assets for a list of all supported chains and tokens
POST
/
quote

Try it
Body
application/json
​
fromAmountBaseUnit
stringrequired
Amount of tokens to send

Example:
"10000000"

​
fromChainId
stringrequired
Source Chain ID

Example:
"137"

​
fromTokenAddress
stringrequired
Source token address

Example:
"0x3c499c542cEF5E3811e1192ce70d8cC03d5c3359"

​
recipientAddress
stringrequired
Address of the recipient

Example:
"0x17eC161f126e82A8ba337f4022d574DBEaFef575"

​
toChainId
stringrequired
Destination Chain ID

Example:
"137"

​
toTokenAddress
stringrequired
Destination token address

Example:
"0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174"

Response

200

application/json
Quote retrieved successfully

​
estCheckoutTimeMs
integer
Estimated time to complete the checkout in milliseconds

Example:
25000

​
estFeeBreakdown
object
Breakdown of the estimated fees

Show child attributes

​
estInputUsd
number
Estimated token amount received in USD

Example:
14.488305

​
estOutputUsd
number
Estimated token amount sent in USD

Example:
14.488305

​
estToTokenBaseUnit
string
Estimated token amount received

Example:
"14491203"

​
quoteId
string
Unique quote id of the request

Example:
"0x00c34ba467184b0146406d62b0e60aaa24ed52460bd456222b6155a0d9de0ad5"

Get deposit status
Overview
Ask a question...

github
Powered by
Get a quote - Polymarket Documentation

Skip to main content
Polymarket Documentation home pagedark logo

Search...
Ctrl K

Ask AI
Main Site

User Guide
For Developers
Changelog
Polymarket
Discord Community
Twitter
Developer Quickstart
Developer Quickstart
Fetching Market Data
Placing Your First Order
Glossary
API Rate Limits
Endpoints
Market Makers
Market Maker Introduction
Setup
Trading
Liquidity Rewards
Maker Rebates Program
Data Feeds
Inventory Management
Polymarket Builders Program
Builder Program Introduction
Builder Tiers
Builder Profile & Keys
Order Attribution
Relayer Client
Examples
Central Limit Order Book
CLOB Introduction
Status
Quickstart
Authentication
Geographic Restrictions

Client
Methods Overview
Public Methods
L1 Methods
L2 Methods
Builder Methods

REST API

Orderbook
GET
Get order book summary
POST
Get multiple order books summaries by request

Pricing
GET
Get market price
GET
Get multiple market prices
POST
Get multiple market prices by request
GET
Get midpoint price
GET
Get price history for a traded token

Spreads
POST
Get bid-ask spreads

Historical Timeseries Data
GET
Historical Timeseries Data

Order Management
Orders Overview
Place Single Order
Place Multiple Orders (Batching)
Get Order
Get Active Orders
Check Order Reward Scoring
Cancel Orders(s)
Onchain Order Info

Trades
Trades Overview
Get Trades
Websocket
WSS Overview
WSS Quickstart
WSS Authentication
User Channel
Market Channel

Sports Websocket
Overview
Message Format
Quickstart
Real Time Data Stream
RTDS Overview
RTDS Crypto Prices
RTDS Comments
Gamma Structure
Overview
Gamma Structure
Fetching Markets
Gamma Endpoints

Gamma Status
GET
Gamma API Health check

Sports
GET
List teams
GET
Get sports metadata information
GET
Get valid sports market types

Tags
GET
List tags
GET
Get tag by id
GET
Get tag by slug
GET
Get related tags (relationships) by tag id
GET
Get related tags (relationships) by tag slug
GET
Get tags related to a tag id
GET
Get tags related to a tag slug

Events
GET
List events
GET
Get event by id
GET
Get event tags
GET
Get event by slug

Markets
GET
List markets
GET
Get market by id
GET
Get market tags by id
GET
Get market by slug

Series
GET
List series
GET
Get series by id

Comments
GET
List comments
GET
Get comments by comment id
GET
Get comments by user address

Profiles
GET
Get public profile by wallet address

Search
GET
Search markets, events, and profiles
Data-API

Data API Status
GET
Data API Health check

Core
GET
Get current positions for a user
GET
Get trades for a user or markets
GET
Get user activity
GET
Get top holders for markets
GET
Get total value of a user's positions
GET
Get closed positions for a user
GET
Get trader leaderboard rankings

Misc
GET
Get total markets a user has traded
GET
Get open interest
GET
Get live volume for an event

Builders
GET
Get aggregated builder leaderboard
GET
Get daily builder volume time-series
Bridge & Swap
Overview

Bridge
POST
Create deposit addresses
GET
Get supported assets
GET
Get deposit status
POST
Get a quote
Subgraph
Overview
Resolution
Resolution
Conditional Token Frameworks
Overview
Splitting USDC
Merging Tokens
Reedeeming Tokens
Deployment and Additional Information
Proxy Wallets
Proxy wallet
Negative Risk
Overview

On this page
Subgraph Overview
Source
Subgraph
Overview
​
Subgraph Overview
Polymarket has written and open sourced a subgraph that provides, via a GraphQL query interface, useful aggregate calculations and event indexing for things like volume, user position, market and liquidity data. The subgraph updates in real time to be able to be mixed, and match core data from the primary Polymarket interface, providing positional data, activity history and more. The subgraph can be hosted by anyone.
​
Source
The Polymarket subgraph is entirely open source and can be found on the Polymarket Github.
Subgraph Github Repository
Note: The available models/schemas can be found in the schema.graphql file.
Get a quote
Resolution
Ask a question...

github
Powered by
Overview - Polymarket Documentation

Skip to main content
Polymarket Documentation home pagedark logo

Search...
Ctrl K

Ask AI
Main Site

User Guide
For Developers
Changelog
Polymarket
Discord Community
Twitter
Developer Quickstart
Developer Quickstart
Fetching Market Data
Placing Your First Order
Glossary
API Rate Limits
Endpoints
Market Makers
Market Maker Introduction
Setup
Trading
Liquidity Rewards
Maker Rebates Program
Data Feeds
Inventory Management
Polymarket Builders Program
Builder Program Introduction
Builder Tiers
Builder Profile & Keys
Order Attribution
Relayer Client
Examples
Central Limit Order Book
CLOB Introduction
Status
Quickstart
Authentication
Geographic Restrictions

Client
Methods Overview
Public Methods
L1 Methods
L2 Methods
Builder Methods

REST API

Orderbook
GET
Get order book summary
POST
Get multiple order books summaries by request

Pricing
GET
Get market price
GET
Get multiple market prices
POST
Get multiple market prices by request
GET
Get midpoint price
GET
Get price history for a traded token

Spreads
POST
Get bid-ask spreads

Historical Timeseries Data
GET
Historical Timeseries Data

Order Management
Orders Overview
Place Single Order
Place Multiple Orders (Batching)
Get Order
Get Active Orders
Check Order Reward Scoring
Cancel Orders(s)
Onchain Order Info

Trades
Trades Overview
Get Trades
Websocket
WSS Overview
WSS Quickstart
WSS Authentication
User Channel
Market Channel

Sports Websocket
Overview
Message Format
Quickstart
Real Time Data Stream
RTDS Overview
RTDS Crypto Prices
RTDS Comments
Gamma Structure
Overview
Gamma Structure
Fetching Markets
Gamma Endpoints

Gamma Status
GET
Gamma API Health check

Sports
GET
List teams
GET
Get sports metadata information
GET
Get valid sports market types

Tags
GET
List tags
GET
Get tag by id
GET
Get tag by slug
GET
Get related tags (relationships) by tag id
GET
Get related tags (relationships) by tag slug
GET
Get tags related to a tag id
GET
Get tags related to a tag slug

Events
GET
List events
GET
Get event by id
GET
Get event tags
GET
Get event by slug

Markets
GET
List markets
GET
Get market by id
GET
Get market tags by id
GET
Get market by slug

Series
GET
List series
GET
Get series by id

Comments
GET
List comments
GET
Get comments by comment id
GET
Get comments by user address

Profiles
GET
Get public profile by wallet address

Search
GET
Search markets, events, and profiles
Data-API

Data API Status
GET
Data API Health check

Core
GET
Get current positions for a user
GET
Get trades for a user or markets
GET
Get user activity
GET
Get top holders for markets
GET
Get total value of a user's positions
GET
Get closed positions for a user
GET
Get trader leaderboard rankings

Misc
GET
Get total markets a user has traded
GET
Get open interest
GET
Get live volume for an event

Builders
GET
Get aggregated builder leaderboard
GET
Get daily builder volume time-series
Bridge & Swap
Overview

Bridge
POST
Create deposit addresses
GET
Get supported assets
GET
Get deposit status
POST
Get a quote
Subgraph
Overview
Resolution
Resolution
Conditional Token Frameworks
Overview
Splitting USDC
Merging Tokens
Reedeeming Tokens
Deployment and Additional Information
Proxy Wallets
Proxy wallet
Negative Risk
Overview

On this page
UMA Optimistic Oracle Integration
Overview
Clarifications
Resolution Process
Actions
Possible Flows
Deployed Addresses
v3.0
v2.0
v1.0
Additional Resources
Resolution
Resolution
​
UMA Optimistic Oracle Integration
​
Overview
Polymarket leverages UMA’s Optimistic Oracle (OO) to resolve arbitrary questions, permissionlessly. From UMA’s docs:
“UMA’s Optimistic Oracle allows contracts to quickly request and receive data information … The Optimistic Oracle acts as a generalized escalation game between contracts that initiate a price request and UMA’s dispute resolution system known as the Data Verification Mechanism (DVM). Prices proposed by the Optimistic Oracle will not be sent to the DVM unless it is disputed. If a dispute is raised, a request is sent to the DVM. All contracts built on UMA use the DVM as a backstop to resolve disputes. Disputes sent to the DVM will be resolved within a few days — after UMA tokenholders vote on what the correct outcome should have been.”
To allow CTF markets to be resolved via the OO, Polymarket developed a custom adapter contract called UmaCtfAdapter that provides a way for the two contract systems to interface.
​
Clarifications
Recent versions (v2+) of the UmaCtfAdapter also include a bulletin board feature that allows market creators to issue “clarifications”. Questions that allow updates will include the sentence in their ancillary data:
“Updates made by the question creator via the bulletin board on 0x6A5D0222186C0FceA7547534cC13c3CFd9b7b6A4F74 should be considered. In summary, clarifications that do not impact the question’s intent should be considered.”
Where the transaction reference outlining what outlining should be considered.
​
Resolution Process
​
Actions
Initiate - Binary CTF markets are initialized via the UmaCtfAdapter’s initialize() function. This stores the question parameters on the contract, prepares the CTF and requests a price for a question from the OO. It returns a questionID that is also used to reference on the UmaCtfAdapter. The caller provides:
ancillaryData - data used to resolve a question (i.e the question + clarifications)
rewardToken - ERC20 token address used for payment of rewards and fees
reward - Reward amount offered to a successful proposer. The caller must have set allowance so that the contract can pull this reward in.
proposalBond - Bond required to be posted by OO proposers/disputers. If 0, the default OO bond is used.
liveness - UMA liveness period in seconds. If 0, the default liveness period is used.
Propose Price - Anyone can then propose a price to the question on the OO. To do this they must post the proposalBond. The liveness period begins after a price is proposed.
Dispute - Anyone that disagrees with the proposed price has the opportunity to dispute the price by posting a counter bond via the OO, this proposed will now be escalated to the DVM for a voter-wide vote.
​
Possible Flows
When the first proposed price is disputed for a questionID on the adapter, a callback is made and posted as the reward for this new proposal. This means a second questionID, making a new questionID to the OO (the reward is returned before the callback is made and posted as the reward for this new proposal). This allows for a second round of resolution, and correspondingly a second dispute is required for it to go to the DVM. The thinking behind this is to doubles the cost of a potential griefing vector (two disputes are required just one) and also allows far-fetched (incorrect) first price proposals to not delay the resolution. As such there are two possible flows:
Initialize (CTFAdapter) -> Propose (OO) -> Resolve (CTFAdapter)
Initialize (CTFAdaptor) -> Propose (OO) -> Challenge (OO) -> Propose (OO) -> Resolve (CTFAdaptor)
Initialize (CTFAdaptor) -> Propose (OO) -> Challenge (OO) -> Propose (OO) -> Challenge (CtfAdapter) -> Resolve (CTFAdaptor)
​
Deployed Addresses
​
v3.0
Network	Address
Polygon Mainnet	0x157Ce2d672854c848c9b79C49a8Cc6cc89176a49
​
v2.0
Network	Address
Polygon Mainnet	0x6A9D0222186C0FceA7547534cC13c3CFd9b7b6A4F74
​
v1.0
Network	Address
Polygon Mainnet	0xC8B122858a4EF82C2d4eE2E6A276C719e692995130
​
Additional Resources
Audit
Source Code
UMA Documentation
UMA Oracle Portal
Overview
Overview
Ask a question...

github
Powered by
Resolution - Polymarket Documentation

Skip to main content
Polymarket Documentation home pagedark logo

Search...
Ctrl K

Ask AI
Main Site

User Guide
For Developers
Changelog
Polymarket
Discord Community
Twitter
Developer Quickstart
Developer Quickstart
Fetching Market Data
Placing Your First Order
Glossary
API Rate Limits
Endpoints
Market Makers
Market Maker Introduction
Setup
Trading
Liquidity Rewards
Maker Rebates Program
Data Feeds
Inventory Management
Polymarket Builders Program
Builder Program Introduction
Builder Tiers
Builder Profile & Keys
Order Attribution
Relayer Client
Examples
Central Limit Order Book
CLOB Introduction
Status
Quickstart
Authentication
Geographic Restrictions

Client
Methods Overview
Public Methods
L1 Methods
L2 Methods
Builder Methods

REST API

Orderbook
GET
Get order book summary
POST
Get multiple order books summaries by request

Pricing
GET
Get market price
GET
Get multiple market prices
POST
Get multiple market prices by request
GET
Get midpoint price
GET
Get price history for a traded token

Spreads
POST
Get bid-ask spreads

Historical Timeseries Data
GET
Historical Timeseries Data

Order Management
Orders Overview
Place Single Order
Place Multiple Orders (Batching)
Get Order
Get Active Orders
Check Order Reward Scoring
Cancel Orders(s)
Onchain Order Info

Trades
Trades Overview
Get Trades
Websocket
WSS Overview
WSS Quickstart
WSS Authentication
User Channel
Market Channel

Sports Websocket
Overview
Message Format
Quickstart
Real Time Data Stream
RTDS Overview
RTDS Crypto Prices
RTDS Comments
Gamma Structure
Overview
Gamma Structure
Fetching Markets
Gamma Endpoints

Gamma Status
GET
Gamma API Health check

Sports
GET
List teams
GET
Get sports metadata information
GET
Get valid sports market types

Tags
GET
List tags
GET
Get tag by id
GET
Get tag by slug
GET
Get related tags (relationships) by tag id
GET
Get related tags (relationships) by tag slug
GET
Get tags related to a tag id
GET
Get tags related to a tag slug

Events
GET
List events
GET
Get event by id
GET
Get event tags
GET
Get event by slug

Markets
GET
List markets
GET
Get market by id
GET
Get market tags by id
GET
Get market by slug

Series
GET
List series
GET
Get series by id

Comments
GET
List comments
GET
Get comments by comment id
GET
Get comments by user address

Profiles
GET
Get public profile by wallet address

Search
GET
Search markets, events, and profiles
Data-API

Data API Status
GET
Data API Health check

Core
GET
Get current positions for a user
GET
Get trades for a user or markets
GET
Get user activity
GET
Get top holders for markets
GET
Get total value of a user's positions
GET
Get closed positions for a user
GET
Get trader leaderboard rankings

Misc
GET
Get total markets a user has traded
GET
Get open interest
GET
Get live volume for an event

Builders
GET
Get aggregated builder leaderboard
GET
Get daily builder volume time-series
Bridge & Swap
Overview

Bridge
POST
Create deposit addresses
GET
Get supported assets
GET
Get deposit status
POST
Get a quote
Subgraph
Overview
Resolution
Resolution
Conditional Token Frameworks
Overview
Splitting USDC
Merging Tokens
Reedeeming Tokens
Deployment and Additional Information
Proxy Wallets
Proxy wallet
Negative Risk
Overview
Conditional Token Frameworks
Overview
All outcomes on Polymarket are tokenized on the Polygon network. Specifically, Polymarket outcomes shares are binary outcomes (ie “YES” and “NO”) using Gnosis’ Conditional Token Framework (CTF). They are distinct ERC1155 tokens related to a parent condition and backed by the same collateral. More technically, the binary outcome tokens are referred to as “positionIds” in Gnosis’s documentation. “PositionIds” are derived from a collateral token and distinct “collectionIds”. “CollectionIds” are derived from a “parentCollectionId”, (always bytes32(0) in our case) a “conditionId”, and a unique “indexSet”.
The “indexSet” is a 256 bit array denoting which outcome slots are in an outcome collection; it MUST be a nonempty proper subset of a condition’s outcome slots. In the binary case, which we are interested in, there are two “indexSets”, one for the first outcome and one for the second. The first outcome’s “indexSet” is 0b01 = 1 and the second’s is 0b10 = 2. The parent “conditionId” (shared by both “collectionIds” and therefore “positionIds”) is derived from a “questionId” (a hash of the UMA ancillary data), an “oracle” (the UMA adapter V2), and an “outcomeSlotCount” (always 2 in the binary case). The steps for calculating the ERC1155 token ids (positionIds) is as follows:
Get the conditionId
Function:
getConditionId(oracle, questionId, outcomeSlotCount)
Inputs:
oracle: address - UMA adapter V2
questionId: bytes32 - hash of the UMA ancillary data
outcomeSlotCount: uint - 2 for binary markets
Get the two collectionIds
Function:
getCollectionId(parentCollectionId, conditionId, indexSet)
Inputs:
parentCollectionId: bytes32 - bytes32(0)
conditionId: bytes32 - the conditionId derived from (1)
indexSet: uint - 1 (0b01) for the first and 2 (0b10) for the second.
Get the two positionIds
Function:
getPositionId(collateralToken, collectionId)
Inputs:
collateralToken: IERC20 - address of ERC20 token collateral (USDC)
collectionId: bytes32 - the two collectionIds derived from (3)
Leveraging the relations above, specifically “conditionIds” -> “positionIds” the Gnosis CTF contract allows for “splitting” and “merging” full outcome sets. We explore these actions and provide code examples below.
Resolution
Splitting USDC
Ask a question...

github
Powered by
Overview - Polymarket Documentation

Skip to main content
Polymarket Documentation home pagedark logo

Search...
Ctrl K

Ask AI
Main Site

User Guide
For Developers
Changelog
Polymarket
Discord Community
Twitter
Developer Quickstart
Developer Quickstart
Fetching Market Data
Placing Your First Order
Glossary
API Rate Limits
Endpoints
Market Makers
Market Maker Introduction
Setup
Trading
Liquidity Rewards
Maker Rebates Program
Data Feeds
Inventory Management
Polymarket Builders Program
Builder Program Introduction
Builder Tiers
Builder Profile & Keys
Order Attribution
Relayer Client
Examples
Central Limit Order Book
CLOB Introduction
Status
Quickstart
Authentication
Geographic Restrictions

Client
Methods Overview
Public Methods
L1 Methods
L2 Methods
Builder Methods

REST API

Orderbook
GET
Get order book summary
POST
Get multiple order books summaries by request

Pricing
GET
Get market price
GET
Get multiple market prices
POST
Get multiple market prices by request
GET
Get midpoint price
GET
Get price history for a traded token

Spreads
POST
Get bid-ask spreads

Historical Timeseries Data
GET
Historical Timeseries Data

Order Management
Orders Overview
Place Single Order
Place Multiple Orders (Batching)
Get Order
Get Active Orders
Check Order Reward Scoring
Cancel Orders(s)
Onchain Order Info

Trades
Trades Overview
Get Trades
Websocket
WSS Overview
WSS Quickstart
WSS Authentication
User Channel
Market Channel

Sports Websocket
Overview
Message Format
Quickstart
Real Time Data Stream
RTDS Overview
RTDS Crypto Prices
RTDS Comments
Gamma Structure
Overview
Gamma Structure
Fetching Markets
Gamma Endpoints

Gamma Status
GET
Gamma API Health check

Sports
GET
List teams
GET
Get sports metadata information
GET
Get valid sports market types

Tags
GET
List tags
GET
Get tag by id
GET
Get tag by slug
GET
Get related tags (relationships) by tag id
GET
Get related tags (relationships) by tag slug
GET
Get tags related to a tag id
GET
Get tags related to a tag slug

Events
GET
List events
GET
Get event by id
GET
Get event tags
GET
Get event by slug

Markets
GET
List markets
GET
Get market by id
GET
Get market tags by id
GET
Get market by slug

Series
GET
List series
GET
Get series by id

Comments
GET
List comments
GET
Get comments by comment id
GET
Get comments by user address

Profiles
GET
Get public profile by wallet address

Search
GET
Search markets, events, and profiles
Data-API

Data API Status
GET
Data API Health check

Core
GET
Get current positions for a user
GET
Get trades for a user or markets
GET
Get user activity
GET
Get top holders for markets
GET
Get total value of a user's positions
GET
Get closed positions for a user
GET
Get trader leaderboard rankings

Misc
GET
Get total markets a user has traded
GET
Get open interest
GET
Get live volume for an event

Builders
GET
Get aggregated builder leaderboard
GET
Get daily builder volume time-series
Bridge & Swap
Overview

Bridge
POST
Create deposit addresses
GET
Get supported assets
GET
Get deposit status
POST
Get a quote
Subgraph
Overview
Resolution
Resolution
Conditional Token Frameworks
Overview
Splitting USDC
Merging Tokens
Reedeeming Tokens
Deployment and Additional Information
Proxy Wallets
Proxy wallet
Negative Risk
Overview
Conditional Token Frameworks
Splitting USDC
At any time, after a condition has been prepared on the CTF contract (via prepareCondition), it is possible to “split” collateral into a full (position) set. In other words, one unit USDC can be split into 1 YES unit and 1 NO unit. If splitting from the collateral, the CTF contract will attempt to transfer amount collateral from the message sender to itself. If successful, amount stake will be minted in the split target positions. If any of the transfers, mints, or burns fail, the transaction will revert. The transaction will also revert if the given partition is trivial, invalid, or refers to more slots than the condition is prepared with. This operation happens via the splitPosition() function on the CTF contract with the following parameters:
collateralToken: IERC20 - The address of the positions’ backing collateral token.
parentCollectionId: bytes32 - The ID of the outcome collections common to the position being split and the split target positions. Null in Polymarket case.
conditionId: bytes32 - The ID of the condition to split on.
partition: uint[] - An array of disjoint index sets representing a nontrivial partition of the outcome slots of the given condition. E.G. A|B and C but not A|B and B|C (is not disjoint). Each element’s a number which, together with the condition, represents the outcome collection. E.G. 0b110 is A|B, 0b010 is B, etc. In the Polymarket case 1|2.
amount - The amount of collateral or stake to split. Also the number of full sets to receive.
Overview
Merging Tokens
Ask a question...

github
Powered by
Splitting USDC - Polymarket Documentation

Skip to main content
Polymarket Documentation home pagedark logo

Search...
Ctrl K

Ask AI
Main Site

User Guide
For Developers
Changelog
Polymarket
Discord Community
Twitter
Developer Quickstart
Developer Quickstart
Fetching Market Data
Placing Your First Order
Glossary
API Rate Limits
Endpoints
Market Makers
Market Maker Introduction
Setup
Trading
Liquidity Rewards
Maker Rebates Program
Data Feeds
Inventory Management
Polymarket Builders Program
Builder Program Introduction
Builder Tiers
Builder Profile & Keys
Order Attribution
Relayer Client
Examples
Central Limit Order Book
CLOB Introduction
Status
Quickstart
Authentication
Geographic Restrictions

Client
Methods Overview
Public Methods
L1 Methods
L2 Methods
Builder Methods

REST API

Orderbook
GET
Get order book summary
POST
Get multiple order books summaries by request

Pricing
GET
Get market price
GET
Get multiple market prices
POST
Get multiple market prices by request
GET
Get midpoint price
GET
Get price history for a traded token

Spreads
POST
Get bid-ask spreads

Historical Timeseries Data
GET
Historical Timeseries Data

Order Management
Orders Overview
Place Single Order
Place Multiple Orders (Batching)
Get Order
Get Active Orders
Check Order Reward Scoring
Cancel Orders(s)
Onchain Order Info

Trades
Trades Overview
Get Trades
Websocket
WSS Overview
WSS Quickstart
WSS Authentication
User Channel
Market Channel

Sports Websocket
Overview
Message Format
Quickstart
Real Time Data Stream
RTDS Overview
RTDS Crypto Prices
RTDS Comments
Gamma Structure
Overview
Gamma Structure
Fetching Markets
Gamma Endpoints

Gamma Status
GET
Gamma API Health check

Sports
GET
List teams
GET
Get sports metadata information
GET
Get valid sports market types

Tags
GET
List tags
GET
Get tag by id
GET
Get tag by slug
GET
Get related tags (relationships) by tag id
GET
Get related tags (relationships) by tag slug
GET
Get tags related to a tag id
GET
Get tags related to a tag slug

Events
GET
List events
GET
Get event by id
GET
Get event tags
GET
Get event by slug

Markets
GET
List markets
GET
Get market by id
GET
Get market tags by id
GET
Get market by slug

Series
GET
List series
GET
Get series by id

Comments
GET
List comments
GET
Get comments by comment id
GET
Get comments by user address

Profiles
GET
Get public profile by wallet address

Search
GET
Search markets, events, and profiles
Data-API

Data API Status
GET
Data API Health check

Core
GET
Get current positions for a user
GET
Get trades for a user or markets
GET
Get user activity
GET
Get top holders for markets
GET
Get total value of a user's positions
GET
Get closed positions for a user
GET
Get trader leaderboard rankings

Misc
GET
Get total markets a user has traded
GET
Get open interest
GET
Get live volume for an event

Builders
GET
Get aggregated builder leaderboard
GET
Get daily builder volume time-series
Bridge & Swap
Overview

Bridge
POST
Create deposit addresses
GET
Get supported assets
GET
Get deposit status
POST
Get a quote
Subgraph
Overview
Resolution
Resolution
Conditional Token Frameworks
Overview
Splitting USDC
Merging Tokens
Reedeeming Tokens
Deployment and Additional Information
Proxy Wallets
Proxy wallet
Negative Risk
Overview
Conditional Token Frameworks
Merging Tokens
In addition to splitting collateral for a full set, the inverse can also happen; a full set can be “merged” for collateral. This operation can again happen at any time after a condition has been prepared on the CTF contract. One unit of each position in a full set is burned in return for 1 collateral unit. This operation happens via the mergePositions() function on the CTF contract with the following parameters:
collateralToken: IERC20 - The address of the positions’ backing collateral token.
parentCollectionId: bytes32 - The ID of the outcome collections common to the position being merged and the merge target positions. Null in Polymarket case.
conditionId: bytes32 - The ID of the condition to merge on.
partition: uint[] - An array of disjoint index sets representing a nontrivial partition of the outcome slots of the given condition. E.G. A|B and C but not A|B and B|C (is not disjoint). Each element’s a number which, together with the condition, represents the outcome collection. E.G. 0b110 is A|B, 0b010 is B, etc. In the Polymarket case 1|2.
amount - The number of full sets to merge. Also the amount of collateral to receive.
Splitting USDC
Reedeeming Tokens
Ask a question...

github
Powered by
Merging Tokens - Polymarket Documentation

Skip to main content
Polymarket Documentation home pagedark logo

Search...
Ctrl K

Ask AI
Main Site

User Guide
For Developers
Changelog
Polymarket
Discord Community
Twitter
Developer Quickstart
Developer Quickstart
Fetching Market Data
Placing Your First Order
Glossary
API Rate Limits
Endpoints
Market Makers
Market Maker Introduction
Setup
Trading
Liquidity Rewards
Maker Rebates Program
Data Feeds
Inventory Management
Polymarket Builders Program
Builder Program Introduction
Builder Tiers
Builder Profile & Keys
Order Attribution
Relayer Client
Examples
Central Limit Order Book
CLOB Introduction
Status
Quickstart
Authentication
Geographic Restrictions

Client
Methods Overview
Public Methods
L1 Methods
L2 Methods
Builder Methods

REST API

Orderbook
GET
Get order book summary
POST
Get multiple order books summaries by request

Pricing
GET
Get market price
GET
Get multiple market prices
POST
Get multiple market prices by request
GET
Get midpoint price
GET
Get price history for a traded token

Spreads
POST
Get bid-ask spreads

Historical Timeseries Data
GET
Historical Timeseries Data

Order Management
Orders Overview
Place Single Order
Place Multiple Orders (Batching)
Get Order
Get Active Orders
Check Order Reward Scoring
Cancel Orders(s)
Onchain Order Info

Trades
Trades Overview
Get Trades
Websocket
WSS Overview
WSS Quickstart
WSS Authentication
User Channel
Market Channel

Sports Websocket
Overview
Message Format
Quickstart
Real Time Data Stream
RTDS Overview
RTDS Crypto Prices
RTDS Comments
Gamma Structure
Overview
Gamma Structure
Fetching Markets
Gamma Endpoints

Gamma Status
GET
Gamma API Health check

Sports
GET
List teams
GET
Get sports metadata information
GET
Get valid sports market types

Tags
GET
List tags
GET
Get tag by id
GET
Get tag by slug
GET
Get related tags (relationships) by tag id
GET
Get related tags (relationships) by tag slug
GET
Get tags related to a tag id
GET
Get tags related to a tag slug

Events
GET
List events
GET
Get event by id
GET
Get event tags
GET
Get event by slug

Markets
GET
List markets
GET
Get market by id
GET
Get market tags by id
GET
Get market by slug

Series
GET
List series
GET
Get series by id

Comments
GET
List comments
GET
Get comments by comment id
GET
Get comments by user address

Profiles
GET
Get public profile by wallet address

Search
GET
Search markets, events, and profiles
Data-API

Data API Status
GET
Data API Health check

Core
GET
Get current positions for a user
GET
Get trades for a user or markets
GET
Get user activity
GET
Get top holders for markets
GET
Get total value of a user's positions
GET
Get closed positions for a user
GET
Get trader leaderboard rankings

Misc
GET
Get total markets a user has traded
GET
Get open interest
GET
Get live volume for an event

Builders
GET
Get aggregated builder leaderboard
GET
Get daily builder volume time-series
Bridge & Swap
Overview

Bridge
POST
Create deposit addresses
GET
Get supported assets
GET
Get deposit status
POST
Get a quote
Subgraph
Overview
Resolution
Resolution
Conditional Token Frameworks
Overview
Splitting USDC
Merging Tokens
Reedeeming Tokens
Deployment and Additional Information
Proxy Wallets
Proxy wallet
Negative Risk
Overview
Conditional Token Frameworks
Reedeeming Tokens
Once a condition has had it’s payouts reported (ie by the UMACTFAdapter calling reportPayouts on the CTF contract), users with shares in the winning outcome can redeem them for the underlying collateral. Specifically, users can call the redeemPositions function on the CTF contract which will burn all valuable conditional tokens in return for collateral according to the reported payout vector. This function has the following parameters:
collateralToken: IERC20 - The address of the positions’ backing collateral token.
parentCollectionId: bytes32 - The ID of the outcome collections common to the position being redeemed. Null in Polymarket case.
indexSets: uint[] - The ID of the condition to redeem.
indexSets: uint[] - An array of disjoint index sets representing a nontrivial partition of the outcome slots of the given condition. E.G. A|B and C but not A|B and B|C (is not disjoint). Each element’s a number which, together with the condition, represents the outcome collection. E.G. 0b110 is A|B, 0b010 is B, etc. In the Polymarket case 1|2.
Merging Tokens
Deployment and Additional Information
Ask a question...

github
Powered by
Reedeeming Tokens - Polymarket Documentation

Skip to main content
Polymarket Documentation home pagedark logo

Search...
Ctrl K

Ask AI
Main Site

User Guide
For Developers
Changelog
Polymarket
Discord Community
Twitter
Developer Quickstart
Developer Quickstart
Fetching Market Data
Placing Your First Order
Glossary
API Rate Limits
Endpoints
Market Makers
Market Maker Introduction
Setup
Trading
Liquidity Rewards
Maker Rebates Program
Data Feeds
Inventory Management
Polymarket Builders Program
Builder Program Introduction
Builder Tiers
Builder Profile & Keys
Order Attribution
Relayer Client
Examples
Central Limit Order Book
CLOB Introduction
Status
Quickstart
Authentication
Geographic Restrictions

Client
Methods Overview
Public Methods
L1 Methods
L2 Methods
Builder Methods

REST API

Orderbook
GET
Get order book summary
POST
Get multiple order books summaries by request

Pricing
GET
Get market price
GET
Get multiple market prices
POST
Get multiple market prices by request
GET
Get midpoint price
GET
Get price history for a traded token

Spreads
POST
Get bid-ask spreads

Historical Timeseries Data
GET
Historical Timeseries Data

Order Management
Orders Overview
Place Single Order
Place Multiple Orders (Batching)
Get Order
Get Active Orders
Check Order Reward Scoring
Cancel Orders(s)
Onchain Order Info

Trades
Trades Overview
Get Trades
Websocket
WSS Overview
WSS Quickstart
WSS Authentication
User Channel
Market Channel

Sports Websocket
Overview
Message Format
Quickstart
Real Time Data Stream
RTDS Overview
RTDS Crypto Prices
RTDS Comments
Gamma Structure
Overview
Gamma Structure
Fetching Markets
Gamma Endpoints

Gamma Status
GET
Gamma API Health check

Sports
GET
List teams
GET
Get sports metadata information
GET
Get valid sports market types

Tags
GET
List tags
GET
Get tag by id
GET
Get tag by slug
GET
Get related tags (relationships) by tag id
GET
Get related tags (relationships) by tag slug
GET
Get tags related to a tag id
GET
Get tags related to a tag slug

Events
GET
List events
GET
Get event by id
GET
Get event tags
GET
Get event by slug

Markets
GET
List markets
GET
Get market by id
GET
Get market tags by id
GET
Get market by slug

Series
GET
List series
GET
Get series by id

Comments
GET
List comments
GET
Get comments by comment id
GET
Get comments by user address

Profiles
GET
Get public profile by wallet address

Search
GET
Search markets, events, and profiles
Data-API

Data API Status
GET
Data API Health check

Core
GET
Get current positions for a user
GET
Get trades for a user or markets
GET
Get user activity
GET
Get top holders for markets
GET
Get total value of a user's positions
GET
Get closed positions for a user
GET
Get trader leaderboard rankings

Misc
GET
Get total markets a user has traded
GET
Get open interest
GET
Get live volume for an event

Builders
GET
Get aggregated builder leaderboard
GET
Get daily builder volume time-series
Bridge & Swap
Overview

Bridge
POST
Create deposit addresses
GET
Get supported assets
GET
Get deposit status
POST
Get a quote
Subgraph
Overview
Resolution
Resolution
Conditional Token Frameworks
Overview
Splitting USDC
Merging Tokens
Reedeeming Tokens
Deployment and Additional Information
Proxy Wallets
Proxy wallet
Negative Risk
Overview

On this page
Deployment
Resources
Conditional Token Frameworks
Deployment and Additional Information
​
Deployment
The CTF contract is deployed (and verified) at the following addresses:
Network	Deployed Address
Polygon Mainnet	0x4D97DCd97eC945f40cF65F87097ACe5EA0476045
Polygon Mainnet	0x4bFb41d5B3570DeFd03C39a9A4D8dE6Bd8B8982E
Polymarket provides code samples in both Python and TypeScript for interacting with our smart chain contracts. You will need an RPC endpoint to access the blockchain, and you’ll be responsible for paying gas fees when executing these RPC/function calls. Please ensure you’re using the correct example for your wallet type (Safe Wallet vs Proxy Wallet) when implementing.
​
Resources
On-Chain Code Samples
Polygon RPC List
CTF Source Code
Audits
Gist For positionId Calculation
Reedeeming Tokens
Proxy wallet
Ask a question...

github
Powered by
Deployment and Additional Information - Polymarket Documentation

Skip to main content
Polymarket Documentation home pagedark logo

Search...
Ctrl K

Ask AI
Main Site

User Guide
For Developers
Changelog
Polymarket
Discord Community
Twitter
Developer Quickstart
Developer Quickstart
Fetching Market Data
Placing Your First Order
Glossary
API Rate Limits
Endpoints
Market Makers
Market Maker Introduction
Setup
Trading
Liquidity Rewards
Maker Rebates Program
Data Feeds
Inventory Management
Polymarket Builders Program
Builder Program Introduction
Builder Tiers
Builder Profile & Keys
Order Attribution
Relayer Client
Examples
Central Limit Order Book
CLOB Introduction
Status
Quickstart
Authentication
Geographic Restrictions

Client
Methods Overview
Public Methods
L1 Methods
L2 Methods
Builder Methods

REST API

Orderbook
GET
Get order book summary
POST
Get multiple order books summaries by request

Pricing
GET
Get market price
GET
Get multiple market prices
POST
Get multiple market prices by request
GET
Get midpoint price
GET
Get price history for a traded token

Spreads
POST
Get bid-ask spreads

Historical Timeseries Data
GET
Historical Timeseries Data

Order Management
Orders Overview
Place Single Order
Place Multiple Orders (Batching)
Get Order
Get Active Orders
Check Order Reward Scoring
Cancel Orders(s)
Onchain Order Info

Trades
Trades Overview
Get Trades
Websocket
WSS Overview
WSS Quickstart
WSS Authentication
User Channel
Market Channel

Sports Websocket
Overview
Message Format
Quickstart
Real Time Data Stream
RTDS Overview
RTDS Crypto Prices
RTDS Comments
Gamma Structure
Overview
Gamma Structure
Fetching Markets
Gamma Endpoints

Gamma Status
GET
Gamma API Health check

Sports
GET
List teams
GET
Get sports metadata information
GET
Get valid sports market types

Tags
GET
List tags
GET
Get tag by id
GET
Get tag by slug
GET
Get related tags (relationships) by tag id
GET
Get related tags (relationships) by tag slug
GET
Get tags related to a tag id
GET
Get tags related to a tag slug

Events
GET
List events
GET
Get event by id
GET
Get event tags
GET
Get event by slug

Markets
GET
List markets
GET
Get market by id
GET
Get market tags by id
GET
Get market by slug

Series
GET
List series
GET
Get series by id

Comments
GET
List comments
GET
Get comments by comment id
GET
Get comments by user address

Profiles
GET
Get public profile by wallet address

Search
GET
Search markets, events, and profiles
Data-API

Data API Status
GET
Data API Health check

Core
GET
Get current positions for a user
GET
Get trades for a user or markets
GET
Get user activity
GET
Get top holders for markets
GET
Get total value of a user's positions
GET
Get closed positions for a user
GET
Get trader leaderboard rankings

Misc
GET
Get total markets a user has traded
GET
Get open interest
GET
Get live volume for an event

Builders
GET
Get aggregated builder leaderboard
GET
Get daily builder volume time-series
Bridge & Swap
Overview

Bridge
POST
Create deposit addresses
GET
Get supported assets
GET
Get deposit status
POST
Get a quote
Subgraph
Overview
Resolution
Resolution
Conditional Token Frameworks
Overview
Splitting USDC
Merging Tokens
Reedeeming Tokens
Deployment and Additional Information
Proxy Wallets
Proxy wallet
Negative Risk
Overview

On this page
Overview
Deployments
Proxy Wallets
Proxy wallet
​
Overview
When a user first uses Polymarket.com to trade they are prompted to create a wallet. When they do this, a 1 of 1 multisig is deployed to Polygon which is controlled/owned by the accessing EOA (either MetaMask wallet or MagicLink wallet). This proxy wallet is where all the user’s positions (ERC1155) and USDC (ERC20) are held.
Using proxy wallets allows Polymarket to provide an improved UX where multi-step transactions can be executed atomically and transactions can be relayed by relayers on the gas station network. If you are a developer looking to programmatically access positions you accumulated via the Polymarket.com interface, you can either continue using the smart contract wallet by executing transactions through it from the owner account, or you can transfer these assets to a new address using the owner account.
​
Deployments
Each user has their own proxy wallet (and thus proxy wallet address) but the factories are available at the following deployed addresses on the Polygon network:
Address	Details
0xaacfeea03eb1561c4e67d661e40682bd20e3541b	Gnosis safe factory – Gnosis safes are used for all MetaMask users
0xaB45c5A4B0c941a2F231C04C3f49182e1A254052	Polymarket proxy factory – Polymarket custom proxy contracts are used for all MagicLink users
Deployment and Additional Information
Overview
Ask a question...

github
Powered by
Proxy wallet - Polymarket Documentation

Skip to main content
Polymarket Documentation home pagedark logo

Search...
Ctrl K

Ask AI
Main Site

User Guide
For Developers
Changelog
Polymarket
Discord Community
Twitter
Developer Quickstart
Developer Quickstart
Fetching Market Data
Placing Your First Order
Glossary
API Rate Limits
Endpoints
Market Makers
Market Maker Introduction
Setup
Trading
Liquidity Rewards
Maker Rebates Program
Data Feeds
Inventory Management
Polymarket Builders Program
Builder Program Introduction
Builder Tiers
Builder Profile & Keys
Order Attribution
Relayer Client
Examples
Central Limit Order Book
CLOB Introduction
Status
Quickstart
Authentication
Geographic Restrictions

Client
Methods Overview
Public Methods
L1 Methods
L2 Methods
Builder Methods

REST API

Orderbook
GET
Get order book summary
POST
Get multiple order books summaries by request

Pricing
GET
Get market price
GET
Get multiple market prices
POST
Get multiple market prices by request
GET
Get midpoint price
GET
Get price history for a traded token

Spreads
POST
Get bid-ask spreads

Historical Timeseries Data
GET
Historical Timeseries Data

Order Management
Orders Overview
Place Single Order
Place Multiple Orders (Batching)
Get Order
Get Active Orders
Check Order Reward Scoring
Cancel Orders(s)
Onchain Order Info

Trades
Trades Overview
Get Trades
Websocket
WSS Overview
WSS Quickstart
WSS Authentication
User Channel
Market Channel

Sports Websocket
Overview
Message Format
Quickstart
Real Time Data Stream
RTDS Overview
RTDS Crypto Prices
RTDS Comments
Gamma Structure
Overview
Gamma Structure
Fetching Markets
Gamma Endpoints

Gamma Status
GET
Gamma API Health check

Sports
GET
List teams
GET
Get sports metadata information
GET
Get valid sports market types

Tags
GET
List tags
GET
Get tag by id
GET
Get tag by slug
GET
Get related tags (relationships) by tag id
GET
Get related tags (relationships) by tag slug
GET
Get tags related to a tag id
GET
Get tags related to a tag slug

Events
GET
List events
GET
Get event by id
GET
Get event tags
GET
Get event by slug

Markets
GET
List markets
GET
Get market by id
GET
Get market tags by id
GET
Get market by slug

Series
GET
List series
GET
Get series by id

Comments
GET
List comments
GET
Get comments by comment id
GET
Get comments by user address

Profiles
GET
Get public profile by wallet address

Search
GET
Search markets, events, and profiles
Data-API

Data API Status
GET
Data API Health check

Core
GET
Get current positions for a user
GET
Get trades for a user or markets
GET
Get user activity
GET
Get top holders for markets
GET
Get total value of a user's positions
GET
Get closed positions for a user
GET
Get trader leaderboard rankings

Misc
GET
Get total markets a user has traded
GET
Get open interest
GET
Get live volume for an event

Builders
GET
Get aggregated builder leaderboard
GET
Get daily builder volume time-series
Bridge & Swap
Overview

Bridge
POST
Create deposit addresses
GET
Get supported assets
GET
Get deposit status
POST
Get a quote
Subgraph
Overview
Resolution
Resolution
Conditional Token Frameworks
Overview
Splitting USDC
Merging Tokens
Reedeeming Tokens
Deployment and Additional Information
Proxy Wallets
Proxy wallet
Negative Risk
Overview

On this page
Augmented Negative Risk
Original Outcomes
Placeholder Outcomes
Explicit Other
Negative Risk
Overview
Certain events which meet the criteria of being “winner-take-all” may be deployed as “negative risk” events/markets. The Gamma API includes a boolean field on events, negRisk, which indicates whether the event is negative risk.
Negative risk allows for increased capital efficiency by relating all markets within events via a convert action. More explicitly, a NO share in any market can be converted into 1 YES share in all other markets. Converts can be exercised via the Negative Adapter. You can read more about negative risk here.
​
Augmented Negative Risk
There is a known issue with the negative risk architecture which is that the outcome universe must be complete before conversions are made or otherwise conversion will “cost” something. In most cases, the outcome universe can be made complete by deploying all the named outcomes and then an “other” option. But in some cases this is undesirable as new outcomes can come out of nowhere and you’d rather them be directly named versus grouped together in an “other”.
To fix this, some markets use a system of “augmented negative risk”, where named outcomes, a collection of unnamed outcomes, and an other is deployed. When a new outcome needs to be added, an unnamed outcome can be clarified to be the new outcome via the bulletin board. This means the “other” in the case of augmented negative risk can effectively change definitions (outcomes can be taken out of it).
As such, trading should only happen on the named outcomes, and the other outcomes should be ignored until they are named or until resolution occurs. The Polymarket UI will not show unnamed outcomes.
If a market becomes resolvable and the correct outcome is not named (originally or via placeholder clarification), it should resolve to the “other” outcome. An event can be considered “augmented negative risk” when enableNegRisk is true AND negRiskAugmented is true.
The naming conventions are as follows:
​
Original Outcomes
Outcome A
Outcome B
…
​
Placeholder Outcomes
Person A -> can be clarified to a named outcome
Person B -> can be clarified to a named outcome
…
​
Explicit Other
Other -> not meant to be traded as the definition of this changes as placeholder outcomes are clarified to named outcomes
Proxy wallet
Ask a question...

github
Powered by
Overview - Polymarket Documentation


