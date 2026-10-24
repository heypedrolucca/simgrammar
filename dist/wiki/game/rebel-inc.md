# Rebel Inc.

*Game* · `rebel-inc` · status: **sourced**

A counterinsurgency strategy game in which the player, as a coalition governor, spends a monthly budget on civilian and military initiatives to build popular support and stabilize regions of a war-torn country while corruption, inflation, and an insurgency push back.

| field | value |
|---|---|
| aliases | Rebel Inc: Escalation |
| year | 2018 |
| developer | Ndemic Creations |
| platforms | Mobile, PC |
| subgenre | Political sim |
| subgenre secondary | Wargame / military sim |
| sim domain | Political / governance, Military / conflict, Economic |
| player role | Ruler / statesman |
| agency model | Policy / parameter, Direct unit control |
| time model | Real-time with pause |
| sim scale | Region |
| fidelity | Stylized |
| perspective | Top-down / side 2D |
| win structure | Scenario goals |
| failure model | Hard restart |
| narrative mode | Hybrid |
| multiplayer | Single-player |
| modding | None |
| production tier | Indie |
| agent count order | Aggregate only |
| emergence | 2 |
| influence | 1 |
| influenced by | [Plague Inc.](../game/plague-inc.md) |
| cluster *(computed)* | C01 |
| core count *(computed)* | 3 |
| mechanic count *(computed)* | 7 |

## Summary

A counterinsurgency strategy game in which the player, as a coalition governor, spends a monthly budget on civilian and military initiatives to build popular support and stabilize regions of a war-torn country while corruption, inflation, and an insurgency push back.

## Core Loop

fund civilian initiatives in regions -> popular support rises -> spending raises corruption and inflation -> an insurgency emerges and contests regions -> deploy troops, counter corruption, or negotiate -> stabilize the country to win

## Design Notes

Rebel Inc. inverts Ndemic's earlier Plague Inc.: instead of spreading a disease, the player contains an insurgency by building popular support, and spending itself generates corruption and inflation. The tension is between civilian initiatives that win support slowly and military spending that holds ground without building support. Corruption as a side effect of spending is not yet a mechanic in the taxonomy (proposal corruption-leakage).

## Relations

**influenced by**

- [Plague Inc.](../game/plague-inc.md)

**uses**

- [Treasury and budget](../mechanic/budget-treasury.md) (core): A monthly budget funds infrastructure, jobs, education, roads, and military spending; the more initiatives the player funds, the more corruption and inflation rise, and the Economist governor receives the whole budget annually.
- [Stability and unrest](../mechanic/stability-unrest.md) (core): An insurgency emerges partway through and contests regions against coalition forces; later, peace can be negotiated with insurgent leaders.
- [Citizen satisfaction](../mechanic/citizen-satisfaction.md) (core): Civilian initiatives raise popular support region by region, and stabilizing the country without letting insurgents take control is the goal.
- [Policy toggles](../mechanic/policy-toggles.md) (supporting): A governance tab offers anti-corruption measures.
- [Triggered event chains](../mechanic/triggered-event-chains.md) (supporting): Random events interrupt plans and offer choices.
- [Scenario objectives](../mechanic/scenario-objectives.md) (supporting): Each region has its own geography, and selectable governors such as the Economist and the Warlord change the rules.
- [Corruption leakage](../mechanic/corruption-leakage.md) (supporting): Funding more civilian initiatives raises corruption and inflation, which erode what the monthly budget achieves; the governance tab offers anti-corruption measures.

## Backlinks (computed)

**precedent for:** [Calibrated serious simulations](../opportunity/calibrated-serious-sims.md)

## Sources

- [Rebel Inc. (video game)](../source/src-wikipedia-rebel-inc.md)

---
Provenance: created in run `2026-10-24-catalog-gi`.
