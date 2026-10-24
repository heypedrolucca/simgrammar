# Massively parallel GPU simulation

*Technique* · `massively-parallel-simulation` · status: **sourced**

Simulators that keep thousands of world instances as tensors on a GPU or TPU and step them all in one kernel, raising throughput to millions of steps per second for agent training and Monte Carlo sweeps.

| field | value |
|---|---|
| aliases | batch simulation, many-world simulation, GPU-accelerated simulators, Isaac Gym, Brax, MJX, Madrona |
| category | Differentiable & accelerated simulation |
| year | 2021 |
| maturity | Research |
| trl | 4 |
| runtime | Offline authoring, Design assist |
| determinism impact | Preserves |
| horizon | 1-2 years |
| risks | Controllability, Evaluation difficulty, Determinism |
| deployed in |  |
| affects count *(computed)* | 8 |

## Summary

Simulators that keep thousands of world instances as tensors on a GPU or TPU and step them all in one kernel, raising throughput to millions of steps per second for agent training and Monte Carlo sweeps.

## Mechanism

World state for N independent instances is stored as structure-of-arrays tensors in accelerator memory. Each tick launches one set of kernels that integrates physics, evaluates game logic, and computes observations and rewards for every instance at once, so policy inference and training read the state without CPU-GPU copies. Implementations compile the step function: JAX/XLA (Brax, MJX, Craftax), CUDA kernels written in Python (NVIDIA Warp, MuJoCo Warp), or a GPU entity-component-system with a task graph (Madrona, where game logic is C++ compiled to CUDA). Throughput comes from parallelism across worlds, not from making one world faster, so the main uses are reinforcement learning (billions of steps), parameter sweeps, and evaluating many randomized variants of one design.

## Limitations

- Speedups come from running many independent worlds in parallel; a single large coupled world, such as one city, gains much less and per-world latency does not improve.
- Game logic must be rewritten in a GPU-friendly form (JAX in Craftax, C++ compiled to CUDA in GPUDrive and Madrona), which is a port rather than a recompile.
- Madrona requires all component archetypes to be declared up front and does not support adding or removing components at runtime; it is labeled research code with breaking API changes.
- Headline frame rates are for simple scenes; contact-rich and dexterous scenes remain hard and much slower (reported caveat on Genesis).
- Much of the stack is NVIDIA-specific: MuJoCo Warp needs an NVIDIA GPU for speed, and porting PhysX's 500+ CUDA kernels to other vendors is described as a lot of work.
- Policies trained in a batched simulator exploit its physics quirks, so behavior must be re-validated in the shipping engine if that engine differs.

## Sources

- src-makoviychuk-2021-isaac-gym
- src-freeman-2021-brax
- src-shacklett-2023-madrona
- src-madrona-2026-repository
- src-matthews-2024-craftax
- src-kazemkhani-2024-gpudrive
- src-zakka-2025-mujoco-playground
- src-deepmind-2026-mujoco-warp
- src-genesis-2024-genesis-world
- src-kemper-2024-genesis-430000x
- src-thacker-2025-physx-gpu-open-source
- src-larabel-2025-newton-linux-foundation

## Relations

**affects**

- [Rigid-body physics](../mechanic/rigid-body-physics.md) (Accelerates): Batched GPU rigid-body solvers step thousands of worlds or bodies per kernel launch, so physics-heavy evaluation that was CPU-bound becomes cheap enough for large sweeps.
- [Creature learning](../mechanic/creature-learning.md) (Enables new form): Locomotion policies train in seconds to minutes on one GPU (Brax, MuJoCo Playground), so a creature could learn to move or act through RL during a play session instead of from canned animation.
- [Modular assembly](../mechanic/modular-assembly.md) (Enables new form): A player-built creature or machine can be dropped into thousands of parallel worlds and have a controller trained for its specific body, so assembled designs move competently without the player programming them.
- [Natural selection](../mechanic/natural-selection.md) (Deepens): Fitness can be measured by simulating every individual of a large population in its own physics world each generation, so selection acts on actual behavior rather than on summed stat values.
- [Design performance rating](../mechanic/design-performance-rating.md) (Deepens): A player design can be scored over hundreds of randomized loads, terrains or seeds in parallel, giving a robustness distribution instead of one deterministic test run.
- [Attribute-driven match engine](../mechanic/attribute-match-engine.md) (Tunes / balances): Millions of simulated matches per hour let designers check how attribute weights and tactic modifiers shift outcome distributions before shipping a match-engine change.
- [Traffic congestion](../mechanic/traffic-congestion.md) (Accelerates): GPUDrive shows multi-agent vehicle simulation above one million steps per second, which points to agent-level traffic at counts where city builders now fall back to aggregate flow.
- [Utility action selection](../mechanic/utility-action-selection.md) (Tunes / balances): Cheap batched rollouts make it practical to search utility-curve weights, or train a policy to replace them, against metrics such as survival or need satisfaction over many simulated colonies.

