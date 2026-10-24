# Quality-diversity search (MAP-Elites) for content and balance

*Technique* · `quality-diversity-search` · status: **sourced**

Evolutionary search that keeps the best solution found in each cell of a grid of designer-chosen behavior descriptors, returning an archive of diverse high-quality levels, decks, or strategies instead of one optimum.

| field | value |
|---|---|
| aliases | MAP-Elites, CMA-ME, MESB, DSAGE, QDAIF, illumination search |
| category | Procedural content generation |
| year | 2015 |
| maturity | Research |
| trl | 4 |
| runtime | Offline authoring, Design assist |
| determinism impact | Preserves |
| horizon | Now |
| risks | Evaluation difficulty, Compute cost |
| affects count *(computed)* | 6 |

## Summary

Evolutionary search that keeps the best solution found in each cell of a grid of designer-chosen behavior descriptors, returning an archive of diverse high-quality levels, decks, or strategies instead of one optimum.

## Mechanism

The designer picks k behavior descriptors (for a level: enemy count and number of jumps; for a deck: mean mana cost and minion count) and discretizes them into a grid. Each cell stores the highest-fitness solution seen with those descriptor values. Each iteration selects elites from the archive, mutates or recombines them, evaluates the child's fitness and descriptors (usually by simulation or an agent playthrough), and inserts it if its cell is empty or it beats the incumbent. The archive shows which trait combinations can be good and how good. Variants slide cell boundaries to follow where solutions cluster (MESB), search a generative model's latent space with CMA-ES emitters (CMA-ME on a Mario GAN), use a learned surrogate to predict agent behavior and skip simulations (DSAGE), or use language models both to propose variations and to judge quality and diversity (QDAIF). GAVEL applies MAP-Elites to game rule sets.

## Limitations

- Every candidate needs a fitness and descriptor evaluation, usually a simulated playthrough, so large archives cost many simulations; surrogate methods such as DSAGE exist to cut that cost.
- Results depend on the chosen descriptors: poor choices give diversity along axes players do not perceive, and the grid grows exponentially with the number of descriptors.
- Fitness measured with AI agents reflects agent skill, not human experience, so cells marked playable or balanced may not match player perception.
- Game applications in the cited work are research prototypes on small games (Mario levels, Hearthstone decks); no documented shipped use in a simulation game was found in this run.

## Sources

- src-mouret-2015-map-elites
- src-gravina-2019-pcg-quality-diversity
- src-fontaine-2019-hearthstone-mesb
- src-fontaine-2020-mario-gan-qd
- src-bhatt-2022-dsage
- src-bradley-2023-qdaif

## Relations

**affects**

- [Modular assembly](../mechanic/modular-assembly.md) (Tunes / balances): Mapping the build space by behavior descriptors, as was done for Hearthstone decks, shows the best design in each style niche, exposing dominant part combinations and empty niches before players find them.
- [Design performance rating](../mechanic/design-performance-rating.md) (Tunes / balances): Searching for the top-scoring design in every descriptor cell stress-tests the rating formula and surfaces degenerate designs that score well, such as rides or bridges that game the metric.
- [Procedural terrain](../mechanic/procedural-terrain.md) (Deepens): Instead of one seed-to-map generator, a game can ship an archive of maps spanning designer axes, such as resource density by chokepoint count, each verified by simulation and served to players by trait.
- [Rival firms](../mechanic/rival-firms.md) (Deepens): An archive of competitor strategies, each the strongest found for its niche (aggressive expander, low-price discounter), gives AI rivals distinct styles without hand-tuning each persona.
- [Scenario objectives](../mechanic/scenario-objectives.md) (Cuts authoring cost): Scenario maps and starting conditions can be generated across a difficulty-by-style grid and filtered by agent playthroughs, replacing hand-built scenario sets with a curated archive.
- [Machine boosting](../mechanic/machine-boosting.md) (Tunes / balances): Searches over module and beacon layouts expose dominant boosting configurations that collapse design choice.

## Backlinks (computed)

**applied in:** [Generated recipe graphs](../opportunity/generated-recipe-graphs.md), [Learned build assist for cities](../opportunity/learned-build-assist.md), [Automated mechanic discovery](../opportunity/mechanic-discovery-search.md), [Open-ended evolution sandbox](../opportunity/open-ended-evolution-sandbox.md), [Parallel autobalancing of economies](../opportunity/parallel-autobalance.md), [Quality-diversity scenario libraries](../opportunity/qd-scenario-libraries.md)

**built upon by:** [Automated generation of game rules and mechanics](../technique/automated-rule-generation.md)

## Claims

- MAP-Elites (2015) returns a map of high-performing solutions across user-chosen dimensions of variation, revealing trade-offs and often finding a better best solution than standard search. *(confidence: high)* [[268](../source/src-mouret-2015-map-elites.md)]
- Gravina et al. (IEEE CoG 2019) framed procedural content generation as a quality-diversity problem and reviewed early applications to content generation and game playing. *(confidence: high)* [[269](../source/src-gravina-2019-pcg-quality-diversity.md)]
- MAP-Elites with sliding boundaries mapped Hearthstone deck spaces along play-style dimensions, found diverse strong decks, and was proposed as an aid to rebalancing. *(confidence: high)* [[270](../source/src-fontaine-2019-hearthstone-mesb.md)]
- CMA-ME searching a GAN's latent space produced playable Super Mario Bros levels spanning designer-chosen measures such as enemy and obstacle counts, and a user study found those measures changed perceived difficulty. *(confidence: high)* [[271](../source/src-fontaine-2020-mario-gan-qd.md)]
- DSAGE (2022) used a deep surrogate to predict agent behavior in generated environments and beat earlier QD environment-generation methods at finding environments that elicit diverse agent behaviors. *(confidence: medium)* [[272](../source/src-bhatt-2022-dsage.md)]
- QDAIF (2023) used language models to generate variations and to judge quality and diversity of creative text, covering more of the target space than non-QD baselines with reasonable agreement with human raters. *(confidence: medium)* [[273](../source/src-bradley-2023-qdaif.md)]

## Sources

- [Illuminating search spaces by mapping elites](../source/src-mouret-2015-map-elites.md)
- [Procedural Content Generation through Quality Diversity](../source/src-gravina-2019-pcg-quality-diversity.md)
- [Mapping Hearthstone Deck Spaces through MAP-Elites with Sliding Boundaries](../source/src-fontaine-2019-hearthstone-mesb.md)
- [Illuminating Mario Scenes in the Latent Space of a Generative Adversarial Network](../source/src-fontaine-2020-mario-gan-qd.md)
- [Deep Surrogate Assisted Generation of Environments](../source/src-bhatt-2022-dsage.md)
- [Quality-Diversity through AI Feedback](../source/src-bradley-2023-qdaif.md)

---
Provenance: created in run `2026-10-24-techniques-rl-design`; reviewed in `2026-10-24-technique-links`.
