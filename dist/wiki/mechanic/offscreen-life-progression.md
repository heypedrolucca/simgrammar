# Off-screen life progression

*Mechanic* · `offscreen-life-progression` · status: **sourced**

Households or agents outside the player's active simulation advance through life events on a cheap stochastic model, so the world changes between visits.

| field | value |
|---|---|
| aliases | story progression, neighborhood stories, background life simulation, off-screen simulation level of detail |
| family | Population & lineage |
| substrate | Stochastic events, Agent-based |
| math basis | Markov / stochastic processes, Population dynamics |
| feedback | Balancing (negative) |
| player interface | Parameter, Observation only |
| legibility | 2 |
| emergence potential | 3 |
| authoring cost | 2 |
| compute cost | 2 |
| tuning difficulty | 3 |
| ai leverage | 4 |
| maturity | Established |
| core count *(computed)* | 0 |
| earliest game *(computed)* | [The Sims 3](../game/the-sims-3.md) |
| earliest year *(computed)* | 2009 |
| prevalence *(computed)* | 3 |
| prevalence share *(computed)* | 0.017 |
| subgenre spread *(computed)* | 1 |
| technique count *(computed)* | 2 |
| technique exposure *(computed)* | 0.812 |

## Definition

Owns a per-period update for agents or households outside the player's active simulation: unplayed households, agents beyond a radius, or regions not loaded. Instead of running needs, action selection, and pathing, each period it rolls life events for every off-screen unit from a table (age up, take or lose a job, move in or out, start or end a relationship, marry, have a child, die) with probabilities set by coarse state such as age, relationships, money, and household size, and writes the results straight into the shared state that the full simulation reads when the unit comes back into view. Many versions also manage population, moving households in when a town is sparse and out when it is crowded. The Sims 3's Story Progression keeps unplayed households aging, working, and forming relationships across its open neighborhood. It differs from lifecycle-aging, which owns life stages and mortality for every agent, and from autonomy-levels, which filters the choices of agents that are fully simulated; here simulation is replaced by event rolls.

## Player Experience

The world feels lived in: visiting a neighbor reveals a new spouse, a baby, or a funeral the player never saw. The same rule also takes control away, since favorite characters can marry, move away, or die off-screen, so players either embrace the surprises or switch the feature off for the households they care about.

## Design Levers

- which event types may fire off-screen (aging, jobs, moves, romance, births, deaths)
- event rates relative to the pace of played households
- per-household or per-world opt-outs that protect characters the player cares about
- population targets that move households in or out
- fidelity of the off-screen model, from pure event tables to simplified versions of the on-screen systems
- how off-screen events are reported (notifications, a newspaper, or nothing)

## Failure Modes

- Off-screen events split families or move away characters the player was invested in, which reads as the game vandalizing the save.
- The off-screen and on-screen models disagree, so an agent returns in a state the full simulation would never produce, such as a job its skills cannot support.
- Unreported events leave players unsure why the town changed and push them to wikis or mods.
- Unbounded population management fills a town with generated strangers and dilutes authored characters.

## Dynamics

- Neighborhoods drift into new social graphs over generations, giving long saves a history no one played.
- Players protect some households and leave others to the dice, producing a two-tier world of directed and generated lives.
- Players install community mods that replace The Sims 3's Story Progression with per-household controls, which shows they want the surprises on their own terms.

## Open Questions

- Can a language model write coherent off-screen life summaries for unplayed agents that the full simulation can resume without contradictions?
- How large a fidelity gap between on-screen and off-screen agents do players notice, and where does it stop mattering?

## Backlinks (computed)

**affected by:** [Generative agents (memory stream, reflection, planning)](../technique/generative-agents.md), [Many-agent LLM societies](../technique/llm-agent-societies.md)

**used by:** [inZOI](../game/inzoi.md), [The Sims 3](../game/the-sims-3.md), [The Sims 4](../game/the-sims-4.md)

## Claims

- The Sims 3 places households in a seamless open neighborhood, and its Story Progression keeps households the player is not controlling aging, working, and forming relationships. *(confidence: medium)* [[56](../source/src-wikipedia-the-sims-3.md)]

## Sources

- [The Sims 3](../source/src-wikipedia-the-sims-3.md)

---
Provenance: created in run `2026-10-24-taxonomy-triage-a`.
