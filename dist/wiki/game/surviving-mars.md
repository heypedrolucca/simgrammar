# Surviving Mars

*Game* · `surviving-mars` · status: **sourced**

A Mars colony city builder in which drones build power, water, and oxygen networks before colonists with traits arrive in domes, while research, Earth sponsors, and dust storms, meteors, and cold waves shape survival.

| field | value |
|---|---|
| year | 2018 |
| developer | Haemimont Games |
| platforms | PC, Console |
| subgenre | City builder |
| subgenre secondary | Colony sim |
| sim domain | Urban, Cosmic / space, Planetary / natural |
| player role | Planner / mayor |
| agency model | Zoning / placement, Indirect incentive |
| time model | Real-time with pause |
| sim scale | Settlement |
| fidelity | Stylized |
| perspective | Free 3D camera |
| win structure | Open sandbox |
| failure model | Cascading collapse |
| narrative mode | Hybrid |
| multiplayer | Single-player |
| modding | Scripting |
| production tier | AA |
| agent count order | ~100 |
| emergence | 3 |
| influence | 1 |
| cluster *(computed)* | C01 |
| core count *(computed)* | 4 |
| mechanic count *(computed)* | 13 |

## Summary

A Mars colony city builder in which drones build power, water, and oxygen networks before colonists with traits arrive in domes, while research, Earth sponsors, and dust storms, meteors, and cold waves shape survival.

## Core Loop

land rockets with drones and prefabs -> drones build power, water, and oxygen infrastructure -> build domes and bring colonists from Earth -> colonists' traits, comfort, and sanity drive work and stability -> research and export rare metals for funding -> weather disasters and Mysteries

## Design Notes

Surviving Mars splits construction from population: drones working within range of hubs build and maintain everything, and colonists arrive only after domes have power, water, and oxygen. Colonists carry traits, flaws, and specializations and track morale, comfort, sanity, and health, so dome services decide whether they work, turn Earthsick, or rebel. Mysteries layer authored storylines (plagues, rival corporations, AI revolts, alien contact) on top of disasters such as dust storms, meteors, and cold waves.

## Relations

**uses**

- [Power grid](../mechanic/power-grid.md) (core): Generators and batteries feed cable networks to domes and buildings; a dome without power, water, or oxygen cannot sustain colonists.
- [Fluid pipe networks](../mechanic/fluid-pipe-network.md) (core): Water and oxygen travel by pipe from extractors and producers to domes.
- [Hauling jobs](../mechanic/hauling-jobs.md) (core): Drones within a hub's range carry resources, build, and maintain buildings.
- [Tech tree](../mechanic/tech-tree.md) (core): Research spans physics, engineering, social, biotechnology, and robotics fields.
- [Service coverage](../mechanic/service-coverage.md) (supporting): Drone hubs and dome services serve within a range.
- [Personality traits](../mechanic/personality-traits.md) (supporting): Colonists have traits, flaws, and specializations that suit them to jobs.
- [Needs decay](../mechanic/needs-decay.md) (supporting): Comfort, sanity, health, and morale change with services and events.
- [Mood and breakdowns](../mechanic/mood-breakdown.md) (supporting): Unhappy colonists may become Earthsick or rebels.
- [Random disasters](../mechanic/random-disasters.md) (supporting): Dust storms, meteor storms, cold waves, and dust devils.
- [Wear and breakdown](../mechanic/wear-breakdown.md) (supporting): Buildings need drone maintenance to keep working.
- [Planetary climate](../mechanic/planetary-climate.md) (supporting): Green Planet (2019) adds terraforming of atmosphere, temperature, and water.
- [Triggered event chains](../mechanic/triggered-event-chains.md) (supporting): Mysteries run storylines such as plagues, rival corporations, AI revolts, and alien contact.
- [Resource extraction](../mechanic/resource-extraction.md) (supporting): Metals, rare metals, concrete, and water are extracted; rare metal exports fund imports.

## Backlinks (computed)

**precedent for:** [Branch preview of policy futures](../opportunity/branch-preview-forecasts.md), [Weather-coupled energy grids](../opportunity/weather-coupled-grids.md)

## Sources

- [Surviving Mars](../source/src-wikipedia-surviving-mars.md)

---
Provenance: created in run `2026-10-24-catalog-ga`.
