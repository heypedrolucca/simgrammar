# Genie foundation world models

*Technique* · `genie-world-models` · status: **sourced**

Google DeepMind's Genie models generate playable worlds from a text or image prompt and render them in real time from player input, with Genie 3 reaching 720p at 24 fps and about a minute of visual memory.

| field | value |
|---|---|
| aliases | Genie, Genie 2, Genie 3, Project Genie |
| category | Generative world model |
| year | 2025 |
| maturity | Prototype |
| trl | 6 |
| runtime | Server real-time |
| determinism impact | Breaks |
| horizon | 3-5 years |
| risks | Determinism, Consistency / hallucination, Compute cost, Controllability, IP / provenance, Content safety |
| affects count *(computed)* | 7 |

## Summary

Google DeepMind's Genie models generate playable worlds from a text or image prompt and render them in real time from player input, with Genie 3 reaching 720p at 24 fps and about a minute of visual memory.

## Mechanism

Genie (2024) learned from 30k hours of unlabeled 2D platformer video: a video tokenizer, a latent action model that infers 8 discrete actions between frames without labels, and a 10.1B-parameter dynamics model that predicts the next frame tokens given an action. Genie 2 (December 2024) is an autoregressive latent diffusion model with a transformer dynamics model that turns a single image into a 3D world controlled by keyboard and mouse. Genie 3 (August 2025) generates frames auto-regressively in real time from a text prompt, keeps visual memory of earlier frames for about a minute so revisited places look the same, and accepts text 'promptable world events' during play that add objects, characters, or weather changes. No explicit 3D scene or game state is stored; consistency comes from the frame history.

## Limitations

- Session length: Genie 2 coherence is usually 10 to 20 seconds; Genie 3 manages a few minutes; Project Genie caps exploration at 60 seconds because of compute.
- No inspectable state: there are no variables for inventory, health, or object identity, so mechanics that need stocks or rules must live in a separate system.
- Limited action space and no reliable multi-agent interaction (DeepMind's stated Genie 3 limitations).
- Access is a hosted research prototype for paying subscribers; no public API, price per hour, or on-device version is published.
- Guardrails refuse copyrighted settings and nudity, which constrains user-generated worlds.

## Sources

- src-bruce-2024-genie
- src-deepmind-2024-genie-2
- src-deepmind-2025-genie-3
- src-techcrunch-2026-project-genie
- src-wikipedia-project-genie
- src-wikipedia-genie-ai-model

## Relations

**affects**

- [Weather](../mechanic/weather.md) (Enables new form): Genie 3's promptable world events change weather by text during a session with no weather simulation or authored weather assets; the change is visual only and has no stored state for crops, agents, or travel to read.
- [Storyteller director](../mechanic/storyteller-director.md) (Cuts authoring cost): A director could inject an event (a new character, object, or condition) as a text prompt that Genie 3 renders into the running world, removing per-event art and animation; event selection and pacing still need a separate system with real state.
- [Procedural terrain](../mechanic/procedural-terrain.md) (Enables new form): Worlds come from a text or image prompt instead of a seed and noise pipeline, in any visual style; persistence is minutes long (about one minute of visual memory in Genie 3, 60-second sessions in Project Genie).
- [Direct avatar control](../mechanic/direct-avatar.md) (Replaces substrate): First- or third-person character movement is rendered by the model from WASD, camera, and jump input; the action space is small and collisions are not guaranteed (characters passing through walls).
- [Rigid-body physics](../mechanic/rigid-body-physics.md) (Replaces substrate): Object responses such as doors opening, balloons bursting, water, and smoke are produced by learned video dynamics (Genie 2) rather than a physics engine, with no conservation or collision guarantees.
- [Generative content on demand](../mechanic/generative-content.md) (Enables new form): Whole explorable scenes, characters, and events are generated at runtime from player text, sketches, or photos, which extends generative content from text and items to playable space.
- [God powers](../mechanic/god-powers.md) (Enables new form): Promptable world events work as a free-form god power: typed text adds characters, objects, or weather to the running world; Genie 3 attaches no cost or rule to them and their effects exist only in rendered frames.

## Backlinks (computed)

**applied in:** [Generated dream and replay views](../opportunity/dream-replay-layer.md), [Symbolic simulation, neural rendering](../opportunity/symbolic-sim-neural-render.md)

**built upon by:** [Open-ended co-generation of environments and agents](../technique/open-ended-environment-generation.md)

## Claims

- Genie has 11B parameters trained on 30k hours of 2D platformer clips with 8 latent actions; it generates about 1 frame per second and has 16 frames of memory, which the paper lists as limitations. *(confidence: high)* [[139](../source/src-bruce-2024-genie.md)]
- Genie 2 turns one image into a playable 3D world with water, smoke, gravity, lighting, door opening, and NPCs; worlds stay coherent for up to a minute, but most examples last 10 to 20 seconds. *(confidence: high)* [[140](../source/src-deepmind-2024-genie-2.md)]
- Genie 3 renders 720p at 24 fps in real time, stays consistent for a few minutes with visual memory reaching back about one minute, and supports text prompts that change weather or add objects and characters mid-session; DeepMind lists limited action space and multi-agent interaction as open problems. *(confidence: high)* [[141](../source/src-deepmind-2025-genie-3.md)]
- Project Genie opened Genie 3 to US Google AI Ultra subscribers on 2026-01-29 with a 60-second limit per world set by compute cost; a reviewer saw characters walk through walls and sometimes unresponsive controls, and copyrighted settings were refused. *(confidence: high)* [[142](../source/src-techcrunch-2026-project-genie.md), [143](../source/src-wikipedia-project-genie.md)]
- Shares of video game companies, including Unity, fell after the Project Genie launch. *(confidence: medium)* [[143](../source/src-wikipedia-project-genie.md)]
- Waymo built a world model on Genie 3 (February 2026) to simulate driving edge cases, controllable by driving action, scene layout, and language. *(confidence: medium)* [[144](../source/src-wikipedia-genie-ai-model.md)]

## Sources

- [Genie: Generative Interactive Environments](../source/src-bruce-2024-genie.md)
- [Genie 2: A large-scale foundation world model](../source/src-deepmind-2024-genie-2.md)
- [Genie 3: A new frontier for world models](../source/src-deepmind-2025-genie-3.md)
- [I built marshmallow castles in Google's new AI world generator Project Genie](../source/src-techcrunch-2026-project-genie.md)
- [Project Genie (website)](../source/src-wikipedia-project-genie.md)
- [Genie (AI model)](../source/src-wikipedia-genie-ai-model.md)

---
Provenance: created in run `2026-10-24-techniques-world-models`; reviewed in `2026-10-24-review-fixes`.
