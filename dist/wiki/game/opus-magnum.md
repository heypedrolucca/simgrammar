# Opus Magnum

*Game* · `opus-magnum` · status: **sourced**

A programming puzzle game in which the player builds alchemical machines from arms, tracks, and glyphs on a hex grid, programs them on an instruction timeline, and compares each looping solution's cost, cycles, and area against other players' histograms.

| field | value |
|---|---|
| year | 2017 |
| developer | Zachtronics |
| platforms | PC, Console, Handheld |
| subgenre | Programming sim |
| subgenre secondary | Construction / engineering |
| sim domain | Computational / abstract |
| player role | Programmer |
| agency model | Programmatic, Design then test |
| time model | Run on demand |
| sim scale | Micro |
| fidelity | Abstract |
| perspective | Top-down / side 2D |
| win structure | Campaign |
| failure model | None |
| narrative mode | Authored |
| multiplayer | Single-player, Async / shared content |
| modding | Content |
| production tier | Indie |
| agent count order | None |
| emergence | 2 |
| influence | 2 |
| boundary case | True |
| influenced by | [SpaceChem](../game/spacechem.md) |
| cluster *(computed)* | C02 |
| core count *(computed)* | 4 |
| mechanic count *(computed)* | 6 |

## Summary

A programming puzzle game in which the player builds alchemical machines from arms, tracks, and glyphs on a hex grid, programs them on an instruction timeline, and compares each looping solution's cost, cycles, and area against other players' histograms.

## Core Loop

read the reagents and product -> place arms, tracks, and glyphs on the hex grid -> write instructions on the timeline -> run until the required products are made -> compare cost, cycles, and area histograms -> export a looping GIF or optimize

## Design Notes

Opus Magnum refines Zach Barth's 2008 Flash game The Codex of Alchemical Engineering into Zachtronics' most permissive puzzle design: there is no part limit, any machine that delivers the products counts, and the difficulty is choosing among three competing metrics. Arms grab, rotate, pivot, extend, and move on tracks under a per-arm instruction tape, and glyphs bond, unbond, calcify, and project metals one step toward gold. Solutions are ranked on cost in gold, cycles, and area, with no in-game reward for optimizing, so motivation comes from friends' scores and the histograms. Barth's experience with solution recording in Infinifactory led to built-in export of seamlessly looping GIFs, which made solutions shareable outside the game; a puzzle editor feeds Steam Workshop.

## Relations

**influenced by**

- [SpaceChem](../game/spacechem.md)

**uses**

- [Player programming](../mechanic/player-programming.md) (core): Each arm has a row on a shared instruction timeline of grab, drop, rotate, pivot, extend, retract, and track moves; the machine loops the program until the required number of products is output.
- [Design performance rating](../mechanic/design-performance-rating.md) (core): Solutions are scored on cost in gold, cycles to complete, and area in hex tiles, with the community adding an unofficial sum metric.
- [Comparative histograms](../mechanic/comparative-histograms.md) (core): Cost, cycles, and area are shown on histograms of all players' scores and against friends' scores; Zachtronics deliberately attaches no rewards to optimization.
- [Modular assembly](../mechanic/modular-assembly.md) (core): A machine is assembled from arms, extendable arms, tracks, and glyphs of bonding, unbonding, calcification, and projection, plus devices such as Van Berlo's wheel, with no limit on parts beyond their cost.
- [Scenario objectives](../mechanic/scenario-objectives.md) (supporting): Each puzzle fixes the input reagents and the required product molecule; chapters must be completed to advance.
- [Content sharing](../mechanic/content-sharing.md) (supporting): A puzzle editor publishes solvable user puzzles to Steam Workshop, curated puzzles appear in the Journal of Alchemical Engineering, and solutions export as looping GIFs.

## Backlinks (computed)

**precedent for:** [Quality-diversity scenario libraries](../opportunity/qd-scenario-libraries.md), [Specification programming games](../opportunity/specification-programming-games.md)

## Claims

- Opus Magnum is a refined version of Zach Barth's 2008 Flash game The Codex of Alchemical Engineering, which is not in this dataset; the influenced_by edge to SpaceChem records Barth's shared instruction-grid and histogram design rather than a stated influence in the cited encyclopedia. *(confidence: medium)* [[28](../source/src-wikipedia-opus-magnum.md), [29](../source/src-wikipedia-spacechem.md)]
- A Nintendo Switch version, Opus Magnum The Complete Edition, released on 2026-03-17. *(confidence: medium)* [[28](../source/src-wikipedia-opus-magnum.md)]

## Sources

- [Opus Magnum](../source/src-wikipedia-opus-magnum.md)
- [Opus Magnum](../source/src-steam-2026-opus-magnum.md)
- [Road to the IGF: Zachtronics' Opus Magnum](../source/src-couture-2019-road-to-igf-opus-magnum.md)

---
Provenance: created in run `2026-10-24-catalog-gh`.
