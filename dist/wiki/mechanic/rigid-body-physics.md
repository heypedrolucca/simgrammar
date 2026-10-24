# Rigid-body physics

*Mechanic* · `rigid-body-physics` · status: **sourced**

Objects with mass and inertia move under forces and collide, constrained by contacts and joints solved each step.

| field | value |
|---|---|
| aliases | physics engine, rigid-body dynamics |
| family | Physics & materials |
| substrate | Continuous physics |
| math basis | Classical mechanics |
| feedback | None |
| player interface | Direct manipulation, Embodied skill |
| legibility | 4 |
| emergence potential | 4 |
| authoring cost | 2 |
| compute cost | 3 |
| tuning difficulty | 3 |
| ai leverage | 3 |
| maturity | Classic |
| core count *(computed)* | 10 |
| earliest game *(computed)* | [The Incredible Machine](../game/the-incredible-machine.md) |
| earliest year *(computed)* | 1993 |
| prevalence *(computed)* | 13 |
| prevalence share *(computed)* | 0.075 |
| subgenre spread *(computed)* | 7 |
| technique count *(computed)* | 8 |
| technique exposure *(computed)* | 2.788 |

## Definition

Each body holds mass, an inertia tensor, position, orientation, and linear and angular velocity. Each step the engine applies forces and gravity, finds colliding pairs with a broad phase and contact points with a narrow phase, solves contact and joint constraints iteratively (sequential impulses or projected Gauss-Seidel), and integrates positions; resting bodies sleep to save compute. Engines include Havok, used for Half-Life 2's gravity gun puzzles in 2004, PhysX, and Box2D by Erin Catto. Dennis Gustafsson's voxel physics engine after Teardown uses substeps instead of more solver iterations, in the style of temporal Gauss-Seidel, with a parallel solver for large piles. Outputs are motion, contact events, and impact forces that other systems read as damage or sound.

## Player Experience

Tactile and playful. Objects behave as expected, so players stack, throw, and build contraptions, and failures turn into slapstick. Physics puzzles feel solved by understanding rather than by finding the intended key.

## Design Levers

- solver iterations or substeps per frame
- friction and restitution per material
- allowed mass ratios between interacting bodies
- joint types and limits
- sleep thresholds and active simulation range
- determinism requirements for replays and networking

## Failure Modes

- Large mass ratios and stiff joints cause jitter or explosive separation.
- Fast small objects tunnel through thin walls without continuous collision detection.
- Non-deterministic solvers desynchronize multiplayer sessions and replays.
- Players exploit clipping and stacking to launch themselves or bypass level geometry.
- Body count caps scale and causes late slowdowns in sandbox play.

## Dynamics

- Contraptions, chain reactions, and Rube Goldberg machines arise in sandboxes such as Garry's Mod, whose tool gun welds and constrains props.
- Impact forces feed damage, sound, and destruction systems.
- Ragdoll physics turns failure into comedy and shareable clips.

## Open Questions

- Can learned simulators handle thousands of interacting bodies more cheaply than iterative solvers while staying stable?
- Can deterministic GPU solvers make large rigid-body worlds practical in multiplayer?

## Backlinks (computed)

**affected by:** [Diffusion and autoregressive neural game engines](../technique/diffusion-game-engines.md), [Prompt-to-persistent 3D world generation](../technique/generated-3d-worlds.md), [Genie foundation world models](../technique/genie-world-models.md), [Massively parallel GPU simulation](../technique/massively-parallel-simulation.md), [Muse World and Human Action Model (WHAM)](../technique/muse-wham.md), [Open real-time interactive video world models](../technique/open-interactive-video-models.md), [Physical-world foundation models](../technique/physical-world-foundation-models.md), [Learned physics-based character control](../technique/physics-based-character-control.md)

**involved in:** [Learned motion for simulated crowds](../opportunity/neural-npc-motion.md)

**used by:** [Besiege](../game/besiege.md), [Garry's Mod](../game/garrys-mod.md), [Hardspace: Shipbreaker](../game/hardspace-shipbreaker.md), [Job Simulator](../game/job-simulator.md), [Kerbal Space Program](../game/kerbal-space-program.md), [Noita](../game/noita.md), [Poly Bridge](../game/poly-bridge.md), [Second Life](../game/second-life.md), [Space Engineers](../game/space-engineers.md), [Surgeon Simulator](../game/surgeon-simulator.md), [Teardown](../game/teardown.md), [The Incredible Machine](../game/the-incredible-machine.md), [The Legend of Zelda: Breath of the Wild](../game/zelda-breath-of-the-wild.md)

## Sources

- [See What's New In Teardown Creator's Custom Voxel Physics Engine](../source/src-80lv-2025-teardown-voxel-physics.md)
- [Garry's Mod](../source/src-wikipedia-garrys-mod.md)

---
Provenance: created in run `2026-10-24-taxonomy-m4`.
