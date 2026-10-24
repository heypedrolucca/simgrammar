# OpenRCT2 source: Ride.cpp (ride reliability, inspection, and breakdowns)

*Source* · `src-openrct2-2026-ride-breakdowns` · status: **n/a**

| field | value |
|---|---|
| kind | Code repository / dataset |
| authors | OpenRCT2 contributors |
| venue | GitHub (OpenRCT2/OpenRCT2) |
| date | 2026 |
| url | https://github.com/OpenRCT2/OpenRCT2/blob/develop/src/openrct2/ride/Ride.cpp |
| accessed | 2026-10-24 |

## Notes

GPL-3.0 reimplementation of RollerCoaster Tycoon 2. Reliability starts at 100% and drops every 256 ticks by the ride's unreliability factor plus an age penalty (one-eighth of it in year 1 up to double after 8 years); breakdown chance rises with reliability lost; weighted breakdown types, brake failure more likely in rain; inspection interval set by the player; repair restores reliability in proportion to its deficit.

## Backlinks (computed)

**cited by:** [Wear and breakdown](../mechanic/wear-breakdown.md)

## Citation

OpenRCT2 contributors (2026). *OpenRCT2 source: Ride.cpp (ride reliability, inspection, and breakdowns)*. GitHub (OpenRCT2/OpenRCT2) https://github.com/OpenRCT2/OpenRCT2/blob/develop/src/openrct2/ride/Ride.cpp

---
Provenance: created in run `2026-10-24-taxonomy-m7`.
