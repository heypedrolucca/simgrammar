# Generated recipe graphs

*Opportunity* · `generated-recipe-graphs` · status: **asserted**

Generate solvable, non-degenerate, on-theme production recipe graphs and tech trees, verified by agents, to cut content cost for factory and crafting games.

| field | value |
|---|---|
| opportunity type | Authoring tool |
| involves | [Production chains](../mechanic/production-chain.md), [Tech tree](../mechanic/tech-tree.md), [Hand crafting](../mechanic/hand-crafting.md), [Milestone unlocks](../mechanic/milestone-unlocks.md) |
| applies | [Automated generation of game rules and mechanics](../technique/automated-rule-generation.md), [Quality-diversity search (MAP-Elites) for content and balance](../technique/quality-diversity-search.md), [Agent-based automated playtesting and balancing](../technique/automated-playtesting.md), [LLM-guided evolutionary program search](../technique/alphaevolve-algorithm-discovery.md) |
| precedent | [Factorio](../game/factorio.md), [Satisfactory](../game/satisfactory.md), [Dyson Sphere Program](../game/dyson-sphere-program.md), [Minecraft](../game/minecraft.md) |
| novelty | 3 |
| feasibility | 4 |
| impact | 2 |
| horizon | 1-2 years |
| key risks | Generated graphs feel arbitrary without thematic logic., Agents optimize for metrics that miss what makes a recipe satisfying. |
| falsifiable signal | {'prediction': 'A factory or crafting game or overhaul mod will credit algorithmic or model-based generation for its recipe graph or tech tree.', 'resolve_by': '2028-12-31', 'criteria': 'Released after 2026-10-24; a game with at least 1,000 Steam user reviews, or a mod with at least 10,000 downloads on its official mod portal; the developer or mod author states that the shipped recipe graph was produced or substantially shaped by a generative tool.'} |
| priority *(computed)* | 2.764 |

## Thesis

Recipe graphs and tech trees are among the most prevalent content structures in the catalog, and their design is slow: each new item must be reachable, useful, and not dominated. Automated rule generation and quality-diversity search can propose graph variants, and agent playtests can check reachability, ratio complexity, and whether alternate recipes create real choices. Modding communities could use the same tool for overhaul mods.

## Design Sketch

Designers set a theme, resource set, and target depth; the tool proposes recipe graphs with cycle times and alternates, simulates optimal and novice factories, and returns an archive ranked by depth, branching, and degeneracy checks. Designers edit and lock items they like.

## Key Risks

- Generated graphs feel arbitrary without thematic logic.
- Agents optimize for metrics that miss what makes a recipe satisfying.

## Validation Experiment

Generate 100 recipe graphs for a fixed resource set and have experienced factory players rate a sample against an authored graph blind. Success: top-decile generated graphs rated equal to the authored one.

## Falsifiable signal

- **Prediction:** A factory or crafting game or overhaul mod will credit algorithmic or model-based generation for its recipe graph or tech tree.
- **Resolve by:** 2028-12-31
- **Criteria:** Released after 2026-10-24; a game with at least 1,000 Steam user reviews, or a mod with at least 10,000 downloads on its official mod portal; the developer or mod author states that the shipped recipe graph was produced or substantially shaped by a generative tool.

## Relations

**applies**

- [Automated generation of game rules and mechanics](../technique/automated-rule-generation.md)
- [Quality-diversity search (MAP-Elites) for content and balance](../technique/quality-diversity-search.md)
- [Agent-based automated playtesting and balancing](../technique/automated-playtesting.md)
- [LLM-guided evolutionary program search](../technique/alphaevolve-algorithm-discovery.md)

**involves**

- [Production chains](../mechanic/production-chain.md)
- [Tech tree](../mechanic/tech-tree.md)
- [Hand crafting](../mechanic/hand-crafting.md)
- [Milestone unlocks](../mechanic/milestone-unlocks.md)

**precedent**

- [Factorio](../game/factorio.md)
- [Satisfactory](../game/satisfactory.md)
- [Dyson Sphere Program](../game/dyson-sphere-program.md)
- [Minecraft](../game/minecraft.md)

---
Provenance: created in run `2026-10-24-synthesis`; reviewed in `2026-10-24-review-fixes`.
