# Offworld Trading Company

*Game* · `offworld-trading-company` · status: **sourced**

A real-time economic strategy game on Mars where companies claim resource tiles, refine goods for a shared market whose prices move with every trade, and win by buying out every rival's stock.

| field | value |
|---|---|
| year | 2015 |
| year full release | 2016 |
| developer | Mohawk Games |
| platforms | PC |
| subgenre | Business / economic sim |
| sim domain | Economic, Industrial / logistics |
| player role | Manager / owner |
| agency model | Zoning / placement, Policy / parameter |
| time model | Real-time with pause |
| sim scale | Region |
| fidelity | Stylized |
| perspective | Free 3D camera |
| win structure | Competitive victory |
| failure model | Hard restart |
| narrative mode | None |
| multiplayer | Single-player, Competitive |
| modding | Content |
| production tier | Indie |
| agent count order | None |
| emergence | 3 |
| influence | 2 |
| influenced by | [M.U.L.E.](../game/mule.md), [Railroad Tycoon](../game/railroad-tycoon.md) |
| cluster *(computed)* | C02 |
| core count *(computed)* | 5 |
| mechanic count *(computed)* | 12 |

## Summary

A real-time economic strategy game on Mars where companies claim resource tiles, refine goods for a shared market whose prices move with every trade, and win by buying out every rival's stock.

## Core Loop

land an HQ -> claim tiles and build extractors -> refine resources into goods -> sell into a market whose prices move with each trade -> buy black market sabotage and stock -> buy out every rival

## Design Notes

Soren Johnson replaced combat with a shared market: 13 resources trade at prices that move with every purchase and sale, so selling a large stockpile drives the price down and one player's bulk purchases create openings for others. Black market items such as nukes, EMPs, and mutinies act through the economy, and each purchase raises the price of the next one. Victory comes from equity: players buy shares in rivals until they hold a majority of every company, and buying back one's own shares makes a takeover more expensive. Johnson names M.U.L.E. and Railroad Tycoon as inspirations.

## Sources

- src-wikipedia-offworld-trading-company
- src-steam-2026-offworld-trading-company
- src-gamesbeat-2015-offworld-trading-company
- src-spacesector-2015-offworld-early-access

## Relations

**influenced by**

- [M.U.L.E.](../game/mule.md)
- [Railroad Tycoon](../game/railroad-tycoon.md)

**uses**

- [Supply-demand pricing](../mechanic/supply-demand-pricing.md) (core): Each of 13 resources has a market price that falls when players sell and rises when they buy, with shortages and gluts driving rapid swings.
- [Equity and buyouts](../mechanic/equity-buyouts.md) (core): Players buy shares in rival companies and win by holding a majority of every company; debt lowers stock price, and buying back one's own stock raises buyout cost.
- [Resource extraction](../mechanic/resource-extraction.md) (core): Extractors on claimed hex tiles mine water, aluminum, iron, silicon, and carbon at rates set by tile richness.
- [Production chains](../mechanic/production-chain.md) (core): Steel mills, glass kilns, electronics factories, greenhouses, and hydrolysis reactors turn raw resources into higher-value goods and life support.
- [Rival firms](../mechanic/rival-firms.md) (core): Up to eight companies, AI or human, compete in one market and attack each other through black market sabotage such as nukes, EMPs, and mutinies.
- [Auctions](../mechanic/auctions.md) (supporting): Some resource tiles and patents are sold by auction.
- [Goods consumption](../mechanic/goods-consumption.md) (supporting): Each HQ consumes life support resources such as water, food, oxygen, and power, which must be produced or bought.
- [Loans and debt](../mechanic/loans-debt.md) (supporting): Companies can run into debt, which depresses their share price.
- [Tech tree](../mechanic/tech-tree.md) (supporting): Patents and HQ upgrades unlock buildings and bonuses.
- [Procedural terrain](../mechanic/procedural-terrain.md) (supporting): Each match generates a new Martian map, so resource layouts and claims differ.
- [Pause and speed control](../mechanic/variable-speed.md) (supporting)
- [Building placement](../mechanic/free-placement.md) (supporting)

## Backlinks (computed)

**precedent for:** [Agent ambassadors between player worlds](../opportunity/agent-ambassadors-async.md), [Parallel autobalancing of economies](../opportunity/parallel-autobalance.md)

## Sources

- [Offworld Trading Company](../source/src-wikipedia-offworld-trading-company.md)
- [Offworld Trading Company on Steam](../source/src-steam-2026-offworld-trading-company.md)
- [Civilization IV's lead designer wants you to financially ruin your enemies](../source/src-gamesbeat-2015-offworld-trading-company.md)
- [Offworld Trading Company: Early Access First Impressions](../source/src-spacesector-2015-offworld-early-access.md)

---
Provenance: created in run `2026-10-24-catalog-ge`; reviewed in `2026-10-24-review-fixes`.
