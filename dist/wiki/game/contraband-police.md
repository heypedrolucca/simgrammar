# Contraband Police

*Game* · `contraband-police` · status: **sourced**

A first-person border-post sim set in 1981 in which the player checks drivers' documents, searches vehicles for hidden contraband, chases smugglers, and upgrades the post against gang attacks.

| field | value |
|---|---|
| year | 2023 |
| developer | Crazy Rocks Studios |
| platforms | PC, Console |
| subgenre | Job sim |
| sim domain | Occupational, Political / governance |
| player role | Worker |
| agency model | Direct avatar |
| time model | Real-time |
| sim scale | Individual |
| fidelity | Stylized |
| perspective | First-person |
| win structure | Campaign |
| failure model | Soft / recoverable |
| narrative mode | Hybrid |
| multiplayer | Single-player |
| modding | None |
| production tier | Indie |
| agent count order | ~10 |
| emergence | 2 |
| influence | 1 |
| influenced by | [Papers, Please](../game/papers-please.md) |
| cluster *(computed)* | C14 |
| core count *(computed)* | 2 |
| mechanic count *(computed)* | 6 |

## Summary

A first-person border-post sim set in 1981 in which the player checks drivers' documents, searches vehicles for hidden contraband, chases smugglers, and upgrades the post against gang attacks.

## Core Loop

check documents -> search the vehicle with UV light and tools -> extract contraband or approve -> arrest or chase fleeing smugglers -> earn cash -> upgrade the post, cars, and defenses -> story missions and raids

## Design Notes

It moves the Papers, Please inspection loop into a 3D first-person space: document discrepancies are found on paper, but contraband is found physically by examining the vehicle with a UV flashlight and extracting it with tools. The number of documents per entrant grows over time, raising the error rate at constant attention. Inspection income funds post upgrades whose maintenance costs rise, while authored special assignments, chases, and gang raids interrupt the shift loop.

## Relations

**influenced by**

- [Papers, Please](../game/papers-please.md)

**uses**

- [Rule-checking inspection](../mechanic/rule-checking-inspection.md) (core): Drivers present documents whose number grows over the campaign; small discrepancies require refusal, and suspicious vehicles are searched with a UV flashlight before tools extract hidden goods.
- [Direct avatar control](../mechanic/direct-avatar.md) (core): The player walks the post in first person, opens and searches vehicles, drives upgradable police cars in pursuits, and uses firearms in shootouts.
- [Treasury and budget](../mechanic/budget-treasury.md) (supporting): Cash from inspections, foiled smuggling, and interventions pays for upgrades while post maintenance costs rise over time.
- [Raid defense](../mechanic/raid-defense.md) (supporting): Gang attacks on the post are countered with purchased defense upgrades.
- [Triggered event chains](../mechanic/triggered-event-chains.md) (supporting): Special assignments and story decisions shape the fate of Acaristan and lead to multiple endings.
- [Procedural characters](../mechanic/procedural-characters.md) (supporting)

## Backlinks (computed)

**precedent for:** [Generated inspection shifts](../opportunity/generated-inspection-shifts.md)

## Sources

- [Contraband Police](../source/src-wikipedia-contraband-police.md)
- [Contraband Police on Steam](../source/src-steam-2026-contraband-police.md)
- [With 100K copies sold in less than 2 weeks, this Steam game could be the next Papers, Please](../source/src-twinfinite-2023-contraband-police.md)

---
Provenance: created in run `2026-10-24-catalog-gf`.
