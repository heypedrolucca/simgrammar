# Car Mechanic Simulator 2021

*Game* · `car-mechanic-simulator-2021` · status: **sourced**

A first-person garage sim in which the player diagnoses and repairs customer cars part by part, restores auction and barn-find cars, and expands the workshop.

| field | value |
|---|---|
| aliases | CMS 2021 |
| year | 2021 |
| developer | Red Dot Games |
| platforms | PC, Console |
| subgenre | Job sim |
| sim domain | Occupational, Physical / mechanical |
| player role | Worker |
| agency model | Direct avatar |
| time model | Real-time |
| sim scale | Individual |
| fidelity | Stylized |
| perspective | First-person |
| win structure | Open sandbox |
| failure model | None |
| narrative mode | None |
| multiplayer | Single-player |
| modding | Content |
| production tier | Indie |
| agent count order | None |
| emergence | 1 |
| influence | 1 |
| cluster *(computed)* | C02 |
| core count *(computed)* | 2 |
| mechanic count *(computed)* | 6 |

## Core Loop

accept a generated customer order -> inspect and test the car -> remove parts in order to reach faulty ones -> buy or repair replacements -> reassemble and test drive -> get paid -> upgrade the garage and restore cars for sale

## Design Notes

The car is a tree of modeled parts (over 4000 across 72 cars) with a removal order, so labor is spent reaching a faulty component before replacing it, the series loop carried over from Car Mechanic Simulator 2018. Customer orders are generated without end, while story missions, car and salvage auctions, barn finds, and a project-car restoration supply variety. A skills and garage-upgrade system gates faster or more capable work.

## Relations

**uses**

- [Diagnose and repair](../mechanic/diagnose-repair.md) (core): Orders list symptoms; the player examines engine, suspension, and chassis, removes covering parts in a realistic order to reach damaged ones, replaces or repairs them, and verifies the fix, across over 4000 parts on 72 cars.
- [Contracts and orders](../mechanic/contracts-orders.md) (core): An endless supply of generated customer orders plus story missions with their own requirements provide income.
- [Auctions](../mechanic/auctions.md) (supporting): Car auctions and salvage auctions supply restoration projects for resale.
- [Agent skills](../mechanic/agent-skills.md) (supporting): Experience feeds a skills and garage-upgrade system.
- [Vehicle dynamics](../mechanic/vehicle-dynamics.md) (supporting): Repaired and tuned cars can be driven, including time trials on a race track.
- [Direct avatar control](../mechanic/direct-avatar.md) (supporting)

## Sources

- [Car Mechanic Simulator 2021 on Steam](../source/src-steam-2026-car-mechanic-simulator-2021.md)
- [Car Mechanic Simulator 2021 on Xbox](../source/src-xbox-2026-car-mechanic-simulator-2021.md)
- [Car Mechanic Simulator 2018](../source/src-wikipedia-car-mechanic-simulator-2018.md)

---
Provenance: created in run `2026-10-24-catalog-gf`.
