# Diagnose and repair

*Mechanic* · `diagnose-repair` · status: **sourced**

The player inspects a machine, finds faulty parts with tools and tests, disassembles in order to reach them, and repairs or replaces them.

| field | value |
|---|---|
| aliases | mechanic job, troubleshooting, fault finding |
| family | Operation & procedure |
| substrate | Rule system |
| math basis | Information theory, Graph search |
| feedback | None |
| player interface | Direct manipulation |
| legibility | 4 |
| emergence potential | 2 |
| authoring cost | 4 |
| compute cost | 1 |
| tuning difficulty | 2 |
| ai leverage | 3 |
| maturity | Established |
| core count *(computed)* | 2 |
| earliest game *(computed)* | [PC Building Simulator](../game/pc-building-simulator.md) |
| earliest year *(computed)* | 2018 |
| prevalence *(computed)* | 2 |
| prevalence share *(computed)* | 0.011 |
| subgenre spread *(computed)* | 1 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

A machine is a tree of parts with a removal-order dependency graph, each part carrying a condition or fault state. A job arrives with symptoms; the player uses tests and tools to reveal hidden part states, removes covering parts in valid order, replaces or repairs faulty ones, reassembles, and verifies with a final test. In Car Mechanic Simulator 2018 and its 2021 sequel the player examines engine, suspension, and chassis, removes parts in a realistic order to reach a damaged component, buys a replacement or repairs it at higher levels, and uses a test track to find brake and suspension problems. PC Building Simulator applies the same loop to computers. Unlike diagnosis-treatment, the target is a machine whose state is fully deterministic once revealed. Inputs: fault state, symptoms, tools. Outputs: repaired machine, payment, and experience.

## Player Experience

Methodical, calm problem-solving with a clear finish. Players narrow down causes from symptoms, enjoy the order of unbolting and rebolting parts, and see a fixed machine run again. Learning the real structure of an engine or PC is part of the appeal.

## Design Levers

- how symptoms map to faults, and how many faults hide behind one symptom
- tool set and what each test reveals
- disassembly depth and how many parts block access
- repair versus replace economics
- job time limits and payment for partial fixes

## Failure Modes

- When the game highlights faulty parts directly, diagnosis disappears and only the removal chore remains.
- Deep disassembly for a single part becomes tedious once the novelty fades.
- Faults that do not follow from symptoms make diagnosis guesswork.

## Dynamics

- Players build mental models of real machine structure and speed up dramatically with experience.
- Tool unlocks reshape the diagnosis strategy, since better tests skip disassembly.
- Coupled with economy and workshop progression, choosing which jobs to accept becomes a planning layer.

## Open Questions

- Can fault states generated from a causal model of the machine, rather than authored per job, produce varied but solvable diagnoses?
- Could a language-model customer describing symptoms in their own words make diagnosis a real inference task?

## Relations

**synergy**

- [Wear and breakdown](../mechanic/wear-breakdown.md): Breakdowns create the repair work; repair makes wear a skill problem rather than a tax.

## Backlinks (computed)

**involved in:** [Simulator instructor coaching](../opportunity/sim-instructor-coach.md)

**used by:** [Car Mechanic Simulator 2021](../game/car-mechanic-simulator-2021.md), [PC Building Simulator](../game/pc-building-simulator.md)

## Sources

- [Car Mechanic Simulator 2018](../source/src-wikipedia-car-mechanic-simulator-2018.md)

---
Provenance: created in run `2026-10-24-taxonomy-m7`.
