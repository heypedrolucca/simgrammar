# Timberborn

*Game* · `timberborn` · status: **sourced**

A city builder for beaver colonies in which simulated water flows over terrain, recurring droughts and toxic badtides cut or poison it, and players dam, channel, and store water while building upward.

| field | value |
|---|---|
| year | 2021 |
| year full release | 2026 |
| developer | Mechanistry |
| platforms | PC |
| subgenre | City builder |
| sim domain | Urban, Planetary / natural, Biological / ecological |
| player role | Planner / mayor |
| agency model | Zoning / placement, Policy / parameter, Programmatic |
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
| influence | 1 |
| cluster *(computed)* | C10 |
| core count *(computed)* | 2 |
| mechanic count *(computed)* | 13 |

## Summary

A city builder for beaver colonies in which simulated water flows over terrain, recurring droughts and toxic badtides cut or poison it, and players dam, channel, and store water while building upward.

## Core Loop

dam and channel rivers -> irrigate farms and forests from stored water -> beavers work, eat, and seek wellbeing -> a drought or badtide cuts or poisons the flow -> stockpiles and reservoirs carry the colony through -> build upward and expand

## Design Notes

Water is a simulated field rather than a resource count: a 2D model adapted from erosion simulation linked each tile to four neighbors by virtual pipes and was replaced by 3D water in Update 6 (October 2024), so dams, floodgates, and canals change where moisture reaches crops. Recurring droughts grow harsher and badtides turn sources into contaminating badwater, so play alternates between building reservoirs and surviving a known dry period. Limited space pushes housing and workshops into vertical stacks, and sensors and relays let players automate floodgates.

## Relations

**uses**

- [Hydrology](../mechanic/hydrology.md) (core): Tiles exchange water through virtual pipes with evaporation; moisture spreads to nearby land and falls off sharply uphill; dams, levees, floodgates, and canals redirect flow.
- [Crisis countdown](../mechanic/crisis-countdown.md) (core): Recurring droughts switch sources off and badtides release contaminating badwater; both grow harsher over time and are signalled in advance.
- [Terraforming](../mechanic/terraforming.md) (supporting): Explosives dig tunnels and reshape terrain.
- [Vertical layers](../mechanic/vertical-layers.md) (supporting): Lodges and workshops stack on platforms; ziplines and tubeways move beavers between levels.
- [Crop cultivation](../mechanic/crop-cultivation.md) (supporting): Crops grow only on irrigated soil and fail when it dries.
- [Needs decay](../mechanic/needs-decay.md) (supporting): Beavers need food, water, rest, and wellbeing from diet variety, entertainment, and decorations.
- [Storage and buffers](../mechanic/storage-capacity.md) (supporting): Water tanks and warehouses buffer droughts.
- [Power grid](../mechanic/power-grid.md) (supporting): Water wheels and other generators power workshops and bots through a connected network.
- [Signal circuits](../mechanic/signal-circuits.md) (supporting): Sensors, relays, and counters control dams and factories.
- [Hauling jobs](../mechanic/hauling-jobs.md) (supporting)
- [Lifecycle and aging](../mechanic/lifecycle-aging.md) (supporting)
- [Pause and speed control](../mechanic/variable-speed.md) (supporting)
- [Building placement](../mechanic/free-placement.md) (supporting)

## Backlinks (computed)

**precedent for:** [Learned regional weather](../opportunity/learned-weather-layer.md)

## Sources

- [Timberborn](../source/src-wikipedia-timberborn.md)
- [Timberborn on Steam](../source/src-steam-2026-timberborn.md)
- [Deep Dive: Designing the dynamic irrigation and water systems in Timberborn](../source/src-amielanczyk-2023-timberborn-water.md)

---
Provenance: created in run `2026-10-24-catalog-ga`; reviewed in `2026-10-24-review-fixes`.
