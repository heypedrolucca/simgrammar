# Diffusion and autoregressive neural game engines

*Technique* · `diffusion-game-engines` · status: **sourced**

Action-conditioned generative models trained on recordings of one existing game predict each next frame from recent frames and player input, so the model itself plays the role of the game engine.

| field | value |
|---|---|
| aliases | neural game engine, GameNGen, DIAMOND, Oasis, MineWorld |
| category | Generative world model |
| year | 2024 |
| maturity | Prototype |
| trl | 6 |
| runtime | Server real-time, Client real-time |
| determinism impact | Breaks |
| horizon | 3-5 years |
| risks | Consistency / hallucination, Compute cost, Controllability, IP / provenance, Latency |
| affects count *(computed)* | 5 |

## Summary

Action-conditioned generative models trained on recordings of one existing game predict each next frame from recent frames and player input, so the model itself plays the role of the game engine.

## Mechanism

A game is recorded as pairs of frames and player actions (from an RL agent in GameNGen, human play in DIAMOND's CS:GO model, or gameplay video in Oasis). A generator is trained to predict frame t+1 from the last N frames and the action at t: a latent diffusion model in GameNGen, DIAMOND, and Oasis, or a transformer over interleaved image and action tokens in MineWorld. Context frames are noised during training (noise augmentation, Diffusion Forcing, dynamic noising) so the model can recover from its own errors during long rollouts, and sampling is cut to a few denoising steps for real-time play. There is no explicit game state: position, health, enemies, and map layout exist only as pixels or latents inside the context window, so anything that leaves the window is forgotten unless it is visible on screen.

## Limitations

- Memory is a few seconds: GameNGen's 64-frame context covers about 3 seconds, and Oasis shows about 3 seconds of memory in one example, so off-screen state such as map layout or enemy positions is lost.
- Requires an existing game to record: GameNGen needed about 70M agent frames from DOOM, DIAMOND 87 hours of CS:GO play; the approach clones a game rather than authoring a new one.
- Each player needs a dedicated accelerator (one TPU-v5 for GameNGen, H100s for Oasis); Maginative reports cost remains a significant barrier to deploying such models at scale, and no per-player-hour figure is published.
- State such as health, ammo, inventory, and score is only as reliable as the pixels that show it; Oasis inventory control is imprecise and distant geometry is fuzzy.
- Training on footage of commercial games raises unresolved licensing questions.

## Sources

- src-valevski-2024-gamengen
- src-alonso-2024-diamond
- src-decart-2024-oasis
- src-techcrunch-2024-decart-oasis
- src-maginative-2024-decart-oasis
- src-infoq-2024-decart-etched-oasis
- src-guo-2025-mineworld

## Relations

**affects**

- [Direct avatar control](../mechanic/direct-avatar.md) (Replaces substrate): Avatar movement, camera response, and weapon use are predicted frame by frame from keyboard and mouse input instead of computed by engine code; responsiveness depends on denoising steps and frame rate (20 fps GameNGen and Oasis, about 10 fps DIAMOND CS:GO).
- [Rigid-body physics](../mechanic/rigid-body-physics.md) (Replaces substrate): Collision, gravity, and jumping are learned statistically from pixels rather than integrated; rules the data rarely violates can still be broken, as with DIAMOND's repeated mid-air jumps in CS:GO.
- [Procedural terrain](../mechanic/procedural-terrain.md) (Enables new form): Terrain is invented on demand from the learned distribution of the training game with no seed or noise function (Oasis), but it is not persistent: regions that leave the short context window are regenerated differently on return.
- [Generative content on demand](../mechanic/generative-content.md) (Enables new form): Every frame, enemy, and pickup is generated content conditioned on play, so a game can in principle contain situations its source game never had; in practice output stays inside the training game's distribution.
- [Voxel destruction](../mechanic/voxel-destruction.md) (Replaces substrate): In Oasis and MineWorld, breaking and placing Minecraft blocks is predicted as pixels with no stored voxel grid, so edits are not durable; Oasis placing a dirt block can bring up an entirely different environment.

## Backlinks (computed)

**applied in:** [Generated dream and replay views](../opportunity/dream-replay-layer.md), [Symbolic simulation, neural rendering](../opportunity/symbolic-sim-neural-render.md)

**built upon by:** [Open real-time interactive video world models](../technique/open-interactive-video-models.md), [Real-time generative restyling of game video](../technique/real-time-video-restyling.md)

## Claims

- GameNGen simulates DOOM at 20 frames per second on a single TPU, with next-frame PSNR of 29.43; human raters picked the real game over the simulation only 58 percent (1.6 s clips) and 60 percent (3.2 s clips) of the time. *(confidence: high)* [[126](../source/src-valevski-2024-gamengen.md)]
- GameNGen conditions on 64 past frames (about 3 seconds) and was trained on about 70M frames recorded from a PPO agent trained for 50M environment steps; the authors state the model cannot be used to create new games. *(confidence: high)* [[126](../source/src-valevski-2024-gamengen.md)]
- DIAMOND reached a mean human-normalized score of 1.46 on Atari 100k for agents trained entirely inside a diffusion world model, and a CS:GO world model trained on 87 hours of human play runs at about 10 fps on an RTX 3090 but lets the player jump repeatedly in mid-air, which the real game forbids. *(confidence: high)* [[127](../source/src-alonso-2024-diamond.md)]
- Oasis (Decart and Etched, October 2024) generated a Minecraft-like open world at 20 fps in a public browser demo with 500M-parameter open weights; reviewers found the layout rearranged after turning around, and Decart did not say it had Microsoft's permission to train on Minecraft footage. *(confidence: high)* [[128](../source/src-decart-2024-oasis.md), [129](../source/src-techcrunch-2024-decart-oasis.md), [130](../source/src-infoq-2024-decart-etched-oasis.md)]
- MineWorld (Microsoft Research, 2025) released an open visual-action autoregressive transformer for Minecraft that generates 4 to 7 frames per second depending on model scale. *(confidence: high)* [[131](../source/src-guo-2025-mineworld.md)]

## Sources

- [Diffusion Models Are Real-Time Game Engines](../source/src-valevski-2024-gamengen.md)
- [Diffusion for World Modeling: Visual Details Matter in Atari](../source/src-alonso-2024-diamond.md)
- [Oasis project page (Decart and Etched)](../source/src-decart-2024-oasis.md)
- [Decart's AI simulates a real-time, playable version of Minecraft](../source/src-techcrunch-2024-decart-oasis.md)
- [Decart Unveils Real-Time AI Game Engine, Raises $21M to Make AI-Generated Worlds More Affordable](../source/src-maginative-2024-decart-oasis.md)
- [Decart and Etched release Oasis, a real-time AI-generated Minecraft-like world model](../source/src-infoq-2024-decart-etched-oasis.md)
- [MineWorld: a Real-Time and Open-Source Interactive World Model on Minecraft](../source/src-guo-2025-mineworld.md)

---
Provenance: created in run `2026-10-24-techniques-world-models`.
