# Power allocation

*Mechanic* · `power-allocation` · status: **asserted**

The player splits a fixed power budget among a vehicle's subsystems in real time, trading shields, weapons, engines, and life support against each other.

| field | value |
|---|---|
| aliases | power distribution, energy management, power pips, reactor allocation |
| family | Resources & production |
| substrate | Aggregate stocks, Rule system |
| math basis | Optimization |
| feedback | Balancing (negative) |
| player interface | Parameter |
| legibility | 4 |
| emergence potential | 3 |
| authoring cost | 1 |
| compute cost | 1 |
| tuning difficulty | 3 |
| ai leverage | 2 |
| maturity | Established |
| core count *(computed)* | 1 |
| earliest game *(computed)* | [FTL: Faster Than Light](../game/ftl.md) |
| earliest year *(computed)* | 2012 |
| prevalence *(computed)* | 2 |
| prevalence share *(computed)* | 0.011 |
| subgenre spread *(computed)* | 1 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

Owns a total budget B (reactor bars, distributor pips) and an allocated level a_i for each subsystem, with sum(a_i) <= B and each a_i capped by the subsystem's installed level. Each subsystem's output is a step or linear function of its allocation: shield layers, weapon charge rate, evasion, oxygen production. The player moves units between subsystems at any time, often while paused, and the effect applies at once or through a charge rate. FTL's reactor supplies bars that the player assigns to shields, engines, weapons, oxygen, and the medbay; each shield layer takes two bars, and the reactor and each system are upgraded separately with scrap. Elite Dangerous splits distributor pips among systems, engines, and weapons capacitors, which sets each capacitor's recharge rate, while a separate priority list decides which modules shut down when the power plant is overloaded. Unlike power-grid, there is no network topology and no automatic shortfall rule: the split itself is the decision. Inputs: budget, subsystem caps, damage to the reactor or subsystems. Outputs: per-subsystem effectiveness.

## Player Experience

A running triage under pressure. The player pulls power from oxygen to charge one more weapon, moves it all into engines to escape, or holds shields high while waiting for a volley. Each reallocation is a small bet about what the opponent will do next, and a damaged reactor turns a comfortable budget into a painful choice.

## Design Levers

- total budget relative to the sum of subsystem caps, which sets how often the player must choose
- cost per subsystem level and step thresholds such as two units per shield layer
- reallocation speed: instant, only while paused, or through capacitor recharge rates
- how damage reduces the budget or a subsystem's cap, and how repair restores it
- which subsystems draw from the budget and which run without it
- upgrade path for the budget versus the subsystems

## Failure Modes

- A budget large enough to max every subsystem removes the decision; one too small leaves a single viable split.
- A dominant split, such as maximum shields at all times, turns allocation into a one-time setup step.
- Real-time reallocation without pause rewards input speed over judgment in games that are otherwise tactical.
- Hidden thresholds, such as a shield layer needing two units, make partial allocations look like wasted power.

## Dynamics

- Opponents target the reactor or a key subsystem to force bad splits, coupling allocation to subsystem damage.
- Players shift power in phases of a fight (shields early, weapons once enemy shields drop, engines to escape), giving combat a rhythm.
- Upgrade choices become a question of which subsystems the budget can actually feed at once.

## Open Questions

- Could an AI crew officer that proposes splits from the tactical situation keep allocation a decision rather than a reflex?
- What ratio of budget to total subsystem cap keeps allocation meaningful across a whole campaign of upgrades?

## Backlinks (computed)

**used by:** [Elite Dangerous](../game/elite-dangerous.md), [FTL: Faster Than Light](../game/ftl.md)

---
Provenance: created in run `2026-10-24-taxonomy-triage-b`; reviewed in `2026-10-24-review-fixes`.
