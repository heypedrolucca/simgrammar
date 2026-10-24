# Villager requests

*Mechanic* · `villager-requests` · status: **asserted**

Characters generate small requests or quests from templates whose parameters are filled from simulation state, with rewards and deadlines.

| field | value |
|---|---|
| aliases | radiant quests, favors, help wanted |
| family | Narrative & generation |
| substrate | Rule system, Stochastic events, Agent-based |
| math basis | Probability / statistics, Utility / decision theory |
| feedback | None |
| player interface | Observation only, Choice / cards |
| legibility | 5 |
| emergence potential | 2 |
| authoring cost | 3 |
| compute cost | 1 |
| tuning difficulty | 2 |
| ai leverage | 4 |
| maturity | Established |
| core count *(computed)* | 1 |
| earliest game *(computed)* | [The Sims 3](../game/the-sims-3.md) |
| earliest year *(computed)* | 2009 |
| prevalence *(computed)* | 3 |
| prevalence share *(computed)* | 0.017 |
| subgenre spread *(computed)* | 2 |
| technique count *(computed)* | 2 |
| technique exposure *(computed)* | 0.75 |

## Definition

A generator periodically picks a requester, a template (fetch an item, deliver a gift, clear pests, make a visit), and parameters drawn from current state, such as an item in season or a nearby location. It posts the request with a reward, often relationship points or money, and a deadline. Completing it applies the reward; expiry may cost relationship. Stardew Valley's Help Wanted board posts item delivery and gathering requests from villagers; Skyrim's radiant quests fill templates with locations and targets; Animal Crossing villagers ask small favors; Mount and Blade lords issue procedural tasks. Inputs: requester state, inventory and season, relationship. Outputs: posted tasks and reward deltas.

## Player Experience

A light stream of small goals that gives daily play direction and makes characters feel like they have needs. Requests nudge players toward activities they might skip and reward them with friendship. Players learn which requests are worth it and ignore the rest.

## Design Levers

- template set and how parameters bind to live state
- posting frequency and number of concurrent requests
- reward type and size relative to effort
- deadlines and penalties for expiry
- requester selection by need, relationship, or location

## Failure Modes

- Template repetition makes requests read as generic chores; radiant quests in Skyrim drew this criticism.
- Requests that ignore state ask for impossible items or locations already cleared.
- Low rewards teach players to ignore the system entirely.

## Dynamics

- Requests pull players across map areas and seasonal resources they would otherwise skip.
- Rewards in relationship points couple requests to romance and social progression.
- When requests read live scarcity, they double as a signal of what the economy lacks.

## Open Questions

- Can requests generated from a character's actual needs and memories, with language-model dialogue, avoid template fatigue?
- What request rate keeps them meaningful without crowding out self-directed play?

## Backlinks (computed)

**affected by:** [LLM game master and narrative director](../technique/llm-game-master.md), [Open-ended co-generation of environments and agents](../technique/open-ended-environment-generation.md)

**involved in:** [Content-elastic event systems](../opportunity/content-elastic-events.md), [Placement that tells stories](../opportunity/placement-that-tells-stories.md)

**used by:** [Stardew Valley](../game/stardew-valley.md), [The Sims 3](../game/the-sims-3.md), [Tomodachi Life](../game/tomodachi-life.md)

---
Provenance: created in run `2026-10-24-taxonomy-m7`.
