# Stability and unrest

*Mechanic* · `stability-unrest` · status: **sourced**

Grievances accumulate into unrest that triggers protests, strikes, or revolt.

| field | value |
|---|---|
| aliases | unrest, rebellion, revolt meter |
| family | Governance & policy |
| substrate | Aggregate stocks, Stochastic events |
| math basis | System dynamics / ODEs, Markov / stochastic processes |
| feedback | Reinforcing (positive) |
| player interface | Observation only, Choice / cards |
| legibility | 3 |
| emergence potential | 4 |
| authoring cost | 2 |
| compute cost | 1 |
| tuning difficulty | 4 |
| ai leverage | 3 |
| maturity | Classic |
| core count *(computed)* | 3 |
| earliest game *(computed)* | [Utopia](../game/utopia.md) |
| earliest year *(computed)* | 1982 |
| prevalence *(computed)* | 12 |
| prevalence share *(computed)* | 0.069 |
| subgenre spread *(computed)* | 5 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

Owns an unrest or radicalism stock per region, group, or nation. Each period grievances (unmet needs, opposed laws, taxes, war exhaustion, occupation) add to it and suppression (police, garrisons, concessions, propaganda) subtracts. Crossing thresholds triggers escalating events: protests, strikes, riots, rebel spawns, secession, revolution, or game over. Civilization (1991) puts a city into disorder, halting production, when unhappy citizens outnumber happy ones. Europa Universalis IV accumulates rebel progress in provinces with positive unrest until rebels rise. Victoria 3 starts a revolution clock when a political movement's radicalism is high enough that it turns to revolt, and each time the clock fills the revolution advances through events. Frostpunk (2018) ends in revolt when discontent stays too high or hope too low for an extended period.

## Player Experience

A pressure cooker. The player watches unrest rise, decides whether to concede, suppress, or wait it out, and feels the cost of each option. Thresholds create anxious countdowns and dramatic turning points.

## Design Levers

- grievance sources and their weights
- suppression tools, their costs, and side effects such as increasing long-term grievance
- threshold ladder and escalation speed
- spatial scope: per province, per group, or national
- warning visibility, such as clocks, meters, and forecasts

## Failure Modes

- Cheap suppression makes unrest trivial, as with stacking garrisons or police.
- Instant revolt at a threshold feels arbitrary without visible warning.
- Revolts that only spawn more units to fight turn politics into whack-a-mole combat.

## Dynamics

- Disorder halts production, which worsens shortages and raises grievances, a death spiral.
- Suppression buys time but raises long-term grievances, deferring rather than resolving crises.
- Unrest in one region can spread or inspire neighboring regions.

## Open Questions

- Can agent-based protest dynamics (social contagion, leaders) replace scalar unrest meters while staying readable?
- Can LLM-generated demands make movements negotiable rather than just threats to suppress?

## Backlinks (computed)

**involved in:** [Natural-language legislation](../opportunity/natural-language-legislation.md)

**used by:** [Balance of Power](../game/balance-of-power.md), [Crusader Kings III](../game/crusader-kings-3.md), [Europa Universalis IV](../game/europa-universalis-4.md), [Frostpunk 2](../game/frostpunk-2.md), [Hearts of Iron IV](../game/hearts-of-iron-4.md), [Prison Architect](../game/prison-architect.md), [Rebel Inc.](../game/rebel-inc.md), [Songs of Syx](../game/songs-of-syx.md), [Stellaris](../game/stellaris.md), [Tropico 6](../game/tropico-6.md), [Utopia](../game/utopia.md), [Victoria 3](../game/victoria-3.md)

## Sources

- [Victoria 3 Dev Diary #80: Law Enactment and Revolution Clock in 1.3](../source/src-paradox-2023-vic3-law-enactment.md)
- [Frostpunk](../source/src-wikipedia-frostpunk.md)

---
Provenance: created in run `2026-10-24-taxonomy-m2`.
