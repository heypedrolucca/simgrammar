# Smart objects

*Mechanic* · `smart-objects` · status: **sourced**

Objects advertise the need satisfaction they offer, and agents query nearby objects to decide what to do.

| field | value |
|---|---|
| aliases | object advertisements, affordance broadcasting |
| family | Agents & behavior |
| substrate | Agent-based, Rule system |
| math basis | Utility / decision theory |
| feedback | None |
| player interface | Placement, Observation only |
| legibility | 4 |
| emergence potential | 3 |
| authoring cost | 4 |
| compute cost | 2 |
| tuning difficulty | 3 |
| ai leverage | 3 |
| maturity | Classic |
| core count *(computed)* | 2 |
| earliest game *(computed)* | [The Sims](../game/the-sims.md) |
| earliest year *(computed)* | 2000 |
| prevalence *(computed)* | 4 |
| prevalence share *(computed)* | 0.023 |
| subgenre spread *(computed)* | 1 |
| technique count *(computed)* | 1 |
| technique exposure *(computed)* | 0.125 |

## Definition

Owns per-object interaction definitions: each interaction carries advertisements (which needs it satisfies and by how much), availability checks, distance attenuation, and the behavior script the agent runs. Agents carry no knowledge of how to use things; when choosing, an agent gathers advertisements from reachable objects, scales them by its needs, personality, and distance, selects one, and runs that object's script. In The Sims, per Forbus and Wright's notes, advertisements cover nine motives, can scale with personality points, attenuate with distance through high, moderate, low, or none presets, and check trees hide unavailable interactions; a toilet advertises 0-70 Bladder. Because behavior lives in objects, new objects add new behaviors without changing agent code, which suits expansion packs and mods. Inputs: objects in range, agent needs. Outputs: candidate actions, need restoration, animations.

## Player Experience

Buying or placing an object changes what agents want to do, so the player designs behavior through the environment. Players learn that a better object pulls agents across the room and use placement to steer them.

## Design Levers

- advertised magnitude per need and whether it scales with personality or object quality
- distance attenuation curve per interaction
- advertised versus delivered value, which allows deceptive or broken objects
- availability and permission checks such as ownership, age, and room
- how many agents one object can serve at once

## Failure Modes

- An over-tuned advertisement makes one object a magnet that agents queue for regardless of need.
- Assuming honest advertisements breaks when objects fail, producing loops of agents repeatedly using broken objects.
- Attenuation errors make agents walk past nearby options to distant ones.
- Behavior spread across hundreds of objects is harder to debug than one agent controller.

## Dynamics

- Each new object adds behaviors, so the behavior space grows with content packs, which is how The Sims expansions extended play.
- Players use objects as lures to route agents, coupling placement to behavior.
- Scarce objects create queues and conflicts when several agents select the same one.

## Open Questions

- Can generative models author new objects with consistent advertisements, scripts, and animations, turning content packs into runtime generation?
- Should language-model agents read object affordances as numeric advertisements, as text descriptions, or both?

## Backlinks (computed)

**affected by:** [Learned physics-based character control](../technique/physics-based-character-control.md)

**used by:** [The Sims](../game/the-sims.md), [The Sims 2](../game/the-sims-2.md), [The Sims 3](../game/the-sims-3.md), [The Sims 4](../game/the-sims-4.md)

## Sources

- [Some notes on programming objects in The Sims](../source/src-forbus-2001-programming-objects-sims.md)

---
Provenance: created in run `2026-10-24-taxonomy-m3`.
