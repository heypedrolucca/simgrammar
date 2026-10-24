# Physical-world foundation models

*Technique* · `physical-world-foundation-models` · status: **sourced**

Video-pretrained models of physical dynamics, NVIDIA Cosmos for generating action-conditioned training video and Meta's V-JEPA 2 for latent prediction and planning, target robotics and driving rather than games.

| field | value |
|---|---|
| aliases | NVIDIA Cosmos, V-JEPA 2, world foundation models |
| category | Generative world model |
| year | 2025 |
| maturity | Research |
| trl | 3 |
| runtime | Offline authoring, Server real-time |
| determinism impact | Breaks |
| horizon | 5+ years |
| risks | Determinism, Consistency / hallucination, Compute cost, Evaluation difficulty, Controllability |
| builds on | [Massively parallel GPU simulation](../technique/massively-parallel-simulation.md) |
| affects count *(computed)* | 3 |

## Summary

Video-pretrained models of physical dynamics, NVIDIA Cosmos for generating action-conditioned training video and Meta's V-JEPA 2 for latent prediction and planning, target robotics and driving rather than games.

## Mechanism

Cosmos curates about 20M hours of raw video into about 100M clips, compresses them with causal video tokenizers, and pretrains diffusion (Text2World, Video2World) and autoregressive world models that developers post-train into action- or camera-conditioned simulators; Cosmos 3 (2026) is an omni family at 4B, 16B, and 64B parameters. V-JEPA 2 instead predicts masked video in a learned embedding space, not pixels, from over 1M hours of video; its action-conditioned variant V-JEPA 2-AC is post-trained on under 62 hours of robot video and plans by searching for action sequences whose predicted embedding approaches a goal image.

## Limitations

- Designed for robots and vehicles; no game integration or game-specific evaluation exists in the cited sources.
- Physical plausibility is unreliable: video models are at or near chance on IntPhys 2.
- Large models (up to 64B in Cosmos 3) are far from per-player real-time budgets.
- V-JEPA 2 predicts at a single time scale, limiting long-horizon planning (Meta's stated limitation).

## Relations

**affects**

- [Vehicle dynamics](../mechanic/vehicle-dynamics.md) (Replaces substrate): Cosmos is positioned for autonomous-vehicle training and closed-loop evaluation; a driving model post-trained from it predicts scene video under driving inputs with no tire or suspension model, which suits traffic scenarios more than the handling fidelity a racing sim needs.
- [Rigid-body physics](../mechanic/rigid-body-physics.md) (Replaces substrate): Learned video dynamics could stand in for a physics engine in open-ended scenes, but near-chance IntPhys 2 scores show current models do not reliably reject impossible motion.
- [Utility action selection](../mechanic/utility-action-selection.md) (Replaces substrate): V-JEPA 2-AC scores candidate action sequences by predicted distance to a goal image in latent space, a learned alternative to hand-written utility curves for agents whose goals can be pictured.

**builds on**

- [Massively parallel GPU simulation](../technique/massively-parallel-simulation.md)

## Claims

- Cosmos (January 2025) pretrained diffusion and autoregressive world foundation models on about 100M clips curated from about 20M hours of video and released them as open weights with permissive licenses. *(confidence: high)* [[261](../source/src-nvidia-2025-cosmos-wfm.md)]
- Cosmos 3 ships Super 64B, Nano 16B, and Edge 4B models under the OpenMDW1.1 license, positioned for autonomous vehicle and robot synthetic data, closed-loop evaluation, and robot policy training, with no mention of games. *(confidence: high)* [[262](../source/src-nvidia-2026-cosmos-page.md)]
- V-JEPA 2-AC, post-trained on under 62 hours of DROID robot video, performed zero-shot pick-and-place with image goals on Franka arms in two labs without task-specific data or reward. *(confidence: high)* [[263](../source/src-assran-2025-v-jepa-2.md)]
- On Meta's IntPhys 2 benchmark of physical plausibility, current video models including V-JEPA 2 score at or near chance while humans score 85 to 95 percent across the released benchmarks. *(confidence: high)* [[264](../source/src-meta-2025-v-jepa-2-blog.md)]

## Sources

- [Cosmos World Foundation Model Platform for Physical AI](../source/src-nvidia-2025-cosmos-wfm.md)
- [NVIDIA Cosmos](../source/src-nvidia-2026-cosmos-page.md)
- [V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning](../source/src-assran-2025-v-jepa-2.md)
- [Introducing V-JEPA 2 world model and new physical reasoning benchmarks](../source/src-meta-2025-v-jepa-2-blog.md)

---
Provenance: created in run `2026-10-24-techniques-world-models`; reviewed in `2026-10-24-review-fixes`.
