# Project Hospital

*Game* · `project-hospital` · status: **sourced**

A hospital management sim in which the player builds departments and hires staff while doctors diagnose patients by ordering examinations that reveal symptoms until one diagnosis remains.

| field | value |
|---|---|
| year | 2018 |
| developer | Oxymoron Games |
| platforms | PC |
| subgenre | Medical sim |
| subgenre secondary | Management / tycoon |
| sim domain | Medical, Economic |
| player role | Manager / owner |
| agency model | Zoning / placement, Direct unit control |
| time model | Real-time with pause |
| sim scale | Facility |
| fidelity | Stylized |
| perspective | Isometric |
| win structure | Scenario goals |
| failure model | Soft / recoverable |
| narrative mode | None |
| multiplayer | Single-player |
| modding | Content |
| production tier | Indie |
| agent count order | ~100 |
| emergence | 2 |
| influence | 1 |
| cluster *(computed)* | C01 |
| core count *(computed)* | 3 |
| mechanic count *(computed)* | 10 |

## Summary

A hospital management sim in which the player builds departments and hires staff while doctors diagnose patients by ordering examinations that reveal symptoms until one diagnosis remains.

## Core Loop

sign insurer contracts -> patients arrive with complaints -> doctors order examinations and lab tests -> revealed symptoms narrow the diagnosis -> treat, hospitalize, or operate -> insurers pay -> build departments and hire staff

## Design Notes

Oxymoron Games reduced medicine to symptom rules: each diagnosis has symptoms with tuned occurrence frequencies, examinations reveal them, and a diagnosis becomes clear once enough are found; frequencies were set so a case is rarely obvious after the first exam. Patients reach the hospital through insurance company contracts, and the developers say the resulting economy came to resemble the American system. The free Doctor Mode update lets the player make individual doctors' exam and treatment choices, turning the facility sim into a diagnosis game.

## Relations

**uses**

- [Diagnosis and treatment](../mechanic/diagnosis-treatment.md) (core): Each patient has a hidden diagnosis; doctors order examinations, lab tests, and equipment procedures that each reveal symptoms, symptom frequencies are tuned so one exam rarely settles a case, and treatment, hospitalization, or surgery follows.
- [Staff hiring and rosters](../mechanic/staff-hiring.md) (core): The player hires and specializes doctors, nurses, lab staff, and janitors and manages their job satisfaction; the Hospital Services DLC adds staff training.
- [Building placement](../mechanic/free-placement.md) (core): The player lays foundations, walls, floor tiles, doors, and windows and places equipment for each department, or starts from prefabs.
- [Room recognition](../mechanic/room-recognition.md) (supporting)
- [Agent skills](../mechanic/agent-skills.md) (supporting)
- [Treasury and budget](../mechanic/budget-treasury.md) (supporting)
- [Service queues](../mechanic/service-queues.md) (supporting)
- [Unit commands](../mechanic/unit-commands.md) (supporting): Doctor Mode (2019) lets the player choose exams, diagnoses, and treatments for individual doctors and their patients.
- [Scenario objectives](../mechanic/scenario-objectives.md) (supporting): A campaign and six challenge levels set goals; sandbox mode removes them.
- [Pause and speed control](../mechanic/variable-speed.md) (supporting)

## Sources

- [Project Hospital](../source/src-wikipedia-project-hospital.md)
- [Project Hospital: a realistic take on hospital simulation](../source/src-jgeekstudies-2020-project-hospital.md)
- [Project Hospital on Steam](../source/src-steam-2026-project-hospital.md)

---
Provenance: created in run `2026-10-24-catalog-gf`; reviewed in `2026-10-24-review-fixes`.
