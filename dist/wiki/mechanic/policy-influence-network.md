# Policy influence network

*Mechanic* · `policy-influence-network` · status: **sourced**

Policies, indicators, and voter groups connect through a weighted causal graph with delays.

| field | value |
|---|---|
| aliases | Democracy-style simulation, policy web, effects graph |
| family | Governance & policy |
| substrate | Network / graph, Aggregate stocks |
| math basis | System dynamics / ODEs, Machine learning, Social network models |
| feedback | Both |
| player interface | Parameter, Observation only |
| legibility | 3 |
| emergence potential | 3 |
| authoring cost | 3 |
| compute cost | 1 |
| tuning difficulty | 4 |
| ai leverage | 4 |
| maturity | Emerging |
| requires | [Policy toggles](../mechanic/policy-toggles.md) |
| core count *(computed)* | 1 |
| earliest game *(computed)* | [Democracy 4](../game/democracy-4.md) |
| earliest year *(computed)* | 2020 |
| prevalence *(computed)* | 1 |
| prevalence share *(computed)* | 0.006 |
| subgenre spread *(computed)* | 1 |
| technique count *(computed)* | 1 |
| technique exposure *(computed)* | 0.25 |

## Definition

Owns a directed graph whose nodes are policies (with slider levels), simulation values (crime, GDP, pollution), situations, and voter groups, and whose edges are weighted effect equations. Each turn every node's value is recomputed as a function of its weighted inputs, bounded to a fixed range, and effects can be lagged or averaged over several turns; situations switch on and off when their input values cross thresholds. Voter-group happiness at the end of the chain sets approval and election results. Positech's Democracy series (2005-2022) is the canonical form: its designer describes it as a homebrew neural network in which voters, voter groups, policies, ministers, and events are neurons capped to 0..1 or -1..+1, with most logic in editable CSV files. Democracy 4 added fixed-income neurons that can exceed 1 because percentage effects on a 0-1 income scale gave wealthy voters more than poor ones.

## Player Experience

Pulling one thread and watching the web move. The player hovers a policy to see lines to everything it touches, raises a tax and sees the deficit shrink while a voter group sours, and plans reforms in sequence because effects arrive with delays.

## Design Levers

- graph density: how many effects each policy and value has
- effect equation forms (linear, power, threshold) and weights
- delays and averaging per edge
- value bounds and normalization
- situation trigger and clear thresholds with hysteresis
- how much of the graph is shown to the player

## Failure Modes

- Percentage effects on bounded values distort distribution, the problem that led Democracy 4 to add fixed-income values.
- Dense graphs with small weights make most policies feel inert while a few dominate.
- Long delays without visible pending effects make players misattribute causes.

## Dynamics

- Feedback loops between values (unemployment, crime, GDP) produce virtuous or vicious cycles across several turns.
- Situations appear and vanish as values cross thresholds, creating emergent crises from slow drifts.
- Overlapping voter-group memberships turn every policy into a tradeoff among coalitions.

## Open Questions

- Could learned causal models fit to real policy data replace hand-authored effect equations, and would players accept the loss of authored intent?
- Can an LLM generate new policies and situations with consistent graph effects from a text description?

## Relations

**requires**

- [Policy toggles](../mechanic/policy-toggles.md)

## Backlinks (computed)

**affected by:** [Many-agent LLM societies](../technique/llm-agent-societies.md)

**used by:** [Democracy 4](../game/democracy-4.md)

## Sources

- [Democracy 4: the fixed income rewrite](../source/src-harris-2020-democracy4-fixed-income.md)
- [Democracy 4](../source/src-wikipedia-democracy-4.md)

---
Provenance: created in run `2026-10-24-taxonomy-m2`.
