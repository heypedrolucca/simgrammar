# Learned motion for simulated crowds

*Opportunity* · `neural-npc-motion` · status: **asserted**

Physics-based learned character controllers let simulated agents move and react physically, so crowds, injuries, and labor look like what the simulation says is happening.

| field | value |
|---|---|
| opportunity type | Mechanic upgrade |
| involves | [Injury body model](../mechanic/injury-body-model.md), [Crowd preferences](../mechanic/crowd-preferences.md), [Hauling jobs](../mechanic/hauling-jobs.md), [Agent inspection](../mechanic/agent-inspection.md), [Rigid-body physics](../mechanic/rigid-body-physics.md) |
| applies | [Learned physics-based character control](../technique/physics-based-character-control.md), [Massively parallel GPU simulation](../technique/massively-parallel-simulation.md) |
| precedent | [RimWorld](../game/rimworld.md), [Dwarf Fortress](../game/dwarf-fortress.md), [Planet Zoo](../game/planet-zoo.md), [The Sims 4](../game/the-sims-4.md) |
| novelty | 3 |
| feasibility | 3 |
| impact | 2 |
| horizon | 1-2 years |
| key risks | Runtime cost at crowd scale., Uncanny motion worse than stylized animation., Physics instability in edge cases. |
| falsifiable signal | {'prediction': 'A management or colony sim will ship learned physics-based motion for its simulated population.', 'resolve_by': '2029-06-30', 'criteria': 'Developer documentation naming learned motion control in a shipped simulation game.'} |
| priority *(computed)* | 2.5 |

## Summary

Physics-based learned character controllers let simulated agents move and react physically, so crowds, injuries, and labor look like what the simulation says is happening.

## Thesis

Simulation games describe rich internal states (injured, exhausted, carrying heavy loads) but show them with a handful of canned animations, which undermines legibility and attachment. Learned physics-based controllers can produce motion conditioned on state at scale, so an agent with a leg wound limps believably and a tired hauler slows and stumbles.

## Design Sketch

Agent animation is driven by a learned controller conditioned on body-model state, load, and mood. The inspector shows the same state the motion expresses. Crowds use cheaper approximations at distance.

## Key Risks

- Runtime cost at crowd scale.
- Uncanny motion worse than stylized animation.
- Physics instability in edge cases.

## Validation Experiment

Drive 200 agents with a learned controller conditioned on three state variables; measure frame cost and whether observers can identify agent state from motion alone. Success: 80 percent identification at under 2 ms per frame.

## Falsifiable signal

- **Prediction:** A management or colony sim will ship learned physics-based motion for its simulated population.
- **Resolve by:** 2029-06-30
- **Criteria:** Developer documentation naming learned motion control in a shipped simulation game.

## Relations

**applies**

- [Learned physics-based character control](../technique/physics-based-character-control.md)
- [Massively parallel GPU simulation](../technique/massively-parallel-simulation.md)

**involves**

- [Injury body model](../mechanic/injury-body-model.md)
- [Crowd preferences](../mechanic/crowd-preferences.md)
- [Hauling jobs](../mechanic/hauling-jobs.md)
- [Agent inspection](../mechanic/agent-inspection.md)
- [Rigid-body physics](../mechanic/rigid-body-physics.md)

**precedent**

- [RimWorld](../game/rimworld.md)
- [Dwarf Fortress](../game/dwarf-fortress.md)
- [Planet Zoo](../game/planet-zoo.md)
- [The Sims 4](../game/the-sims-4.md)

---
Provenance: created in run `2026-10-24-synthesis`.
