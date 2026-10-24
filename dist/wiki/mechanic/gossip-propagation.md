# Gossip propagation

*Mechanic* · `gossip-propagation` · status: **sourced**

Information about events spreads through social contacts, changing what agents know and believe.

| field | value |
|---|---|
| aliases | rumor spread, information diffusion, knowledge propagation |
| family | Social relations |
| substrate | Network / graph, Agent-based, Stochastic events |
| math basis | Social network models, Epidemiology, Information theory |
| feedback | Reinforcing (positive) |
| player interface | Observation only, Choice / cards |
| legibility | 2 |
| emergence potential | 4 |
| authoring cost | 2 |
| compute cost | 3 |
| tuning difficulty | 3 |
| ai leverage | 4 |
| maturity | Experimental |
| core count *(computed)* | 2 |
| earliest game *(computed)* | [Generative Agents (Smallville)](../game/generative-agents-smallville.md) |
| earliest year *(computed)* | 2023 |
| prevalence *(computed)* | 3 |
| prevalence share *(computed)* | 0.017 |
| subgenre spread *(computed)* | 2 |
| technique count *(computed)* | 2 |
| technique exposure *(computed)* | 0.75 |

## Definition

Owns per-agent knowledge sets (facts, rumors, beliefs about events or other agents), optionally with source and confidence, and the social graph they travel over. When two agents interact, each fact the speaker holds passes with a probability set by salience, relationship, and personality, possibly distorted; receiving a fact can trigger opinion or memory updates. Most games skip this and treat events as known to all: Comme il Faut's social facts database in Prom Week records every event as known to every character. Generative Agents (2023) shows diffusion through language-model conversation: over two game days, awareness of a Valentine's Day party grew from 1 to 13 of 25 agents and of a mayoral candidacy from 1 to 8. Inputs: interactions, event salience, the social graph. Outputs: who knows what, reputation and opinion effects that lag the event, misinformation.

## Player Experience

Actions have a spreading radius: a crime matters once someone talks, so the player manages witnesses, timing, and who to tell. Watching news reach a rival late creates suspense and room for deception.

## Design Levers

- transmission probability per interaction and decay of salience over time
- graph structure: who talks to whom in households, workplaces, and gathering places
- distortion rate and whether sources are tracked
- which facts are worth gossip and how they change opinions
- player tools to plant, suppress, or trace rumors

## Failure Modes

- Slow or patchy propagation makes consequences feel disconnected from actions.
- Untraceable chains make reputation changes look random.
- Tracking every fact for every agent costs memory and update time in large populations.
- Language-model gossip can invent facts that never happened and corrupt game state.

## Dynamics

- Information cascades through social hubs such as innkeepers and leaders, so centrality determines influence.
- Lagged knowledge lets players act before consequences arrive, enabling crime, deception, and damage control.
- Distorted rumors create conflicts over events that did not happen as told.

## Open Questions

- Can language-model gossip be constrained to facts in the simulation log while keeping distortion as a designed, tunable variable?
- What propagation speed makes consequences feel both earned and suspenseful?

## Relations

**synergy**

- [Reputation](../mechanic/reputation.md): Reputation travels through gossip, so deeds have audiences.
- [Relationship values](../mechanic/relationship-values.md): What agents hear about each other changes how they feel.

## Backlinks (computed)

**affected by:** [Generative agents (memory stream, reflection, planning)](../technique/generative-agents.md), [Many-agent LLM societies](../technique/llm-agent-societies.md)

**involved in:** [Generated dream and replay views](../opportunity/dream-replay-layer.md), [Language-agent society terrarium](../opportunity/llm-society-terrarium.md)

**used by:** [Generative Agents (Smallville)](../game/generative-agents-smallville.md), [inZOI](../game/inzoi.md), [Project Sid](../game/project-sid.md)

## Sources

- [Social Story Worlds With Comme il Faut](../source/src-mccoy-2014-social-story-worlds.md)
- [Generative Agents: Interactive Simulacra of Human Behavior](../source/src-park-2023-generative-agents.md)

---
Provenance: created in run `2026-10-24-taxonomy-m3`.
