# Text- and image-to-3D asset generation

*Technique* · `text-to-3d-assets` · status: **sourced**

Open 3D generative models (TRELLIS, Hunyuan3D 2.x, Roblox Cube) produce textured meshes from a text prompt or image in seconds to a minute, and inZOI exposes image-to-3D object creation to players.

| field | value |
|---|---|
| aliases | TRELLIS, Hunyuan3D, Roblox Cube, image-to-3D |
| category | Neural rendering & 3D generation |
| year | 2025 |
| maturity | Shipped (niche) |
| trl | 7 |
| runtime | Offline authoring, Design assist |
| determinism impact | Mitigable |
| horizon | Now |
| risks | IP / provenance, Player trust / reception, Labor displacement, Content safety, Evaluation difficulty |
| deployed in | [inZOI](../game/inzoi.md) |
| affects count *(computed)* | 3 |

## Summary

Open 3D generative models (TRELLIS, Hunyuan3D 2.x, Roblox Cube) produce textured meshes from a text prompt or image in seconds to a minute, and inZOI exposes image-to-3D object creation to players.

## Mechanism

Generation is split into shape and appearance. A flow-matching or diffusion transformer generates a 3D latent conditioned on an image or text: TRELLIS uses a Structured LATent (sparse voxels carrying features from a vision foundation model), Hunyuan3D-DiT a shape latent, and Roblox Cube discrete shape tokens predicted autoregressively. Decoders turn the latent into meshes, 3D Gaussians, or radiance fields. Texture is painted by a multi-view diffusion model (Hunyuan3D-Paint) or decoded directly, with 2025 versions emitting PBR maps (base color, roughness, metallic). Output is a GLB or OBJ file that drops into an engine like any other asset.

## Limitations

- Hardware: 16 GB (TRELLIS) to about 29 GB (Hunyuan3D 2.1 shape plus texture) of GPU memory, so player-side generation usually runs in the cloud or on high-end PCs.
- Output topology and UVs are not authored for animation or LOD; production use still needs cleanup and review, which inZOI states it applies.
- Generated assets are single objects without gameplay semantics; the game must assign function, footprint, and value.
- Training data provenance and licenses vary by model, and player reception of generative AI can be negative (inZOI reviews in 2025).

## Sources

- src-xiang-2024-trellis
- src-microsoft-2025-trellis-2-repo
- src-tencent-2025-hunyuan3d-2
- src-tencent-2025-hunyuan3d-2-1-repo
- src-roblox-2025-cube
- src-roblox-2026-cube-repo
- src-steam-2025-inzoi
- src-wikipedia-inzoi

## Relations

**affects**

- [Decoration and beauty](../mechanic/decoration-beauty.md) (Cuts authoring cost): Decor and furniture catalogs that beauty and environment scores consume can be produced from prompts or reference images in seconds per asset, so catalog size stops being bounded by modeling time.
- [Generative content on demand](../mechanic/generative-content.md) (Deepens): Runtime generation extends from text and textures to placeable 3D props: inZOI players convert their own images into in-game objects.
- [Modular assembly](../mechanic/modular-assembly.md) (Enables new form): Part-controllable generation (Roblox CubePart) produces assets split into parts intended for physics and scripts, which could supply new components for build-from-parts mechanics on request; not yet shown in a shipped assembly game.

**deployed in**

- [inZOI](../game/inzoi.md)

## Backlinks (computed)

**applied in:** [Generative decoration catalogs](../opportunity/generative-decoration-catalogs.md), [Illustrated chronicles](../opportunity/illustrated-chronicles.md)

## Claims

- TRELLIS (Microsoft, CVPR 2025) trains models up to 2B parameters on about 500K 3D objects and decodes one latent to radiance fields, 3D Gaussians, or meshes; it is MIT-licensed and needs a GPU with at least 16 GB. *(confidence: high)* [[312](../source/src-xiang-2024-trellis.md)]
- TRELLIS.2 (4B parameters) outputs PBR-textured GLB assets in about 3 seconds at 512^3, 17 seconds at 1024^3, and 60 seconds at 1536^3 on an H100. *(confidence: high)* [[313](../source/src-microsoft-2025-trellis-2-repo.md)]
- Hunyuan3D 2.0 (January 2025) released open shape and texture models; Hunyuan3D 2.1 (June 2025) added PBR texturing and training code and needs about 29 GB of VRAM for shape plus texture. *(confidence: high)* [[314](../source/src-tencent-2025-hunyuan3d-2.md), [315](../source/src-tencent-2025-hunyuan3d-2-1-repo.md)]
- Roblox released Cube 3D text-to-shape (v0.1 March 2025, v0.5 July 2025) and CubePart part-controllable generation (May 2026) aimed at assets usable with animation, physics, and scripts. *(confidence: high)* [[316](../source/src-roblox-2025-cube.md), [317](../source/src-roblox-2026-cube-repo.md)]
- inZOI's store page states that players can turn 2D images into in-game 3D objects, with AI tools described as auxiliary and generated content reviewed by the team. *(confidence: high)* [[138](../source/src-steam-2025-inzoi.md)]
- inZOI received negative user reviews in May 2025 after Krafton announced its use of generative AI. *(confidence: medium)* [[318](../source/src-wikipedia-inzoi.md)]

## Sources

- [Structured 3D Latents for Scalable and Versatile 3D Generation](../source/src-xiang-2024-trellis.md)
- [TRELLIS.2 repository](../source/src-microsoft-2025-trellis-2-repo.md)
- [Hunyuan3D 2.0: Scaling Diffusion Models for High Resolution Textured 3D Assets Generation](../source/src-tencent-2025-hunyuan3d-2.md)
- [Hunyuan3D-2.1 repository](../source/src-tencent-2025-hunyuan3d-2-1-repo.md)
- [Cube: A Roblox View of 3D Intelligence](../source/src-roblox-2025-cube.md)
- [Roblox Cube repository](../source/src-roblox-2026-cube-repo.md)
- [inZOI on Steam](../source/src-steam-2025-inzoi.md)
- [inZOI](../source/src-wikipedia-inzoi.md)

---
Provenance: created in run `2026-10-24-techniques-world-models`.
