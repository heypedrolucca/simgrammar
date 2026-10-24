# Deep reinforcement learning policies for NPC opponents and navigation

*Technique* · `deep-rl-npc-policies` · status: **sourced**

Neural control policies trained with deep reinforcement learning inside the game's own simulation drive opponents and NPCs, as with Sony AI's Gran Turismo Sophy, a selectable rival in Gran Turismo 7 since 2023.

| field | value |
|---|---|
| aliases | Gran Turismo Sophy, GT Sophy, learned NPC controllers, Unity ML-Agents |
| category | Reinforcement learning |
| year | 2022 |
| maturity | Shipped (niche) |
| trl | 7 |
| runtime | Offline authoring, Client real-time |
| determinism impact | Mitigable |
| horizon | Now |
| risks | Compute cost, Controllability, Evaluation difficulty |
| builds on | [Massively parallel GPU simulation](../technique/massively-parallel-simulation.md) |
| deployed in | [Gran Turismo 7](../game/gran-turismo-7.md) |
| affects count *(computed)* | 3 |

## Summary

Neural control policies trained with deep reinforcement learning inside the game's own simulation drive opponents and NPCs, as with Sony AI's Gran Turismo Sophy, a selectable rival in Gran Turismo 7 since 2023.

## Mechanism

The game exposes observations (car state, track geometry, nearby opponents; or local terrain and goal direction for navigation) and actions (steering, throttle, brake; or movement and ability inputs) to a learning agent. Many instances run in parallel, and model-free deep RL learns a policy network that maps observations to actions to maximize a shaped reward. For GT Sophy the reward values course progress and was designed to encode racing's under-specified sportsmanship rules, and training mixed racing scenarios so one policy handles both speed and tactics. For NPCs with jetpacks, grappling hooks, or double jumps, where navigation meshes break down, the reward is reaching a goal. The trained network is small enough to run every frame. Difficulty is set by giving the agent cars of different performance or alternate checkpoints, and later GT Sophy versions expose settings such as tire and fuel consumption. Toolkits such as Unity ML-Agents connect engine scenes to training code.

## Limitations

- Coverage arrives per content item: GT Sophy grew from four cars and four tracks to nine tracks and 340 cars across updates, because each track and car needs training and validation.
- A policy trained to win needs reward shaping and later refinement for sportsmanship and enjoyment; Sony AI describes refining GT Sophy's behavior for etiquette and players of all skill levels after the research version.
- Availability was narrow at first: GT Sophy 2.0 ran only in Quick Race on PS5, not in other events on the same tracks.
- Learned policies are hard to direct for scripted moments, and physics or content patches can require retraining and re-validation.
- Deep RL transfers poorly between games without heavy tuning, as EA reported, so each title builds its own training setup.

## Sources

- src-wurman-2022-gt-sophy
- src-polyphony-2023-gt-sophy-race-together
- src-polyphony-2023-gt-sophy-2
- src-sony-2025-gt-sophy-2-1
- src-alonso-2020-drl-navigation-aaa
- src-juliani-2018-unity-ml-agents
- src-zhao-2019-winning-isnt-everything

## Relations

**affects**

- [Vehicle dynamics](../mechanic/vehicle-dynamics.md) (Deepens): AI drivers operate the same tire, suspension, and weight-transfer model as the player at champion level, so handling fidelity matters in races against the AI instead of being sidestepped by scripted racing lines.
- [Embodied skill control](../mechanic/embodied-skill-control.md) (Deepens): Players practice against an opponent whose skill comes from the same controls and physics, at selectable levels (Beginner to Expert, then custom tire and fuel settings), raising the ceiling of a skill-centered mechanic.
- [Agent pathfinding](../mechanic/agent-pathfinding.md) (Replaces substrate): For movement abilities such as grappling hooks, jetpacks, and double jumps, a learned policy replaces hand-placed navigation-mesh links, so NPCs can traverse spaces designers would otherwise annotate by hand.

**builds on**

- [Massively parallel GPU simulation](../technique/massively-parallel-simulation.md)

**deployed in**

- [Gran Turismo 7](../game/gran-turismo-7.md)

## Claims

- GT Sophy, trained with model-free deep RL across mixed racing scenarios and a reward designed around sportsmanship rules, beat four of the world's best Gran Turismo drivers head to head (Nature, February 2022). *(confidence: high)* [[117](../source/src-wurman-2022-gt-sophy.md)]
- GT Sophy entered Gran Turismo 7 as the time-limited Race Together event in update 1.29 (February 2023), with four races against GT Sophy cars of different performance at Beginner, Intermediate, and Expert levels and a 1vs1 mode. *(confidence: high)* [[118](../source/src-polyphony-2023-gt-sophy-race-together.md)]
- GT Sophy 2.0 became a permanent Quick Race rival in GT7's Spec II update (November 2023) on nine tracks and 340 cars, 95% of the car models, up from four cars and four tracks, on PS5 only. *(confidence: high)* [[22](../source/src-polyphony-2023-gt-sophy-2.md)]
- GT Sophy 2.1 (update 1.57, March 2025) moved into Custom Race with 19 car and track options, lap count, parts and tuning changes, and adjustable tire and fuel consumption. *(confidence: high)* [[23](../source/src-sony-2025-gt-sophy-2-1.md)]
- Ubisoft La Forge's deep RL navigation handled grappling hooks, jetpacks, teleporters, and double jumps on maps about ten times larger than typical RL research maps, one modeled on a Ubisoft AAA game, with at least 90% success. *(confidence: medium)* [[119](../source/src-alonso-2020-drl-navigation-aaa.md)]
- Unity's open-source ML-Agents Toolkit lets developers train agents inside Unity scenes. *(confidence: high)* [[120](../source/src-juliani-2018-unity-ml-agents.md)]

## Sources

- [Outracing champion Gran Turismo drivers with deep reinforcement learning](../source/src-wurman-2022-gt-sophy.md)
- [Gran Turismo Sophy Race Together event in Gran Turismo 7](../source/src-polyphony-2023-gt-sophy-race-together.md)
- [Gran Turismo Sophy 2.0 permanently added to Gran Turismo 7](../source/src-polyphony-2023-gt-sophy-2.md)
- [Sony AI Expands Capabilities of Breakthrough AI Agent Gran Turismo Sophy](../source/src-sony-2025-gt-sophy-2-1.md)
- [Deep Reinforcement Learning for Navigation in AAA Video Games](../source/src-alonso-2020-drl-navigation-aaa.md)
- [Unity: A General Platform for Intelligent Agents](../source/src-juliani-2018-unity-ml-agents.md)
- [Winning Isn't Everything: Enhancing Game Development with Intelligent Agents](../source/src-zhao-2019-winning-isnt-everything.md)

---
Provenance: created in run `2026-10-24-techniques-rl-design`.
