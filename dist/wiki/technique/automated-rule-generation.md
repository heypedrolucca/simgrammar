# Automated generation of game rules and mechanics

*Technique* · `automated-rule-generation` · status: **sourced**

Systems that write complete game rule sets as code in a description language, using evolution or language models to propose rules and self-play agents to score balance, decisiveness, and strategic depth before a human sees them.

| field | value |
|---|---|
| aliases | Ludi, Ludii, GAVEL, VGDL generation, LLM rule generation |
| category | Automated game design & playtesting |
| year | 2024 |
| maturity | Prototype |
| trl | 5 |
| runtime | Offline authoring, Design assist |
| determinism impact | Preserves |
| horizon | 3-5 years |
| risks | Evaluation difficulty, Controllability, Labor displacement |
| builds on | [Quality-diversity search (MAP-Elites) for content and balance](../technique/quality-diversity-search.md), [Monte Carlo tree search for game AI](../technique/monte-carlo-tree-search.md) |
| affects count *(computed)* | 5 |

## Summary

Systems that write complete game rule sets as code in a description language, using evolution or language models to propose rules and self-play agents to score balance, decisiveness, and strategic depth before a human sees them.

## Mechanism

Rules are written in a game description language. Ludii describes a game as a tree of ludemes (board, pieces, moves, end conditions) that compiles to a playable game; VGDL describes sprites, interactions, and termination for 2D video games. A generator proposes new rule trees: Browne and Maire's system evolved them by crossover and mutation, while GAVEL fine-tunes CodeLlama-13b with a fill-in-the-middle objective on 574 Ludii games and uses it as the mutation operator in MAP-Elites: a span of an existing game's rule code is masked and the model writes a replacement, and the archive is indexed by a 2D PCA projection of 510 Ludii concept features (1,600 cells). Candidates pass hierarchical tests (compiles, is playable, random playouts are not trivially one-sided and offer real choices) and are then scored by MCTS self-play on balance, decisiveness, completion, agency, coverage, and strategic depth. LLM frameworks built on VGDL generate rules and levels together from prompts. The output is a set of verified candidate rule sets for designers to play and select.

## Limitations

- Generated rule sets are small abstract board games; GAVEL trained on 574 games after removing those over 1,024 tokens, far below the size of a simulation game's rule base.
- Self-play metrics such as balance, decisiveness, and agency describe agent play, not whether people enjoy the game, so human evaluation is still required.
- Every candidate needs compilation plus random and MCTS playouts, so the search is offline and compute-bound.
- Language models often emit rule code that fails to compile or is unplayable; GAVEL penalizes such candidates rather than preventing them.
- Simulation games rarely have a formal rule language like Ludii or VGDL, so applying this needs the game's systems exposed as data or a scripting layer the generator can edit.

## Relations

**affects**

- [Policy toggles](../mechanic/policy-toggles.md) (Enables new form): Candidate policies can be written as rule code in the game's own description language and screened by agent playouts for dominance and balance, so a policy list can be grown by search rather than authored one law at a time.
- [Player legislation](../mechanic/player-legislation.md) (Enables new form): Laws players propose could be translated by a code model into enforceable rule code and run through the same compile and playout tests GAVEL uses, rejecting laws that fail to compile or break play.
- [Turn structure](../mechanic/turn-structure.md) (Tunes / balances): Self-play over each generated variant measures first-player advantage, decisiveness, and the share of states with real choices, so turn order, phases, and move allowances can be adjusted by search.
- [Scenario objectives](../mechanic/scenario-objectives.md) (Cuts authoring cost): End conditions are generated together with the rules and kept only if MCTS play reaches them without trivial draws or one-sided wins, replacing hand-tuned victory thresholds.
- [Generative content on demand](../mechanic/generative-content.md) (Deepens): Generated content extends from text, items, and levels to complete executable rule sets that are compiled and filtered by playability and balance tests before anyone plays them.

**builds on**

- [Quality-diversity search (MAP-Elites) for content and balance](../technique/quality-diversity-search.md)
- [Monte Carlo tree search for game AI](../technique/monte-carlo-tree-search.md)

## Backlinks (computed)

**applied in:** [Generated inspection shifts](../opportunity/generated-inspection-shifts.md), [Generated recipe graphs](../opportunity/generated-recipe-graphs.md), [Mechanic modding by description](../opportunity/language-modding.md), [Automated mechanic discovery](../opportunity/mechanic-discovery-search.md), [Specification programming games](../opportunity/specification-programming-games.md)

## Claims

- Browne and Maire (IEEE TCIAIG 2010) evolved board game rule sets and ranked them with measures computed from self-play. *(confidence: medium)* [[110](../source/src-browne-2010-evolutionary-game-design.md)]
- Ludii describes games with high-level ludemes and outperformed a propositional-network GDL reasoner on all games in the Tiltyard repository. *(confidence: high)* [[111](../source/src-piette-2019-ludii.md)]
- GAVEL (2024) fine-tuned CodeLlama-13b (about 40 hours on one RTX8000) on 574 Ludii games as a MAP-Elites mutation operator and generated playable games in rule-space regions not covered by existing Ludii games, scored by MCTS self-play metrics; samples are playable on the Ludii portal. *(confidence: high)* [[112](../source/src-todd-2024-gavel.md)]
- An LLM framework built on VGDL generated game rules and levels together, extending LLM generation from levels for fixed games to whole games. *(confidence: medium)* [[113](../source/src-hu-2024-llm-game-generation-vgdl.md)]

## Sources

- [Evolutionary Game Design](../source/src-browne-2010-evolutionary-game-design.md)
- [Ludii -- The Ludemic General Game System](../source/src-piette-2019-ludii.md)
- [GAVEL: Generating Games Via Evolution and Language Models](../source/src-todd-2024-gavel.md)
- [Game Generation via Large Language Models](../source/src-hu-2024-llm-game-generation-vgdl.md)

---
Provenance: created in run `2026-10-24-techniques-rl-design`.
