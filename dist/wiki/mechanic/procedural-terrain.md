# Procedural terrain

*Mechanic* · `procedural-terrain` · status: **sourced**

Maps are generated from a seed through noise, erosion, climate, and placement rules.

| field | value |
|---|---|
| aliases | map generation, worldgen terrain, heightmap generation |
| family | World generation |
| substrate | Cellular grid, Stochastic events |
| math basis | Procedural noise / generative grammars, Cellular automata |
| feedback | None |
| player interface | Parameter, Observation only |
| legibility | 4 |
| emergence potential | 3 |
| authoring cost | 2 |
| compute cost | 3 |
| tuning difficulty | 3 |
| ai leverage | 4 |
| maturity | Classic |
| core count *(computed)* | 5 |
| earliest game *(computed)* | [Elite](../game/elite.md) |
| earliest year *(computed)* | 1984 |
| prevalence *(computed)* | 20 |
| prevalence share *(computed)* | 0.115 |
| subgenre spread *(computed)* | 11 |
| technique count *(computed)* | 10 |
| technique exposure *(computed)* | 4.188 |

## Definition

A seeded pipeline builds layered fields over a grid or chunks: elevation from fractal noise or midpoint displacement, then derived temperature, rainfall, drainage, and biome classification, then rivers, ores, vegetation, and points of interest placed by rules. Perlin gradient noise (1985) is the basis of most heightmaps; Minecraft samples noise per chunk on demand for an effectively endless world. Dwarf Fortress starts from a randomized fractal elevation map, adds temperature, rainfall, drainage, vegetation, and salinity layers, traces rivers by erosion from mountains to oceans, and models rain shadows. Inputs: seed, size, and parameters such as sea level or mineral frequency. Outputs: terrain, biome, and resource maps used by construction, pathfinding, and ecology systems.

## Player Experience

Each start is new ground to read: players scout for flat land near water, ore, and defensible chokepoints, and share seeds with unusual landforms. Exploration means something because no guide has mapped this world.

## Design Levers

- noise type, octaves, frequency, and amplitude
- erosion and hydrology passes
- climate model for temperature, rainfall, and biome thresholds
- resource and point-of-interest placement rules and guaranteed fairness constraints
- world size and whether generation is finite or chunked on demand
- player-exposed parameters and seed sharing

## Failure Modes

- Pure noise produces terrain with no recognizable structure that players stop finding interesting after a few runs.
- Unconstrained placement yields unfair or unplayable starts, such as no water or no ore near the spawn point.
- Version updates that change the generator break seed sharing and older saves at chunk borders.

## Dynamics

- Terrain shapes where settlements, roads, and defenses go, so map features drive later strategy.
- Communities trade seeds and rank them, turning generation into shared content.
- Resource scarcity set at generation time determines the pace of mid-game economies.

## Open Questions

- Can generative models trained on real elevation data or player-favored maps produce terrain with more recognizable structure than noise?
- How should learned generators keep fairness constraints, such as guaranteed resources near spawn, that rule-based pipelines enforce directly?

## Backlinks (computed)

**affected by:** [Diffusion and autoregressive neural game engines](../technique/diffusion-game-engines.md), [Prompt-to-persistent 3D world generation](../technique/generated-3d-worlds.md), [Genie foundation world models](../technique/genie-world-models.md), [Learned level and map generation (PCGRL, MarioGPT, LLM generators)](../technique/learned-level-generation.md), [Neural cellular automata](../technique/neural-cellular-automata.md), [Open-ended co-generation of environments and agents](../technique/open-ended-environment-generation.md), [Open real-time interactive video world models](../technique/open-interactive-video-models.md), [Quality-diversity search (MAP-Elites) for content and balance](../technique/quality-diversity-search.md), [ML reconstruction of the planet from aerial imagery](../technique/satellite-world-reconstruction.md), [Wave Function Collapse and constraint-based tile generation](../technique/wave-function-collapse.md)

**involved in:** [Quality-diversity scenario libraries](../opportunity/qd-scenario-libraries.md)

**used by:** [Against the Storm](../game/against-the-storm.md), [Aurora 4X](../game/aurora-4x.md), [Caves of Qud](../game/caves-of-qud.md), [Sid Meier's Civilization](../game/civilization.md), [Don't Starve](../game/dont-starve.md), [Dyson Sphere Program](../game/dyson-sphere-program.md), [Elite](../game/elite.md), [Elite Dangerous](../game/elite-dangerous.md), [Factorio](../game/factorio.md), [FTL: Faster Than Light](../game/ftl.md), [Islanders](../game/islanders.md), [Kingdoms and Castles](../game/kingdoms-and-castles.md), [Minecraft](../game/minecraft.md), [Noita](../game/noita.md), [Offworld Trading Company](../game/offworld-trading-company.md), [Oxygen Not Included](../game/oxygen-not-included.md), [Space Haven](../game/space-haven.md), [Spore](../game/spore.md), [Stellaris](../game/stellaris.md), [Valheim](../game/valheim.md)

## Sources

- [An Image Synthesizer](../source/src-perlin-1985-image-synthesizer.md)
- [Simulation Principles from Dwarf Fortress](../source/src-adams-2015-df-simulation-principles.md)
- [Dwarf Fortress](../source/src-wikipedia-dwarf-fortress.md)

---
Provenance: created in run `2026-10-24-taxonomy-m7`.
