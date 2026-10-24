# Diagnosis and treatment

*Mechanic* · `diagnosis-treatment` · status: **sourced**

Patients present symptoms, examinations reduce uncertainty about a hidden condition, and the correct treatment cures it while wrong or late treatment harms.

| field | value |
|---|---|
| aliases | medical diagnosis, differential diagnosis |
| family | Biology & health |
| substrate | Rule system, Stochastic events |
| math basis | Probability / statistics, Information theory |
| feedback | Balancing (negative) |
| player interface | Choice / cards, Parameter, Orders |
| legibility | 3 |
| emergence potential | 2 |
| authoring cost | 3 |
| compute cost | 1 |
| tuning difficulty | 3 |
| ai leverage | 4 |
| maturity | Established |
| core count *(computed)* | 3 |
| earliest game *(computed)* | [Theme Hospital](../game/theme-hospital.md) |
| earliest year *(computed)* | 1997 |
| prevalence *(computed)* | 3 |
| prevalence share *(computed)* | 0.017 |
| subgenre spread *(computed)* | 2 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

Owns, per patient, a hidden condition, a set of symptoms (some visible, some revealed only by examinations), a diagnosis certainty or candidate list, and a deterioration timer. Each examination reveals symptoms or raises certainty at a cost in time and capacity; once certainty passes a threshold or one candidate remains, the patient goes to the matching treatment, whose success depends on staff skill or equipment. Untreated or mistreated patients worsen or die. Theme Hospital sends patients from a GP's office to diagnosis rooms, lets policy raise the required diagnosis level, and can kill patients when a guessed cure is wrong; Project Hospital has examinations uncover symptoms drawn from real medicine, tunes symptom overlap so one examination rarely settles a case, and requires finding dangerous hidden symptoms in time. Inputs are arrivals and examination capacity; outputs are cures, deaths, and throughput.

## Player Experience

Detective work under time pressure. The player weighs another test against the risk of the patient worsening and decides when certainty is good enough to act. In management games the same choice becomes a policy over many patients: how much diagnosis to buy before treating.

## Design Levers

- number of conditions and the overlap of their symptom sets
- information gained per examination and its time, cost, and capacity
- certainty threshold for treatment and whether the player can override it
- deterioration rate of untreated patients and the cost of misdiagnosis
- staff skill and equipment effects on test accuracy and treatment success

## Failure Modes

- Distinctive symptom sets let one examination solve every case, removing the uncertainty that defines the mechanic.
- Opaque certainty math leaves players unable to tell whether a death was bad luck or bad policy.
- Conditions are expensive to author, so case variety runs out and players memorize answers.

## Dynamics

- Diagnosis capacity becomes a bottleneck that creates queues, so room layout and staffing drive outcomes.
- Guessing cures to clear queues trades throughput against deaths and reputation.
- Contagious conditions couple diagnosis speed to outbreaks inside the facility.

## Open Questions

- Can language-model patients that describe symptoms in their own words make history-taking a real diagnostic channel?
- Can generated cases keep symptom overlap tuned so diagnosis stays uncertain but solvable?

## Relations

**synergy**

- [Service queues](../mechanic/service-queues.md): Patients queue at each diagnostic step, so hospital layout is queue design (Theme Hospital).

## Backlinks (computed)

**used by:** [Project Hospital](../game/project-hospital.md), [Theme Hospital](../game/theme-hospital.md), [Two Point Hospital](../game/two-point-hospital.md)

## Sources

- [Theme Hospital](../source/src-wikipedia-theme-hospital.md)
- [Project Hospital: a realistic take on hospital simulation](../source/src-jgeekstudies-2020-project-hospital.md)

---
Provenance: created in run `2026-10-24-taxonomy-m5`.
