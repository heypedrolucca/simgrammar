# Rule-checking inspection

*Mechanic* · `rule-checking-inspection` · status: **sourced**

The player checks documents, people, or cargo against a rulebook that changes over time, under time pressure, with penalties for errors.

| field | value |
|---|---|
| aliases | document inspection, checkpoint inspection |
| family | Operation & procedure |
| substrate | Rule system, Stochastic events |
| math basis | Information theory, Combinatorics |
| feedback | None |
| player interface | Direct manipulation, Choice / cards |
| legibility | 4 |
| emergence potential | 2 |
| authoring cost | 3 |
| compute cost | 1 |
| tuning difficulty | 3 |
| ai leverage | 4 |
| maturity | Established |
| core count *(computed)* | 2 |
| earliest game *(computed)* | [Papers, Please](../game/papers-please.md) |
| earliest year *(computed)* | 2013 |
| prevalence *(computed)* | 2 |
| prevalence share *(computed)* | 0.011 |
| subgenre spread *(computed)* | 1 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

A generator produces cases (travelers, documents, cargo) with attributes, some injected with discrepancies at a configured rate. A rulebook of predicates defines valid cases and grows or changes each day. The player inspects, cross-references, uses tools to reveal hidden attributes, and issues a verdict; errors produce penalties and correct verdicts produce pay, within a fixed time per shift. In Papers, Please each day sets documentation requirements that grow over time, tools include interrogation, fingerprinting, and body scans, citations for protocol violations cut daily earnings, and wages must cover rent, food, and heat. Contraband Police applies the loop to cargo and vehicles. Inputs: case attributes and rules. Outputs: verdicts, earnings, penalties, and story flags.

## Player Experience

Rising cognitive load and moral pressure. Players scan for mismatches against a growing rulebook, race the clock to earn enough for their family, and face cases where following the rules is cruel. Rule changes keep competence from settling into routine.

## Design Levers

- rule count and the rate at which rules are added
- discrepancy injection rate and subtlety
- time per shift and pay per correct case
- penalty structure for errors
- inspection tools and their cost in time
- authored cases with moral stakes mixed into generated ones

## Failure Modes

- Too many concurrent rules overload working memory and become frustrating.
- Purely generated cases without authored stakes reduce play to a matching task.
- Binary penalties with no explanation leave players unsure which rule they broke.

## Dynamics

- Time pressure trades accuracy against throughput, and income pressure pushes players to cut corners.
- Bribes and sympathetic cases set economic incentives against moral judgment.
- Rule growth makes earlier skill obsolete, renewing difficulty every day.

## Open Questions

- Can language models generate cases and dialogue whose discrepancies are subtle yet verifiable against a formal rulebook?
- What rule-addition rate keeps load challenging without exceeding working memory?

## Backlinks (computed)

**involved in:** [Generated inspection shifts](../opportunity/generated-inspection-shifts.md)

**used by:** [Contraband Police](../game/contraband-police.md), [Papers, Please](../game/papers-please.md)

## Sources

- [Papers, Please](../source/src-wikipedia-papers-please.md)

---
Provenance: created in run `2026-10-24-taxonomy-m7`; reviewed in `2026-10-24-review-fixes`.
