# PowerWash Simulator

*Game* · `powerwash-simulator` · status: **sourced**

A first-person cleaning sim in which the player power-washes vehicles and buildings, choosing nozzles and soaps to strip dirt layers until every part reports clean.

| field | value |
|---|---|
| year | 2021 |
| year full release | 2022 |
| developer | FuturLab |
| platforms | PC, Console, Handheld, VR, Mobile |
| subgenre | Job sim |
| sim domain | Occupational |
| player role | Worker |
| agency model | Direct avatar |
| time model | Real-time |
| sim scale | Individual |
| fidelity | Stylized |
| perspective | First-person |
| win structure | Completion |
| failure model | None |
| narrative mode | Authored |
| multiplayer | Single-player, Co-op |
| modding | None |
| production tier | Indie |
| agent count order | None |
| emergence | 1 |
| influence | 2 |
| core loop | accept a job -> pick nozzle and soap -> wash surfaces -> per-part progress reaches 100 percent -> job pays -> buy washer upgrades -> next job |
| cluster *(computed)* | C02 |
| core count *(computed)* | 1 |
| mechanic count *(computed)* | 4 |

## Summary

A first-person cleaning sim in which the player power-washes vehicles and buildings, choosing nozzles and soaps to strip dirt layers until every part reports clean.

## Design Notes

The simulation is a per-surface dirt state: each surface carries layers (dirt, grime, lichen, moss, rust) that the spray removes according to nozzle, soap, and range, and every object reports its percentage done. Four nozzles trade power against spray width, so play is matching the tool to the layer and distance. Progress bars per object and a highlight for remaining dirt make completion fully legible, and the career's story arrives as client text messages rather than through the simulation.

## Relations

**uses**

- [Surface work tools](../mechanic/surface-work-tools.md) (core): Four nozzles with different power and spray width and surface-specific soaps remove dirt, grime, lichen, moss, and rust; progress bars track each object and the level, and a button highlights remaining dirt.
- [Contracts and orders](../mechanic/contracts-orders.md) (supporting): Career mode in the town of Muckingham offers 38 main jobs plus bonus jobs whose pay buys upgrades and cosmetics.
- [Direct avatar control](../mechanic/direct-avatar.md) (supporting): Ladders and scaffolding reach higher surfaces.
- [Scenario objectives](../mechanic/scenario-objectives.md) (supporting): Challenge mode limits water or time and ranks the result.

## Sources

- [PowerWash Simulator](../source/src-wikipedia-powerwash-simulator.md)

---
Provenance: created in run `2026-10-24-catalog-gf`.
