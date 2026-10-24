# Subsystem damage

*Mechanic* · `subsystem-damage` · status: **asserted**

A vehicle or ship is a set of named components with their own integrity, and damage to one removes its capacity, such as power, thrust, shields, or sensors, until it is repaired.

| field | value |
|---|---|
| aliases | component damage, system damage, module damage, damage control |
| family | Risk & failure |
| substrate | Aggregate stocks, Rule system, Stochastic events |
| math basis | System dynamics / ODEs, Markov / stochastic processes |
| feedback | Reinforcing (positive) |
| player interface | Orders, Observation only |
| legibility | 4 |
| emergence potential | 4 |
| authoring cost | 2 |
| compute cost | 1 |
| tuning difficulty | 3 |
| ai leverage | 2 |
| maturity | Established |
| core count *(computed)* | 1 |
| earliest game *(computed)* | [DCS World](../game/dcs-world.md) |
| earliest year *(computed)* | 2008 |
| prevalence *(computed)* | 5 |
| prevalence share *(computed)* | 0.029 |
| subgenre spread *(computed)* | 3 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Summary

A vehicle or ship is a set of named components with their own integrity, and damage to one removes its capacity, such as power, thrust, shields, or sensors, until it is repaired.

## Definition

Owns, per vehicle, a list of components (reactor, engines, shields, weapons, sensors, oxygen, hydraulics, individual blocks or parts), each with integrity, a capacity that depends on integrity, and a repair state. Incoming damage is routed to a component by hit location, a targeting choice, or a random draw; the component's capacity falls in steps or to zero, and the vehicle's derived abilities update at once. Repair restores integrity over time, through crew or damage-control teams, or at a dock. FTL ships are rooms holding systems whose power bars are disabled by hits until crew repair them, and players aim weapons at specific enemy systems. Elite Dangerous tracks integrity per module; Space Engineers functional blocks stop working when damaged below a threshold; Kerbal Space Program parts are destroyed by impact or overheating. Unlike wear-breakdown, damage comes from events rather than use and age; unlike injury-body-model, components are machines with capacities, not organisms with wounds and healing.

## Player Experience

Damage is specific and tactical. Losing shields, engines, or oxygen each forces a different response, so the player triages repairs, reroutes power, and targets the enemy's weapons or shields first. A fight can turn on one lucky hit to a key system, and limping home with half a ship working is a story in itself.

## Design Levers

- component granularity: a few named systems, dozens of modules, or every block or part
- damage routing: hit location, player-targeted subsystems, or random allocation
- capacity curve: binary loss, stepped loss, or proportional degradation
- repair model: crew time, consumable parts, damage-control assignments, or docking only
- cascades such as fires, breaches, or power loss that spread damage to other components

## Failure Modes

- Random allocation of critical hits ends fights on a single roll, which reads as unfair.
- Fine granularity without clear status displays leaves players unsure which component failed.
- Repair that is too fast or free removes the decision; repair that requires a dock makes one hit end a mission.

## Dynamics

- Targeting the opponent's key system first becomes a standard opening, such as disabling weapons or shields.
- Damage to one component cascades into others: a lost reactor removes power, a lost oxygen system suffocates crew.
- Repair crews and damage control become a resource that competes with combat roles.

## Open Questions

- Can AI opponents choose subsystem targets based on a model of the player's ship and plan rather than fixed priorities?
- What granularity of components keeps damage readable during real-time combat?

## Backlinks (computed)

**used by:** [DCS World](../game/dcs-world.md), [Elite Dangerous](../game/elite-dangerous.md), [FTL: Faster Than Light](../game/ftl.md), [Kerbal Space Program](../game/kerbal-space-program.md), [Space Engineers](../game/space-engineers.md)

---
Provenance: created in run `2026-10-24-taxonomy-triage-b`; reviewed in `2026-10-24-review-fixes`.
