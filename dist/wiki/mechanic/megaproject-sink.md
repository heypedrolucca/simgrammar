# Megaproject sink

*Mechanic* · `megaproject-sink` · status: **sourced**

A terminal construction absorbs very large quantities of produced goods in staged phases and serves as the long-run goal and output sink of a production game.

| field | value |
|---|---|
| aliases | endgame megastructure, terminal project, space elevator, Dyson sphere |
| family | Progression & goals |
| substrate | Aggregate stocks, Rule system |
| math basis | Optimization, System dynamics / ODEs |
| feedback | Reinforcing (positive) |
| player interface | Observation only, Placement |
| legibility | 4 |
| emergence potential | 2 |
| authoring cost | 3 |
| compute cost | 2 |
| tuning difficulty | 3 |
| ai leverage | 2 |
| maturity | Established |
| core count *(computed)* | 1 |
| earliest game *(computed)* | [Pharaoh](../game/pharaoh.md) |
| earliest year *(computed)* | 1999 |
| prevalence *(computed)* | 6 |
| prevalence share *(computed)* | 0.034 |
| subgenre spread *(computed)* | 2 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

Owns one or more megaprojects, each a sequence of phases with large delivery requirements (item types and quantities, or energy), the deliveries accumulated so far, and the reward for each phase or the whole project (unlocks, power, a victory, or an ending). Delivered goods are consumed, so the project converts factory throughput into progress and gives an open-ended economy both a target and an outlet. Satisfactory's Space Elevator takes five Project Assembly phases, from 50 Smart Plating in phase 1 to Nuclear Pasta, Biochemical Sculptors, AI Expansion Servers, and Ballistic Warp Drives in phase 5, and its phases unlock tiers. Dyson Sphere Program builds its sphere from solar sails fired by EM-Rail Ejectors and frames carried by rockets, and sails expire after 5,400 seconds unless a completed shell absorbs them. shapez 2 operator goal lines grow exponentially in cost per level. Factorio's rocket silo is a similar sink for rocket parts. It differs from milestone-unlocks, which tests thresholds without consuming goods, and from goods-consumption, which feeds a population's recurring needs rather than a one-off structure.

## Player Experience

A monument to throughput. The player reads the bill of materials, works backward through the factory to supply it, and watches a structure fill phase by phase. It turns an endless sandbox into a campaign with a finish line, or in endless versions a scoreboard of scale.

## Design Levers

- number of phases and the quantity curve across them (linear, geometric, exponential)
- which goods are required and how deep in the production chain they sit
- reward per phase (unlocks, power, cosmetics, an ending)
- whether deliveries persist or expire, as Dyson sphere sails do
- whether play continues after completion
- shared versus individual progress in multiplayer

## Failure Modes

- A finale that ends the game abruptly leaves large factories without purpose.
- Requirements that only scale quantity turn the endgame into waiting rather than designing.
- A phase gated on one bottleneck good stalls the whole project.
- A sink too small to matter fails to absorb late-game surplus, so production has no outlet.

## Dynamics

- Players design factories backward from the project's bill of materials, so it organizes the layout.
- Exponential requirements push players to rebuild for throughput rather than add variety, as with shapez 2 operator levels.
- Completed phases unlock technology that raises throughput for the next phase, a reinforcing ramp.

## Open Questions

- Can megaproject requirements adapt to the player's factory so the finale tests its weak points rather than a fixed list?
- Does an endless exponential sink keep factory games engaging longer than a fixed finale, or does it reduce play to scaling?

## Backlinks (computed)

**used by:** [Anno 1800](../game/anno-1800.md), [Dyson Sphere Program](../game/dyson-sphere-program.md), [Factorio](../game/factorio.md), [Pharaoh](../game/pharaoh.md), [Satisfactory](../game/satisfactory.md), [shapez 2](../game/shapez-2.md)

## Claims

- Satisfactory's Space Elevator has five Project Assembly phases that unlock tiers 3-4, 5-6, 7-8, 9, and the ending; phase 1 needs 50 Smart Plating, and phase 5 needs Nuclear Pasta, Biochemical Sculptors, AI Expansion Servers, and Ballistic Warp Drives. *(confidence: medium)* [[78](../source/src-satisfactorywiki-2026-space-elevator.md)]
- Dyson Sphere Program solar sails are fired by EM-Rail Ejectors, last 5,400 seconds by default, and are absorbed permanently by completed shells, while Small Carrier Rockets build frames. *(confidence: medium)* [[79](../source/src-dspwiki-2026-dyson-sphere.md)]
- shapez 2 operator goal lines grow exponentially in cost per level, for example 15,000 shapes at 18% growth. *(confidence: medium)* [[80](../source/src-shapez2wiki-2026-operator-level.md)]

## Sources

- [Space Elevator](../source/src-satisfactorywiki-2026-space-elevator.md)
- [Dyson Sphere](../source/src-dspwiki-2026-dyson-sphere.md)
- [Operator Level](../source/src-shapez2wiki-2026-operator-level.md)

---
Provenance: created in run `2026-10-24-taxonomy-triage-a`.
