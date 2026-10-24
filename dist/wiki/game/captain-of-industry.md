# Captain of Industry

*Game* · `captain-of-industry` · status: **sourced**

An industrial colony builder in which the player reshapes island terrain with excavators and trucks, runs production chains to feed, house, and power a settlement, and spends the Unity its satisfied population generates on edicts, quick builds, and world-map expansion.

| field | value |
|---|---|
| year | 2022 |
| developer | MaFi Games |
| platforms | PC |
| subgenre | Factory / automation |
| subgenre secondary | City builder |
| sim domain | Industrial / logistics, Urban, Economic |
| player role | Engineer / designer |
| agency model | Zoning / placement, Order queue, Policy / parameter |
| time model | Real-time with pause |
| sim scale | Settlement |
| fidelity | Systemic |
| perspective | Free 3D camera |
| win structure | Open sandbox |
| failure model | Cascading collapse |
| narrative mode | None |
| multiplayer | Single-player |
| modding | Scripting |
| production tier | Indie |
| agent count order | ~100 |
| emergence | 3 |
| influence | 1 |
| influenced by |  |
| cluster *(computed)* | C01 |
| core count *(computed)* | 6 |
| mechanic count *(computed)* | 20 |

## Summary

An industrial colony builder in which the player reshapes island terrain with excavators and trucks, runs production chains to feed, house, and power a settlement, and spends the Unity its satisfied population generates on edicts, quick builds, and world-map expansion.

## Core Loop

designate mining and dumping areas -> trucks haul ore and rock -> smelt and refine into goods -> feed, power, and house the population -> satisfied needs generate Unity -> spend Unity and products on research, edicts, and ship expeditions -> expand and terraform

## Design Notes

Captain of Industry joins a factory game to a settlement whose population is both labor and a consumer: residents need housing, food, water, electricity, healthcare, and household goods, each fully satisfied need yields about one to two Unity per month, and Unity buys edicts, outposts, quick trades, instant construction, and emergency repairs. Every working vehicle and many buildings consume crafted Maintenance I, II, or III; below 75% a monthly breakdown roll begins, reaching 50% at zero, so maintenance is itself a production chain whose failure cascades through the economy. Terrain is a stock of materials: excavators dig inside a Mine Control Tower's area, trucks dump rock and dirt that settle at per-material angles of repose (about 42 degrees for loose dirt to 78 for hardened rock), and dumping reclaims ocean for ports. A ship explores a world map for islands, refugees, and trade partners. Unity works like a political-capital currency earned from welfare, which the taxonomy lacks; this run proposed one.

## Relations

**uses**

- [Production chains](../mechanic/production-chain.md) (core): Smelters, refineries, chemical plants, food processors, and assembly lines run recipe chains from iron and copper ore to electronics, fuel, consumer goods, and nuclear fuel across 100+ technologies.
- [Hauling jobs](../mechanic/hauling-jobs.md) (core): Trucks are assigned to mines, storages, and buildings and automatically deliver products where they are needed, so fleet size and road layout cap throughput before belts and trains replace them.
- [Terraforming](../mechanic/terraforming.md) (core): Mining designations inside a Mine Control Tower area lower terrain and dumping designations raise it; loose material settles at per-material angles of repose, retaining walls stabilize slopes, and dumping can reclaim ocean.
- [Goods consumption](../mechanic/goods-consumption.md) (core): Residents consume food, water, electricity, healthcare, and household goods; each fully satisfied need yields Unity, and unmet food or health shrinks the population.
- [Wear and breakdown](../mechanic/wear-breakdown.md) (core): Working vehicles and buildings consume Maintenance I to III crafted at depots (idle at about a third); below 75% maintenance a breakdown is rolled monthly with chance rising to 50% at zero.
- [Resource extraction](../mechanic/resource-extraction.md) (core): Excavators dig ore, coal, limestone, and rock from designated terrain, while oil rigs, quartz and uranium mines, and water pumps work fixed deposits and outposts.
- [Designation orders](../mechanic/designation-orders.md) (supporting): The player paints mining and dumping designations, and excavators and trucks assigned to a Mine Control Tower carry out the work inside its area.
- [Conveyor transport](../mechanic/conveyor-transport.md) (supporting): Belts and pipes give high-throughput direct links between machines once truck logistics become a bottleneck.
- [Power grid](../mechanic/power-grid.md) (supporting): Generators up to nuclear reactors feed the settlement and factories, and residents require electricity as one of their needs.
- [Tech tree](../mechanic/tech-tree.md) (supporting): Research labs consume products and Unity to unlock over 100 technologies from basic smelting to space flight.
- [Pollution spread](../mechanic/pollution-spread.md) (supporting): Air and water pollution and unmanaged waste spread disease among the population.
- [Byproducts and waste](../mechanic/byproducts-waste.md) (supporting): Production emits slag, waste, carbon dioxide, wastewater, and spent nuclear fuel that must be dumped, treated, recycled, or stored.
- [Policy toggles](../mechanic/policy-toggles.md) (supporting): Captain's Office edicts change settlement rules, such as raising population growth by tier, for a monthly Unity cost.
- [Trade routes](../mechanic/trade-routes.md) (supporting): Ships explore a world map to discover islands and trading partners; quick trades and recurring contracts exchange goods.
- [Crop cultivation](../mechanic/crop-cultivation.md) (supporting): Farms grow crops for food and industrial inputs, fertilizer boosts yields, and greenhouses grow advanced crops.
- [Storage and buffers](../mechanic/storage-capacity.md) (supporting): Storages and loose storage piles buffer materials, and full outputs stall production upstream.
- [Vehicle routes and schedules](../mechanic/vehicle-route-scheduling.md) (supporting): Trains move bulk cargo over long distances, and ships run trade contracts between the home island and partners.
- [Periodic ticks](../mechanic/periodic-ticks.md) (supporting): Unity income, population change, edict costs, and maintenance breakdown rolls resolve monthly.
- [Political capital](../mechanic/political-capital.md) (supporting): Each fully satisfied settlement need yields about 1 to 2 Unity per month, spent on edicts, outposts, quick trades, instant construction, and emergency repairs.
- [Machine boosting](../mechanic/machine-boosting.md) (supporting): Unity is spent on building boosts (0.25 Unity each) that speed up individual buildings.

## Backlinks (computed)

**precedent for:** [Factories with a living workforce](../opportunity/living-workforce-factories.md)

## Claims

- Captain of Industry entered Steam Early Access on 2022-05-31 and was still in Early Access in October 2026, with the developers estimating two to four more years. *(confidence: high)* [[11](../source/src-steam-2026-captain-of-industry.md)]

## Sources

- [Captain of Industry](../source/src-steam-2026-captain-of-industry.md)
- [Maintenance](../source/src-coiwiki-2026-maintenance.md)
- [Unity](../source/src-coiwiki-2026-unity.md)
- [Population](../source/src-coiwiki-2026-population.md)
- [Dumping Designation](../source/src-coiwiki-2026-dumping-designation.md)

---
Provenance: created in run `2026-10-24-catalog-gh`.
