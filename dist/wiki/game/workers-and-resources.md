# Workers & Resources: Soviet Republic

*Game* · `workers-and-resources` · status: **sourced**

A planned-economy city builder in which every building, commodity, and citizen moves through explicit logistics, from construction materials delivered by truck to exports at border customs for rubles or dollars.

| field | value |
|---|---|
| aliases | Workers and Resources |
| year | 2019 |
| year full release | 2024 |
| developer | 3Division |
| platforms | PC |
| subgenre | City builder |
| subgenre secondary | Transport / logistics |
| sim domain | Urban, Industrial / logistics, Economic |
| player role | Planner / mayor |
| agency model | Zoning / placement, Policy / parameter |
| time model | Real-time with pause |
| sim scale | Region |
| fidelity | Systemic |
| perspective | Free 3D camera |
| win structure | Open sandbox |
| failure model | Soft / recoverable |
| narrative mode | Emergent |
| multiplayer | Single-player |
| modding | Content |
| production tier | Indie |
| agent count order | ~1,000 |
| emergence | 3 |
| influence | 1 |
| cluster *(computed)* | C01 |
| core count *(computed)* | 3 |
| mechanic count *(computed)* | 13 |

## Summary

A planned-economy city builder in which every building, commodity, and citizen moves through explicit logistics, from construction materials delivered by truck to exports at border customs for rubles or dollars.

## Core Loop

set up construction offices and deliver materials to sites -> extract and process over 30 commodities by truck, rail, conveyor, and pipe -> house citizens near jobs and transit -> supply food, clothing, heat, and services to keep health, happiness, and loyalty -> export at customs for rubles or dollars -> import what the republic lacks

## Design Notes

Workers & Resources treats construction itself as logistics: buildings and roads need delivered concrete, steel, and prefab panels plus workers from the player's construction offices, or imported foreign labor at a cost, a system the taxonomy lacks (see run proposal). Over 30 commodities move by mode suited to their form (pipes and tanks for liquids, conveyors and trucks for ores, covered vehicles for goods), so freight network design is the main puzzle. Trade runs through East and West customs houses, flooding one bloc's market lowers returns, and heating demand rising in winter ties utilities to the calendar.

## Relations

**uses**

- [Production chains](../mechanic/production-chain.md) (core): Over 30 commodities are extracted, processed, and stored in staffed plants.
- [Vehicle routes and schedules](../mechanic/vehicle-route-scheduling.md) (core): Trucks, trains, ships, and aircraft are assigned to depots and routes that move goods and workers between buildings.
- [Trade routes](../mechanic/trade-routes.md) (core): Exports and imports pass through customs houses at Eastern (rubles) and Western (dollars) borders.
- [Conveyor transport](../mechanic/conveyor-transport.md) (supporting): Conveyors move ores and bulk goods between facilities.
- [Fluid pipe networks](../mechanic/fluid-pipe-network.md) (supporting): Liquids, water, and heating travel through pipes and tanks.
- [Public transit lines](../mechanic/public-transit.md) (supporting): Buses, trams, trains, subways, ships, and planes carry citizens.
- [Rail signaling](../mechanic/rail-signaling.md) (supporting): Rail signals and interchanges govern shared track.
- [Supply-demand pricing](../mechanic/supply-demand-pricing.md) (supporting): Flooding one market lowers returns there.
- [Goods consumption](../mechanic/goods-consumption.md) (supporting): Citizens need food, clothing, and alcohol from shops.
- [Citizen satisfaction](../mechanic/citizen-satisfaction.md) (supporting): Health and happiness decide whether citizens stay; low loyalty raises crime and lowers work efficiency.
- [Education and workforce](../mechanic/education-workforce.md) (supporting): Optional complex education gates skilled jobs.
- [Seasons](../mechanic/seasons.md) (supporting): Optional seasons raise heating demand in winter.
- [Storage and buffers](../mechanic/storage-capacity.md) (supporting)

## Backlinks (computed)

**precedent for:** [Factories with a living workforce](../opportunity/living-workforce-factories.md)

## Sources

- [Workers & Resources: Soviet Republic](../source/src-wikipedia-workers-and-resources.md)
- [Workers & Resources: Soviet Republic on Steam](../source/src-steam-2026-workers-and-resources.md)

---
Provenance: created in run `2026-10-24-catalog-ga`.
