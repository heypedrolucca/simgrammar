# Teachable sim companion

*Opportunity* · `teachable-sim-companion` · status: **asserted**

A co-player agent that learns factory, colony, or farm routines from demonstration and language, and grows a library of reusable skills the player can inspect.

| field | value |
|---|---|
| opportunity type | New mechanic |
| involves | [Delegation to AI managers](../mechanic/delegation-to-ai.md), [Blueprints](../mechanic/blueprints.md), [Player programming](../mechanic/player-programming.md), [Natural-language interaction](../mechanic/natural-language-interaction.md) |
| applies | [Generalist instructable game agents (SIMA)](../technique/generalist-game-agents.md), [LLM-written skill libraries (Voyager)](../technique/voyager-skill-libraries.md), [On-device small language models for characters](../technique/on-device-language-models.md) |
| precedent | [Autonauts](../game/autonauts.md), [Factorio](../game/factorio.md), [Minecraft](../game/minecraft.md), [Satisfactory](../game/satisfactory.md) |
| novelty | 4 |
| feasibility | 3 |
| impact | 3 |
| horizon | 1-2 years |
| falsifiable signal | {'prediction': 'A released automation or sandbox game will feature an in-game companion that learns reusable skills from player demonstration or instruction.', 'resolve_by': '2028-12-31', 'criteria': 'Store page or developer documentation describing learned, reusable companion skills in a shipped title.'} |
| priority *(computed)* | 3.178 |

## Thesis

Generalist game agents (SIMA, SIMA 2) follow language instructions across 3D games, and Voyager showed skill libraries of reusable code that grow over play. Automation games already reward teaching: Autonauts made programming bots by demonstration the core loop. A companion that learns skills from the player and stores them as inspectable, shareable routines turns automation from wiring to mentoring.

## Design Sketch

The player demonstrates 'set up a smelting column' once while narrating; the companion abstracts it into a named skill with parameters, shows the generated plan, and reuses it elsewhere. Skills can be edited, combined, and shared. The companion asks clarifying questions when a skill fails.

## Key Risks

- Agents that play the game for you can remove the core pleasure.
- Skill abstraction from one demonstration often over- or under-generalizes.
- Runtime cost of a capable agent on consumer hardware.

## Validation Experiment

In a voxel automation prototype, have players teach five routines by demonstration and narration; measure how often the learned skill succeeds in a new location and whether players report more or less enjoyment than blueprints. Success: 70 percent transfer success and preference over blueprints for at least half of players.

## Falsifiable signal

- **Prediction:** A released automation or sandbox game will feature an in-game companion that learns reusable skills from player demonstration or instruction.
- **Resolve by:** 2028-12-31
- **Criteria:** Store page or developer documentation describing learned, reusable companion skills in a shipped title.

## Relations

**applies**

- [Generalist instructable game agents (SIMA)](../technique/generalist-game-agents.md)
- [LLM-written skill libraries (Voyager)](../technique/voyager-skill-libraries.md)
- [On-device small language models for characters](../technique/on-device-language-models.md)

**involves**

- [Delegation to AI managers](../mechanic/delegation-to-ai.md)
- [Blueprints](../mechanic/blueprints.md)
- [Player programming](../mechanic/player-programming.md)
- [Natural-language interaction](../mechanic/natural-language-interaction.md)

**precedent**

- [Autonauts](../game/autonauts.md)
- [Factorio](../game/factorio.md)
- [Minecraft](../game/minecraft.md)
- [Satisfactory](../game/satisfactory.md)

---
Provenance: created in run `2026-10-24-synthesis`.
