# Weather-coupled energy grids

*Opportunity* · `weather-coupled-grids` · status: **asserted**

Power grids whose renewable supply follows realistic weather, so storage, forecasting, and demand response become the grid puzzle.

| field | value |
|---|---|
| opportunity type | Mechanic upgrade |
| involves | [Power grid](../mechanic/power-grid.md), [Weather](../mechanic/weather.md), [Forecasting](../mechanic/forecasting.md), [Supply-demand pricing](../mechanic/supply-demand-pricing.md), [Storage and buffers](../mechanic/storage-capacity.md) |
| applies | [Machine-learned weather forecasting](../technique/ml-weather-models.md), [Simulation-based inference for calibrating simulators](../technique/simulation-based-inference.md) |
| precedent | [Cities: Skylines II](../game/cities-skylines-2.md), [Anno 1800](../game/anno-1800.md), [Timberborn](../game/timberborn.md), [Surviving Mars](../game/surviving-mars.md) |
| novelty | 3 |
| feasibility | 4 |
| impact | 2 |
| horizon | 1-2 years |
| key risks | Realistic intermittency may frustrate players without good forecasting tools., Weather that dominates the economy reduces player agency. |
| falsifiable signal | {'prediction': 'A commercial city builder or management game will couple renewable generation to simulated weather as a core grid mechanic.', 'resolve_by': '2028-12-31', 'criteria': 'Developer documentation describing weather-dependent renewable output and storage in the grid system.'} |
| priority *(computed)* | 2.764 |

## Thesis

Power grids and weather are both common in the catalog but almost never coupled; most games treat generation as constant. Learned weather emulators make realistic, correlated wind, sun, and temperature affordable, and the coupling creates a familiar modern problem: balancing intermittent supply with storage, forecasts, and flexible demand.

## Design Sketch

Solar and wind output follow simulated weather; heating and cooling demand follow temperature; the player builds storage, buys forecasts, and sets demand-response policies. Rare long calm, cold spells test the grid. Prices respond to scarcity if the game has markets.

## Key Risks

- Realistic intermittency may frustrate players without good forecasting tools.
- Weather that dominates the economy reduces player agency.

## Validation Experiment

Couple a city prototype's grid to a weather emulator and test whether players with forecast tools build mixed storage strategies rather than one dominant plant type. Success: strategy diversity increases and blackout frustration ratings stay below the baseline game's disaster ratings.

## Falsifiable signal

- **Prediction:** A commercial city builder or management game will couple renewable generation to simulated weather as a core grid mechanic.
- **Resolve by:** 2028-12-31
- **Criteria:** Developer documentation describing weather-dependent renewable output and storage in the grid system.

## Relations

**applies**

- [Machine-learned weather forecasting](../technique/ml-weather-models.md)
- [Simulation-based inference for calibrating simulators](../technique/simulation-based-inference.md)

**involves**

- [Power grid](../mechanic/power-grid.md)
- [Weather](../mechanic/weather.md)
- [Forecasting](../mechanic/forecasting.md)
- [Supply-demand pricing](../mechanic/supply-demand-pricing.md)
- [Storage and buffers](../mechanic/storage-capacity.md)

**precedent**

- [Cities: Skylines II](../game/cities-skylines-2.md)
- [Anno 1800](../game/anno-1800.md)
- [Timberborn](../game/timberborn.md)
- [Surviving Mars](../game/surviving-mars.md)

---
Provenance: created in run `2026-10-24-synthesis`.
