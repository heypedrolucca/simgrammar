# BeamNG.drive

*Game* · `beamng-drive` · status: **sourced**

A vehicle sim built on soft-body physics in which every vehicle is a node-and-beam skeleton that flexes, deforms, and breaks under impact, played as a free-roam sandbox with scenarios.

| field | value |
|---|---|
| year | 2013 |
| developer | BeamNG GmbH |
| platforms | PC |
| subgenre | Vehicle sim |
| subgenre secondary | Physics sandbox |
| sim domain | Physical / mechanical |
| player role | Operator / pilot |
| agency model | Direct avatar, Policy / parameter |
| time model | Real-time with pause |
| sim scale | Individual |
| fidelity | High-fidelity |
| perspective | Third-person |
| win structure | Open sandbox |
| failure model | None |
| narrative mode | None |
| multiplayer | Single-player |
| modding | Scripting |
| production tier | Indie |
| agent count order | ~10 |
| emergence | 3 |
| influence | 3 |
| cluster *(computed)* | C03 |
| core count *(computed)* | 2 |
| mechanic count *(computed)* | 7 |

## Summary

A vehicle sim built on soft-body physics in which every vehicle is a node-and-beam skeleton that flexes, deforms, and breaks under impact, played as a free-roam sandbox with scenarios.

## Core Loop

pick a vehicle and map -> drive, race, or stage a crash -> node-beam structure deforms and parts fail -> inspect the damage -> reset or change vehicle, conditions, or mods

## Design Notes

Vehicles are defined in JBeam, a JSON format of nodes and beams, and the same structure produces both handling and damage: frames flex, doors detach, windows shatter, tires blow, engines degrade, and fuel tanks can explode. Free roam exposes simulation parameters (time, gravity, wind), so much play is experiment rather than goal. Lua scripting and an official in-game mod repository make the vehicle and scenario set community-driven, and BeamNG.tech forks the engine for education and research.

## Relations

**uses**

- [Soft-body deformation](../mechanic/soft-body-deformation.md) (core): Vehicles are JBeam node-and-beam skeletons that flex and deform under impact; damage degrades engines, detaches doors, shatters windows, blows tires, and can make fuel tanks explode.
- [Vehicle dynamics](../mechanic/vehicle-dynamics.md) (core): Handling comes from the same node-beam structure, so suspension, chassis flex, and tires respond to the vehicle's build and its damage.
- [Embodied skill control](../mechanic/embodied-skill-control.md) (supporting)
- [Scenario objectives](../mechanic/scenario-objectives.md) (supporting): Campaigns group short races, chases, and stunts, and time trials race against the player's best times.
- [Modding API](../mechanic/modding-api.md) (supporting): The game relies heavily on Lua, and mods add real and fictional vehicles.
- [Content sharing](../mechanic/content-sharing.md) (supporting): An official mod repository is browsable from the website and in game, with a manager that keeps mods updated.
- [Pause and speed control](../mechanic/variable-speed.md) (supporting)

## Backlinks (computed)

**precedent for:** [Learned material surrogates at world scale](../opportunity/learned-material-surrogates.md)

## Claims

- A free tech demo and paid alpha launched on 2013-08-03 through FastSpring, before Steam Early Access on 2015-05-29; the source reports no 1.0 release. *(confidence: high)* [[5](../source/src-wikipedia-beamng-drive.md)]

## Sources

- [BeamNG.drive](../source/src-wikipedia-beamng-drive.md)

---
Provenance: created in run `2026-10-24-catalog-gf`; reviewed in `2026-10-24-review-fixes`.
