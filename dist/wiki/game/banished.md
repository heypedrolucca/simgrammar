# Banished

*Game* · `banished` · status: **sourced**

A survival city builder without money or a tech tree in which exiled families gather, farm, and stockpile for winter while aging, births, disease, and disasters decide whether the town grows or starves.

| field | value |
|---|---|
| year | 2014 |
| developer | Shining Rock Software |
| platforms | PC |
| subgenre | City builder |
| sim domain | Urban, Biological / ecological, Economic |
| player role | Planner / mayor |
| agency model | Zoning / placement, Policy / parameter |
| time model | Real-time with pause |
| sim scale | Settlement |
| fidelity | Systemic |
| perspective | Free 3D camera |
| win structure | Open sandbox |
| failure model | Cascading collapse |
| narrative mode | Emergent |
| multiplayer | Single-player |
| modding | Content |
| production tier | Indie |
| agent count order | ~100 |
| emergence | 3 |
| influence | 4 |
| cluster *(computed)* | C02 |
| core count *(computed)* | 3 |
| mechanic count *(computed)* | 16 |

## Summary

A survival city builder without money or a tech tree in which exiled families gather, farm, and stockpile for winter while aging, births, disease, and disasters decide whether the town grows or starves.

## Core Loop

assign citizens to gathering, farming, and building jobs -> stockpile food, firewood, and tools for winter -> families form when housing exists and children grow into workers -> aging, disease, and disasters remove citizens -> expand or collapse

## Design Notes

Citizens are the main resource: every worker is a person who was born, ages, needs a house to start a family, and dies, so the town's age structure produces labor booms and busts years after a decision. There is no money and no tech tree; any building is available once its resources exist, and trade is barter with visiting ships that can also bring disease. Designer Luke Hodorowicz cited the Anno series as a big inspiration and left combat out, and the genre literature credits Banished with starting the survival city-builder trend.

## Relations

**uses**

- [Lifecycle and aging](../mechanic/lifecycle-aging.md) (core): Residents are born, age, work, start families, and die; age cohorts create delayed labor shortages.
- [Seasons](../mechanic/seasons.md) (core): Crops are planted and harvested on an annual cycle, and winter demands stored food and firewood.
- [Goods consumption](../mechanic/goods-consumption.md) (core): Each household consumes food, firewood, clothing, and tools; shortages lead to cold, illness, and starvation.
- [Crop cultivation](../mechanic/crop-cultivation.md) (supporting)
- [Work priorities](../mechanic/work-priorities.md) (supporting): The player sets worker counts per workplace and profession; unassigned citizens become laborers.
- [Hauling jobs](../mechanic/hauling-jobs.md) (supporting): Laborers carry resources to stockpiles and construction sites, so their number sets delivery speed.
- [Renewable regrowth](../mechanic/renewable-regrowth.md) (supporting): Foresters cut and replant forests; land used for forests or quarries cannot hold housing.
- [Storage and buffers](../mechanic/storage-capacity.md) (supporting)
- [Contagion](../mechanic/contagion.md) (supporting): Trade ships can bring illness from abroad.
- [Trade routes](../mechanic/trade-routes.md) (supporting): Resources are bartered with trade vessels at a trading post; there is no currency.
- [Random disasters](../mechanic/random-disasters.md) (supporting): Fires and tornadoes destroy buildings.
- [Romance and family](../mechanic/romance-family.md) (supporting): Couples need an empty house to start a family and have children.
- [Immigration by attractiveness](../mechanic/immigration-attractiveness.md) (supporting): Nomad groups can arrive and ask to join the town.
- [Pause and speed control](../mechanic/variable-speed.md) (supporting)
- [Building placement](../mechanic/free-placement.md) (supporting)
- [Fire spread](../mechanic/fire-spread.md) (supporting)

## Backlinks (computed)

**precedent for:** [Factories with a living workforce](../opportunity/living-workforce-factories.md)

## Claims

- Banished is credited with starting the survival city-builder trend. *(confidence: medium)* [[4](../source/src-wikipedia-city-building-game.md)]

## Sources

- [Banished (video game)](../source/src-wikipedia-banished.md)
- [Banished on Steam](../source/src-steam-2026-banished.md)
- [City-building game](../source/src-wikipedia-city-building-game.md)

---
Provenance: created in run `2026-10-24-catalog-ga`; reviewed in `2026-10-24-review-fixes`.
