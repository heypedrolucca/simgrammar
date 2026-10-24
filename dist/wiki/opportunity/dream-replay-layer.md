# Generated dream and replay views

*Opportunity* · `dream-replay-layer` · status: **asserted**

Use generative world models for non-authoritative views such as memories, rumors, and alternate histories, where drift is acceptable and variety is the point.

| field | value |
|---|---|
| opportunity type | New mechanic |
| involves | [Memories and thoughts](../mechanic/memories-thoughts.md), [History chronicle](../mechanic/history-chronicle.md), [Gossip propagation](../mechanic/gossip-propagation.md), [Simulated history generation](../mechanic/history-generation.md), [Forecasting](../mechanic/forecasting.md) |
| applies | [Genie foundation world models](../technique/genie-world-models.md), [Diffusion and autoregressive neural game engines](../technique/diffusion-game-engines.md), [Open real-time interactive video world models](../technique/open-interactive-video-models.md) |
| precedent | [Dwarf Fortress](../game/dwarf-fortress.md), [RimWorld](../game/rimworld.md), [Kenshi](../game/kenshi.md) |
| novelty | 5 |
| feasibility | 3 |
| impact | 2 |
| horizon | 1-2 years |
| key risks | Generation latency breaks the inspection flow., Generated imagery of violent events needs content controls., Players may read subjective views as ground truth. |
| falsifiable signal | {'prediction': 'A shipped game will use a generative video or world model to show character memories or in-world histories.', 'resolve_by': '2028-12-31', 'criteria': 'Store page, trailer, or patch notes describing generated memory or history visualizations.'} |
| priority *(computed)* | 2.769 |

## Thesis

The weaknesses of generative world models (short consistency horizon, no exact state) disqualify them as engines but suit a different role: showing things that are supposed to be subjective. A colonist's memory, a rumor that changed in the telling, a forecast that might not happen, or the history of a ruin are views where approximation reads as character rather than bug.

## Design Sketch

Clicking a memory in a colonist's inspector plays a few seconds of generated footage conditioned on the logged event and the colonist's mood. Rumors render with distortions proportional to how many retellings they passed through. Ruins found in worldgen offer a short generated vision of their past from history-generation records.

## Key Risks

- Generation latency breaks the inspection flow.
- Generated imagery of violent events needs content controls.
- Players may read subjective views as ground truth.

## Validation Experiment

Prototype generated memory clips from 50 logged events in a colony sim using an available video model; measure generation time and ask players whether clips increased attachment. Success: under 10 seconds per clip and a majority reporting increased attachment.

## Falsifiable signal

- **Prediction:** A shipped game will use a generative video or world model to show character memories or in-world histories.
- **Resolve by:** 2028-12-31
- **Criteria:** Store page, trailer, or patch notes describing generated memory or history visualizations.

## Relations

**applies**

- [Genie foundation world models](../technique/genie-world-models.md)
- [Diffusion and autoregressive neural game engines](../technique/diffusion-game-engines.md)
- [Open real-time interactive video world models](../technique/open-interactive-video-models.md)

**involves**

- [Memories and thoughts](../mechanic/memories-thoughts.md)
- [History chronicle](../mechanic/history-chronicle.md)
- [Gossip propagation](../mechanic/gossip-propagation.md)
- [Simulated history generation](../mechanic/history-generation.md)
- [Forecasting](../mechanic/forecasting.md)

**precedent**

- [Dwarf Fortress](../game/dwarf-fortress.md)
- [RimWorld](../game/rimworld.md)
- [Kenshi](../game/kenshi.md)

---
Provenance: created in run `2026-10-24-synthesis`.
