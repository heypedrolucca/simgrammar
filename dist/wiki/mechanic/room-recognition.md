# Room recognition

*Mechanic* · `room-recognition` · status: **sourced**

Enclosed spaces are detected by flood fill and classified into room types by their size and contents, and the type grants effects.

| field | value |
|---|---|
| aliases | room detection, room roles, room types |
| family | Space & construction |
| substrate | Cellular grid, Rule system |
| math basis | Graph search, Combinatorics |
| feedback | None |
| player interface | Placement, Observation only |
| legibility | 4 |
| emergence potential | 3 |
| authoring cost | 2 |
| compute cost | 2 |
| tuning difficulty | 2 |
| ai leverage | 3 |
| maturity | Established |
| requires | [Building placement](../mechanic/free-placement.md) |
| core count *(computed)* | 0 |
| earliest game *(computed)* | [Dwarf Fortress](../game/dwarf-fortress.md) |
| earliest year *(computed)* | 2006 |
| prevalence *(computed)* | 6 |
| prevalence share *(computed)* | 0.034 |
| subgenre spread *(computed)* | 3 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

When walls, doors, or floors change, a flood fill over passable tiles bounded by impassable structures finds enclosed regions. Each region is scored against role templates by its furniture and size; the best match becomes the room type, and room stats feed effects. In RimWorld rooms are bounded by walls, doors, and natural rock; roles are scored from contents (12 per table for a dining room, 27 per workbench for a workshop, and a room with more than one unassigned human bed scores as barracks rather than a bedroom); rooms are capped at 36 map regions or 5,184 tiles; and wealth, beauty, space, and cleanliness combine into impressiveness that sets mood thoughts. Oxygen Not Included recognizes rooms such as barracks and mess halls by enclosure, size limits, and required buildings. Theme Hospital and Prison Architect instead have the player designate the room type and validate its requirements.

## Player Experience

Walls acquire meaning. Players build a room, watch it get its label, and upgrade it to earn bonuses. A broken wall or an extra bed silently downgrades the room, which teaches players to read enclosure carefully.

## Design Levers

- enclosure rule: what counts as a wall, whether doors and vents close a room, diagonal gaps
- minimum and maximum room size
- role templates, their scores, and tie-breaking
- whether one room can hold several roles
- effects granted per role and stat tier

## Failure Modes

- Invisible enclosure breaks, such as a destroyed wall or an opened gap, silently change room roles and their effects.
- Role conflicts surprise players; in RimWorld a second unassigned bed turns a bedroom into barracks.
- Tiny or multipurpose rooms that satisfy templates cheaply become the optimal design.
- Very large open spaces exceed size limits and stop counting as rooms.

## Dynamics

- Raid or disaster damage breaks enclosures and triggers mood or productivity drops across the base.
- Rooms double as thermal and atmospheric zones, coupling layout to temperature and gas systems.
- Room upgrades become a progression track toward higher stat tiers.

## Open Questions

- Can a vision or language model classify rooms by what they are used for rather than by fixed furniture templates?
- How should recognition explain to the player why a space failed to qualify?

## Relations

**requires**

- [Building placement](../mechanic/free-placement.md)

## Backlinks (computed)

**involved in:** [Generative decoration catalogs](../opportunity/generative-decoration-catalogs.md)

**used by:** [Dwarf Fortress](../game/dwarf-fortress.md), [Going Medieval](../game/going-medieval.md), [Oxygen Not Included](../game/oxygen-not-included.md), [Project Hospital](../game/project-hospital.md), [RimWorld](../game/rimworld.md), [Townscaper](../game/townscaper.md)

## Sources

- [Room](../source/src-rimworldwiki-2026-room.md)

---
Provenance: created in run `2026-10-24-taxonomy-m4`.
