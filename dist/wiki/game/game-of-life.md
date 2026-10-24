# Conway's Game of Life

*Game* · `game-of-life` · status: **sourced**

A zero-player cellular automaton on an infinite square grid in which each cell lives or dies by the B3/S23 neighbor-count rule, producing gliders, oscillators, and universal computation from a seeded pattern.

| field | value |
|---|---|
| aliases | Life, Game of Life |
| year | 1970 |
| developer | John Horton Conway |
| platforms | Mainframe / early micro, PC, Web, Mobile |
| subgenre | Artificial life |
| sim domain | Computational / abstract |
| player role | Observer / gardener |
| agency model | Design then test |
| time model | Run on demand |
| sim scale | Micro |
| fidelity | Abstract |
| perspective | Top-down / side 2D |
| win structure | Open sandbox |
| failure model | None |
| narrative mode | None |
| multiplayer | Single-player |
| modding | Scripting |
| production tier | Academic / research |
| agent count order | None |
| emergence | 5 |
| influence | 5 |
| cluster *(computed)* | C03 |
| core count *(computed)* | 2 |
| mechanic count *(computed)* | 4 |

## Summary

A zero-player cellular automaton on an infinite square grid in which each cell lives or dies by the B3/S23 neighbor-count rule, producing gliders, oscillators, and universal computation from a seeded pattern.

## Core Loop

place live cells on the grid -> apply birth on 3 and survival on 2 or 3 neighbors to every cell at once -> pattern stabilizes, oscillates, dies, or emits gliders -> observe -> edit the seed and rerun

## Design Notes

Conway's rule is the minimal case of emergence from local update: each cell's next state depends only on how many of its eight neighbors are alive, all cells update simultaneously, and the only input is the initial pattern. The rule is Turing complete, so whether an arbitrary pattern stops changing is undecidable, and decades of discovery (Gosper's period-30 glider gun of November 1970, the R-pentomino's 1,103-generation run) came from players searching seeds. Simulators such as Golly add Hashlife for large time jumps and scripting for rule variants. A general cellular-automaton rule is not yet a mechanic in the taxonomy (proposal cellular-automaton-rule); adjacency-scoring is the nearest existing id.

## Relations

**uses**

- [Adjacency scoring](../mechanic/adjacency-scoring.md) (core): A dead cell with exactly 3 live neighbors is born, a live cell with 2 or 3 survives, and all others die; the neighbor count is the whole update rule.
- [Building placement](../mechanic/free-placement.md) (core): The player's only act is toggling cells on the grid to set the seed before running generations.
- [Blueprints](../mechanic/blueprints.md) (supporting): Implementations store patterns as files and libraries that can be stamped into a grid and shared.
- [Pause and speed control](../mechanic/variable-speed.md) (supporting): Simulators step one generation at a time or run fast, and Hashlife in Golly jumps far ahead in time.

## Backlinks (computed)

**precedent for:** [Language-agent society terrarium](../opportunity/llm-society-terrarium.md), [Open-ended evolution sandbox](../opportunity/open-ended-evolution-sandbox.md)

## Sources

- [Conway's Game of Life](../source/src-wikipedia-conways-game-of-life.md)

---
Provenance: created in run `2026-10-24-catalog-gd`.
