# Procedural build assist

*Mechanic* · `procedural-build-assist` · status: **sourced**

Coarse player input such as a block or a drawn wall is turned into detailed, organic structures by procedural rules.

| field | value |
|---|---|
| aliases | mixed-initiative building, smart building, auto-detailing |
| family | Space & construction |
| substrate | Rule system, Cellular grid |
| math basis | Procedural noise / generative grammars, Combinatorics |
| feedback | None |
| player interface | Placement, Direct manipulation |
| legibility | 4 |
| emergence potential | 2 |
| authoring cost | 3 |
| compute cost | 2 |
| tuning difficulty | 1 |
| ai leverage | 4 |
| maturity | Emerging |
| core count *(computed)* | 2 |
| earliest game *(computed)* | [Townscaper](../game/townscaper.md) |
| earliest year *(computed)* | 2020 |
| prevalence *(computed)* | 2 |
| prevalence share *(computed)* | 0.011 |
| subgenre spread *(computed)* | 1 |
| technique count *(computed)* | 4 |
| technique exposure *(computed)* | 1.812 |

## Definition

The player supplies coarse intent (add or remove a block, drag a wall or path) and local rules pick the detailed geometry for the affected cells and their neighbors. In Townscaper each click adds or removes a block on an irregular quad grid made by subdividing a hex grid and jittering points; corner modules are chosen with a marching-cubes-style lookup and a real-time wave function collapse that narrows valid modules per cell, then decorations such as windows, chimneys, and bushes are added, and gardens appear only in enclosed areas. Each change ripples through connected cells, so delay grows with structure size, and the solver may fail silently. Tiny Glade (2024) turns drawn walls and paths into detailed castles and gardens. State: a coarse occupancy grid; output: derived geometry, recomputed locally on edit.

## Player Experience

Low effort, high expressiveness. A few clicks yield something that looks hand-made, which feels like collaborating with a builder. There is no failure state, so play is calm, exploratory, and screenshot-driven.

## Design Levers

- input granularity: blocks, strokes, or brushes
- size of the module library and number of variants per configuration
- constraint priorities, such as which modules win when several fit
- determinism: whether the same input always yields the same output
- how much manual override the player gets

## Failure Modes

- After hours of play the module library repeats and outputs start to look the same.
- Players cannot get the exact shape they want because the rules decide the detail.
- Silent solver failures leave odd fragments; Townscaper can leave loose structures where no module fits.
- Recalculation delay grows on large builds.

## Dynamics

- Builds spread through screenshots and social media more than through gameplay goals.
- Rules produce context-sensitive surprises, such as stairs, arches, or gardens appearing where the player did not place them.
- Shipped examples rarely couple the output to a simulation; when they do, agents must interpret generated spaces.

## Open Questions

- Can generative 3D models replace hand-built module libraries while keeping the instant, local response players expect?
- Can build-assist output feed a simulation (rooms, pathing, structural load) without the player losing track of what they built?

## Relations

**tension**

- [Structural integrity](../mechanic/structural-integrity.md): Assisted organic building favors freedom; strict structural rules punish it.

## Backlinks (computed)

**affected by:** [Prompt-to-persistent 3D world generation](../technique/generated-3d-worlds.md), [Neural cellular automata](../technique/neural-cellular-automata.md), [Real-time generative restyling of game video](../technique/real-time-video-restyling.md), [Wave Function Collapse and constraint-based tile generation](../technique/wave-function-collapse.md)

**involved in:** [Learned build assist for cities](../opportunity/learned-build-assist.md), [Symbolic simulation, neural rendering](../opportunity/symbolic-sim-neural-render.md)

**used by:** [Tiny Glade](../game/tiny-glade.md), [Townscaper](../game/townscaper.md)

## Sources

- [How Townscaper Works: A Story Four Games in the Making](../source/src-thompson-2022-how-townscaper-works.md)

---
Provenance: created in run `2026-10-24-taxonomy-m4`.
