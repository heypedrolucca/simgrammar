# Seasonal world reset

*Mechanic* · `seasonal-world-reset` · status: **sourced**

A shared world runs for a bounded season and is then wiped and restarted, often with rule changes carried into the next season.

| field | value |
|---|---|
| aliases | wipes, [Seasons](../mechanic/seasons.md), Tellings, server cycles |
| family | Multiplayer & persistence |
| substrate | Rule system |
| math basis | Mechanism design / auctions, Game theory |
| feedback | Balancing (negative) |
| player interface | Observation only |
| legibility | 5 |
| emergence potential | 2 |
| authoring cost | 2 |
| compute cost | 1 |
| tuning difficulty | 2 |
| ai leverage | 2 |
| maturity | Established |
| requires | [Persistent shared world](../mechanic/persistent-world.md) |
| core count *(computed)* | 1 |
| earliest game *(computed)* | [A Tale in the Desert](../game/a-tale-in-the-desert.md) |
| earliest year *(computed)* | 2003 |
| prevalence *(computed)* | 2 |
| prevalence share *(computed)* | 0.011 |
| subgenre spread *(computed)* | 1 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

Owns the season's state: start date, an end condition (fixed duration, a scheduled wipe, or a world-level goal or catastrophe), and the carryover rules that say what survives into the next season (nothing, account-level unlocks, records, or changed rules). When the end condition fires, world state is archived or deleted, a new world is generated or loaded, and carryover is applied. A Tale in the Desert runs in Tellings that average about 18 months and end in a wipe, with rule changes for the next Telling shaped by what players achieved. Eco gives each world a meteor due in thirty days, so a server's run is bounded by stopping it or suffering the impact, and servers are commonly restarted as new worlds. Unlike persistent-world, which assumes continuity, this mechanic owns the bounded lifetime of a shared world and the transition between lifetimes.

## Player Experience

Fresh starts on a schedule. Everyone begins equal at the start of a season, so new players can matter, and the end date gives the season an arc of land rush, consolidation, and final push. Players plan around the wipe, deciding what is worth building when it will not last.

## Design Levers

- season length or end condition
- carryover: nothing, cosmetics, account unlocks, records, or rule changes
- rule variation between seasons, including player-proposed changes
- whether players can migrate between seasonal and permanent worlds
- announcement lead time before a wipe

## Failure Modes

- Wipes erase work players were attached to, and some quit rather than start over.
- Short seasons reward a known opening rush, so seasons play out the same way.
- Carryover that is too generous rebuilds the early-arrival advantage the reset was meant to remove.

## Dynamics

- Activity surges at season start and fades toward the end, giving the population a cycle.
- Players refine openings across seasons, and community guides target the first days of a wipe.
- Rule changes between seasons let designers and players treat each season as an experiment.

## Open Questions

- Could AI summaries and chronicles of past seasons preserve their history so wipes feel less like loss?
- Which carryover rules keep returning players motivated without restoring early-arrival dominance?

## Relations

**requires**

- [Persistent shared world](../mechanic/persistent-world.md)

## Backlinks (computed)

**used by:** [A Tale in the Desert](../game/a-tale-in-the-desert.md), [Eco](../game/eco.md)

## Sources

- [A Tale in the Desert](../source/src-wikipedia-a-tale-in-the-desert.md)
- [Eco on Steam](../source/src-steam-2018-eco.md)

---
Provenance: created in run `2026-10-24-taxonomy-triage-b`.
