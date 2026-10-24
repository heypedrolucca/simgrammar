# Projectile ballistics

*Mechanic* · `projectile-ballistics` · status: **sourced**

Shots are simulated as projectiles in flight with velocity, gravity, drag, and penetration, so range, angle, and lead decide hits rather than an instant trace or a dice roll.

| field | value |
|---|---|
| aliases | external ballistics, bullet drop, penetration modeling, torpedo and shell flight |
| family | Physics & materials |
| substrate | Continuous physics |
| math basis | Classical mechanics, Probability / statistics |
| feedback | None |
| player interface | Embodied skill, Parameter |
| legibility | 3 |
| emergence potential | 3 |
| authoring cost | 3 |
| compute cost | 2 |
| tuning difficulty | 3 |
| ai leverage | 2 |
| maturity | Classic |
| core count *(computed)* | 1 |
| earliest game *(computed)* | [Silent Hunter III](../game/silent-hunter-3.md) |
| earliest year *(computed)* | 2005 |
| prevalence *(computed)* | 4 |
| prevalence share *(computed)* | 0.023 |
| subgenre spread *(computed)* | 3 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Summary

Shots are simulated as projectiles in flight with velocity, gravity, drag, and penetration, so range, angle, and lead decide hits rather than an instant trace or a dice roll.

## Definition

Owns, per fired projectile, position, velocity, and type data (mass, drag or ballistic coefficient, guidance if any, and penetration or warhead parameters). Each physics step integrates gravity, drag, and wind (or propulsion and guidance for torpedoes and missiles), tests for intersection with targets or terrain, and on impact resolves penetration against the struck material's thickness and angle, then passes damage to the target. Arma 3 weapons are affected by external ballistics and recoil, so shooters must account for drop and travel time at range; Silent Hunter III torpedoes run at a set speed, depth, and gyro angle toward a computed intercept; DCS World flies missiles, bombs, and gun rounds as projectiles; Command: Modern Operations lists ballistics among its modeled effects. Unlike rigid-body-physics, the projectile is a point mass or simple body integrated at high speed with no contact solver; unlike military-operations, this mechanic owns only the shot's flight and impact, not detection or doctrine.

## Player Experience

Hitting a target is a skill or a calculation rather than a cursor placement. The player estimates range, holds over for drop, leads a moving target, or computes a torpedo solution, and a long-range hit feels earned. Misses teach the model; cover that stops some rounds and not others teaches materials.

## Design Levers

- which forces are integrated: gravity only, drag, wind, Coriolis, or guidance
- penetration model: none, thickness and angle tables, or material-based energy loss
- projectile speed relative to engagement ranges, which sets how much lead and drop matter
- dispersion and weapon accuracy versus player aim
- aids that show the solution, such as ranging reticles or automatic firing solutions

## Failure Modes

- Ballistics fidelity beyond what players can perceive costs compute and data without changing decisions.
- Fast projectiles tunnel through thin geometry at low step rates and register no hit.
- Penetration tables that disagree with visible armor make hits and non-hits feel arbitrary.
- Networked games must reconcile projectile flight across clients, and disagreements show as hits that did not happen.

## Dynamics

- Engagement ranges spread out as skilled players exploit long-range accuracy, changing how teams move across terrain.
- Cover becomes material-dependent, so the environment's construction feeds tactics.
- Aids such as rangefinders and fire-control computers become valuable equipment, coupling ballistics to loadouts and procedures.

## Open Questions

- Can learned surrogate models of penetration and fragmentation replace hand-built tables while staying consistent with what players see?
- Which aids keep long-range ballistics learnable for new players without removing the skill?

## Backlinks (computed)

**used by:** [Arma 3](../game/arma-3.md), [Command: Modern Operations](../game/command-modern-operations.md), [DCS World](../game/dcs-world.md), [Silent Hunter III](../game/silent-hunter-3.md)

## Sources

- [Arma 3](../source/src-wikipedia-arma-3.md)
- [Silent Hunter III](../source/src-wikipedia-silent-hunter-3.md)
- [Command: Modern Operations on Steam](../source/src-steam-2019-command-modern-operations.md)

---
Provenance: created in run `2026-10-24-taxonomy-triage-b`.
