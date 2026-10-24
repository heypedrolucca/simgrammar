# Continuous cellular automata and foundation-model search for artificial life

*Technique* · `continuous-alife-and-asal` · status: **sourced**

Continuous cellular automata such as Lenia and mass-conserving Flow-Lenia produce lifelike self-organizing creatures, and ASAL uses vision-language foundation models to search their rule spaces for phenomena described in text or for open-ended novelty.

| field | value |
|---|---|
| aliases | Lenia, Flow-Lenia, ASAL, Automated Search for Artificial Life |
| category | Artificial life research |
| year | 2024 |
| maturity | Research |
| trl | 3 |
| runtime | Design assist, Offline authoring, Client real-time |
| determinism impact | Preserves |
| horizon | 3-5 years |
| risks | Controllability, Legibility, Evaluation difficulty |
| deployed in |  |
| affects count *(computed)* | 3 |

## Summary

Continuous cellular automata such as Lenia and mass-conserving Flow-Lenia produce lifelike self-organizing creatures, and ASAL uses vision-language foundation models to search their rule spaces for phenomena described in text or for open-ended novelty.

## Mechanism

Lenia stores a continuous field A(x) in [0,1]. Each step it convolves A with a smooth ring-shaped kernel K, passes the result through a bell-shaped growth function G, and updates A by a small time step dt times G(K*A), clipped to [0,1]; certain kernel and growth parameters yield moving, self-maintaining patterns ('species'). Flow-Lenia replaces additive growth with an affinity field that moves matter along its gradient, conserving total mass, and stores the rule parameters in the matter itself, so creatures carrying different rules can coexist, collide and mix. ASAL renders a simulation, embeds the frames with a vision-language foundation model, and scores parameter sets by similarity to a text prompt, by novelty of the embedding trajectory over time, or by diversity across a population; an evolutionary optimizer then searches the substrate's parameters (Boids, Particle Life, Game of Life, Lenia, NCA).

## Limitations

- Lenia creatures exist in a narrow band of parameter space; most settings die out or explode, which is what made search tools necessary.
- Creatures are fields without discrete identity, needs or stats, so connecting them to resource economies or player goals needs extra interpretation layers.
- ASAL scores runs with a foundation model on rendered frames, which is offline-scale compute and inherits that model's notion of what looks interesting.
- Open-ended evolution in these substrates is a stated aim, not an established result.

## Relations

**affects**

- [Natural selection](../mechanic/natural-selection.md) (Enables new form): In Flow-Lenia, rules travel with matter, so selection can act on creatures that emerge from the physics itself rather than on declared fitness stats.
- [Trait inheritance](../mechanic/trait-inheritance.md) (Deepens): Rule parameters mix where creatures meet in Flow-Lenia, giving inheritance and hybridization as a spatial process instead of an explicit genome crossover function.
- [Generative content on demand](../mechanic/generative-content.md) (Enables new form): ASAL turns a text prompt into a search over simulation rules that produce the described phenomenon, a route to generating new creature rule sets from player or designer descriptions at design time.

## Backlinks (computed)

**applied in:** [Open-ended evolution sandbox](../opportunity/open-ended-evolution-sandbox.md)

## Claims

- Lenia catalogued over 400 species in 18 families of geometric, segmented, resilient lifeforms, many found by interactive evolutionary search. *(confidence: high)* [[114](../source/src-chan-2019-lenia.md)]
- Flow-Lenia's mass conservation made localized creatures easier to find, and parameter localization let multiple species with different rules coexist and interact in one world. *(confidence: high)* [[115](../source/src-plantec-2023-flow-lenia.md)]
- ASAL found previously unseen Lenia and Boids lifeforms and open-ended cellular automata in the style of Game of Life, and quantified qualitative phenomena in ways that aligned with human judgment. *(confidence: medium)* [[116](../source/src-kumar-2024-asal.md)]

## Sources

- [Lenia: Biology of Artificial Life](../source/src-chan-2019-lenia.md)
- [Flow-Lenia: Towards open-ended evolution in cellular automata through mass conservation and parameter localization](../source/src-plantec-2023-flow-lenia.md)
- [Automating the Search for Artificial Life with Foundation Models](../source/src-kumar-2024-asal.md)

---
Provenance: created in run `2026-10-24-techniques-sim-math`.
