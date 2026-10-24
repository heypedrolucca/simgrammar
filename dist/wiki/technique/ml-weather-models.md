# Machine-learned weather forecasting

*Technique* · `ml-weather-models` · status: **sourced**

Neural networks trained on decades of atmospheric reanalysis forecast global weather 10-15 days ahead in seconds to minutes on one accelerator, matching or beating physics-based operational models on most verification targets.

| field | value |
|---|---|
| aliases | GraphCast, GenCast, Aurora, AIFS, FGN, WeatherNext, ML weather prediction |
| category | Neural physics & surrogates |
| year | 2023 |
| maturity | Research |
| trl | 3 |
| runtime | Offline authoring, Server real-time |
| determinism impact | Mitigable |
| horizon | 3-5 years |
| risks | Compute cost, Controllability |
| builds on | [Graph network simulators and neural operators](../technique/graph-network-simulators.md) |
| deployed in |  |
| affects count *(computed)* | 5 |

## Summary

Neural networks trained on decades of atmospheric reanalysis forecast global weather 10-15 days ahead in seconds to minutes on one accelerator, matching or beating physics-based operational models on most verification targets.

## Mechanism

Models take the current and recent atmospheric state on a global 0.25 degree latitude-longitude grid (temperature, wind, humidity, pressure at many levels plus surface variables) and predict the state one fixed step later; rolling the prediction forward gives a 10-15 day forecast. GraphCast maps grid cells onto a multi-resolution icosahedral mesh and runs learned message passing there. GenCast is a conditional diffusion model that samples stochastic trajectories in 12-hour steps, so repeated samples form an ensemble with calibrated spread. FGN (2025) builds ensembles from learned model perturbations trained on CRPS. Aurora is a 1.3B-parameter foundation model pretrained on over a million hours of geophysical data and fine-tuned for air quality, ocean waves, cyclone tracks and 0.1 degree weather. Inference replaces hours on a supercomputer with seconds to minutes on one accelerator.

## Limitations

- Trained on Earth's reanalysis record, so they reproduce Earth's atmosphere only; fictional planets, altered geography or deliberate climate change lie outside the training data.
- Grids are coarse for game maps: 0.25 degree (about 28 km at the equator), and operational AIFS runs at 28 km.
- Inference needs an accelerator and gigabytes of weights (Aurora has 1.3B parameters), heavy for client-side use.
- Designers cannot author dramatic timing; the model follows the statistics of real weather, so pacing must be imposed by selecting or conditioning forecasts.
- Autoregressive rollouts are validated to 10-15 days; behavior over seasons or years is not established by these sources.

## Relations

**affects**

- [Weather](../mechanic/weather.md) (Deepens): Weather becomes a coherent global field with fronts, cyclones and multi-day evolution across hundreds of variables, instead of a per-region Markov chain of weather states.
- [Forecasting](../mechanic/forecasting.md) (Enables new form): Ensembles (50 GenCast members) give calibrated probabilities, so an in-game forecast can carry real uncertainty that players plan against and that occasionally misses honestly.
- [Random disasters](../mechanic/random-disasters.md) (Deepens): Storms emerge from atmospheric state with forecastable tracks (Aurora beat operational centres on 5-day cyclone tracks), turning disasters from dice rolls into threats with lead time.
- [Pollution spread](../mechanic/pollution-spread.md) (Deepens): Aurora's fine-tuned air-quality forecasts run about 100,000x faster than CAMS, a path to pollution plumes transported by simulated wind at playable cost.
- [Planetary climate](../mechanic/planetary-climate.md) (Deepens): Earth-system foundation models fine-tuned to several domains suggest climate sims coupling atmosphere, ocean waves and air chemistry, though they are trained for days-ahead weather, not decades.

**builds on**

- [Graph network simulators and neural operators](../technique/graph-network-simulators.md)

## Backlinks (computed)

**applied in:** [Learned regional weather](../opportunity/learned-weather-layer.md), [Weather-coupled energy grids](../opportunity/weather-coupled-grids.md)

## Claims

- GraphCast produced 0.25 degree, 10-day global forecasts in under one minute on one TPU v4 machine and beat ECMWF HRES on over 90% of 1,380 verification targets. *(confidence: high)* [[200](../source/src-lam-2023-graphcast.md), [201](../source/src-deepmind-2023-graphcast-blog.md)]
- GenCast's 50-member diffusion ensembles were more skillful than ECMWF's ENS on 97.2% of 1,320 targets; one 15-day forecast took about 8 minutes on a Cloud TPU v5. *(confidence: high)* [[202](../source/src-price-2024-gencast.md)]
- Aurora (1.3B parameters) matched or beat operational systems on 74% of air-quality targets, 86% of ocean-wave variables and 92% of 0.1 degree weather targets, beat seven centres on 5-day cyclone tracks, and ran about 100,000x faster than CAMS for air quality. *(confidence: high)* [[203](../source/src-bodnar-2025-aurora.md)]
- ECMWF made its AIFS machine-learned model operational on 25 February 2025, reporting about 1,000x less energy per forecast than its physics model, at 28 km grid spacing versus 9 km. *(confidence: high)* [[204](../source/src-ecmwf-2025-aifs-operational.md)]
- FGN (2025) reported state-of-the-art ensemble skill and cyclone tracks while being trained only on per-location targets. *(confidence: medium)* [[205](../source/src-alet-2025-fgn.md)]

## Sources

- [GraphCast: Learning skillful medium-range global weather forecasting](../source/src-lam-2023-graphcast.md)
- [GraphCast: AI model for faster and more accurate global weather forecasting](../source/src-deepmind-2023-graphcast-blog.md)
- [Probabilistic weather forecasting with machine learning](../source/src-price-2024-gencast.md)
- [A foundation model for the Earth system](../source/src-bodnar-2025-aurora.md)
- [ECMWF's AI forecasts become operational](../source/src-ecmwf-2025-aifs-operational.md)
- [Skillful joint probabilistic weather forecasting from marginals](../source/src-alet-2025-fgn.md)

---
Provenance: created in run `2026-10-24-techniques-sim-math`.
