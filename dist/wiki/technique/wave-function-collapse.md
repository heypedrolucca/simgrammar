# Wave Function Collapse and constraint-based tile generation

*Technique* · `wave-function-collapse` · status: **sourced**

An example-driven constraint solver that fills a grid by repeatedly collapsing the lowest-entropy cell to one tile and propagating adjacency constraints, shipped in games including Townscaper, Bad North, and Caves of Qud.

| field | value |
|---|---|
| aliases | WFC, WaveFunctionCollapse, model synthesis |
| category | Procedural content generation |
| year | 2016 |
| maturity | Shipped (niche) |
| trl | 8 |
| runtime | Client real-time, Offline authoring, Design assist |
| determinism impact | Preserves |
| horizon | Now |
| risks | Controllability, Latency |
| deployed in | [Townscaper](../game/townscaper.md), [Caves of Qud](../game/caves-of-qud.md) |
| affects count *(computed)* | 3 |

## Summary

An example-driven constraint solver that fills a grid by repeatedly collapsing the lowest-entropy cell to one tile and propagating adjacency constraints, shipped in games including Townscaper, Bad North, and Caves of Qud.

## Mechanism

Each output cell starts with a domain of all tiles (simple tiled model) or of all N x N patterns extracted from one example image (overlapping model, typically N = 3). The solver repeatedly picks the undecided cell with the lowest Shannon entropy over its remaining options, a minimum-remaining-values heuristic, collapses it to one option sampled by that option's frequency in the example, and propagates: neighbors drop options that no longer have a compatible partner, which is arc consistency as in AC-3. If a domain empties, the attempt fails and the original algorithm restarts; later implementations add backtracking or local repair. Designers steer output with tile sets, adjacency rules, weights, pre-set cells, and extra global constraints. Townscaper runs it in real time on an irregular quad grid: the player toggles a cell's occupancy and the solver chooses compatible building modules from the surrounding shape, with decoration applied in a separate pass.

## Limitations

- Only local adjacency is enforced; reachability, room counts, or path lengths need extra constraints, and Karth and Smith found a global constraint caused hundreds of conflicts that restarts could not clear within a minute.
- Contradictions are possible because the underlying problem is NP-hard; shipped systems restart (Bad North) or accept silent local failures (Townscaper).
- Interactive generation delay grows with structure size, and the overlapping model is slower and can copy the example too closely.
- Quality depends on an authored module set, often hundreds of tiles (Bad North uses over 300), so art cost moves into modules rather than disappearing.

## Sources

- src-gumin-2016-wavefunctioncollapse
- src-karth-2017-wfc-constraint-solving
- src-thompson-2022-how-townscaper-works
- src-steam-2024-caves-of-qud
- src-boristhebrave-2020-wfc-explained

## Relations

**affects**

- [Procedural build assist](../mechanic/procedural-build-assist.md) (Deepens): Rough player input becomes consistent detailed structure through constraint propagation over hundreds of modules: in Townscaper a click toggles one cell and the solver re-chooses compatible modules around it, so each placement reshapes its neighbors.
- [Procedural terrain](../mechanic/procedural-terrain.md) (Deepens): Tile maps can be generated from a small example or adjacency table instead of noise thresholds, giving locally coherent coastlines, cliffs, and interiors, as in Bad North's islands and Caves of Qud's areas; large-scale structure still needs another layer.
- [Zoning](../mechanic/zoning.md) (Cuts authoring cost): Buildings on painted zones could be assembled from modular tile sets constrained by neighbors and lot shape rather than authored per lot, varying silhouettes without new art for every building.

**deployed in**

- [Townscaper](../game/townscaper.md)
- [Caves of Qud](../game/caves-of-qud.md)

## Backlinks (computed)

**applied in:** [Learned build assist for cities](../opportunity/learned-build-assist.md)

## Claims

- Maxim Gumin released WaveFunctionCollapse publicly on 2016-09-30 with overlapping and simple tiled models, and developers began experimenting with it within a day. *(confidence: high)* [[13](../source/src-gumin-2016-wavefunctioncollapse.md), [319](../source/src-karth-2017-wfc-constraint-solving.md)]
- The WFC repository lists Bad North, Caves of Qud, Dead Static Drive, Townscaper, and Matrix Awakens as users, with adaptations for Unity, Unreal Engine 5, Godot 4, and Houdini. *(confidence: high)* [[13](../source/src-gumin-2016-wavefunctioncollapse.md)]
- Karth and Smith (FDG 2017) showed WFC is constraint solving with MRV ordering, frequency-weighted value choice, arc-consistency propagation, and global restarts; with an added global constraint restarts failed to finish within a minute while a backtracking solver resolved it quickly. *(confidence: high)* [[319](../source/src-karth-2017-wfc-constraint-solving.md)]
- Townscaper runs WFC in real time on an irregular quad grid to choose building tiles from the surrounding shape and may fail silently where cells cannot fit, whereas Bad North restarts generation; Bad North uses over 300 tiles. *(confidence: high)* [[320](../source/src-thompson-2022-how-townscaper-works.md)]
- Caves of Qud, an early user of WFC alongside multipass generation, reached 1.0 on 2024-12-05 after early access began in 2015. *(confidence: high)* [[319](../source/src-karth-2017-wfc-constraint-solving.md), [12](../source/src-steam-2024-caves-of-qud.md)]
- WFC constrains only nearby tiles, so it rarely produces large-scale structure without added constraints or other techniques. *(confidence: medium)* [[321](../source/src-boristhebrave-2020-wfc-explained.md)]

## Sources

- [WaveFunctionCollapse](../source/src-gumin-2016-wavefunctioncollapse.md)
- [WaveFunctionCollapse is Constraint Solving in the Wild](../source/src-karth-2017-wfc-constraint-solving.md)
- [How Townscaper Works: A Story Four Games in the Making](../source/src-thompson-2022-how-townscaper-works.md)
- [Caves of Qud](../source/src-steam-2024-caves-of-qud.md)
- [Wave Function Collapse Explained](../source/src-boristhebrave-2020-wfc-explained.md)

---
Provenance: created in run `2026-10-24-techniques-rl-design`.
