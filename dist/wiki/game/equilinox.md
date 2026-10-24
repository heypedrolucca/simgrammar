# Equilinox

*Game* · `equilinox` · status: **sourced**

A relaxed nature-building game in which the player spreads biomes with grasses, places plants and animals that each have environmental requirements, and spends diversity points earned by healthy species on evolutions and genetic modifications.

| field | value |
|---|---|
| year | 2018 |
| developer | ThinMatrix |
| platforms | PC |
| subgenre | Ecosystem / evolution |
| sim domain | Biological / ecological |
| player role | Caretaker |
| agency model | Zoning / placement, Indirect incentive |
| time model | Real-time |
| sim scale | Facility |
| fidelity | Stylized |
| perspective | Free 3D camera |
| win structure | Open sandbox |
| failure model | Soft / recoverable |
| narrative mode | None |
| multiplayer | Single-player |
| modding | None |
| production tier | Indie |
| agent count order | ~100 |
| emergence | 2 |
| influence | 1 |
| cluster *(computed)* | C05 |
| core count *(computed)* | 3 |
| mechanic count *(computed)* | 8 |

## Summary

A relaxed nature-building game in which the player spreads biomes with grasses, places plants and animals that each have environmental requirements, and spends diversity points earned by healthy species on evolutions and genetic modifications.

## Core Loop

plant grasses to spread biomes -> place plants and animals whose requirements are met -> healthy species live longer, breed, and earn diversity points -> spend points on new species, genetic modifications, and evolutions -> complete tasks for rewards

## Design Notes

Equilinox, built solo by ThinMatrix, ties its economy to ecological fit: each species has a life cycle and requirements, and healthy individuals live longer, breed more, and yield more diversity points, the currency for new species and modifications. Evolution is a gated unlock (meet a species' evolution conditions, then pay to evolve) rather than simulated selection, which keeps the 120+ species on an authored progression. Biomes spread from planted grasses, so terrain type is itself a player-placed stock. Paid genetic modification matches the genome-modification proposal from run catalog-ge.

## Relations

**uses**

- [Habitat suitability](../mechanic/habitat-suitability.md) (core): Each species needs a biome, food, and nearby plants or water; satisfied individuals stay healthy, live longer, and breed, while unmet needs reduce health.
- [Milestone unlocks](../mechanic/milestone-unlocks.md) (core): Species evolve into new species once their conditions are met and points are paid, and 60+ tasks grant points or content.
- [Treasury and budget](../mechanic/budget-treasury.md) (core): Diversity points earned by healthy plants and animals are the single currency for buying species, modifications, and evolutions; repeatable tasks let players farm a steady income.
- [Lifecycle and aging](../mechanic/lifecycle-aging.md) (supporting): Plants and animals grow, eat, reproduce, and die on species-specific cycles.
- [Food web](../mechanic/food-web.md) (supporting): Some animals hunt others, so predator placement constrains prey populations.
- [Terraforming](../mechanic/terraforming.md) (supporting): Planted grasses convert ground into one of 10 biome types, and algae turns water into river for fish.
- [Building placement](../mechanic/free-placement.md) (supporting)
- [Collection goals](../mechanic/collection-goals.md) (supporting)

## Backlinks (computed)

**precedent for:** [Open-ended evolution sandbox](../opportunity/open-ended-evolution-sandbox.md)

## Sources

- [Equilinox on Steam](../source/src-steam-2026-equilinox.md)
- [Relaxing nature sim Equilinox is out and seems to be a hit with users](../source/src-gamingonlinux-2018-equilinox-release.md)

---
Provenance: created in run `2026-10-24-catalog-gd`.
