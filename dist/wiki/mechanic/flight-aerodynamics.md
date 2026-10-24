# Flight aerodynamics

*Mechanic* · `flight-aerodynamics` · status: **sourced**

Lift, drag, thrust, and control-surface forces computed from airspeed and attitude govern aircraft motion.

| field | value |
|---|---|
| aliases | flight model, flight dynamics |
| family | Physics & materials |
| substrate | Continuous physics |
| math basis | Classical mechanics, Continuum mechanics, Control theory |
| feedback | Balancing (negative) |
| player interface | Embodied skill, Parameter |
| legibility | 3 |
| emergence potential | 2 |
| authoring cost | 3 |
| compute cost | 2 |
| tuning difficulty | 3 |
| ai leverage | 3 |
| maturity | Classic |
| core count *(computed)* | 4 |
| earliest game *(computed)* | [X-Plane](../game/x-plane.md) |
| earliest year *(computed)* | 1995 |
| prevalence *(computed)* | 5 |
| prevalence share *(computed)* | 0.029 |
| subgenre spread *(computed)* | 2 |
| technique count *(computed)* | 1 |
| technique exposure *(computed)* | 0.188 |

## Definition

The aircraft state holds position, attitude, linear and angular velocity, control-surface deflections, and engine state. Each physics step computes aerodynamic forces from airspeed, angle of attack, sideslip, and air density, adds thrust and gravity, and integrates six-degree-of-freedom rigid-body motion. Two families exist. Coefficient-table models look up lift, drag, and moment coefficients per flight condition. Blade element models, as in X-Plane, divide wings, control surfaces, and propellers into small elements, compute forces on each from aircraft geometry rather than relying only on performance tables, and sum them, so stalls, spins, and ground effect arise from the geometry. Arcade games use simplified models that keep the aircraft stable. Outputs are aircraft motion and instrument readings.

## Player Experience

Hands-on control with real consequences. Players learn energy management, trim, stall warnings, and landings, and skill grows visibly over hours. Arcade variants keep the feeling of speed without the workload.

## Design Levers

- model fidelity: arcade, coefficient tables, or blade elements
- assists such as auto-trim, stability augmentation, and stall protection
- stall and spin behavior near the edge of the envelope
- weather and turbulence coupling
- control response curves and input filtering

## Failure Modes

- Over-stable models feel on rails and remove the skill.
- Without assists, high fidelity makes flight unflyable for new players.
- Table-driven models misbehave in regimes outside their data, such as spins or ground handling.
- Each new aircraft needs costly per-model tuning before it feels right.

## Dynamics

- Weather and terrain create emergent challenges such as crosswind landings and mountain wave turbulence.
- System failures interact with aerodynamics to produce scenarios no one scripted.
- Energy management becomes the core tactical resource in air combat.

## Open Questions

- Can learned surrogates trained on computational fluid dynamics give accurate flight models for aircraft without hand tuning?
- Can an AI instructor read the flight model state and coach novices through stalls and landings?

## Relations

**synergy**

- [Procedural checklists](../mechanic/procedural-checklists.md): A faithful flight model makes real procedures necessary rather than ceremonial.

## Backlinks (computed)

**affected by:** [Graph network simulators and neural operators](../technique/graph-network-simulators.md)

**involved in:** [Simulator instructor coaching](../opportunity/sim-instructor-coach.md)

**used by:** [DCS World](../game/dcs-world.md), [Kerbal Space Program](../game/kerbal-space-program.md), [Microsoft Flight Simulator (2020)](../game/microsoft-flight-simulator-2020.md), [Microsoft Flight Simulator 2024](../game/microsoft-flight-simulator-2024.md), [X-Plane](../game/x-plane.md)

## Sources

- [X-Plane (simulator)](../source/src-wikipedia-x-plane.md)

---
Provenance: created in run `2026-10-24-taxonomy-m4`.
