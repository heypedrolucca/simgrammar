# SimAnt

*Game* · `simant` · status: **sourced**

A Maxis ant-colony simulation in which the player controls one yellow ant that lays trails and recruits nestmates while managing a black colony's castes against a rival red colony, predators, and the household.

| field | value |
|---|---|
| aliases | SimAnt: The Electronic Ant Colony |
| year | 1991 |
| developer | Maxis |
| platforms | PC, Console |
| subgenre | Artificial life |
| subgenre secondary | Colony sim |
| sim domain | Biological / ecological |
| player role | Inhabitant |
| agency model | Direct avatar, Indirect incentive, Policy / parameter |
| time model | Real-time with pause |
| sim scale | Settlement |
| fidelity | Stylized |
| perspective | Top-down / side 2D |
| win structure | Competitive victory |
| failure model | Hard restart |
| narrative mode | Emergent |
| multiplayer | Single-player |
| modding | None |
| production tier | AA |
| agent count order | ~100 |
| emergence | 3 |
| influence | 2 |
| cluster *(computed)* | C01 |
| core count *(computed)* | 3 |
| mechanic count *(computed)* | 9 |

## Summary

A Maxis ant-colony simulation in which the player controls one yellow ant that lays trails and recruits nestmates while managing a black colony's castes against a rival red colony, predators, and the household.

## Core Loop

steer the yellow ant -> lay trails and recruit followers to food or the red nest -> colony grows under caste allocation -> fight the red colony and survive hazards -> send young queens and drones to found new nests -> take the yard and drive out the humans

## Design Notes

Will Wright drew on Hölldobler and Wilson's The Ants to show emergence: individual ants follow simple rules, and the player's main lever on the colony is the trail field that other ants follow, not orders. The player embodies one ant and can swap into any other, which pairs a direct-avatar view with colony-level allocation of workers, soldiers, and breeders. Rain washes away trails and floods nests, and lawnmowers, bug spray, spiders, and antlions kill ants, so the environment erodes the information the player lays down. Trail-following agents are not yet a mechanic in the taxonomy (proposal stigmergic-trails).

## Relations

**uses**

- [Direct avatar control](../mechanic/direct-avatar.md) (core): The player is one yellow ant that digs, carries food and pebbles, receives food by trophallaxis, and fights; double-clicking another ant moves control to it.
- [Unit commands](../mechanic/unit-commands.md) (core): The yellow ant lays trails to food or enemy nests that other black ants follow, and can recruit a group of nearby ants to follow it into fights against spiders, caterpillars, antlions, or red ants.
- [Population strata](../mechanic/population-strata.md) (core): The colony divides into workers (forage, dig, tend brood), soldiers (fight, eat more, cannot tend brood), the queen, and winged breeders, and the player sets the balance.
- [Work priorities](../mechanic/work-priorities.md) (supporting)
- [Lifecycle and aging](../mechanic/lifecycle-aging.md) (supporting): The queen lays eggs that become larvae and adults; young queens and drones mate to found colonies in new map squares.
- [Weather](../mechanic/weather.md) (supporting): Rain washes away trails and can flood nests.
- [Random disasters](../mechanic/random-disasters.md) (supporting): Human footsteps, lawnmowers, bug spray, and electrical outlets kill ants without warning.
- [Vertical layers](../mechanic/vertical-layers.md) (supporting): Surface yard play is viewed from above while nests are shown in side view underground.
- [Scenario objectives](../mechanic/scenario-objectives.md) (supporting)

## Sources

- [SimAnt](../source/src-wikipedia-simant.md)

---
Provenance: created in run `2026-10-24-catalog-gd`.
