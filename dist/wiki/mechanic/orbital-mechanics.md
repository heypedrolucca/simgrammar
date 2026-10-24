# Orbital mechanics

*Mechanic* · `orbital-mechanics` · status: **sourced**

Bodies move under gravity, and maneuvers spend delta-v to change orbits, intercepts, and transfers.

| field | value |
|---|---|
| aliases | orbital dynamics, astrodynamics, patched conics |
| family | Physics & materials |
| substrate | Continuous physics |
| math basis | Classical mechanics, Optimization |
| feedback | None |
| player interface | Parameter, Embodied skill |
| legibility | 3 |
| emergence potential | 2 |
| authoring cost | 1 |
| compute cost | 2 |
| tuning difficulty | 2 |
| ai leverage | 2 |
| maturity | Established |
| open questions | Can an AI mission planner that explains its burns flatten the learning cliff without removing the planning itself? |
| core count *(computed)* | 2 |
| earliest game *(computed)* | [Universe Sandbox](../game/universe-sandbox.md) |
| earliest year *(computed)* | 2008 |
| prevalence *(computed)* | 2 |
| prevalence share *(computed)* | 0.011 |
| subgenre spread *(computed)* | 2 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

Each body holds a position and velocity under gravity. Under the patched conic approximation, used by Kerbal Space Program, each celestial body has a sphere of influence; inside it only that body's gravity is modeled, so the trajectory is an analytic conic propagated on rails, and segments are joined at sphere boundaries by matching position and velocity. This turns the n-body problem into a chain of two-body problems and cannot represent Lagrange points. Full n-body integration, as in Universe Sandbox or the Principia mod for Kerbal Space Program, integrates every body's gravity numerically. Engine burns change velocity, the rocket equation sets the delta-v budget, and maneuver planners preview the orbit that a planned burn will produce.

## Player Experience

A counterintuitive system that becomes mastery. Players learn that speeding up raises the far side of the orbit, plan burns on maneuver nodes, and earn rendezvous and landings through precise planning.

## Design Levers

- patched conics or n-body integration
- scale of the system; Kerbal Space Program uses a planet with a 600 km radius
- time warp limits and whether thrust is allowed during warp
- maneuver planning tools and how much they automate
- atmospheric drag and its coupling to orbits

## Failure Modes

- Many players never get past the learning cliff without external tutorials.
- Patched conics cannot model Lagrange points or halo orbits, which surprises experienced players.
- Floating-point precision at solar-system distances causes jitter unless the engine re-centers the origin.

## Dynamics

- Transfer windows create timing pressure and missions that run in parallel.
- Delta-v couples orbital planning to vehicle design, so mission ambition shapes the rocket.
- Gravity assists and aerobraking reward players who learn the system deeply.

## Open Questions

- Can an AI mission planner that explains its burns flatten the learning cliff without removing the planning itself?

## Backlinks (computed)

**used by:** [Kerbal Space Program](../game/kerbal-space-program.md), [Universe Sandbox](../game/universe-sandbox.md)

## Sources

- [Patched conic approximation](../source/src-wikipedia-patched-conic-approximation.md)
- [Kerbal Space Program](../source/src-wikipedia-kerbal-space-program.md)
- [Universe Sandbox](../source/src-wikipedia-universe-sandbox.md)

---
Provenance: created in run `2026-10-24-taxonomy-m4`.
