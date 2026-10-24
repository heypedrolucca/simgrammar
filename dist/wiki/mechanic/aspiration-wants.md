# Aspirations and wants

*Mechanic* · `aspiration-wants` · status: **sourced**

An agent's long-term aspiration and current state generate short-horizon wants, and sometimes fears, whose fulfillment pays into a reward meter or currency.

| field | value |
|---|---|
| aliases | wants and fears, wishes, whims, life goals |
| family | Agents & behavior |
| substrate | Agent-based, Rule system, Stochastic events |
| math basis | Utility / decision theory, Markov / stochastic processes |
| feedback | Reinforcing (positive) |
| player interface | Observation only, Choice / cards |
| legibility | 4 |
| emergence potential | 3 |
| authoring cost | 3 |
| compute cost | 1 |
| tuning difficulty | 3 |
| ai leverage | 4 |
| maturity | Established |
| core count *(computed)* | 1 |
| earliest game *(computed)* | [The Sims 2](../game/the-sims-2.md) |
| earliest year *(computed)* | 2004 |
| prevalence *(computed)* | 3 |
| prevalence share *(computed)* | 0.017 |
| subgenre spread *(computed)* | 1 |
| technique count *(computed)* | 1 |
| technique exposure *(computed)* | 0.75 |

## Definition

Owns, per agent, a long-term aspiration (a goal type such as family, knowledge, or fortune), a few open want slots, sometimes paired with fear slots, and a reward stock. A generator refills empty slots by sampling wants from a pool weighted by aspiration, traits, life stage, needs, and recent events; each want is a predicate over simulation state (make a friend, gain a skill level, get promoted) with a point value. When a predicate becomes true the want pays its points and leaves its slot, and a realized fear subtracts. Points feed a meter that shifts mood or behavior and usually a currency for rewards. The Sims 2 set the form: the aspiration biases which wants and fears appear, fulfilled wants fill the aspiration meter, and an elder's remaining lifespan depends on that meter. The Sims 3 replaced it with wishes that pay Lifetime Happiness, and The Sims 4 ties a bonus trait and a goal track to the chosen aspiration. Wants do not decay like needs; unlike a career ladder they are generated from state rather than authored as a fixed sequence, and unlike villager requests they are the agent's own goals.

## Player Experience

A stream of small, personal goals. The player reads what each character wants right now, plans the day around one or two of them, and collects a payout when they land, so an open sandbox gains a to-do list that comes from the character rather than the designer. Fears add dread: the player steers away from events the character would hate.

## Design Levers

- number of open slots and whether fears exist alongside wants
- reroll, lock, and dismiss rules for slots
- generator weights by aspiration, traits, life stage, and recent events
- point value per want and what points buy (meter effects, reward objects, traits)
- difficulty and time horizon of individual wants relative to play pace
- whether unmet wants cost anything or simply expire

## Failure Modes

- Wants that need unavailable or off-lot actions clutter the slots and teach players to ignore the panel.
- Cheap repeatable wants let players farm points, so the reward store empties early and the meter stops mattering.
- Generators that ignore context produce incoherent wants, such as wanting a first date the day after a spouse dies, which breaks the illusion of a mind.
- Too many slots turn the panel into a checklist with no choice in it.

## Dynamics

- Players chase wants that line up across household members, so generated goals couple separate characters' days.
- Wants seeded by recent events (a promotion, a new baby) create follow-on arcs, an informal story chain driven by state.
- Points buy rewards that make later wants easier to meet, a reinforcing loop toward a comfortable late game.

## Open Questions

- Can a language model write wants from an agent's memories and relationships while keeping each want checkable as a predicate over game state?
- Do fears add enough drama to justify goals the player cannot fully prevent from failing?

## Backlinks (computed)

**affected by:** [Generative agents (memory stream, reflection, planning)](../technique/generative-agents.md)

**used by:** [The Sims 2](../game/the-sims-2.md), [The Sims 3](../game/the-sims-3.md), [The Sims 4](../game/the-sims-4.md)

## Claims

- The Sims 2 gives each Sim an aspiration with wants and fears, and an elder's remaining lifespan depends on the aspiration meter; The Sims 3 replaced wants and fears with wishes that pay Lifetime Happiness. *(confidence: medium)* [[55](../source/src-wikipedia-the-sims-2.md), [56](../source/src-wikipedia-the-sims-3.md)]
- The Sims 4 adults take a bonus trait from their chosen aspiration. *(confidence: medium)* [[57](../source/src-wikipedia-the-sims-4.md)]

## Sources

- [The Sims 2](../source/src-wikipedia-the-sims-2.md)
- [The Sims 3](../source/src-wikipedia-the-sims-3.md)
- [The Sims 4](../source/src-wikipedia-the-sims-4.md)

---
Provenance: created in run `2026-10-24-taxonomy-triage-a`.
