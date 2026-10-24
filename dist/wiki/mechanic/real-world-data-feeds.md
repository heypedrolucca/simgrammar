# Real-world data feeds

*Mechanic* · `real-world-data-feeds` · status: **sourced**

Simulation state is initialized or driven at runtime by external real-world data such as map imagery, elevation, star catalogs, live weather, or live traffic instead of authored or procedural content.

| field | value |
|---|---|
| aliases | live data, real-world weather, streamed earth, data-driven world |
| family | World generation |
| substrate | Cellular grid, Agent-based |
| math basis | Probability / statistics, Machine learning |
| feedback | None |
| player interface | Observation only, Parameter |
| legibility | 4 |
| emergence potential | 2 |
| authoring cost | 3 |
| compute cost | 3 |
| tuning difficulty | 2 |
| ai leverage | 4 |
| maturity | Established |
| core count *(computed)* | 1 |
| earliest game *(computed)* | [Aurora 4X](../game/aurora-4x.md) |
| earliest year *(computed)* | 2004 |
| prevalence *(computed)* | 4 |
| prevalence share *(computed)* | 0.023 |
| subgenre spread *(computed)* | 3 |
| technique count *(computed)* | 1 |
| technique exposure *(computed)* | 0.562 |

## Summary

Simulation state is initialized or driven at runtime by external real-world data such as map imagery, elevation, star catalogs, live weather, or live traffic instead of authored or procedural content.

## Definition

Owns a mapping from external datasets to simulation state, a refresh schedule, a cache, and fallback rules. At world creation or on a schedule it fetches data (imagery, elevation, building footprints, star catalogs, weather observations, aircraft positions), converts it into terrain tiles, objects, weather fields, or agents, blends it with procedural or authored content where data is missing, and falls back to cached or generated state when offline. Microsoft Flight Simulator (2020) streams Bing Maps imagery updated every 28 days and AI-generated 3D content from more than two petabytes in the cloud, and feeds in Meteoblue live weather and live air traffic. Elite Dangerous blends real astronomical catalog systems into its procedural galaxy, and Aurora 4X can build systems from real star data. Unlike procedural-terrain, which generates from a seed, and weather, which owns weather state and its effects, this mechanic owns the import of outside data into the simulation.

## Player Experience

Recognition. Players fly over their own house, check the sim against the sky outside, or navigate to a star they can see. Live data makes every session a little different and ties the game to the present day, while gaps and errors in the data are noticed and shared as quickly as its successes.

## Design Levers

- which subsystems are fed: terrain, buildings, weather, traffic, catalogs
- refresh rate: one-time import, periodic updates, or live streaming
- blending rules with procedural or authored content where data is missing or poor
- offline fallback and caching
- player choice between live data and preset conditions

## Failure Modes

- Errors in source data appear in the world as artifacts; a widely shared example is a lone skyscraper in Melbourne in Microsoft Flight Simulator (2020), traced to a mistyped building height in OpenStreetMap data.
- Dependence on servers makes the game fragile; Microsoft Flight Simulator 2024 launched with server problems that caused long loads and missing content.
- Licensing or service changes can remove a data feed after release.

## Dynamics

- Real events such as storms enter play, and players fly into them as they happen.
- Communities fix and supplement data with handcrafted add-ons, building an ecosystem around the gaps.
- Players use the sim as a reference for real places, raising expectations of accuracy.

## Open Questions

- Can generative models fill gaps in real-world data, such as inferring 3D buildings from imagery, without introducing visible errors?
- Could learned weather models fed by live observations give small studios accurate global weather at low cost?

## Backlinks (computed)

**affected by:** [ML reconstruction of the planet from aerial imagery](../technique/satellite-world-reconstruction.md)

**used by:** [Aurora 4X](../game/aurora-4x.md), [Elite Dangerous](../game/elite-dangerous.md), [Microsoft Flight Simulator (2020)](../game/microsoft-flight-simulator-2020.md), [Microsoft Flight Simulator 2024](../game/microsoft-flight-simulator-2024.md)

## Sources

- [Microsoft Flight Simulator (2020 video game)](../source/src-wikipedia-microsoft-flight-simulator-2020.md)
- [Microsoft Flight Simulator 2024](../source/src-wikipedia-microsoft-flight-simulator-2024.md)
- [Elite Dangerous](../source/src-wikipedia-elite-dangerous.md)

---
Provenance: created in run `2026-10-24-taxonomy-triage-b`.
