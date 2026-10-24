# Versu

*Game* · `versu` · status: **sourced**

A 2013 iPad interactive story platform from Linden Lab in which the player controls one character among autonomous agents who choose actions by simulating their outcomes against hundreds of desires within authored social practices.

| field | value |
|---|---|
| year | 2013 |
| developer | Linden Lab |
| platforms | Mobile |
| subgenre | Social sim |
| sim domain | Social / interpersonal |
| player role | Inhabitant |
| agency model | Direct avatar |
| time model | Turn-based |
| sim scale | Household / crew |
| fidelity | Systemic |
| perspective | Text / UI |
| win structure | Scenario goals |
| failure model | None |
| narrative mode | Hybrid |
| multiplayer | Single-player |
| modding | None |
| production tier | AA |
| agent count order | ~10 |
| emergence | 3 |
| influence | 2 |
| cluster *(computed)* | C04 |
| core count *(computed)* | 2 |
| mechanic count *(computed)* | 6 |

## Summary

A 2013 iPad interactive story platform from Linden Lab in which the player controls one character among autonomous agents who choose actions by simulating their outcomes against hundreds of desires within authored social practices.

## Core Loop

choose a character and episode -> practices offer actions for the situation -> player acts or waits -> other agents simulate each option and take the best for their desires -> emotions, evaluations, and relationships update -> the episode reaches an outcome

## Design Notes

Richard Evans and Emily Short built Versu around social practices: recurring situations such as a meal or a conversation written as reactive joint plans that offer actions to participants without controlling them. Each agent tests a candidate action by applying it to the world state, scoring the result against its desires (over 300 in total), and undoing it, which the authors contrast with the estimated consequences used in The Sims. World state is a set of exclusion-logic sentences, and the Praxis language with a stress tester that runs hundreds of simulated instances supported over 1,000 parameterized actions. Linden Lab cancelled the project in early 2014; social practices have no mechanic id and are proposed as social-practices.

## Relations

**uses**

- [Utility action selection](../mechanic/utility-action-selection.md) (core): Agents score each available action by executing it on the world state, evaluating the result against their desires, and undoing it; the best-scoring action is taken.
- [Social exchanges](../mechanic/social-exchanges.md) (core): Social practices such as a dinner party or a conversation offer role-specific actions with preconditions, and most actions change how characters regard each other.
- [Relationship values](../mechanic/relationship-values.md) (supporting): Agents hold evaluations of each other on roles such as attractiveness or breeding, which actions raise or lower.
- [Memories and thoughts](../mechanic/memories-thoughts.md) (supporting): Fine-grained emotions on Ekman's typology record their target and cause.
- [Personality traits](../mechanic/personality-traits.md) (supporting): Character files assign each agent desires that weight its action scoring.
- [Storyteller director](../mechanic/storyteller-director.md) (supporting): A drama manager agent can act to push an episode's authored plot.

## Sources

- [Versu: A Simulationist Storytelling System](../source/src-evans-2014-versu.md)
- [Introducing Versu](../source/src-short-2013-introducing-versu.md)
- [Versu](../source/src-ifwiki-2026-versu.md)

---
Provenance: created in run `2026-10-24-catalog-gc`.
