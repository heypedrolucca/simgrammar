# Material interactions

*Mechanic* · `material-interactions` · status: **sourced**

A rule table defines how elements such as fire, water, and electricity change materials and each other on contact.

| field | value |
|---|---|
| aliases | chemistry engine, elemental interactions, systemic elements |
| family | Physics & materials |
| substrate | Rule system, Cellular grid, Agent-based |
| math basis | Combinatorics, Cellular automata |
| feedback | Both |
| player interface | Direct manipulation |
| legibility | 4 |
| emergence potential | 4 |
| authoring cost | 2 |
| compute cost | 2 |
| tuning difficulty | 3 |
| ai leverage | 4 |
| maturity | Established |
| core count *(computed)* | 4 |
| earliest game *(computed)* | [The Incredible Machine](../game/the-incredible-machine.md) |
| earliest year *(computed)* | 1993 |
| prevalence *(computed)* | 8 |
| prevalence share *(computed)* | 0.046 |
| subgenre spread *(computed)* | 5 |
| technique count *(computed)* | 2 |
| technique exposure *(computed)* | 0.938 |

## Definition

Entities carry material tags (wood, metal, grass) and element states (burning, wet, frozen, electrified). A rule table maps element-material and element-element pairs to state changes applied on contact or within an area each tick. In The Legend of Zelda: Breath of the Wild, Takuhiro Dohta described a chemistry engine beside the physics engine: physics is a rule-based movement calculator and chemistry a rule-based state calculator. Elements (fire, water, ice, electricity, wind) change the states of materials and of each other, and materials do not change each other. Divinity: Original Sin uses surfaces where oil burns and water conducts lightning. Outputs are state changes that trigger damage, movement, and new elements.

## Player Experience

Asking "what if" and having the world answer consistently. Players combine elements for creative solutions in puzzles and fights, and the satisfaction is in solutions that feel discovered rather than designed.

## Design Levers

- number of elements and material tags
- density of the interaction table: which pairs react
- propagation: contact, area, or spread rate over time
- duration and decay of states
- how closely rules follow real-world intuition
- how strongly reactions are telegraphed visually

## Failure Modes

- An interaction that works in one place but not another breaks trust in the whole system.
- Combinatorial growth of pairs produces untested reactions and bugs.
- One reaction combo dominates combat and flattens choice.
- Authored puzzles with single intended solutions conflict with systemic shortcuts.

## Dynamics

- Chained reactions, such as fire on grass creating an updraft for gliding in Breath of the Wild.
- Environmental kills and accidents emerge from mixing combat with terrain and weather.
- Players find puzzle solutions designers did not plan.

## Open Questions

- Can a language model judge interactions for arbitrary pairs of materials at runtime while staying consistent across a session?
- What is the smallest rule table that still produces chains players experience as emergent?

## Backlinks (computed)

**affected by:** [Graph network simulators and neural operators](../technique/graph-network-simulators.md), [LLM-adjudicated state transitions (LLM as game mechanic)](../technique/llm-rule-adjudication.md)

**used by:** [Besiege](../game/besiege.md), [Caves of Qud](../game/caves-of-qud.md), [From Dust](../game/from-dust.md), [Noita](../game/noita.md), [Teardown](../game/teardown.md), [The Incredible Machine](../game/the-incredible-machine.md), [The Powder Toy](../game/the-powder-toy.md), [The Legend of Zelda: Breath of the Wild](../game/zelda-breath-of-the-wild.md)

## Sources

- [Change and Constant: Breaking Conventions with 'The Legend of Zelda: Breath of the Wild'](../source/src-fujibayashi-2017-botw-change-and-constant.md)
- [Breath of the Wild, science, and clever little lies](../source/src-thumbsticks-2017-botw-chemistry.md)
- [The Legend of Zelda: Breath of the Wild](../source/src-wikipedia-zelda-breath-of-the-wild.md)

---
Provenance: created in run `2026-10-24-taxonomy-m4`.