## Backlinks (computed)

**applied in:** [Branch preview of policy futures](../opportunity/branch-preview-forecasts.md), [Calibrated serious simulations](../opportunity/calibrated-serious-sims.md), [Event-sourced simulation runtime](../opportunity/event-sourced-sim-runtime.md), [Learned material surrogates at world scale](../opportunity/learned-material-surrogates.md), [Factories with a living workforce](../opportunity/living-workforce-factories.md), [Mean-field crowds and traffic](../opportunity/mean-field-crowds.md), [Learned motion for simulated crowds](../opportunity/neural-npc-motion.md), [Open-ended evolution sandbox](../opportunity/open-ended-evolution-sandbox.md), [Parallel autobalancing of economies](../opportunity/parallel-autobalance.md)

**built upon by:** [Deep reinforcement learning policies for NPC opponents and navigation](../technique/deep-rl-npc-policies.md), [Physical-world foundation models](../technique/physical-world-foundation-models.md), [Learned physics-based character control](../technique/physics-based-character-control.md)

## Claims

- Isaac Gym ran physics and policy training on a single GPU and reported 2-3 orders of magnitude faster RL training than pipelines using a CPU simulator. *(confidence: high)* [[208](../source/src-makoviychuk-2021-isaac-gym.md)]
- Brax reported millions of simulation steps per second on one accelerator and hundreds of millions across accelerators, training Ant locomotion in about ten seconds versus close to half an hour for standard PPO. *(confidence: high)* [[122](../source/src-freeman-2021-brax.md)]
- Madrona's GPU batch ECS ran OpenAI Hide and Seek at over 1.9 million steps per second, Overcooked-AI at 40 million and Hanabi at 20 million on an RTX 4090, 5-33x faster than strong 32-thread CPU baselines. *(confidence: high)* [[209](../source/src-shacklett-2023-madrona.md)]
- Craftax reimplemented the survival-crafting game Crafter in JAX, ran up to 250x faster than the Python original, and trained PPO for 1 billion interactions in under an hour on one GPU. *(confidence: high)* [[210](../source/src-matthews-2024-craftax.md)]
- GPUDrive, built on Madrona, simulated multi-agent driving from real road scenarios at over one million steps per second. *(confidence: high)* [[211](../source/src-kazemkhani-2024-gpudrive.md)]
- MuJoCo Playground (2025) trained locomotion and manipulation policies in minutes on a single GPU and transferred them zero-shot to real robots. *(confidence: high)* [[212](../source/src-zakka-2025-mujoco-playground.md)]
- Genesis (December 2024) was publicized as reaching 43 million FPS (430,000x real time) on simple scenes; press noted skepticism and that contact-rich dexterous scenes remain hard. *(confidence: low)* [[213](../source/src-kemper-2024-genesis-430000x.md), [214](../source/src-genesis-2024-genesis-world.md)]
- GPU physics became more open in 2025: NVIDIA released PhysX 5.6 GPU source under BSD-3 in April, and the Warp-based Newton engine (NVIDIA, Google DeepMind, Disney Research) moved to the Linux Foundation in September. *(confidence: high)* [[215](../source/src-thacker-2025-physx-gpu-open-source.md), [216](../source/src-larabel-2025-newton-linux-foundation.md)]

## Sources

- [Isaac Gym: High Performance GPU-Based Physics Simulation For Robot Learning](../source/src-makoviychuk-2021-isaac-gym.md)
- [Brax: A Differentiable Physics Engine for Large Scale Rigid Body Simulation](../source/src-freeman-2021-brax.md)
- [An Extensible, Data-Oriented Architecture for High-Performance, Many-World Simulation](../source/src-shacklett-2023-madrona.md)
- [Madrona: a prototype engine for high-throughput batch simulation](../source/src-madrona-2026-repository.md)
- [Craftax: A Lightning-Fast Benchmark for Open-Ended Reinforcement Learning](../source/src-matthews-2024-craftax.md)
- [GPUDrive: Data-driven, multi-agent driving simulation at 1 million FPS](../source/src-kazemkhani-2024-gpudrive.md)
- [MuJoCo Playground](../source/src-zakka-2025-mujoco-playground.md)
- [MuJoCo Warp (MJWarp)](../source/src-deepmind-2026-mujoco-warp.md)
- [Genesis World (formerly Genesis): a generative and universal physics engine for robotics and beyond](../source/src-genesis-2024-genesis-world.md)
- [Genesis speeds up AI robot training with simulations 430,000x faster than reality](../source/src-kemper-2024-genesis-430000x.md)
- [NVIDIA open-sources PhysX's GPU simulation code](../source/src-thacker-2025-physx-gpu-open-source.md)
- [NVIDIA, Disney and Google contribute open-source Newton engine to the Linux Foundation](../source/src-larabel-2025-newton-linux-foundation.md)

---
Provenance: created in run `2026-10-24-techniques-sim-math`.
