# The Sims

*Game* · `the-sims` · status: **sourced**

A life sim in which the player builds a house and guides a household of Sims whose decaying motives, personalities, careers, and relationships produce an open-ended domestic story.

| field | value |
|---|---|
| year | 2000 |
| developer | Maxis |
| platforms | PC, Console |
| subgenre | Life sim |
| sim domain | Domestic / personal, Social / interpersonal |
| player role | Caretaker |
| agency model | Direct unit control, Indirect incentive, Zoning / placement |
| time model | Real-time with pause |
| sim scale | Household / crew |
| fidelity | Stylized |
| perspective | Isometric |
| win structure | Open sandbox |
| failure model | Permadeath |
| narrative mode | Emergent |
| multiplayer | Single-player, Co-op |
| modding | Content |
| production tier | AAA |
| agent count order | ~10 |
| emergence | 3 |
| influence | 5 |
| influenced by | [Little Computer People](../game/little-computer-people.md) |
| cluster *(computed)* | C01 |
| core count *(computed)* | 3 |
| mechanic count *(computed)* | 15 |

## Summary

A life sim in which the player builds a house and guides a household of Sims whose decaying motives, personalities, careers, and relationships produce an open-ended domestic story.

## Core Loop

build and furnish the lot -> motives decay -> objects advertise motive gains and Sims act or take queued orders -> jobs pay for upgrades -> skills and friendships unlock promotions -> expand house and family

## Design Notes

Will Wright drew on Christopher Alexander's A Pattern Language, treating a house as a set of functional patterns judged by how well they serve the people living in it. Much of the behavioral logic sits in objects: each object advertises which motives it raises and by how much, and Sims with free will enabled choose among those advertisements weighted by their current motives. Sims are deliberately not fully autonomous, since paying bills, finding jobs, exercising, and having children need explicit commands, so the player alternates between architect and caretaker. Build and Buy modes pause time, separating spatial design from the live simulation.

## Relations

**influenced by**

- [Little Computer People](../game/little-computer-people.md)

**uses**

- [Needs decay](../mechanic/needs-decay.md) (core): Eight motives (Hunger, Comfort, Hygiene, Bladder, Energy, Fun, Social, Room) decay at different rates; low motives drag down mood, and neglect can kill.
- [Smart objects](../mechanic/smart-objects.md) (core): Each of the 150-plus base-game objects advertises motive gains (a refrigerator advertises Hunger, a bed Energy), and Sims query the lot's objects to find interactions.
- [Building placement](../mechanic/free-placement.md) (core): Build and Buy modes freeze time while the player lays walls, floors, and objects on a square tile grid; object quality and layout set how efficiently motives can be met.
- [Utility action selection](../mechanic/utility-action-selection.md) (supporting): Free will scores advertised interactions against current motive levels so the most depleted motive tends to win; players can cancel queued autonomous actions.
- [Autonomy levels](../mechanic/autonomy-levels.md) (supporting): Free will is an option toggle; even with it on, bills, job hunting, exercise, and having children need commands.
- [Personality traits](../mechanic/personality-traits.md) (supporting): Twenty-five personality points are split across Neat, Outgoing, Active, Playful, and Nice, which change preferred activities and social outcomes.
- [Agent skills](../mechanic/agent-skills.md) (supporting): Cooking, Mechanical, Charisma, Body, Logic, and Creativity rise through objects such as bookshelves, mirrors, and chess tables, and gate promotions.
- [Career ladder](../mechanic/career-ladder.md) (supporting): Ten career tracks with ten levels each; promotions need skill points and a minimum number of household friends, and change salary and hours.
- [Treasury and budget](../mechanic/budget-treasury.md) (supporting): Every household starts with 20,000 simoleons regardless of size; wages, bills, and purchases set the balance.
- [Relationship values](../mechanic/relationship-values.md) (supporting): Each pair holds a relationship score moved by interactions and eroding without contact; friend counts feed promotions.
- [Social exchanges](../mechanic/social-exchanges.md) (supporting): Talk, joke, compliment, hug, kiss, tease, slap, and similar interactions succeed or fail on relationship, mood, and personality.
- [Romance and family](../mechanic/romance-family.md) (supporting): Sims can become partners, marry, and have a baby by explicit command; neglected babies can be taken away by a social worker.
- [Decoration and beauty](../mechanic/decoration-beauty.md) (supporting): The Room motive reflects lighting, cleanliness, and decorative value around the Sim.
- [Permadeath](../mechanic/permadeath.md) (supporting): Sims die from neglect or accidents and leave an urn or tombstone; the household continues without them.
- [Pause and speed control](../mechanic/variable-speed.md) (supporting)

## Backlinks (computed)

**influenced:** [Generative Agents (Smallville)](../game/generative-agents-smallville.md), [inZOI](../game/inzoi.md), [Oxygen Not Included](../game/oxygen-not-included.md), [Paralives](../game/paralives.md), [The Sims 2](../game/the-sims-2.md)

**precedent for:** [Salience-gated language agents](../opportunity/salience-gated-llm-agents.md)

## Sources

- [The Sims (video game)](../source/src-wikipedia-the-sims.md)

---
Provenance: created in run `2026-10-24-catalog-gc`; reviewed in `2026-10-24-review-fixes`.
