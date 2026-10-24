# Automated mechanic discovery

*Opportunity* · `mechanic-discovery-search` · status: **asserted**

Search the space of rule programs with language-model-guided evolution and agent playtests to propose new mechanics that are learnable, deep, and unlike existing ones.

| field | value |
|---|---|
| opportunity type | Authoring tool |
| involves | [Production chains](../mechanic/production-chain.md), [Design performance rating](../mechanic/design-performance-rating.md), [Adaptive threat scaling](../mechanic/adaptive-threat-scaling.md), [Modding API](../mechanic/modding-api.md) |
| applies | [LLM-guided evolutionary program search](../technique/alphaevolve-algorithm-discovery.md), [Automated generation of game rules and mechanics](../technique/automated-rule-generation.md), [Quality-diversity search (MAP-Elites) for content and balance](../technique/quality-diversity-search.md), [Agent-based automated playtesting and balancing](../technique/automated-playtesting.md) |
| precedent | [Factorio](../game/factorio.md), [Dwarf Fortress](../game/dwarf-fortress.md), [SpaceChem](../game/spacechem.md) |
| novelty | 5 |
| feasibility | 2 |
| impact | 4 |
| horizon | 3-5 years |
| key risks | Proxies for fun are weak; search optimizes the proxy., Discovered mechanics may be illegible to humans., Compute cost of agent evaluation. |
| falsifiable signal | {'prediction': 'A commercial game will credit one of its shipped mechanics to an automated rule-discovery system.', 'resolve_by': '2030-12-31', 'criteria': 'Title released after 2026-10-24 with at least 1,000 Steam user reviews or a console release; a developer statement or paper attributes the origin of a shipped rule to automated search over rule sets.'} |
| priority *(computed)* | 3.282 |

## Summary

Search the space of rule programs with language-model-guided evolution and agent playtests to propose new mechanics that are learnable, deep, and unlike existing ones.

## Thesis

Automated game design has produced board-game rules (Ludii and GAVEL) and levels, and LLM-guided evolutionary search (FunSearch, AlphaEvolve) has found new algorithms and constructions. Simulation mechanics are small rule programs over state; a search that proposes rule variants, evaluates them with agent populations for depth and learnability proxies, and keeps a diversity archive could surface mechanics designers have not tried. The taxonomy in this repository is a candidate search space and novelty reference.

## Design Sketch

A designer selects a base simulation and a family. The system mutates rule code, runs agent populations, scores emergent variety, strategic depth, and legibility proxies, and returns an archive of diverse candidates with replays and plain-language descriptions, deduplicated against the existing taxonomy.

## Key Risks

- Proxies for fun are weak; search optimizes the proxy.
- Discovered mechanics may be illegible to humans.
- Compute cost of agent evaluation.

## Validation Experiment

Run LLM-guided evolution over rule variants of a small production-chain sim with a quality-diversity archive, then have designers rate the top 20 candidates for novelty and promise. Success: at least three candidates rated novel and worth prototyping by a majority of designers.

## Falsifiable signal

- **Prediction:** A commercial game will credit one of its shipped mechanics to an automated rule-discovery system.
- **Resolve by:** 2030-12-31
- **Criteria:** Title released after 2026-10-24 with at least 1,000 Steam user reviews or a console release; a developer statement or paper attributes the origin of a shipped rule to automated search over rule sets.

## Relations

**applies**

- [LLM-guided evolutionary program search](../technique/alphaevolve-algorithm-discovery.md)
- [Automated generation of game rules and mechanics](../technique/automated-rule-generation.md)
- [Quality-diversity search (MAP-Elites) for content and balance](../technique/quality-diversity-search.md)
- [Agent-based automated playtesting and balancing](../technique/automated-playtesting.md)

**involves**

- [Production chains](../mechanic/production-chain.md)
- [Design performance rating](../mechanic/design-performance-rating.md)
- [Adaptive threat scaling](../mechanic/adaptive-threat-scaling.md)
- [Modding API](../mechanic/modding-api.md)

**precedent**

- [Factorio](../game/factorio.md)
- [Dwarf Fortress](../game/dwarf-fortress.md)
- [SpaceChem](../game/spacechem.md)

---
Provenance: created in run `2026-10-24-synthesis`; reviewed in `2026-10-24-review-fixes`.
