# Anno 117: Pax Romana

*Game* · `anno-117` · status: **sourced**

A Roman-era Anno city builder in which residents advance from Liberti to Patricians through categorized needs, buildings affect their neighbors, schools generate research, and modular ships guard multi-island trade.

| field | value |
|---|---|
| aliases | Anno 117 |
| year | 2025 |
| developer | Ubisoft Mainz |
| platforms | PC, Console |
| subgenre | City builder |
| subgenre secondary | Transport / logistics |
| sim domain | Urban, Economic, Industrial / logistics |
| player role | Planner / mayor |
| agency model | Zoning / placement, Direct unit control, Policy / parameter |
| time model | Real-time with pause |
| sim scale | Region |
| fidelity | Stylized |
| perspective | Free 3D camera |
| win structure | Open sandbox |
| failure model | Soft / recoverable |
| narrative mode | Hybrid |
| multiplayer | Single-player, Co-op |
| modding | Content |
| production tier | AAA |
| agent count order | Aggregate only |
| emergence | 3 |
| influence | 1 |
| influenced by | [Anno 1800](../game/anno-1800.md) |
| cluster *(computed)* | C01 |
| core count *(computed)* | 3 |
| mechanic count *(computed)* | 11 |

## Summary

A Roman-era Anno city builder in which residents advance from Liberti to Patricians through categorized needs, buildings affect their neighbors, schools generate research, and modular ships guard multi-island trade.

## Core Loop

settle Latium or Albion and house Liberti -> meet categorized needs with multi-island production chains -> residences advance toward Patricians -> schools produce research and temples belief -> ships carry goods on tracked routes -> defend routes and provinces

## Design Notes

Anno 117 loosens the strict tier-need ladder: needs fall into categories that can be partly filled, and each good carries attributes with benefits and drawbacks for population, income, health, and satisfaction. Placement matters more than in Anno 1800 because production buildings help or harm nearby structures, paved roads extend building range, and diagonal placement is allowed. Belief tied to chosen gods grants scaling bonuses, a system with no exact taxonomy match (see run proposal).

## Relations

**influenced by**

- [Anno 1800](../game/anno-1800.md)

**uses**

- [Population strata](../mechanic/population-strata.md) (core): Residences advance from Liberti up to Patricians based on access to goods and on nearby prestige or polluting buildings.
- [Goods consumption](../mechanic/goods-consumption.md) (core): Needs are grouped into categories that can be partly fulfilled; each good's attributes add benefits and drawbacks to population, income, health, and satisfaction.
- [Production chains](../mechanic/production-chain.md) (core): Chains span multiple islands and provinces, linked by warehouses, waystations, and hubs.
- [Adjacency scoring](../mechanic/adjacency-scoring.md) (supporting): Production buildings have positive or negative effects on nearby structures.
- [Trade routes](../mechanic/trade-routes.md) (supporting): Assigned ships carry goods between islands along routes that can be tracked and rerouted.
- [Vehicle routes and schedules](../mechanic/vehicle-route-scheduling.md) (supporting)
- [Tech tree](../mechanic/tech-tree.md) (supporting): Schools generate research points for a tree of over 100 unlocks, including repeatable technologies.
- [Road networks](../mechanic/road-network.md) (supporting): Paved roads extend the range and efficiency of structures.
- [Unit commands](../mechanic/unit-commands.md) (supporting): Melee, ranged, and siege units in a rock-paper-scissors system; warships protect routes from pirates.
- [Modular assembly](../mechanic/modular-assembly.md) (supporting): Ships are modular; adding oars or sails changes how they move.
- [Reputation](../mechanic/reputation.md) (supporting): Standing with the emperor's successor Calidus can earn Consul status or Proconsular authority.

## Sources

- [Anno 117: Pax Romana](../source/src-wikipedia-anno-117.md)

---
Provenance: created in run `2026-10-24-catalog-ga`.
