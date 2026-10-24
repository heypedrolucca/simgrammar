# Big Ambitions

*Game* · `big-ambitions` · status: **sourced**

A business life sim set in a simulated New York City in which the player's avatar rents storefronts, stocks and staffs shops, builds warehouse logistics, and grows from one store into a business empire.

| field | value |
|---|---|
| year | 2023 |
| year full release | 2026 |
| developer | Hovgaard Games |
| platforms | PC |
| subgenre | Business / economic sim |
| subgenre secondary | Life sim |
| sim domain | Economic, Urban, Domestic / personal |
| player role | Manager / owner |
| agency model | Direct avatar, Zoning / placement, Policy / parameter |
| time model | Real-time with pause |
| sim scale | City |
| fidelity | Stylized |
| perspective | Third-person |
| win structure | Open sandbox |
| failure model | Soft / recoverable |
| narrative mode | None |
| multiplayer | Single-player |
| modding | None |
| production tier | Indie |
| agent count order | ~100 |
| emergence | 2 |
| influence | 1 |
| cluster *(computed)* | C01 |
| core count *(computed)* | 4 |
| mechanic count *(computed)* | 12 |

## Summary

A business life sim set in a simulated New York City in which the player's avatar rents storefronts, stocks and staffs shops, builds warehouse logistics, and grows from one store into a business empire.

## Core Loop

rent a building and renovate it -> buy stock and set prices -> customers visit and buy -> hire staff and managers -> import from the harbour into warehouses -> trucks deliver to stores -> invest profits in more businesses and real estate

## Design Notes

Big Ambitions starts the business at street level: the avatar personally rents, furnishes, stocks, and runs the first store and must also eat, sleep, and stay healthy and happy. Growth comes from replacing the player's own labor with staff and then with managers (HR managers, logistics managers, purchasing agents) who automate hiring, purchasing, and delivery from an HQ. Supply moves through a physical chain from harbour importers to warehouses to stores on delivery trucks. Business types range from gift shops and supermarkets to law firms and web development.

## Relations

**uses**

- [Direct avatar control](../mechanic/direct-avatar.md) (core): The player walks and drives through New York City to rent buildings, buy stock, restock shelves, and run errands until staff take over.
- [Customer value choice](../mechanic/customer-value-choice.md) (core): Customers decide whether to buy based on the store's prices and the products and service it offers.
- [Staff hiring and rosters](../mechanic/staff-hiring.md) (core): Employees are hired with skills and wages for each business, then HR managers, logistics managers, and purchasing agents automate operations from an HQ.
- [Building placement](../mechanic/free-placement.md) (core): Rented buildings are renovated and furnished with shelves, registers, and fixtures that set what a store can sell and how many customers it serves.
- [Storage and buffers](../mechanic/storage-capacity.md) (supporting): Stock fills store shelves and warehouses; empty shelves lose sales.
- [Vehicle routes and schedules](../mechanic/vehicle-route-scheduling.md) (supporting): Delivery trucks carry goods from harbour importers to warehouses and stores.
- [Delegation to AI managers](../mechanic/delegation-to-ai.md) (supporting): Managers at the HQ take over hiring, purchasing, and logistics.
- [Survival meters](../mechanic/survival-meters.md) (supporting): The avatar must eat food stored at home, sleep, and stay healthy and happy.
- [Loans and debt](../mechanic/loans-debt.md) (supporting): Bank loans fund early expansion.
- [Daily schedules](../mechanic/daily-schedules.md) (supporting): Businesses keep opening hours and staff work scheduled shifts.
- [Advertising and awareness](../mechanic/advertising-awareness.md) (supporting): Paid marketing campaigns raise customer traffic to the player's businesses.
- [Pause and speed control](../mechanic/variable-speed.md) (supporting)

## Backlinks (computed)

**precedent for:** [Human-calibrated customers](../opportunity/human-calibrated-customers.md)

## Sources

- [Big Ambitions on Steam](../source/src-steam-2026-big-ambitions.md)

---
Provenance: created in run `2026-10-24-catalog-ge`; reviewed in `2026-10-24-review-fixes`.
