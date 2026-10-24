# PC Building Simulator

*Game* · `pc-building-simulator` · status: **sourced**

A workshop sim in which the player takes email jobs to build, upgrade, repair, and overclock PCs from licensed parts and verifies the results with benchmark software.

| field | value |
|---|---|
| aliases | PCBS |
| year | 2018 |
| year full release | 2019 |
| developer | Claudiu Kiss and The Irregular Corporation |
| platforms | PC, Console, Handheld |
| subgenre | Job sim |
| sim domain | Occupational, Physical / mechanical |
| player role | Worker |
| agency model | Design then test |
| time model | Real-time |
| sim scale | Individual |
| fidelity | Stylized |
| perspective | First-person |
| win structure | Open sandbox |
| failure model | Soft / recoverable |
| narrative mode | None |
| multiplayer | Single-player |
| modding | None |
| production tier | Indie |
| agent count order | None |
| emergence | 1 |
| influence | 1 |
| cluster *(computed)* | C15 |
| core count *(computed)* | 3 |
| mechanic count *(computed)* | 6 |

## Summary

A workshop sim in which the player takes email jobs to build, upgrade, repair, and overclock PCs from licensed parts and verifies the results with benchmark software.

## Core Loop

accept an email job -> order parts with a shipping tier -> open the case and diagnose or assemble -> install software, remove viruses, or overclock -> benchmark -> get paid -> pay rent and electricity -> unlock better parts

## Design Notes

Parts are licensed real components with compatibility rules, and a machine's performance is measured with the real 3DMark benchmark, so a build's quality is an output of its parts rather than a designer-set score. Assembly has physical consequences: a CPU cooler mounted without thermal paste lets the processor overheat and fail. The career wraps this in a small business with monthly rent and electricity, accept-or-reject email jobs, and timed jobs that become more common later.

## Relations

**uses**

- [Diagnose and repair](../mechanic/diagnose-repair.md) (core): Email jobs ask for virus removal, upgrades, fixes, or overclocking on customer PCs; the player opens the case, identifies the faulty or missing part, and swaps it.
- [Modular assembly](../mechanic/modular-assembly.md) (core): PCs are assembled from licensed cases, motherboards, CPUs, coolers, GPUs, memory, and storage; part choice and installation details such as thermal paste decide whether and how well the machine runs.
- [Contracts and orders](../mechanic/contracts-orders.md) (core): Customer requests, discount alerts, spam, and scams arrive in an inbox; accepted orders left unfulfilled are rejected, and timed jobs grow more common as the career advances.
- [Design performance rating](../mechanic/design-performance-rating.md) (supporting): 3DMark benchmarking scores built or repaired machines.
- [Milestone unlocks](../mechanic/milestone-unlocks.md) (supporting): Leveling up from job experience unlocks more advanced parts.
- [Treasury and budget](../mechanic/budget-treasury.md) (supporting): Monthly rent and electricity bills must be paid or the player incurs debt.

## Sources

- [PC Building Simulator](../source/src-wikipedia-pc-building-simulator.md)

---
Provenance: created in run `2026-10-24-catalog-gf`.
