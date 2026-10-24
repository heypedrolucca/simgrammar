# Trainable creatures revival

*Opportunity* · `trainable-creatures-revival` · status: **asserted**

Revive the Creatures and Black & White lineage with creatures whose behavior is genuinely learned from player feedback and can explain itself.

| field | value |
|---|---|
| opportunity type | Mechanic upgrade |
| involves | [Creature learning](../mechanic/creature-learning.md), [Creature care](../mechanic/creature-care.md), [Natural-language interaction](../mechanic/natural-language-interaction.md), [Trait inheritance](../mechanic/trait-inheritance.md), [God powers](../mechanic/god-powers.md) |
| applies | [Self-play planning with learned models (AlphaZero, MuZero, Dreamer)](../technique/model-based-planning-muzero.md), [On-device small language models for characters](../technique/on-device-language-models.md), [Generalist instructable game agents (SIMA)](../technique/generalist-game-agents.md) |
| precedent | [Creatures](../game/creatures.md), [Black & White](../game/black-and-white.md), [Seaman](../game/seaman.md), [Nintendogs](../game/nintendogs.md), [Tamagotchi](../game/tamagotchi.md) |
| novelty | 3 |
| feasibility | 3 |
| impact | 3 |
| horizon | 1-2 years |
| key risks | Learning that is too slow or too fast reads as fake., Reward hacking produces creatures that game the player., On-device training cost. |
| falsifiable signal | {'prediction': 'A commercial virtual-pet or god game will ship a creature whose behavior is trained online by player feedback with a learned model.', 'resolve_by': '2029-06-30', 'criteria': 'Developer documentation describing on-device or server learning of a creature policy from player feedback.'} |
| priority *(computed)* | 3.0 |

## Thesis

Creatures (1996) used neural networks and genetics; Black & White (2001) let a creature learn from slaps and strokes. Both were limited by tiny learning systems that generalized poorly and were opaque. Modern reinforcement learning, preference learning, and small language models allow a creature that learns real policies from feedback, generalizes to new situations, and can say in simple words what it thinks it was rewarded for.

## Design Sketch

The player raises a creature in a small world. Rewards, punishments, demonstrations, and spoken commands shape its policy. A 'what I learned' panel lists the creature's inferred rules in plain language with examples; the player can correct misunderstandings. Creatures can be traded and bred, inheriting learned dispositions partially.

## Key Risks

- Learning that is too slow or too fast reads as fake.
- Reward hacking produces creatures that game the player.
- On-device training cost.

## Validation Experiment

Build a creature with a learned policy trained online from player feedback in a 2D world; measure how many feedback events it takes to learn three behaviors and whether its self-explanations match its actual policy. Success: under 30 feedback events per behavior and 80 percent explanation accuracy.

## Falsifiable signal

- **Prediction:** A commercial virtual-pet or god game will ship a creature whose behavior is trained online by player feedback with a learned model.
- **Resolve by:** 2029-06-30
- **Criteria:** Developer documentation describing on-device or server learning of a creature policy from player feedback.

## Relations

**applies**

- [Self-play planning with learned models (AlphaZero, MuZero, Dreamer)](../technique/model-based-planning-muzero.md)
- [On-device small language models for characters](../technique/on-device-language-models.md)
- [Generalist instructable game agents (SIMA)](../technique/generalist-game-agents.md)

**involves**

- [Creature learning](../mechanic/creature-learning.md)
- [Creature care](../mechanic/creature-care.md)
- [Natural-language interaction](../mechanic/natural-language-interaction.md)
- [Trait inheritance](../mechanic/trait-inheritance.md)
- [God powers](../mechanic/god-powers.md)

**precedent**

- [Creatures](../game/creatures.md)
- [Black & White](../game/black-and-white.md)
- [Seaman](../game/seaman.md)
- [Nintendogs](../game/nintendogs.md)
- [Tamagotchi](../game/tamagotchi.md)

---
Provenance: created in run `2026-10-24-synthesis`.
