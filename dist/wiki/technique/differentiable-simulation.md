# Differentiable simulation

*Technique* · `differentiable-simulation` · status: **sourced**

Simulators written so automatic differentiation returns gradients of an outcome with respect to initial state, controls, or rule parameters, replacing black-box search with gradient descent for tuning and inverse design.

| field | value |
|---|---|
| aliases | differentiable physics, DiffTaichi, NVIDIA Warp, GradABM, differentiable agent-based models |
| category | Differentiable & accelerated simulation |
| year | 2020 |
| maturity | Research |
| trl | 3 |
| runtime | Offline authoring, Design assist |
| determinism impact | Preserves |
| horizon | 3-5 years |
| risks | Controllability, Compute cost |
| deployed in |  |
| affects count *(computed)* | 6 |

## Summary

Simulators written so automatic differentiation returns gradients of an outcome with respect to initial state, controls, or rule parameters, replacing black-box search with gradient descent for tuning and inverse design.

## Mechanism

The simulator step is written in a language with automatic differentiation: source-transformed kernels (DiffTaichi, NVIDIA Warp) or traced array programs (JAX in Brax). A loss is defined on the final or accumulated state, for example distance of a soft robot from a goal or error between simulated and observed infection counts. Reverse-mode differentiation propagates the gradient back through every timestep to the parameters, which are updated by gradient descent. Contacts and discrete events are smoothed or given surrogate gradients. For agent-based models, agent state is held in tensors and stochastic discrete events are replaced by differentiable relaxations so the whole population update has gradients (GradABM). The payoff is that tuning takes tens of gradient iterations instead of thousands of blind rollouts.

## Limitations

- Collisions, contact switching, and integer or threshold game rules give zero, undefined, or misleading gradients and need smoothing or relaxations that change the dynamics being tuned.
- Reverse-mode differentiation must store or recompute intermediate states, so memory grows with timesteps times state size; long horizons also produce exploding or vanishing gradients.
- Support is incomplete in production-grade GPU engines; MuJoCo Warp lists differentiability via Warp as not yet available.
- Gradient descent finds local optima of a stated loss; matching a target curve is not the same as making a system fun or balanced.

## Relations

**affects**

- [Design performance rating](../mechanic/design-performance-rating.md) (Explains): The gradient of a design's rating with respect to each part parameter tells the player which strut, joint or track segment most changes the score, enabling hints like 'move this support left'.
- [Soft-body deformation](../mechanic/soft-body-deformation.md) (Tunes / balances): Material stiffness and damping of node-beam or finite-element bodies can be fitted to reference motion or a target feel by gradient descent, as DiffTaichi does for elastic objects.
- [Vehicle dynamics](../mechanic/vehicle-dynamics.md) (Tunes / balances): Tire, suspension and drivetrain constants can be fitted to recorded telemetry by differentiating lap or trajectory error, replacing manual parameter sweeps.
- [Contagion](../mechanic/contagion.md) (Tunes / balances): GradABM shows transmission parameters of a million-agent outbreak model calibrated to real case data by gradients, a route to epidemic games whose curves match real diseases or designer targets.
- [Fluid and gas simulation](../mechanic/fluid-gas-simulation.md) (Tunes / balances): Differentiable fluid kernels (Warp, DiffTaichi) allow inverse design, solving for emitter or vent settings that produce a target flow, usable for level authoring or tuning puzzles.
- [Modular assembly](../mechanic/modular-assembly.md) (Enables new form): A controller for a player-built soft or articulated body can be optimized in tens of gradient iterations, so assembled machines can learn to walk or swim during play.

## Backlinks (computed)

**applied in:** [Bottleneck explainer for production networks](../opportunity/bottleneck-explainer.md), [Branch preview of policy futures](../opportunity/branch-preview-forecasts.md), [Calibrated serious simulations](../opportunity/calibrated-serious-sims.md), [Parallel autobalancing of economies](../opportunity/parallel-autobalance.md)

## Claims

- DiffTaichi implemented 10 differentiable simulators; its elastic-object simulator was 4.2x shorter than hand-written CUDA at similar speed and 188x faster than a TensorFlow version, and neural controllers optimized in tens of iterations. *(confidence: high)* [[121](../source/src-hu-2020-difftaichi.md)]
- Brax exposed gradients through a JAX rigid-body engine running at millions of steps per second on one accelerator. *(confidence: medium)* [[122](../source/src-freeman-2021-brax.md)]
- NVIDIA Warp lets developers write differentiable GPU kernels in Python; NVIDIA reports Autodesk fluid simulations 8x faster and 5x larger than with traditional frameworks. *(confidence: medium)* [[123](../source/src-nvidia-2024-warp-blog.md)]
- GradABM made a million-agent epidemic agent-based model differentiable, ran it in a few seconds on commodity hardware, and calibrated it to COVID-19 and influenza data by gradient descent. *(confidence: high)* [[124](../source/src-chopra-2023-gradabm.md)]
- As of 2026, gradient support is uneven across GPU engines: MuJoCo Warp lists differentiability via Warp as not yet available. *(confidence: medium)* [[125](../source/src-deepmind-2026-mujoco-warp.md)]

## Sources

- [DiffTaichi: Differentiable Programming for Physical Simulation](../source/src-hu-2020-difftaichi.md)
- [Brax: A Differentiable Physics Engine for Large Scale Rigid Body Simulation](../source/src-freeman-2021-brax.md)
- [Warp Speed: NVIDIA Open-Source Framework Accelerates Scientific Computing in Python](../source/src-nvidia-2024-warp-blog.md)
- [Differentiable Agent-based Epidemiology](../source/src-chopra-2023-gradabm.md)
- [MuJoCo Warp (MJWarp)](../source/src-deepmind-2026-mujoco-warp.md)

---
Provenance: created in run `2026-10-24-techniques-sim-math`.
