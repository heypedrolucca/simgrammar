# Realtime speech-to-speech and expressive TTS for characters

*Technique* · `realtime-voice-models` · status: **sourced**

Streaming speech recognition, speech-native language models, and context-aware text-to-speech that let characters hold spoken, interruptible conversations with roughly 200-250 ms response onset and generated emotional delivery.

| field | value |
|---|---|
| aliases | speech-to-speech, full-duplex dialogue, Realtime API, Moshi, expressive TTS, AI NPC voices |
| category | Speech & audio |
| year | 2024 |
| maturity | Shipped (niche) |
| trl | 8 |
| runtime | Server real-time, Client real-time |
| determinism impact | Breaks |
| horizon | Now |
| risks | Determinism, Compute cost, Latency, Labor displacement, Player trust / reception, Content safety |
| builds on |  |
| deployed in | [Whispers from the Star](../game/whispers-from-the-star.md), [Where Winds Meet](../game/where-winds-meet.md) |
| affects count *(computed)* | 4 |

## Summary

Streaming speech recognition, speech-native language models, and context-aware text-to-speech that let characters hold spoken, interruptible conversations with roughly 200-250 ms response onset and generated emotional delivery.

## Mechanism

Two pipelines. Cascaded: streaming speech recognition, then an LLM, then streaming TTS, each optimized for time to first output. Speech-native: the model reads and writes audio tokens from a neural codec. Moshi models the user's and its own speech as parallel streams (full duplex, so it can listen while speaking) and predicts time-aligned text tokens before audio tokens. Hosted realtime APIs keep a persistent WebSocket session with voice activity detection, interruption handling, and function calls that can trigger game actions. Expressive TTS conditions delivery on context: Sesame's CSM feeds prior conversation audio and text to a Llama-style backbone over codec tokens, and Eleven v3 accepts inline tags such as [whispers] or [sighs]. Small ASR and TTS models (hundreds of millions of parameters) can run on device.

## Limitations

- Cost scales with talk time: at 2024 Realtime API rates, an hour split evenly between player and NPC speech is roughly $9 before context re-reads; gpt-realtime rates cut that to roughly $3 (estimates derived from list prices).
- Expressive delivery and low latency trade off: context-conditioned prosody still trails humans, and the most expressive TTS was not suited to real time at launch.
- Voice actor consent and compensation are now contract terms, and players have penalized AI voices in reviews.
- Speech-native models are hard to constrain to game-legal actions; most games keep a text layer between speech and game state.
- Microphone use and online connectivity raise privacy and access barriers (Whispers from the Star lists a broadband connection and an account).

## Sources

- src-defossez-2024-moshi
- src-openai-2024-realtime-api
- src-openai-2025-gpt-realtime
- src-sesame-2025-csm
- src-elevenlabs-2025-eleven-v3
- src-inworld-2026-tts-1-5
- src-inworld-2026-consumer-ai-cost
- src-inworld-2025-death-by-ai
- src-steam-2026-whispers-from-the-star
- src-steam-2025-where-winds-meet
- src-wikipedia-artificial-intelligence-in-video-games
- src-krafton-2026-pubg-ally-beta
- src-gdc-2026-state-of-industry
- src-gdc-2025-state-of-industry

## Relations

**affects**

- [Natural-language interaction](../mechanic/natural-language-interaction.md) (Enables new form): Characters can hold spoken, interruptible, full-duplex conversations with response onset near human turn-taking, replacing dialogue wheels or typed input; Whispers from the Star is built around this loop.
- [Social exchanges](../mechanic/social-exchanges.md) (Deepens): Delivery carries social meaning (whispering, sighing, hesitation, warmth) generated from conversational context, so the same line can land as a flirt, apology, or threat.
- [Unit commands](../mechanic/unit-commands.md) (Deepens): Squad orders can be spoken mid-action and parsed into function calls, as in PUBG Ally's voice-directed teammate, without menus.
- [Procedural characters](../mechanic/procedural-characters.md) (Cuts authoring cost): Generated characters can get distinct designed or cloned voices and speak unscripted lines without recording sessions, which removes the voice-acting cost that keeps procedural characters silent.

**deployed in**

- [Whispers from the Star](../game/whispers-from-the-star.md)
- [Where Winds Meet](../game/where-winds-meet.md)

## Backlinks (computed)

**applied in:** [Simulator instructor coaching](../opportunity/sim-instructor-coach.md)

## Claims

