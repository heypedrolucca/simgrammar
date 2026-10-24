# Corruption leakage

*Mechanic* · `corruption-leakage` · status: **sourced**

A corruption level driven by spending, administrative reach, or size removes a share of revenue or output until countermeasures bring it down.

| field | value |
|---|---|
| aliases | corruption, waste, graft |
| family | Governance & policy |
| substrate | Aggregate stocks |
| math basis | System dynamics / ODEs, Optimization |
| feedback | Balancing (negative) |
| player interface | Parameter, Choice / cards |
| legibility | 3 |
| emergence potential | 2 |
| authoring cost | 1 |
| compute cost | 1 |
| tuning difficulty | 3 |
| ai leverage | 2 |
| maturity | Established |
| core count *(computed)* | 0 |
| earliest game *(computed)* | [Sid Meier's Civilization](../game/civilization.md) |
| earliest year *(computed)* | 1991 |
| prevalence *(computed)* | 4 |
| prevalence share *(computed)* | 0.023 |
| subgenre spread *(computed)* | 3 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

Owns a corruption level per polity, region, or city and the rule that turns it into losses. Each period the level rises with drivers such as the volume of spending or programs, distance from the seat of government, the number of administered territories, or weak institutions, and falls with countermeasures such as anti-corruption policies, courthouses, audits, or dedicated spending; some games accumulate it as a stock with slow decay, others recompute it each turn from current conditions. A share that grows with the level is then removed from tax revenue, trade, production, or program effectiveness, or added to costs. Rebel Inc. (2018) makes corruption a side effect of governing: the more civilian initiatives the player funds, the more corruption and inflation rise, and a governance tab offers anti-corruption measures. Civilization (1991) and Europa Universalis IV use other forms. It differs from taxation, which sets the rate of collection, and from stability-unrest, which owns grievance; corruption owns the leak between what the state raises and what it gets to use.

## Player Experience

Growth carries a hidden tax. The player watches part of every budget vanish, weighs how much to spend fighting it, and learns that expanding programs or territory faster than institutions can follow makes each new unit of spending worth less.

## Design Levers

- drivers of corruption (spending volume, distance, territory count, institution quality)
- what leaks and how much: revenue, output, program effectiveness, or costs
- countermeasures and their price (policies, buildings, dedicated spending)
- accumulated stock with decay versus a level recomputed each period
- visibility, from a shown meter to losses visible only in the ledger

## Failure Modes

- One cheap countermeasure, a single building or policy, zeroes corruption and removes the mechanic from play.
- A flat percentage loss with no driver the player can influence feels like an arbitrary tax rather than a decision.
- Distance-based corruption punishes spread-out realms so hard that one empire shape dominates.
- Leaks without a breakdown make budgets feel randomly short.

## Dynamics

- Corruption caps efficient size, since each additional city, territory, or program returns less, a balancing loop on expansion.
- Spending to win support raises corruption that erodes the budget for further spending, as in Rebel Inc.
- Players invest in countermeasures first in regions far from the center, which shapes expansion order.

## Open Questions

- Can corruption be modeled as agents (officials, contractors) who skim and can be investigated, rather than as a percentage, while staying readable?
- Which drivers make corruption a strategic constraint rather than a flat tax?

## Backlinks (computed)

**used by:** [Sid Meier's Civilization](../game/civilization.md), [Europa Universalis IV](../game/europa-universalis-4.md), [Rebel Inc.](../game/rebel-inc.md), [Stellaris](../game/stellaris.md)

## Claims

- In Rebel Inc. the more initiatives the player funds from the monthly budget, the more corruption and inflation rise, and a governance tab offers anti-corruption measures. *(confidence: medium)* [[69](../source/src-wikipedia-rebel-inc.md)]

## Sources

- [Rebel Inc. (video game)](../source/src-wikipedia-rebel-inc.md)

---
Provenance: created in run `2026-10-24-taxonomy-triage-a`.
