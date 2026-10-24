# Content sharing

*Mechanic* · `content-sharing` · status: **sourced**

Player creations such as buildings, creatures, or blueprints are uploaded, browsed, rated, and imported into other players' games.

| field | value |
|---|---|
| aliases | user-generated content, workshop, creation sharing |
| family | Multiplayer & persistence |
| substrate | Network / graph, Player-authored logic |
| math basis | Social network models, Probability / statistics |
| feedback | Reinforcing (positive) |
| player interface | Observation only, Choice / cards |
| legibility | 5 |
| emergence potential | 3 |
| authoring cost | 2 |
| compute cost | 2 |
| tuning difficulty | 2 |
| ai leverage | 3 |
| maturity | Established |
| core count *(computed)* | 2 |
| earliest game *(computed)* | [The Incredible Machine](../game/the-incredible-machine.md) |
| earliest year *(computed)* | 1993 |
| prevalence *(computed)* | 24 |
| prevalence share *(computed)* | 0.138 |
| subgenre spread *(computed)* | 11 |
| technique count *(computed)* | 1 |
| technique exposure *(computed)* | 0.5 |

## Definition

A creation is serialized to a compact format, uploaded to a shared catalog with metadata, and ranked by downloads, ratings, or curation; other players browse and import it, or the game pulls catalog items into their worlds automatically. Spore uploaded every creature, vehicle, and building to the Sporepedia, ranked items by downloads, and redistributed them to populate other players' galaxies, with only a few kilobytes per item because the game rebuilds each creation procedurally from its template; it passed 100 million creations by May 2009, and players could filter or ban user content. Steam Workshop for Cities: Skylines, Planet Coaster blueprints, and Factorio blueprint strings are other forms. Inputs: serialized creations. Outputs: imported content and creator reputation.

## Player Experience

Creators build for an audience and check how their work spreads; browsers get far more variety than the developer shipped. Seeing another player's creature walk through your world, or importing a polished city block, makes the game feel populated.

## Design Levers

- serialization format and size, such as procedural templates versus full assets
- ranking and discovery signals (downloads, ratings, curation, subscriptions)
- automatic versus opt-in import into other players' worlds
- moderation tools and content filters
- attribution and feedback to creators

## Failure Modes

- Offensive or infringing uploads spread fast without moderation; Spore needed filters and in-game bans.
- Popularity rankings concentrate attention on a few creators and bury new work.
- Imported content that breaks balance or performance degrades the importer's game.

## Dynamics

- A small share of creators produce most of the popular content.
- Shared blueprints spread optimal designs quickly, which compresses the discovery phase for later players.
- Communities form around creator challenges and showcases.

## Open Questions

- Can models classify and moderate uploaded creations at scale with fewer false positives than keyword or report systems?
- How should catalogs recommend shared content without concentrating attention on a few top creators?

## Relations

**synergy**

- [Generative content on demand](../mechanic/generative-content.md): Shared first discoveries give generated content social value (Infinite Craft).
- [Modding API](../mechanic/modding-api.md): Mods need distribution; sharing platforms need mods.

## Backlinks (computed)

**affected by:** [Open real-time interactive video world models](../technique/open-interactive-video-models.md)

**involved in:** [Generative decoration catalogs](../opportunity/generative-decoration-catalogs.md), [Illustrated chronicles](../opportunity/illustrated-chronicles.md), [Mechanic modding by description](../opportunity/language-modding.md), [Open-ended evolution sandbox](../opportunity/open-ended-evolution-sandbox.md)

**used by:** [AI Dungeon](../game/ai-dungeon.md), [Arma 3](../game/arma-3.md), [BeamNG.drive](../game/beamng-drive.md), [Besiege](../game/besiege.md), [Command: Modern Operations](../game/command-modern-operations.md), [Creatures](../game/creatures.md), [Garry's Mod](../game/garrys-mod.md), [inZOI](../game/inzoi.md), [Opus Magnum](../game/opus-magnum.md), [Paralives](../game/paralives.md), [Planet Coaster](../game/planet-coaster.md), [Planet Zoo](../game/planet-zoo.md), [Poly Bridge](../game/poly-bridge.md), [Prison Architect](../game/prison-architect.md), [Second Life](../game/second-life.md), [SpaceChem](../game/spacechem.md), [Spore](../game/spore.md), [Suck Up!](../game/suck-up.md), [The Incredible Machine](../game/the-incredible-machine.md), [The Powder Toy](../game/the-powder-toy.md), [The Sims 4](../game/the-sims-4.md), [Tomodachi Life](../game/tomodachi-life.md), [Two Point Hospital](../game/two-point-hospital.md), [Universe Sandbox](../game/universe-sandbox.md)

## Sources

- [Spore (2008 video game)](../source/src-wikipedia-spore.md)

---
Provenance: created in run `2026-10-24-taxonomy-m7`.
