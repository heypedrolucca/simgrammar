## 5. The structure of the design space

### 5.1 What games are made of

The average catalog game uses {{stat:mean_mechanics_per_game}} mechanics (median {{stat:median_mechanics_per_game}}). The most widely used is {{stat:most_prevalent_mechanic}}, present in {{stat:most_prevalent_mechanic_share_pct}} percent of games. The head of the distribution is interface and structure more than simulation: time controls, placement, progression structures (tech trees, scenarios), then production, skills, avatars, and modding.{{assert:derived.variable-speed.prevalence > derived.production-chain.prevalence}}{{assert:derived.free-placement.prevalence > derived.production-chain.prevalence}}{{assert:derived.tech-tree.prevalence > derived.production-chain.prevalence}} The table ranks mechanics across families; §4.2 lists them within each family.

{{table:top-mechanics}}

### 5.2 How the vocabulary grew

{{figure:mechanic-accumulation}}

{{assert:pct_mechanics_seen_by_2000 >= 60}}{{stat:pct_mechanics_seen_by_2000}} percent of mechanics appear in at least one catalog game released by 2000, and {{stat:pct_mechanics_first_seen_1980_1999}} percent first appear in the 1980s or 1990s ({{stat:peak_origin_decade}} the largest decade).{{assert:peak_origin_decade == "1990s"}} The early vocabulary came from a short list of titles: [[simcity-1989]] (zoning, land value, overlays, disasters), [[populous]] (terraforming as a god power), [[railroad-tycoon]] and [[transport-tycoon]] (route scheduling and competitors), [[theme-park]] and [[theme-hospital]] (crowds with preferences, queues, diagnosis), [[creatures]] (learning creatures and genetics), and [[the-sims]] (smart objects).

{{table:mechanic-origins-by-decade}}

{{stat:n_mechanics_since_2010}} mechanics first appear in 2010 or later. They come mainly from four places: factory games (conveyors, request-provider logistics, machine boosting), grand strategy (dynasties, conversion, interest groups), job sims (inspection, repair, surface work), and destructible materials (soft bodies, voxels, terrain deformation).{{assert:derived.conveyor-transport.earliest_year >= 2010}}{{assert:derived.request-provider-logistics.earliest_year >= 2010}}{{assert:derived.dynasty-succession.earliest_year >= 2010}}{{assert:derived.rule-checking-inspection.earliest_year >= 2010}}{{assert:derived.surface-work-tools.earliest_year >= 2010}}{{assert:derived.voxel-destruction.earliest_year >= 2010}}{{assert:derived.soft-body-deformation.earliest_year >= 2010}}

{{table:mechanics-since-2010}}

The dataset is a sample, so these are lower bounds on origin dates, and the pattern partly reflects which early games are canonical.

### 5.3 Which mechanics travel together

Co-occurrence lift measures how much more often two mechanics share a game than independence predicts. The strongest pairs are packages inherited from one lineage: the sports-management trio of match engine, board confidence, and negotiation; the grand-strategy package of war score, territorial control, and conversion; the SimCity core of land value, demand, and traffic; aspirations with smart objects from The Sims; care with learning from virtual pets.{{assert:rank.cooccurrence-top.attribute-match-engine.board-confidence <= 10}}{{assert:rank.cooccurrence-top.culture-religion-conversion.war-score-peace <= 10}}{{assert:rank.cooccurrence-top.land-value.traffic-congestion <= 15}}{{assert:rank.cooccurrence-top.aspiration-wants.smart-objects <= 10}}{{assert:rank.cooccurrence-top.creature-care.creature-learning <= 15}}

{{table:cooccurrence-top}}

{{stat:pair_coverage_pct}} percent of possible mechanic pairs co-occur in at least one game. Most of the combinatorial space is untried, which is the subject of §5.5.

### 5.4 Families of games by what they use

