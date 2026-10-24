# Neural cellular automata

*Technique* · `neural-cellular-automata` · status: **sourced**

Cellular automata whose local update rule is a small learned network or logic circuit, trained so that cells grow, maintain, and regenerate a target pattern, texture, structure, or level from a seed.

| field | value |
|---|---|
| aliases | NCA, Growing NCA, DiffLogic CA, differentiable logic cellular automata, self-organising textures |
| category | Artificial life research |
| year | 2020 |
| maturity | Research |
| trl | 4 |
| runtime | Client real-time, Offline authoring |
| determinism impact | Mitigable |
| horizon | 3-5 years |
| risks | Controllability, Legibility, Evaluation difficulty |
| deployed in |  |
| affects count *(computed)* | 4 |

## Summary

Cellular automata whose local update rule is a small learned network or logic circuit, trained so that cells grow, maintain, and regenerate a target pattern, texture, structure, or level from a seed.

## Mechanism

Each grid cell holds a state vector (16 channels in Growing NCA: RGB, an alpha channel that marks living cells, and hidden signaling channels). Every step a cell perceives its 3x3 neighborhood through fixed Sobel gradient filters, a shared network of about 8,000 parameters maps the perception vector to a state increment, and a random mask applies the update to roughly half the cells, so no global clock is needed. Cells with no living neighbor are zeroed. The rule is trained by backpropagating through many steps toward a target image or style, with damaged samples in the training pool to teach regeneration. Variants use 3D convolutions for voxel structures, quality-diversity search instead of gradients for game levels, or differentiable logic gates that compile to a discrete binary circuit (DiffLogic CA).

## Limitations

- Each trained rule targets one pattern, texture or structure family; changing the target requires retraining.
- Growth unfolds over many steps, so getting a stable result has a latency that instant procedural methods do not have.
- Learned rules are opaque to designers and players, apart from small logic-gate circuits, which makes failures hard to diagnose.
- Demonstrations are small 2D images, 3D structures of a few thousand blocks, and simple tile domains; robustness under player interference at game scale is not shown.

## Sources

- src-mordvintsev-2020-growing-nca
- src-mordvintsev-2021-nca-textures
- src-sudhakaran-2021-3d-nca-minecraft
- src-earle-2021-nca-level-generation
- src-miotti-2025-difflogic-ca

## Relations

**affects**

- [Falling-sand materials](../mechanic/falling-sand-materials.md) (Replaces substrate): Local per-cell material rules can be learned from examples of desired behavior instead of hand-coded; DiffLogic CA recovered Game of Life exactly as a compact logic circuit cheap enough for per-pixel use.
- [Voxel destruction](../mechanic/voxel-destruction.md) (Enables new form): Regenerating NCA regrow damaged shapes and 3D NCA regrow parts of machines, enabling destructible structures and organisms that heal from local rules rather than respawning.
- [Procedural build assist](../mechanic/procedural-build-assist.md) (Enables new form): A seed block placed by the player can grow into a castle or tree over time under a learned 3D rule, a growth-based alternative to instant procedural detailing.
- [Procedural terrain](../mechanic/procedural-terrain.md) (Replaces substrate): Tile maps and levels can be grown by NCA generators selected by quality-diversity search for solvability and diversity, replacing hand-tuned noise and placement rules.

## Backlinks (computed)

**applied in:** [Learned material surrogates at world scale](../opportunity/learned-material-surrogates.md), [Open-ended evolution sandbox](../opportunity/open-ended-evolution-sandbox.md)

## Claims

- Growing NCA grew an image from one seed cell with a shared update network of about 8,000 parameters; models trained on damaged samples regrew erased regions, including damage types not seen in training. *(confidence: high)* [[231](../source/src-mordvintsev-2020-growing-nca.md)]
- NCA texture models with 5,868 parameters synthesized textures interactively in real time in a WebGL demo. *(confidence: high)* [[232](../source/src-mordvintsev-2021-nca-textures.md)]
- 3D NCA grew Minecraft castles, apartment blocks and trees, some over 3,000 blocks, and regrew parts of simple functional machines. *(confidence: high)* [[233](../source/src-sudhakaran-2021-3d-nca-minecraft.md)]
- Quality-diversity search (CMA-ME) produced diverse NCA level generators for maze, Sokoban and Zelda domains, often meeting solvability criteria, and explored level space better than a CPPN baseline. *(confidence: high)* [[234](../source/src-earle-2021-nca-level-generation.md)]
- DiffLogic CA (2025) learned Conway's Game of Life from all 512 3x3 configurations as a 336-gate binary circuit and grew patterns such as a lizard with 577 gates, with asynchronous and self-healing variants. *(confidence: high)* [[235](../source/src-miotti-2025-difflogic-ca.md)]

## Sources

- [Growing Neural Cellular Automata](../source/src-mordvintsev-2020-growing-nca.md)
- [Texture Generation with Neural Cellular Automata](../source/src-mordvintsev-2021-nca-textures.md)
- [Growing 3D Artefacts and Functional Machines with Neural Cellular Automata](../source/src-sudhakaran-2021-3d-nca-minecraft.md)
- [Illuminating Diverse Neural Cellular Automata for Level Generation](../source/src-earle-2021-nca-level-generation.md)
- [Differentiable Logic Cellular Automata: From Game of Life to Pattern Generation](../source/src-miotti-2025-difflogic-ca.md)

---
Provenance: created in run `2026-10-24-techniques-sim-math`.
