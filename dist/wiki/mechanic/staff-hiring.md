# Staff hiring and rosters

*Mechanic* · `staff-hiring` · status: **sourced**

The player hires individual staff with skills, traits, and wages to operate a facility or team.

| field | value |
|---|---|
| aliases | hiring, roster management, staff management |
| family | Economy & finance |
| substrate | Agent-based, Stochastic events |
| math basis | Optimization, Probability / statistics |
| feedback | Reinforcing (positive) |
| player interface | Choice / cards, Orders |
| legibility | 4 |
| emergence potential | 3 |
| authoring cost | 2 |
| compute cost | 1 |
| tuning difficulty | 3 |
| ai leverage | 3 |
| maturity | Classic |
| core count *(computed)* | 10 |
| earliest game *(computed)* | [Theme Park](../game/theme-park.md) |
| earliest year *(computed)* | 1994 |
| prevalence *(computed)* | 16 |
| prevalence share *(computed)* | 0.092 |
| subgenre spread *(computed)* | 5 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

Owns a candidate pool and a roster. Each candidate has skills or attributes, traits, and a wage demand; hiring moves them to the roster at a recurring wage. Rostered staff are assigned to rooms, roles, or positions, and their skill sets the speed or quality of work there; fatigue, morale, and pay satisfaction change over time and can trigger rest, raise demands, or quitting. Training spends money and time to raise skills. Theme Hospital (1997) has the player hire doctors, nurses, handymen, and receptionists with performance statistics, train doctors, require specialist skills for rooms such as the operating theatre, send staff to rest, and dismiss staff who argue about pay. Football Manager builds a whole game around player and staff attributes, contracts, and wages, and Two Point Hospital follows Theme Hospital's model.

## Player Experience

Assembling a team. The player compares candidates' stats against their wages, places the best people where they matter most, and nurses tired or unhappy staff. Names and faces make the facility feel staffed by people rather than counters.

## Design Levers

- number of staff types and skill dimensions
- candidate pool size, refresh rate, and quality distribution
- wage curve relative to skill and how raises are demanded
- fatigue, morale, and quitting rules
- training cost, duration, and skill ceilings
- how much candidate information is hidden until hired or scouted

## Failure Modes

- When one stat dominates, hiring becomes sorting a list and staff stop feeling like individuals.
- Raise demands that grow too fast make experienced staff a liability and push players to churn employees.
- Generic stats without traits make staff interchangeable and remove attachment.

## Dynamics

- Strong staff raise income, which funds better hires, so facilities snowball toward elite rosters.
- Fatigue and rest create capacity dips that ripple into queues.
- Losing a star employee causes a sudden performance drop and a recovery arc.

## Open Questions

- Can LLM-generated candidates with backstories, interviews, and evolving workplace relationships make rosters as memorable as authored characters?
- What is the smallest set of staff attributes that keeps hiring a real decision?

## Backlinks (computed)

**involved in:** [Explained delegation to AI managers](../opportunity/explained-delegation.md), [Research by named scientists](../opportunity/scientists-not-tech-trees.md)

**used by:** [Big Ambitions](../game/big-ambitions.md), [Euro Truck Simulator 2](../game/euro-truck-simulator-2.md), [Football Manager](../game/football-manager.md), [Game Dev Tycoon](../game/game-dev-tycoon.md), [Motorsport Manager](../game/motorsport-manager.md), [Out of the Park Baseball](../game/out-of-the-park-baseball.md), [Planet Coaster](../game/planet-coaster.md), [Planet Zoo](../game/planet-zoo.md), [Prison Architect](../game/prison-architect.md), [Project Hospital](../game/project-hospital.md), [RollerCoaster Tycoon](../game/rollercoaster-tycoon.md), [Schedule I](../game/schedule-i.md), [Theme Hospital](../game/theme-hospital.md), [Theme Park](../game/theme-park.md), [Two Point Hospital](../game/two-point-hospital.md), [Zoo Tycoon](../game/zoo-tycoon.md)

## Sources

- [Theme Hospital](../source/src-wikipedia-theme-hospital.md)

---
Provenance: created in run `2026-10-24-taxonomy-m2`.
