# Crime and policing

*Mechanic* · `crime-policing` · status: **sourced**

Crime levels arise from local conditions such as land value, density, or unemployment, and police coverage, prisons, and justice reduce them.

| field | value |
|---|---|
| aliases | crime rate, law enforcement |
| family | Risk & failure |
| substrate | Cellular grid, Aggregate stocks, Agent-based |
| math basis | System dynamics / ODEs, Cellular automata, Queueing theory |
| feedback | Both |
| player interface | Placement, Parameter |
| legibility | 3 |
| emergence potential | 3 |
| authoring cost | 2 |
| compute cost | 2 |
| tuning difficulty | 3 |
| ai leverage | 2 |
| maturity | Classic |
| core count *(computed)* | 1 |
| earliest game *(computed)* | [SimCity](../game/simcity-1989.md) |
| earliest year *(computed)* | 1989 |
| prevalence *(computed)* | 5 |
| prevalence share *(computed)* | 0.029 |
| subgenre spread *(computed)* | 4 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

Each map cell, district, or agent holds a crime level derived from a propensity function over conditions, minus a suppression term from policing. In the open-sourced SimCity engine (Micropolis), crimeScan sets each cell to 128 - land value + population density (capped at 300), subtracts a police-influence map smoothed three times from station positions and funding, and clamps to 0-250; the city average drives a high-crime warning above 100 and crime feeds back into land value. Agent-based variants such as Cities: Skylines 2 spawn criminals and crime events that police units respond to, with arrests flowing into jails and prisons of limited capacity. Tropico and SimCity 2000 use similar aggregate fields, and Prison Architect models the justice end, where reform and labour programmes lower recidivism and the prison is graded on recidivism, happiness, and violence. Inputs: land value, density, education, employment, happiness, police coverage and funding. Outputs: crime map, satisfaction and value penalties, incidents, and incarcerated population.

## Player Experience

The player reads a crime overlay, spots hot districts, and decides between adding stations, raising police funding, or fixing root causes such as low land value or unemployment. Crime is a visible symptom of neglected neighborhoods and a running cost of growth.

## Design Levers

- inputs and weights of the crime propensity function (land value, density, unemployment, education, happiness)
- police coverage radius, capacity, and the funding-to-effect curve
- justice pipeline capacity: jail and prison slots and what happens when they fill
- strength of crime's feedback into land value, migration, and satisfaction
- aggregate field versus discrete crime events with agents

## Failure Modes

- When suppression is just coverage, the optimal play is blanketing the map with stations, and the social causes the model encodes stop mattering.
- Crime lowers land value, which raises crime, so poor districts can lock into a spiral the player cannot read as a loop.
- Hidden justice capacity limits make crime rise for no visible reason once jails fill.

## Dynamics

- Coverage creates safe islands around stations and crime pockets in gaps, so station placement becomes a covering problem.
- Coupling with land value and zoning makes crime track inequality across the map.
- Budget cuts to policing show up with a lag, producing oscillation when players react late.

## Open Questions

- Can agent-level motives (need, opportunity, social ties) produce crime patterns that reward social policy over coverage, without becoming illegible?
- Would generated investigations or court cases make the justice side of the loop a playable system rather than a capacity number?

## Backlinks (computed)

**used by:** [Dwarf Fortress](../game/dwarf-fortress.md), [Prison Architect](../game/prison-architect.md), [Schedule I](../game/schedule-i.md), [SimCity](../game/simcity-1989.md), [Theme Park](../game/theme-park.md)

## Sources

- [Micropolis: open-source SimCity source code](../source/src-hopkins-2008-micropolis.md)
- [Prison Architect](../source/src-wikipedia-prison-architect.md)

---
Provenance: created in run `2026-10-24-taxonomy-m7`.
