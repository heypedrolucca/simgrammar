# Weather

*Mechanic* · `weather` · status: **sourced**

Weather states such as rain, storms, snow, wind, and temperature change over time and modify activities and other systems.

| field | value |
|---|---|
| aliases | weather system, storms |
| family | Environment & ecology |
| substrate | Stochastic events, Rule system |
| math basis | Markov / stochastic processes, Procedural noise / generative grammars |
| feedback | None |
| player interface | Observation only |
| legibility | 4 |
| emergence potential | 3 |
| authoring cost | 3 |
| compute cost | 1 |
| tuning difficulty | 2 |
| ai leverage | 2 |
| maturity | Classic |
| open questions | Can learned global weather models supply spatially coherent, plausible weather for procedural worlds at low runtime cost? |
| core count *(computed)* | 4 |
| earliest game *(computed)* | [The Oregon Trail](../game/oregon-trail.md) |
| earliest year *(computed)* | 1971 |
| prevalence *(computed)* | 26 |
| prevalence share *(computed)* | 0.149 |
| subgenre spread *(computed)* | 15 |
| technique count *(computed)* | 2 |
| technique exposure *(computed)* | 0.688 |

## Definition

Owns a current weather state, and sometimes a forecast, drawn each day or interval from season-dependent probabilities or evolved as a Markov chain or noise field across the map. The state sets modifiers other systems read: rain waters crops or puts out fire, storms bring lightning that damages things, cold lowers body temperature, wind changes travel or spread, and fog cuts visibility. Stardew Valley picks daily weather, shows tomorrow's forecast on the TV, never rains in winter without a Rain Totem, and lets lightning destroy crops unless lightning rods intercept it; The Long Dark's blizzards and cold nights drive its survival loop; Microsoft Flight Simulator 2020 can stream real-world weather. Inputs are season, location, and random draws; outputs are condition flags and values such as temperature and wind.

## Player Experience

Adapting plans to conditions outside the player's control. The player checks the forecast, moves tasks indoors on stormy days, waits out a blizzard, or takes advantage of rain. Weather makes days feel different and gives the world a mood.

## Design Levers

- set of weather states and their transition probabilities by season and region
- duration and spatial extent of weather events
- which systems each state modifies and by how much
- forecast availability and accuracy
- protection tools: shelter, lightning rods, clothing, irrigation

## Failure Modes

- Purely cosmetic weather costs effects budget without changing decisions.
- Severe weather with no forecast or counterplay feels like an unfair random penalty.
- Weather rolled independently each day can flip implausibly between extremes.

## Dynamics

- Weather couples many systems at once: crops, fire, travel, mood, and body temperature.
- Forecasts turn weather from noise into a planning input, rewarding flexible schedules.
- Rare extreme weather becomes a memorable event that players prepare for.

## Open Questions

- Can learned global weather models supply spatially coherent, plausible weather for procedural worlds at low runtime cost?

## Backlinks (computed)

**affected by:** [Genie foundation world models](../technique/genie-world-models.md), [Machine-learned weather forecasting](../technique/ml-weather-models.md)

**involved in:** [Learned regional weather](../opportunity/learned-weather-layer.md), [Weather-coupled energy grids](../opportunity/weather-coupled-grids.md)

**used by:** [Animal Crossing: New Horizons](../game/animal-crossing-new-horizons.md), [Arma 3](../game/arma-3.md), [Black & White](../game/black-and-white.md), [Command: Modern Operations](../game/command-modern-operations.md), [DCS World](../game/dcs-world.md), [Euro Truck Simulator 2](../game/euro-truck-simulator-2.md), [Farming Simulator 25](../game/farming-simulator-25.md), [Frostpunk](../game/frostpunk.md), [Gran Turismo 7](../game/gran-turismo-7.md), [Hearts of Iron IV](../game/hearts-of-iron-4.md), [Kenshi](../game/kenshi.md), [Lemonade Stand](../game/lemonade-stand.md), [Microsoft Flight Simulator (2020)](../game/microsoft-flight-simulator-2020.md), [Microsoft Flight Simulator 2024](../game/microsoft-flight-simulator-2024.md), [Motorsport Manager](../game/motorsport-manager.md), [The Oregon Trail](../game/oregon-trail.md), [Planet Zoo](../game/planet-zoo.md), [Project Zomboid](../game/project-zomboid.md), [Silent Hunter III](../game/silent-hunter-3.md), [SimAnt](../game/simant.md), [Stardew Valley](../game/stardew-valley.md), [The Long Dark](../game/the-long-dark.md), [Utopia](../game/utopia.md), [Valheim](../game/valheim.md), [X-Plane](../game/x-plane.md), [The Legend of Zelda: Breath of the Wild](../game/zelda-breath-of-the-wild.md)

## Sources

- [Weather](../source/src-stardewvalleywiki-2026-weather.md)
- [The Long Dark](../source/src-wikipedia-the-long-dark.md)

---
Provenance: created in run `2026-10-24-taxonomy-m5`.
