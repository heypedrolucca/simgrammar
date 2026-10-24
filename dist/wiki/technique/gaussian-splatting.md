# 3D Gaussian Splatting

*Technique* · `gaussian-splatting` · status: **sourced**

Scenes are represented as millions of anisotropic 3D Gaussians optimized from photos and rasterized in real time, giving photoreal captured or generated environments at 1080p and 30+ fps.

| field | value |
|---|---|
| aliases | 3DGS, Gaussian splats, radiance field splatting |
| category | Neural rendering & 3D generation |
| year | 2023 |
| maturity | Prototype |
| trl | 6 |
| runtime | Offline authoring, Client real-time |
| determinism impact | Preserves |
| horizon | 1-2 years |
| risks | Compute cost, Controllability, IP / provenance |
| affects count *(computed)* | 2 |

## Summary

Scenes are represented as millions of anisotropic 3D Gaussians optimized from photos and rasterized in real time, giving photoreal captured or generated environments at 1080p and 30+ fps.

## Mechanism

Starting from sparse structure-from-motion points, each Gaussian stores position, anisotropic covariance, opacity, and view-dependent color as spherical harmonics. A differentiable tile-based rasterizer projects, depth-sorts, and alpha-blends the Gaussians; gradients from photo reconstruction error update parameters while adaptive density control splits, clones, and prunes Gaussians. Rendering needs no neural network at runtime, so it runs at real-time rates. Extensions attach physics directly to the Gaussians (PhysGaussian runs a Material Point Method on the kernels), stream level-of-detail on the web, and standardize the format in glTF.

## Limitations

- Colors store captured radiance, so lighting is baked in; dynamic time of day, player-placed lights, and relighting are not supported by the base method.
- Memory heavy: millions of Gaussians per scene and training peaks above 20 GB.
- No collision geometry or semantics: gameplay needs separate meshes or proxies for physics and pathfinding.
- Editing and stylizing splats is harder than editing meshes; tooling and a ratified interchange standard were still arriving in 2026.

## Sources

- src-kerbl-2023-3d-gaussian-splatting
- src-wikipedia-gaussian-splatting
- src-xie-2023-physgaussian
- src-khronos-2026-gltf-gaussian-splatting
- src-worldlabs-2025-marble
- src-worldlabs-2026-blog

## Relations

**affects**

- [Soft-body deformation](../mechanic/soft-body-deformation.md) (Enables new form): PhysGaussian deforms captured objects with MPM directly on the rendered Gaussians, so a scanned real object can bend, dent, or flow without building a node-beam or finite-element mesh first.
- [Decoration and beauty](../mechanic/decoration-beauty.md) (Cuts authoring cost): Photoreal props and scenery can be captured from photos in under an hour of training instead of modeled and textured by hand, enlarging decor catalogs that beauty scores consume; lighting is baked into the capture.

## Backlinks (computed)

**applied in:** [Generative decoration catalogs](../opportunity/generative-decoration-catalogs.md), [Symbolic simulation, neural rendering](../opportunity/symbolic-sim-neural-render.md)

**built upon by:** [Prompt-to-persistent 3D world generation](../technique/generated-3d-worlds.md)

## Claims

- Kerbl et al. (2023) reached real-time (30 fps or more) novel-view synthesis at 1080p with state-of-the-art visual quality and competitive training times. *(confidence: high)* [[97](../source/src-kerbl-2023-3d-gaussian-splatting.md)]
- A full 3DGS scene trains in about 35 to 45 minutes versus about 48 hours for Mip-NeRF 360, but uses more memory than NeRF methods, with peak training memory over 20 GB, and shows popping and elongated-splat artifacts. *(confidence: medium)* [[98](../source/src-wikipedia-gaussian-splatting.md)]
- PhysGaussian simulates elastic, metal, non-Newtonian, and granular behavior directly on Gaussian kernels with an MPM solver, avoiding meshing so the simulated and rendered representation are the same. *(confidence: medium)* [[99](../source/src-xie-2023-physgaussian.md)]
- Khronos released a KHR_gaussian_splatting glTF 2.0 extension as a release candidate on 2026-02-03 with contributors including Autodesk, Cesium, Esri, Niantic Spatial, and NVIDIA, expecting ratification in Q2 2026. *(confidence: high)* [[100](../source/src-khronos-2026-gltf-gaussian-splatting.md)]
- Generated-world products export splats as their highest-fidelity format and render them in the browser (World Labs Marble with the Spark renderer). *(confidence: medium)* [[101](../source/src-worldlabs-2025-marble.md), [102](../source/src-worldlabs-2026-blog.md)]

## Sources

- [3D Gaussian Splatting for Real-Time Radiance Field Rendering](../source/src-kerbl-2023-3d-gaussian-splatting.md)
- [Gaussian splatting](../source/src-wikipedia-gaussian-splatting.md)
- [PhysGaussian: Physics-Integrated 3D Gaussians for Generative Dynamics](../source/src-xie-2023-physgaussian.md)
- [Khronos releases KHR_gaussian_splatting glTF extension release candidate](../source/src-khronos-2026-gltf-gaussian-splatting.md)
- [Marble: A Multimodal World Model](../source/src-worldlabs-2025-marble.md)
- [World Labs blog and news index](../source/src-worldlabs-2026-blog.md)

---
Provenance: created in run `2026-10-24-techniques-world-models`.
