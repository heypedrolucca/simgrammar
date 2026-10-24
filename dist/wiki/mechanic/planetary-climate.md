# Planetary climate

*Mechanic* · `planetary-climate` · status: **sourced**

Planet-scale variables such as atmospheric composition, temperature, sea level, and biosphere evolve under coupled feedbacks and can be deliberately altered.

| field | value |
|---|---|
| aliases | global climate, gaia model, global warming |
| family | Environment & ecology |
| substrate | Aggregate stocks, Cellular grid |
| math basis | System dynamics / ODEs, Control theory |
| feedback | Both |
| player interface | Parameter, Placement, Observation only |
| legibility | 2 |
| emergence potential | 3 |
| authoring cost | 2 |
| compute cost | 2 |
| tuning difficulty | 4 |
| ai leverage | 3 |
| maturity | Established |
| core count *(computed)* | 1 |
| earliest game *(computed)* | [SimEarth](../game/simearth.md) |
| earliest year *(computed)* | 1990 |
| prevalence *(computed)* | 5 |
| prevalence share *(computed)* | 0.029 |
| subgenre spread *(computed)* | 5 |
| technique count *(computed)* | 1 |
| technique exposure *(computed)* | 0.188 |

## Definition

Owns a small set of planet-scale stocks such as atmospheric gas fractions, greenhouse level, mean temperature, ice cover, sea level, and biomass, sometimes resolved on a coarse map grid. Each tick emissions, volcanism, and life change the gases, temperature follows radiative balance and albedo, and temperature moves ice, sea level, and where life can grow. SimEarth, advised by James Lovelock, shows gas levels as percentages, melts ice caps and raises seas under warming, cools the planet with volcanic dust, and offers a Daisyworld mode based on Watson and Lovelock's model, in which daisies of different albedo regulate temperature. Civilization added global warming from unchecked pollution; Surviving Mars: Green Planet terraforms by raising planetary parameters toward habitable targets; Eco lets player emissions raise sea level. Inputs are emissions and player projects; outputs are habitability and disasters.

## Player Experience

Slow consequence at the largest scale. The player makes small persistent changes, such as emissions or terraforming projects, and watches planet-wide numbers creep toward thresholds where oceans boil, ice advances, or the planet becomes habitable. Success feels like stewardship; failure arrives long after its cause.

## Design Levers

- which planetary stocks exist and how many feedbacks link them (albedo, greenhouse, biosphere)
- time constants between emissions and temperature or sea-level response
- presence of tipping points or runaway regimes versus smooth response
- player levers: emissions policy, terraforming buildings, direct parameter sliders
- spatial resolution: single global numbers or a gridded map

## Failure Modes

- Many coupled variables with long delays make cause and effect opaque, so players change sliders without learning what moved the planet.
- Linear, delay-free responses reduce climate to a single meter to keep below a line.
- Runaway feedback with no recovery path ends runs because of early mistakes the player could not see.

## Dynamics

- Biosphere-climate feedback can stabilize temperature, as in Daisyworld, or amplify change when it breaks down.
- Climate shifts move habitat suitability, crop yields, and coastlines, forcing migration or rebuilding.
- Shared emissions in multiplayer worlds such as Eco create commons problems between players.

## Open Questions

- Can learned climate emulators give fast, plausible regional responses to player emissions without hand-tuned equations?
- How short can feedback delays be made before climate stops reading as climate?

## Backlinks (computed)

**affected by:** [Machine-learned weather forecasting](../technique/ml-weather-models.md)

**involved in:** [Learned regional weather](../opportunity/learned-weather-layer.md)

**used by:** [Aurora 4X](../game/aurora-4x.md), [Eco](../game/eco.md), [SimEarth](../game/simearth.md), [Surviving Mars](../game/surviving-mars.md), [Universe Sandbox](../game/universe-sandbox.md)

## Sources

- [SimEarth](../source/src-wikipedia-simearth.md)
- [Biological homeostasis of the global environment: the parable of Daisyworld](../source/src-watson-1983-daisyworld.md)

---
Provenance: created in run `2026-10-24-taxonomy-m5`.
