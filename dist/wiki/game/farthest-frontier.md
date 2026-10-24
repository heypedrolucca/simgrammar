# Farthest Frontier

*Game* · `farthest-frontier` · status: **sourced**

A frontier-town city builder in which crop rotation, soil fertility, diet variety, clean water, and healers decide whether named diseases spread, while prosperity draws stronger raiders against walled defenses.

| field | value |
|---|---|
| year | 2022 |
| year full release | 2025 |
| developer | Crate Entertainment |
| platforms | PC |
| subgenre | City builder |
| sim domain | Urban, Biological / ecological, Military / conflict |
| player role | Planner / mayor |
| agency model | Zoning / placement, Policy / parameter, Direct unit control |
| time model | Real-time with pause |
| sim scale | Settlement |
| fidelity | Systemic |
| perspective | Free 3D camera |
| win structure | Open sandbox |
| failure model | Cascading collapse |
| narrative mode | Emergent |
| multiplayer | Single-player |
| modding | None |
| production tier | Indie |
| agent count order | ~100 |
| emergence | 3 |
| influence | 1 |
| cluster *(computed)* | C02 |
| core count *(computed)* | 3 |
| mechanic count *(computed)* | 14 |

## Summary

A frontier-town city builder in which crop rotation, soil fertility, diet variety, clean water, and healers decide whether named diseases spread, while prosperity draws stronger raiders against walled defenses.

## Core Loop

gather, hunt, forage, and farm -> rotate crops to hold soil fertility -> feed a varied diet and supply clean water, clothing, and healers against disease -> upgrade housing and the town center as desirability rises -> fortify against raiders drawn by prosperity

## Design Notes

Farthest Frontier makes public health the main failure path: dysentery, cholera, tetanus, rabies, frostbite, and bubonic plague each have causes the player can address with clean water, clothing and shoes, healers, and rat catchers. Farming adds soil state, with 12 crops that must be rotated and fields improved by clearing weeds and rocks, and 19 food types with berries and greens preventing scurvy. Prosperity raises raider strength, so growth itself increases military pressure.

## Relations

**uses**

- [Crop cultivation](../mechanic/crop-cultivation.md) (core): Twelve crops with rotation to preserve soil fertility; fields improve by clearing weeds and rocks and adjusting the soil mix.
- [Contagion](../mechanic/contagion.md) (core): Dysentery, cholera, tetanus, rabies, frostbite, and plague spread or strike based on water, clothing, rats, and healer coverage.
- [Goods consumption](../mechanic/goods-consumption.md) (core): Nineteen food types; diet variety, including berries and greens against scurvy, is needed for health.
- [Adaptive threat scaling](../mechanic/adaptive-threat-scaling.md) (supporting): Rising prosperity draws stronger raiders and foreign armies; difficulty is adjustable and pacifist mode removes them.
- [Raid defense](../mechanic/raid-defense.md) (supporting): Palisades, stone walls, towers, barracks, and equipped soldiers.
- [Population strata](../mechanic/population-strata.md) (supporting): Housing and the town center advance through tiers as prosperity and desirability grow.
- [Decoration and beauty](../mechanic/decoration-beauty.md) (supporting): Desirability from surroundings gates housing upgrades.
- [Tech tree](../mechanic/tech-tree.md) (supporting): A tree of over 140 points of upgrades.
- [Seasons](../mechanic/seasons.md) (supporting)
- [Production chains](../mechanic/production-chain.md) (supporting)
- [Trade routes](../mechanic/trade-routes.md) (supporting): Crafted goods are traded for resources the town lacks.
- [Pause and speed control](../mechanic/variable-speed.md) (supporting)
- [Building placement](../mechanic/free-placement.md) (supporting)
- [Storage and buffers](../mechanic/storage-capacity.md) (supporting)

## Sources

- [Farthest Frontier](../source/src-wikipedia-farthest-frontier.md)
- [Farthest Frontier on Steam](../source/src-steam-2026-farthest-frontier.md)

---
Provenance: created in run `2026-10-24-catalog-ga`; reviewed in `2026-10-24-review-fixes`.
