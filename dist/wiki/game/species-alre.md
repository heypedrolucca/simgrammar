# Species: Artificial Life, Real Evolution

*Game* · `species-alre` · status: **sourced**

A solo-developed evolution simulator in which creatures defined by numeric genes mutate, breed, and speciate in real time across a 3D world while the player observes, edits the gene pool, and alters climate.

| field | value |
|---|---|
| aliases | Species ALRE, Species |
| year | 2012 |
| developer | Quasar |
| platforms | PC |
| subgenre | Artificial life |
| subgenre secondary | Ecosystem / evolution |
| sim domain | Biological / ecological |
| player role | Observer / gardener |
| agency model | Supernatural intervention, Policy / parameter, Indirect incentive |
| time model | Real-time with pause |
| sim scale | Region |
| fidelity | Systemic |
| perspective | Free 3D camera |
| win structure | Open sandbox |
| failure model | None |
| narrative mode | Emergent |
| multiplayer | Single-player |
| modding | Content |
| production tier | Indie |
| agent count order | ~100 |
| emergence | 3 |
| influence | 1 |
| cluster *(computed)* | C10 |
| core count *(computed)* | 2 |
| mechanic count *(computed)* | 8 |

## Summary

A solo-developed evolution simulator in which creatures defined by numeric genes mutate, breed, and speciate in real time across a 3D world while the player observes, edits the gene pool, and alters climate.

## Core Loop

creatures feed, pay energy costs, and reproduce -> offspring genomes mutate -> environment and rovers decide who eats and who starves -> trait averages drift and lineages split into species -> player edits genes, climate, or triggers ice ages and floods -> watch the clade diagram branch

## Design Notes

Species, built by a single developer known as Quasar, simulates evolution with no fitness function: genes are numbers, most mutations add a random value in [-1, 1] scaled by a background mutation rate and radiation, and survival is whatever the body and environment allow. Energy costs come from analyzing each creature's skeleton for internal forces and torques, so morphology has a physical price, and creatures can eat only what their head reaches. Species are not predefined: a species is a population that can interbreed within a genetic distance, and it splits only when intermediate forms die out, which the clade diagram records. Species defined at runtime by genetic distance are not yet a mechanic in the taxonomy (proposal runtime-speciation). A free alpha (0.4.0) was public from 2012, and the Steam Early Access build from 2018 has not reached 1.0.

## Relations

**uses**

- [Trait inheritance](../mechanic/trait-inheritance.md) (core): Each creature's body and behavior come from numeric genes; offspring are randomly modified copies of one or more parents, with most mutations a random value in [-1, 1] times a modifier for background mutation rate and radiation.
- [Natural selection](../mechanic/natural-selection.md) (core): No fitness score exists; creatures that cannot pay skeleton-derived energy costs, reach food, or tolerate local climate fail to reproduce, so trait averages drift and lineages speciate.
- [Habitat suitability](../mechanic/habitat-suitability.md) (supporting): Climate varies across the map, and climate control devices create local cold, hot, fertile, or dead ground.
- [God powers](../mechanic/god-powers.md) (supporting): The player triggers ice ages and world floods, programs rovers to feed or kill creatures by genetic distance to a target genome, and edits genomes in an isolated nursery.
- [Lifecycle and aging](../mechanic/lifecycle-aging.md) (supporting)
- [Agent inspection](../mechanic/agent-inspection.md) (supporting): Creature inspection shows each individual's DNA and stats.
- [Stats dashboards](../mechanic/stats-dashboards.md) (supporting): Species averages over time, a clade diagram (Tree of Life), a satellite range map, and a web-of-life view of genetic variety.
- [Pause and speed control](../mechanic/variable-speed.md) (supporting)

## Backlinks (computed)

**precedent for:** [Open-ended evolution sandbox](../opportunity/open-ended-evolution-sandbox.md)

## Claims

- The free Proof of Concept Demo Alpha 0.4.0 was publicly released on 2012-05-27, and the game entered Steam Early Access on 2018-09-28 without a later 1.0 release. *(confidence: high)* [[40](../source/src-quasar-2012-species-alpha-release.md), [41](../source/src-steam-2026-species-alre.md)]
- The developer is credited only by the handle Quasar on Steam and the development blog; no personal name was found in the sources checked. *(confidence: medium)* [[41](../source/src-steam-2026-species-alre.md), [42](../source/src-revolutionarygames-2016-thrive-vs-species.md)]

## Sources

- [Species: Artificial Life, Real Evolution on Steam](../source/src-steam-2026-species-alre.md)
- [ALPHA RELEASE! WHOO!](../source/src-quasar-2012-species-alpha-release.md)
- [Species 0.7.0 Released!](../source/src-quasar-2014-species-0-7-0.md)
- [Devblog #5: Thrive vs Species](../source/src-revolutionarygames-2016-thrive-vs-species.md)

---
Provenance: created in run `2026-10-24-catalog-gd`.
