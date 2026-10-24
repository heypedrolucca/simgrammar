# Jurassic World Evolution

*Game* · `jurassic-world-evolution` · status: **sourced**

A dinosaur park management game in which the player excavates fossils for DNA, breeds and modifies dinosaurs, and keeps them contained through storms, sabotage, and breakouts while balancing three division contracts.

| field | value |
|---|---|
| year | 2018 |
| developer | Frontier Developments |
| platforms | PC, Console, Handheld |
| subgenre | Management / tycoon |
| sim domain | Biological / ecological, Economic |
| player role | Manager / owner |
| agency model | Zoning / placement, Direct unit control, Direct avatar |
| time model | Real-time with pause |
| sim scale | Facility |
| fidelity | Stylized |
| perspective | Free 3D camera |
| win structure | Campaign |
| failure model | Soft / recoverable |
| narrative mode | Hybrid |
| multiplayer | Single-player |
| modding | None |
| production tier | AA |
| agent count order | ~100 |
| emergence | 3 |
| influence | 2 |
| cluster *(computed)* | C08 |
| core count *(computed)* | 4 |
| mechanic count *(computed)* | 12 |

## Summary

A dinosaur park management game in which the player excavates fossils for DNA, breeds and modifies dinosaurs, and keeps them contained through storms, sabotage, and breakouts while balancing three division contracts.

## Core Loop

send expeditions for fossils -> sequence DNA and modify genomes -> incubate dinosaurs -> meet feeding and social needs in enclosures -> guests spend while divisions offer contracts -> contain storms and breakouts -> raise the star rating to unlock islands

## Design Notes

Jurassic World Evolution turns a park sim into a containment problem. Each species has feeding, social, and territory needs; unmet needs lower comfort, and low-comfort dinosaurs fight, break fences, and escape to attack guests. Three divisions (Science, Security, Entertainment) offer contracts and track reputation, and letting one fall triggers sabotage such as a power shutdown or disease outbreak, which turns faction standing into a source of hazards. Genome modification changes a species' stats, aggression, and appearance, and the player can drive ranger and ACU vehicles to sedate, medicate, transport, and repair. Dinosaurs do not breed in this game; adding modern-species DNA to a genome trades stats against aggression, a rule the taxonomy lacks (proposed as genome-modification).

## Relations

**uses**

- [Needs decay](../mechanic/needs-decay.md) (core): Dinosaurs have feeding and social needs plus grassland, forest, and population limits; unmet needs lower comfort, and carnivores hunt herbivores and attack fences and guests.
- [Reputation](../mechanic/reputation.md) (core): Science, Security, and Entertainment divisions track reputation; low standing in one triggers sabotage such as power cuts or disease outbreaks.
- [Contracts and orders](../mechanic/contracts-orders.md) (core): Each division offers contracts with requirements and rewards that unlock research and story missions.
- [Random disasters](../mechanic/random-disasters.md) (core): Storms damage fences and power and set dinosaurs loose; breakouts must be contained before guests are hurt.
- [Power grid](../mechanic/power-grid.md) (supporting): Facilities need power from plants through substations; outages open electric fences.
- [Crowd preferences](../mechanic/crowd-preferences.md) (supporting): Guests want viewing of varied species plus shopping, food, and amenities, and flee or die during breakouts.
- [Tech tree](../mechanic/tech-tree.md) (supporting): Fossil DNA completion unlocks species, and the research center unlocks buildings, upgrades, and genome modifications.
- [Resource extraction](../mechanic/resource-extraction.md) (supporting): The Expedition Center sends teams to global dig sites that yield fossils for DNA and for sale.
- [Direct avatar control](../mechanic/direct-avatar.md) (supporting): The player can drive ranger jeeps and ACU helicopters to resupply feeders, repair fences, and tranquilize dinosaurs.
- [Contagion](../mechanic/contagion.md) (supporting): Diseases spread among dinosaurs and must be treated by rangers or ACU.
- [Building placement](../mechanic/free-placement.md) (supporting)
- [Milestone unlocks](../mechanic/milestone-unlocks.md) (supporting): Island star ratings unlock the next island in the Las Cinco Muertes archipelago.

## Sources

- [Jurassic World Evolution](../source/src-wikipedia-jurassic-world-evolution.md)

---
Provenance: created in run `2026-10-24-catalog-ge`.
