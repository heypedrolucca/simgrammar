# Balance of Power

*Game* · `balance-of-power` · status: **sourced**

A Cold War geopolitical sim in which the player, as US or Soviet leader, spends aid, treaties, and interventions on minor countries over eight annual turns and manages escalating crises to gain prestige without triggering nuclear war.

| field | value |
|---|---|
| year | 1985 |
| developer | Chris Crawford |
| platforms | PC, Mainframe / early micro |
| subgenre | Political sim |
| sim domain | Political / governance, Military / conflict |
| player role | Ruler / statesman |
| agency model | Policy / parameter |
| time model | Turn-based |
| sim scale | Nation / polity |
| fidelity | Stylized |
| perspective | Top-down / side 2D |
| win structure | Score / ranking |
| failure model | Hard restart |
| narrative mode | Hybrid |
| multiplayer | Single-player |
| modding | None |
| production tier | Indie |
| agent count order | Aggregate only |
| emergence | 2 |
| influence | 2 |
| cluster *(computed)* | C12 |
| core count *(computed)* | 3 |
| mechanic count *(computed)* | 6 |

## Summary

A Cold War geopolitical sim in which the player, as US or Soviet leader, spends aid, treaties, and interventions on minor countries over eight annual turns and manages escalating crises to gain prestige without triggering nuclear war.

## Core Loop

review the world map and country data -> commit aid, treaties, and interventions -> rival superpower responds -> contested moves become crises -> escalate or back down -> prestige shifts -> next annual turn

## Design Notes

Crawford built the game around country-level state (alignment, government stability, insurgency) that responds to superpower actions, and around a two-sided crisis exchange in which backing down costs prestige and pushing too far ends the game in nuclear war. Ending the game at nuclear war, rather than letting the war be fought, is its main difference from Bruce Ketchledge's Geopolitique 1990. The crisis escalation exchange is not yet a mechanic in the taxonomy (proposal crisis-escalation).

## Relations

**uses**

- [Faction diplomacy](../mechanic/faction-diplomacy.md) (core): Each turn the player allocates economic and military aid, support for governments or insurgents, interventions, and treaties to minor countries to pull their alignment; the AI superpower answers, and contested moves become crises resolved by no action, diplomatic notes, or military maneuvers.
- [Reputation](../mechanic/reputation.md) (core): Prestige points are the score: winning crises and holding aligned countries raises prestige, backing down in a crisis costs prestige and has political repercussions, and the total after eight years decides the outcome.
- [Turn structure](../mechanic/turn-structure.md) (core): Eight one-year turns; each turn resolves both superpowers' policies and then presents the year's incidents as crises to settle before advancing.
- [Stability and unrest](../mechanic/stability-unrest.md) (supporting): Minor-country governments face insurgencies whose strength shifts with superpower aid to the government or the rebels.
- [Alerts feed](../mechanic/alerts-feed.md) (supporting): Incidents and crises arrive framed as newspaper stories.
- [Data overlays](../mechanic/data-overlays.md) (supporting): The world map can be shaded by country-level variables such as alignment and insurgency.

## Backlinks (computed)

**precedent for:** [Negotiating faction AI](../opportunity/negotiating-faction-ai.md)

## Sources

- [Balance of Power (video game)](../source/src-wikipedia-balance-of-power.md)

---
Provenance: created in run `2026-10-24-catalog-gi`.
