# Euro Truck Simulator 2

*Game* · `euro-truck-simulator-2` · status: **sourced**

A truck driving sim in which the player hauls timed cargo deliveries across a scaled European road network and grows a transport company of trucks, garages, and hired drivers.

| field | value |
|---|---|
| aliases | ETS2 |
| year | 2012 |
| developer | SCS Software |
| platforms | PC |
| subgenre | Vehicle sim |
| subgenre secondary | Job sim |
| sim domain | Physical / mechanical, Industrial / logistics, Occupational |
| player role | Operator / pilot |
| agency model | Direct avatar |
| time model | Real-time |
| sim scale | Individual |
| fidelity | Stylized |
| perspective | First-person |
| win structure | Open sandbox |
| failure model | Soft / recoverable |
| narrative mode | None |
| multiplayer | Single-player, Co-op |
| modding | Content |
| production tier | AA |
| agent count order | ~100 |
| emergence | 2 |
| influence | 3 |
| cluster *(computed)* | C06 |
| core count *(computed)* | 2 |
| mechanic count *(computed)* | 11 |

## Summary

A truck driving sim in which the player hauls timed cargo deliveries across a scaled European road network and grows a transport company of trucks, garages, and hired drivers.

## Core Loop

take a cargo job -> couple the trailer -> drive the route paying fuel and tolls -> deliver on time with little damage -> earn money and experience -> spend skill points and buy trucks, garages, and drivers -> longer and riskier jobs

## Design Notes

The pleasure is long-haul driving through a compressed map (71 cities in 12 countries in the base game), with economic pressure from delivery deadlines, fuel, tolls, and repair costs and with damage deducted from pay. Progression is a skill-point tree that unlocks cargo classes (ADR hazardous, long distance, valuable, fragile, urgent, eco driving), plus a company layer in which owned garages host hired AI drivers who earn money off-screen. Multiplayer began as the fan mod TruckersMP in 2013 before official support in 2021.

## Relations

**uses**

- [Vehicle dynamics](../mechanic/vehicle-dynamics.md) (core): Licensed trucks with modeled engines and gearboxes pull trailers whose cargo changes acceleration and braking; collisions damage truck, trailer, and cargo.
- [Contracts and orders](../mechanic/contracts-orders.md) (core): Jobs specify cargo, destination, and a time limit; less damage earns more money and experience, while fuel, tolls, and repairs are paid from earnings.
- [Road networks](../mechanic/road-network.md) (supporting): A continuous road map linking European cities sets route distance, tolls, and travel time.
- [Agent skills](../mechanic/agent-skills.md) (supporting): Skill points from experience unlock ADR, long-distance, valuable, fragile, urgent, and eco-driving jobs.
- [Staff hiring and rosters](../mechanic/staff-hiring.md) (supporting): Recruitment agencies supply AI drivers who work from owned garages and return income.
- [Loans and debt](../mechanic/loans-debt.md) (supporting): A bank loan is the alternative to saving 100,000 euros for the first truck.
- [Treasury and budget](../mechanic/budget-treasury.md) (supporting)
- [Wear and breakdown](../mechanic/wear-breakdown.md) (supporting): Damage requires paid maintenance at service shops.
- [Day-night cycle](../mechanic/day-night-cycle.md) (supporting)
- [Weather](../mechanic/weather.md) (supporting)
- [Modding API](../mechanic/modding-api.md) (supporting)

## Backlinks (computed)

**precedent for:** [Simulator instructor coaching](../opportunity/sim-instructor-coach.md)

## Sources

- [Euro Truck Simulator 2](../source/src-wikipedia-euro-truck-simulator-2.md)
- [Euro Truck Simulator 2 on Steam](../source/src-steam-2026-euro-truck-simulator-2.md)
- [Euro Truck Simulator 2 (Truck Simulator Wiki)](../source/src-trucksimulatorwiki-2026-ets2.md)

---
Provenance: created in run `2026-10-24-catalog-gf`.
