# LLM-guided evolutionary program search

*Technique* · `alphaevolve-algorithm-discovery` · status: **sourced**

An LLM proposes edits to code, an automated evaluator scores each candidate, and an evolutionary database keeps the best and most diverse programs, finding heuristics and constructions that beat human-designed ones.

| field | value |
|---|---|
| aliases | AlphaEvolve, FunSearch, OpenEvolve, ShinkaEvolve, evolutionary coding agents |
| category | Mathematical & algorithmic discovery |
| year | 2025 |
| maturity | Research |
| trl | 3 |
| runtime | Offline authoring, Design assist |
| determinism impact | Preserves |
| horizon | 1-2 years |
| risks | Evaluation difficulty, Compute cost |
| deployed in |  |
| affects count *(computed)* | 6 |

## Summary

An LLM proposes edits to code, an automated evaluator scores each candidate, and an evolutionary database keeps the best and most diverse programs, finding heuristics and constructions that beat human-designed ones.

## Mechanism

A human supplies a program skeleton, the part to evolve (one priority function in FunSearch; arbitrary blocks across a file in AlphaEvolve), and an evaluator that runs a candidate and returns scores. A programs database holds evaluated programs; samplers build prompts from high-scoring and diverse parents and ask an LLM for a modified program; evaluators execute and score it; results flow back into the database. Diversity is kept with island populations (FunSearch) or MAP-Elites grids (OpenEvolve). Samplers and evaluators run asynchronously in parallel. The output is readable source code, so a discovered heuristic can be inspected, tested and shipped like hand-written code.

## Limitations

- Requires a fast, automatic, trustworthy evaluator; anything judged by taste or fun has no such evaluator, and evolved code overfits whatever the evaluator measures.
- Each run consumes thousands of LLM samples and program executions in earlier systems; ShinkaEvolve's roughly 150-sample result shows efficiency varies widely by problem.
- Evolved heuristics are tuned to the benchmark instances and must be re-validated on new maps, content or patches.
- No game studio use was found in this run's sources; all cited results are in mathematics, scheduling and systems code.

## Sources

- src-romeraparedes-2023-funsearch
- src-deepmind-2025-alphaevolve-blog
- src-novikov-2025-alphaevolve
- src-georgiev-2025-math-discovery-at-scale
- src-lange-2025-shinkaevolve
- src-sharma-2025-openevolve

## Relations

**affects**

- [Agent pathfinding](../mechanic/agent-pathfinding.md) (Accelerates): Path cost heuristics or search-ordering functions can be evolved against a benchmark of the game's own maps for fewer node expansions at equal route quality, as FunSearch evolved priority functions.
- [Hauling jobs](../mechanic/hauling-jobs.md) (Tunes / balances): Job-to-hauler assignment is a scheduling problem like the Borg case; the dispatch heuristic can be evolved against simulated throughput and idle time on recorded colony states.
- [Vehicle routes and schedules](../mechanic/vehicle-route-scheduling.md) (Tunes / balances): Automatic load and stop-ordering heuristics resemble the bin-packing heuristics FunSearch improved, and can be evolved against delivery-rate benchmarks.
- [Utility action selection](../mechanic/utility-action-selection.md) (Tunes / balances): Utility scoring functions can be evolved as code against designer metrics (survival, need satisfaction, behavior variety), keeping the result readable unlike a neural policy.
- [Comparative histograms](../mechanic/comparative-histograms.md) (Tunes / balances): Evolving solutions to each puzzle before launch estimates near-optimal cost, cycle or area scores, anchoring histogram axes and flagging degenerate puzzles.
- [Player programming](../mechanic/player-programming.md) (Enables new form): Rivals or coaches could evolve programs in the game's own language against its evaluator, so player-written code competes with machine-evolved code under the same rules.

## Backlinks (computed)

**applied in:** [Generated recipe graphs](../opportunity/generated-recipe-graphs.md), [Automated mechanic discovery](../opportunity/mechanic-discovery-search.md), [Specification programming games](../opportunity/specification-programming-games.md)

## Claims

- FunSearch found a cap set of size 512 in dimension 8 and online bin-packing heuristics that beat first fit and best fit on benchmark distributions. *(confidence: high)* [[192](../source/src-romeraparedes-2023-funsearch.md)]
- AlphaEvolve found a 4x4 complex matrix multiplication with 48 scalar multiplications, matched about 75% and improved about 20% of over 50 open math problems, and produced a Borg scheduling heuristic that has recovered about 0.7% of Google's fleet compute in production for over a year. *(confidence: high)* [[193](../source/src-deepmind-2025-alphaevolve-blog.md), [194](../source/src-novikov-2025-alphaevolve.md)]
- Applied by Georgiev, Gomez-Serrano, Tao and Wagner to 67 problems, AlphaEvolve mostly rediscovered the best known constructions, improved several, and sometimes generalized finite results into formulas. *(confidence: high)* [[195](../source/src-georgiev-2025-math-discovery-at-scale.md)]
- Open-source successors lowered the barrier: ShinkaEvolve reported a new state-of-the-art circle packing with about 150 samples, and OpenEvolve runs the loop with any OpenAI-compatible or local model under Apache-2.0. *(confidence: medium)* [[196](../source/src-lange-2025-shinkaevolve.md), [197](../source/src-sharma-2025-openevolve.md)]

## Sources

- [Mathematical discoveries from program search with large language models](../source/src-romeraparedes-2023-funsearch.md)
- [AlphaEvolve: A Gemini-powered coding agent for designing advanced algorithms](../source/src-deepmind-2025-alphaevolve-blog.md)
- [AlphaEvolve: A coding agent for scientific and algorithmic discovery](../source/src-novikov-2025-alphaevolve.md)
- [Mathematical exploration and discovery at scale](../source/src-georgiev-2025-math-discovery-at-scale.md)
- [ShinkaEvolve: Towards Open-Ended And Sample-Efficient Program Evolution](../source/src-lange-2025-shinkaevolve.md)
- [OpenEvolve: open-source implementation of AlphaEvolve](../source/src-sharma-2025-openevolve.md)

---
Provenance: created in run `2026-10-24-techniques-sim-math`.
