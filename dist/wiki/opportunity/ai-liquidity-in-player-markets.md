# AI liquidity in player markets

*Opportunity* · `ai-liquidity-in-player-markets` · status: **asserted**

Keep player-driven markets liquid on small servers with model-driven traders whose behavior is calibrated to human trading and constrained by market rules.

| field | value |
|---|---|
| opportunity type | Mechanic upgrade |
| involves | [Player-driven markets](../mechanic/player-driven-market.md), [Persistent shared world](../mechanic/persistent-world.md), [Auctions](../mechanic/auctions.md), [Supply-demand pricing](../mechanic/supply-demand-pricing.md) |
| applies | [LLM models of individual human choice](../technique/human-behavior-simulation-models.md), [Mean field games and mean-field learning](../technique/mean-field-games.md), [Many-agent LLM societies](../technique/llm-agent-societies.md) |
| precedent | [EVE Online](../game/eve-online.md), [Second Life](../game/second-life.md), [Ultima Online](../game/ultima-online.md), [M.U.L.E.](../game/mule.md) |
| novelty | 3 |
| feasibility | 3 |
| impact | 2 |
| horizon | 1-2 years |
| key risks | Players perceive bots as unfair competition., Agents can be exploited for arbitrage., Calibration drift as the human population changes. |
| falsifiable signal | {'prediction': 'A persistent online game will add AI traders to its player-driven market, with their behavior fitted to observed player trading.', 'resolve_by': '2029-06-30', 'criteria': 'Announced or shipped after 2026-10-24 in a persistent online game with a player-driven market; developer material states that AI market participants were trained or calibrated on player trade data. NPC vendors with fixed prices do not count.'} |
| priority *(computed)* | 2.5 |

## Thesis

Player-driven economies need large populations; EVE Online works because it has them, and smaller persistent worlds stagnate. Agents calibrated to human trading behavior, and analyzed with mean-field methods for stability, can supply liquidity and price discovery without dominating. Mechanism design keeps them from front-running humans.

## Design Sketch

Each market has a population of agent traders with budgets, risk profiles, and information limits matching human traders, operating under the same order-book rules. Their share of volume is capped and published. Designers tune agent populations to target liquidity and volatility bands.

## Key Risks

- Players perceive bots as unfair competition.
- Agents can be exploited for arbitrage.
- Calibration drift as the human population changes.

## Validation Experiment

Simulate a 200-player market with and without calibrated agents using logged order data from a public game economy; measure spread, depth, volatility, and human profit share. Success: tighter spreads and lower volatility with human profit share unchanged within 5 percent.

## Falsifiable signal

- **Prediction:** A persistent online game will add AI traders to its player-driven market, with their behavior fitted to observed player trading.
- **Resolve by:** 2029-06-30
- **Criteria:** Announced or shipped after 2026-10-24 in a persistent online game with a player-driven market; developer material states that AI market participants were trained or calibrated on player trade data. NPC vendors with fixed prices do not count.

## Relations

**applies**

- [LLM models of individual human choice](../technique/human-behavior-simulation-models.md)
- [Mean field games and mean-field learning](../technique/mean-field-games.md)
- [Many-agent LLM societies](../technique/llm-agent-societies.md)

**involves**

- [Player-driven markets](../mechanic/player-driven-market.md)
- [Persistent shared world](../mechanic/persistent-world.md)
- [Auctions](../mechanic/auctions.md)
- [Supply-demand pricing](../mechanic/supply-demand-pricing.md)

**precedent**

- [EVE Online](../game/eve-online.md)
- [Second Life](../game/second-life.md)
- [Ultima Online](../game/ultima-online.md)
- [M.U.L.E.](../game/mule.md)

---
Provenance: created in run `2026-10-24-synthesis`; reviewed in `2026-10-24-review-fixes`.
