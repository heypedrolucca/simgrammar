# Whispers from the Star

*Game* · `whispers-from-the-star` · status: **sourced**

A voice-driven sci-fi narrative game in which the player helps stranded astronaut Stella survive on the planet Gaia through open-ended spoken or typed conversation answered by an AI-generated, voiced performance.

| field | value |
|---|---|
| year | 2025 |
| developer | Anuttacon |
| platforms | PC |
| subgenre | AI-native |
| subgenre secondary | Social sim |
| sim domain | Social / interpersonal |
| player role | Overseer |
| agency model | Conversational, Indirect incentive |
| time model | Real-time |
| sim scale | Individual |
| fidelity | Stylized |
| perspective | Third-person |
| win structure | Campaign |
| failure model | Hard restart |
| narrative mode | Generative |
| multiplayer | Single-player |
| modding | None |
| production tier | AA |
| agent count order | ~1 |
| emergence | 2 |
| influence | 1 |
| boundary case | True |
| cluster *(computed)* | C09 |
| core count *(computed)* | 2 |
| mechanic count *(computed)* | 3 |

## Summary

A voice-driven sci-fi narrative game in which the player helps stranded astronaut Stella survive on the planet Gaia through open-ended spoken or typed conversation answered by an AI-generated, voiced performance.

## Core Loop

Stella calls, texts, or sends voice messages about her situation -> player answers by voice or text -> model generates her spoken reply and choice -> her choices change whether she survives the situation -> story advances

## Design Notes

At runtime a model generates Stella's side of every exchange: the player's microphone or text input is answered with dialogue and a fully voiced performance that Anuttacon says was created in collaboration with an actor, with safety filters screening output. The store page says there is no script and that the player's words shape her choices and her survival, so advice acts as an indirect control on an agent the player cannot command. The surrounding structure is linear and story-driven per its store tags, which makes it a hybrid of authored situations and generated conversation. Anuttacon was formed in late 2023 by miHoYo co-founder Cai Haoyu, and this is its first game. It is a boundary case: the only simulated state is the conversation and Stella's choices.

## Relations

**uses**

- [Natural-language interaction](../mechanic/natural-language-interaction.md) (core): Open-ended conversation by voice (a microphone is required for the full experience) or text over Stella's communicator, through video calls, voice messages, and texts.
- [Generative content on demand](../mechanic/generative-content.md) (core): An AI model generates Stella's dialogue and voiced performance in real time, constrained by safety filters, and her in-story decisions follow from what the player says.
- [Triggered event chains](../mechanic/triggered-event-chains.md) (supporting): The store tags the game as linear and story-rich, so generated conversation plays out inside a sequence of survival situations.

## Backlinks (computed)

**deploys:** [Realtime speech-to-speech and expressive TTS for characters](../technique/realtime-voice-models.md)

**precedent for:** [Local-first AI simulation games](../opportunity/local-first-ai-sims.md)

## Claims

- Anuttacon, the developer, was formed in late 2023 by Cai Haoyu, and Whispers from the Star is its first game. *(confidence: medium)* [[51](../source/src-wikipedia-cai-haoyu.md)]

## Sources

- [Whispers from the Star on Steam](../source/src-steam-2026-whispers-from-the-star.md)
- [Cai Haoyu](../source/src-wikipedia-cai-haoyu.md)

---
Provenance: created in run `2026-10-24-catalog-gd`.
