## 8. Where the techniques land

### 8.1 How techniques change mechanics

Each `affects` edge records one of seven effects. Across {{stat:n_affects_edges}} edges the most common effect is *deepens* ({{stat:n_effect_deepens}} edges): the technique makes an existing mechanic richer, larger, or more varied without changing its role.{{assert:top_effect == Deepens}} Explanation is the rarest effect ({{stat:n_effect_explains}} edges){{assert:rarest_effect == Explains}}, although §6 argued that legibility is often the binding constraint on simulation depth.

{{table:effect-distribution}}

The imbalance is a finding about where research effort points. Generating content and replacing substrates (rule-based behavior with language models, numerical physics with learned dynamics) attract most work; explaining a simulation to the person playing it attracts little, even though the techniques it needs (retrieval over structured logs, constrained generation, summarization) are among the most mature.

### 8.2 Exposure by family

Technique exposure weights each `affects` edge by the technique's maturity in games and by its effect type (weights in `vocab/rubrics.yaml`), then sums over a family's mechanics.

{{figure:exposure-by-family}}

{{table:family-summary}}

Exposure concentrates in four families: narrative and generation, control and automation, agents and behavior, and physics and materials:{{assert:top_exposed_family == Narrative & generation}} the layers where content is expensive to author or where behavior is expensive to compute. It is low across the economic and logistic core of the genre (resources, logistics, economy, population) and lowest of all in operation and procedure.{{assert:least_exposed_family == Operation & procedure}} {{stat:n_mechanics_zero_exposure}} mechanics are affected by no technique in the set, and they account for {{stat:pct_uses_on_zero_exposure}} percent of all game-to-mechanic uses in the catalog. Of the ten most widely used mechanics, {{stat:n_top10_prevalent_zero_exposure}} have no technique attached.

In other words, current AI research mostly targets what a simulation game shows and says, not the rule-systems most simulation games are built from. That is partly sensible (production chains and budgets are cheap and legible already) and partly a gap: the economic core is where balance work, legibility problems, and authoring of recipes and scenarios consume design time.

### 8.3 Most exposed mechanics

{{table:most-exposed-mechanics}}

[[generative-content]] and [[procedural-terrain]] lead because many techniques generate content or worlds. [[utility-action-selection]] is next: language models, planners, and learned policies all offer to replace the hand-written scoring at the center of agent behavior. [[rigid-body-physics]] and [[direct-avatar]] are exposed mainly to frame-generating world models, which replace both with learned prediction and therefore inherit those models' consistency limits.

### 8.4 Judgment versus evidence

Each mechanic carries an expert-judged `ai_leverage` score. It correlates with measured exposure at ρ = {{stat:rho_ai_leverage_exposure}}, so judgment and the technique graph mostly agree.{{assert:rho_ai_leverage_exposure >= 0.3}} The leverage-gap table lists where they disagree: mechanics judged highly open to AI that no technique in the set yet addresses.

{{table:leverage-gap}}

The gap list is a research agenda in its own right. Modding interfaces, blueprints, romance and family systems, creature care, diagnosis, product design, history generation, and rule-checking inspection are each judged ready for substantial change, and none has a technique pointed at it in this dataset.{{assert:derived.modding-api.technique_exposure == 0}}{{assert:derived.blueprints.technique_exposure == 0}}{{assert:derived.history-generation.technique_exposure == 0}}{{assert:derived.rule-checking-inspection.technique_exposure == 0}} Some of these are covered implicitly by general techniques (code generation for modding, language models for romance dialogue); the absence of an explicit, cited result is itself informative.

### 8.5 Authoritative state versus presentation

The techniques divide cleanly by whether they touch authoritative simulation state. Those that only change presentation (neural upscaling and frame generation, restyling, asset generation, motion synthesis) preserve determinism and have shipped. Those that would replace rules or physics with learned prediction remain prototypes or research in games. Language characters sit in between: they have shipped, but as companions and conversation partners at the edge of the simulation, and they belong to the {{stat:n_technique_breaks_determinism}} techniques that break reproducibility outright when used at runtime. The pattern suggests a design principle that recurs through §9: keep the simulation symbolic, typed, and logged, and let learned models read it, explain it, decorate it, and propose changes to it through validated interfaces.
