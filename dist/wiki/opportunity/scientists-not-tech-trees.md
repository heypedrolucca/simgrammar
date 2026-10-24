# Research by named scientists

*Opportunity* · `scientists-not-tech-trees` · status: **asserted**

Replace the abstract research meter with named researchers whose skills, relationships, and rivalries determine what gets discovered and when.

| field | value |
|---|---|
| opportunity type | Mechanic upgrade |
| involves | [Tech tree](../mechanic/tech-tree.md), [Relationship values](../mechanic/relationship-values.md), [Agent skills](../mechanic/agent-skills.md), [Personality traits](../mechanic/personality-traits.md), [Staff hiring and rosters](../mechanic/staff-hiring.md) |
| applies | [Generative agents (memory stream, reflection, planning)](../technique/generative-agents.md), [On-device small language models for characters](../technique/on-device-language-models.md) |
| precedent | [Stellaris](../game/stellaris.md), [Sid Meier's Civilization](../game/civilization.md), [Game Dev Tycoon](../game/game-dev-tycoon.md), [Dwarf Fortress](../game/dwarf-fortress.md) |
| novelty | 3 |
| feasibility | 4 |
| impact | 2 |
| horizon | Now |
| key risks | Stochastic research frustrates players planning builds., Micromanaging researchers adds busywork. |
| falsifiable signal | {'prediction': 'A strategy or management game will ship research performed by a simulated population of named researchers whose relationships affect outcomes.', 'resolve_by': '2029-06-30', 'criteria': 'Title or expansion released after 2026-10-24 with at least 1,000 Steam user reviews; documentation describes research progress that depends on relationships between named researcher characters, not only on their individual stats.'} |
| priority *(computed)* | 2.764 |

## Thesis

Tech trees are the most common mechanic in the catalog and among the least simulated: research is a currency spent on a graph. Relationship systems are common too, but the white-space analysis shows the two rarely meet. Research performed by a small population of named scientists with skills, collaborations, and grudges turns progression into a social system and makes breakthroughs into stories, using the same agent stack as colony sims.

## Design Sketch

Each project needs a lead and collaborators; compatibility and rivalry change speed and the chance of side discoveries; scientists publish, poach, and defect. The tech graph becomes partially stochastic: what is discovered depends on who works together.

## Key Risks

- Stochastic research frustrates players planning builds.
- Micromanaging researchers adds busywork.

## Validation Experiment

Swap the research meter in a strategy prototype for a ten-scientist system and compare player-recalled research events and build-plan satisfaction. Success: more recalled research stories without lower plan satisfaction.

## Falsifiable signal

- **Prediction:** A strategy or management game will ship research performed by a simulated population of named researchers whose relationships affect outcomes.
- **Resolve by:** 2029-06-30
- **Criteria:** Title or expansion released after 2026-10-24 with at least 1,000 Steam user reviews; documentation describes research progress that depends on relationships between named researcher characters, not only on their individual stats.

## Relations

**applies**

- [Generative agents (memory stream, reflection, planning)](../technique/generative-agents.md)
- [On-device small language models for characters](../technique/on-device-language-models.md)

**involves**

- [Tech tree](../mechanic/tech-tree.md)
- [Relationship values](../mechanic/relationship-values.md)
- [Agent skills](../mechanic/agent-skills.md)
- [Personality traits](../mechanic/personality-traits.md)
- [Staff hiring and rosters](../mechanic/staff-hiring.md)

**precedent**

- [Stellaris](../game/stellaris.md)
- [Sid Meier's Civilization](../game/civilization.md)
- [Game Dev Tycoon](../game/game-dev-tycoon.md)
- [Dwarf Fortress](../game/dwarf-fortress.md)

---
Provenance: created in run `2026-10-24-synthesis`; reviewed in `2026-10-24-review-fixes`.
