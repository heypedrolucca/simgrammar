# Tropico 6

*Game* · `tropico-6` · status: **sourced**

A political city builder in which El Presidente develops an island archipelago across four eras while individually simulated citizens' happiness and faction loyalties decide elections, protests, and revolts.

| field | value |
|---|---|
| year | 2019 |
| developer | Limbic Entertainment |
| platforms | PC, Console, Handheld |
| subgenre | City builder |
| subgenre secondary | Political sim |
| sim domain | Urban, Political / governance, Economic |
| player role | Ruler / statesman |
| agency model | Zoning / placement, Policy / parameter |
| time model | Real-time with pause |
| sim scale | Nation / polity |
| fidelity | Stylized |
| perspective | Free 3D camera |
| win structure | Scenario goals |
| failure model | Hard restart |
| narrative mode | Hybrid |
| multiplayer | Single-player, Co-op, Competitive |
| modding | None |
| production tier | AA |
| agent count order | ~1,000 |
| emergence | 3 |
| influence | 1 |
| cluster *(computed)* | C04 |
| core count *(computed)* | 3 |
| mechanic count *(computed)* | 12 |

## Summary

A political city builder in which El Presidente develops an island archipelago across four eras while individually simulated citizens' happiness and faction loyalties decide elections, protests, and revolts.

## Core Loop

build housing, jobs, and services across the islands -> each citizen's happiness and faction alignment shift with conditions -> issue edicts, trade, and raid to fund the treasury -> advance through four eras -> win elections or suppress rebels to stay in power

## Design Notes

Tropico couples a conventional production and services city builder to a political layer: each simulated citizen holds happiness and faction alignments, and those aggregate into election results and rebel recruitment. Edicts and policies trade one faction's approval against another's, so building decisions double as political ones. Tropico 6 moves play to an archipelago joined by bridges from the World Wars era onward and organizes progress into Colonial, World Wars, Cold War, and Modern eras.

## Relations

**uses**

- [Interest groups](../mechanic/interest-groups.md) (core): Political factions each approve or disapprove of El Presidente based on conditions and decisions that match their ideology.
- [Elections](../mechanic/elections.md) (core): Elections can be held or rigged; losing one removes El Presidente and ends the game.
- [Citizen satisfaction](../mechanic/citizen-satisfaction.md) (core): Each citizen's happiness across categories such as food, housing, and liberty aggregates into approval.
- [Policy toggles](../mechanic/policy-toggles.md) (supporting): Edicts with costs and effects on factions and citizens.
- [Stability and unrest](../mechanic/stability-unrest.md) (supporting): Low approval breeds rebels, protests, and coup attempts.
- [Building placement](../mechanic/free-placement.md) (supporting): Buildings placed freely across the islands; bridges connect islands from the World Wars era.
- [Trade routes](../mechanic/trade-routes.md) (supporting): Exports through docks fund the treasury.
- [Production chains](../mechanic/production-chain.md) (supporting)
- [Treasury and budget](../mechanic/budget-treasury.md) (supporting)
- [Education and workforce](../mechanic/education-workforce.md) (supporting): Skilled jobs require citizens with high school or college education.
- [Faction diplomacy](../mechanic/faction-diplomacy.md) (supporting): Relations with foreign powers affect trade and aid.
- [Pause and speed control](../mechanic/variable-speed.md) (supporting)

## Sources

- [Tropico 6](../source/src-wikipedia-tropico-6.md)

---
Provenance: created in run `2026-10-24-catalog-ga`; reviewed in `2026-10-24-review-fixes`.
