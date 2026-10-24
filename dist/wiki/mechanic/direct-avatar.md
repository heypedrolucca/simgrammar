# Direct avatar control

*Mechanic* · `direct-avatar` · status: **asserted**

The player directly controls one embodied character's movement and actions in the simulated world.

| field | value |
|---|---|
| aliases | avatar control, third-person control, first-person control |
| family | Control & automation |
| substrate | Continuous physics, Agent-based |
| math basis | Classical mechanics, Control theory |
| feedback | None |
| player interface | Embodied skill, Direct manipulation |
| legibility | 5 |
| emergence potential | 2 |
| authoring cost | 4 |
| compute cost | 2 |
| tuning difficulty | 2 |
| ai leverage | 3 |
| maturity | Classic |
| core count *(computed)* | 8 |
| earliest game *(computed)* | [M.U.L.E.](../game/mule.md) |
| earliest year *(computed)* | 1983 |
| prevalence *(computed)* | 31 |
| prevalence share *(computed)* | 0.178 |
| subgenre spread *(computed)* | 17 |
| technique count *(computed)* | 6 |
| technique exposure *(computed)* | 2.75 |

## Definition

The player maps controller or keyboard input to one character's locomotion (walk, run, jump, swim, fly) and interactions (pick up, use, attack, build) in real time. State owned: the avatar's position, velocity, facing, stance, and interaction target. Update rule: each frame, read input, apply a movement controller (kinematic or physics-based) subject to collision and terrain, and resolve interaction requests against objects in range. The world simulation runs around the avatar, often with only the area near it simulated in detail. It contrasts with overseer control, where the player commands at a distance. Canonical forms: Minecraft, Stardew Valley, The Long Dark, Subnautica, Valheim, and the farmer in Harvest Moon; hybrid games such as Satisfactory and Factorio put a factory builder in an avatar.

## Player Experience

The player is in the world rather than above it. Scale, distance, and danger are felt in the body: a long walk to a resource, a fall, darkness. Systems are learned by touching them, and attachment shifts from managed agents to one's own character.

## Design Levers

- movement speed, traversal options, and fast travel, which set how large the world feels
- interaction reach and whether actions take time or animate
- physics-based versus kinematic controller
- whether the avatar has needs or survival meters
- camera: first person, third person, or top-down
- how much of the world simulates outside the avatar's vicinity

## Failure Modes

- Large worlds with slow movement turn logistics into walking chores until fast travel or automation unlocks.
- Simulation limited to the avatar's surroundings freezes distant systems, breaking the illusion that the world runs without the player.
- Avatar control competes with overseer tools in hybrid games, forcing awkward building from a character's viewpoint.

## Dynamics

- The avatar's travel time becomes the hidden limiting resource, pushing players to build transport and automation.
- Embodied presence makes environmental systems such as weather, temperature, and day-night directly threatening.
- Avatar location sets what is simulated, so player movement shapes world state in games that simulate only loaded chunks.

## Open Questions

- Can learned motion models (physics-based character controllers trained by RL) give avatars natural interaction with arbitrary simulated objects without per-object animation?
- In generative world models where the world is rendered from the avatar's action stream, what simulation persistence can survive outside the view?

## Backlinks (computed)

**affected by:** [Diffusion and autoregressive neural game engines](../technique/diffusion-game-engines.md), [Genie foundation world models](../technique/genie-world-models.md), [Learned kinematic motion synthesis](../technique/learned-motion-synthesis.md), [Muse World and Human Action Model (WHAM)](../technique/muse-wham.md), [Open real-time interactive video world models](../technique/open-interactive-video-models.md), [Learned physics-based character control](../technique/physics-based-character-control.md)

**used by:** [Animal Crossing: New Horizons](../game/animal-crossing-new-horizons.md), [Arma 3](../game/arma-3.md), [Autonauts](../game/autonauts.md), [Big Ambitions](../game/big-ambitions.md), [Car Mechanic Simulator 2021](../game/car-mechanic-simulator-2021.md), [Contraband Police](../game/contraband-police.md), [Don't Starve](../game/dont-starve.md), [Dyson Sphere Program](../game/dyson-sphere-program.md), [Façade](../game/facade.md), [Factorio](../game/factorio.md), [Garry's Mod](../game/garrys-mod.md), [House Flipper](../game/house-flipper.md), [inZOI](../game/inzoi.md), [Job Simulator](../game/job-simulator.md), [Jurassic World Evolution](../game/jurassic-world-evolution.md), [Microsoft Flight Simulator 2024](../game/microsoft-flight-simulator-2024.md), [M.U.L.E.](../game/mule.md), [Noita](../game/noita.md), [PowerWash Simulator](../game/powerwash-simulator.md), [Satisfactory](../game/satisfactory.md), [Schedule I](../game/schedule-i.md), [Second Life](../game/second-life.md), [SimAnt](../game/simant.md), [Spore](../game/spore.md), [Subnautica](../game/subnautica.md), [Suck Up!](../game/suck-up.md), [The Long Dark](../game/the-long-dark.md), [Ultima Online](../game/ultima-online.md), [Valheim](../game/valheim.md), [Where Winds Meet](../game/where-winds-meet.md), [The Legend of Zelda: Breath of the Wild](../game/zelda-breath-of-the-wild.md)

---
Provenance: created in run `2026-10-24-taxonomy-m6`.
