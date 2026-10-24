# Real-time generative restyling of game video

*Technique* · `real-time-video-restyling` · status: **sourced**

A live video-to-video diffusion model repaints each frame of a running game from a text prompt in under 40 ms, leaving the game's own simulation and state untouched.

| field | value |
|---|---|
| aliases | MirageLSD, Oasis 2.0, live-stream diffusion, video-to-video game skin |
| category | Neural rendering & 3D generation |
| year | 2025 |
| maturity | Prototype |
| trl | 6 |
| runtime | Server real-time |
| determinism impact | Mitigable |
| horizon | 1-2 years |
| risks | Consistency / hallucination, Legibility, Latency, Compute cost, Controllability |
| builds on | [Diffusion and autoregressive neural game engines](../technique/diffusion-game-engines.md) |
| deployed in | [Minecraft](../game/minecraft.md) |
| affects count *(computed)* | 2 |

## Summary

A live video-to-video diffusion model repaints each frame of a running game from a text prompt in under 40 ms, leaving the game's own simulation and state untouched.

## Mechanism

The host game renders normally and streams its frames to a video-to-video diffusion model. Each output frame is conditioned on the current input frame, a window of recently generated frames, and a text prompt; Diffusion Forcing and history augmentation keep the stream from drifting, and distillation, pruning, and custom GPU kernels bring response under 40 ms at 24 fps. Because the model only replaces pixels, collision, inventory, and world state stay in the host engine. Decart's Oasis 2.0 packages this as a Minecraft mod with chat commands and command-block hooks that switch the prompt.

## Limitations

- Short frame window and no long-term memory, so restyled objects can change appearance between views.
- Rendered detail can contradict game state (a block that looks like a door but is solid), hurting legibility.
- Cloud-served stream adds network latency and per-player GPU cost; no price per hour is published.

## Relations

**affects**

- [Procedural build assist](../mechanic/procedural-build-assist.md) (Enables new form): Blocky player builds are rendered as detailed structures in a prompted style (for example Roman), a visual-only form of build assist: collision and block state stay coarse while the view is detailed.
- [Generative content on demand](../mechanic/generative-content.md) (Enables new form): Players or in-world logic change the whole world's look at runtime by text, without new textures or models; the game's systems cannot read the new look, so it carries no gameplay meaning.

**builds on**

- [Diffusion and autoregressive neural game engines](../technique/diffusion-game-engines.md)

**deployed in**

- [Minecraft](../game/minecraft.md)

## Claims

- MirageLSD responds in under 40 ms per frame at 24 fps, conditioning each frame on recent output, the current input frame, and a prompt; Decart lists limited memory, weak control of specific objects or regions, and structure distortion under extreme style shifts. *(confidence: high)* [[274](../source/src-decart-2025-miragelsd.md)]
- Oasis 2.0 is a Minecraft 1.21.8 mod that restyles the player's world in real time from prompts set by chat command or by in-world command blocks. *(confidence: high)* [[275](../source/src-decart-2025-oasis-2.md)]

## Sources

- [MirageLSD: live-stream diffusion video model](../source/src-decart-2025-miragelsd.md)
- [How to Play Oasis 2.0](../source/src-decart-2025-oasis-2.md)

---
Provenance: created in run `2026-10-24-techniques-world-models`.
