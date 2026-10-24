# Fluid and gas simulation

*Mechanic* · `fluid-gas-simulation` · status: **sourced**

Liquids and gases stored per cell or as fields flow, mix, and pressurize across space according to pressure and density differences.

| field | value |
|---|---|
| aliases | fluid dynamics, gas spread, liquid simulation |
| family | Physics & materials |
| substrate | Cellular grid, Continuous physics |
| math basis | Continuum mechanics, Cellular automata |
| feedback | Balancing (negative) |
| player interface | Placement, Observation only |
| legibility | 3 |
| emergence potential | 4 |
| authoring cost | 1 |
| compute cost | 4 |
| tuning difficulty | 3 |
| ai leverage | 4 |
| maturity | Established |
| core count *(computed)* | 6 |
| earliest game *(computed)* | [Dwarf Fortress](../game/dwarf-fortress.md) |
| earliest year *(computed)* | 2006 |
| prevalence *(computed)* | 11 |
| prevalence share *(computed)* | 0.063 |
| subgenre spread *(computed)* | 7 |
| technique count *(computed)* | 2 |
| technique exposure *(computed)* | 0.2 |

## Definition

Fluid state is stored per cell (mass, depth, pressure, element) or as velocity and density fields. Cellular games move mass between neighbor cells in proportion to height or pressure differences and sort elements by density, as in Oxygen Not Included, where each cell holds one gas or liquid element with a mass, and Dwarf Fortress, where water depth runs from 1 to 7 per tile. Continuous solvers follow Jos Stam's Stable Fluids for games (2003): add sources, diffuse implicitly with Gauss-Seidel relaxation, advect semi-Lagrangian by tracing cells back through the velocity field, and project velocity to be divergence-free by solving a Poisson equation, which stays stable at any time step. Outputs feed breathing, flooding, pressure damage, and heat transport.

## Player Experience

Managing something that spreads on its own. Players seal leaks, vent gases, pump floods, and plan around pressure they can only see through overlays. Small mistakes spread slowly, then all at once.

## Design Levers

- representation: cellular mass transfer, particles, or velocity fields
- grid resolution and update rate
- one element per cell or mixtures
- compressibility and pressure limits
- viscosity and flow speed per fluid
- whether mass is strictly conserved

## Failure Modes

- Non-conserving rules let players delete or duplicate fluid, which becomes an exploit.
- Fluid simulation dominates compute and forces small maps or reduced update rates.
- Semi-Lagrangian solvers lose detail to numerical dissipation, so flow looks thick and smoothed.
- Gases are unreadable without overlays, so players misjudge spreading hazards.

## Dynamics

- Leaks contaminate connected spaces and couple room layout to air quality.
- Floods spread through open layers and paths and reshape priorities across a colony.
- Coupled with heat, fluids carry temperature and drive phase changes.

## Open Questions

- Can learned fluid simulators run 3D liquids at game budgets while conserving mass well enough for gameplay?
- What overlays make invisible gas flow legible without constant mode switching?

## Relations

**synergy**

- [Heat transfer](../mechanic/heat-transfer.md): Gases and liquids carry heat, so thermal management becomes plumbing (Oxygen Not Included).

## Backlinks (computed)

**affected by:** [Differentiable simulation](../technique/differentiable-simulation.md), [Graph network simulators and neural operators](../technique/graph-network-simulators.md)

**involved in:** [Learned material surrogates at world scale](../opportunity/learned-material-surrogates.md)

**used by:** [Caves of Qud](../game/caves-of-qud.md), [Dwarf Fortress](../game/dwarf-fortress.md), [FTL: Faster Than Light](../game/ftl.md), [Hardspace: Shipbreaker](../game/hardspace-shipbreaker.md), [Minecraft](../game/minecraft.md), [Noita](../game/noita.md), [Oxygen Not Included](../game/oxygen-not-included.md), [Space Engineers](../game/space-engineers.md), [Space Haven](../game/space-haven.md), [Stationeers](../game/stationeers.md), [The Powder Toy](../game/the-powder-toy.md)

## Sources

- [Real-Time Fluid Dynamics for Games](../source/src-stam-2003-real-time-fluid-dynamics.md)

---
Provenance: created in run `2026-10-24-taxonomy-m4`.
