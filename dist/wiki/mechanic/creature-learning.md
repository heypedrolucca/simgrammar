# Creature learning

*Mechanic* · `creature-learning` · status: **sourced**

A creature's behavior is learned from player reward and punishment or from neural adaptation over its life.

| field | value |
|---|---|
| aliases | trainable creature, reinforcement training |
| family | Agents & behavior |
| substrate | Learned model, Agent-based |
| math basis | Machine learning, Utility / decision theory |
| feedback | Both |
| player interface | Direct manipulation, Observation only |
| legibility | 2 |
| emergence potential | 4 |
| authoring cost | 2 |
| compute cost | 2 |
| tuning difficulty | 4 |
| ai leverage | 4 |
| maturity | Experimental |
| core count *(computed)* | 3 |
| earliest game *(computed)* | [Creatures](../game/creatures.md) |
| earliest year *(computed)* | 1996 |
| prevalence *(computed)* | 4 |
| prevalence share *(computed)* | 0.023 |
| subgenre spread *(computed)* | 3 |
| technique count *(computed)* | 3 |
| technique exposure *(computed)* | 0.625 |

## Definition

Owns a creature's learned decision parameters: weights linking perceived situations or objects to actions. After the creature acts, a reward or punishment signal (a player stroke or slap, or a change in an internal drive) adjusts the weights for that situation-action pair, so its future selection probability rises or falls and generalizes to similar situations. Creatures (1996) uses about 1,000 neurons in 9 lobes; a 16-cell decision layer picks the strongest-firing action; drive reduction releases a reward chemical and drive increase a punishment chemical, which reinforce excitatory or inhibitory synapses, so norns learn to eat when hungry but not when full. In Black & White (2001) the creature follows a belief-desire-intention model with desires as simplified perceptrons and opinions as decision trees; the player strokes or slaps it after actions and uses leashes to direct its attention. Inputs: player feedback, drives, perceived objects. Outputs: changed action probabilities.

## Player Experience

The player becomes a parent or trainer. Each reward is a bet about what the creature will generalize, and personality emerges from the history of training. Success feels like understanding; failure feels like a stubborn pet, and players blame themselves for bad habits.

## Design Levers

- learning rate and how quickly old associations fade
- credit assignment window that decides which recent action receives the feedback
- granularity of the situation representation (object types, desires, contexts), which decides what generalizes
- feedback channels such as stroke and slap, food, demonstration, and attention leashes
- innate drives and biases the learning starts from

## Failure Modes

- Credit assignment errors attach feedback to the wrong action or object, and players cannot tell why the creature learned something.
- Learning too slowly makes training feel ignored; too quickly lets one slap erase hours of shaping.
- Generalization surprises, such as a creature learning to eat villagers, read as bugs rather than lessons.
- Emergent learned behavior varies by player, which makes testing and balancing expensive; Black & White was later called overrated for underusing its creature.

## Dynamics

- Creatures from the same start diverge into distinct personalities, which drives players to share and compare them.
- Learned behavior acts on the world, so training choices reshape villages, alignment, and appearance in Black & White.
- Learning from internal drives without player input produces self-taught habits and odd local optima.

## Open Questions

- Can modern reinforcement learning or language-conditioned policies give creatures learning that generalizes the way players intend, with explainable credit assignment?
- Does exposing a creature's learned associations improve attachment or destroy the illusion of a mind?

## Relations

**synergy**

- [God powers](../mechanic/god-powers.md): The creature learns from how the god acts, making the player's own behavior a training signal (Black & White).

## Backlinks (computed)

**affected by:** [Massively parallel GPU simulation](../technique/massively-parallel-simulation.md), [Self-play planning with learned models (AlphaZero, MuZero, Dreamer)](../technique/model-based-planning-muzero.md), [Open-ended co-generation of environments and agents](../technique/open-ended-environment-generation.md)

**involved in:** [Trainable creatures revival](../opportunity/trainable-creatures-revival.md)

**used by:** [Black & White](../game/black-and-white.md), [Creatures](../game/creatures.md), [Nintendogs](../game/nintendogs.md), [Seaman](../game/seaman.md)

## Sources

- [Creatures: Artificial Life Autonomous Software Agents for Home Entertainment](../source/src-grand-1996-creatures-alife.md)
- [Black & White (video game)](../source/src-wikipedia-black-and-white.md)

---
Provenance: created in run `2026-10-24-taxonomy-m3`.
