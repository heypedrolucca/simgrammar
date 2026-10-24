# Event-sourced simulation runtime

*Opportunity* · `event-sourced-sim-runtime` · status: **asserted**

An engine layer that records simulation and model calls as an append-only event log, giving replay, forking, explanation, and determinism for games with AI components.

| field | value |
|---|---|
| opportunity type | Infrastructure |
| involves | [History chronicle](../mechanic/history-chronicle.md), [Forecasting](../mechanic/forecasting.md), [Persistent shared world](../mechanic/persistent-world.md), [Causal breakdown tooltips](../mechanic/causal-tooltips.md), [Modding API](../mechanic/modding-api.md) |
| applies | [Grammar-constrained decoding for valid game actions](../technique/constrained-decoding.md), [LLM explanation of simulation state](../technique/llm-explanation-of-state.md), [Massively parallel GPU simulation](../technique/massively-parallel-simulation.md) |
| precedent | [Dwarf Fortress](../game/dwarf-fortress.md), [Factorio](../game/factorio.md), [EVE Online](../game/eve-online.md) |
| novelty | 3 |
| feasibility | 4 |
| impact | 4 |
| horizon | 1-2 years |
| key risks | Log size grows quickly in large simulations., Retrofitting existing engines is costly., Privacy and storage of logged player text. |
| falsifiable signal | {'prediction': 'A game engine or middleware vendor will ship an event-log-based replay and determinism layer designed for generative AI components.', 'resolve_by': '2028-12-31', 'criteria': 'Public release from Unity, Epic, a major middleware vendor, or an open-source project with documented adoption in a shipped game.'} |
| priority *(computed)* | 3.776 |

## Summary

An engine layer that records simulation and model calls as an append-only event log, giving replay, forking, explanation, and determinism for games with AI components.

## Thesis

Most AI-component risks in simulation games are determinism risks: model outputs are not reproducible, so replays, lockstep multiplayer, bug reports, and save integrity break. Recording every model call and its output as an event, and treating the log as the source of truth with state as a projection, restores reproducibility: replays read cached outputs, forks branch from any event, and explanations cite events. The same log feeds why-queries, branch previews, and chronicles.

## Design Sketch

Developers use a runtime where every state change, including those decided by a model, is an event with inputs, outputs, and causes. Replays and multiplayer clients consume logged outputs instead of re-calling models. Tools offer fork-from-here, diff-between-branches, and cause tracing.

## Key Risks

- Log size grows quickly in large simulations.
- Retrofitting existing engines is costly.
- Privacy and storage of logged player text.

## Validation Experiment

Wrap the model calls of an AI-agent prototype in an event log, then replay 100 sessions and verify byte-identical state reconstruction and fork divergence only after the fork point. Success: 100 percent reproducible replays with log overhead under 20 percent of save size per hour.

## Falsifiable signal

- **Prediction:** A game engine or middleware vendor will ship an event-log-based replay and determinism layer designed for generative AI components.
- **Resolve by:** 2028-12-31
- **Criteria:** Public release from Unity, Epic, a major middleware vendor, or an open-source project with documented adoption in a shipped game.

## Relations

**applies**

- [Grammar-constrained decoding for valid game actions](../technique/constrained-decoding.md)
- [LLM explanation of simulation state](../technique/llm-explanation-of-state.md)
- [Massively parallel GPU simulation](../technique/massively-parallel-simulation.md)

**involves**

- [History chronicle](../mechanic/history-chronicle.md)
- [Forecasting](../mechanic/forecasting.md)
- [Persistent shared world](../mechanic/persistent-world.md)
- [Causal breakdown tooltips](../mechanic/causal-tooltips.md)
- [Modding API](../mechanic/modding-api.md)

**precedent**

- [Dwarf Fortress](../game/dwarf-fortress.md)
- [Factorio](../game/factorio.md)
- [EVE Online](../game/eve-online.md)

---
Provenance: created in run `2026-10-24-synthesis`.
