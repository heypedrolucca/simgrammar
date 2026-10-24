# Player-driven markets

*Mechanic* · `player-driven-market` · status: **sourced**

Players post buy and sell orders in shared order books, and prices emerge from player behavior.

| field | value |
|---|---|
| aliases | order book, regional market, player economy |
| family | Economy & finance |
| substrate | Agent-based, Rule system |
| math basis | Mechanism design / auctions, Game theory |
| feedback | Both |
| player interface | Orders, Parameter |
| legibility | 3 |
| emergence potential | 4 |
| authoring cost | 1 |
| compute cost | 2 |
| tuning difficulty | 4 |
| ai leverage | 3 |
| maturity | Established |
| core count *(computed)* | 2 |
| earliest game *(computed)* | [EVE Online](../game/eve-online.md) |
| earliest year *(computed)* | 2003 |
| prevalence *(computed)* | 5 |
| prevalence share *(computed)* | 0.029 |
| subgenre spread *(computed)* | 3 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

Owns per-market order books. Each order has an item, a price, a quantity, a location or range, and an expiry. A new buy order fills against the cheapest compatible sell order and vice versa; any remainder rests in the book. Transaction fees and sales taxes remove currency while NPC bounties and sales add it, so the operator manages faucets and sinks rather than prices. Players make nearly all goods, so prices emerge from their mining, manufacturing, hauling, and speculation. EVE Online (2003) is the canonical form: regional markets where players gather most raw materials and build nearly all ships, price history charts, and large-scale manipulation such as ramping and bear raids; its developer hired an economist in 2007 to monitor the economy. Ultima Online's player vendors and Albion Online's player-crafted gear economy are other forms.

## Player Experience

Being one trader among thousands. The player hunts arbitrage between regions, undercuts by a fraction of a unit, posts low buy orders and waits, and reads price charts like a real trader. Wealth comes from information and patience as much as production.

## Design Levers

- market topology: one global book, regional books, or local station markets with hauling between them
- fees, sales tax, and order modification costs as sinks and anti-spam measures
- how much NPC supply or demand exists to anchor prices
- order range, duration, and how much order-book depth is visible
- currency faucets (bounties, NPC sales) relative to sinks

## Failure Modes

- Faucets that outpace sinks inflate prices and devalue new players' earnings.
- Low population leaves thin books where one player sets prices or nothing sells.
- Bots and automated relisting dominate when order updates are free and fast.
- Manipulation and scams drive away players who did not opt into that kind of play.

## Dynamics

- Trade hubs form where liquidity concentrates, as at EVE's Jita, which concentrates trade further.
- Wars destroy goods and raise demand, coupling combat to manufacturing prices.
- Speculators anticipate patches and events, so prices move before a change ships.

## Open Questions

- Can LLM or RL trader agents supply liquidity for small servers or single-player worlds without becoming exploitable market makers?
- Which sink and faucet controls keep a long-running player market stable without visible developer intervention?

## Backlinks (computed)

**involved in:** [AI liquidity in player markets](../opportunity/ai-liquidity-in-player-markets.md)

**used by:** [Eco](../game/eco.md), [EVE Online](../game/eve-online.md), [Planet Zoo](../game/planet-zoo.md), [Screeps](../game/screeps.md), [Second Life](../game/second-life.md)

## Sources

- [Eve Online](../source/src-wikipedia-eve-online.md)

---
Provenance: created in run `2026-10-24-taxonomy-m2`.
