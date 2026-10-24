# Player organizations

*Mechanic* · `player-organizations` · status: **sourced**

Players form corporations, guilds, or governments with membership, roles, permissions, and shared assets.

| field | value |
|---|---|
| aliases | guilds, corporations, clans, alliances |
| family | Multiplayer & persistence |
| substrate | Network / graph, Rule system |
| math basis | Game theory, Social network models, Mechanism design / auctions |
| feedback | Reinforcing (positive) |
| player interface | Parameter, Orders |
| legibility | 4 |
| emergence potential | 4 |
| authoring cost | 1 |
| compute cost | 1 |
| tuning difficulty | 4 |
| ai leverage | 3 |
| maturity | Classic |
| core count *(computed)* | 1 |
| earliest game *(computed)* | [Ultima Online](../game/ultima-online.md) |
| earliest year *(computed)* | 1997 |
| prevalence *(computed)* | 5 |
| prevalence share *(computed)* | 0.029 |
| subgenre spread *(computed)* | 2 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

An organization entity holds a membership list, a role table that maps roles to permissions (hire, spend, access storage, declare war), shared assets such as a treasury, hangars, or land, and optional revenue rules such as a tax on members' income. Organizations can nest into federations and act as parties to diplomacy and war. In Eve Online, a CEO runs each corporation and assigns roles such as director and accountant, corporations can tax members' earnings, declare war on other corporations for a weekly fee, and join alliances that claim sovereignty over null-sec star systems. Ultima Online guilds, Eco governments, and A Tale in the Desert's guilds are other forms. Inputs: membership and role changes, member income. Outputs: shared pools, permissions, and collective standing.

## Player Experience

Players belong to something larger than their own account. They take on roles such as leader, logistician, or recruiter, coordinate on projects too big for one person, and argue about governance. Betrayal and politics become play.

## Design Levers

- role and permission granularity
- shared asset types and access controls
- organization taxes and costs of founding or upkeep
- size caps and federation rules
- war and diplomacy rules between organizations
- protection against theft by members with access

## Failure Modes

- Coarse permissions let a single member empty shared storage; Eve Online has a history of such corporate thefts.
- Large blocs coordinate so well that they lock smaller groups out of contested territory.
- Leaders who quit leave organizations, and their assets, stranded.

## Dynamics

- Specialization inside organizations, with miners, haulers, fighters, and diplomats, creates internal economies.
- Coalitions form and split, producing large-scale political history.
- Organizations act as onboarding for new players and as a reason veterans stay.

## Open Questions

- Can AI officers or members fill organizational roles in small groups without crowding out human players?
- Which permission and asset rules best reduce insider theft while preserving trust-based play?

## Backlinks (computed)

**involved in:** [Language-agent society terrarium](../opportunity/llm-society-terrarium.md)

**used by:** [A Tale in the Desert](../game/a-tale-in-the-desert.md), [Elite Dangerous](../game/elite-dangerous.md), [EVE Online](../game/eve-online.md), [Second Life](../game/second-life.md), [Ultima Online](../game/ultima-online.md)

## Sources

- [Eve Online](../source/src-wikipedia-eve-online.md)

---
Provenance: created in run `2026-10-24-taxonomy-m7`.
