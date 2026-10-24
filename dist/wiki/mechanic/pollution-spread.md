# Pollution spread

*Mechanic* · `pollution-spread` · status: **sourced**

Pollution emitted by sources accumulates and diffuses across land, water, or air cells and harms health, land value, or growth, or provokes threats.

| field | value |
|---|---|
| aliases | pollution diffusion, contamination |
| family | Environment & ecology |
| substrate | Cellular grid, Aggregate stocks |
| math basis | Cellular automata, Continuum mechanics |
| feedback | Both |
| player interface | Placement, Observation only |
| legibility | 3 |
| emergence potential | 3 |
| authoring cost | 1 |
| compute cost | 2 |
| tuning difficulty | 3 |
| ai leverage | 2 |
| maturity | Classic |
| open questions | Can learned dispersion surrogates make air and water pollution fields physically plausible while staying cheap and legible? |
| core count *(computed)* | 2 |
| earliest game *(computed)* | [SimCity](../game/simcity-1989.md) |
| earliest year *(computed)* | 1989 |
| prevalence *(computed)* | 7 |
| prevalence share *(computed)* | 0.04 |
| subgenre spread *(computed)* | 4 |
| technique count *(computed)* | 1 |
| technique exposure *(computed)* | 0.188 |

## Definition

Owns a pollution value per cell or chunk. Each update, emitters add pollution, a fraction diffuses to neighboring cells, and terrain, vegetation, or water absorb some; other systems read the local value as a penalty to health, land value, crop growth, or happiness. Factorio stores pollution per 32x32-tile chunk, updates every 64 ticks, diffuses 2% to each cardinal neighbor once a chunk holds 15 or more, absorbs it by tile type and trees (trees are damaged above 60), and lets enemy spawners absorb it to fund attack waves. SimCity computes a pollution map from industry and traffic that depresses land value; Cities: Skylines separates ground, noise, and water pollution, and sewage released upstream contaminates water intakes downstream. Inputs are emitter locations and rates; outputs are a spatial field read by other systems.

## Player Experience

Growth leaves a visible stain. The player separates factories from homes, plants green buffers, and watches the overlay creep outward; in Factorio a bigger factory directly invites bigger attacks. Cleanup competes with expansion for the same resources.

## Design Levers

- emission rate per source and modifiers such as efficiency upgrades or filters
- diffusion fraction, minimum amount before diffusing, and grid resolution
- absorption by terrain, water, and vegetation, and whether absorbers are damaged
- what pollution affects: health, land value, crops, happiness, enemy aggression
- cleanup tools and their cost

## Failure Modes

- Pollution that only lowers land value is solved once by zoning distance and then ignored.
- Fine-grained diffusion with no threshold or chunking costs compute and produces smeared, unreadable fields.
- Effects carried by hidden channels, such as water contamination far downstream, read as unexplained sickness.

## Dynamics

- Zoning separates polluting and sensitive uses, which lengthens commutes and adds traffic.
- In Factorio pollution couples production scale to attack size, so efficiency becomes a defense strategy.
- Absorbers degrade under load, so a polluted region can tip into faster spread as forests die.

## Open Questions

- Can learned dispersion surrogates make air and water pollution fields physically plausible while staying cheap and legible?

## Backlinks (computed)

**affected by:** [Machine-learned weather forecasting](../technique/ml-weather-models.md)

**used by:** [Captain of Industry](../game/captain-of-industry.md), [Eco](../game/eco.md), [Factorio](../game/factorio.md), [SimCity](../game/simcity-1989.md), [SimCity (2013)](../game/simcity-2013.md), [SimCity 4](../game/simcity-4.md), [SimEarth](../game/simearth.md)

## Sources

- [Pollution](../source/src-factoriowiki-2026-pollution.md)
- [Micropolis: open-source SimCity source code](../source/src-hopkins-2008-micropolis.md)

---
Provenance: created in run `2026-10-24-taxonomy-m5`.
