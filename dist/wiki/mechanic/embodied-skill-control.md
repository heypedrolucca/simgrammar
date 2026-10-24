# Embodied skill control

*Mechanic* · `embodied-skill-control` · status: **asserted**

Real-time motor skill operating a simulated mechanism, such as hand-flying, driving, or surgery, is the main challenge.

| field | value |
|---|---|
| aliases | hands-on control, manual piloting, sim control |
| family | Control & automation |
| substrate | Continuous physics |
| math basis | Control theory, Classical mechanics |
| feedback | None |
| player interface | Embodied skill |
| legibility | 3 |
| emergence potential | 3 |
| authoring cost | 3 |
| compute cost | 2 |
| tuning difficulty | 3 |
| ai leverage | 3 |
| maturity | Classic |
| core count *(computed)* | 6 |
| earliest game *(computed)* | [Elite](../game/elite.md) |
| earliest year *(computed)* | 1984 |
| prevalence *(computed)* | 14 |
| prevalence share *(computed)* | 0.08 |
| subgenre spread *(computed)* | 5 |
| technique count *(computed)* | 4 |
| technique exposure *(computed)* | 1.9 |

## Definition

The player's continuous inputs (stick, wheel, pedals, mouse, motion controllers) drive the control surfaces or actuators of a physically simulated mechanism, and the challenge is the skill of producing good inputs, not choosing goals. State owned: mapping from input devices to actuator commands, including curves, deadzones, and assists. Update rule: each physics step, read inputs, apply response curves and optional assists (stability control, auto-trim, autopilot), and send commands to the mechanism model, such as flight aerodynamics or vehicle dynamics. Skill emerges because the mechanism has inertia, delays, and nonlinearities the player must learn to anticipate. Canonical forms: hand-flying in Microsoft Flight Simulator, X-Plane, and DCS World; driving in iRacing, Gran Turismo, and BeamNG.drive; and deliberately clumsy hand control in Surgeon Simulator.

## Player Experience

Competence lives in the hands. The player practices, crashes, and gradually internalizes how the mechanism responds until difficult maneuvers feel fluid. Mastery is personal and hard-won, and assists let novices participate before they have the skill.

## Design Levers

- fidelity of the underlying mechanism model
- assist layers that can be turned on or off (traction control, stability assist, auto-rudder, autopilot)
- input device support and response curves
- feedback channels: force feedback, motion, sound, and visual cues
- deliberate awkwardness of control mapping for comedy, as in Surgeon Simulator
- consequences of error: reset, damage, or permanent loss

## Failure Modes

- Keyboard or gamepad play of a mechanism tuned for wheels or sticks is nearly impossible, splitting the audience by hardware.
- Missing tactile and vestibular cues make real-world techniques fail on screen.
- Assists that are all or nothing leave no learning ramp between novice and full simulation.

## Dynamics

- Skill becomes a personal progression system independent of unlocks, sustaining long-term play in racing and flight communities.
- Hardware investment (wheels, HOTAS, VR) forms around the mechanic and reinforces community identity.
- Combined with damage models, small control errors cascade into dramatic, unscripted failures.

## Open Questions

- Can learned coaching models watch input traces and teach technique the way an instructor does?
- Can adaptive assists, trained to keep the player near the edge of competence, replace fixed difficulty toggles?

## Relations

**synergy**

- [Vehicle dynamics](../mechanic/vehicle-dynamics.md): Detailed handling models reward motor skill and hardware like wheels and pedals.

**tension**

- [Pause and speed control](../mechanic/variable-speed.md): Real-time motor skill and time compression are hard to offer together.
- [Turn structure](../mechanic/turn-structure.md): Turns remove the real-time pressure motor skill depends on.

## Backlinks (computed)

**affected by:** [Deep reinforcement learning policies for NPC opponents and navigation](../technique/deep-rl-npc-policies.md), [Neural rendering in the graphics pipeline](../technique/neural-rendering-shaders.md), [ML reconstruction of the planet from aerial imagery](../technique/satellite-world-reconstruction.md), [Subspace neural physics and learned deformers](../technique/subspace-neural-physics.md)

**involved in:** [Simulator instructor coaching](../opportunity/sim-instructor-coach.md)

**used by:** [BeamNG.drive](../game/beamng-drive.md), [Besiege](../game/besiege.md), [DCS World](../game/dcs-world.md), [Elite](../game/elite.md), [Elite Dangerous](../game/elite-dangerous.md), [Gran Turismo](../game/gran-turismo.md), [Gran Turismo 7](../game/gran-turismo-7.md), [iRacing](../game/iracing.md), [Kerbal Space Program](../game/kerbal-space-program.md), [Microsoft Flight Simulator (2020)](../game/microsoft-flight-simulator-2020.md), [Microsoft Flight Simulator 2024](../game/microsoft-flight-simulator-2024.md), [SnowRunner](../game/snowrunner.md), [Surgeon Simulator](../game/surgeon-simulator.md), [X-Plane](../game/x-plane.md)

---
Provenance: created in run `2026-10-24-taxonomy-m6`.
