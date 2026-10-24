# Open real-time interactive video world models

*Technique* · `open-interactive-video-models` · status: **sourced**

Open and startup interactive video models (Matrix-Game, Hunyuan-GameCraft, WorldPlay, Yan, Mirage, Odyssey) adapt pretrained video diffusion transformers to keyboard and mouse control and stream frames in real time, adding pose-indexed memory and text edits during play.

| field | value |
|---|---|
| aliases | Matrix-Game, Hunyuan-GameCraft, WorldPlay, Yan, Mirage, Odyssey-2 |
| category | Generative world model |
| year | 2025 |
| maturity | Prototype |
| trl | 6 |
| runtime | Server real-time |
| determinism impact | Breaks |
| horizon | 3-5 years |
| risks | Determinism, Consistency / hallucination, Compute cost, IP / provenance, Controllability, Latency |
| builds on | [Diffusion and autoregressive neural game engines](../technique/diffusion-game-engines.md) |
| affects count *(computed)* | 6 |

## Summary

Open and startup interactive video models (Matrix-Game, Hunyuan-GameCraft, WorldPlay, Yan, Mirage, Odyssey) adapt pretrained video diffusion transformers to keyboard and mouse control and stream frames in real time, adding pose-indexed memory and text edits during play.

## Mechanism

A pretrained text- or image-to-video diffusion transformer (SkyReels-V2 for Matrix-Game 2.0, HunyuanVideo for GameCraft) gets action modules: keyboard and mouse mapped to camera translation and rotation, injected through cross-attention, token addition, or Plucker camera embeddings. Training uses gameplay recordings from Unreal Engine scenes, GTA V, Minecraft, Temple Run, or 100+ AAA titles. The bidirectional model is then distilled into a causal few-step generator (Self-Forcing with distribution matching, or phased consistency models) that streams chunks with a rolling KV cache. 2026 systems add memory by retrieving past frames whose camera pose overlaps the current view (Matrix-Game 3.0, WorldPlay). Yan, Mirage 2, and Odyssey-2 accept typed text during play to edit the world.

## Limitations

- Resolution and speed trade against hardware: Matrix-Game 2.0 is 352x640 on one H100, Matrix-Game 3.0's 720p 40 fps needs 9 GPUs, and GameCraft runs at 6.6 fps after distillation.
- Consistency horizon is about a minute even with retrieval memory; earlier open models have no explicit memory at all.
- Training data includes recordings of commercial games (GTA V, 100+ AAA titles), so output provenance is contested.
- Stronger history conditioning improves consistency but reduces responsiveness to new actions (GameCraft ablation).
- Action spaces cover camera movement and basic locomotion; game verbs such as shooting, building, or trading are not modeled.

## Sources

- src-he-2025-matrix-game-2
- src-li-2025-hunyuan-gamecraft
- src-tencent-2025-hunyuan-gamecraft-weights
- src-tencent-2025-yan
- src-wang-2026-matrix-game-3
- src-sun-2025-worldplay
- src-thedecoder-2025-mirage-2
- src-odyssey-2025-odyssey-2

## Relations

**affects**

- [Vehicle dynamics](../mechanic/vehicle-dynamics.md) (Replaces substrate): Matrix-Game 2.0 was fine-tuned on 574 hours of GTA driving; car handling is reproduced from video rather than tire and suspension models, with no guarantee of consistent grip or mass.
- [Direct avatar control](../mechanic/direct-avatar.md) (Replaces substrate): Walking, turning, and jumping are rendered from a unified camera-action space; GameCraft's action space lacks shooting, throwing, and explosions.
- [Procedural terrain](../mechanic/procedural-terrain.md) (Enables new form): A world starts from any image, sketch, or photo (Mirage 2, GameCraft); pose-indexed memory in Matrix-Game 3.0 and WorldPlay lets revisited areas stay consistent for about a minute, still far short of a save file.
- [Generative content on demand](../mechanic/generative-content.md) (Enables new form): Typed text during play adds or restyles objects and scenes (Yan editing, Mirage 2 commands, Odyssey-2 prompts), so content is requested at runtime rather than authored.
- [Content sharing](../mechanic/content-sharing.md) (Enables new form): Mirage 2 lets players save and share generated worlds; what is shared is a prompt and seed image for a model rather than an asset bundle, so the receiver needs the same hosted model.
- [Rigid-body physics](../mechanic/rigid-body-physics.md) (Replaces substrate): Contact and motion responses come from video priors; out-of-domain views degrade (Matrix-Game 2.0 reports over-saturation under sustained upward or forward camera motion).

