# Hardspace: Shipbreaker

*Game* · `hardspace-shipbreaker` · status: **sourced**

A zero-gravity salvage sim in which the player cuts derelict ships apart with a laser cutter and grapple, manages decompression and volatile systems, and sorts salvage to pay down a large debt.

| field | value |
|---|---|
| year | 2020 |
| year full release | 2022 |
| developer | Blackbird Interactive |
| platforms | PC, Console |
| subgenre | Job sim |
| subgenre secondary | Space sim |
| sim domain | Occupational, Physical / mechanical, Cosmic / space |
| player role | Worker |
| agency model | Direct avatar |
| time model | Real-time |
| sim scale | Individual |
| fidelity | Systemic |
| perspective | First-person |
| win structure | Campaign |
| failure model | Soft / recoverable |
| narrative mode | Authored |
| multiplayer | Single-player |
| modding | None |
| production tier | AA |
| agent count order | None |
| emergence | 3 |
| influence | 1 |
| cluster *(computed)* | C02 |
| core count *(computed)* | 2 |
| mechanic count *(computed)* | 7 |

## Summary

A zero-gravity salvage sim in which the player cuts derelict ships apart with a laser cutter and grapple, manages decompression and volatile systems, and sorts salvage to pay down a large debt.

## Core Loop

start a shift -> scan the ship -> vent pressure and make power, fuel, coolant, and reactor systems safe -> cut parts free -> grapple them to the correct receptacle -> salvage value pays down debt -> buy tool upgrades

## Design Notes

Each ship is a physics assembly of joined parts and typed hazards rather than an authored level: cutting into a pressurized room causes explosive decompression, cutting live electrical wires or coolant pipes can explode, and a reactor removed from its casing must be delivered before it melts down. The order of disassembly is the puzzle, and the taxonomy lacks a mechanic for it (proposed as salvage-deconstruction). Oxygen and thruster fuel act as survival stocks, and shifts are timed except in Open Shift mode.

## Relations

**uses**

- [Rigid-body physics](../mechanic/rigid-body-physics.md) (core): Ships are assemblies of separable parts; freed parts keep mass and momentum in zero gravity and are pulled or flung with the tether grapple toward the right receptacle.
- [Surface work tools](../mechanic/surface-work-tools.md) (core): The laser cutter severs structure at cut points and joints; cutting live electrical wires or coolant pipes can cause an explosion, so where and in what order to cut is the core decision.
- [Procedural checklists](../mechanic/procedural-checklists.md) (supporting): Systems must be made safe in order: pressurized rooms vented, electrical and coolant lines avoided, and reactors delivered before they melt down; mistakes produce the physical result rather than an error.
- [Fluid and gas simulation](../mechanic/fluid-gas-simulation.md) (supporting): Rooms hold atmosphere, and an uncontrolled decompression flushes the player and loose objects out of the ship.
- [Survival meters](../mechanic/survival-meters.md) (supporting): Oxygen and thruster fuel deplete during a shift and must be replenished.
- [Daily action budget](../mechanic/daily-action-budget.md) (supporting): Shifts are timed; Open Shift mode removes the limit.
- [Loans and debt](../mechanic/loans-debt.md) (supporting): The character owes $1.2 billion to Lynx Corporation, and salvage earnings pay it down.

## Sources

- [Hardspace: Shipbreaker](../source/src-wikipedia-hardspace-shipbreaker.md)
- [Hardspace: Shipbreaker on Steam](../source/src-steam-2026-hardspace-shipbreaker.md)

---
Provenance: created in run `2026-10-24-catalog-gf`.
