# Theme Park

*Game* · `theme-park` · status: **sourced**

A theme park management game in which the player builds rides and shops, tunes prices and recipes for individually simulated visitors, and sells parks to expand worldwide.

| field | value |
|---|---|
| year | 1994 |
| developer | Bullfrog Productions |
| platforms | PC, Console, Handheld, Mobile |
| subgenre | Management / tycoon |
| subgenre secondary | Business / economic sim |
| sim domain | Economic |
| player role | Manager / owner |
| agency model | Zoning / placement, Policy / parameter, Direct unit control |
| time model | Real-time with pause |
| sim scale | Facility |
| fidelity | Stylized |
| perspective | Isometric |
| win structure | Score / ranking |
| failure model | Soft / recoverable |
| narrative mode | None |
| multiplayer | Single-player |
| modding | None |
| production tier | AA |
| agent count order | ~100 |
| emergence | 3 |
| influence | 4 |
| cluster *(computed)* | C03 |
| core count *(computed)* | 5 |
| mechanic count *(computed)* | 13 |

## Summary

A theme park management game in which the player builds rides and shops, tunes prices and recipes for individually simulated visitors, and sells parks to expand worldwide.

## Core Loop

place rides, shops, and paths -> visitors arrive by bus and choose attractions -> tune prices and shop ingredients -> fund research and hire staff -> yearly judging against rivals -> sell the park and buy a plot abroad

## Design Notes

Theme Park gives every visitor its own record (about 200 bytes each) and lets the player change the product as well as its price: ingredient settings such as sugar in ice cream trade cost against whether customers return. The full-simulation level adds wage and supply negotiations, where failure means staff strikes or lost shipments, plus research funding and shares; the sandbox level removes them, so one engine serves three depths. Unhappy visitors attract thugs, which ties satisfaction to crime. Negotiation has no mechanic in the taxonomy (proposed as negotiation).

## Relations

**uses**

- [Crowd preferences](../mechanic/crowd-preferences.md) (core): Each visitor is an individual with its own personality and arrives and leaves by bus; unhappy crowds draw thugs who vandalize and attack entertainers.
- [Customer value choice](../mechanic/customer-value-choice.md) (core): Entry, ride, and shop prices plus ingredient levels such as sugar in ice cream decide what visitors buy and whether they come back.
- [Building placement](../mechanic/free-placement.md) (core): Over thirty attractions, shops, toilets, and scenery are placed on a plot, with coasters needing laid-out track.
- [Wear and breakdown](../mechanic/wear-breakdown.md) (core): Rides wear down and explode if mechanics do not maintain them; research can make rides more durable.
- [Staff hiring and rosters](../mechanic/staff-hiring.md) (core): Entertainers, security guards, mechanics, and handymen are hired and their wages negotiated; understaffing brings litter, breakdowns, and crime.
- [Needs decay](../mechanic/needs-decay.md) (supporting): Visitors need food, drink, and toilets as their visit goes on.
- [Service queues](../mechanic/service-queues.md) (supporting): Visitors queue for rides and shops.
- [Tech tree](../mechanic/tech-tree.md) (supporting): A funding level drives research into new items, ride durability, staff efficiency, and bus capacity.
- [Crime and policing](../mechanic/crime-policing.md) (supporting): Thugs appear when visitors are unhappy; security guards counter them.
- [Rival firms](../mechanic/rival-firms.md) (supporting): The park is judged against rival parks each year.
- [Loans and debt](../mechanic/loans-debt.md) (supporting)
- [Pause and speed control](../mechanic/variable-speed.md) (supporting)
- [Negotiation](../mechanic/negotiation.md) (supporting): On the full-simulation level, staff wage talks and supply negotiations are haggles; failed wage talks end in strikes and failed supply talks in lost shipments.

## Backlinks (computed)

**influenced:** [Theme Hospital](../game/theme-hospital.md), [Transport Tycoon](../game/transport-tycoon.md)

## Sources

- [Theme Park (video game)](../source/src-wikipedia-theme-park.md)

---
Provenance: created in run `2026-10-24-catalog-ge`.