**builds on**

- [Diffusion and autoregressive neural game engines](../technique/diffusion-game-engines.md)

## Backlinks (computed)

**applied in:** [Generated dream and replay views](../opportunity/dream-replay-layer.md)

## Claims

- Matrix-Game 2.0 (Skywork, August 2025) streams 352x640 video at 25 fps on one H100 with about 1.8B parameters trained on about 1,200 hours of Unreal Engine, GTA driving, Minecraft, and Temple Run data, and releases weights and code; it has no explicit memory. *(confidence: high)* [[250](../source/src-he-2025-matrix-game-2.md)]
- Hunyuan-GameCraft trained on over 1M recordings from more than 100 AAA titles; distillation raised speed from 0.25 to 6.6 fps with under 5 seconds latency per action, and weights released in August 2025 need at least 24 GB of GPU memory (80 GB recommended). *(confidence: high)* [[251](../source/src-li-2025-hunyuan-gamecraft.md), [252](../source/src-tencent-2025-hunyuan-gamecraft-weights.md)]
- Yan (Tencent, August 2025) reports 1080p at 50 to 60 fps for its simulation module trained on the game Yuan Meng Star and an editing module that separates interactive mechanics simulation from visual rendering so text can restyle the world during play. *(confidence: medium)* [[253](../source/src-tencent-2025-yan.md)]
- Matrix-Game 3.0 (April 2026) reaches up to 40 fps at 720p with a 5B model on an 8+1 GPU setup and keeps minute-long consistency by retrieving memory frames by camera pose; WorldPlay (Tencent Hunyuan) streams 720p at 24 fps with a reconstituted context memory for long-term geometric consistency. *(confidence: high)* [[254](../source/src-wang-2026-matrix-game-3.md), [255](../source/src-sun-2025-worldplay.md)]
- Mirage 2 (Dynamics Lab, August 2025) lets players turn photos or sketches into browser-playable worlds and change them by typing commands, with saved and shared worlds, but struggles with precise controls and visual stability; Odyssey-2 (October 2025) generates each frame in under 50 ms from text prompts. *(confidence: medium)* [[256](../source/src-thedecoder-2025-mirage-2.md), [257](../source/src-odyssey-2025-odyssey-2.md)]

## Sources

- [Matrix-Game 2.0: An Open-Source, Real-Time, and Streaming Interactive World Model](../source/src-he-2025-matrix-game-2.md)
- [Hunyuan-GameCraft: High-dynamic Interactive Game Video Generation with Hybrid History Condition](../source/src-li-2025-hunyuan-gamecraft.md)
- [Hunyuan-GameCraft-1.0 model card](../source/src-tencent-2025-hunyuan-gamecraft-weights.md)
- [Yan: Foundational Interactive Video Generation](../source/src-tencent-2025-yan.md)
- [Matrix-Game 3.0: Real-Time and Streaming Interactive World Model with Long-Horizon Memory](../source/src-wang-2026-matrix-game-3.md)
- [WorldPlay: Towards Long-Term Geometric Consistency for Real-Time Interactive World Modeling](../source/src-sun-2025-worldplay.md)
- [Mirage 2 allows users to turn sketches and photos into interactive game worlds](../source/src-thedecoder-2025-mirage-2.md)
- [Introducing Odyssey-2: A General-Purpose World Model](../source/src-odyssey-2025-odyssey-2.md)

---
Provenance: created in run `2026-10-24-techniques-world-models`; reviewed in `2026-10-24-review-fixes`.
