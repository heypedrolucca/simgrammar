# AI Dungeon

*Game* · `ai-dungeon` · status: **sourced**

A text adventure in which a large language model continues the story after each player input, so actions, dialogue, and world facts the player types are improvised into narration rather than resolved by authored rules.

| field | value |
|---|---|
| aliases | AI Dungeon 2 |
| year | 2019 |
| developer | Latitude |
| platforms | Web, Mobile, PC |
| subgenre | AI-native |
| sim domain | Social / interpersonal |
| player role | Inhabitant |
| agency model | Conversational |
| time model | Turn-based |
| sim scale | Individual |
| fidelity | Abstract |
| perspective | Text / UI |
| win structure | Open sandbox |
| failure model | None |
| narrative mode | Generative |
| multiplayer | Single-player, Co-op, Async / shared content |
| modding | Content |
| production tier | Indie |
| agent count order | None |
| emergence | 2 |
| influence | 3 |
| boundary case | True |
| cluster *(computed)* | C09 |
| core count *(computed)* | 2 |
| mechanic count *(computed)* | 4 |

## Summary

A text adventure in which a large language model continues the story after each player input, so actions, dialogue, and world facts the player types are improvised into narration rather than resolved by authored rules.

## Core Loop

choose a setting -> type a Do, Say, or Story input -> model continues the text from recent story and pinned memory -> player undoes, retries, or edits the output -> next input

## Design Notes

At runtime the model does all the work: each turn, the game assembles a prompt from the scenario premise, player-pinned memory, and recent story text, and a language model (GPT-2 with 1.5 billion parameters in AI Dungeon 2, GPT-3 through OpenAI's API for the premium Dragon model from July 2020) generates the next passage. There is no separate world state, inventory, or rules engine, so consistency lasts only as long as facts stay in the context window, and undo, retry, and edit are the player's tools for steering. Nick Walton built the first version at a BYU hackathon on a 126-million-parameter GPT-2 and released it in May 2019; Latitude relaunched it in December 2019. It is a boundary case: no system is simulated outside the model's text.

## Relations

**uses**

- [Generative content on demand](../mechanic/generative-content.md) (core): A language model continues the story text from a prompt of scenario, pinned memory, and recent turns; the See input generates an image that does not change play.
- [Natural-language interaction](../mechanic/natural-language-interaction.md) (core): Free-text input typed as Do (action), Say (dialogue), or Story (narration or facts), with blank input asking the model to continue.
- [Content sharing](../mechanic/content-sharing.md) (supporting): Players publish custom adventures and scenarios that others can start from.
- [Turn structure](../mechanic/turn-structure.md) (supporting): Play alternates player input and model output; multiplayer (from April 2020) rotates turns among players' characters while the host can edit model output.

## Backlinks (computed)

**deploys:** [LLM game master and narrative director](../technique/llm-game-master.md)

## Sources

- [AI Dungeon](../source/src-wikipedia-ai-dungeon.md)

---
Provenance: created in run `2026-10-24-catalog-gd`.
