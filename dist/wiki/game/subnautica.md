# Subnautica

*Game* · `subnautica` · status: **sourced**

An underwater survival game on an ocean planet where the player manages oxygen, food, and water while crafting tools, submersibles, and bases to explore deeper and escape.

| field | value |
|---|---|
| year | 2014 |
| year full release | 2018 |
| developer | Unknown Worlds Entertainment |
| platforms | PC, Console, Handheld, Mobile |
| subgenre | Survival sim |
| sim domain | Biological / ecological |
| player role | Inhabitant |
| agency model | Direct avatar |
| time model | Real-time |
| sim scale | Individual |
| fidelity | Stylized |
| perspective | First-person |
| win structure | Completion |
| failure model | Soft / recoverable |
| narrative mode | Authored |
| multiplayer | Single-player |
| modding | Scripting |
| production tier | Indie |
| agent count order | ~100 |
| emergence | 2 |
| influence | 3 |
| boundary case | True |
| cluster *(computed)* | C05 |
| core count *(computed)* | 2 |
| mechanic count *(computed)* | 8 |

## Summary

An underwater survival game on an ocean planet where the player manages oxygen, food, and water while crafting tools, submersibles, and bases to explore deeper and escape.

## Core Loop

dive from the lifepod -> gather resources and recover blueprints -> craft tools, vehicles, and base modules -> manage oxygen, food, and water -> dive deeper into new biomes and story sites -> build the means to escape the planet

## Design Notes

Included as a boundary case: the map, story, and progression are hand-authored, and the simulated layer is a set of survival meters plus base power and fauna behavior. Oxygen is the distinctive meter because it ties survival to depth and distance from air, making range a resource. Mode settings remove meters to change genre: Freedom drops hunger and thirst, Creative drops all depleting stats, and Hardcore adds permanent death without low-oxygen warnings.

## Relations

**uses**

- [Survival meters](../mechanic/survival-meters.md) (core): Health, hunger, thirst, and oxygen deplete in Survival mode; oxygen limits each dive's depth and duration, Freedom mode removes hunger and thirst, and Creative removes all depleting stats.
- [Hand crafting](../mechanic/hand-crafting.md) (core): Gathered resources are crafted into tools, base parts, and submersibles from blueprints the player has recovered.
- [Building placement](../mechanic/free-placement.md) (supporting): Bases are assembled from placed modules.
- [Power grid](../mechanic/power-grid.md) (supporting): Bases and vehicles need energy sources.
- [Day-night cycle](../mechanic/day-night-cycle.md) (supporting): A day-night cycle and frequent eclipses change visibility.
- [Spoilage](../mechanic/spoilage.md) (supporting): Cooked fish spoils over time; cured fish does not.
- [Permadeath](../mechanic/permadeath.md) (supporting): Optional in Hardcore mode.
- [Direct avatar control](../mechanic/direct-avatar.md) (supporting)

## Sources

- [Subnautica](../source/src-wikipedia-subnautica.md)

---
Provenance: created in run `2026-10-24-catalog-gb`.
