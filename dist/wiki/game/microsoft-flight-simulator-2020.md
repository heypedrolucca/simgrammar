# Microsoft Flight Simulator (2020)

*Game* · `microsoft-flight-simulator-2020` · status: **sourced**

A flight sim that streams a photorealistic model of the whole Earth built from map and photogrammetry data and flies aircraft through live weather with a surface-level aerodynamic model.

| field | value |
|---|---|
| aliases | MSFS 2020, Microsoft Flight Simulator |
| year | 2020 |
| developer | Asobo Studio |
| platforms | PC, Console, VR |
| subgenre | Flight sim |
| sim domain | Physical / mechanical, Planetary / natural |
| player role | Operator / pilot |
| agency model | Direct avatar |
| time model | Real-time with pause |
| sim scale | Individual |
| fidelity | High-fidelity |
| perspective | First-person |
| win structure | Open sandbox |
| failure model | Hard restart |
| narrative mode | None |
| multiplayer | Single-player, Co-op |
| modding | Scripting |
| production tier | AAA |
| agent count order | ~100 |
| emergence | 2 |
| influence | 3 |
| cluster *(computed)* | C03 |
| core count *(computed)* | 3 |
| mechanic count *(computed)* | 9 |

## Summary

A flight sim that streams a photorealistic model of the whole Earth built from map and photogrammetry data and flies aircraft through live weather with a surface-level aerodynamic model.

## Core Loop

pick aircraft, airport, and time -> preflight and start up -> take off into live or set weather -> navigate and hand-fly or use autopilot -> approach and land -> pick the next flight

## Design Notes

The world is data rather than authored terrain: Bing Maps imagery refreshed every 28 days, Blackshark.ai photogrammetry, and Azure AI 3D generation streamed from more than two petabytes, with Meteoblue weather and real air traffic fed in live. The flight model simulates over 1,000 control surfaces and wind over terrain, and a legacy model is kept as an option. No mechanic in the taxonomy covers simulation state driven by real-world data feeds (proposed as real-world-data-feeds).

## Relations

**uses**

- [Flight aerodynamics](../mechanic/flight-aerodynamics.md) (core): The physics engine computes forces over more than 1,000 control surfaces and models wind flowing over terrain; a legacy flight model option remains.
- [Weather](../mechanic/weather.md) (core): Meteoblue live global weather sets clouds, wind, and precipitation in real time, and wind interacts with the terrain model.
- [Embodied skill control](../mechanic/embodied-skill-control.md) (supporting)
- [Procedural checklists](../mechanic/procedural-checklists.md) (supporting)
- [Day-night cycle](../mechanic/day-night-cycle.md) (supporting)
- [Scenario objectives](../mechanic/scenario-objectives.md) (supporting)
- [Modding API](../mechanic/modding-api.md) (supporting): An in-game marketplace and third-party aircraft and airports extend the sim.
- [Real-world data feeds](../mechanic/real-world-data-feeds.md) (core): The whole Earth is built from Bing Maps imagery updated every 28 days and AI-generated 3D content streamed from more than two petabytes in the cloud, while Meteoblue live weather and live air traffic feed the sim at runtime.
- [Pause and speed control](../mechanic/variable-speed.md) (supporting)

## Backlinks (computed)

**deploys:** [Neural rendering in the graphics pipeline](../technique/neural-rendering-shaders.md), [ML reconstruction of the planet from aerial imagery](../technique/satellite-world-reconstruction.md)

**influenced:** [Microsoft Flight Simulator 2024](../game/microsoft-flight-simulator-2024.md)

**precedent for:** [Learned regional weather](../opportunity/learned-weather-layer.md)

## Sources

- [Microsoft Flight Simulator (2020 video game)](../source/src-wikipedia-microsoft-flight-simulator-2020.md)

---
Provenance: created in run `2026-10-24-catalog-gf`; reviewed in `2026-10-24-review-fixes`.
