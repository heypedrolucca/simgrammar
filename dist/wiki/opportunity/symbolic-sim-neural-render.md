# Symbolic simulation, neural rendering

*Opportunity* · `symbolic-sim-neural-render` · status: **asserted**

Keep gameplay in a small deterministic symbolic simulation and let a generative world model render it, decoupling visual variety from simulation cost and art budgets.

| field | value |
|---|---|
| opportunity type | Infrastructure |
| involves | [Decoration and beauty](../mechanic/decoration-beauty.md), [Procedural build assist](../mechanic/procedural-build-assist.md), [Building placement](../mechanic/free-placement.md), [Zoning](../mechanic/zoning.md), [Data overlays](../mechanic/data-overlays.md) |
| applies | [Diffusion and autoregressive neural game engines](../technique/diffusion-game-engines.md), [Genie foundation world models](../technique/genie-world-models.md), [Neural rendering in the graphics pipeline](../technique/neural-rendering-shaders.md), [3D Gaussian Splatting](../technique/gaussian-splatting.md) |
| precedent | [Townscaper](../game/townscaper.md), [Tiny Glade](../game/tiny-glade.md), [Cities: Skylines](../game/cities-skylines.md), [Islanders](../game/islanders.md) |
| novelty | 5 |
| feasibility | 2 |
| impact | 4 |
| horizon | 3-5 years |
| falsifiable signal | {'prediction': 'A released game will render its primary view with a generative model conditioned on an explicit symbolic game state.', 'resolve_by': '2029-12-31', 'criteria': 'Developer documentation showing gameplay state is symbolic and the main viewport is produced by a learned generative renderer.'} |
| priority *(computed)* | 3.282 |

## Summary

Keep gameplay in a small deterministic symbolic simulation and let a generative world model render it, decoupling visual variety from simulation cost and art budgets.

## Thesis

Generative world models (GameNGen, Genie 3, Muse, Oasis) produce convincing interactive frames but drift, forget, and cannot be trusted as game state. Simulation games need the opposite: exact, persistent, inspectable state. Splitting the stack resolves the conflict: the authoritative simulation stays symbolic (grids, agents, stocks), and a conditioned generative model renders it, so visual variety becomes nearly free while rules, saves, replays, and multiplayer sync remain deterministic.

## Design Sketch

A city builder whose simulation is a tile grid of typed buildings, agents, and fields. A renderer conditioned on the grid, time of day, and a style prompt produces the view; players restyle their city as medieval, solarpunk, or watercolor without new art. Inspection tools always read the symbolic state.

## Key Risks

- Rendered frames that misrepresent symbolic state confuse players (a building that looks like a hospital but is not).
- Inference cost per frame on consumer GPUs.
- Temporal flicker and style drift across sessions.

## Validation Experiment

Condition an open video or image model on a 32x32 symbolic city grid and measure per-tile semantic fidelity (does a rendered tile read as its type to human raters) and frame time. Success: over 95 percent rater agreement with the symbolic type at 10 frames per second on a current consumer GPU.

## Falsifiable signal

- **Prediction:** A released game will render its primary view with a generative model conditioned on an explicit symbolic game state.
- **Resolve by:** 2029-12-31
- **Criteria:** Developer documentation showing gameplay state is symbolic and the main viewport is produced by a learned generative renderer.

## Relations

**applies**

- [Diffusion and autoregressive neural game engines](../technique/diffusion-game-engines.md)
- [Genie foundation world models](../technique/genie-world-models.md)
- [Neural rendering in the graphics pipeline](../technique/neural-rendering-shaders.md)
- [3D Gaussian Splatting](../technique/gaussian-splatting.md)

**involves**

- [Decoration and beauty](../mechanic/decoration-beauty.md)
- [Procedural build assist](../mechanic/procedural-build-assist.md)
- [Building placement](../mechanic/free-placement.md)
- [Zoning](../mechanic/zoning.md)
- [Data overlays](../mechanic/data-overlays.md)

**precedent**

- [Townscaper](../game/townscaper.md)
- [Tiny Glade](../game/tiny-glade.md)
- [Cities: Skylines](../game/cities-skylines.md)
- [Islanders](../game/islanders.md)

---
Provenance: created in run `2026-10-24-synthesis`.
