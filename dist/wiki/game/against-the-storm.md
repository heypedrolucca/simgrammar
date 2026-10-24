# Against the Storm

*Game* · `against-the-storm` · status: **sourced**

A roguelite city builder in which each settlement must fill a reputation gauge before the Queen's impatience runs out, balancing three villager species' needs while opening dangerous forest glades under a recurring blightstorm.

| field | value |
|---|---|
| year | 2021 |
| year full release | 2023 |
| developer | Eremite Games |
| platforms | PC, Console, Handheld |
| subgenre | City builder |
| sim domain | Urban, Economic |
| player role | Planner / mayor |
| agency model | Zoning / placement, Policy / parameter |
| time model | Real-time with pause |
| sim scale | Settlement |
| fidelity | Stylized |
| perspective | Isometric |
| win structure | Scenario goals |
| failure model | Hard restart |
| narrative mode | Hybrid |
| multiplayer | Single-player |
| modding | None |
| production tier | Indie |
| agent count order | ~100 |
| emergence | 3 |
| influence | 2 |
| cluster *(computed)* | C04 |
| core count *(computed)* | 4 |
| mechanic count *(computed)* | 13 |

## Summary

A roguelite city builder in which each settlement must fill a reputation gauge before the Queen's impatience runs out, balancing three villager species' needs while opening dangerous forest glades under a recurring blightstorm.

## Core Loop

embark with three species and a few goods -> build camps, production, and housing in a cleared glade -> meet each species' needs to keep it content -> complete orders and open glades for reputation -> win before the Queen's impatience fills -> carry rewards to the Smoldering City

## Design Notes

Against the Storm compresses a city builder into short runs: each settlement is a fresh generated map with a race between two gauges, reputation that the player fills and the Queen's impatience that fills on its own, and earning reputation also lowers impatience. Each village hosts three of seven species with distinct housing, food, luxury, and recreation preferences, so the same production network must serve conflicting demands. Rewards carry over to upgrade the Smoldering City between runs, a meta-progression system the taxonomy lacks (see run proposal).

## Relations

**uses**

- [Crisis countdown](../mechanic/crisis-countdown.md) (core): The Queen's Impatience gauge fills over time and recalls the player when full; recurring storms raise pressure between calm periods.
- [Scenario objectives](../mechanic/scenario-objectives.md) (core): Each settlement is won by filling the Reputation gauge through orders, villager contentment, and opened glades.
- [Production chains](../mechanic/production-chain.md) (core): Production buildings convert goods by recipes such as raincoats, ale, and pies, chosen from a run-specific building set.
- [Citizen satisfaction](../mechanic/citizen-satisfaction.md) (core): Contentment per species responds to met needs; discontented villagers leave and content ones raise reputation.
- [Population strata](../mechanic/population-strata.md) (supporting): Seven species with distinct preferences; three per village.
- [Procedural terrain](../mechanic/procedural-terrain.md) (supporting): A new map is generated for each settlement across six biomes.
- [Seasons](../mechanic/seasons.md) (supporting): A calm building period alternates with the storm.
- [Fog of war](../mechanic/fog-of-war.md) (supporting): Forest glades stay hidden until cut open and may hold boons or threats.
- [Adaptive threat scaling](../mechanic/adaptive-threat-scaling.md) (supporting): Forest hostility rises as the settlement cuts trees and opens glades.
- [Tech tree](../mechanic/tech-tree.md) (supporting): Meta-progression resources upgrade the Smoldering City between runs.
- [Trade routes](../mechanic/trade-routes.md) (supporting): A visiting trader's wares change each year.
- [Pause and speed control](../mechanic/variable-speed.md) (supporting)
- [Building placement](../mechanic/free-placement.md) (supporting)

## Sources

- [Against the Storm (video game)](../source/src-wikipedia-against-the-storm.md)
- [Against the Storm](../source/src-pcgamingwiki-2026-against-the-storm.md)
- [Against the Storm on Steam](../source/src-steam-2026-against-the-storm.md)

---
Provenance: created in run `2026-10-24-catalog-ga`; reviewed in `2026-10-24-review-fixes`.
