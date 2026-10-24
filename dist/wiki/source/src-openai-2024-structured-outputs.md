# Introducing Structured Outputs in the API

*Source* · `src-openai-2024-structured-outputs` · status: **n/a**

| field | value |
|---|---|
| kind | Technical report / blog |
| authors | OpenAI |
| venue | OpenAI blog |
| date | 2024-08-06 |
| url | https://openai.com/index/introducing-structured-outputs-in-the-api/ |
| accessed | 2026-10-24 |

## Notes

JSON Schema converted to a CFG; invalid tokens masked each step; gpt-4o-2024-08-06 scored 100% on complex schema following vs under 40% for gpt-4-0613. Limits: JSON Schema subset; first request with a new schema adds latency (under 10 s, up to a minute); max_tokens can still break output; values can be wrong.

## Backlinks (computed)

**cited by:** [Grammar-constrained decoding for valid game actions](../technique/constrained-decoding.md)

## Citation

OpenAI (2024-08-06). *Introducing Structured Outputs in the API*. OpenAI blog https://openai.com/index/introducing-structured-outputs-in-the-api/

---
Provenance: created in run `2026-10-24-techniques-llm-agents`.
