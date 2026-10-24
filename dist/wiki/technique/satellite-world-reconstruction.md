# ML reconstruction of the planet from aerial imagery

*Technique* · `satellite-world-reconstruction` · status: **sourced**

Machine learning classifies buildings, vegetation, and terrain in satellite and aerial imagery and procedural rules rebuild them as 3D scenery, which Microsoft Flight Simulator streams for the whole Earth.

| field | value |
|---|---|
| aliases | Blackshark.ai, satellite-to-3D, planet-scale scenery generation |
| category | Procedural content generation |
| year | 2020 |
| maturity | Shipped (niche) |
| trl | 8 |
| runtime | Offline authoring |
| determinism impact | Preserves |
| horizon | Now |
| risks | Consistency / hallucination, IP / provenance, Compute cost |
| deployed in | [Microsoft Flight Simulator (2020)](../game/microsoft-flight-simulator-2020.md), [Microsoft Flight Simulator 2024](../game/microsoft-flight-simulator-2024.md) |
| affects count *(computed)* | 3 |

## Summary

Machine learning classifies buildings, vegetation, and terrain in satellite and aerial imagery and procedural rules rebuild them as 3D scenery, which Microsoft Flight Simulator streams for the whole Earth.

## Mechanism

Models trained on labeled imagery detect buildings, trees, and land cover in satellite and aerial imagery and map data and extrapolate approximate geometry; offline procedural generation then builds and dresses the buildings and places vegetation, while selected cities use photogrammetry meshes. The reconstruction runs offline in the cloud, and the result is streamed to players on demand as they fly, with procedural filling where imagery is poor.

## Limitations

- Accuracy is bounded by imagery quality; blurred or pixelated areas fall back to procedural fill.
- Requires cloud streaming of petabyte-scale data and a licensed imagery source.
- Reconstructed buildings are generic from inferred class and height, not modeled individually, except in photogrammetry cities.

## Relations

**affects**

- [Procedural terrain](../mechanic/procedural-terrain.md) (Replaces substrate): The world is reconstructed from real imagery instead of generated from a seed and noise; the player-facing role of an explorable map is unchanged, but its content is the real planet, with procedural filling only where imagery is missing.
- [Embodied skill control](../mechanic/embodied-skill-control.md) (Deepens): Recognizable real buildings and landmarks across the planet make visual navigation by reference to the ground practicable anywhere, extending hand-flying practice beyond hand-modeled airports and cities.
- [Real-world data feeds](../mechanic/real-world-data-feeds.md) (Deepens): Learned classification of satellite imagery turns real-world map data into simulated scenery at planetary scale (Microsoft Flight Simulator).

**deployed in**

- [Microsoft Flight Simulator (2020)](../game/microsoft-flight-simulator-2020.md)
- [Microsoft Flight Simulator 2024](../game/microsoft-flight-simulator-2024.md)

## Claims

- Microsoft Flight Simulator (2020) used Blackshark.ai's AI on Azure to generate 3D buildings, trees, and terrain from Bing Maps data and photogrammetry, covering about 1.5 billion buildings and 2 trillion trees from over two petabytes of streamed map data. *(confidence: medium)* [[222](../source/src-wikipedia-microsoft-flight-simulator-2020.md)]
- Blackshark.ai describes its products as turning satellite and aerial imagery into structured models of terrain, buildings, and infrastructure. *(confidence: high)* [[223](../source/src-blackshark-2026-homepage.md)]
- Microsoft Flight Simulator 2024 carries over the satellite-derived scenery systems of the 2020 game. *(confidence: medium)* [[224](../source/src-wikipedia-microsoft-flight-simulator-2024.md)]

## Sources

- [Microsoft Flight Simulator (2020 video game)](../source/src-wikipedia-microsoft-flight-simulator-2020.md)
- [Blackshark.ai](../source/src-blackshark-2026-homepage.md)
- [Microsoft Flight Simulator 2024](../source/src-wikipedia-microsoft-flight-simulator-2024.md)

---
Provenance: created in run `2026-10-24-techniques-world-models`; reviewed in `2026-10-24-technique-links`.
