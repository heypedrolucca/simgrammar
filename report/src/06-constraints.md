## 6. Five ceilings

Simulation design has been shaped less by imagination than by five constraints. Each one explains a family of conventions, and each one is the target of a different group of techniques in §7.

### 6.1 Compute per tick

A consumer machine must advance the whole simulation many times per second while rendering it. The constraint explains why city builders simulate aggregate populations with a sample of visible agents, why per-particle material simulation ([[falling-sand-materials]], [[fluid-gas-simulation]]) appears in 2D or small arenas, why late-game slowdown is a genre-wide complaint, and why [[agent-pathfinding]] and [[traffic-congestion]] are the usual bottlenecks. Mechanics scored 4 or 5 on compute cost are the ones whose scale is capped by hardware rather than design.

**Relaxed by:** GPU-parallel and accelerated simulation, learned surrogates for physics and weather, mean-field approximations for large populations, and inference-efficient models for agent decisions.

### 6.2 Authoring cost

Every unit of variety in some mechanics must be made by hand: an animation for each interaction, a line of dialogue for each social exchange, an event for each situation, an asset for each catalog entry. Mechanics with high authoring cost are capped by budgets, and players exhaust them; this is why event decks repeat, why villagers recycle requests, and why social systems in rule-based games read as formulaic. Across mechanics, authoring cost and judged AI leverage have a Spearman correlation of {{stat:rho_authoring_cost_ai_leverage}} (p {{stat:p_authoring_cost_ai_leverage}}): the mechanics most limited by content budgets are, on expert judgment, the ones most open to generative techniques.{{assert:rho_authoring_cost_ai_leverage > 0.2}}

**Relaxed by:** constrained language generation for events and dialogue, text-to-3D and neural rendering for assets, learned motion for animation, and procedural generation with learned priors.

### 6.3 Legibility

Players must form a working model of why the simulation did what it did, or they experience the depth as randomness. Rubric scores show the tension directly: across mechanics, legibility and emergence potential correlate at {{stat:rho_legibility_emergence_potential}} (p {{stat:p_legibility_emergence_potential}}). The mechanics that generate the most unscripted variety are the hardest to understand.{{assert:rho_legibility_emergence_potential < -0.2}}

{{figure:legibility-vs-emergence}}

Designers have answered with a whole family of mechanics that own no simulation state ([[data-overlays]], [[causal-tooltips]], [[agent-inspection]], [[history-chronicle]]). Legibility, not compute, is often the binding constraint on how much coupling a commercial game can afford.

**Relaxed by:** language models that read state and event logs and explain causes, forecasting by simulating futures, and learned surrogates that make expensive hidden fields cheap to visualize.

### 6.4 Determinism

Replays, lockstep multiplayer, bug reproduction, competitive leaderboards, and save integrity require that the same inputs produce the same state. [[factorio]]'s multiplayer depends on it. Determinism has kept stochastic or learned components out of authoritative game state, and it is the constraint that most runtime AI techniques violate: of the {{count:technique}} techniques here, {{stat:n_technique_breaks_determinism}} break reproducibility outright when used at runtime (see `determinism_impact`).

**Relaxed by:** recording model outputs as events so replays read the log rather than re-call the model, splitting authoritative symbolic state from non-authoritative generated presentation, and constrained decoding that maps open-ended outputs into typed, validated state changes.

### 6.5 Believability of agents

Rule-driven agents are legible and cheap but shallow: their utilities are visible formulas and their speech is canned. The constraint shapes the genre's preference for many shallow agents ([[crowd-preferences]]) or few agents with thick systemic state ([[memories-thoughts]], [[injury-body-model]]) over agents with rich minds.

**Relaxed by:** language-model agents with memory and reflection, models trained to predict human choices, and small local models that make per-agent language affordable.

### 6.6 What the ceilings imply

The five constraints do not move together. Compute and authoring cost are being relaxed fastest, with techniques already shipped. Agent believability is being relaxed at a new cost in determinism and legibility. Legibility is the constraint most worth attacking deliberately, because a deeper simulation is worthless if no one can read it, and it is also where the techniques are most mature relative to their use: explanation over structured state is an application of capabilities that already exist.
