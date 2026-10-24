# Bitburner

*Game* · `bitburner` · status: **sourced**

A free, open-source incremental hacking game in which the player writes JavaScript scripts that hack, grow, and weaken simulated servers for money, then spends it with faction reputation on augmentations that reset progress in exchange for permanent multipliers.

| field | value |
|---|---|
| year | 2017 |
| year full release | 2021 |
| developer | danielyxie and Bitburner contributors |
| platforms | Web, PC |
| subgenre | Programming sim |
| sim domain | Computational / abstract, Economic |
| player role | Programmer |
| agency model | Programmatic |
| time model | Real-world clock |
| sim scale | Individual |
| fidelity | Abstract |
| perspective | Text / UI |
| win structure | Campaign |
| failure model | None |
| narrative mode | Authored |
| multiplayer | Single-player |
| modding | Scripting |
| production tier | Hobbyist / free |
| agent count order | None |
| emergence | 2 |
| influence | 1 |
| boundary case | True |
| influenced by |  |
| cluster *(computed)* | C06 |
| core count *(computed)* | 3 |
| mechanic count *(computed)* | 8 |

## Summary

A free, open-source incremental hacking game in which the player writes JavaScript scripts that hack, grow, and weaken simulated servers for money, then spends it with faction reputation on augmentations that reset progress in exchange for permanent multipliers.

## Core Loop

write a script -> gain root on servers -> run hack, grow, and weaken threads -> earn money and hacking experience -> buy RAM and programs -> gain faction reputation -> buy augmentations and install them, resetting progress -> destroy a BitNode for a Source-File and start the next

## Design Notes

Bitburner is an incremental game whose economy is a small numerical model the player automates in code. Each server holds a money stock and a security level: hack() steals a percentage of the money and raises security, grow() multiplies money back and also raises security, and weaken() lowers security toward a floor of max(1, round(starting security / 3)), with hack chance and timing set by security and the player's hacking level. Writing schedulers that balance these three calls across many servers and threads is the main skill. Progress is layered by resets: augmentations bought with money and faction reputation (each purchase doubling later prices) take effect only when installed, which wipes most progress, and destroying a BitNode by hacking w0r1d_d43m0n at hacking level 3000 resets further but grants a permanent Source-File. This prestige-reset structure has no taxonomy entry, so this run proposed one. Later BitNodes add systems such as Bladeburner and sleeves.

## Sources

- src-steam-2026-bitburner
- src-danielyxie-2026-bitburner-repository
- src-bitburner-2026-changelog-v0
- src-bitburner-2026-changelog-v1
- src-oddiz-2026-bitburner-docs
- src-mobygames-2026-bitburner

## Relations

**uses**

- [Player programming](../mechanic/player-programming.md) (core): Netscript scripts in JavaScript run on servers whose RAM caps how many threads can run; the TIX API automates stock trading, and a beginner path teaches programming from scratch.
- [Resource extraction](../mechanic/resource-extraction.md) (core): hack() takes a share of a server's finite money that rises with hacking level and falls with security; grow() restores money and weaken() lowers security toward its floor, and both hack and grow raise security, so sustained yield needs a balanced hack-grow-weaken schedule.
- [Reputation](../mechanic/reputation.md) (core): Working for factions builds reputation that gates which augmentations can be bought; Daedalus reputation gates The Red Pill needed to end a BitNode.
- [Agent skills](../mechanic/agent-skills.md) (supporting): Hacking, combat, and charisma stats rise with use; hacking level raises success chance and money stolen, shortens hack time, and gates which servers can be hacked.
- [Supply-demand pricing](../mechanic/supply-demand-pricing.md) (supporting): Stock prices move about every 6 seconds by a forecast probability that large trades shift; hacking or growing a company's server can lower or raise its stock's hidden forecast.
- [Contracts and orders](../mechanic/contracts-orders.md) (supporting): Coding contracts found on servers pose programming problems that earn rewards when solved.
- [Real-time clock](../mechanic/real-time-clock.md) (supporting): Time spent offline accumulates and later speeds stock-market updates from about every 6 seconds to about every 4.
- [Execution budget](../mechanic/execution-budget.md) (supporting): Each script has a RAM cost, and a server's RAM caps how many script threads can run on it, so buying RAM and writing lean scripts both raise income.

## Backlinks (computed)

**precedent for:** [Specification programming games](../opportunity/specification-programming-games.md)

## Claims

- The earliest dated changelog entry is v0.26.4 on 2017-08-01 and earlier versions are undated, so the 2017 first public web release is inferred; version 1.0.0 is dated 2021-11-10 and the Steam release was 2021-12-10. *(confidence: medium)* [[6](../source/src-bitburner-2026-changelog-v0.md), [7](../source/src-bitburner-2026-changelog-v1.md), [8](../source/src-steam-2026-bitburner.md)]
- Bitburner was started by danielyxie and is now developed as open source by hundreds of contributors, with the Steam release credited to Fulcrum Games, hydroflame, and GitHub contributors. *(confidence: high)* [[9](../source/src-danielyxie-2026-bitburner-repository.md), [8](../source/src-steam-2026-bitburner.md)]
- Its listed inspirations are Else Heart.break(), Hacknet, Uplink, and Deus Ex, none of which are in this dataset. *(confidence: medium)* [[10](../source/src-mobygames-2026-bitburner.md)]

## Sources

- [Bitburner](../source/src-steam-2026-bitburner.md)
- [Bitburner (original repository)](../source/src-danielyxie-2026-bitburner-repository.md)
- [Bitburner changelog (v0)](../source/src-bitburner-2026-changelog-v0.md)
- [Bitburner changelog (v1)](../source/src-bitburner-2026-changelog-v1.md)
- [Bitburner documentation (community fork)](../source/src-oddiz-2026-bitburner-docs.md)
- [Bitburner](../source/src-mobygames-2026-bitburner.md)

---
Provenance: created in run `2026-10-24-catalog-gh`.
