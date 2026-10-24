# SimLife

*Game* · `simlife` · status: **sourced**

A Maxis artificial-life toy in which the player edits plant and animal genes, landscape, and the world's physical parameters, then watches food chains and evolution play out.

| field | value |
|---|---|
| aliases | SimLife: The Genetic Playground |
| year | 1992 |
| developer | Maxis |
| platforms | PC |
| subgenre | Artificial life |
| subgenre secondary | Ecosystem / evolution |
| sim domain | Biological / ecological |
| player role | Observer / gardener |
| agency model | Design then test, Policy / parameter, Supernatural intervention |
| time model | Real-time with pause |
| sim scale | Region |
| fidelity | Stylized |
| perspective | Top-down / side 2D |
| win structure | Open sandbox |
| failure model | Soft / recoverable |
| narrative mode | Emergent |
| multiplayer | Single-player |
| modding | None |
| production tier | AA |
| agent count order | ~100 |
| emergence | 3 |
| influence | 2 |
| cluster *(computed)* | C10 |
| core count *(computed)* | 3 |
| mechanic count *(computed)* | 8 |

## Summary

A Maxis artificial-life toy in which the player edits plant and animal genes, landscape, and the world's physical parameters, then watches food chains and evolution play out.

## Core Loop

design species genes and world physics -> plants grow and animals eat, breed, and mutate -> populations boom, crash, or go extinct -> read graphs -> edit genes or environment and run again

## Design Notes

Designed by Ken Karakotsios, SimLife moves the player's control point down to the genome: plant and animal species are edited gene by gene, and the world's physical parameters can be changed, so the toy is about running ecological and evolutionary experiments rather than pursuing goals. Where SimEarth aggregates taxa into planetary stocks, SimLife works at the scale of a landscape and its individual species, mixing exclusive designed animals such as the Killer Penguin and Monkeyphant with player-made ones. Direct gene editing matches the genome-modification proposal from run catalog-ge.

## Relations

**uses**

- [Trait inheritance](../mechanic/trait-inheritance.md) (core): The player edits the genetics of plant and animal species directly, and offspring inherit those genes with variation.
- [Natural selection](../mechanic/natural-selection.md) (core): Evolution is simulated and can be steered; species whose genes fit the designed environment persist while others decline.
- [Food web](../mechanic/food-web.md) (core): Designed ecosystems pair plant species with the animals that eat them, so gene edits ripple through who can feed on whom.
- [Habitat suitability](../mechanic/habitat-suitability.md) (supporting)
- [Terraforming](../mechanic/terraforming.md) (supporting): Players create and modify worlds and environments as well as species.
- [Lifecycle and aging](../mechanic/lifecycle-aging.md) (supporting)
- [Stats dashboards](../mechanic/stats-dashboards.md) (supporting)
- [Pause and speed control](../mechanic/variable-speed.md) (supporting)

## Backlinks (computed)

**precedent for:** [Open-ended evolution sandbox](../opportunity/open-ended-evolution-sandbox.md)

## Sources

- [SimLife](../source/src-wikipedia-simlife.md)

---
Provenance: created in run `2026-10-24-catalog-gd`.
