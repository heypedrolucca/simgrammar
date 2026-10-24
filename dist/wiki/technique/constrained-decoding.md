# Grammar-constrained decoding for valid game actions

*Technique* · `constrained-decoding` · status: **sourced**

Decoding that masks every token which cannot extend a valid string of a schema, regular expression, or grammar, so a model's output always parses as a legal game action or data record.

| field | value |
|---|---|
| aliases | structured outputs, JSON mode, grammar-guided generation, GBNF, Outlines, XGrammar |
| category | LLM agents |
| year | 2024 |
| maturity | Research |
| trl | 4 |
| runtime | Server real-time, Client real-time, Design assist |
| determinism impact | Mitigable |
| horizon | Now |
| risks | Consistency / hallucination, Latency, Evaluation difficulty |
| builds on |  |
| deployed in |  |
| affects count *(computed)* | 5 |

## Summary

Decoding that masks every token which cannot extend a valid string of a schema, regular expression, or grammar, so a model's output always parses as a legal game action or data record.

## Mechanism

The output format (a JSON Schema, regular expression, or context-free grammar) is compiled into an automaton. At each decoding step the engine computes which vocabulary tokens keep the partial output a valid prefix and sets the logits of all others to minus infinity before sampling. Outlines precomputes an index from finite-state-machine states to allowed tokens; XGrammar handles full CFGs by prechecking context-independent tokens and checking context-dependent ones with a persistent stack, overlapping grammar work with GPU execution; hosted APIs convert schemas to CFGs and cache them; llama.cpp accepts GBNF grammars for local models. For games, the schema is built from current state: an enum of legal verbs, target ids that exist, and numeric fields with bounds, so every output maps to an action the engine can execute. A simpler variant scores a fixed list of candidate actions and returns the chosen index.

## Limitations

- Validity is not correctness: a well-formed action can still be the wrong action or reference stale state, so engines must re-check preconditions.
- Format constraints can lower reasoning quality; a common workaround is free-form reasoning followed by a constrained final answer, which costs tokens.
- Schema coverage varies: hosted APIs support a JSON Schema subset, and llama.cpp silently skips unsupported features such as nested $ref and uniqueItems and slows down with many optional items.
- First use of a new schema adds compile latency (OpenAI reports under 10 seconds, up to a minute), so per-turn dynamic schemas need caching.
- Output can still fail validation if generation hits a token limit.

## Sources

- src-willard-2023-outlines
- src-dong-2024-xgrammar
- src-openai-2024-structured-outputs
- src-tam-2024-let-me-speak-freely
- src-geng-2025-jsonschemabench
- src-ggml-2026-llama-cpp-gbnf
- src-deepmind-2026-concordia-repo

## Relations

**affects**

- [Generative content on demand](../mechanic/generative-content.md) (Enables new form): Generated items, recipes, or characters can be written straight into typed game state (enum types, bounded stats, existing ids) instead of shown as text or parsed with retries, because invalid records cannot be emitted.
- [Natural-language interaction](../mechanic/natural-language-interaction.md) (Deepens): Free player text can be mapped onto the closed set of verbs and target ids legal in the current state, so conversation reliably triggers real game actions rather than only replies.
- [Utility action selection](../mechanic/utility-action-selection.md) (Replaces substrate): An LLM can be dropped into the action-selection slot by constraining it to choose among the same enumerated actions the utility scorer would rank, keeping the engine's action set and preconditions intact.
- [Dilemma cards](../mechanic/dilemma-cards.md) (Cuts authoring cost): Card prompts, two to four options, and per-meter effect values can be generated in the game's card schema with effect sizes bounded by the grammar, leaving designers to curate rather than write.
- [Player legislation](../mechanic/player-legislation.md) (Enables new form): Laws proposed in plain language can be compiled into the world's structured condition-and-effect rule language by grammar-constrained generation, so players need not learn the rule editor.

## Backlinks (computed)

**applied in:** [Agent ambassadors between player worlds](../opportunity/agent-ambassadors-async.md), [Bottleneck explainer for production networks](../opportunity/bottleneck-explainer.md), [Why-query over the simulation log](../opportunity/causal-why-query.md), [Content-elastic event systems](../opportunity/content-elastic-events.md), [Drama-aware storyteller](../opportunity/drama-aware-storyteller.md), [Event-sourced simulation runtime](../opportunity/event-sourced-sim-runtime.md), [Generated inspection shifts](../opportunity/generated-inspection-shifts.md), [Generative decoration catalogs](../opportunity/generative-decoration-catalogs.md), [Intent-level orders](../opportunity/intent-level-orders.md), [Mechanic modding by description](../opportunity/language-modding.md), [Local-first AI simulation games](../opportunity/local-first-ai-sims.md), [Natural-language legislation](../opportunity/natural-language-legislation.md), [Negotiating faction AI](../opportunity/negotiating-faction-ai.md), [Placement that tells stories](../opportunity/placement-that-tells-stories.md), [Salience-gated language agents](../opportunity/salience-gated-llm-agents.md), [Specification programming games](../opportunity/specification-programming-games.md)

## Claims

- OpenAI's Structured Outputs (August 2024) reached 100% on a complex JSON-schema-following eval with gpt-4o-2024-08-06, versus under 40% for gpt-4-0613 without constraints. *(confidence: high)* [[145](../source/src-openai-2024-structured-outputs.md)]
- XGrammar reports up to 100x faster grammar-constrained generation than prior engines and near-zero end-to-end overhead when integrated with an inference server. *(confidence: medium)* [[146](../source/src-dong-2024-xgrammar.md)]
- Outlines showed that regex and CFG guidance can be implemented as finite-state-machine transitions with a precomputed vocabulary index and little per-token overhead. *(confidence: high)* [[147](../source/src-willard-2023-outlines.md)]
- Strict format restrictions such as JSON or XML significantly reduced LLM reasoning accuracy compared with free-form answers, with stricter formats causing larger drops. *(confidence: medium)* [[148](../source/src-tam-2024-let-me-speak-freely.md)]
- Concordia's language-model interface includes a sample_choice call that scores a list of candidate responses and returns an index, raising an error after repeated invalid attempts, which is how its agents pick from closed option sets. *(confidence: high)* [[149](../source/src-deepmind-2026-concordia-repo.md)]
- No source found documents constrained decoding in a specific shipped game; adoption in games is inferred from engine support (llama.cpp GBNF, hosted APIs) rather than observed. *(confidence: low)* [[150](../source/src-ggml-2026-llama-cpp-gbnf.md), [151](../source/src-geng-2025-jsonschemabench.md)]

## Sources

- [Efficient Guided Generation for Large Language Models](../source/src-willard-2023-outlines.md)
- [XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models](../source/src-dong-2024-xgrammar.md)
- [Introducing Structured Outputs in the API](../source/src-openai-2024-structured-outputs.md)
- [Let Me Speak Freely? A Study on the Impact of Format Restrictions on Performance of Large Language Models](../source/src-tam-2024-let-me-speak-freely.md)
- [JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models](../source/src-geng-2025-jsonschemabench.md)
- [llama.cpp GBNF grammar guide (grammars/README.md)](../source/src-ggml-2026-llama-cpp-gbnf.md)
- [Concordia: a library for generative social simulation](../source/src-deepmind-2026-concordia-repo.md)

---
Provenance: created in run `2026-10-24-techniques-llm-agents`.
