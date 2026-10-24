# Foundation

*Game* · `foundation` · status: **sourced**

A gridless medieval city builder in which painted zones grow homes organically, monuments are assembled from modular parts, and the village advances along Labor, Clergy, or Kingdom estates.

| field | value |
|---|---|
| year | 2019 |
| year full release | 2025 |
| developer | Polymorph Games |
| platforms | PC |
| subgenre | City builder |
| sim domain | Urban, Economic, Political / governance |
| player role | Planner / mayor |
| agency model | Zoning / placement, Policy / parameter |
| time model | Real-time with pause |
| sim scale | Settlement |
| fidelity | Stylized |
| perspective | Free 3D camera |
| win structure | Open sandbox |
| failure model | Soft / recoverable |
| narrative mode | Emergent |
| multiplayer | Single-player |
| modding | Content |
| production tier | Indie |
| agent count order | ~100 |
| emergence | 2 |
| influence | 1 |
| cluster *(computed)* | C02 |
| core count *(computed)* | 2 |
| mechanic count *(computed)* | 9 |

## Summary

A gridless medieval city builder in which painted zones grow homes organically, monuments are assembled from modular parts, and the village advances along Labor, Clergy, or Kingdom estates.

## Core Loop

paint residential, road, patrol, and forestry zones -> villagers build homes inside them -> assign workers and production chains -> trade with neighbors and pay taxes -> advance Labor, Clergy, or Kingdom estates -> assemble monuments from parts

## Design Notes

Foundation separates intent from layout: the player paints areas for homes, roads, patrols, and forestry, and housing appears inside them without a grid. Major buildings are not fixed footprints but assemblies of parts, so a monument's function and capacity follow from the modules chosen. Progress runs along three estates, which can be specialized or combined.

## Relations

**uses**

- [Zoning](../mechanic/zoning.md) (core): A painting tool marks areas for homes, roads, patrol routes, and forest extraction; homes fill residential zones organically.
- [Modular assembly](../mechanic/modular-assembly.md) (core): Buildings and monuments are assembled from individual parts whose choice sets function and appearance.
- [Building placement](../mechanic/free-placement.md) (supporting): Buildings are placed and rotated without a grid.
- [Production chains](../mechanic/production-chain.md) (supporting)
- [Trade routes](../mechanic/trade-routes.md) (supporting): Trade with neighboring villages.
- [Taxation](../mechanic/taxation.md) (supporting)
- [Milestone unlocks](../mechanic/milestone-unlocks.md) (supporting): Progress unlocks through tiers guided by a book, along Labor, Clergy, or Kingdom estates.
- [Goods consumption](../mechanic/goods-consumption.md) (supporting)
- [Pause and speed control](../mechanic/variable-speed.md) (supporting)

## Sources

- [Foundation (video game)](../source/src-wikipedia-foundation-video-game.md)
- [Foundation on Steam](../source/src-steam-2026-foundation.md)

---
Provenance: created in run `2026-10-24-catalog-ga`; reviewed in `2026-10-24-review-fixes`.
