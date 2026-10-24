# Natural-language interaction

*Mechanic* · `natural-language-interaction` · status: **sourced**

The player communicates with characters by free text or voice, and the system interprets intent and responds.

| field | value |
|---|---|
| aliases | free-text dialogue, conversational characters, voice input |
| family | Social relations |
| substrate | Learned model, Rule system |
| math basis | Machine learning, Information theory |
| feedback | None |
| player interface | Language |
| legibility | 2 |
| emergence potential | 4 |
| authoring cost | 3 |
| compute cost | 4 |
| tuning difficulty | 4 |
| ai leverage | 5 |
| maturity | Established |
| core count *(computed)* | 6 |
| earliest game *(computed)* | [Little Computer People](../game/little-computer-people.md) |
| earliest year *(computed)* | 1985 |
| prevalence *(computed)* | 11 |
| prevalence share *(computed)* | 0.063 |
| subgenre spread *(computed)* | 6 |
| technique count *(computed)* | 6 |
| technique exposure *(computed)* | 2.175 |

## Definition

Owns the mapping from a player utterance to a game-meaningful interpretation and the character's reply. A parser or model classifies free text or speech into intents, or produces an open reply, and the result updates character state, relationships, or plot. Facade (2005) maps typed text through about 800 hand-authored template rules (compiled to about 6,800 Jess rules) into 24 discourse act types such as agree, criticize, and flirt, plus a catch-all for non-understanding; the rules are permissive, accepting false positives to avoid non-understanding, and a drama manager sequences story beats from the result. AI Dungeon (2019) passes player text to GPT-2 and from 2020 GPT-3 to continue the story. Seaman (1999) took microphone input, and Suck Up! (2023) has players talk their way into homes of language-model characters. Inputs: text or speech, game state. Outputs: intent or discourse act, state updates, generated dialogue.

## Player Experience

The player says what they mean instead of picking from a menu, which raises both agency and anxiety: phrasing becomes a skill and characters can surprise. Misunderstandings and off-topic replies break immersion quickly, so players probe the system's limits.

## Design Levers

- interpretation target: a fixed intent set, discourse acts, or open generation
- fallback behavior when input is not understood
- grounding constraints that tie replies to game state and authored canon
- input modality (typed or voice) and response latency
- how strongly language outcomes change simulation state versus adding flavor only

## Failure Modes

- Non-understanding loops: the system misreads input and the player rephrases repeatedly.
- Open models drift from canon or game state and promise things the simulation cannot deliver; AI Dungeon was criticized for forgetting earlier content.
- Players manipulate characters with meta-instructions, trivializing persuasion goals.
- Moderation filters misfire; AI Dungeon's 2021 filter flagged harmless content.

## Dynamics

- Players develop phrasing strategies (flattery, logic traps, role-play) that work as skill expression.
- Language outcomes feed relationship and opinion systems, making conversation a primary social lever.
- Players share transcripts, so interactions become community content.

## Open Questions

- How can free-form dialogue be grounded so that what characters say always matches simulation state and what they can do?
- What evaluation shows that language input adds agency rather than guesswork compared with dialogue menus?

## Relations

**synergy**

- [Relationship values](../mechanic/relationship-values.md): Free-text conversation can move relationship state in ways menu choices cannot enumerate.

## Backlinks (computed)

**affected by:** [Language models grounded in strategic planning for negotiation games](../technique/cicero-strategic-dialogue.md), [Grammar-constrained decoding for valid game actions](../technique/constrained-decoding.md), [Generalist instructable game agents (SIMA)](../technique/generalist-game-agents.md), [LLM game master and narrative director](../technique/llm-game-master.md), [On-device small language models for characters](../technique/on-device-language-models.md), [Realtime speech-to-speech and expressive TTS for characters](../technique/realtime-voice-models.md)

**involved in:** [Agent ambassadors between player worlds](../opportunity/agent-ambassadors-async.md), [Intent-level orders](../opportunity/intent-level-orders.md), [Local-first AI simulation games](../opportunity/local-first-ai-sims.md), [Natural-language legislation](../opportunity/natural-language-legislation.md), [Teachable sim companion](../opportunity/teachable-sim-companion.md), [Trainable creatures revival](../opportunity/trainable-creatures-revival.md)

**used by:** [AI Dungeon](../game/ai-dungeon.md), [Creatures](../game/creatures.md), [Façade](../game/facade.md), [Generative Agents (Smallville)](../game/generative-agents-smallville.md), [inZOI](../game/inzoi.md), [Little Computer People](../game/little-computer-people.md), [Nintendogs](../game/nintendogs.md), [Seaman](../game/seaman.md), [Suck Up!](../game/suck-up.md), [Where Winds Meet](../game/where-winds-meet.md), [Whispers from the Star](../game/whispers-from-the-star.md)

## Sources

- [Natural Language Understanding in Facade: Surface-text Processing](../source/src-mateas-2004-facade-nlu.md)
- [Façade (video game)](../source/src-wikipedia-facade.md)
- [AI Dungeon](../source/src-wikipedia-ai-dungeon.md)

---
Provenance: created in run `2026-10-24-taxonomy-m3`; reviewed in `2026-10-24-review-fixes`.
