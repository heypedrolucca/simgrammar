# Local-first AI simulation games

*Opportunity* · `local-first-ai-sims` · status: **asserted**

Ship small language and generative models inside the game so AI features run offline with no per-hour inference bill, changing the economics of AI-native simulation.

| field | value |
|---|---|
| opportunity type | Business model |
| involves | [Natural-language interaction](../mechanic/natural-language-interaction.md), [Generative content on demand](../mechanic/generative-content.md), [Procedural characters](../mechanic/procedural-characters.md) |
| applies | [On-device small language models for characters](../technique/on-device-language-models.md), [Grammar-constrained decoding for valid game actions](../technique/constrained-decoding.md) |
| precedent | [inZOI](../game/inzoi.md), [Whispers from the Star](../game/whispers-from-the-star.md), [Suck Up!](../game/suck-up.md) |
| novelty | 2 |
| feasibility | 4 |
| impact | 4 |
| horizon | Now |
| key risks | Hardware minimums shrink the audience., Model quality gap versus cloud models., Download size and VRAM competition with rendering. |
| falsifiable signal | {'prediction': 'At least five Steam games with over 1,000 reviews will ship an on-device language model used at runtime without requiring an internet connection.', 'resolve_by': '2027-12-31', 'criteria': 'Store pages or documentation confirming local model inference for runtime features, and review counts over 1,000.'} |
| priority *(computed)* | 3.482 |

## Summary

Ship small language and generative models inside the game so AI features run offline with no per-hour inference bill, changing the economics of AI-native simulation.

## Thesis

Cloud inference makes AI features a variable cost per player-hour, which conflicts with the one-time-purchase model of most simulation games and their very long play sessions. Small models running on consumer GPUs and NPUs reached usable quality for constrained tasks in 2025 (inZOI's on-device characters are an example). Local-first design bounds cost, works offline, protects privacy, and survives the vendor's model deprecations.

## Design Sketch

The game ships a quantized model for dialogue, event generation, and explanation, with a schema-constrained interface. Higher-quality cloud calls are optional and clearly metered. Mods can swap models.

## Key Risks

- Hardware minimums shrink the audience.
- Model quality gap versus cloud models.
- Download size and VRAM competition with rendering.

## Validation Experiment

Benchmark a 1 to 4 billion parameter quantized model on the median Steam hardware survey GPU for schema-constrained NPC dialogue, measuring latency, VRAM, and frame-time impact. Success: under 500 ms first token with less than 10 percent frame-time impact.

## Falsifiable signal

- **Prediction:** At least five Steam games with over 1,000 reviews will ship an on-device language model used at runtime without requiring an internet connection.
- **Resolve by:** 2027-12-31
- **Criteria:** Store pages or documentation confirming local model inference for runtime features, and review counts over 1,000.

## Relations

**applies**

- [On-device small language models for characters](../technique/on-device-language-models.md)
- [Grammar-constrained decoding for valid game actions](../technique/constrained-decoding.md)

**involves**

- [Natural-language interaction](../mechanic/natural-language-interaction.md)
- [Generative content on demand](../mechanic/generative-content.md)
- [Procedural characters](../mechanic/procedural-characters.md)

**precedent**

- [inZOI](../game/inzoi.md)
- [Whispers from the Star](../game/whispers-from-the-star.md)
- [Suck Up!](../game/suck-up.md)

---
Provenance: created in run `2026-10-24-synthesis`.
