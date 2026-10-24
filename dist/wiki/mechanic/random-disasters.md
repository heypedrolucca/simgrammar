# Random disasters

*Mechanic* · `random-disasters` · status: **sourced**

Stochastic disasters such as fires, floods, earthquakes, storms, or meteors strike at random times and places and damage the system.

| field | value |
|---|---|
| aliases | natural disasters, catastrophes |
| family | Risk & failure |
| substrate | Stochastic events, Cellular grid |
| math basis | Markov / stochastic processes, Probability / statistics |
| feedback | None |
| player interface | Observation only, Placement |
| legibility | 4 |
| emergence potential | 3 |
| authoring cost | 3 |
| compute cost | 2 |
| tuning difficulty | 2 |
| ai leverage | 2 |
| maturity | Classic |
| core count *(computed)* | 2 |
| earliest game *(computed)* | [Hamurabi](../game/hamurabi.md) |
| earliest year *(computed)* | 1968 |
| prevalence *(computed)* | 17 |
| prevalence share *(computed)* | 0.098 |
| subgenre spread *(computed)* | 7 |
| technique count *(computed)* | 1 |
| technique exposure *(computed)* | 0.188 |

## Definition

A hazard process samples each tick or cycle whether a disaster occurs, picks a type from a weighted table that may be conditioned on state, picks a location, and applies a damage template such as destroying tiles, starting fires, or flooding. In the SimCity engine (Micropolis), doDisasters fires with probability 1/481, 1/241, or 1/61 per cycle depending on difficulty, then chooses among fire, flood, tornado, earthquake, or nothing, and spawns a monster only if average pollution exceeds 60. Cities: Skylines Natural Disasters adds early-warning buildings and shelters; RimWorld adds short circuits, solar flares, and toxic fallout; Banished has tornadoes and fires. Unlike a crisis countdown, timing is unknown in advance. Inputs: difficulty, optional state conditions. Outputs: damage events and secondary hazards passed to fire, flood, or health systems.

## Player Experience

Background dread and sudden recovery work. The player builds redundancy, spreads out critical infrastructure, keeps cash in reserve, and then scrambles to rebuild when a disaster hits. Players who want a calm build often disable disasters, which shows how much they change the tone.

## Design Levers

- base frequency per difficulty level and whether the player can disable or manually trigger disasters
- type weights and state conditions, such as monsters tied to pollution or fires tied to dry weather
- magnitude distribution and area of effect
- warning time and mitigation tools (shelters, firefighters, seawalls, insurance)
- secondary effects that hand off to fire spread, flooding, or disease

## Failure Modes

- Large unmitigable disasters erase hours of building and read as arbitrary rather than as a test of preparation.
- Frequent small disasters turn into repetitive cleanup chores.
- If disasters are rare and easily disabled, the mechanic adds content that most players never see.

## Dynamics

- Players disperse and duplicate critical services so one hit cannot cripple the system.
- Disaster damage reduces income and service coverage, which can cascade into abandonment if reserves are thin.
- State-conditioned disasters turn neglected variables, such as pollution, into delayed risks.

## Open Questions

- Can learned physical simulators make disaster damage depend on how the player actually built, rather than on fixed templates?
- What warning lead time makes disasters feel like a test of preparation rather than bad luck?

## Backlinks (computed)

**affected by:** [Machine-learned weather forecasting](../technique/ml-weather-models.md)

**used by:** [Banished](../game/banished.md), [Cities: Skylines II](../game/cities-skylines-2.md), [Farming Simulator 25](../game/farming-simulator-25.md), [From Dust](../game/from-dust.md), [Hamurabi](../game/hamurabi.md), [Jurassic World Evolution](../game/jurassic-world-evolution.md), [Kingdoms and Castles](../game/kingdoms-and-castles.md), [Lemonade Stand](../game/lemonade-stand.md), [M.U.L.E.](../game/mule.md), [The Oregon Trail](../game/oregon-trail.md), [SimAnt](../game/simant.md), [SimCity](../game/simcity-1989.md), [SimCity 2000](../game/simcity-2000.md), [SimCity 4](../game/simcity-4.md), [SimEarth](../game/simearth.md), [SimTower](../game/simtower.md), [Surviving Mars](../game/surviving-mars.md)

## Sources

- [Micropolis: open-source SimCity source code](../source/src-hopkins-2008-micropolis.md)

---
Provenance: created in run `2026-10-24-taxonomy-m7`.
