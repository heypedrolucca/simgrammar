# Natural selection

*Mechanic* · `natural-selection` · status: **sourced**

Differential survival and reproduction by fitness shifts trait distributions across generations.

| field | value |
|---|---|
| aliases | evolution, survival of the fittest |
| family | Population & lineage |
| substrate | Agent-based, Stochastic events |
| math basis | Genetics / evolutionary computation, Population dynamics |
| feedback | Both |
| player interface | Observation only, Parameter |
| legibility | 2 |
| emergence potential | 5 |
| authoring cost | 1 |
| compute cost | 3 |
| tuning difficulty | 4 |
| ai leverage | 3 |
| maturity | Established |
| requires | [Trait inheritance](../mechanic/trait-inheritance.md) |
| core count *(computed)* | 3 |
| earliest game *(computed)* | [SimEarth](../game/simearth.md) |
| earliest year *(computed)* | 1990 |
| prevalence *(computed)* | 3 |
| prevalence share *(computed)* | 0.017 |
| subgenre spread *(computed)* | 2 |
| technique count *(computed)* | 2 |
| technique exposure *(computed)* | 0.438 |

## Definition

Owns no trait values itself; it is the rule that ties reproduction and death to how well an individual's traits fit the environment, so populations change without a designer choosing outcomes. Each generation, individuals that find food, avoid predators, and tolerate climate leave more offspring; with heritable variation the trait distribution moves toward fitter values, and when populations split by geography or genetic distance new species can form. Species: ALRE (Early Access 2018) charges energy for movement from skeleton forces and torques, lets creatures eat only within head reach, and defines species by interbreeding within a genetic distance. SimLife (1992) lets players edit genetics and environments and watch evolution. Spore (2008), by contrast, has players design creatures directly and is not natural selection. Inputs: heritable traits, environment, mortality and reproduction. Outputs: changing trait distributions, speciation, extinction.

## Player Experience

The player shifts from designer to gardener: setting conditions and watching which bodies and behaviors win. Results surprise and teach, as in finding why the long-necked line died out after an ice age.

## Design Levers

- fitness sources (energy budgets, predation, climate tolerance, mate choice)
- generation time relative to play pace
- population size, which sets drift versus selection strength
- speciation rule (genetic distance, geography)
- player interventions such as culling, feeding, catastrophes, and nurseries

## Failure Modes

- Evolution is too slow to see within a session, so players perceive nothing happening.
- Degenerate optima: populations converge on one exploit body plan and diversity collapses.
- Fitness hidden behind physics is opaque, so players cannot tell why traits win.
- Games that call designed progression evolution set expectations they do not meet; biologists criticized Spore's model.

## Dynamics

- Arms races between predator and prey traits.
- Environmental shocks cause extinction and radiation into emptied niches.
- Coupled with food webs, species composition and trait distributions shift together.

## Open Questions

- Can learned simulators or GPU-accelerated physics make open-ended evolution fast enough to watch in a session?
- What visualizations let players see selection pressure acting, not just its outcome?

## Relations

**requires**

- [Trait inheritance](../mechanic/trait-inheritance.md)

**synergy**

- [Trait inheritance](../mechanic/trait-inheritance.md): Selection needs heritable variation; inheritance needs selection to produce adaptation.

## Backlinks (computed)

**affected by:** [Continuous cellular automata and foundation-model search for artificial life](../technique/continuous-alife-and-asal.md), [Massively parallel GPU simulation](../technique/massively-parallel-simulation.md)

**involved in:** [Open-ended evolution sandbox](../opportunity/open-ended-evolution-sandbox.md)

**used by:** [SimEarth](../game/simearth.md), [SimLife](../game/simlife.md), [Species: Artificial Life, Real Evolution](../game/species-alre.md)

## Sources

- [Devblog #5: Thrive vs Species](../source/src-revolutionarygames-2016-thrive-vs-species.md)
- [Species 0.7.0 Released!](../source/src-quasar-2014-species-0-7-0.md)
- [Species: Artificial Life, Real Evolution on Steam](../source/src-steam-2026-species-alre.md)
- [SimLife](../source/src-wikipedia-simlife.md)
- [Spore (2008 video game)](../source/src-wikipedia-spore.md)

---
Provenance: created in run `2026-10-24-taxonomy-m3`; reviewed in `2026-10-24-review-fixes`.