Clustering games by the mechanics they use, ignoring their subgenre labels, produces {{stat:n_clusters}} clusters, {{stat:n_clusters_cross_subgenre}} of which mix subgenres.{{assert:n_clusters_cross_subgenre >= 10}} Each mechanic is weighted by inverse prevalence, so two games sharing a rare mechanic count as closer than two games sharing a pause button.

{{table:game-clusters}}

The clusters read as design families:

- **Minds.** Life sims, colony sims, and agent-driven management share the largest cluster, built on utility action selection, personality, and needs: [[the-sims]], [[rimworld]], [[dwarf-fortress]], [[two-point-hospital]].{{assert:derived.rimworld.cluster == derived.the-sims.cluster}}{{assert:derived.dwarf-fortress.cluster == derived.the-sims.cluster}}{{assert:derived.two-point-hospital.cluster == derived.the-sims.cluster}} Virtual pets and trainable creatures form a separate cluster on care and learning: [[creatures]], [[tamagotchi]], [[black-and-white]].{{assert:derived.creatures.cluster == derived.tamagotchi.cluster}}{{assert:derived.black-and-white.cluster == derived.creatures.cluster}}{{assert:derived.creatures.cluster != derived.the-sims.cluster}}
- **Planned economies.** City builders split into two lineages: production chains and placement ([[anno-1800]], [[factorio]], [[manor-lords]]) and the SimCity line of zoning, land value, and traffic ([[simcity-1989]], [[cities-skylines]]).{{assert:derived.factorio.cluster == derived.anno-1800.cluster}}{{assert:derived.manor-lords.cluster == derived.anno-1800.cluster}}{{assert:derived.simcity-1989.cluster == derived.cities-skylines.cluster}}{{assert:derived.simcity-1989.cluster != derived.anno-1800.cluster}} Grand strategy and political city builders cluster on policy and unrest: [[europa-universalis-4]], [[crusader-kings-3]], [[tropico-6]], [[frostpunk]].{{assert:derived.europa-universalis-4.cluster == derived.crusader-kings-3.cluster}}{{assert:derived.tropico-6.cluster == derived.europa-universalis-4.cluster}}{{assert:derived.frostpunk.cluster == derived.europa-universalis-4.cluster}}{{assert:derived.europa-universalis-4.cluster != derived.anno-1800.cluster}}
- **Build and test.** Physics sandboxes and construction games cluster on rigid bodies and signal circuits: [[besiege]], [[teardown]], [[poly-bridge]].{{assert:derived.teardown.cluster == derived.besiege.cluster}}{{assert:derived.poly-bridge.cluster == derived.besiege.cluster}} Programming puzzles share a cluster with persistent programmable worlds, since both are about systems the player writes and leaves running: [[spacechem]], [[screeps]], [[eve-online]].{{assert:derived.spacechem.cluster == derived.screeps.cluster}}{{assert:derived.eve-online.cluster == derived.screeps.cluster}}
- **Hands-on work.** Job sims form their own cluster on surface tools and contracts, apart from the physics sandboxes: [[powerwash-simulator]], [[car-mechanic-simulator-2021]], [[pc-building-simulator]].{{assert:derived.powerwash-simulator.cluster == derived.pc-building-simulator.cluster}}{{assert:derived.car-mechanic-simulator-2021.cluster == derived.powerwash-simulator.cluster}}{{assert:derived.powerwash-simulator.cluster != derived.besiege.cluster}} Vehicle and flight sims cluster on embodied skill and weather: [[iracing]], [[x-plane]], [[dcs-world]].{{assert:derived.iracing.cluster == derived.x-plane.cluster}}{{assert:derived.dcs-world.cluster == derived.x-plane.cluster}}{{assert:derived.iracing.cluster != derived.besiege.cluster}}
- **Authored decisions.** Inspection and dilemma games cluster on event chains and dilemma cards across subgenres: [[papers-please]], [[reigns]], [[suzerain]], [[this-war-of-mine]].{{assert:derived.papers-please.cluster == derived.reigns.cluster}}{{assert:derived.suzerain.cluster == derived.reigns.cluster}}{{assert:derived.this-war-of-mine.cluster == derived.reigns.cluster}}
- **Turn reports.** The 1970s text sims ([[hamurabi]], [[oregon-trail]], [[lemonade-stand]]) form a cluster on turn structure and random events.{{assert:derived.hamurabi.cluster == derived.oregon-trail.cluster}}{{assert:derived.lemonade-stand.cluster == derived.hamurabi.cluster}}
- **Generated worlds.** The AI-native titles cluster on generated content and natural-language interaction, apart from the life sims they resemble on the surface: [[ai-dungeon]], [[infinite-craft]], [[suck-up]].{{assert:derived.ai-dungeon.cluster == derived.infinite-craft.cluster}}{{assert:derived.suck-up.cluster == derived.ai-dungeon.cluster}}{{assert:derived.ai-dungeon.cluster != derived.inzoi.cluster}}

