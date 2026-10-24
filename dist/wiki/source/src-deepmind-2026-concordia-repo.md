# Concordia: a library for generative social simulation

*Source* · `src-deepmind-2026-concordia-repo` · status: **n/a**

| field | value |
|---|---|
| kind | Code repository / dataset |
| authors | Google DeepMind |
| venue | GitHub |
| date | 2026 |
| url | https://github.com/google-deepmind/concordia |
| accessed | 2026-10-24 |

## Notes

Apache-2.0. Entities (player agents and Game Masters), components, and an engine loop. LanguageModel interface defines sample_text and sample_choice; sample_choice scores a list of candidate responses and returns the chosen index, raising InvalidResponseError after several failed attempts. Requires a text embedder for associative memory.

## Backlinks (computed)

**cited by:** [Grammar-constrained decoding for valid game actions](../technique/constrained-decoding.md), [LLM game master and narrative director](../technique/llm-game-master.md)

## Citation

Google DeepMind (2026). *Concordia: a library for generative social simulation*. GitHub https://github.com/google-deepmind/concordia

---
Provenance: created in run `2026-10-24-techniques-llm-agents`.
