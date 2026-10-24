# Subspace neural physics and learned deformers

*Technique* · `subspace-neural-physics` · status: **sourced**

Small networks trained on offline cloth, flesh, or muscle simulation predict deformation in a compressed subspace or as corrective morph targets, running hundreds to thousands of times faster than the source simulation inside a game engine.

| field | value |
|---|---|
| aliases | Ubisoft subspace neural physics, Unreal ML Deformer, learned cloth deformation, neural morph model |
| category | Neural physics & surrogates |
| year | 2019 |
| maturity | Prototype |
| trl | 6 |
| runtime | Client real-time, Offline authoring |
| determinism impact | Preserves |
| horizon | Now |
| risks | Consistency / hallucination, Controllability |
| deployed in |  |
| affects count *(computed)* | 2 |

## Summary

Small networks trained on offline cloth, flesh, or muscle simulation predict deformation in a compressed subspace or as corrective morph targets, running hundreds to thousands of times faster than the source simulation inside a game engine.

## Mechanism

Developers run an expensive offline simulation (cloth, soft tissue, muscle, volume-preserving flesh) over many randomized poses or interactions. Vertex positions are compressed, for example with principal component analysis, into a low-dimensional subspace. A small network is trained to predict the next subspace coordinates from the current coordinates plus external inputs such as bone transforms or collider positions (Holden et al. 2019), or to predict per-pose corrective morph-target weights applied on top of linear skinning (Unreal Engine ML Deformer, Neural Morph Model and Nearest Neighbor Model). At runtime only the network and the decode from subspace to full mesh run, on the GPU.

## Limitations

- Quality holds only near the training distribution of poses and interactions; unusual poses or collisions produce artifacts, so coverage of the offline dataset sets the limit.
- Training is heavy: Unreal's documentation notes long training times and Alembic training caches of 50-100 GB.
- GPU memory for morph targets is the main runtime cost, and compression settings trade memory and speed for quality.
- Output is usually cosmetic; it does not feed back into gameplay physics unless the game reads the deformed state, which brings determinism and consistency issues.
- No commercial title using these models at runtime was confirmed in this run's sources.

## Relations

**affects**

- [Soft-body deformation](../mechanic/soft-body-deformation.md) (Accelerates): Deformation learned from an offline solver runs 300-5000x faster than that solver, putting near-offline-quality cloth and flesh response within a real-time budget.
- [Embodied skill control](../mechanic/embodied-skill-control.md) (Deepens): Hands-on tasks such as surgery or handling soft objects could show tissue and cloth reacting plausibly to tools in real time, adding feedback the player reads to perform the skill.

## Claims

- Ubisoft La Forge's subspace neural physics ran interactive cloth and deformable simulation 300 to 5000 times faster than conventional simulation at a small additional memory cost (the project page states 300 to 4000). *(confidence: medium)* [[308](../source/src-holden-2019-subspace-neural-physics.md), [309](../source/src-ubisoft-2019-data-driven-physics.md), [310](../source/src-holden-2020-gdc-squishy-bunnies.md)]
- Unreal Engine's ML Deformer trains models on externally generated deformation caches from Maya or Houdini and applies them at runtime as GPU morph targets; the Neural Morph Model is the recommended default and the cloth-oriented Nearest Neighbor Model is marked experimental. *(confidence: high)* [[311](../source/src-epic-2026-ml-deformer.md)]

## Sources

- [Subspace Neural Physics: Fast Data-Driven Interactive Simulation](../source/src-holden-2019-subspace-neural-physics.md)
- [Ubisoft La Forge produces a data-driven physics simulation based on machine learning](../source/src-ubisoft-2019-data-driven-physics.md)
- [Machine Learning: Physics Simulation, Kolmogorov Complexity, and Squishy Bunnies](../source/src-holden-2020-gdc-squishy-bunnies.md)
- [How to use the Machine Learning Deformer in Unreal Engine](../source/src-epic-2026-ml-deformer.md)

---
Provenance: created in run `2026-10-24-techniques-sim-math`.
