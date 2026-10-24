# Gran Turismo 7

*Game* · `gran-turismo-7` · status: **sourced**

A console racing simulator that combines a detailed vehicle dynamics model and car collection with GT Sophy, a deep reinforcement learning opponent added as a permanent rival in 2023.

| field | value |
|---|---|
| year | 2022 |
| developer | Polyphony Digital |
| platforms | Console |
| subgenre | Vehicle sim |
| sim domain | Physical / mechanical, Sports |
| player role | Operator / pilot |
| agency model | Direct avatar |
| time model | Real-time |
| sim scale | Individual |
| fidelity | High-fidelity |
| perspective | Third-person |
| win structure | Campaign |
| failure model | Soft / recoverable |
| narrative mode | Authored |
| multiplayer | Single-player, Competitive |
| modding | None |
| production tier | AAA |
| agent count order | ~10 |
| emergence | 2 |
| influence | 3 |
| core loop | buy or tune a car -> race against AI or players -> earn credits -> expand the collection -> harder events |
| influenced by | [Gran Turismo](../game/gran-turismo.md) |
| cluster *(computed)* | C03 |
| core count *(computed)* | 2 |
| mechanic count *(computed)* | 6 |

## Summary

A console racing simulator that combines a detailed vehicle dynamics model and car collection with GT Sophy, a deep reinforcement learning opponent added as a permanent rival in 2023.

## Design Notes

Included because it is the clearest shipped case of a learned opponent in a simulation game. GT Sophy, trained with model-free deep reinforcement learning on parallel simulator instances, became selectable as a permanent rival in 2023 and was extended to custom races in 2025, one content update at a time.

## Relations

**influenced by**

- [Gran Turismo](../game/gran-turismo.md)

**uses**

- [Vehicle dynamics](../mechanic/vehicle-dynamics.md) (core): Tire, suspension, aerodynamics, and drivetrain models per car; tuning parts and settings change handling.
- [Embodied skill control](../mechanic/embodied-skill-control.md) (core): Racing lines, braking points, and throttle control on wheel or pad decide results; GT Sophy is trained to the same physics.
- [Collection goals](../mechanic/collection-goals.md) (supporting)
- [Career ladder](../mechanic/career-ladder.md) (supporting)
- [Scenario objectives](../mechanic/scenario-objectives.md) (supporting)
- [Weather](../mechanic/weather.md) (supporting)

## Backlinks (computed)

**deploys:** [Deep reinforcement learning policies for NPC opponents and navigation](../technique/deep-rl-npc-policies.md)

## Claims

- GT Sophy 2.0 was added to Gran Turismo 7 as a rival in Quick Race across nine tracks and 340 cars in November 2023. *(confidence: high)* [[22](../source/src-polyphony-2023-gt-sophy-2.md)]
- In 2025 GT Sophy 2.1 extended to Custom Race with tuning, tire, and fuel options. *(confidence: high)* [[23](../source/src-sony-2025-gt-sophy-2-1.md)]

## Sources

- [Gran Turismo Sophy 2.0 permanently added to Gran Turismo 7](../source/src-polyphony-2023-gt-sophy-2.md)
- [Sony AI Expands Capabilities of Breakthrough AI Agent Gran Turismo Sophy](../source/src-sony-2025-gt-sophy-2-1.md)
- [Outracing champion Gran Turismo drivers with deep reinforcement learning](../source/src-wurman-2022-gt-sophy.md)

---
Provenance: created in run `2026-10-24-catalog-additions`.
