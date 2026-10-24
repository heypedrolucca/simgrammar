# Auctions

*Mechanic* · `auctions` · status: **sourced**

Goods, land, or rights are allocated by bidding procedures in which players or agents compete on price under rules for timing, ties, and reserves.

| field | value |
|---|---|
| aliases | bidding, auction house |
| family | Economy & finance |
| substrate | Rule system, Agent-based |
| math basis | Mechanism design / auctions, Game theory |
| feedback | Reinforcing (positive) |
| player interface | Parameter, Embodied skill |
| legibility | 4 |
| emergence potential | 3 |
| authoring cost | 1 |
| compute cost | 1 |
| tuning difficulty | 3 |
| ai leverage | 3 |
| maturity | Established |
| core count *(computed)* | 1 |
| earliest game *(computed)* | [M.U.L.E.](../game/mule.md) |
| earliest year *(computed)* | 1983 |
| prevalence *(computed)* | 4 |
| prevalence share *(computed)* | 0.023 |
| subgenre spread *(computed)* | 2 |
| technique count *(computed)* | 1 |
| technique exposure *(computed)* | 0.25 |

## Definition

Owns a lot (item, quantity, optional reserve price), the standing bids, and a clock. Bidders submit or raise bids under a format: ascending open outcry, sealed bid, descending price, or a timed listing with a buyout price. When the clock ends or no bidder will go higher, the rule assigns the lot to the winner, transfers money, and settles fees. AI bidders bid up to a valuation computed from their needs and cash. M.U.L.E. (1983) runs real-time auctions for each resource, breaks ties in favor of the trailing player, and lets players who withhold supply raise prices on later turns; its designers replaced land auctions with one free plot per turn because auctioning land fed a runaway loop. MMO auction houses such as World of Warcraft's use timed listings with a minimum bid and an optional buyout price.

## Player Experience

Reading rivals. The player estimates what a lot is worth to each competitor, decides how far to push the price, and feels the sting of overpaying or the relief of a bargain. In real-time formats such as M.U.L.E. bidding is a test of nerve and timing; in timed listings it becomes patient sniping and undercutting.

## Design Levers

- auction format (ascending, sealed-bid first or second price, descending, timed listing with buyout)
- tie-breaking and catch-up rules, such as awarding ties to the trailing player
- reserve prices, minimum increments, and listing fees or deposits that act as money sinks
- auction duration and whether bidding happens in real time or between turns
- AI bidder valuation function and how much cash it holds back
- which goods are auctioned versus sold at fixed prices or granted for free

## Failure Modes

- Auctioning productive assets such as land lets the richest player buy more production, the snowball M.U.L.E.'s designers removed by granting free plots.
- AI bidders with simple valuation rules can be baited into overpaying or never compete, so auctions become trivial.
- Long timed auctions in MMOs reward bots and last-second sniping over judgment.
- Collusion between human bidders suppresses prices when the rules cannot detect it.

## Dynamics

- Withholding supply from an auction raises clearing prices on later rounds, enabling deliberate shortage play.
- Bidding wars between two rivals let a third party buy cheaply elsewhere.
- Reserve prices and fees act as money sinks that slow inflation in persistent economies.

## Open Questions

- Can LLM bidders with private valuations and bluffing make single-player auctions as tense as multiplayer ones?
- Which catch-up rules (tie-breaks, budget caps) prevent auction snowballs without feeling arbitrary?

## Backlinks (computed)

**affected by:** [Regret minimization and search for imperfect-information games](../technique/imperfect-information-solvers.md)

**involved in:** [AI liquidity in player markets](../opportunity/ai-liquidity-in-player-markets.md)

**used by:** [Car Mechanic Simulator 2021](../game/car-mechanic-simulator-2021.md), [House Flipper](../game/house-flipper.md), [M.U.L.E.](../game/mule.md), [Offworld Trading Company](../game/offworld-trading-company.md)

## Sources

- [M.U.L.E.](../source/src-wikipedia-mule.md)

---
Provenance: created in run `2026-10-24-taxonomy-m2`.
