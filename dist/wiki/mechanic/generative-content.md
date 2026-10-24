# Generative content on demand

*Mechanic* · `generative-content` · status: **sourced**

A generative model creates new content such as text, items, recipes, or rules at runtime in response to player input.

| field | value |
|---|---|
| aliases | runtime generation, AI-generated content, model-generated content |
| family | Narrative & generation |
| substrate | Learned model |
| math basis | Machine learning, Probability / statistics |
| feedback | None |
| player interface | Language, Direct manipulation |
| legibility | 2 |
| emergence potential | 3 |
| authoring cost | 2 |
| compute cost | 5 |
| tuning difficulty | 4 |
| ai leverage | 4 |
| maturity | Emerging |
| core count *(computed)* | 5 |
| earliest game *(computed)* | [AI Dungeon](../game/ai-dungeon.md) |
| earliest year *(computed)* | 2019 |
| prevalence *(computed)* | 7 |
| prevalence share *(computed)* | 0.04 |
| subgenre spread *(computed)* | 2 |
| technique count *(computed)* | 13 |
| technique exposure *(computed)* | 5.812 |

## Definition

Player input (free text, a combination of objects, or a request) plus selected game context is sent to a generative model, usually a large language model, and the output is either shown as content or parsed into game state such as a new item, a combination result, or a rule change. AI Dungeon continues a story from Do, Say, Story, and See inputs, first on GPT-2 (1.5 billion parameters in AI Dungeon 2, 2019) and later GPT-3, with a player-editable memory field. Infinite Craft asks a model to name the result of combining two elements and records first discoveries. Suck Up! and Whispers from the Star use models to drive character responses. Key parts: a context builder, an output schema or parser, a cache that may make results deterministic, and moderation. Inputs: player request and context window. Outputs: text or structured content.

## Player Experience

Open-ended curiosity. Players try things no designer anticipated to see what the model will produce, and part of the fun is probing its boundaries. When the output changes game state, finds feel personal; when it is only text, players notice that nothing is remembered or consequential.

## Design Levers

- what the model may change: presentation only, or typed game state through a constrained schema
- caching and determinism: fresh generation per request versus a shared global cache
- context and memory construction, such as summaries, retrieved facts, and player-pinned memory
- moderation filters and their false-positive rate
- model size, latency budget, and per-request cost
- authored seeds, examples, and rules that anchor tone and balance

## Failure Modes

- Models forget earlier content beyond their context, so stories contradict themselves (a criticism of AI Dungeon).
- Unprompted inappropriate output, and broad filters that flag harmless text, both damaged AI Dungeon's community in 2021.
- Output that does not alter simulation state feels weightless, because nothing it says has consequences.
- Per-request inference cost and latency limit how often generation can run and push it to servers.

## Dynamics

- Players treat the model as a system to probe, sharing prompts that produce surprising or broken outputs.
- A shared global cache turns generation into a discovery race, with first discoveries as social status.
- When outputs are typed into game state, they combine with other systems and can unbalance economies or progression.

## Open Questions

- What output schemas let a model add items or rules to a running simulation without breaking its balance?
- Can on-device models make generation cheap enough to run per tick rather than per player request?
- How should generated content be persisted and versioned so that worlds stay consistent across sessions?

## Relations

**synergy**

- [Natural-language interaction](../mechanic/natural-language-interaction.md): Language input invites generated responses; generated content invites further language input.

**tension**

- [Triggered event chains](../mechanic/triggered-event-chains.md): Generated content resists the authored preconditions event chains rely on.

## Backlinks (computed)

**affected by:** [Automated generation of game rules and mechanics](../technique/automated-rule-generation.md), [Grammar-constrained decoding for valid game actions](../technique/constrained-decoding.md), [Continuous cellular automata and foundation-model search for artificial life](../technique/continuous-alife-and-asal.md), [Diffusion and autoregressive neural game engines](../technique/diffusion-game-engines.md), [Genie foundation world models](../technique/genie-world-models.md), [Learned level and map generation (PCGRL, MarioGPT, LLM generators)](../technique/learned-level-generation.md), [Learned kinematic motion synthesis](../technique/learned-motion-synthesis.md), [LLM game master and narrative director](../technique/llm-game-master.md), [LLM-adjudicated state transitions (LLM as game mechanic)](../technique/llm-rule-adjudication.md), [Muse World and Human Action Model (WHAM)](../technique/muse-wham.md), [Open real-time interactive video world models](../technique/open-interactive-video-models.md), [Real-time generative restyling of game video](../technique/real-time-video-restyling.md), [Text- and image-to-3D asset generation](../technique/text-to-3d-assets.md)

**involved in:** [Local-first AI simulation games](../opportunity/local-first-ai-sims.md)

**used by:** [AI Dungeon](../game/ai-dungeon.md), [Generative Agents (Smallville)](../game/generative-agents-smallville.md), [Infinite Craft](../game/infinite-craft.md), [inZOI](../game/inzoi.md), [Project Sid](../game/project-sid.md), [Suck Up!](../game/suck-up.md), [Whispers from the Star](../game/whispers-from-the-star.md)

## Sources

- [AI Dungeon](../source/src-wikipedia-ai-dungeon.md)

---
Provenance: created in run `2026-10-24-taxonomy-m7`.
