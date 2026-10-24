# RCI demand

*Mechanic* · `rci-demand` · status: **sourced**

A demand signal for residential, commercial, and industrial land derived from the balance of jobs, workers, and goods.

| field | value |
|---|---|
| aliases | RCI meter, demand bars, zone demand |
| family | Economy & finance |
| substrate | Aggregate stocks |
| math basis | System dynamics / ODEs, Control theory |
| feedback | Balancing (negative) |
| player interface | Observation only, Placement |
| legibility | 4 |
| emergence potential | 3 |
| authoring cost | 1 |
| compute cost | 1 |
| tuning difficulty | 3 |
| ai leverage | 2 |
| maturity | Classic |
| requires | [Zoning](../mechanic/zoning.md) |
| core count *(computed)* | 3 |
| earliest game *(computed)* | [SimCity](../game/simcity-1989.md) |
| earliest year *(computed)* | 1989 |
| prevalence *(computed)* | 3 |
| prevalence share *(computed)* | 0.017 |
| subgenre spread *(computed)* | 1 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

Owns three demand valves (residential, commercial, industrial) updated from the balance of population, jobs, and outside trade, and read by zone growth. In Micropolis, the SimCity engine, projected residents = residents + migration (proportional to jobs per resident - 1) + 2% births; projected commerce = total population / 3.7 x a labor ratio capped at 1.3; projected industry = industry x labor ratio x an external market factor (1.2, 1.1, or 0.98 by difficulty). Each valve moves by (projected / actual - 1) x 600 plus a tax offset (+200 at 0% tax, 0 at 7%, -600 at 20% on easy), is clamped to +/-2000 (residential) or +/-1500, and is held at 0 until a needed stadium, seaport, or airport exists. A zone grows when valve + a local score (land value for homes) passes a random test. SimCity's RCI bar and Cities: Skylines' demand bars display these valves.

## Player Experience

A steering signal. The player glances at three bars, zones whatever is in demand, and learns that homes need jobs, jobs need workers, and industry needs outside trade. When a bar stays pinned despite growth, the player hunts for the missing stadium, port, or tax cut.

## Design Levers

- inputs to each valve (jobs per resident, internal market size, external trade, taxes)
- gain and clamp on each valve, which set how fast demand swings
- caps that hold demand at zero until a specific building is placed
- how much local factors (land value, traffic, pollution) add to the global valve
- whether demand is split further by wealth or density tier

## Failure Modes

- Players treat the bar as an instruction and zone mechanically, so the city grows without plan or tradeoff.
- Hidden caps (needing a stadium or port) freeze growth with no explanation unless an advisor says why.
- High gain makes demand oscillate between booms and abandonment.

## Dynamics

- Residential and job growth chase each other, producing alternating waves of house and workplace construction.
- Raising taxes depresses all three valves at once, so tax policy shows up as slower development rather than a direct penalty.
- Valve caps create milestone moments when one building unlocks a growth spurt.

## Open Questions

- Would demand derived bottom-up from simulated households and firms be more interesting than a three-valve controller, and could players still read it?
- Can an AI advisor turn valve inputs into a plain causal explanation of why demand is low?

## Relations

**requires**

- [Zoning](../mechanic/zoning.md)

**synergy**

- [Zoning](../mechanic/zoning.md): The demand meter tells the player which zone to paint next; zoning answers it.

## Backlinks (computed)

**used by:** [SimCity](../game/simcity-1989.md), [SimCity 2000](../game/simcity-2000.md), [SimCity 4](../game/simcity-4.md)

## Sources

- [Micropolis: open-source SimCity source code](../source/src-hopkins-2008-micropolis.md)

---
Provenance: created in run `2026-10-24-taxonomy-m2`.
