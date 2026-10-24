## 10. Risks and open problems

The opportunities in §9 inherit the risks of their techniques. Each technique records its primary risks from a closed vocabulary:

{{table:techniques-by-risk}}

**Consistency.** Language and world models contradict state, forget, and drift. In a simulation game a contradiction is worse than a gap, because players use the simulation's outputs to build mental models. Constrained decoding, typed write-back, and grounding every generated claim in logged state are necessary; none is sufficient for open-ended generation.

**Determinism.** Runtime generation breaks replays, lockstep multiplayer, and bug reproduction unless outputs are recorded and replayed as events. Games that already depend on determinism (competitive leaderboards, large multiplayer factories) should treat model outputs as inputs from an external system, logged at the boundary.

**Cost.** Per-player-hour inference conflicts with one-time purchases and with how long simulation players play. Local models, salience gating, and caching bound cost; frame-generating world models remain far from affordable at the session lengths simulation games require (§7.2).

**Legibility of learned systems.** A learned policy or generated rule can be as opaque as the simulation it replaced. Every learned component that affects state needs an explanation path, or it moves a mechanic down the legibility scale in §5.6.

**Evaluation.** Open-ended outputs are hard to QA. Automated playtesting checks validity and balance, not quality; human evaluation does not scale to generated variety. Simulation games need evaluation methods for generated content analogous to the verification queue in this dataset: sampled, scored against anchors, and logged.

**Player trust and labor.** Reception of generative features has been mixed, and developers' view of generative AI's effect on the industry has turned more negative while reported use held steady (§7.2). Disclosure rules on the largest PC store already distinguish pre-generated from live-generated content [@src-valve-2026-steamworks-content-survey]. Opportunities that make games more legible or let players author more (explanation, modding by description, intent-level orders) are less exposed to this risk than those that replace authored work.

**Safety and provenance.** Live generation in social simulations needs content guardrails, especially where players can steer characters with language. Asset generation carries training-data and likeness questions. These risks are recorded per technique so they can be filtered and tracked.

**Open research problems** recorded on mechanic and technique pages include: grounding generated explanations in simulation logs with measurable faithfulness; conservation guarantees for learned physics; semantic fidelity for neural rendering of symbolic state; inferring needs and preferences from behavior instead of declaring them; and fair, inspectable AI participants in player economies.
