# Player legislation

*Mechanic* · `player-legislation` · status: **sourced**

Players author, propose, and vote on rules that the game then enforces inside a shared world, such as taxes, bans, and permits.

| field | value |
|---|---|
| aliases | player government, player-made laws |
| family | Governance & policy |
| substrate | Player-authored logic, Rule system |
| math basis | Mechanism design / auctions, Computation theory, Game theory |
| feedback | Both |
| player interface | Programming, Choice / cards, Language |
| legibility | 3 |
| emergence potential | 4 |
| authoring cost | 1 |
| compute cost | 1 |
| tuning difficulty | 4 |
| ai leverage | 4 |
| maturity | Established |
| core count *(computed)* | 2 |
| earliest game *(computed)* | [A Tale in the Desert](../game/a-tale-in-the-desert.md) |
| earliest year *(computed)* | 2003 |
| prevalence *(computed)* | 2 |
| prevalence share *(computed)* | 0.011 |
| subgenre spread *(computed)* | 1 |
| technique count *(computed)* | 3 |
| technique exposure *(computed)* | 1.0 |

## Definition

Owns a set of player-authored laws, each a condition and an effect expressed in a structured rule language (for example: when a player fells a tree in district X, charge a tax or block the action), a proposal and voting procedure, and an enforcement hook that checks every relevant action against the active laws. A law passes when its vote meets the threshold set by the world's constitution or government type, after which the simulation enforces it automatically. Eco (early access 2018) lets players form governments and propose and vote on laws that restrict what other players can do or apply taxes and grants to specific actions, to manage an ecosystem that overharvest and pollution can damage. A Tale in the Desert (2003) let players petition and vote on laws that the developers then implemented.

## Player Experience

Politics with real teeth. Players argue about what should be allowed, draft rules, lobby for votes, and then live under the result. A logging ban or a carbon tax becomes a social contract that some players obey, some evade, and some campaign to repeal.

## Design Levers

- expressiveness of the rule language (which triggers, conditions, and effects are available)
- voting thresholds, quorum, and who can propose
- constitutional limits on what laws may do
- enforcement mode: hard blocks, automatic fines, or reports for players to act on
- how government offices are filled and how long laws persist

## Failure Modes

- A small active group can pass laws that grief or exclude other players.
- A rule language too limited to express what players want pushes politics into informal agreements the game cannot enforce.
- Low participation makes votes meaningless, and governance becomes the hobby of a few players.

## Dynamics

- Ecological or economic crises create pressure for regulation, and regulation shifts which professions are profitable.
- Laws generate evasion strategies and loophole-seeking, which prompts amendments.
- Factions form around legislative interests, producing persistent political rivalries.

## Open Questions

- Can LLMs compile natural-language laws into enforceable rules faithfully enough that players trust the translation?
- What constitutional constraints prevent minority capture without making legislation toothless?

## Relations

**synergy**

- [Player organizations](../mechanic/player-organizations.md): Organized player groups are the constituencies that write and enforce laws.

## Backlinks (computed)

**affected by:** [Automated generation of game rules and mechanics](../technique/automated-rule-generation.md), [Grammar-constrained decoding for valid game actions](../technique/constrained-decoding.md), [Many-agent LLM societies](../technique/llm-agent-societies.md)

**involved in:** [Natural-language legislation](../opportunity/natural-language-legislation.md)

**used by:** [A Tale in the Desert](../game/a-tale-in-the-desert.md), [Eco](../game/eco.md)

## Sources

- [Eco (2018 video game)](../source/src-wikipedia-eco-2018.md)

---
Provenance: created in run `2026-10-24-taxonomy-m2`; reviewed in `2026-10-24-review-fixes`.
