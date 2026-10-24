# Prompt-to-persistent 3D world generation

*Technique* · `generated-3d-worlds` · status: **sourced**

Models such as World Labs Marble and HunyuanWorld turn text, images, video, or coarse 3D blockouts into persistent explorable scenes exported as Gaussian splats and meshes with collision proxies.

| field | value |
|---|---|
| aliases | Marble, World Labs, HunyuanWorld, RTFM, Atlas |
| category | Neural rendering & 3D generation |
| year | 2025 |
| maturity | Prototype |
| trl | 6 |
| runtime | Offline authoring, Design assist |
| determinism impact | Preserves |
| horizon | 1-2 years |
| risks | Consistency / hallucination, Controllability, IP / provenance, Labor displacement, Player trust / reception |
| builds on | [3D Gaussian Splatting](../technique/gaussian-splatting.md) |
| affects count *(computed)* | 4 |

## Summary

Models such as World Labs Marble and HunyuanWorld turn text, images, video, or coarse 3D blockouts into persistent explorable scenes exported as Gaussian splats and meshes with collision proxies.

## Mechanism

An image or video diffusion model generates views of a scene (a 360-degree panorama in HunyuanWorld, multi-view images in Marble) from the prompt; the views are lifted to an explicit 3D representation (3D Gaussian splats, or a semantically layered mesh) that can be walked through and re-rendered without regeneration. Marble also emits triangle meshes and coarse collider meshes for physics, can expand or merge worlds, and in Chisel mode takes a blockout of boxes and planes as structure and a text prompt as style. A parallel line renders frames directly instead of building geometry: RTFM keeps generated frames with camera poses as spatial memory and retrieves nearby frames as context. Atlas (2026) is a multimodal model that outputs video, point clouds, and splats.

## Limitations

- Scenes are static: no dynamic objects, agents, or rules are generated, and RTFM lists dynamics and interaction as future work.
- Single-image or text prompts force the model to invent unseen regions; Marble notes artifacts and less crisp far regions that expansion may fix.
- Splat output bakes lighting into colors, so day-night cycles and relighting need conversion to meshes or other methods.
- Collider meshes are coarse and need manual work for gameplay-critical collision.
- Corporate change (World Labs joining AMD in 2026) leaves the hosted product's future terms uncertain.

## Relations

**affects**

- [Procedural terrain](../mechanic/procedural-terrain.md) (Enables new form): Maps come from a prompt, photo, or video rather than a seed and noise pipeline, and unlike frame-based world models the result is baked geometry that persists, can be saved, and can be expanded region by region.
- [Scenario objectives](../mechanic/scenario-objectives.md) (Cuts authoring cost): Bespoke scenario maps can be produced from a reference image or description and exported with collider meshes, reducing hand modeling per scenario; objectives and rules still need authoring.
- [Procedural build assist](../mechanic/procedural-build-assist.md) (Enables new form): Chisel turns a coarse blockout into a detailed styled scene, the same rough-input to detailed-output contract as Townscaper-style build assist but with a learned generator; today it is an editor mode, not a runtime player tool.
- [Rigid-body physics](../mechanic/rigid-body-physics.md) (Cuts authoring cost): Exported collider meshes give generated scenes collision geometry automatically; Marble describes them as coarse, so precise physics still needs cleanup.

**builds on**

- [3D Gaussian Splatting](../technique/gaussian-splatting.md)

## Claims

- Marble became generally available on 2025-11-12, taking text, images, video, or coarse 3D layouts and exporting Gaussian splats, triangle meshes including collider meshes for coarse physics, and rendered video; Chisel separates blocked-out structure from prompted style. *(confidence: high)* [[101](../source/src-worldlabs-2025-marble.md)]
- HunyuanWorld 1.0 (Tencent, July 2025) generates explorable worlds from text or images via panoramic proxies converted to a semantically layered 3D mesh exportable to standard graphics pipelines, listing game development as an application. *(confidence: high)* [[265](../source/src-tencent-2025-hunyuanworld-1.md)]
- RTFM (October 2025) renders generated or real scenes from a single image at interactive frame rates on one H100, using posed frames as spatial memory; it models static scenes only. *(confidence: high)* [[266](../source/src-worldlabs-2025-rtfm.md)]
- World Labs launched a public World API in January 2026, released Atlas to early-access partners in September 2026, and announced it is joining AMD on 2026-09-28. *(confidence: medium)* [[102](../source/src-worldlabs-2026-blog.md), [267](../source/src-worldlabs-2026-atlas.md)]

## Sources

- [Marble: A Multimodal World Model](../source/src-worldlabs-2025-marble.md)
- [HunyuanWorld 1.0: Generating Immersive, Explorable, and Interactive 3D Worlds from Words or Pixels](../source/src-tencent-2025-hunyuanworld-1.md)
- [RTFM: A Real-Time Frame Model](../source/src-worldlabs-2025-rtfm.md)
- [World Labs blog and news index](../source/src-worldlabs-2026-blog.md)
- [Atlas: A World Model for Spatial Intelligence](../source/src-worldlabs-2026-atlas.md)

---
Provenance: created in run `2026-10-24-techniques-world-models`.
