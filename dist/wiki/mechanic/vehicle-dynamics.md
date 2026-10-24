# Vehicle dynamics

*Mechanic* · `vehicle-dynamics` · status: **sourced**

Tire, suspension, drivetrain, and weight-transfer models compute vehicle handling from forces at each wheel.

| field | value |
|---|---|
| aliases | handling model, car physics, tire model |
| family | Physics & materials |
| substrate | Continuous physics |
| math basis | Classical mechanics, Control theory |
| feedback | Balancing (negative) |
| player interface | Embodied skill, Parameter |
| legibility | 3 |
| emergence potential | 2 |
| authoring cost | 3 |
| compute cost | 2 |
| tuning difficulty | 3 |
| ai leverage | 2 |
| maturity | Classic |
| open questions | Can tire models learned from real telemetry replace hand-fitted coefficients for each car? |
| core count *(computed)* | 7 |
| earliest game *(computed)* | [Gran Turismo](../game/gran-turismo.md) |
| earliest year *(computed)* | 1997 |
| prevalence *(computed)* | 9 |
| prevalence share *(computed)* | 0.052 |
| subgenre spread *(computed)* | 4 |
| technique count *(computed)* | 4 |
| technique exposure *(computed)* | 1.413 |

## Definition

The vehicle state holds the chassis rigid body, wheel angular speeds, suspension compression, engine speed, gear, and often tire temperature and wear. Each physics step routes engine torque through the drivetrain, computes each tire's longitudinal and lateral force from slip ratio, slip angle, and vertical load, applies suspension forces that transfer weight under braking, acceleration, and cornering, and integrates. A common tire model is Hans Pacejka's semi-empirical Magic Formula, which fits force against slip as y = D sin(C arctan(Bx - E(Bx - arctan Bx))). Simulators such as iRacing and Gran Turismo use detailed tire and suspension models; arcade racers simplify grip into tunable curves. Assists such as ABS and traction control act on the same quantities.

## Player Experience

Feel and control. Players sense grip through the screen or wheel, learn to balance the car at the limit, and tinker with setups. Mastery is slow and physical, and small improvements feel large.

## Design Levers

- tire model fidelity: simple grip curve to full Magic Formula
- driving assists and their strength
- physics step rate relative to frame rate
- setup parameters exposed to the player
- surface grip by material and weather
- force feedback and camera cues that communicate grip

## Failure Modes

- Grip that falls off too sharply produces snap oversteer that feels unfair.
- Tire models become unstable at very low speeds, causing jitter at standstill.
- Too little detail feels like ice skating; too much excludes players without wheels.
- Physics tied to frame rate makes handling change with performance.

## Dynamics

- Setup choices create a tuning meta per track and car.
- Tire wear and temperature create race strategy over a stint.
- Changing weather and surfaces force mid-race adaptation.

## Open Questions

- Can tire models learned from real telemetry replace hand-fitted coefficients for each car?

## Backlinks (computed)

**affected by:** [Deep reinforcement learning policies for NPC opponents and navigation](../technique/deep-rl-npc-policies.md), [Differentiable simulation](../technique/differentiable-simulation.md), [Open real-time interactive video world models](../technique/open-interactive-video-models.md), [Physical-world foundation models](../technique/physical-world-foundation-models.md)

**involved in:** [Simulator instructor coaching](../opportunity/sim-instructor-coach.md)

**used by:** [BeamNG.drive](../game/beamng-drive.md), [Car Mechanic Simulator 2021](../game/car-mechanic-simulator-2021.md), [Euro Truck Simulator 2](../game/euro-truck-simulator-2.md), [Farming Simulator 25](../game/farming-simulator-25.md), [Gran Turismo](../game/gran-turismo.md), [Gran Turismo 7](../game/gran-turismo-7.md), [iRacing](../game/iracing.md), [Project Zomboid](../game/project-zomboid.md), [SnowRunner](../game/snowrunner.md)

## Sources

- [Tire and Vehicle Dynamics (3rd edition)](../source/src-pacejka-2012-tire-and-vehicle-dynamics.md)

---
Provenance: created in run `2026-10-24-taxonomy-m4`.
