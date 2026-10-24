# Rival firms

*Mechanic* · `rival-firms` · status: **sourced**

AI or player competitors contest markets, prices, and assets; market share decides who wins.

| field | value |
|---|---|
| aliases | AI competitors, competing companies |
| family | Economy & finance |
| substrate | Agent-based |
| math basis | Game theory, Utility / decision theory |
| feedback | Both |
| player interface | Parameter, Observation only |
| legibility | 3 |
| emergence potential | 3 |
| authoring cost | 2 |
| compute cost | 2 |
| tuning difficulty | 4 |
| ai leverage | 4 |
| maturity | Classic |
| core count *(computed)* | 4 |
| earliest game *(computed)* | [M.U.L.E.](../game/mule.md) |
| earliest year *(computed)* | 1983 |
| prevalence *(computed)* | 8 |
| prevalence share *(computed)* | 0.046 |
| subgenre spread *(computed)* | 5 |
| technique count *(computed)* | 4 |
| technique exposure *(computed)* | 1.188 |

## Definition

Owns one or more competitor companies, each with cash, assets, market presence, and strategy parameters such as aggressiveness, expansion rate, and pricing policy. Each turn or tick a rival evaluates opportunities, builds or buys capacity, sets prices, and competes for the same customers, so market share splits by relative price, quality, coverage, and brand. Rivals can go bankrupt, be bought, or buy the player. Railroad Tycoon (1990) has rival railroad barons who try to drive the player out through stock dealings and rate wars. Capitalism (1995) lets the player set rivals' competence and managerial style from very aggressive to conservative and makes being bought out a loss. Transport Tycoon's AI companies build competing routes, and Offworld Trading Company's rivals contest the same resources and prices.

## Player Experience

Having someone to beat. The player watches rivals enter their markets, cuts prices or raises quality to hold share, and sometimes waits for a rival to overextend before striking. Victory becomes relative, which gives the sandbox a scoreboard.

## Design Levers

- number of rivals and their strategy profiles (aggressive, conservative, specialist)
- whether rivals obey the same rules and economics as the player or receive bonuses
- responsiveness: how quickly rivals react to price cuts or new entrants
- interaction channels: price, location, stock, sabotage, poaching staff
- bankruptcy and merger rules for rivals

## Failure Modes

- Passive AI that never contests markets turns competition into decoration.
- AI that receives hidden resource bonuses feels unfair once players notice it.
- Rivals that keep building in unprofitable markets go bankrupt early and leave the player alone.

## Dynamics

- Price wars drive margins toward zero until one firm exits, after which prices rebound.
- Market leaders gain economies of scale that compound their lead.
- Rivals entering a player's niche push the player to diversify into new markets.

## Open Questions

- Can LLM or RL-driven firms pursue legible strategies (cornering a supply, undercutting, collusion) that players can read and counter?
- How should rival competence scale with difficulty without hidden bonuses?

## Relations

**synergy**

- [Supply-demand pricing](../mechanic/supply-demand-pricing.md): Competitors move prices, turning a market into a strategic game.

## Backlinks (computed)

**affected by:** [Regret minimization and search for imperfect-information games](../technique/imperfect-information-solvers.md), [Self-play planning with learned models (AlphaZero, MuZero, Dreamer)](../technique/model-based-planning-muzero.md), [Monte Carlo tree search for game AI](../technique/monte-carlo-tree-search.md), [Quality-diversity search (MAP-Elites) for content and balance](../technique/quality-diversity-search.md)

**involved in:** [Parallel autobalancing of economies](../opportunity/parallel-autobalance.md)

**used by:** [Anno 1800](../game/anno-1800.md), [Big Pharma](../game/big-pharma.md), [Capitalism](../game/capitalism.md), [M.U.L.E.](../game/mule.md), [Offworld Trading Company](../game/offworld-trading-company.md), [Railroad Tycoon](../game/railroad-tycoon.md), [Theme Park](../game/theme-park.md), [Transport Tycoon](../game/transport-tycoon.md)

## Sources

- [Railroad Tycoon (video game)](../source/src-wikipedia-railroad-tycoon.md)
- [Capitalism (video game)](../source/src-wikipedia-capitalism-video-game.md)
- [Offworld Trading Company](../source/src-wikipedia-offworld-trading-company.md)

---
Provenance: created in run `2026-10-24-taxonomy-m2`.
