# Autonomy levels

*Mechanic* · `autonomy-levels` · status: **sourced**

The degree to which agents act on their own is adjustable, from full free will to explicit commands only.

| field | value |
|---|---|
| aliases | free will setting, autonomy slider |
| family | Agents & behavior |
| substrate | Agent-based, Rule system |
| math basis | Utility / decision theory |
| feedback | None |
| player interface | Parameter, Orders |
| legibility | 4 |
| emergence potential | 2 |
| authoring cost | 1 |
| compute cost | 1 |
| tuning difficulty | 2 |
| ai leverage | 3 |
| maturity | Established |
| core count *(computed)* | 0 |
| earliest game *(computed)* | [The Sims](../game/the-sims.md) |
| earliest year *(computed)* | 2000 |
| prevalence *(computed)* | 3 |
| prevalence share *(computed)* | 0.017 |
| subgenre spread *(computed)* | 2 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

Owns a global, per-agent, or per-category autonomy setting that gates which actions an agent may select for itself. Each decision cycle the setting filters or reweights the candidate set before action selection: at full autonomy the agent chooses among all actions; at reduced levels only urgent self-care or specific categories remain; at zero the agent idles until ordered. Player orders always take precedence while queued. The Sims (2000) exposes free will as an option, and even with it on, Sims need orders to pay bills, find jobs, exercise, or conceive. RimWorld's drafting switches a colonist from self-assigned work to direct control for combat or emergencies. Inputs: the setting, the order queue, urgency of needs. Outputs: the share of agent time under player versus agent control.

## Player Experience

Lets the player choose how much to micromanage. High autonomy turns play into arranging and watching; low autonomy turns it into puppetry with responsibility for every need. Players switch per situation: autonomy for routine life, manual control for crises and set pieces.

## Design Levers

- number of levels and whether the setting is global, per agent, or per action category
- which actions stay autonomous at each level (survival needs, social, self-care)
- override rules when player orders conflict with urgent needs
- quality of autonomous choices (competent versus deliberately flawed agents)

## Failure Modes

- Autonomous choices are worse than the player's, so players turn autonomy off and drown in micromanagement.
- Autonomy that is too competent removes the player's role and turns the game into a screensaver.
- Agents override intent at bad moments, such as wandering off mid-task, which reads as disobedience rather than personality.
- Unclear boundaries between autonomous and ordered actions make failures hard to attribute.

## Dynamics

- Players run mixed teams of puppets and free agents, adjusting per character and per crisis.
- Low-autonomy play exposes needs systems as chores, while high-autonomy play exposes utility-scoring quirks as personality.
- With permadeath, the choice to delegate during danger (drafting colonists for a raid) becomes a risk decision.

## Open Questions

- Can language-model agents accept intent-level delegation (keep the house running during the party) as a richer replacement for discrete autonomy levels?
- Do players attach more strongly to agents they control or to agents they watch, and which autonomy setting maximizes attachment?

## Relations

**tension**

- [Unit commands](../mechanic/unit-commands.md): Agents with strong free will resist direct commands; designers must decide who is in charge.

## Backlinks (computed)

**used by:** [RimWorld](../game/rimworld.md), [The Sims](../game/the-sims.md), [The Sims 4](../game/the-sims-4.md)

## Sources

- [The Sims (video game)](../source/src-wikipedia-the-sims.md)

---
Provenance: created in run `2026-10-24-taxonomy-m3`.
