# Planet Zoo

*Game* · `planet-zoo` · status: **sourced**

A zoo management game where the player builds habitats to meet each species' welfare needs, manages genetics and breeding, and raises a conservation rating, using Planet Coaster's building tools.

| field | value |
|---|---|
| year | 2019 |
| developer | Frontier Developments |
| platforms | PC, Console |
| subgenre | Management / tycoon |
| subgenre secondary | Ecosystem / evolution |
| sim domain | Biological / ecological, Economic |
| player role | Manager / owner |
| agency model | Zoning / placement, Policy / parameter |
| time model | Real-time with pause |
| sim scale | Facility |
| fidelity | Systemic |
| perspective | Free 3D camera |
| win structure | Open sandbox |
| failure model | Soft / recoverable |
| narrative mode | None |
| multiplayer | Single-player, Async / shared content |
| modding | Content |
| production tier | AA |
| agent count order | ~1,000 |
| emergence | 3 |
| influence | 2 |
| influenced by | [Zoo Tycoon](../game/zoo-tycoon.md), [Planet Coaster](../game/planet-coaster.md) |
| cluster *(computed)* | C01 |
| core count *(computed)* | 3 |
| mechanic count *(computed)* | 15 |

## Summary

A zoo management game where the player builds habitats to meet each species' welfare needs, manages genetics and breeding, and raises a conservation rating, using Planet Coaster's building tools.

## Core Loop

build a habitat for a species' needs -> animals respond to space, terrain, enrichment, and group size -> breed and manage genomes -> trade or release animals for conservation -> guests pay and learn -> expand the zoo

## Design Notes

Planet Zoo gives each animal species a requirements profile (habitat size, land and water, terrain and plant biome, temperature, group size and sex ratio, enrichment, privacy, and guest exposure) and reports the shortfalls as welfare, so habitat design is a constraint-satisfaction problem. Each animal carries a genome that affects lifespan, size, health, and fertility; offspring inherit it, and inbreeding harms the young, which turns breeding into a population-genetics task. Franchise mode connects zoos to an online market where players buy and trade animals with conservation credits. It reuses Planet Coaster's construction and Workshop tools.

## Relations

**influenced by**

- [Zoo Tycoon](../game/zoo-tycoon.md)
- [Planet Coaster](../game/planet-coaster.md)

**uses**

- [Habitat suitability](../mechanic/habitat-suitability.md) (core): Each species needs habitat size, land and water area, biome terrain and plants, temperature, shelter, and enrichment; welfare drops when any requirement is unmet.
- [Trait inheritance](../mechanic/trait-inheritance.md) (core): Animals carry genomes that set lifespan, size, health, and fertility; offspring inherit them, and inbreeding causes harmful effects.
- [Needs decay](../mechanic/needs-decay.md) (core): Animals have food, water, social, enrichment, and privacy needs whose shortfalls lower welfare and can cause illness.
- [Player-driven markets](../mechanic/player-driven-market.md) (supporting): In Franchise mode an online animal market shared across players lists animals for sale and trade, priced in conservation credits.
- [Reputation](../mechanic/reputation.md) (supporting): A conservation rating rises with endangered species, releases to the wild, and education.
- [Crowd preferences](../mechanic/crowd-preferences.md) (supporting): Guests choose exhibits, shops, and talks and react to animal welfare and park layout.
- [Staff hiring and rosters](../mechanic/staff-hiring.md) (supporting): Keepers, vets, mechanics, security, and vendors are hired with work zones and facility needs.
- [Lifecycle and aging](../mechanic/lifecycle-aging.md) (supporting): Animals age from juveniles to adults and die of old age.
- [Modular assembly](../mechanic/modular-assembly.md) (supporting): Barriers, buildings, and scenery use Planet Coaster's modular piece system.
- [Tech tree](../mechanic/tech-tree.md) (supporting): Vets research species to unlock knowledge and enrichment items.
- [Content sharing](../mechanic/content-sharing.md) (supporting): Habitat and building blueprints are shared on the Steam Workshop.
- [Day-night cycle](../mechanic/day-night-cycle.md) (supporting)
- [Weather](../mechanic/weather.md) (supporting)
- [Pause and speed control](../mechanic/variable-speed.md) (supporting)
- [Building placement](../mechanic/free-placement.md) (supporting)

## Backlinks (computed)

**precedent for:** [Learned motion for simulated crowds](../opportunity/neural-npc-motion.md)

## Sources

- [Planet Zoo](../source/src-wikipedia-planet-zoo.md)

---
Provenance: created in run `2026-10-24-catalog-ge`; reviewed in `2026-10-24-review-fixes`.
