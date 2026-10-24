# Factories with a living workforce

*Opportunity* · `living-workforce-factories` · status: **asserted**

Automation games whose workers age, learn, form families, and retire, so a production network is also a society that must be sustained across generations.

| field | value |
|---|---|
| opportunity type | New genre |
| involves | [Production chains](../mechanic/production-chain.md), [Lifecycle and aging](../mechanic/lifecycle-aging.md), [Agent skills](../mechanic/agent-skills.md), [Education and workforce](../mechanic/education-workforce.md), [Needs decay](../mechanic/needs-decay.md), [Romance and family](../mechanic/romance-family.md) |
| applies | [Generative agents (memory stream, reflection, planning)](../technique/generative-agents.md), [On-device small language models for characters](../technique/on-device-language-models.md), [Massively parallel GPU simulation](../technique/massively-parallel-simulation.md) |
| precedent | [Captain of Industry](../game/captain-of-industry.md), [Workers & Resources: Soviet Republic](../game/workers-and-resources.md), [Oxygen Not Included](../game/oxygen-not-included.md), [Dwarf Fortress](../game/dwarf-fortress.md), [Banished](../game/banished.md) |
| novelty | 3 |
| feasibility | 4 |
| impact | 3 |
| horizon | Now |
| falsifiable signal | {'prediction': 'A factory or automation game in which workers age, train, and are replaced by a simulated next generation will reach 1,000 Steam user reviews.', 'resolve_by': '2029-12-31', 'criteria': 'Title released after 2026-10-24; its Steam page describes generational workforce mechanics (aging, training, succession) in a factory or automation game, and it has at least 1,000 Steam user reviews by the resolve date.'} |
| priority *(computed)* | 3.318 |

## Thesis

The white-space analysis shows production chains and agent lifecycles are both common yet almost never combined: factory games are run by machines or faceless workers, and games with aging, family-forming agents rarely have deep production. Colony sims and Workers & Resources sit closest. A factory whose throughput depends on a workforce with skills, schooling, households, and turnover couples the most-used rule-system in the catalog to the most attachment-generating ones. Salience-gated language agents make that workforce individually legible without per-tick cost.

## Design Sketch

Machines need operators with trained skills; skilled workers age and retire; children of workers attend schools the player builds; housing, food, and morale affect shift output. A bottleneck can be a missing machine or a missing mentor. Generational play replaces the usual tech-tree endgame with succession planning for the workforce.

## Key Risks

- Workforce management can bury the logistics puzzle players came for.
- Agent counts at factory scale strain compute.
- Two audiences (automation and life-sim) may each find half the game unwanted.

## Validation Experiment

Prototype a small automation map where each machine needs a skilled operator drawn from a simulated population with aging and schooling; compare session length and self-reported attachment with a machines-only control. Success: longer sessions and higher attachment without lower throughput-puzzle ratings.

## Falsifiable signal

- **Prediction:** A factory or automation game in which workers age, train, and are replaced by a simulated next generation will reach 1,000 Steam user reviews.
- **Resolve by:** 2029-12-31
- **Criteria:** Title released after 2026-10-24; its Steam page describes generational workforce mechanics (aging, training, succession) in a factory or automation game, and it has at least 1,000 Steam user reviews by the resolve date.

## Relations

**applies**

- [Generative agents (memory stream, reflection, planning)](../technique/generative-agents.md)
- [On-device small language models for characters](../technique/on-device-language-models.md)
- [Massively parallel GPU simulation](../technique/massively-parallel-simulation.md)

**involves**

- [Production chains](../mechanic/production-chain.md)
- [Lifecycle and aging](../mechanic/lifecycle-aging.md)
- [Agent skills](../mechanic/agent-skills.md)
- [Education and workforce](../mechanic/education-workforce.md)
- [Needs decay](../mechanic/needs-decay.md)
- [Romance and family](../mechanic/romance-family.md)

**precedent**

- [Captain of Industry](../game/captain-of-industry.md)
- [Workers & Resources: Soviet Republic](../game/workers-and-resources.md)
- [Oxygen Not Included](../game/oxygen-not-included.md)
- [Dwarf Fortress](../game/dwarf-fortress.md)
- [Banished](../game/banished.md)

---
Provenance: created in run `2026-10-24-synthesis`; reviewed in `2026-10-24-review-fixes`.
