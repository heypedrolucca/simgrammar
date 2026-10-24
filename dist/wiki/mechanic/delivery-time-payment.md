# Delivery-time payment

*Mechanic* · `delivery-time-payment` · status: **sourced**

Payment for a delivery depends on cargo type, quantity, distance, and transit time, with each cargo losing value at its own rate the longer it travels.

| field | value |
|---|---|
| aliases | cargo payment rates, time-decaying cargo value, transit-time pricing |
| family | Economy & finance |
| substrate | Rule system |
| math basis | Optimization, Scheduling |
| feedback | None |
| player interface | Observation only |
| legibility | 3 |
| emergence potential | 2 |
| authoring cost | 2 |
| compute cost | 1 |
| tuning difficulty | 2 |
| ai leverage | 1 |
| maturity | Established |
| open questions | Could time sensitivity come from simulated recipients' needs, such as a town short of food paying more for fast grain, rather than fixed per-cargo curves? |
| core count *(computed)* | 0 |
| earliest game *(computed)* | [Railroad Tycoon](../game/railroad-tycoon.md) |
| earliest year *(computed)* | 1990 |
| prevalence *(computed)* | 2 |
| prevalence share *(computed)* | 0.011 |
| subgenre spread *(computed)* | 1 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

Owns a payment table per cargo type (a base rate, a distance weight, and a value curve over time in transit) and computes revenue at delivery from quantity, base rate, and distance, multiplied by a time factor that falls as transit time grows; in common implementations the factor holds flat for a cargo-specific grace period before it declines. Fast-decaying cargo such as mail and passengers rewards short or fast routes, while bulk cargo such as coal keeps its value over long, slow hauls. Cargo moved in stages can be paid in parts at transfer points. Transport Tycoon (1994) pays by cargo type, distance, quantity, and delivery time, and OpenTTD keeps the model and adds transfer orders with partial payment for feeder services. It differs from vehicle-route-scheduling, which owns the order lists that move cargo, and from contracts-orders, which owns discrete jobs with fixed payouts and deadlines; here every delivery is priced continuously by how long it took.

## Player Experience

Speed has a price per cargo. The player matches cargo to mode, putting mail on fast trains or aircraft and coal on slow freight, and reads every delay at a junction as lost money. Upgrading to faster vehicles becomes an investment with a visible return.

## Design Levers

- base rate per cargo type
- shape of each cargo's value curve (grace period, slope, floor)
- distance measure, straight-line between endpoints or route length
- partial payment rules for transfers and feeder legs
- inflation or era scaling of rates

## Failure Modes

- Paying by route length rather than endpoint distance rewards deliberate detours.
- Near-identical curves make every cargo the same and remove route specialization.
- Transfer credits shown at feeder stations can make feeder vehicles look profitable while the final leg shows a loss, confusing players about which vehicles earn money.
- Decay so steep that slow modes earn nothing collapses mode choice to the fastest vehicle.

## Dynamics

- Cargo sorts by mode, with mail and passengers on fast services and bulk goods on slow ones.
- Faster vehicles pay back through higher rates, coupling payment to fleet renewal.
- Congestion and signal delays cost money directly, so network design is priced.

## Open Questions

- Could time sensitivity come from simulated recipients' needs, such as a town short of food paying more for fast grain, rather than fixed per-cargo curves?

## Backlinks (computed)

**used by:** [Railroad Tycoon](../game/railroad-tycoon.md), [Transport Tycoon](../game/transport-tycoon.md)

## Claims

- Transport Tycoon pays for deliveries by delivery time as well as distance and cargo. *(confidence: medium)* [[73](../source/src-wikipedia-transport-tycoon.md)]
- OpenTTD orders include transfer with partial payment for feeder services. *(confidence: high)* [[74](../source/src-openttd-2026-manual-orders.md)]

## Sources

- [Transport Tycoon](../source/src-wikipedia-transport-tycoon.md)
- [Manual/Orders](../source/src-openttd-2026-manual-orders.md)

---
Provenance: created in run `2026-10-24-taxonomy-triage-a`.
