# Prison Architect

*Game* · `prison-architect` · status: **sourced**

A prison management sim in which the player builds a facility, sets an hourly regime, and staffs it while hundreds of prisoners pursue needs whose neglect leads to fights, escapes, and riots.

| field | value |
|---|---|
| year | 2012 |
| year full release | 2015 |
| developer | Introversion Software |
| platforms | PC, Console, Mobile, Handheld |
| subgenre | Management / tycoon |
| subgenre secondary | Colony sim |
| sim domain | Social / interpersonal, Economic |
| player role | Manager / owner |
| agency model | Zoning / placement, Policy / parameter, Indirect incentive, Direct unit control |
| time model | Real-time with pause |
| sim scale | Facility |
| fidelity | Systemic |
| perspective | Top-down / side 2D |
| win structure | Open sandbox |
| failure model | Soft / recoverable |
| narrative mode | Emergent |
| multiplayer | Single-player, Async / shared content |
| modding | Scripting |
| production tier | Indie |
| agent count order | ~100 |
| emergence | 3 |
| influence | 3 |
| influenced by | [Theme Hospital](../game/theme-hospital.md), [Dwarf Fortress](../game/dwarf-fortress.md) |
| cluster *(computed)* | C01 |
| core count *(computed)* | 5 |
| mechanic count *(computed)* | 17 |

## Summary

A prison management sim in which the player builds a facility, sets an hourly regime, and staffs it while hundreds of prisoners pursue needs whose neglect leads to fights, escapes, and riots.

## Core Loop

build cells, canteens, and yards -> set the hourly regime -> prisoners pursue needs within the schedule -> unmet needs raise misconduct, contraband, and riots -> hire staff, run programs, and claim grants -> expand capacity for more prisoners and income

## Design Notes

Control is indirect: the player cannot order prisoners, only shape the regime, the buildings that satisfy each need, and the staff who enforce rules. Each of about 21 needs is a charge from 1 to 10 satisfied by specific objects for set durations (a phone booth takes 25 minutes, a shower 20), and needs left at the top charge produce side effects. Information itself is a staffed system: features such as viewing finances unlock only after hiring the matching staff member, such as an accountant. Prisoners fall into five security levels with different temperaments, sentence lengths, and cashflow, and reform and labor programs reduce recidivism, which feeds the prison's grade.

## Relations

**influenced by**

- [Theme Hospital](../game/theme-hospital.md)
- [Dwarf Fortress](../game/dwarf-fortress.md)

**uses**

- [Needs decay](../mechanic/needs-decay.md) (core): About 21 prisoner needs (bladder, food, sleep, hygiene, freedom, family, privacy, spirituality, and others) each charge from 1 to 10 and are reset by specific objects or activities; a need at 10 triggers its side effect, and reports color needs from green to red.
- [Daily schedules](../mechanic/daily-schedules.md) (core): Hiring a Warden unlocks an hourly regime per risk category with Lockup, Sleep, Eat, Yard, Shower, Free Time, and Work blocks; each block confines prisoners to areas rather than forcing actions, so needs are met only where the current block lets prisoners go.
- [Building placement](../mechanic/free-placement.md) (core): The prison is drawn tile by tile: foundations, walls, doors, and objects are placed, then workmen build them, and room types are assigned to enclosed areas that contain required objects.
- [Stability and unrest](../mechanic/stability-unrest.md) (core): Needs left unmet for long periods make prisoners irritated, then likely to fight, attack staff, attempt escape, or riot, and violence spreads to nearby prisoners until guards restore order.
- [Crime and policing](../mechanic/crime-policing.md) (core): Guards, dog handlers, armed guards, and snitches counter contraband, gangs, and escape attempts through patrols, searches, and lockdowns.
- [Treasury and budget](../mechanic/budget-treasury.md) (supporting): Income per prisoner per day against staff wages and construction.
- [Staff hiring and rosters](../mechanic/staff-hiring.md) (supporting): Staff such as guards, cooks, janitors, doctors, psychologists, and lawyers are hired individually, and administrators unlock features.
- [Tech tree](../mechanic/tech-tree.md) (supporting): A bureaucracy research tree unlocked through administrative staff.
- [Contracts and orders](../mechanic/contracts-orders.md) (supporting): Federal grants pay out for meeting stated construction or program objectives.
- [Population strata](../mechanic/population-strata.md) (supporting): Five security levels with different temperaments, sentence lengths, and cashflow, plus death row.
- [Agent pathfinding](../mechanic/agent-pathfinding.md) (supporting): Crowd flow through doors and corridors shapes congestion and fights.
- [Power grid](../mechanic/power-grid.md) (supporting): Generators and cables power doors, lights, and kitchens.
- [Fluid pipe networks](../mechanic/fluid-pipe-network.md) (supporting): Water pumps and pipes supply showers and toilets.
- [Fire spread](../mechanic/fire-spread.md) (supporting): Fires spread through the prison and must be fought by firemen.
- [Content sharing](../mechanic/content-sharing.md) (supporting): Player prisons are shared online, and Escape Mode lets players break out of shared prisons.
- [Pause and speed control](../mechanic/variable-speed.md) (supporting)
- [Utility action selection](../mechanic/utility-action-selection.md) (supporting)

## Backlinks (computed)

**influenced:** [Oxygen Not Included](../game/oxygen-not-included.md)

**precedent for:** [Intent-level orders](../opportunity/intent-level-orders.md)

## Sources

- [Prison Architect](../source/src-wikipedia-prison-architect.md)
- [Prison Architect on Steam](../source/src-steam-2026-prison-architect.md)
- [Needs](../source/src-prisonarchitectwiki-2026-needs.md)
- [Regime](../source/src-paradoxwikis-2026-prison-architect-regime.md)

---
Provenance: created in run `2026-10-24-catalog-gb`; reviewed in `2026-10-24-review-fixes`.
