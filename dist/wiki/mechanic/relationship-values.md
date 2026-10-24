# Relationship values

*Mechanic* · `relationship-values` · status: **sourced**

Pairwise numeric affinity between characters changes with interactions and drives social choices.

| field | value |
|---|---|
| aliases | affinity, friendship meter, relationship score |
| family | Social relations |
| substrate | Network / graph, Agent-based, Aggregate stocks |
| math basis | Social network models, System dynamics / ODEs |
| feedback | Reinforcing (positive) |
| player interface | Observation only, Choice / cards |
| legibility | 4 |
| emergence potential | 4 |
| authoring cost | 2 |
| compute cost | 2 |
| tuning difficulty | 3 |
| ai leverage | 3 |
| maturity | Classic |
| core count *(computed)* | 3 |
| earliest game *(computed)* | [Harvest Moon](../game/harvest-moon.md) |
| earliest year *(computed)* | 1996 |
| prevalence *(computed)* | 21 |
| prevalence share *(computed)* | 0.121 |
| subgenre spread *(computed)* | 8 |
| technique count *(computed)* | 1 |
| technique exposure *(computed)* | 0.75 |

## Definition

Owns a weighted, often directed graph over agent pairs holding one or more scalar affinities (friendship, romance, respect) and labels derived by threshold (friend, rival, lover). Interactions add or subtract amounts that depend on the action, personalities, and the current value; many games decay values toward neutral without contact. Agents read the values to decide whom to approach, help, or attack. RimWorld opinion runs -100 to 100 with rival below -20 and friend above 20; chitchat adds about 0.66 up to +10, while insults, up to 6 times likelier at -100 opinion, can start social fights. Prom Week keeps three bidirectional networks: buddy, romance, and cool. The Sims: Hot Date introduced separate short-term and long-term relationship scores. Inputs: interactions, traits, events. Outputs: social choices, cooperation, romance eligibility, conflict.

## Player Experience

The player watches friendships and feuds form, reads relationship meters, and engineers meetings to repair or create bonds. Relationships make losses personal and give characters reasons to act together.

## Design Levers

- number of dimensions per pair (single affinity versus friendship, romance, respect)
- change per interaction and its dependence on the current value
- decay toward neutral and its rate
- label thresholds such as friend, rival, and partner
- symmetry: directed or mutual values

## Failure Modes

- One-dimensional affinity conflates liking with respect or attraction, so relationships feel thin.
- Positive feedback drives every long-standing pair to best friends or mortal enemies.
- Repeating one friendly action maxes a relationship with no story behind it.
- Pairwise storage grows with the square of population, so large games restrict it to notable characters.

## Dynamics

- Agents with compatible traits cluster into friend groups, producing cliques within a colony or town.
- Insults at low opinion push values lower, a reinforcing loop into feuds and fights.
- Deaths and breakups spread grief along the graph, coupling relationships to mood.

## Open Questions

- Can relationship state be inferred from language-model agent conversations rather than incremented by fixed amounts, and stay stable?
- How many relationship dimensions do players track before additional meters stop adding meaning?

## Relations

**synergy**

- [Villager requests](../mechanic/villager-requests.md): Completing requests raises friendship, giving the social meter a concrete verb (Animal Crossing, Stardew).

## Backlinks (computed)

**affected by:** [Generative agents (memory stream, reflection, planning)](../technique/generative-agents.md)

**involved in:** [Drama-aware storyteller](../opportunity/drama-aware-storyteller.md), [Salience-gated language agents](../opportunity/salience-gated-llm-agents.md), [Research by named scientists](../opportunity/scientists-not-tech-trees.md)

**required by:** [Romance and family](../mechanic/romance-family.md), [Social exchanges](../mechanic/social-exchanges.md)

**used by:** [Animal Crossing: New Horizons](../game/animal-crossing-new-horizons.md), [Crusader Kings III](../game/crusader-kings-3.md), [Dwarf Fortress](../game/dwarf-fortress.md), [Façade](../game/facade.md), [Football Manager](../game/football-manager.md), [Generative Agents (Smallville)](../game/generative-agents-smallville.md), [Harvest Moon](../game/harvest-moon.md), [inZOI](../game/inzoi.md), [Paralives](../game/paralives.md), [Project Sid](../game/project-sid.md), [Prom Week](../game/prom-week.md), [RimWorld](../game/rimworld.md), [Space Haven](../game/space-haven.md), [Stardew Valley](../game/stardew-valley.md), [The Sims](../game/the-sims.md), [The Sims 2](../game/the-sims-2.md), [The Sims 3](../game/the-sims-3.md), [The Sims 4](../game/the-sims-4.md), [Tomodachi Life](../game/tomodachi-life.md), [Versu](../game/versu.md), [Where Winds Meet](../game/where-winds-meet.md)

## Sources

- [Social](../source/src-rimworldwiki-2026-social.md)
- [Social Story Worlds With Comme il Faut](../source/src-mccoy-2014-social-story-worlds.md)
- [The Sims (video game)](../source/src-wikipedia-the-sims.md)

---
Provenance: created in run `2026-10-24-taxonomy-m3`.
