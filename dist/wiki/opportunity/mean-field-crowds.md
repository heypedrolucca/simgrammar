# Mean-field crowds and traffic

*Opportunity* · `mean-field-crowds` · status: **asserted**

Simulate hundreds of thousands of agents with equilibrium-consistent route and choice behavior by combining mean-field approximations with sampled individuals.

| field | value |
|---|---|
| opportunity type | Infrastructure |
| involves | [Traffic congestion](../mechanic/traffic-congestion.md), [Agent pathfinding](../mechanic/agent-pathfinding.md), [Crowd preferences](../mechanic/crowd-preferences.md), [Public transit lines](../mechanic/public-transit.md), [Service queues](../mechanic/service-queues.md) |
| applies | [Mean field games and mean-field learning](../technique/mean-field-games.md), [Massively parallel GPU simulation](../technique/massively-parallel-simulation.md) |
| precedent | [Cities: Skylines II](../game/cities-skylines-2.md), [SimCity (2013)](../game/simcity-2013.md), [Cities: Skylines](../game/cities-skylines.md), [Planet Coaster](../game/planet-coaster.md) |
| novelty | 4 |
| feasibility | 3 |
| impact | 3 |
| horizon | 3-5 years |
| falsifiable signal | {'prediction': 'A city builder will document a mean-field or continuum crowd model as its primary traffic or population simulation.', 'resolve_by': '2029-12-31', 'criteria': 'Released or patched after 2026-10-24 in a title with at least 1,000 Steam user reviews; developer documentation names a mean-field, continuum, or equilibrium-field method used at runtime for the main traffic or population model.'} |
| priority *(computed)* | 3.178 |

## Thesis

City builders face a ceiling where individually simulated agents cap population and aggregate models feel lifeless. Mean-field game theory describes how large populations of optimizing agents reach equilibrium, and GPU-parallel simulation makes iterating those fields cheap. A hybrid where the mean field sets congestion and choice probabilities and a sample of visible individuals follows them gives large populations that behave coherently.

## Design Sketch

Traffic and pedestrian flows are fields updated each tick from a mean-field equilibrium solver on the GPU; visible cars and citizens are samples drawn from those fields, so congestion is consistent at scale while inspection still shows individuals with plausible trips.

## Key Risks

- Players notice when sampled individuals behave inconsistently with fields.
- Equilibrium solvers can be slow to converge under rapid change.
- Engineering cost to retrofit existing engines.

## Validation Experiment

Implement a mean-field traffic solver on a 100,000-trip city network and compare travel-time distributions with a full agent-based baseline. Success: within 10 percent on mean and 90th percentile travel times at a tenth of the compute.

## Falsifiable signal

- **Prediction:** A city builder will document a mean-field or continuum crowd model as its primary traffic or population simulation.
- **Resolve by:** 2029-12-31
- **Criteria:** Released or patched after 2026-10-24 in a title with at least 1,000 Steam user reviews; developer documentation names a mean-field, continuum, or equilibrium-field method used at runtime for the main traffic or population model.

## Relations

**applies**

- [Mean field games and mean-field learning](../technique/mean-field-games.md)
- [Massively parallel GPU simulation](../technique/massively-parallel-simulation.md)

**involves**

- [Traffic congestion](../mechanic/traffic-congestion.md)
- [Agent pathfinding](../mechanic/agent-pathfinding.md)
- [Crowd preferences](../mechanic/crowd-preferences.md)
- [Public transit lines](../mechanic/public-transit.md)
- [Service queues](../mechanic/service-queues.md)

**precedent**

- [Cities: Skylines II](../game/cities-skylines-2.md)
- [SimCity (2013)](../game/simcity-2013.md)
- [Cities: Skylines](../game/cities-skylines.md)
- [Planet Coaster](../game/planet-coaster.md)

---
Provenance: created in run `2026-10-24-synthesis`; reviewed in `2026-10-24-review-fixes`.
