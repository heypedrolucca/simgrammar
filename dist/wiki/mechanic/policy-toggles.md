# Policy toggles

*Mechanic* · `policy-toggles` · status: **sourced**

Enactable laws or policies change simulation rules with explicit tradeoffs.

| field | value |
|---|---|
| aliases | laws, edicts, civics, ordinances |
| family | Governance & policy |
| substrate | Rule system |
| math basis | Optimization, Utility / decision theory |
| feedback | None |
| player interface | Choice / cards, Parameter |
| legibility | 4 |
| emergence potential | 2 |
| authoring cost | 3 |
| compute cost | 1 |
| tuning difficulty | 3 |
| ai leverage | 3 |
| maturity | Classic |
| core count *(computed)* | 2 |
| earliest game *(computed)* | [Sid Meier's Civilization](../game/civilization.md) |
| earliest year *(computed)* | 1991 |
| prevalence *(computed)* | 15 |
| prevalence share *(computed)* | 0.086 |
| subgenre spread *(computed)* | 5 |
| technique count *(computed)* | 2 |
| technique exposure *(computed)* | 0.6 |

## Definition

Owns a catalog of policies, each with an active flag or a choice among mutually exclusive options in a group, prerequisites, an enactment cost (money, political capital, influence, or time), upkeep, and a cooldown. Enacting a policy applies modifiers or changes rules: it unlocks an action, alters a rate, or changes how agents behave, with a stated benefit and a stated cost. Frostpunk (2018) has a Book of Laws in which similar laws are sequenced so later ones are harsher, and accepting early compromises makes later ones likelier. Victoria 3 groups laws into mutually exclusive sets and, since update 1.3, requires each law to pass three enactment phases whose success chances depend on interest-group support, with up to three setbacks before failure. SimCity 2000 introduced city ordinances, and Civilization civics and Cities: Skylines district policies are other forms.

## Player Experience

Choosing which tradeoff to live with. The player browses a menu of laws, weighs their benefits against costs and side effects, and commits. In Frostpunk each signature feels like a moral line crossed; in grand strategy, passing a law is a political campaign.

## Design Levers

- number of policies and how many can be active at once (slots, groups, budget)
- enactment cost, delay, and cooldown
- size and visibility of side effects
- reversibility: free to revoke, costly, or permanent
- prerequisites and sequencing (escalating law chains)

## Failure Modes

- Policies with no real downside become always-on, leaving a menu of mandatory picks.
- Too many small modifiers make each choice unnoticeable.
- Free revocation lets players toggle policies around events, undermining the tradeoff.

## Dynamics

- Escalating law chains pull players toward harsher policies one reasonable step at a time.
- Policies that change agent behavior ripple into economic and social systems in ways their tooltips do not state.
- Mutually exclusive groups create identity: a society defined by its chosen laws.

## Open Questions

- Could players draft bespoke policies in language and have an LLM translate them into balanced, consistent rule changes?
- Which explanations of second-order policy effects keep surprises interesting rather than unfair?

## Backlinks (computed)

**affected by:** [Automated generation of game rules and mechanics](../technique/automated-rule-generation.md), [Self-play planning with learned models (AlphaZero, MuZero, Dreamer)](../technique/model-based-planning-muzero.md)

**involved in:** [Branch preview of policy futures](../opportunity/branch-preview-forecasts.md), [Explained delegation to AI managers](../opportunity/explained-delegation.md), [Natural-language legislation](../opportunity/natural-language-legislation.md)

**required by:** [Policy influence network](../mechanic/policy-influence-network.md)

**used by:** [Captain of Industry](../game/captain-of-industry.md), [Cities: Skylines](../game/cities-skylines.md), [Sid Meier's Civilization](../game/civilization.md), [Democracy 4](../game/democracy-4.md), [Europa Universalis IV](../game/europa-universalis-4.md), [Frostpunk](../game/frostpunk.md), [Frostpunk 2](../game/frostpunk-2.md), [Hearts of Iron IV](../game/hearts-of-iron-4.md), [Rebel Inc.](../game/rebel-inc.md), [SimCity 2000](../game/simcity-2000.md), [SimCity 4](../game/simcity-4.md), [Stellaris](../game/stellaris.md), [Suzerain](../game/suzerain.md), [Tropico 6](../game/tropico-6.md), [Victoria 3](../game/victoria-3.md)

## Sources

- [Frostpunk](../source/src-wikipedia-frostpunk.md)
- [Victoria 3 Dev Diary #80: Law Enactment and Revolution Clock in 1.3](../source/src-paradox-2023-vic3-law-enactment.md)
- [SimCity 2000](../source/src-wikipedia-simcity-2000.md)

---
Provenance: created in run `2026-10-24-taxonomy-m2`.
