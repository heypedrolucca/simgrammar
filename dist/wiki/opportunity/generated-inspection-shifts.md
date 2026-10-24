# Generated inspection shifts

*Opportunity* · `generated-inspection-shifts` · status: **asserted**

Rule-checking job sims with generated documents, items, and rule changes each shift, verified against an answer key so infinite variety stays fair.

| field | value |
|---|---|
| opportunity type | Mechanic upgrade |
| involves | [Rule-checking inspection](../mechanic/rule-checking-inspection.md), [Contracts and orders](../mechanic/contracts-orders.md), [Dilemma cards](../mechanic/dilemma-cards.md), [Procedural characters](../mechanic/procedural-characters.md) |
| applies | [Grammar-constrained decoding for valid game actions](../technique/constrained-decoding.md), [LLM game master and narrative director](../technique/llm-game-master.md), [Automated generation of game rules and mechanics](../technique/automated-rule-generation.md) |
| precedent | [Papers, Please](../game/papers-please.md), [Contraband Police](../game/contraband-police.md) |
| novelty | 3 |
| feasibility | 5 |
| impact | 2 |
| horizon | Now |
| key risks | Generated text leaks the answer or contradicts the formal case., Repetitive tone across generated applicants. |
| falsifiable signal | {'prediction': 'A released inspection or bureaucracy job sim will use runtime generation of documents or applicants with a rule-derived answer key.', 'resolve_by': '2027-12-31', 'criteria': 'Store page or developer statement describing generated cases scored against formal rules.'} |
| priority *(computed)* | 2.989 |

## Thesis

Papers, Please and its successors are limited by hand-built document sets that players memorize. Constrained generation can produce documents, forgeries, and edge cases from a formal rule set, and because the rules are formal, every generated case has a computable correct answer. That combination gives endless fair variety, which ordinary procedural generation struggles to make interesting and unconstrained generation cannot make fair.

## Design Sketch

Each day introduces rule changes written as formal predicates and rendered as in-world memos. Applicants, documents, and stories are generated to exercise boundary cases of the current rules. The game knows the correct ruling for every case and scores accordingly.

## Key Risks

- Generated text leaks the answer or contradicts the formal case.
- Repetitive tone across generated applicants.

## Validation Experiment

Generate 1,000 inspection cases from a 30-predicate rule set and have a checker and two humans verify the answer key on a sample of 200. Success: 99 percent agreement between generated answers and human rulings.

## Falsifiable signal

- **Prediction:** A released inspection or bureaucracy job sim will use runtime generation of documents or applicants with a rule-derived answer key.
- **Resolve by:** 2027-12-31
- **Criteria:** Store page or developer statement describing generated cases scored against formal rules.

## Relations

**applies**

- [Grammar-constrained decoding for valid game actions](../technique/constrained-decoding.md)
- [LLM game master and narrative director](../technique/llm-game-master.md)
- [Automated generation of game rules and mechanics](../technique/automated-rule-generation.md)

**involves**

- [Rule-checking inspection](../mechanic/rule-checking-inspection.md)
- [Contracts and orders](../mechanic/contracts-orders.md)
- [Dilemma cards](../mechanic/dilemma-cards.md)
- [Procedural characters](../mechanic/procedural-characters.md)

**precedent**

- [Papers, Please](../game/papers-please.md)
- [Contraband Police](../game/contraband-police.md)

---
Provenance: created in run `2026-10-24-synthesis`.
