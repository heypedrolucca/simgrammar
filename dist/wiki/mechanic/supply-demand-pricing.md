# Supply-demand pricing

*Mechanic* · `supply-demand-pricing` · status: **sourced**

Prices adjust to supply and demand, so scarcity raises prices and gluts lower them.

| field | value |
|---|---|
| aliases | dynamic pricing, market prices |
| family | Economy & finance |
| substrate | Aggregate stocks |
| math basis | System dynamics / ODEs, Mechanism design / auctions |
| feedback | Balancing (negative) |
| player interface | Observation only, Orders |
| legibility | 4 |
| emergence potential | 3 |
| authoring cost | 2 |
| compute cost | 2 |
| tuning difficulty | 4 |
| ai leverage | 2 |
| maturity | Classic |
| core count *(computed)* | 4 |
| earliest game *(computed)* | [M.U.L.E.](../game/mule.md) |
| earliest year *(computed)* | 1983 |
| prevalence *(computed)* | 10 |
| prevalence share *(computed)* | 0.057 |
| subgenre spread *(computed)* | 8 |
| technique count *(computed)* | 2 |
| technique exposure *(computed)* | 0.287 |

## Definition

Owns a price per good per market, anchored to a base price. Each tick the rule compares demand (consumption, buy orders) with supply (production, stock, sell orders) and raises the price when demand exceeds supply and lowers it otherwise, usually within a band around the base. Common forms are a stock-based price, p = base x f(stock / target stock), and an incremental update, p += k x (demand - supply) / supply. Prices feed back into production profitability and consumption. Victoria 3 (2022) sets each good's national market price from the balance of buy orders from consumption and sell orders from production relative to a base price, scales each state's orders by its market access, and blends local and market prices for poorly connected states. Offworld Trading Company moves prices continuously with every player's purchases and sales.

## Player Experience

Buy low, sell high, and watch your own trades move the market. The player spots shortages, rushes production to profit from high prices, and sees margins collapse as they and rivals flood the market. Prices become a readout of what the economy lacks.

## Design Levers

- price sensitivity (gain) and the band around base price
- base price per good, which sets the default value hierarchy
- whether the player's own trades move prices (price impact)
- smoothing, inertia, and update frequency
- how far price signals propagate between markets

## Failure Modes

- High gain causes price oscillation and boom-bust cycles that players read as random.
- When the player's trades do not move prices, a single arbitrage loop can be exploited indefinitely.
- Tight bands make prices too sticky to signal shortages; loose bands let goods become worthless.

## Dynamics

- High prices attract new producers whose output then pushes prices down, producing cobweb cycles.
- Producers crowd into the most profitable good, so profit migrates between goods over time.
- Shortages of an input propagate down production chains as price spikes.

## Open Questions

- Can demand models calibrated on real market data give games more believable price dynamics without making them unreadable?
- How much player price impact keeps markets responsive without enabling degenerate exploits?

## Relations

**synergy**

- [Trade routes](../mechanic/trade-routes.md): Price differentials are what make routes profitable; trade flattens them.

## Backlinks (computed)

**affected by:** [Mean field games and mean-field learning](../technique/mean-field-games.md), [Simulation-based inference for calibrating simulators](../technique/simulation-based-inference.md)

**involved in:** [AI liquidity in player markets](../opportunity/ai-liquidity-in-player-markets.md), [Calibrated serious simulations](../opportunity/calibrated-serious-sims.md), [Human-calibrated customers](../opportunity/human-calibrated-customers.md), [Parallel autobalancing of economies](../opportunity/parallel-autobalance.md)

**used by:** [Big Pharma](../game/big-pharma.md), [Bitburner](../game/bitburner.md), [Elite Dangerous](../game/elite-dangerous.md), [M.U.L.E.](../game/mule.md), [Offworld Trading Company](../game/offworld-trading-company.md), [Railroad Tycoon](../game/railroad-tycoon.md), [SimCity (2013)](../game/simcity-2013.md), [This War of Mine](../game/this-war-of-mine.md), [Victoria 3](../game/victoria-3.md), [Workers & Resources: Soviet Republic](../game/workers-and-resources.md)

## Sources

- [Victoria 3 Dev Diary #9: National Markets](../source/src-paradox-2021-vic3-national-markets.md)
- [Offworld Trading Company](../source/src-wikipedia-offworld-trading-company.md)

---
Provenance: created in run `2026-10-24-taxonomy-m2`.
