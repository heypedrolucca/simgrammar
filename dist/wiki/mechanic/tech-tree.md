# Tech tree

*Mechanic* · `tech-tree` · status: **sourced**

A research or unlock graph gates buildings, recipes, or abilities behind prerequisites and accumulated research.

| field | value |
|---|---|
| aliases | research tree, technology tree, research |
| family | Progression & goals |
| substrate | Network / graph, Rule system |
| math basis | Graph search, Optimization |
| feedback | Reinforcing (positive) |
| player interface | Choice / cards |
| legibility | 4 |
| emergence potential | 2 |
| authoring cost | 3 |
| compute cost | 1 |
| tuning difficulty | 4 |
| ai leverage | 3 |
| maturity | Classic |
| core count *(computed)* | 12 |
| earliest game *(computed)* | [Sid Meier's Civilization](../game/civilization.md) |
| earliest year *(computed)* | 1991 |
| prevalence *(computed)* | 43 |
| prevalence share *(computed)* | 0.247 |
| subgenre spread *(computed)* | 13 |
| technique count *(computed)* | 3 |
| technique exposure *(computed)* | 0.3 |

## Definition

Technologies are nodes in a directed acyclic graph; each has prerequisites, a research cost, and unlocks. State owned: which techs are researched, current research progress, and queued research. Update rule: each tick or turn, research output (from labs, scientists, or consumed science items) accumulates toward the selected tech; when it reaches the cost, the tech is researched and its unlocks apply. Variants: complete trees where everything is reachable (Civilization), branching trees with exclusive choices, and weighted random draws (Stellaris). Francis Tresham's 1980 board game Civilization is generally credited with introducing the tree, and Sid Meier's Civilization (1991) carried it into video games. Factorio consumes science packs as research input; Stellaris offers three semi-random options per research area, weighted by ethics, scientist traits, and known techs.

## Player Experience

A visible map of future capability. The player plans paths, makes long bets on branches, anticipates key unlocks, and feels progress as a chain of small upgrades toward transformative ones.

## Design Levers

- graph shape: linear, branching, web, or random draws
- cost curve per tier
- research input: abstract points, science items, or scientists
- exclusivity: mutually exclusive branches versus all reachable
- repeatable infinite techs for the late game
- visibility of future nodes

## Failure Modes

- A dominant path that every player follows removes strategic choice.
- Late-tree techs that do nothing useful leave research facilities idle; some players dismantle labs to save upkeep.
- Top techs so strong that the game ends quickly once they are researched, as with the final technologies in Rise of Nations.
- Fully random draws frustrate players who plan, since a needed tech may not appear.

## Dynamics

- Research pace couples to the economy, so economic snowballing compounds into technological leads.
- Exclusive branches create faction or playstyle identity and replay value.
- In factory games, science items make research a production target, linking progression to logistics throughput.

## Open Questions

- Can a tech tree be generated from the simulation's own physics or chemistry so that research discovers real affordances rather than authored unlocks?
- Can RL agents search tree costs and structures for balance faster than human playtesting?

## Backlinks (computed)

**affected by:** [Generalist instructable game agents (SIMA)](../technique/generalist-game-agents.md), [Self-play planning with learned models (AlphaZero, MuZero, Dreamer)](../technique/model-based-planning-muzero.md), [LLM-written skill libraries (Voyager)](../technique/voyager-skill-libraries.md)

**involved in:** [Generated recipe graphs](../opportunity/generated-recipe-graphs.md), [Parallel autobalancing of economies](../opportunity/parallel-autobalance.md), [Research by named scientists](../opportunity/scientists-not-tech-trees.md)

**used by:** [Against the Storm](../game/against-the-storm.md), [Anno 117: Pax Romana](../game/anno-117.md), [Aurora 4X](../game/aurora-4x.md), [Autonauts](../game/autonauts.md), [Big Pharma](../game/big-pharma.md), [Capitalism](../game/capitalism.md), [Captain of Industry](../game/captain-of-industry.md), [Cities: Skylines II](../game/cities-skylines-2.md), [Sid Meier's Civilization](../game/civilization.md), [Crusader Kings III](../game/crusader-kings-3.md), [Dyson Sphere Program](../game/dyson-sphere-program.md), [Eco](../game/eco.md), [Europa Universalis IV](../game/europa-universalis-4.md), [Factorio](../game/factorio.md), [Farthest Frontier](../game/farthest-frontier.md), [Frostpunk](../game/frostpunk.md), [Frostpunk 2](../game/frostpunk-2.md), [Game Dev Tycoon](../game/game-dev-tycoon.md), [Going Medieval](../game/going-medieval.md), [Hearts of Iron IV](../game/hearts-of-iron-4.md), [Jurassic World Evolution](../game/jurassic-world-evolution.md), [Kenshi](../game/kenshi.md), [Kerbal Space Program](../game/kerbal-space-program.md), [Mindustry](../game/mindustry.md), [Minecraft](../game/minecraft.md), [Offworld Trading Company](../game/offworld-trading-company.md), [Oxygen Not Included](../game/oxygen-not-included.md), [Plague Inc.](../game/plague-inc.md), [Planet Coaster](../game/planet-coaster.md), [Planet Zoo](../game/planet-zoo.md), [Prison Architect](../game/prison-architect.md), [RollerCoaster Tycoon](../game/rollercoaster-tycoon.md), [Satisfactory](../game/satisfactory.md), [Screeps](../game/screeps.md), [shapez 2](../game/shapez-2.md), [Stellaris](../game/stellaris.md), [Surviving Mars](../game/surviving-mars.md), [The Farmer Was Replaced](../game/the-farmer-was-replaced.md), [Theme Hospital](../game/theme-hospital.md), [Theme Park](../game/theme-park.md), [Two Point Hospital](../game/two-point-hospital.md), [Victoria 3](../game/victoria-3.md), [Zoo Tycoon](../game/zoo-tycoon.md)

## Claims

- A technology tree is a directed acyclic graph; Francis Tresham's 1980 board game Civilization is generally credited with introducing it, and Sid Meier's Civilization (1991) is the iconic video game example. *(confidence: medium)* [[95](../source/src-wikipedia-technology-tree.md)]
- Stellaris replaces a fixed tree with three semi-random research options per area, weighted by empire ethics, scientist traits, and known techs, plus rare techs and procedurally generated improvement techs. *(confidence: high)* [[96](../source/src-paradox-2015-stellaris-dev-diary-11.md)]

## Sources

- [Technology tree](../source/src-wikipedia-technology-tree.md)
- [Stellaris Dev Diary #11: Research & Technology](../source/src-paradox-2015-stellaris-dev-diary-11.md)

---
Provenance: created in run `2026-10-24-taxonomy-m6`.
