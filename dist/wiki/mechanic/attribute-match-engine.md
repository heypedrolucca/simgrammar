# Attribute-driven match engine

*Mechanic* · `attribute-match-engine` · status: **sourced**

Contest outcomes are simulated play by play from participant attributes, tactics, and randomness instead of being played directly.

| field | value |
|---|---|
| aliases | match engine, sim engine, play-by-play simulation |
| family | Agents & behavior |
| substrate | Stochastic events, Agent-based |
| math basis | Markov / stochastic processes, Probability / statistics |
| feedback | None |
| player interface | Parameter, Observation only |
| legibility | 2 |
| emergence potential | 3 |
| authoring cost | 3 |
| compute cost | 2 |
| tuning difficulty | 4 |
| ai leverage | 3 |
| maturity | Classic |
| core count *(computed)* | 3 |
| earliest game *(computed)* | [Out of the Park Baseball](../game/out-of-the-park-baseball.md) |
| earliest year *(computed)* | 1999 |
| prevalence *(computed)* | 3 |
| prevalence share *(computed)* | 0.017 |
| subgenre spread *(computed)* | 1 |
| technique count *(computed)* | 2 |
| technique exposure *(computed)* | 0.2 |

## Definition

Owns the state of a contest in progress (score, clock, possession or positions, fatigue, morale) and each participant's attribute vector and tactical instructions. Each step the engine selects the next event (pass, shot, pitch, overtake) and resolves it by sampling probabilities computed from the involved participants' attributes, the tactics in force, fatigue, and context, then updates state and emits commentary or animation. Football Manager, which continues the Championship Manager series begun in 1992, renders its engine as text, as a 2D pitch from Football Manager 2005, and in 3D from Football Manager 2009; Out of the Park Baseball reports simulated games as text play-by-play; Motorsport Manager resolves races from driver and car ratings with player pit and pace calls. Inputs: lineups, attributes, tactics, in-match interventions. Outputs: results, per-participant statistics, injuries, and form that feed rosters, morale, and finances.

## Player Experience

The player is the coach in the stands: setting lineups and tactics, watching a sampled stream of events, and reading results as evidence about whether decisions worked. Upsets feel earned or cruel; across a season noisy results become stories about form, slumps, and tactical identity.

## Design Levers

- event granularity (per possession, per pitch, per lap) and how many events are rendered to the player
- mapping from attributes to event probabilities and the weight of randomness relative to ratings
- tactical instruction set and how strongly each instruction shifts event probabilities
- fatigue, morale, and home-advantage modifiers
- in-match interventions such as substitutions, touchline shouts, and pit calls

## Failure Modes

- One tactic or formation dominates because the engine overweights a parameter, and the player community converges on it.
- Low-variance engines make results feel predetermined by ratings; high-variance engines make tactics feel irrelevant.
- Rendered visuals that disagree with the underlying event logic undermine trust in the simulation.
- Players cannot tell bad luck from bad decisions because the attribute-to-outcome mapping is opaque.

## Dynamics

- Results feed morale, form, finances, and transfers, so streaks compound into dynasties or collapses.
- Communities reverse-engineer engine weights into a tactical meta, which yearly engine revisions then disrupt.
- Simulated statistics become scouting data, coupling the engine to player valuation and transfer markets.

## Open Questions

- Can event models trained on real tracking or event data replace hand-tuned probabilities while keeping tactics legible to players?
- Can generated commentary explain why an event happened in terms of attributes and tactics, so players can separate luck from decisions?

## Relations

**synergy**

- [Scouting knowledge](../mechanic/scouting-knowledge.md): Hidden attributes make scouting valuable because they drive simulated outcomes (Football Manager).

## Backlinks (computed)

**affected by:** [Massively parallel GPU simulation](../technique/massively-parallel-simulation.md), [Simulation-based inference for calibrating simulators](../technique/simulation-based-inference.md)

**used by:** [Football Manager](../game/football-manager.md), [Motorsport Manager](../game/motorsport-manager.md), [Out of the Park Baseball](../game/out-of-the-park-baseball.md)

## Sources

- [Football Manager](../source/src-wikipedia-football-manager.md)
- [Out of the Park Baseball](../source/src-wikipedia-out-of-the-park-baseball.md)

---
Provenance: created in run `2026-10-24-taxonomy-m3`.
