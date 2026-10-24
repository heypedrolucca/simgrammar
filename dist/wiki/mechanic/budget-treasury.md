# Treasury and budget

*Mechanic* · `budget-treasury` · status: **sourced**

A money stock with income and expense flows such as taxes, upkeep, wages, and service funding; a negative balance leads to debt or failure.

| field | value |
|---|---|
| aliases | treasury, cash flow, budget panel |
| family | Economy & finance |
| substrate | Aggregate stocks |
| math basis | System dynamics / ODEs, Optimization |
| feedback | Both |
| player interface | Parameter, Observation only |
| legibility | 4 |
| emergence potential | 3 |
| authoring cost | 1 |
| compute cost | 1 |
| tuning difficulty | 3 |
| ai leverage | 2 |
| maturity | Classic |
| core count *(computed)* | 6 |
| earliest game *(computed)* | [Lemonade Stand](../game/lemonade-stand.md) |
| earliest year *(computed)* | 1973 |
| prevalence *(computed)* | 27 |
| prevalence share *(computed)* | 0.155 |
| subgenre spread *(computed)* | 13 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

Owns one money stock and a ledger of flow categories. Each accounting period income (taxes, fees, sales, trade) is added and expenses (upkeep, wages, service funding, interest) are subtracted. Players often set a funding fraction per department, and service effectiveness scales with it. In Micropolis, the open-source SimCity engine, the collection every 48 city-time steps computes revenue = population x average land value / 120 x tax rate x a difficulty factor, sets required police and fire funds at 100 per station and road funds per road and rail tile, and converts the fraction actually paid into RoadEffect (0-32) and PoliceEffect and FireEffect (0-1000), so underfunded roads decay and coverage shrinks. A negative balance leads to loans, bonds, bankruptcy, or game over; SimCity 2000 ends the game after extreme deficit spending.

## Player Experience

Periodic reckoning. The player watches a running balance and a monthly or yearly ledger, trims service budgets to stay solvent, and decides when a surplus should become new construction. Shortfalls show up as visible decay: crumbling roads, slower fire response, unpaid staff.

## Design Levers

- accounting period length and whether flows post continuously or at fixed ticks
- which expense categories are player-adjustable and how effectiveness scales with the funding fraction
- upkeep per building relative to the revenue it enables
- consequence of a negative balance (borrowing, forced cuts, bankruptcy, or game over)
- how much ledger detail and forecasting the interface shows

## Failure Modes

- Upkeep that scales slower than revenue makes money irrelevant by mid-game, a common complaint about Cities: Skylines.
- Funding sliders whose effects are delayed or hidden teach players to cut services without visible cost until a collapse.
- Fixed upkeep with no link to growth produces an early cash trap with no recovery path.

## Dynamics

- Surpluses fund expansion that raises both revenue and upkeep, so cash pressure returns at each growth stage.
- Underfunding one service degrades a dependent system (roads, crime, fires), which later lowers the revenue base.
- Periodic settlement creates sawtooth cash curves and end-of-period scrambles.

## Open Questions

- Can an LLM advisor explain a deficit as a causal chain through the ledger well enough to replace spreadsheet-style budget panels?
- What upkeep-to-revenue curve keeps money a meaningful constraint into the late game?

## Relations

**synergy**

- [Loans and debt](../mechanic/loans-debt.md): Debt extends the treasury in time, trading future flexibility for present growth.

## Backlinks (computed)

**involved in:** [Participatory planning sandboxes](../opportunity/participatory-planning-sandboxes.md)

**required by:** [Loans and debt](../mechanic/loans-debt.md), [Taxation](../mechanic/taxation.md)

**used by:** [Aurora 4X](../game/aurora-4x.md), [Contraband Police](../game/contraband-police.md), [Equilinox](../game/equilinox.md), [Euro Truck Simulator 2](../game/euro-truck-simulator-2.md), [Football Manager](../game/football-manager.md), [Game Dev Tycoon](../game/game-dev-tycoon.md), [Kerbal Space Program](../game/kerbal-space-program.md), [Lemonade Stand](../game/lemonade-stand.md), [Motorsport Manager](../game/motorsport-manager.md), [Out of the Park Baseball](../game/out-of-the-park-baseball.md), [Papers, Please](../game/papers-please.md), [PC Building Simulator](../game/pc-building-simulator.md), [Princess Maker 2](../game/princess-maker-2.md), [Prison Architect](../game/prison-architect.md), [Project Hospital](../game/project-hospital.md), [Rebel Inc.](../game/rebel-inc.md), [SimCity](../game/simcity-1989.md), [SimCity 2000](../game/simcity-2000.md), [SimCity (2013)](../game/simcity-2013.md), [SimCity 4](../game/simcity-4.md), [SimTower](../game/simtower.md), [Suzerain](../game/suzerain.md), [Terra Nil](../game/terra-nil.md), [The Sims](../game/the-sims.md), [Tropico 6](../game/tropico-6.md), [Utopia](../game/utopia.md), [Victoria 3](../game/victoria-3.md)

## Sources

- [Micropolis: open-source SimCity source code](../source/src-hopkins-2008-micropolis.md)
- [SimCity 2000](../source/src-wikipedia-simcity-2000.md)

---
Provenance: created in run `2026-10-24-taxonomy-m2`.
