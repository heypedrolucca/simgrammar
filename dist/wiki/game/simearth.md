# SimEarth

*Game* · `simearth` · status: **sourced**

A planetary god game built on James Lovelock's Gaia hypothesis in which geology, atmosphere, climate, life, and civilization models interact over billions of years under the player's parameter changes and interventions.

| field | value |
|---|---|
| aliases | SimEarth: The Living Planet |
| year | 1990 |
| developer | Maxis |
| platforms | PC, Console |
| subgenre | God game |
| subgenre secondary | Ecosystem / evolution |
| sim domain | Planetary / natural, Biological / ecological |
| player role | God |
| agency model | Policy / parameter, Supernatural intervention |
| time model | Real-time with pause |
| sim scale | Planet |
| fidelity | Systemic |
| perspective | Top-down / side 2D |
| win structure | Open sandbox |
| failure model | Cascading collapse |
| narrative mode | Emergent |
| multiplayer | Single-player |
| modding | None |
| production tier | AA |
| agent count order | Aggregate only |
| emergence | 3 |
| influence | 2 |
| cluster *(computed)* | C10 |
| core count *(computed)* | 3 |
| mechanic count *(computed)* | 10 |

## Summary

A planetary god game built on James Lovelock's Gaia hypothesis in which geology, atmosphere, climate, life, and civilization models interact over billions of years under the player's parameter changes and interventions.

## Core Loop

set geological, atmospheric, and biological rates -> climate and biomes evolve -> taxa spread, mutate, and diversify -> one sapient species advances through seven ages -> pollution, war, and disasters feed back on climate -> spend energy on interventions

## Design Notes

Will Wright and Fred Haslam built SimEarth with James Lovelock as adviser, and its models encode Gaian feedback: volcanic dust cools the planet, warming melts ice caps and raises seas, and life alters atmospheric gas fractions shown to three decimal places. The player mostly acts through control panels that set rates such as continental drift, reproduction, and mutation, plus energy-priced interventions (50 units per terrain square, 500 per terraforming device), so play is closer to tuning coupled systems than to directing agents. Scenarios include Daisyworld, Lovelock's minimal model of temperature regulation by daisy color, and terraforming Mars and Venus.

## Relations

**uses**

- [Planetary climate](../mechanic/planetary-climate.md) (core): Atmospheric composition, temperature, ocean level, and biomes evolve together under Gaian feedback; volcanic dust cools, warming melts ice caps, extreme heat boils oceans, and Daisyworld reduces it to daisies regulating temperature.
- [God powers](../mechanic/god-powers.md) (core): Placing terrain, life, monoliths, oxygen generators, and terraforming devices costs energy (50 per terrain square, 500 per device) from a budget that grows with planetary development.
- [Natural selection](../mechanic/natural-selection.md) (core): Taxa from prokaryotes to mammals spread and diversify by environment, with player-set reproduction and mutation rates; mass extinctions are often followed by renewed radiation, and any multicellular taxon can become sapient.
- [Habitat suitability](../mechanic/habitat-suitability.md) (supporting)
- [Terraforming](../mechanic/terraforming.md) (supporting): Mars, Venus, Ice Planet, and Dune scenarios ask the player to make hostile planets habitable.
- [Random disasters](../mechanic/random-disasters.md) (supporting): Hurricanes, wildfires, earthquakes, tsunamis, and meteors occur, with disease and pollution scaling with population.
- [Pollution spread](../mechanic/pollution-spread.md) (supporting)
- [Scenario objectives](../mechanic/scenario-objectives.md) (supporting)
- [Data overlays](../mechanic/data-overlays.md) (supporting)
- [Pause and speed control](../mechanic/variable-speed.md) (supporting)

## Backlinks (computed)

**precedent for:** [Learned regional weather](../opportunity/learned-weather-layer.md)

## Sources

- [SimEarth](../source/src-wikipedia-simearth.md)

---
Provenance: created in run `2026-10-24-catalog-gd`.
