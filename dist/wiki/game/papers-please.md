# Papers, Please

*Game* · `papers-please` · status: **sourced**

A border inspection game in which the player checks entrants' documents against daily-changing rules on a timed shift and spends the wages on a family's rent, food, and heat.

| field | value |
|---|---|
| year | 2013 |
| developer | Lucas Pope (3909 LLC) |
| platforms | PC, Mobile, Handheld |
| subgenre | Job sim |
| sim domain | Occupational, Political / governance, Domestic / personal |
| player role | Worker |
| agency model | Direct avatar, Policy / parameter |
| time model | Real-time |
| sim scale | Individual |
| fidelity | Stylized |
| perspective | Top-down / side 2D |
| win structure | Campaign |
| failure model | Hard restart |
| narrative mode | Hybrid |
| multiplayer | Single-player |
| modding | None |
| production tier | Indie |
| agent count order | ~10 |
| emergence | 2 |
| influence | 3 |
| cluster *(computed)* | C14 |
| core count *(computed)* | 3 |
| mechanic count *(computed)* | 7 |

## Summary

A border inspection game in which the player checks entrants' documents against daily-changing rules on a timed shift and spends the wages on a family's rent, food, and heat.

## Core Loop

read the day's rules -> inspect each entrant's papers -> interrogate, fingerprint, or scan discrepancies -> stamp approve, deny, or detain -> citations and bribes adjust pay -> pay rent, food, and heat -> next day adds rules

## Design Notes

The inspection rules are predicates that accumulate day by day as the fictional state's politics shift, so the same entrant generator yields harder cases over time. Pay is per correctly processed entrant within a fixed shift and citations arrive by fax after each error, which makes speed and accuracy a direct trade. The household ledger converts that trade into moral pressure, and bribes and rule-bending choices feed scripted branches that lead to twenty endings.

## Relations

**uses**

- [Rule-checking inspection](../mechanic/rule-checking-inspection.md) (core): Each day adds or changes entry requirements; the player cross-checks passports, permits, and other papers, can interrogate, compare fingerprints, or order body scans, and receives faxed citations after protocol violations.
- [Daily action budget](../mechanic/daily-action-budget.md) (core): Each shift is a fixed real-time working day and pay is per properly processed entrant, so processing speed trades against error risk.
- [Treasury and budget](../mechanic/budget-treasury.md) (core): The end-of-day ledger adds wages and bribes, subtracts citation penalties, and requires paying rent, food, heat, and other necessities; going into debt ends the game.
- [Needs decay](../mechanic/needs-decay.md) (supporting): Family members' condition worsens on days when food, heat, or other necessities go unpaid.
- [Dilemma cards](../mechanic/dilemma-cards.md) (supporting): Scripted entrants pose choices such as admitting a supposed spouse without complete papers, trading rule compliance against helping people.
- [Triggered event chains](../mechanic/triggered-event-chains.md) (supporting): EZIC contacts and other scripted encounters branch the story toward twenty endings, including escape to Obristan.
- [Procedural characters](../mechanic/procedural-characters.md) (supporting): Randomly generated entrants are mixed with scripted ones; the unlockable endless mode uses only generated entrants.

## Backlinks (computed)

**influenced:** [Contraband Police](../game/contraband-police.md)

**precedent for:** [Generated inspection shifts](../opportunity/generated-inspection-shifts.md)

## Sources

- [Papers, Please](../source/src-wikipedia-papers-please.md)

---
Provenance: created in run `2026-10-24-catalog-gf`.
