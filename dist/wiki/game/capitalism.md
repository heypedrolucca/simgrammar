# Capitalism

*Game* · `capitalism` · status: **sourced**

A corporate business sim in which the player builds retail stores, factories, farms, mines, and R&D centers from internal unit layouts and competes with AI firms on price, quality, and brand across city markets.

| field | value |
|---|---|
| year | 1995 |
| developer | Enlight Software |
| platforms | PC |
| subgenre | Business / economic sim |
| sim domain | Economic, Industrial / logistics |
| player role | Manager / owner |
| agency model | Zoning / placement, Policy / parameter |
| time model | Real-time with pause |
| sim scale | Region |
| fidelity | Systemic |
| perspective | Top-down / side 2D |
| win structure | Scenario goals |
| failure model | Hard restart |
| narrative mode | None |
| multiplayer | Single-player |
| modding | Content |
| production tier | Indie |
| agent count order | Aggregate only |
| emergence | 3 |
| influence | 2 |
| cluster *(computed)* | C01 |
| core count *(computed)* | 4 |
| mechanic count *(computed)* | 13 |

## Summary

A corporate business sim in which the player builds retail stores, factories, farms, mines, and R&D centers from internal unit layouts and competes with AI firms on price, quality, and brand across city markets.

## Core Loop

buy land and place a firm -> lay out its internal units -> link purchasing, manufacturing, and sales units into supply chains -> set prices and advertising -> compete for market share on price, quality, and brand -> reinvest, research, or trade stock

## Design Notes

Trevor Chan's Capitalism models a firm as a small grid of internal units (purchasing, manufacturing, sales, advertising) that the player wires together, so every factory, farm, mine, and store is a layout and logistics puzzle inside a market model. Retail is the main income source: each department store sells up to four products, and customers weigh price, product quality, and brand against competing stores. R&D centers raise product quality over projects lasting from six months to ten years, and AI rivals can be set from aggressive to conservative. An optional stock market allows takeovers, and hired presidents can run divisions. Advertising spend that builds brand awareness has no mechanic in the taxonomy (proposed as advertising-awareness).

## Relations

**uses**

- [Production chains](../mechanic/production-chain.md) (core): Factories turn purchased inputs into products through linked manufacturing units; farms, mines, oil wells, and logging camps supply raw materials.
- [Customer value choice](../mechanic/customer-value-choice.md) (core): City consumers pick among stores by price, product quality, and brand; each department store stocks up to four items.
- [Rival firms](../mechanic/rival-firms.md) (core): AI corporations with aggressive to conservative management styles compete in the same cities for market share.
- [Building placement](../mechanic/free-placement.md) (core): Each firm is a grid of internal units placed and linked by the player; layout decides what flows where.
- [Quality tiers](../mechanic/quality-tiers.md) (supporting): Product quality comes from input quality and technology level and drives demand and price.
- [Tech tree](../mechanic/tech-tree.md) (supporting): R&D centers run projects from six months to ten years that raise technology and unlock new products.
- [Equity and buyouts](../mechanic/equity-buyouts.md) (supporting): An optional stock market lets the player buy shares, take over rivals, or be bought out.
- [Resource extraction](../mechanic/resource-extraction.md) (supporting): Mines, oil wells, farms, and logging camps produce raw materials.
- [Delegation to AI managers](../mechanic/delegation-to-ai.md) (supporting): Hired presidents can run divisions day to day.
- [Blueprints](../mechanic/blueprints.md) (supporting): A layout plan library saves and reuses firm unit layouts.
- [Scenario objectives](../mechanic/scenario-objectives.md) (supporting): Seventeen scenarios set goals such as market-share dominance within a time limit.
- [Advertising and awareness](../mechanic/advertising-awareness.md) (supporting): Advertising units inside firms spend money to raise a product's brand rating, which customers weigh with price and quality when choosing among stores.
- [Pause and speed control](../mechanic/variable-speed.md) (supporting)

## Backlinks (computed)

**precedent for:** [Calibrated serious simulations](../opportunity/calibrated-serious-sims.md)

## Sources

- [Capitalism (video game)](../source/src-wikipedia-capitalism-video-game.md)

---
Provenance: created in run `2026-10-24-catalog-ge`; reviewed in `2026-10-24-review-fixes`.
