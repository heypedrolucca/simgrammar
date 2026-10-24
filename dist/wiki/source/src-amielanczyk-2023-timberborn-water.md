# Deep Dive: Designing the dynamic irrigation and water systems in Timberborn

*Source* · `src-amielanczyk-2023-timberborn-water` · status: **n/a**

| field | value |
|---|---|
| kind | Postmortem / interview |
| authors | Michal Amielanczyk, Kamil Dawidow |
| venue | Game Developer |
| date | 2023-02-28 |
| url | https://www.gamedeveloper.com/design/deep-dive-timberborn-s-water-mechanics |
| accessed | 2026-10-24 |

## Notes

Single-layer 2D water model adapted from erosion simulation; tiles linked to four neighbors by virtual pipes; ticks every couple of hundred ms; water levels equalize; evaporation; recurring droughts grow harsher and ramp source strength down early; hard-coded dam values avoided because they caused oscillations; moisture falls off per tile and sharply uphill.

## Backlinks (computed)

**cited by:** [Hydrology](../mechanic/hydrology.md), [Timberborn](../game/timberborn.md)

## Citation

Michal Amielanczyk, Kamil Dawidow (2023-02-28). *Deep Dive: Designing the dynamic irrigation and water systems in Timberborn*. Game Developer https://www.gamedeveloper.com/design/deep-dive-timberborn-s-water-mechanics

---
Provenance: created in run `2026-10-24-taxonomy-m5`.
