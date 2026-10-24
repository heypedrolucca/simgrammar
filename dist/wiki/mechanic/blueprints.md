# Blueprints

*Mechanic* · `blueprints` · status: **sourced**

Player-made layouts can be saved, stamped as build orders, copied, and shared as text or files.

| field | value |
|---|---|
| aliases | templates, stamps, copy-paste building, prefabs |
| family | Control & automation |
| substrate | Player-authored logic, Rule system |
| math basis | Combinatorics, Optimization |
| feedback | Reinforcing (positive) |
| player interface | Placement |
| legibility | 5 |
| emergence potential | 2 |
| authoring cost | 1 |
| compute cost | 1 |
| tuning difficulty | 2 |
| ai leverage | 4 |
| maturity | Established |
| core count *(computed)* | 1 |
| earliest game *(computed)* | [Conway's Game of Life](../game/game-of-life.md) |
| earliest year *(computed)* | 1970 |
| prevalence *(computed)* | 12 |
| prevalence share *(computed)* | 0.069 |
| subgenre spread *(computed)* | 8 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

A blueprint is a saved snapshot of a region's entities with relative positions, rotations, and configuration (recipes, filters, circuit settings, sometimes tiles). State owned: a library of blueprints plus placed ghosts awaiting construction. Capture copies selected entities into a blueprint; stamping projects its entities at a cursor with rotation or mirroring, checks placement validity, and creates ghost build orders that construction agents or the player fulfill. Export serializes a blueprint to a string or file that other players can import. Canonical form: Factorio blueprints, blueprint books, a personal library that persists across saves and is visible to other players in multiplayer, and exchange strings used by community sites. Others: Dyson Sphere Program and Satisfactory blueprints, Mindustry schematics shared as text, and Space Engineers ship blueprints rebuilt through projectors.

## Player Experience

Solving a layout once is enough. The player designs a module carefully, then scales it by stamping, which moves attention from placing pieces to designing systems. Imported community designs let newcomers skip solved problems; some players feel that copying removes the puzzle.

## Design Levers

- unlock timing: available from the start or gated behind progression such as construction robots
- what is captured: entities only or also configuration, tiles, and logic
- parameterized blueprints that substitute items or values at placement
- sharing scope: within a save, across saves, or exported strings and workshop integration
- who fulfills placed ghosts: the player by hand or automated builders
- validity rules when stamping over obstacles or partial resources

## Failure Modes

- Imported meta designs replace the core puzzle, and players report feeling they are executing other people's solutions.
- Late unlock makes the repetitive early game tedious and drives players to mods.
- Blueprints that break when stamped into slightly different terrain or orientation cost more time than rebuilding by hand.

## Dynamics

- Modular, tileable designs become dominant because they stamp cleanly, shaping the visual language of player bases.
- Shared blueprint strings create a design culture of named, versioned community layouts.
- Stamping lowers the marginal cost of expansion, so growth becomes limited by resources and logistics rather than player time.

## Open Questions

- Can generative models produce valid blueprints from a goal such as a 45 per second green circuit block, and does that remove or relocate the design puzzle?
- How should parameterized blueprints be represented so designs adapt to terrain and recipes without becoming full programming?

## Relations

**synergy**

- [Conveyor transport](../mechanic/conveyor-transport.md): Stamping solved belt layouts lets players scale proven designs instead of re-solving them.
- [Content sharing](../mechanic/content-sharing.md): Shareable blueprint strings created whole communities of design exchange.

## Backlinks (computed)

**involved in:** [Teachable sim companion](../opportunity/teachable-sim-companion.md)

**used by:** [Anno 1800](../game/anno-1800.md), [Capitalism](../game/capitalism.md), [Dyson Sphere Program](../game/dyson-sphere-program.md), [Factorio](../game/factorio.md), [Conway's Game of Life](../game/game-of-life.md), [Garry's Mod](../game/garrys-mod.md), [Mindustry](../game/mindustry.md), [Planet Coaster](../game/planet-coaster.md), [Satisfactory](../game/satisfactory.md), [shapez 2](../game/shapez-2.md), [Space Engineers](../game/space-engineers.md), [The Sims 4](../game/the-sims-4.md)

## Claims

- Factorio's blueprint library keeps a player's blueprints across saves, shares them with other players in multiplayer, and separately holds save-specific game blueprints. *(confidence: high)* [[58](../source/src-wube-2016-fff-170-blueprint-library.md)]

## Sources

- [Friday Facts #170 - Blueprint library GUI design and redesign](../source/src-wube-2016-fff-170-blueprint-library.md)

---
Provenance: created in run `2026-10-24-taxonomy-m6`.
