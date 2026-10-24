# Agent inspection

*Mechanic* · `agent-inspection` · status: **asserted**

Selecting an agent opens a panel that reveals its needs, mood contributors, current job, and the reasons behind its behavior.

| field | value |
|---|---|
| aliases | inspect panel, character sheet, unit info panel |
| family | Information & legibility |
| substrate | UI layer, Agent-based |
| math basis | Utility / decision theory |
| feedback | None |
| player interface | Observation only |
| legibility | 4 |
| emergence potential | 1 |
| authoring cost | 2 |
| compute cost | 1 |
| tuning difficulty | 1 |
| ai leverage | 4 |
| maturity | Classic |
| core count *(computed)* | 0 |
| earliest game *(computed)* | [Creatures](../game/creatures.md) |
| earliest year *(computed)* | 1996 |
| prevalence *(computed)* | 5 |
| prevalence share *(computed)* | 0.029 |
| subgenre spread *(computed)* | 4 |
| technique count *(computed)* | 2 |
| technique exposure *(computed)* | 0.75 |

## Definition

Selecting an individual agent opens a live panel that reads that agent's internal state: need levels, mood and its itemized contributors, current action and its target, queued actions, skills, traits, relationships, health by body part, inventory, and sometimes a log of recent thoughts or events. The mechanic owns only the selection and which fields are exposed; it reads state owned by other mechanics and refreshes each tick or on change. Its key design property is whether it shows reasons (why the agent is doing this) or only values. Canonical forms: The Sims need bars and visible action queue, RimWorld's needs, health, and social tabs with each mood thought listed with its source and expiry, Dwarf Fortress unit thoughts and preferences sheets, and RollerCoaster Tycoon guest windows listing a guest's thoughts, cash, hunger, and nausea.

## Player Experience

A crowd becomes individuals. When an agent misbehaves the player clicks it to find out why, reads the cause, and fixes the environment rather than the agent. Reading named thoughts and histories builds attachment and supplies the raw material for player stories.

## Design Levers

- depth of exposure: raw meters, itemized reasons, or a full decision trace
- whether each reason lists its source, magnitude, and remaining duration
- live updating versus snapshot on open
- which variables stay hidden (true personality, latent potential) to preserve uncertainty
- whether every agent is inspectable or only a representative sample at large populations
- supporting affordances such as follow camera, thought bubbles, and pinned favorites

## Failure Modes

- Panels with dozens of unranked numbers overwhelm players without telling them what matters.
- The panel shows state but not the decision rule, so behavior still looks random even after inspection.
- Inspection exposes shortcuts in the agent model; following citizens in SimCity (2013) revealed that agents took the nearest free home and job rather than keeping their own, undermining belief in individual citizens.
- At city scale inspecting one agent is unrepresentative, so players cannot diagnose aggregate problems from it.

## Dynamics

- Players trace aggregate problems to individual causes, such as following one hauler to find a pathing bottleneck.
- Named, inspectable agents raise the emotional cost of loss, which strengthens permadeath and injury systems.
- Exposed reasons create pressure on designers to make the underlying model truthful, since players test it against what the panel says.

## Open Questions

- For agents driven by language models, what inspection format (plans, memories, rationales) lets players predict behavior rather than just read it?
- How much reason exposure maximizes attachment before it turns agents into transparent spreadsheets?

## Relations

**synergy**

- [Memories and thoughts](../mechanic/memories-thoughts.md): Inspection panels expose the thought list, converting hidden state into narrative.

## Backlinks (computed)

**affected by:** [Generative agents (memory stream, reflection, planning)](../technique/generative-agents.md), [LLM explanation of simulation state](../technique/llm-explanation-of-state.md)

**involved in:** [Why-query over the simulation log](../opportunity/causal-why-query.md), [Learned motion for simulated crowds](../opportunity/neural-npc-motion.md)

**used by:** [Creatures](../game/creatures.md), [Generative Agents (Smallville)](../game/generative-agents-smallville.md), [RimWorld](../game/rimworld.md), [RollerCoaster Tycoon](../game/rollercoaster-tycoon.md), [Species: Artificial Life, Real Evolution](../game/species-alre.md)

---
Provenance: created in run `2026-10-24-taxonomy-m6`.
