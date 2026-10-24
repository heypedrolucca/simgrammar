# Infinite Craft

*Game* · `infinite-craft` · status: **sourced**

A browser crafting game in which combining any two elements yields a new element whose name and emoji a language model generates on first request and a shared database then fixes for all players.

| field | value |
|---|---|
| year | 2024 |
| developer | Neal Agarwal |
| platforms | Web, Mobile |
| subgenre | AI-native |
| sim domain | Computational / abstract |
| player role | Engineer / designer |
| agency model | Design then test |
| time model | Turn-based |
| sim scale | Individual |
| fidelity | Abstract |
| perspective | Text / UI |
| win structure | Open sandbox |
| failure model | None |
| narrative mode | None |
| multiplayer | Single-player, Async / shared content |
| modding | None |
| production tier | Hobbyist / free |
| agent count order | None |
| emergence | 2 |
| influence | 1 |
| boundary case | True |
| cluster *(computed)* | C09 |
| core count *(computed)* | 2 |
| mechanic count *(computed)* | 3 |

## Summary

A browser crafting game in which combining any two elements yields a new element whose name and emoji a language model generates on first request and a shared database then fixes for all players.

## Core Loop

start with water, fire, wind, and earth -> drag two elements together -> look up the pair in the shared database -> if new, a language model names the result and picks an emoji -> result is cached for everyone -> combine the new element further

## Design Notes

At runtime the model is consulted only on a cache miss: the game checks a global database for the unordered pair, and if no result exists, Llama 2 (later Llama 3.1) generates a short element name, capped at twenty tokens, plus an emoji; the result is stored so the same pair returns the same element to every player. The recipe graph is therefore written collectively and lazily by players and the model, and a First Discovery label marks players who triggered a generation. Pairwise combination discovery is not yet a mechanic in the taxonomy (proposal combination-discovery). It is a boundary case: there is no simulated system beyond the generated recipe graph.

## Relations

**uses**

- [Generative content on demand](../mechanic/generative-content.md) (core): On a cache miss, a Llama model generates the combined element's name (up to twenty tokens) and emoji; the result is written to a shared database so later requests are deterministic.
- [Collection goals](../mechanic/collection-goals.md) (supporting): Players accumulate discovered elements and First Discoveries, which mark elements no player had made before.
- [Combination discovery](../mechanic/combination-discovery.md) (core): Every action combines two owned elements; on a cache miss a Llama model names the result, the result is stored so every player gets the same answer, and new results earn a First Discovery label.

## Backlinks (computed)

**deploys:** [LLM-adjudicated state transitions (LLM as game mechanic)](../technique/llm-rule-adjudication.md)

## Sources

- [Infinite Craft](../source/src-wikipedia-infinite-craft.md)

---
Provenance: created in run `2026-10-24-catalog-gd`.