- Moshi reported 160 ms theoretical and 200 ms practical latency for full-duplex spoken dialogue. *(confidence: high)* [[276](../source/src-defossez-2024-moshi.md)]
- OpenAI's Realtime API launched in October 2024 at about $0.06 per minute of audio input and $0.24 per minute of output; gpt-realtime (August 2025) priced audio at $32 and $64 per million input and output tokens and raised function-calling accuracy on ComplexFuncBench from 49.7% to 66.5%. *(confidence: high)* [[277](../source/src-openai-2024-realtime-api.md), [278](../source/src-openai-2025-gpt-realtime.md)]
- Sesame's CSM reached parity with human recordings in listener preference without conversational context, but listeners preferred the human recordings when 90 seconds of prior context was provided. *(confidence: high)* [[279](../source/src-sesame-2025-csm.md)]
- Inworld's TTS-1.5 (January 2026) lists P90 time to first audio under 130 ms (Mini) and under 250 ms (Max) at $15 and $25 per million characters, about $0.015-0.025 per minute of speech. *(confidence: medium)* [[280](../source/src-inworld-2026-tts-1-5.md)]
- Whispers from the Star (August 2025) is built around open-ended voice, video-call, and text conversation with an AI-voiced character created with an actor, and Where Winds Meet (global November 2025) discloses real-time AI NPC text and voice chat. *(confidence: high)* [[281](../source/src-steam-2026-whispers-from-the-star.md), [50](../source/src-steam-2025-where-winds-meet.md)]
- ARC Raiders (November 2025) was criticized and marked down by Eurogamer for generative AI NPC voices, and the SAG-AFTRA video game strike (July 2024 to July 2025) ended with contract terms on consent for AI voice replicas. *(confidence: medium)* [[282](../source/src-wikipedia-artificial-intelligence-in-video-games.md)]
- Eleven v3's expressive model was not recommended for real-time conversation at launch because of latency and reliability, so expressive range and low latency were still traded off in mid-2025. *(confidence: high)* [[283](../source/src-elevenlabs-2025-eleven-v3.md)]
- A vendor case study reports Death by AI reached 20 million players in three months with 1.2 billion tokens in its first month after moving LLM and TTS to a gaming-priced provider; the cost claims are unverified. *(confidence: low)* [[284](../source/src-inworld-2025-death-by-ai.md)]
- Inworld's June 2026 price list puts streaming TTS at about $5-25 per million characters and speech-to-text at about $0.10 per hour, and claims only about 3 in 100 consumer AI users ever pay. *(confidence: low)* [[285](../source/src-inworld-2026-consumer-ai-cost.md)]
- In GDC's 2026 survey of over 2,300 professionals, 36% used generative AI at work but 52% thought it was harming the industry, up from 30% in 2025, with game design and narrative (63%) and art (64%) among the most negative groups, which bears on adoption of generated character voices and dialogue. *(confidence: high)* [[286](../source/src-gdc-2026-state-of-industry.md), [287](../source/src-gdc-2025-state-of-industry.md)]

## Sources

- [Moshi: a speech-text foundation model for real-time dialogue](../source/src-defossez-2024-moshi.md)
- [Introducing the Realtime API](../source/src-openai-2024-realtime-api.md)
- [Introducing gpt-realtime](../source/src-openai-2025-gpt-realtime.md)
- [Crossing the uncanny valley of conversational voice](../source/src-sesame-2025-csm.md)
- [Eleven v3 (alpha) announcement](../source/src-elevenlabs-2025-eleven-v3.md)
- [Inworld TTS-1.5: Upgrading the #1 Ranked TTS Model with Production-Grade Latency, Expression and Stability](../source/src-inworld-2026-tts-1-5.md)
- [Cost is the wall in front of consumer AI. We are taking it down.](../source/src-inworld-2026-consumer-ai-cost.md)
- [How Inworld helped an AI game with 20 million players reach profitability](../source/src-inworld-2025-death-by-ai.md)
- [Whispers from the Star on Steam](../source/src-steam-2026-whispers-from-the-star.md)
- [Where Winds Meet on Steam](../source/src-steam-2025-where-winds-meet.md)
- [Artificial intelligence in video games](../source/src-wikipedia-artificial-intelligence-in-video-games.md)
- [KRAFTON Introduces PUBG Ally Beta Test](../source/src-krafton-2026-pubg-ally-beta.md)
- [GDC 2026 State of the Game Industry reveals impact of layoffs, generative AI, and more](../source/src-gdc-2026-state-of-industry.md)
- [GDC 2025 State of the Game Industry: Devs weigh in on layoffs, AI, and more](../source/src-gdc-2025-state-of-industry.md)

---
Provenance: created in run `2026-10-24-techniques-llm-agents`; reviewed in `2026-10-24-review-fixes`.
