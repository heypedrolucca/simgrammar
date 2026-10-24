# Zoo Tycoon

*Game* · `zoo-tycoon` · status: **sourced**

A zoo management game in which the player builds exhibits whose terrain, foliage, shelters, and toys must suit each species, balancing animal happiness against guest happiness and income.

| field | value |
|---|---|
| year | 2001 |
| developer | Blue Fang Games |
| platforms | PC, Handheld |
| subgenre | Management / tycoon |
| sim domain | Biological / ecological, Economic |
| player role | Manager / owner |
| agency model | Zoning / placement, Policy / parameter |
| time model | Real-time with pause |
| sim scale | Facility |
| fidelity | Stylized |
| perspective | Isometric |
| win structure | Scenario goals |
| failure model | Soft / recoverable |
| narrative mode | None |
| multiplayer | Single-player |
| modding | Content |
| production tier | AA |
| agent count order | ~100 |
| emergence | 2 |
| influence | 3 |
| cluster *(computed)* | C01 |
| core count *(computed)* | 3 |
| mechanic count *(computed)* | 11 |

## Summary

A zoo management game in which the player builds exhibits whose terrain, foliage, shelters, and toys must suit each species, balancing animal happiness against guest happiness and income.

## Core Loop

fence an exhibit -> match terrain, foliage, rocks, shelter, and toys to the species -> animals grow happy and breed -> guests visit, spend, and react -> awards and income -> research and adopt more animals

## Design Notes

Zoo Tycoon's core rule is exhibit suitability: each species reports how well its exhibit's terrain mix, foliage, rocks, shelters, toys, and keeper care match its needs, and that suitability drives animal happiness. Guest happiness depends on animal happiness, the species on show, buildings, and scenery, so the two satisfaction meters are chained. Failures are physical: incompatible species in one exhibit kill each other, fences decay, and escaped animals attack guests and staff. Too many complaints about unhappy animals block new adoptions until habitats are fixed.

## Relations

**uses**

- [Habitat suitability](../mechanic/habitat-suitability.md) (core): Each species has preferred terrain types, foliage, rocks, shelters, toys, and companions; suitability drives happiness, and incompatible species in one exhibit kill each other.
- [Crowd preferences](../mechanic/crowd-preferences.md) (core): Guest happiness depends on the animals on show, their happiness, buildings such as restrooms and shops, and scenery.
- [Needs decay](../mechanic/needs-decay.md) (core): Animals need food, water, cleaning, and keeper attention that keepers supply on rounds.
- [Building placement](../mechanic/free-placement.md) (supporting): Fences, paths, buildings, foliage, and scenery are placed on a tile map.
- [Wear and breakdown](../mechanic/wear-breakdown.md) (supporting): Fences decay and must be repaired by maintenance workers to prevent escapes.
- [Staff hiring and rosters](../mechanic/staff-hiring.md) (supporting): Zookeepers, maintenance workers, and tour guides are hired.
- [Tech tree](../mechanic/tech-tree.md) (supporting): In freeform mode, money spent on research unlocks animals, buildings, and scenery.
- [Scenario objectives](../mechanic/scenario-objectives.md) (supporting): Scenarios set targets such as a guest happiness level, exhibit suitability, animal count, or breeding a species.
- [Lifecycle and aging](../mechanic/lifecycle-aging.md) (supporting): Animals breed when content; babies grow into adults.
- [Decoration and beauty](../mechanic/decoration-beauty.md) (supporting): Scenery such as topiary, lamp posts, and benches gives a small guest happiness boost.
- [Pause and speed control](../mechanic/variable-speed.md) (supporting)

## Backlinks (computed)

**influenced:** [Planet Zoo](../game/planet-zoo.md)

## Sources

- [Zoo Tycoon (2001 video game)](../source/src-wikipedia-zoo-tycoon.md)

---
Provenance: created in run `2026-10-24-catalog-ge`; reviewed in `2026-10-24-review-fixes`.
