# Interest groups

*Mechanic* · `interest-groups` · status: **sourced**

Factions within a polity have clout and preferences over policies, and their approval gates what the player can do.

| field | value |
|---|---|
| aliases | factions (domestic), political factions, estates |
| family | Governance & policy |
| substrate | Aggregate stocks, Agent-based |
| math basis | Game theory, Social network models, Utility / decision theory |
| feedback | Both |
| player interface | Choice / cards, Observation only |
| legibility | 3 |
| emergence potential | 4 |
| authoring cost | 3 |
| compute cost | 2 |
| tuning difficulty | 4 |
| ai leverage | 4 |
| maturity | Established |
| core count *(computed)* | 4 |
| earliest game *(computed)* | [Europa Universalis IV](../game/europa-universalis-4.md) |
| earliest year *(computed)* | 2013 |
| prevalence *(computed)* | 6 |
| prevalence share *(computed)* | 0.034 |
| subgenre spread *(computed)* | 4 |
| technique count *(computed)* | 1 |
| technique exposure *(computed)* | 0.188 |

## Definition

Owns a set of groups within the polity, each with members, clout (political power), ideology or preferences over laws and policies, and approval. Clout is recomputed from members' wealth, numbers, and enfranchisement; approval from how well current laws match the group's preferences, whether it is in government, and events. Approval and clout gate what the player can do and trigger effects: favorable traits, petitions, obstruction, radicalization, or revolt. Victoria 3 (2022) is the canonical form: each pop gives political strength to the group it supports based mainly on wealth and the voting law, clout is the group's share of the national total and classifies groups as powerful, influential, or marginalized, marginalized groups cannot activate traits, and law enactment chances depend on the endorsement or opposition of groups in government. Tropico 6, Stellaris factions, and Frostpunk 2's factions are other forms.

## Player Experience

Governing through coalitions. The player reads which groups are strong and what they want, brings friendly groups into government, placates or marginalizes opponents, and accepts that every reform makes someone angry. Power is never absolute.

## Design Levers

- number of groups and how distinct their preferences are
- clout formula (wealth, population, votes, offices held)
- approval inputs (laws, government membership, events, promises)
- effects at each approval and clout band (traits, petitions, obstruction, revolt)
- how members move between groups as their economic conditions change

## Failure Modes

- When one group's clout dominates and nothing shifts it, politics freezes into one optimal coalition.
- Approval effects that are too weak make groups ignorable, and too strong make reforms impossible.
- Opaque clout and approval math makes political outcomes feel random without detailed tooltips.

## Dynamics

- Laws that empower a group raise its clout, which helps it block reforms that would weaken it, so institutions entrench.
- Economic change moves people between groups, so industrialization shifts political power over decades.
- Angry groups with high clout radicalize into movements that can force concessions or civil war.

## Open Questions

- Can LLM-driven group leaders negotiate, make demands, and remember broken deals in ways that stay consistent with the clout and approval model?
- Can interest groups form and dissolve from the population's actual interests rather than from a fixed authored list?

## Relations

**synergy**

- [Policy toggles](../mechanic/policy-toggles.md): Policies gain or lose group approval, so lawmaking becomes coalition management.
- [Stability and unrest](../mechanic/stability-unrest.md): Alienated groups radicalize into unrest.

## Backlinks (computed)

**affected by:** [LLM models of individual human choice](../technique/human-behavior-simulation-models.md)

**involved in:** [Natural-language legislation](../opportunity/natural-language-legislation.md)

**used by:** [Democracy 4](../game/democracy-4.md), [Europa Universalis IV](../game/europa-universalis-4.md), [Frostpunk 2](../game/frostpunk-2.md), [Stellaris](../game/stellaris.md), [Tropico 6](../game/tropico-6.md), [Victoria 3](../game/victoria-3.md)

## Sources

- [Victoria 3 Dev Diary #6: Interest Groups](../source/src-paradox-2021-vic3-interest-groups.md)
- [Victoria 3 Dev Diary #80: Law Enactment and Revolution Clock in 1.3](../source/src-paradox-2023-vic3-law-enactment.md)

---
Provenance: created in run `2026-10-24-taxonomy-m2`.
