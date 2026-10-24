# Language-agent society terrarium

*Opportunity* · `llm-society-terrarium` · status: **asserted**

An observer-gardener genre where players seed and nudge a persistent society of language-model agents and watch institutions, cultures, and histories form.

| field | value |
|---|---|
| opportunity type | New genre |
| involves | [Persistent shared world](../mechanic/persistent-world.md), [Gossip propagation](../mechanic/gossip-propagation.md), [History chronicle](../mechanic/history-chronicle.md), [Player organizations](../mechanic/player-organizations.md), [God powers](../mechanic/god-powers.md), [Faction diplomacy](../mechanic/faction-diplomacy.md) |
| applies | [Many-agent LLM societies](../technique/llm-agent-societies.md), [Generative agents (memory stream, reflection, planning)](../technique/generative-agents.md), [On-device small language models for characters](../technique/on-device-language-models.md) |
| precedent | [Project Sid](../game/project-sid.md), [Generative Agents (Smallville)](../game/generative-agents-smallville.md), [Dwarf Fortress](../game/dwarf-fortress.md), [Conway's Game of Life](../game/game-of-life.md), [Black & White](../game/black-and-white.md) |
| novelty | 5 |
| feasibility | 2 |
| impact | 4 |
| horizon | 3-5 years |
| falsifiable signal | {'prediction': 'A commercially released game whose core loop is observing and nudging a society of at least 50 language-model agents will reach 1,000 Steam reviews.', 'resolve_by': '2029-12-31', 'criteria': 'Steam page confirming LLM-driven agent society as the core loop and a review count of at least 1,000.'} |
| priority *(computed)* | 3.282 |

## Thesis

Generative Agents (2023) and Project Sid (2024) showed that populations of language-model agents produce recognizable social structure: parties, roles, rules, shared beliefs. These are research demos, not games, but the experience they produce resembles the Game of Life and Dwarf Fortress legends: watching a world write its own history. With cheaper inference and chronicle tooling, a terrarium genre becomes viable where the player sets initial conditions and intervenes sparingly, and the product is the history.

## Design Sketch

The player picks a map, founding traits, and scarcity levels, then seeds 50 to 500 agents. Interventions are god-scale and rare: a drought, a prophet, a trade caravan. A chronicle tool summarizes eras, factions, and turning points; players share worlds and replay them from saved event logs.

## Key Risks

- Inference cost for hundreds of agents over long runs.
- Agent societies may converge to bland or repetitive behavior without engineered diversity.
- Emergent content safety in open-ended social simulation.

## Validation Experiment

Run 100 agents for 30 simulated days on a small local model with a chronicle summarizer; have readers rate 20 generated histories against Dwarf Fortress legends excerpts for interest and coherence. Success: comparable interest ratings at under 1 dollar of inference per simulated day.

## Falsifiable signal

- **Prediction:** A commercially released game whose core loop is observing and nudging a society of at least 50 language-model agents will reach 1,000 Steam reviews.
- **Resolve by:** 2029-12-31
- **Criteria:** Steam page confirming LLM-driven agent society as the core loop and a review count of at least 1,000.

## Relations

**applies**

- [Many-agent LLM societies](../technique/llm-agent-societies.md)
- [Generative agents (memory stream, reflection, planning)](../technique/generative-agents.md)
- [On-device small language models for characters](../technique/on-device-language-models.md)

**involves**

- [Persistent shared world](../mechanic/persistent-world.md)
- [Gossip propagation](../mechanic/gossip-propagation.md)
- [History chronicle](../mechanic/history-chronicle.md)
- [Player organizations](../mechanic/player-organizations.md)
- [God powers](../mechanic/god-powers.md)
- [Faction diplomacy](../mechanic/faction-diplomacy.md)

**precedent**

- [Project Sid](../game/project-sid.md)
- [Generative Agents (Smallville)](../game/generative-agents-smallville.md)
- [Dwarf Fortress](../game/dwarf-fortress.md)
- [Conway's Game of Life](../game/game-of-life.md)
- [Black & White](../game/black-and-white.md)

---
Provenance: created in run `2026-10-24-synthesis`.
