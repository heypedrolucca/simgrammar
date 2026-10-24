# iRacing

*Game* · `iracing` · status: **sourced**

A subscription online racing sim with laser-scanned cars and tracks in which drivers race scheduled official series and advance through license classes gated by a no-fault Safety Rating, while an Elo-style iRating sorts fields.

| field | value |
|---|---|
| year | 2008 |
| developer | iRacing Studios (iRacing.com Motorsport Simulations) |
| platforms | PC |
| subgenre | Vehicle sim |
| sim domain | Physical / mechanical, Sports |
| player role | Operator / pilot |
| agency model | Direct avatar |
| time model | Real-time |
| sim scale | Individual |
| fidelity | High-fidelity |
| perspective | First-person |
| win structure | Competitive victory |
| failure model | Soft / recoverable |
| narrative mode | None |
| multiplayer | Single-player, Competitive |
| modding | None |
| production tier | AA |
| agent count order | ~10 |
| emergence | 3 |
| influence | 3 |
| cluster *(computed)* | C03 |
| core count *(computed)* | 3 |
| mechanic count *(computed)* | 4 |

## Summary

A subscription online racing sim with laser-scanned cars and tracks in which drivers race scheduled official series and advance through license classes gated by a no-fault Safety Rating, while an Elo-style iRating sorts fields.

## Core Loop

join a scheduled official race -> qualify and race on laser-scanned tracks -> incidents and results update Safety Rating and iRating -> license promotion opens higher series -> buy cars and tracks for the next season

## Design Notes

iRacing grew from Papyrus's NASCAR Racing 2003 Season code with a new tire model and LIDAR-scanned cars and tracks. Its distinctive layer is the competitive structure: a no-fault Safety Rating from incident points per corner gates license classes (Rookie, D, C, B, A, with Pro reserved for esports), an Elo-style iRating sorts drivers into sessions and divisions, and 13-week seasons rotate tracks weekly. Skill rating and matchmaking have no mechanic in the taxonomy (proposed as skill-rating-matchmaking).

## Relations

**uses**

- [Vehicle dynamics](../mechanic/vehicle-dynamics.md) (core): A new tire model replaced the one in the NASCAR Racing 2003 Season code iRacing was built from, and cars and tracks are LIDAR-scanned.
- [Embodied skill control](../mechanic/embodied-skill-control.md) (core): Races are against human drivers on the publisher's servers, so results depend on the driver's braking, throttle, and line precision.
- [Career ladder](../mechanic/career-ladder.md) (core): Licenses progress Rookie, D, C, B, A, with Pro for esports qualifiers; promotion depends on a per-discipline Safety Rating computed from incident points and corners per incident.
- [Wear and breakdown](../mechanic/wear-breakdown.md) (supporting): Cars take damage and tires wear over a race, which pit stops address.

## Backlinks (computed)

**precedent for:** [Simulator instructor coaching](../opportunity/sim-instructor-coach.md)

## Sources

- [iRacing](../source/src-wikipedia-iracing.md)

---
Provenance: created in run `2026-10-24-catalog-gf`.
