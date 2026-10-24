# Loans and debt

*Mechanic* · `loans-debt` · status: **sourced**

Capital can be borrowed at interest with repayment schedules, so leverage accelerates both growth and failure.

| field | value |
|---|---|
| aliases | bonds, credit, leverage |
| family | Economy & finance |
| substrate | Aggregate stocks |
| math basis | System dynamics / ODEs, Optimization |
| feedback | Reinforcing (positive) |
| player interface | Parameter |
| legibility | 4 |
| emergence potential | 2 |
| authoring cost | 1 |
| compute cost | 1 |
| tuning difficulty | 3 |
| ai leverage | 2 |
| maturity | Classic |
| requires | [Treasury and budget](../mechanic/budget-treasury.md) |
| core count *(computed)* | 0 |
| earliest game *(computed)* | [Railroad Tycoon](../game/railroad-tycoon.md) |
| earliest year *(computed)* | 1990 |
| prevalence *(computed)* | 13 |
| prevalence share *(computed)* | 0.075 |
| subgenre spread *(computed)* | 9 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

Owns outstanding principal, an interest rate, a repayment schedule, and a borrowing limit. Each period interest is charged to the treasury, and principal is repaid on schedule, at will, or at bond maturity. The limit and rate often depend on a credit rating, net worth, or the number of outstanding loans. Missed payments trigger penalties, forced liquidation, bankruptcy, or game over. Railroad Tycoon (1990) starts each railroad with $1 million split evenly between equity and a loan and lets players sell bonds for more capital. SimCity 2000 adds bonds to the city budget, Theme Hospital offers loans through a policy setting, and Transport Tycoon lets companies raise and repay a loan in increments up to a cap.

## Player Experience

Betting on the future. The player borrows to build faster than income allows, watches interest eat margins, and times repayment. A downturn while leveraged turns a confident plan into a scramble to stay solvent.

## Design Levers

- interest rate and whether it rises with debt load, credit rating, or economic conditions
- borrowing cap tied to net worth, rating, or a fixed limit
- repayment structure (amortized, interest-only, bond maturity, repay at will)
- default consequence (penalty, asset seizure, bankruptcy, game over)
- priority of debt service relative to wages and services when cash runs short

## Failure Modes

- Cheap debt with high early returns makes borrowing the maximum at the start a dominant opening in many tycoon games.
- Default with no warning or recovery path ends runs abruptly and teaches players never to borrow.
- Fixed rates in a growing economy make debt irrelevant once revenue scales.

## Dynamics

- Leverage amplifies booms and busts: borrowed capital grows revenue faster but turns a demand dip into bankruptcy.
- Rates that rise with debt load create spirals in which new loans pay old interest.
- Interest acts as a money sink that drains surplus in the late game.

## Open Questions

- Could AI lenders that assess a player's plans and history negotiate terms in language, making credit a relationship rather than a slider?
- What rate curves keep leverage a real choice across a whole game rather than an opening move?

## Relations

**requires**

- [Treasury and budget](../mechanic/budget-treasury.md)

## Backlinks (computed)

**used by:** [Big Ambitions](../game/big-ambitions.md), [Democracy 4](../game/democracy-4.md), [Euro Truck Simulator 2](../game/euro-truck-simulator-2.md), [Europa Universalis IV](../game/europa-universalis-4.md), [Farming Simulator 25](../game/farming-simulator-25.md), [Hardspace: Shipbreaker](../game/hardspace-shipbreaker.md), [Offworld Trading Company](../game/offworld-trading-company.md), [Railroad Tycoon](../game/railroad-tycoon.md), [RollerCoaster Tycoon](../game/rollercoaster-tycoon.md), [SimCity 2000](../game/simcity-2000.md), [Theme Hospital](../game/theme-hospital.md), [Theme Park](../game/theme-park.md), [Transport Tycoon](../game/transport-tycoon.md)

## Sources

- [Railroad Tycoon (video game)](../source/src-wikipedia-railroad-tycoon.md)
- [SimCity 2000](../source/src-wikipedia-simcity-2000.md)
- [Theme Hospital](../source/src-wikipedia-theme-hospital.md)

---
Provenance: created in run `2026-10-24-taxonomy-m2`.
