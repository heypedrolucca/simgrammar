# llama.cpp GBNF grammar guide (grammars/README.md)

*Source* · `src-ggml-2026-llama-cpp-gbnf` · status: **n/a**

| field | value |
|---|---|
| kind | Code repository / dataset |
| authors | ggml-org |
| venue | GitHub |
| date | 2026 |
| url | https://github.com/ggml-org/llama.cpp/blob/master/grammars/README.md |
| accessed | 2026-10-24 |

## Notes

GBNF production rules constrain local model output; a JSON Schema subset converts to GBNF via json_schema or response_format. Caveats: known grammar performance problems, many optional items make sampling slow, unsupported schema features (nested $ref, patternProperties, uniqueItems, conditionals) are skipped silently.

## Backlinks (computed)

**cited by:** [Grammar-constrained decoding for valid game actions](../technique/constrained-decoding.md)

## Citation

ggml-org (2026). *llama.cpp GBNF grammar guide (grammars/README.md)*. GitHub https://github.com/ggml-org/llama.cpp/blob/master/grammars/README.md

---
Provenance: created in run `2026-10-24-techniques-llm-agents`.
