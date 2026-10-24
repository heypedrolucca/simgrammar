# M.U.L.E.

*Game* · `mule` · status: **sourced**

A four-player economic strategy game on a colony planet where players outfit M.U.L.E. robots to produce food, energy, smithore, and crystite and trade them in real-time auctions.

| field | value |
|---|---|
| year | 1983 |
| developer | Ozark Softscape |
| platforms | Mainframe / early micro, PC, Console |
| subgenre | Business / economic sim |
| sim domain | Economic, Industrial / logistics |
| player role | Manager / owner |
| agency model | Direct avatar, Zoning / placement |
| time model | Turn-based |
| sim scale | Settlement |
| fidelity | Stylized |
| perspective | Top-down / side 2D |
| win structure | Competitive victory |
| failure model | Soft / recoverable |
| narrative mode | None |
| multiplayer | Single-player, Competitive |
| modding | None |
| production tier | Indie |
| agent count order | None |
| emergence | 3 |
| influence | 3 |
| cluster *(computed)* | C02 |
| core count *(computed)* | 4 |
| mechanic count *(computed)* | 10 |

## Summary

A four-player economic strategy game on a colony planet where players outfit M.U.L.E. robots to produce food, energy, smithore, and crystite and trade them in real-time auctions.

## Core Loop

claim a land grant -> buy and outfit M.U.L.E.s and walk them to plots -> production with shortages and random events -> real-time auctions set prices -> buy or sell -> next round

## Design Notes

M.U.L.E. couples its four resources: food sets how long a player's development turn lasts, energy shortages stop plots from producing, and smithore supply sets M.U.L.E. prices and whether the store can manufacture more. Prices are set in real-time auctions in which buyers and sellers move avatars toward a price, so withholding goods and private deals between players are legitimate tactics. Danielle Bunten built catch-up rules into the systems: tied bids go to the player in the losing position, favorable events rarely hit the leader and harmful ones never hit last place, and land auctions were replaced by free grants because they compounded the leader's advantage. The taxonomy has no mechanic for systematic catch-up rules (proposed as catch-up-balancing).

## Relations

**uses**

- [Auctions](../mechanic/auctions.md) (core): Each round resources trade in a real-time auction: sellers and buyers walk avatars toward a price line, trades fire when they meet, and ties go to the trailing player.
- [Supply-demand pricing](../mechanic/supply-demand-pricing.md) (core): Store prices respond to supply: refusing to sell raises a resource's price in later rounds, and smithore scarcity raises the price of new M.U.L.E.s.
- [Resource extraction](../mechanic/resource-extraction.md) (core): A M.U.L.E. outfitted for food, energy, smithore, or crystite harvests its plot each round; output depends on terrain and the plot's development.
- [Turn structure](../mechanic/turn-structure.md) (core): Rounds run in fixed phases: land grant, timed development, production, then auctions for each resource.
- [Adjacency scoring](../mechanic/adjacency-scoring.md) (supporting): Plots grouped with others producing the same resource get a production bonus.
- [Goods consumption](../mechanic/goods-consumption.md) (supporting): Each player needs food and energy each round; low food shortens the next development turn and low energy stops some plots.
- [Production chains](../mechanic/production-chain.md) (supporting): The store turns smithore into new M.U.L.E.s; with no smithore it cannot build more.
- [Random disasters](../mechanic/random-disasters.md) (supporting): Sunspots, pirate raids, meteorites, and runaway M.U.L.E.s, targeted away from the last-place player.
- [Rival firms](../mechanic/rival-firms.md) (supporting): Computer opponents fill empty seats and compete for plots and auction trades.
- [Direct avatar control](../mechanic/direct-avatar.md) (supporting): Players walk a colonist through town to buy and outfit M.U.L.E.s and lead them to plots under a turn timer.

## Backlinks (computed)

**influenced:** [Offworld Trading Company](../game/offworld-trading-company.md)

**precedent for:** [AI liquidity in player markets](../opportunity/ai-liquidity-in-player-markets.md)

## Sources

- [M.U.L.E.](../source/src-wikipedia-mule.md)

---
Provenance: created in run `2026-10-24-catalog-ge`.
