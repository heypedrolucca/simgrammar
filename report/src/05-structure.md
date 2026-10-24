## 5. The structure of the design space

### 5.1 What games are made of

The average catalog game uses {{stat:mean_mechanics_per_game}} mechanics (median {{stat:median_mechanics_per_game}}). The most widely used is {{stat:most_prevalent_mechanic}}, present in {{stat:most_prevalent_mechanic_share_pct}} percent of games. The head of the distribution is a set of general-purpose mechanics that appear across subgenres: progression structures, placement, production, skills, avatars, and modding.

{{table:top-mechanics}}

### 5.2 How the vocabulary grew

{{figure:mechanic-accumulation}}

{{assert:pct_mechanics_seen_by_2000 >= 60}}{{stat:pct_mechanics_seen_by_2000}} percent of mechanics appear in at least one catalog game released by 2000. The 1980s and 1990s supplied most of the vocabulary: [[simcity-1989]] (zoning, land value, overlays, disasters), [[populous]] (terraforming as a god power), [[railroad-tycoon]] and [[transport-tycoon]] (route scheduling and competitors), [[theme-park]] and [[theme-hospital]] (crowds with preferences, queues, diagnosis), [[creatures]] (learning creatures and genetics), and [[the-sims]] at the boundary (smart objects). Later decades mostly recombined, deepened, and scaled existing mechanics; the additions after 2010 are concentrated in material simulation, programmable automation, and runtime language.

{{table:mechanic-origins-by-decade}}

The dataset is a sample, so these are lower bounds on origin dates, and the pattern partly reflects which early games are canonical. It is still consistent with a familiar view among designers: the genre's grammar was established early and has since been extended mainly in depth and scale.

### 5.3 Which mechanics travel together

Co-occurrence lift measures how much more often two mechanics share a game than independence predicts. The strongest pairs are tight design packages, many of them inherited from one lineage: the SimCity core of zoning, land value, demand, and traffic; the virtual-pet pair of care and learning; social exchanges with smart objects; diagnosis with queues.

{{table:cooccurrence-top}}

{{stat:pair_coverage_pct}} percent of possible mechanic pairs co-occur in at least one game. Most of the combinatorial space has never been tried, which is the subject of §5.5.

### 5.4 Families of games by what they use

Clustering games by the mechanics they use (ignoring their labels) produces {{stat:n_clusters}} clusters, {{stat:n_clusters_cross_subgenre}} of which mix subgenres.{{assert:n_clusters_cross_subgenre >= 7}} The clusters read as design families rather than market categories:

{{table:game-clusters}}

Several groupings are informative. Life sims, colony sims, and virtual pets share a cluster built on personality, needs, and relationships: [[the-sims]], [[rimworld]], [[dwarf-fortress]], and [[creatures]] are all games about minds.{{assert:derived.rimworld.cluster == derived.the-sims.cluster}}{{assert:derived.dwarf-fortress.cluster == derived.the-sims.cluster}}{{assert:derived.creatures.cluster == derived.the-sims.cluster}} Physics sandboxes, construction games, programming puzzles, and hands-on job sims such as [[powerwash-simulator]] and [[pc-building-simulator]] cluster around modular assembly and physical manipulation: they are build-or-fix-then-test games.{{assert:derived.powerwash-simulator.cluster == derived.besiege.cluster}}{{assert:derived.spacechem.cluster == derived.besiege.cluster}} Vehicle and flight sims form a separate cluster around embodied skill and weather.{{assert:derived.iracing.cluster == derived.x-plane.cluster}}{{assert:derived.iracing.cluster != derived.besiege.cluster}} City builders, factory games, and grand strategy share the largest cluster, organized by production chains and tech trees: [[factorio]], [[anno-1800]], and [[europa-universalis-4]] are all planning economies.{{assert:derived.factorio.cluster == derived.anno-1800.cluster}}{{assert:derived.factorio.cluster == derived.europa-universalis-4.cluster}} The SimCity lineage stands apart on zoning, land value, and traffic.{{assert:derived.simcity-1989.cluster == derived.cities-skylines.cluster}}{{assert:derived.simcity-1989.cluster != derived.anno-1800.cluster}} Inspection and dilemma games ([[papers-please]], [[reigns]], [[suzerain]], [[this-war-of-mine]]) cluster on authored event structures despite belonging to different subgenres.{{assert:derived.papers-please.cluster == derived.reigns.cluster}} The AI-native titles form their own cluster around generated content and natural-language interaction, separate from the life sims they superficially resemble.{{assert:derived.ai-dungeon.cluster != derived.inzoi.cluster}}{{assert:derived.ai-dungeon.cluster == derived.infinite-craft.cluster}}

These families correspond to the six-layer profiles in §4.1: the minds family invests in agents and social coupling; the builders in control and continuous substrate; the operators in direct control and physics; the planners in stocks, networks, and legibility.

### 5.5 White space

Some mechanics are individually common but rarely combined. The table lists pairs where each mechanic appears in at least eight percent of games, the two belong to different families, they are not recorded as being in design tension, and they co-occur at most once.

{{table:whitespace}}

Not every gap is an opportunity; some pairs are absent because they do not fit. But several gaps point at specific underexplored designs: production chains whose workers age, form families, and are replaced (factory games are almost entirely populated by machines or faceless workers); research trees driven by relationships between named scientists; building placement that triggers authored or generated story events; power grids coupled to weather. Section 9 develops these as opportunities.

### 5.6 The legibility frontier

Across all mechanics, legibility and emergence potential are negatively correlated (Spearman ρ = {{stat:rho_legibility_emergence_potential}}, p {{stat:p_legibility_emergence_potential}}), and emergence potential is strongly correlated with tuning difficulty (ρ = {{stat:rho_emergence_potential_tuning_difficulty}}, p {{stat:p_emergence_potential_tuning_difficulty}}). Mechanics that generate unscripted variety are harder to understand and harder to balance.{{assert:rho_legibility_emergence_potential < -0.2}}{{assert:rho_emergence_potential_tuning_difficulty > 0.2}}{{assert:rho_legibility_compute_cost < 0}} Legibility also falls as compute cost rises (ρ = {{stat:rho_legibility_compute_cost}}, p {{stat:p_legibility_compute_cost}}): expensive simulation tends to be hidden simulation.

These scores are expert judgments, so the correlations measure the structure of design knowledge rather than a property measured in players. They nevertheless agree with a constraint every simulation designer reports: depth, legibility, and balance cannot all be maximized with rules alone.
