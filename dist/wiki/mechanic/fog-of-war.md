# Fog of war

*Mechanic* · `fog-of-war` · status: **sourced**

Parts of the world stay hidden or stale until observed by the player's units, structures, or sensors.

| field | value |
|---|---|
| aliases | shroud, line of sight, map reveal |
| family | Information & legibility |
| substrate | Cellular grid, Rule system |
| math basis | Information theory, Game theory |
| feedback | None |
| player interface | Observation only |
| legibility | 4 |
| emergence potential | 3 |
| authoring cost | 1 |
| compute cost | 2 |
| tuning difficulty | 3 |
| ai leverage | 3 |
| maturity | Classic |
| core count *(computed)* | 3 |
| earliest game *(computed)* | [Sid Meier's Civilization](../game/civilization.md) |
| earliest year *(computed)* | 1991 |
| prevalence *(computed)* | 13 |
| prevalence share *(computed)* | 0.075 |
| subgenre spread *(computed)* | 7 |
| technique count *(computed)* | 1 |
| technique exposure *(computed)* | 0.188 |

## Definition

For each player the world holds a visibility state per cell or entity, usually three-valued: unexplored, explored but not currently visible, and visible. Each tick visibility is recomputed from the sight radius of the player's units, buildings, and sensors, optionally modified by line of sight, elevation, weather, and target stealth. Visible cells show live state; explored cells show the last observed snapshot, so changes there go unseen. Inputs are observer positions and sensor ranges; outputs are a per-player view and a hidden-information gap between true and known state. Walter Bright's Empire (1977) is credited as the earliest use; Warcraft and StarCraft used the explored-but-stale shroud. In simulation games: Factorio's radar charts distant chunks slowly and keeps nearby ones live, unexcavated tiles in Dwarf Fortress stay unknown, and Against the Storm keeps forest glades hidden until opened.

## Player Experience

The edge of the known map pulls the player outward. Scouting becomes a decision with costs, darkness reads as threat, and finding a resource deposit or an enemy base feels like discovery rather than lookup.

## Design Levers

- two-state (unexplored or visible) versus three-state with stale memory
- sight radius per unit or building and terrain, elevation, and weather modifiers
- radius check versus true line-of-sight raycasts
- whether remembered cells show last-seen enemies or only terrain
- reveal tools: scouts, radar, satellites, traded maps
- whether the AI obeys the same fog or has full knowledge

## Failure Modes

- An AI given full map knowledge to compensate for weak reasoning feels like cheating once players notice.
- Fog that hides only static terrain becomes a one-time clearing chore with no lasting tension.
- Cheap, fast scouts make fog trivial and reward spamming them.
- In simulations whose threats are systemic rather than adversarial, fog adds travel tedium without decisions.

## Dynamics

- Hidden information enables ambushes, bluffs, and a scouting economy where information has a price.
- Stale memory produces errors such as attacking a base that has since been reinforced.
- Coupled with procedural terrain, fog turns every map into an exploration problem rather than a known layout.

## Open Questions

- Can learned opponents that keep beliefs about unseen state replace AI map-hacking without losing challenge?
- If a generative world model creates unobserved regions only when observed, does fog become a generation trigger rather than concealment?

## Relations

**synergy**

- [Military operations](../mechanic/military-operations.md): Sensor coverage and concealment are central to operational play.

## Backlinks (computed)

**affected by:** [Regret minimization and search for imperfect-information games](../technique/imperfect-information-solvers.md)

**used by:** [Against the Storm](../game/against-the-storm.md), [Aurora 4X](../game/aurora-4x.md), [Sid Meier's Civilization](../game/civilization.md), [Command: Modern Operations](../game/command-modern-operations.md), [Elite Dangerous](../game/elite-dangerous.md), [Europa Universalis IV](../game/europa-universalis-4.md), [Frostpunk](../game/frostpunk.md), [FTL: Faster Than Light](../game/ftl.md), [Hearts of Iron IV](../game/hearts-of-iron-4.md), [Project Zomboid](../game/project-zomboid.md), [Silent Hunter III](../game/silent-hunter-3.md), [SnowRunner](../game/snowrunner.md), [Stellaris](../game/stellaris.md)

## Claims

- Walter Bright's 1977 game Empire is credited as the earliest video game use of fog of war, and Warcraft and StarCraft keep previously seen areas visible as terrain while hiding changes to enemy units. *(confidence: medium)* [[75](../source/src-wikipedia-fog-of-war.md)]

## Sources

- [Fog of war](../source/src-wikipedia-fog-of-war.md)

---
Provenance: created in run `2026-10-24-taxonomy-m6`.
