# Byproducts and waste

*Mechanic* · `byproducts-waste` · status: **sourced**

Production emits secondary outputs such as sludge, garbage, heat, or spent fuel that must be handled or they impair the system.

| field | value |
|---|---|
| aliases | waste products, secondary outputs, garbage |
| family | Resources & production |
| substrate | Aggregate stocks, Rule system |
| math basis | System dynamics / ODEs, Optimization |
| feedback | Balancing (negative) |
| player interface | Placement, Observation only |
| legibility | 3 |
| emergence potential | 3 |
| authoring cost | 2 |
| compute cost | 2 |
| tuning difficulty | 3 |
| ai leverage | 2 |
| maturity | Established |
| core count *(computed)* | 1 |
| earliest game *(computed)* | [Oxygen Not Included](../game/oxygen-not-included.md) |
| earliest year *(computed)* | 2017 |
| prevalence *(computed)* | 3 |
| prevalence share *(computed)* | 0.017 |
| subgenre spread *(computed)* | 2 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

A recipe or activity emits one or more secondary outputs alongside its primary product, at a fixed ratio per cycle or per capita. The byproduct accumulates in a local output buffer or tile stock; when that stock hits a cap, the producer stalls, degrades, or releases it into the environment. The player must route it to a consumer, a sink (incinerator, landfill, vent), or a converter. In Oxygen Not Included a Natural Gas Generator burning 90 g/s of natural gas yields 800 W plus 67.5 g/s of polluted water and 22.5 g/s of carbon dioxide that must be piped away or vented into the base. In Factorio oil processing yields heavy oil, light oil, and petroleum gas together, so an unconsumed output backs up and halts the refinery. In Cities: Skylines buildings generate garbage that trucks must collect or it accumulates and flags the building as a problem. Inputs: production cycles or population. Outputs: a waste stock and an impairment signal (stall, pollution, illness, abandonment).

## Player Experience

Every new building arrives with a cleanup problem attached. The player learns to ask where the waste goes before placing a producer, and designs sinks, reuse loops, or disposal districts. A full output buffer stopping a whole line teaches that the unwanted product sets the pace of the wanted one.

## Design Levers

- byproduct ratio per cycle and whether it scales with efficiency upgrades
- buffer size before the producer stalls or starts releasing waste into the environment
- whether the byproduct is pure waste, a sellable good, or an input to another chain
- available sinks and their costs, such as incinerators, landfills, vents, or voiding
- the impairment when unhandled: production stall, pollution, disease, morale loss, or abandonment

## Failure Modes

- A cheap sink that destroys anything removes the problem and turns the mechanic into a one-time build tax.
- Byproducts with no use and no penalty become clutter that players ignore.
- Fixed-ratio multi-output recipes deadlock silently when one output has no consumer, and the stall appears far from its cause.
- Waste that only matters late, such as a full landfill or spent nuclear fuel, surprises players who built for hours without a disposal plan.

## Dynamics

- Waste outputs become inputs elsewhere, so industrial clusters form around reuse loops (polluted water to a water sieve in Oxygen Not Included, heavy oil cracked to light oil in Factorio).
- Disposal capacity becomes a hidden ceiling on growth, separate from input supply.
- Coupled with pollution spread, unhandled byproducts shift cost onto neighbors and land value.
- Players overbuild storage for byproducts as a buffer, trading space for time before the next fix.

## Open Questions

- Can a generative chemistry model produce byproduct sets for new recipes that stay balanced without hand tuning?
- What ratio of waste to useful output keeps disposal a design problem rather than a chore?

## Relations

**synergy**

- [Pollution spread](../mechanic/pollution-spread.md): Waste outputs are the sources that pollution diffusion spreads.

## Backlinks (computed)

**used by:** [Captain of Industry](../game/captain-of-industry.md), [Oxygen Not Included](../game/oxygen-not-included.md), [Satisfactory](../game/satisfactory.md)

## Sources

- [Natural Gas Generator](../source/src-oniwiki-2026-natural-gas-generator.md)

---
Provenance: created in run `2026-10-24-taxonomy-m1`.
