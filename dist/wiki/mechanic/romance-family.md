# Romance and family

*Mechanic* · `romance-family` · status: **sourced**

Agents court, partner, marry, and form families according to compatibility and relationship state.

| field | value |
|---|---|
| aliases | courtship and marriage, dating, family formation |
| family | Social relations |
| substrate | Agent-based, Rule system, Stochastic events |
| math basis | Social network models, Markov / stochastic processes |
| feedback | Reinforcing (positive) |
| player interface | Choice / cards, Observation only |
| legibility | 4 |
| emergence potential | 4 |
| authoring cost | 3 |
| compute cost | 1 |
| tuning difficulty | 3 |
| ai leverage | 4 |
| maturity | Classic |
| requires | [Relationship values](../mechanic/relationship-values.md) |
| core count *(computed)* | 1 |
| earliest game *(computed)* | [Harvest Moon](../game/harvest-moon.md) |
| earliest year *(computed)* | 1996 |
| prevalence *(computed)* | 11 |
| prevalence share *(computed)* | 0.063 |
| subgenre spread *(computed)* | 4 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

Owns relationship-status edges (crush, lover, fiance, spouse, ex) and family links (parent, child, sibling) plus the rules that move pairs between statuses. Attempts such as flirting, proposals, and breakups succeed with probabilities from attraction, opinion, age, traits, and existing commitments; partnered pairs gain bonuses and can produce children, linking to lifecycle and inheritance. RimWorld pawns over 16 can attempt romance every 12 days; success depends on beauty (Ugly x0.3, Pretty x2.3), relative age, and existing relationships; a rebuff gives -10 and -15 opinion; lover is +35, spouse +30, ex -15, breakup -50, and kin get base opinions such as parent +30. Stardew Valley has 12 marriage candidates courted through a heart-based friendship meter (250 points per heart). Crusader Kings III makes marriage a political act that links dynasties. Inputs: relationship values, traits, ages. Outputs: couples, households, children, grief, jealousy.

## Player Experience

Romance gives characters personal goals and the player a matchmaking game. Players engineer meetings, celebrate weddings, and deal with affairs and breakups; children turn a run into a family saga.

## Design Levers

- attraction model (traits, beauty, orientation, compatibility) and attempt cooldowns
- status ladder and requirements for each step
- jealousy, cheating, and breakup rules
- whether relationships are player-directed, autonomous, or both
- fertility and household formation rules that link to lifecycle

## Failure Modes

- Romance spam: compatible agents pair off immediately and the system stops generating story.
- Autonomous affairs and breakups wreck carefully built families, which feels like the game punishing the player.
- Narrow attraction rules repeat the same few pairings every run.
- Ignoring orientation or consent in autonomous romance produces behavior that players report as harmful.

## Dynamics

- Couples anchor households and change migration, mood, and grief networks.
- Love triangles and rivals produce recurring social conflicts and fights.
- In dynastic games, marriage creates alliance and inheritance claims across factions.

## Open Questions

- Can language-model characters carry courtship as dialogue with consistent preferences, and how should that be constrained for safety and consent?
- What autonomy level for romance maximizes story without making players feel they lost control of their families?

## Relations

**requires**

- [Relationship values](../mechanic/relationship-values.md)

## Backlinks (computed)

**involved in:** [Factories with a living workforce](../opportunity/living-workforce-factories.md)

**used by:** [Banished](../game/banished.md), [Crusader Kings III](../game/crusader-kings-3.md), [Harvest Moon](../game/harvest-moon.md), [inZOI](../game/inzoi.md), [Paralives](../game/paralives.md), [Stardew Valley](../game/stardew-valley.md), [The Sims](../game/the-sims.md), [The Sims 2](../game/the-sims-2.md), [The Sims 3](../game/the-sims-3.md), [The Sims 4](../game/the-sims-4.md), [Tomodachi Life](../game/tomodachi-life.md)

## Sources

- [Social](../source/src-rimworldwiki-2026-social.md)
- [Stardew Valley](../source/src-wikipedia-stardew-valley.md)
- [Friendship](../source/src-stardewwiki-2026-friendship.md)

---
Provenance: created in run `2026-10-24-taxonomy-m3`.
