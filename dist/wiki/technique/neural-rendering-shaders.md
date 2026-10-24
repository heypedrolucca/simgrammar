# Neural rendering in the graphics pipeline

*Technique* · `neural-rendering-shaders` · status: **sourced**

Small neural networks inside the renderer upscale frames, generate extra frames, denoise ray tracing, decode compressed textures and layered materials, and since DLSS 5 re-light the final frame, all without touching simulation state.

| field | value |
|---|---|
| aliases | DLSS, DLSS 4, DLSS 5, neural shaders, RTX Neural Materials, neural texture compression, neural radiance cache |
| category | Neural rendering & 3D generation |
| year | 2025 |
| maturity | Shipped (mainstream) |
| trl | 9 |
| runtime | Client real-time |
| determinism impact | Preserves |
| horizon | Now |
| risks | Player trust / reception, Latency, Compute cost, Controllability |
| deployed in | [Microsoft Flight Simulator (2020)](../game/microsoft-flight-simulator-2020.md), [Cities: Skylines II](../game/cities-skylines-2.md) |
| affects count *(computed)* | 3 |

## Summary

Small neural networks inside the renderer upscale frames, generate extra frames, denoise ray tracing, decode compressed textures and layered materials, and since DLSS 5 re-light the final frame, all without touching simulation state.

## Mechanism

DLSS Super Resolution reconstructs a high-resolution frame from a lower-resolution render plus motion vectors with a transformer network (from DLSS 4); Multi Frame Generation predicts up to three (DLSS 4) or five (DLSS 4.5) frames between rendered frames; Ray Reconstruction replaces hand-tuned denoisers. Neural shaders embed small MLPs inside shader code and run them on tensor units: neural texture compression decodes textures from learned latents, neural materials evaluate layered BRDFs, and the neural radiance cache learns multi-bounce indirect light online. DirectX cooperative vectors expose this to cross-vendor shaders. DLSS 5 adds a final network pass that adds lighting and material detail from color and motion vectors, with developer intensity controls and masks.

## Limitations

- Changes presentation, not simulation: CPU-bound simulation games (agent counts, pathfinding, economy ticks) gain nothing from GPU-side neural rendering.
- Frame generation adds input latency and artifacts; DLSS 5's final pass reportedly costs 50 to 60 percent of frame rate and can alter art direction.
- Hardware-gated: Multi Frame Generation and DLSS 5 require RTX 50-series GPUs at launch, and neural shader features depend on vendor SDKs and cooperative vector support.

## Sources

- src-nvidia-2025-dlss-4
- src-nvidia-2025-rtx-neural-rendering
- src-nvidia-2026-dlss-4-5
- src-nvidia-2026-dlss-5
- src-wikipedia-deep-learning-super-sampling
- src-pcgamingwiki-2026-msfs-2020
- src-pcgamingwiki-2026-cities-skylines-2

## Relations

**affects**

- [Embodied skill control](../mechanic/embodied-skill-control.md) (Accelerates): Upscaling and frame generation raise displayed frame rates in GPU-heavy flight and driving sims for the same render cost; generated frames do not sample new input, so frame generation adds latency that hurts precise hand-flying or driving.
- [Day-night cycle](../mechanic/day-night-cycle.md) (Deepens): Neural denoising and the neural radiance cache make dynamic multi-bounce lighting affordable, so player-built interiors and towns can be lit correctly across a full diurnal cycle where baked lighting cannot follow player construction.
- [Decoration and beauty](../mechanic/decoration-beauty.md) (Deepens): Up to 7x VRAM savings from neural texture compression and cheaper layered materials let more distinct high-detail decor assets be resident at once, raising the variety a beauty-driven builder can show on screen.

**deployed in**

- [Microsoft Flight Simulator (2020)](../game/microsoft-flight-simulator-2020.md)
- [Cities: Skylines II](../game/cities-skylines-2.md)

## Backlinks (computed)

**applied in:** [Symbolic simulation, neural rendering](../opportunity/symbolic-sim-neural-render.md)

## Claims

- DLSS 4 (January 2025) introduced Multi Frame Generation of up to three extra frames per rendered frame on RTX 50 GPUs and transformer models for super resolution and ray reconstruction, with 75 games and apps at launch and up to 8x frame rate over brute-force rendering. *(confidence: high)* [[236](../source/src-nvidia-2025-dlss-4.md)]
- RTX neural shaders (January 2025) included neural texture compression using up to 7x less VRAM than block-compressed textures at equal quality, neural materials up to 5x faster, and a neural radiance cache for multi-bounce indirect lighting, with DirectX cooperative vector support announced. *(confidence: high)* [[237](../source/src-nvidia-2025-rtx-neural-rendering.md)]
- By January 2026 over 250 titles supported Multi Frame Generation and over 400 games and apps supported DLSS Super Resolution; DLSS 4.5 added a 6X mode generating up to five frames per rendered frame. *(confidence: high)* [[238](../source/src-nvidia-2026-dlss-4-5.md)]
- DLSS 5 launched on 2026-09-03 in NBA 2K27 as a deterministic one-frame-in, one-frame-out neural pass that adds lighting and material detail, with structure and tone intensity controls and semantic masks for developers. *(confidence: high)* [[239](../source/src-nvidia-2026-dlss-5.md)]
- DLSS 5's reveal drew largely negative reaction from players and developers over altered faces and art direction, and a reported 50 to 60 percent frame-rate cost; frame generation in general adds input latency and can introduce artifacts. *(confidence: medium)* [[240](../source/src-wikipedia-deep-learning-super-sampling.md)]
- Simulation titles use DLSS: Microsoft Flight Simulator (2020) supports DLSS upscaling and DLSS Frame Generation, and Cities: Skylines II supports DLSS upscaling. *(confidence: medium)* [[241](../source/src-pcgamingwiki-2026-msfs-2020.md), [242](../source/src-pcgamingwiki-2026-cities-skylines-2.md)]

## Sources

- [NVIDIA DLSS 4 Introduces Multi Frame Generation and Transformer-Based AI Models](../source/src-nvidia-2025-dlss-4.md)
- [NVIDIA RTX Neural Rendering Introduces Next Era of AI-Powered Graphics Innovation](../source/src-nvidia-2025-rtx-neural-rendering.md)
- [NVIDIA DLSS 4.5 Delivers Major Upgrade With 2nd Gen Transformer Model For Super Resolution and 6X Dynamic Multi Frame Generation](../source/src-nvidia-2026-dlss-4-5.md)
- [NVIDIA DLSS 5 Available September 3rd: 3D-Guided Neural Rendering Debuts In NBA 2K27](../source/src-nvidia-2026-dlss-5.md)
- [Deep Learning Super Sampling](../source/src-wikipedia-deep-learning-super-sampling.md)
- [Microsoft Flight Simulator (2020)](../source/src-pcgamingwiki-2026-msfs-2020.md)
- [Cities: Skylines II](../source/src-pcgamingwiki-2026-cities-skylines-2.md)

---
Provenance: created in run `2026-10-24-techniques-world-models`.
