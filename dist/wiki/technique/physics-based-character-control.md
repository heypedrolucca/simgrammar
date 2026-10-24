# Learned physics-based character control

*Technique* · `physics-based-character-control` · status: **sourced**

Neural policies trained with reinforcement learning drive simulated humanoids by joint torques to imitate motion capture, and MaskedMimic-style controllers accept partial goals such as keyframes, text, or an object to sit on.

| field | value |
|---|---|
| aliases | MaskedMimic, InterMimic, learned physics controllers, RL motion imitation |
| category | Animation & motion |
| year | 2024 |
| maturity | Research |
| trl | 4 |
| runtime | Offline authoring, Client real-time |
| determinism impact | Mitigable |
| horizon | 3-5 years |
| risks | Compute cost, Controllability, Evaluation difficulty |
| builds on | [Massively parallel GPU simulation](../technique/massively-parallel-simulation.md) |
| affects count *(computed)* | 4 |

## Summary

Neural policies trained with reinforcement learning drive simulated humanoids by joint torques to imitate motion capture, and MaskedMimic-style controllers accept partial goals such as keyframes, text, or an object to sit on.

## Mechanism

A ragdoll with joint actuators is simulated in a physics engine; a policy network outputs PD targets each step and is trained with RL in massively parallel GPU simulation to track motion capture clips. MaskedMimic first trains a full-body tracker, then distills it into a conditional generative student that receives a masked goal: any subset of future joint positions, a text description, a head and hand signal from VR, a path, or a target object. The same controller therefore handles locomotion, steering, and sitting on varied furniture and transfers flat-ground motions to rough terrain. InterMimic distills per-subject teachers into one student refined by RL for whole-body human-object interaction from imperfect mocap.

## Limitations

- Every character needs a physics simulation step plus policy inference, which is costly at the hundreds-of-agents scale colony and management sims use; no crowd-scale runtime figures are published in the cited work.
- Training requires large mocap datasets and GPU-parallel RL; retargeting to non-human or stylized rigs requires retraining.
- Physical controllers can fall or jitter in edge cases, which is hard to QA across open-ended situations.

## Relations

**affects**

- [Smart objects](../mechanic/smart-objects.md) (Cuts authoring cost): When an object advertises an interaction (sit, lie, lean), a goal-conditioned controller can perform it on new furniture geometry without a bespoke animation per object, as MaskedMimic shows for chairs, stools, and sofas.
- [Direct avatar control](../mechanic/direct-avatar.md) (Deepens): The controlled character becomes a physical body that adapts footing to terrain and reacts to pushes, instead of playing canned clips that slide over geometry.
- [Rigid-body physics](../mechanic/rigid-body-physics.md) (Deepens): Characters join the rigid-body simulation as actuated bodies, so carried, pushed, and collided objects affect them and vice versa (InterMimic human-object interaction).
- [Injury body model](../mechanic/injury-body-model.md) (Enables new form): With a simulated body, a wound could change gait by limiting joint torque instead of swapping in an authored limp; the cited work does not demonstrate injury-conditioned motion, so this remains a projection.

**builds on**

- [Massively parallel GPU simulation](../technique/massively-parallel-simulation.md)

## Backlinks (computed)

**applied in:** [Learned motion for simulated crowds](../opportunity/neural-npc-motion.md)

## Claims

- MaskedMimic (SIGGRAPH Asia 2024) formulates physics-based control as motion inpainting: one controller generates motion from keyframes, text, VR head or hand tracking, paths, or objects, and interacts with chairs, stools, tables, and sofas while transferring to irregular terrain; code is released as ProtoMotions. *(confidence: high)* [[168](../source/src-tessler-2024-maskedmimic.md)]
- InterMimic (2025) trains a single policy for physics-based human-object interaction from hours of imperfect motion capture by distilling subject-specific teacher policies and refining with RL; the authors report zero-shot generalization and compatibility with kinematic motion generators. *(confidence: medium)* [[169](../source/src-xu-2025-intermimic.md)]

## Sources

- [MaskedMimic: Unified Physics-Based Character Control Through Masked Motion Inpainting](../source/src-tessler-2024-maskedmimic.md)
- [InterMimic: Towards Universal Whole-Body Control for Physics-Based Human-Object Interactions](../source/src-xu-2025-intermimic.md)

---
Provenance: created in run `2026-10-24-techniques-world-models`.
