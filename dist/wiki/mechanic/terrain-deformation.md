# Terrain deformation

*Mechanic* · `terrain-deformation` · status: **sourced**

Wheels, feet, and impacts displace soft ground such as mud and snow, and the persistent ruts change traction for later passes.

| field | value |
|---|---|
| aliases | mud physics, deformable terrain, ruts |
| family | Physics & materials |
| substrate | Cellular grid, Continuous physics |
| math basis | Continuum mechanics |
| feedback | Reinforcing (positive) |
| player interface | Embodied skill |
| legibility | 4 |
| emergence potential | 3 |
| authoring cost | 2 |
| compute cost | 3 |
| tuning difficulty | 3 |
| ai leverage | 2 |
| maturity | Established |
| open questions | Can learned granular-material models make mud, sand, and snow respond more physically at game frame rates? |
| core count *(computed)* | 1 |
| earliest game *(computed)* | [SnowRunner](../game/snowrunner.md) |
| earliest year *(computed)* | 2020 |
| prevalence *(computed)* | 2 |
| prevalence share *(computed)* | 0.011 |
| subgenre spread *(computed)* | 2 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

Ground is a height field with a soft-material layer. Contacts displace material by pressure, wheel slip, and softness; the displaced height persists and changes contact and traction on later passes. In Spintires: MudRunner, according to its lead developer Pavel Zagrebelny, terrain is a regular vertex grid displaced by a height map and covered by a mud layer that artists paint, with a second higher-resolution grid for the mud; when a wheel is in mud or spins too fast, the game computes forces approximating mud physics, and mud displacement runs entirely on the GPU. SnowRunner (2020) extends the approach to snow. Many games deform terrain cosmetically, leaving tracks that do not affect physics.

## Player Experience

Struggle and patience. Players read the ground, pick lines, rock the vehicle, and winch out. Every crossing feels earned, and the track left behind tells the story of the trip.

## Design Levers

- material softness and depth by terrain type
- rut depth, persistence, and recovery over time
- coupling strength between ruts and traction
- simulation resolution and whether it runs on the GPU
- how deformation is synchronized in multiplayer

## Failure Modes

- Cosmetic deformation that does not affect handling creates a mismatch between what players see and feel.
- Permanent deep ruts can make a route impassable for the rest of a session.
- Deformation state is large and hard to keep synchronized across networked players.

## Dynamics

- Spinning wheels dig deeper and lose traction, a stuck spiral that rewards slow throttle and winching.
- Earlier vehicles' ruts change the route for convoy members that follow.
- Weather that softens ground couples terrain deformation to route planning.

## Open Questions

- Can learned granular-material models make mud, sand, and snow respond more physically at game frame rates?

## Relations

**synergy**

- [Vehicle dynamics](../mechanic/vehicle-dynamics.md): Ruts and mud change traction, making route reading a skill (SnowRunner).

## Backlinks (computed)

**used by:** [Farming Simulator 25](../game/farming-simulator-25.md), [SnowRunner](../game/snowrunner.md)

## Sources

- [MudRunner: Porting a Successful Title to Console](../source/src-80lv-2019-mudrunner-console-port.md)

---
Provenance: created in run `2026-10-24-taxonomy-m4`.
