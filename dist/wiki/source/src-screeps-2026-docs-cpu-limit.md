# How does CPU limit work

*Source* · `src-screeps-2026-docs-cpu-limit` · status: **n/a**

| field | value |
|---|---|
| kind | Documentation |
| venue | Screeps documentation |
| date | 2026 |
| url | https://docs.screeps.com/cpu-limit.html |
| accessed | 2026-10-24 |

## Notes

Per-tick CPU limit (20 without CPU Unlock, otherwise tied to Global Control Level); unused CPU accumulates in a bucket of up to 10,000; a tick may use up to 500 CPU from the bucket; scripts are terminated at the limit.

## Backlinks (computed)

**cited by:** [Execution budget](../mechanic/execution-budget.md), [Player programming](../mechanic/player-programming.md), [Screeps](../game/screeps.md)

## Citation

 (2026). *How does CPU limit work*. Screeps documentation https://docs.screeps.com/cpu-limit.html

---
Provenance: created in run `2026-10-24-taxonomy-m6`.
