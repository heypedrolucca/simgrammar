# Parallel autobalancing of economies

*Opportunity* · `parallel-autobalance` · status: **asserted**

Run thousands of scripted, learned, and diversity-seeking agents through a game's economy at accelerated speed to find degenerate strategies and tune parameters before players do.

| field | value |
|---|---|
| opportunity type | Authoring tool |
| involves | [Production chains](../mechanic/production-chain.md), [Supply-demand pricing](../mechanic/supply-demand-pricing.md), [Tech tree](../mechanic/tech-tree.md), [Adaptive threat scaling](../mechanic/adaptive-threat-scaling.md), [Rival firms](../mechanic/rival-firms.md) |
| applies | [Agent-based automated playtesting and balancing](../technique/automated-playtesting.md), [Massively parallel GPU simulation](../technique/massively-parallel-simulation.md), [Quality-diversity search (MAP-Elites) for content and balance](../technique/quality-diversity-search.md), [Differentiable simulation](../technique/differentiable-simulation.md) |
| precedent | [Factorio](../game/factorio.md), [Offworld Trading Company](../game/offworld-trading-company.md), [Anno 1800](../game/anno-1800.md), [RimWorld](../game/rimworld.md) |
| novelty | 2 |
| feasibility | 4 |
| impact | 3 |
| horizon | Now |
| falsifiable signal | {'prediction': "At least two studios will publicly describe using large-scale agent search to balance a simulation or strategy game's economy before release.", 'resolve_by': '2027-12-31', 'criteria': 'Talks, technical blogs, or papers published after 2026-10-24 by staff of two different studios, each naming a commercial title with at least 1,000 Steam user reviews and describing automated agent play at scale used for economy balance.'} |
| priority *(computed)* | 3.059 |

## Summary

Run thousands of scripted, learned, and diversity-seeking agents through a game's economy at accelerated speed to find degenerate strategies and tune parameters before players do.

## Thesis

Production chains, markets, threat scaling, and tech trees have many interacting parameters and are tuned by small QA teams and patches after launch. GPU-parallel simulation and quality-diversity search make it practical to run very large populations of strategies and to search parameter space for regions with no dominant strategy. This shifts balance work from reactive patching to pre-launch search.

## Design Sketch

A headless build of the simulation runs on a GPU cluster. A quality-diversity search maintains an archive of strategies across behavior descriptors (expansion speed, military share, trade dependence); a tuner adjusts parameters to keep win rates and resource curves inside designer-set bands; reports flag exploits with replays.

## Key Risks

- Bots find exploits humans never would and miss ones humans find.
- Headless builds of legacy engines are expensive to make.
- Over-balancing removes interesting asymmetries.

## Validation Experiment

Run a MAP-Elites search over strategies in an open-source economy game for one GPU-day and compare discovered exploits with the game's historical patch notes. Success: at least half of historically patched economic exploits rediscovered.

## Falsifiable signal

- **Prediction:** At least two studios will publicly describe using large-scale agent search to balance a simulation or strategy game's economy before release.
- **Resolve by:** 2027-12-31
- **Criteria:** Talks, technical blogs, or papers published after 2026-10-24 by staff of two different studios, each naming a commercial title with at least 1,000 Steam user reviews and describing automated agent play at scale used for economy balance.

## Relations

**applies**

- [Agent-based automated playtesting and balancing](../technique/automated-playtesting.md)
- [Massively parallel GPU simulation](../technique/massively-parallel-simulation.md)
- [Quality-diversity search (MAP-Elites) for content and balance](../technique/quality-diversity-search.md)
- [Differentiable simulation](../technique/differentiable-simulation.md)

**involves**

- [Production chains](../mechanic/production-chain.md)
- [Supply-demand pricing](../mechanic/supply-demand-pricing.md)
- [Tech tree](../mechanic/tech-tree.md)
- [Adaptive threat scaling](../mechanic/adaptive-threat-scaling.md)
- [Rival firms](../mechanic/rival-firms.md)

**precedent**

- [Factorio](../game/factorio.md)
- [Offworld Trading Company](../game/offworld-trading-company.md)
- [Anno 1800](../game/anno-1800.md)
- [RimWorld](../game/rimworld.md)

---
Provenance: created in run `2026-10-24-synthesis`; reviewed in `2026-10-24-review-fixes`.
