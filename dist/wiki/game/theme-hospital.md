# Theme Hospital

*Game* · `theme-hospital` · status: **sourced**

A hospital management game where the player builds rooms, hires and trains staff, and routes patients with comic diseases through diagnosis and treatment to meet level goals.

| field | value |
|---|---|
| year | 1997 |
| developer | Bullfrog Productions |
| platforms | PC, Console |
| subgenre | Management / tycoon |
| subgenre secondary | Medical sim |
| sim domain | Medical, Economic |
| player role | Manager / owner |
| agency model | Zoning / placement, Policy / parameter, Direct unit control |
| time model | Real-time with pause |
| sim scale | Facility |
| fidelity | Stylized |
| perspective | Isometric |
| win structure | Scenario goals |
| failure model | Hard restart |
| narrative mode | None |
| multiplayer | Single-player, Competitive |
| modding | Content |
| production tier | AA |
| agent count order | ~100 |
| emergence | 3 |
| influence | 3 |
| influenced by | [Theme Park](../game/theme-park.md) |
| cluster *(computed)* | C01 |
| core count *(computed)* | 4 |
| mechanic count *(computed)* | 16 |

## Summary

A hospital management game where the player builds rooms, hires and trains staff, and routes patients with comic diseases through diagnosis and treatment to meet level goals.

## Core Loop

build rooms from blueprints -> hire and train staff -> patients queue for GP diagnosis and referrals -> treatment cures or kills -> fees and reputation -> research new rooms and meet level goals

## Design Notes

Theme Hospital turns medicine into routing. The GP and specialist diagnosis rooms raise a patient's diagnosis certainty, and the player sets the threshold at which treatment starts (it can be set above 100%), trading throughput against deaths from wrong cures. Rooms are fixed blueprints that need set furniture and, for some, specialist staff, so the staff roster and the floor plan gate each other. Machines that explode without a handyman, epidemics that can be covered up before the health inspector arrives, and timed emergencies add pressure on top of the queues. Much of the code came from Theme Park; CorsixTH is an open-source reimplementation with a level editor.

## Relations

**influenced by**

- [Theme Park](../game/theme-park.md)

**uses**

- [Diagnosis and treatment](../mechanic/diagnosis-treatment.md) (core): A GP diagnoses or refers patients to specialist diagnosis rooms; treatment starts once certainty passes a player-set threshold, and diseases are fictional, such as Bloaty Head.
- [Building placement](../mechanic/free-placement.md) (core): Rooms are placed as blueprints with doors and windows, then furnished with required items; many rooms must be researched first.
- [Staff hiring and rosters](../mechanic/staff-hiring.md) (core): Doctors, nurses, handymen, and receptionists are hired with performance stats; some rooms need doctors with specialist skills.
- [Service queues](../mechanic/service-queues.md) (core): Patients queue outside each room; the player can rearrange queues, and long waits push patients to leave.
- [Agent skills](../mechanic/agent-skills.md) (supporting): Doctors can be trained to gain skills and specialisms.
- [Wear and breakdown](../mechanic/wear-breakdown.md) (supporting): Machines such as the Inflator need handyman servicing or they explode.
- [Contagion](../mechanic/contagion.md) (supporting): Epidemics break out and can be covered up before a health inspector visits; failure brings fines and lost reputation.
- [Tech tree](../mechanic/tech-tree.md) (supporting): Research unlocks rooms, drugs, and machine improvements.
- [Reputation](../mechanic/reputation.md) (supporting): Cures and deaths move a reputation that affects patient intake and level goals.
- [Needs decay](../mechanic/needs-decay.md) (supporting): Staff tire and need breaks under player-set break rules; patients need drinks and toilets.
- [Contracts and orders](../mechanic/contracts-orders.md) (supporting): Emergencies require curing a group of patients within a time limit for a bonus.
- [Scenario objectives](../mechanic/scenario-objectives.md) (supporting): Each level sets goals for money, reputation, cures, and hospital value; negative funds or too many deaths lose the level.
- [Advisors](../mechanic/advisors.md) (supporting)
- [Loans and debt](../mechanic/loans-debt.md) (supporting)
- [Pause and speed control](../mechanic/variable-speed.md) (supporting)
- [Utility action selection](../mechanic/utility-action-selection.md) (supporting)

## Backlinks (computed)

**influenced:** [Prison Architect](../game/prison-architect.md), [Two Point Hospital](../game/two-point-hospital.md)

## Sources

- [Theme Hospital](../source/src-wikipedia-theme-hospital.md)

---
Provenance: created in run `2026-10-24-catalog-ge`; reviewed in `2026-10-24-review-fixes`.
