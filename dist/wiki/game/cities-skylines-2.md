# Cities: Skylines II

*Game* · `cities-skylines-2` · status: **sourced**

The sequel to Cities: Skylines, with citizens choosing routes by time, comfort, and money, a tech tree of development points, preset climates with seasons, and maps of up to 441 tiles.

| field | value |
|---|---|
| year | 2023 |
| developer | Colossal Order (Iceflake Studios from 2026) |
| platforms | PC |
| subgenre | City builder |
| subgenre secondary | Transport / logistics |
| sim domain | Urban, Economic |
| player role | Planner / mayor |
| agency model | Zoning / placement, Policy / parameter |
| time model | Real-time with pause |
| sim scale | City |
| fidelity | Systemic |
| perspective | Free 3D camera |
| win structure | Open sandbox |
| failure model | Soft / recoverable |
| narrative mode | Emergent |
| multiplayer | Single-player |
| modding | Scripting |
| production tier | AA |
| agent count order | 10,000+ |
| emergence | 3 |
| influence | 1 |
| influenced by | [Cities: Skylines](../game/cities-skylines.md) |
| cluster *(computed)* | C09 |
| core count *(computed)* | 3 |
| mechanic count *(computed)* | 18 |

## Summary

The sequel to Cities: Skylines, with citizens choosing routes by time, comfort, and money, a tech tree of development points, preset climates with seasons, and maps of up to 441 tiles.

## Core Loop

zone and draw roads -> citizens choose homes, jobs, and routes by cost, time, and comfort -> taxes and fees fund services -> milestones grant development points and map tiles -> unlock transport and services -> expand

## Design Notes

Route choice is a weighted cost over time, comfort, money, and behavior, so parking fees, transit fares, and lane choice shift where agents go, and the first game's cap of about 65,000 rendered citizens is replaced by a hardware limit. One in-game day and night stands for a month, so daily traffic rhythms and seasonal climate run on different scales. The launch drew criticism for performance and its economy simulation, console versions were delayed indefinitely in 2024, and development moved from Colossal Order to Iceflake Studios after a November 2025 announcement.

## Relations

**influenced by**

- [Cities: Skylines](../game/cities-skylines.md)

**uses**

- [Zoning](../mechanic/zoning.md) (core): Residential, commercial, industrial, and office zones along roads, with signature buildings unlocked at milestones.
- [Traffic congestion](../mechanic/traffic-congestion.md) (core): Vehicles spread across lanes, parking fees enter route cost, and accident checks run per road segment.
- [Agent pathfinding](../mechanic/agent-pathfinding.md) (core): Citizens compare driving, transit, and walking with a cost combining time, comfort, money, and personal preference.
- [Public transit lines](../mechanic/public-transit.md) (supporting)
- [Tech tree](../mechanic/tech-tree.md) (supporting): Development points are spent in a tree to unlock transport options and services.
- [Milestone unlocks](../mechanic/milestone-unlocks.md) (supporting): Milestones grant development points and map tiles, from 9 starting tiles up to 441.
- [Seasons](../mechanic/seasons.md) (supporting): Each map has a preset climate; winters bring snow.
- [Random disasters](../mechanic/random-disasters.md) (supporting): Floods, forest fires, and tornadoes, mitigated by disaster response services.
- [Day-night cycle](../mechanic/day-night-cycle.md) (supporting): Each day and night cycle equals one simulated month.
- [Land value](../mechanic/land-value.md) (supporting): Signature buildings and services change land value in their zone.
- [Taxation](../mechanic/taxation.md) (supporting): Tax rates, fees, and ordinances fund the city.
- [Service coverage](../mechanic/service-coverage.md) (supporting)
- [Modding API](../mechanic/modding-api.md) (supporting): Paradox Mods since 2024-03-25; mods can override game code.
- [Travel mode choice](../mechanic/travel-mode-choice.md) (supporting): Citizens compare driving, transit, and walking using a cost of time, comfort, money, and personal behavior, and parking fees enter the driving cost.
- [Pause and speed control](../mechanic/variable-speed.md) (supporting)
- [Building placement](../mechanic/free-placement.md) (supporting)
- [Power grid](../mechanic/power-grid.md) (supporting): Generation, a connected grid, and batteries; solar output varies with weather and time of day and wind with wind strength.
- [Weather](../mechanic/weather.md) (supporting): Weather and seasons affect solar and wind output and climate conditions.

## Backlinks (computed)

**deploys:** [Neural rendering in the graphics pipeline](../technique/neural-rendering-shaders.md)

**precedent for:** [Why-query over the simulation log](../opportunity/causal-why-query.md), [Learned build assist for cities](../opportunity/learned-build-assist.md), [Mean-field crowds and traffic](../opportunity/mean-field-crowds.md)

## Sources

- [Cities: Skylines II](../source/src-wikipedia-cities-skylines-2.md)
- [Cities: Skylines II Feature Highlight #2: Traffic AI](../source/src-paradox-2023-cs2-traffic-ai.md)
- [Cities: Skylines II features: Electricity and Water](../source/src-paradox-2023-cs2-electricity-water.md)

---
Provenance: created in run `2026-10-24-catalog-ga`; reviewed in `2026-10-24-review-fixes`.
