# Terra Nil

*Game* · `terra-nil` · status: **sourced**

A reverse city builder in which the player places machines to clean toxic soil, restore water, and grow biomes on a barren map, then recycles every building and leaves.

| field | value |
|---|---|
| year | 2023 |
| developer | Free Lives |
| platforms | PC, Mobile, Console, Handheld |
| subgenre | City builder |
| subgenre secondary | Ecosystem / evolution |
| sim domain | Biological / ecological, Planetary / natural |
| player role | Caretaker |
| agency model | Zoning / placement |
| time model | Real-time |
| sim scale | Region |
| fidelity | Stylized |
| perspective | Isometric |
| win structure | Scenario goals |
| failure model | Soft / recoverable |
| narrative mode | None |
| multiplayer | Single-player |
| modding | None |
| production tier | Indie |
| agent count order | None |
| emergence | 2 |
| influence | 1 |
| cluster *(computed)* | C07 |
| core count *(computed)* | 2 |
| mechanic count *(computed)* | 6 |

## Summary

A reverse city builder in which the player places machines to clean toxic soil, restore water, and grow biomes on a barren map, then recycles every building and leaves.

## Core Loop

place wind turbines on rock -> power toxin scrubbers that clean soil -> irrigate and pump water into riverbeds -> upgrade to grow wetlands, meadows, and forest -> attract animals and restore weather -> recycle every building and leave

## Design Notes

It inverts the city-builder loop: growth is measured in restored tiles rather than population, and points earned per restored tile are the only currency for further buildings, so efficient placement compounds. The final step requires recycling all infrastructure to build an airship and leave, so a layout must be removable as well as productive. Subgenre is set to city-builder because its lineage is placement and budget puzzles rather than population or evolution modeling. It began as a Ludum Dare 45 entry in October 2019.

## Relations

**uses**

- [Building placement](../mechanic/free-placement.md) (core): Buildings have placement rules: wind turbines go only on stone tiles and power toxin scrubbers, which clean soil so irrigators can green it.
- [Treasury and budget](../mechanic/budget-treasury.md) (core): Each restored tile earns points, and points are the only currency for buildings and upgrades, so a map can stall if spending outruns restoration.
- [Hydrology](../mechanic/hydrology.md) (supporting): Pumps refill dried riverbeds and tools carve new rivers.
- [Terraforming](../mechanic/terraforming.md) (supporting): Tools create new rivers and some stone tiles.
- [Habitat suitability](../mechanic/habitat-suitability.md) (supporting): Restored biomes attract deer, birds, fish, and bears.
- [Scenario objectives](../mechanic/scenario-objectives.md) (supporting): Each map sets restoration targets before the player can recycle buildings and leave.

## Sources

- [Terra Nil](../source/src-wikipedia-terra-nil.md)

---
Provenance: created in run `2026-10-24-catalog-gb`.