These families match the layer profiles in §4.1: minds invest in agents and social coupling; planned economies in stocks, networks, and legibility; build-and-test games in control and continuous substrate; hands-on work and vehicle sims in direct control and physics.

### 5.5 White space

Some mechanics are individually common but rarely combined. The table lists pairs where each mechanic appears in at least eight percent of games, the two belong to different families, neither is a time-and-pacing control, they are not recorded as being in design tension, and they co-occur at most once.

{{table:whitespace}}

Some pairs are absent because they do not fit: vehicle sims have no use for free building placement. Others point at specific underexplored designs: building placement that triggers authored or generated story events; production chains whose workers age, form families, and are replaced (factory games are populated by machines or faceless workers); research trees driven by relationships between named scientists; production economies whose layouts players publish and remix.{{assert:rank.whitespace.free-placement.triggered-event-chains <= 10}}{{assert:rank.whitespace.lifecycle-aging.production-chain <= 10}}{{assert:rank.whitespace.relationship-values.tech-tree <= 10}}{{assert:rank.whitespace.content-sharing.production-chain <= 10}}{{assert:rank.whitespace.embodied-skill-control.free-placement <= 10}} Section 9 develops several of these as opportunities.

### 5.6 The legibility frontier

Across all mechanics, legibility and emergence potential are negatively correlated (Spearman ρ = {{stat:rho_legibility_emergence_potential}}, p {{stat:p_legibility_emergence_potential}}), and emergence potential is strongly correlated with tuning difficulty (ρ = {{stat:rho_emergence_potential_tuning_difficulty}}, p {{stat:p_emergence_potential_tuning_difficulty}}). Mechanics that generate unscripted variety are harder to understand and harder to balance.{{assert:rho_legibility_emergence_potential < -0.2}}{{assert:rho_emergence_potential_tuning_difficulty > 0.2}}{{assert:rho_legibility_compute_cost < 0}} Legibility also falls as compute cost rises (ρ = {{stat:rho_legibility_compute_cost}}, p {{stat:p_legibility_compute_cost}}): expensive simulation tends to be hidden simulation.

Two caveats bound these numbers. First, every rubric score was assigned by one model rater (claude-opus-5-5) against written anchors, so the correlations describe that rater's reading of design knowledge, not independent expert agreement or player measurement. Second, mechanics in the legibility and time-and-pacing families sit at the bottom of the emergence scale by construction ({{stat:pct_interface_emergence_1}} percent score 1), since an overlay or a pause button generates nothing on its own; excluding them{{assert:pct_interface_emergence_1 >= 50}} leaves the legibility-emergence correlation at ρ = {{stat:rho_legibility_emergence_potential_excl_interface}}, weaker but the same sign.{{assert:rho_legibility_emergence_potential_excl_interface < 0}}{{assert:rho_legibility_emergence_potential_excl_interface > rho_legibility_emergence_potential}}
