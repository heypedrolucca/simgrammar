# House Flipper

*Game* · `house-flipper` · status: **sourced**

A first-person renovation sim in which the player cleans, paints, demolishes, and furnishes rundown houses, then sells them to buyers whose bids depend on how well the house fits their needs.

| field | value |
|---|---|
| year | 2018 |
| developer | Empyrean |
| platforms | PC, Console, Handheld |
| subgenre | Job sim |
| sim domain | Occupational, Domestic / personal, Economic |
| player role | Worker |
| agency model | Direct avatar, Zoning / placement |
| time model | Real-time |
| sim scale | Facility |
| fidelity | Stylized |
| perspective | First-person |
| win structure | Open sandbox |
| failure model | None |
| narrative mode | None |
| multiplayer | Single-player |
| modding | Content |
| production tier | Indie |
| agent count order | None |
| emergence | 1 |
| influence | 2 |
| cluster *(computed)* | C02 |
| core count *(computed)* | 3 |
| mechanic count *(computed)* | 7 |

## Summary

A first-person renovation sim in which the player cleans, paints, demolishes, and furnishes rundown houses, then sells them to buyers whose bids depend on how well the house fits their needs.

## Core Loop

take email jobs for cash -> buy a rundown house -> clean, demolish, paint, tile, furnish -> buyers evaluate fit and bid -> sell at a profit -> buy bigger properties

## Design Notes

Each property is judged by a small set of buyer profiles with requirements such as cleanliness or a family room, and their auction bids reward matching a profile rather than maximizing generic quality. Labor is performed with coverage tools (paint roller, mop, window cleaner, plaster tool) that show visible progress, and tool use earns experience spent on faster tools. Email jobs paid by size and quality supply the capital for the first purchase.

## Relations

**uses**

- [Surface work tools](../mechanic/surface-work-tools.md) (core): Paint roller, mop, window cleaner, and plaster tool apply coverage to walls, floors, and windows with visible progress; tiling and demolition use the same direct tool loop.
- [Contracts and orders](../mechanic/contracts-orders.md) (core): Neighbors send email jobs (cleaning, painting, installing heaters, showers, or air conditioners, furnishing) whose pay depends on job size and quality.
- [Customer value choice](../mechanic/customer-value-choice.md) (core): Each property has potential buyers with different needs, such as cleanliness or a family room, who bid according to how well the renovated house suits them.
- [Auctions](../mechanic/auctions.md) (supporting): Sales are resolved by buyers bidding at auction.
- [Building placement](../mechanic/free-placement.md) (supporting): Furniture, doors, windows, and wallpaper from a catalog are placed freely.
- [Agent skills](../mechanic/agent-skills.md) (supporting): Using tools earns experience that is spent on tool upgrades that speed up work.
- [Direct avatar control](../mechanic/direct-avatar.md) (supporting)

## Sources

- [House Flipper](../source/src-wikipedia-house-flipper.md)
- [House Flipper on Steam](../source/src-steam-2026-house-flipper.md)

---
Provenance: created in run `2026-10-24-catalog-gf`.
