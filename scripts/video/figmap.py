# picture id "<episode prefix>.<scene>.<block index>" -> figure name in dist/paper/figures (without .svg)
FIG = {
 "01.2.0": "grid", "01.4.0": "grid", "01.5.0": "grid", "01.6.0": "grid:top5", "01.9.0": "viz-layer-profile",
 "02.2.0": "viz-strata", "02.4.0": "viz-strata", "02.5.0": "viz-strata", "02.6.0": "mechanic-accumulation", "02.11.2": "viz-design-map",
 "03.2.0": "viz-design-map", "03.4.0": "viz-design-map", "03.5.0": "viz-design-map", "03.9.0": "viz-design-map", "03.11.2": "viz-design-map",
 "04.4.0": "legibility-vs-emergence", "04.5.0": "legibility-vs-emergence", "04.5.3": "legibility-vs-emergence",
 "05.3.3": "viz-constraint-profile", "05.9.0": "viz-constraint-profile", "05.10.0": "viz-constraint-profile",
 "06.4.0": "viz-technique-landscape", "06.10.0": "viz-technique-landscape", "06.13.0": "viz-technique-landscape",
 "07.4.0": "viz-technique-landscape", "07.7.0": "viz-technique-flows", "07.10.0": "exposure-by-family", "07.11.0": "exposure-by-family", "07.12.0": "exposure-by-family",
 "08.5.0": "viz-vacant-lots", "08.12.0": "viz-vacant-lots",
 "09.2.0": "viz-opportunity-priorities", "09.4.3": "viz-opportunity-priorities", "09.10.0": "viz-opportunity-priorities", "09.11.0": "viz-opportunity-priorities", "09.12.0": "viz-prediction-timeline",
 "10.2.0": "viz-determinism-runtime", "10.4.0": "viz-determinism-runtime",
 "11.1.0": "viz-prediction-timeline", "11.2.0": "viz-prediction-timeline", "11.6.0": "viz-prediction-timeline", "11.11.0": "viz-prediction-timeline",
 "12.2.0": "viz-pipeline", "12.3.0": "viz-vacant-lots", "12.4.0": "viz-pipeline", "12.5.0": "grid", "12.5.3": "viz-design-map", "12.9.0": "grid",
 "th.1.0": "grid", "th.1.2": "grid:top5", "th.1.4": "viz-technique-flows", "th.1.6": "viz-prediction-timeline",
 "th.2.0": "viz-constraint-profile", "th.2.2": "viz-determinism-runtime", "th.3.0": "viz-vacant-lots", "th.3.2": "viz-opportunity-priorities",
}
# extra cards a picture should show, for bets and techniques the narration does not name
CARDS = {
 "09.3.0": [("bet", "bottleneck-explainer")], "09.4.0": [("bet", "bottleneck-explainer")], "09.5.0": [("bet", "causal-why-query")],
 "09.6.0": [("bet", "branch-preview-forecasts")], "11.3.0": [("bet", "causal-why-query")],
}

# shorts: picture id "s<NNN>.<scene>.<block>". Wide figures are unreadable in a vertical frame, so shorts use cards instead.
FIG.update({
 "s001.1.0": "grid:top5", "s001.3.0": "grid:top6",
 "s002.3.0": "viz-strata", "s003.2.0": "viz-design-map", "s004.4.0": "legibility-vs-emergence",
 "s007.2.0": "exposure-by-family", "s007.4.0": "exposure-by-family",
 "s012.1.0": "grid", "s012.2.0": "grid", "s012.3.0": "grid:top5",
})
CARDS.update({
 "s001.4.0": [("game", "rimworld"), ("mechanic", "storyteller-director")],
 "s002.1.0": [("game", "stardew-valley")], "s002.4.0": [("game", "stardew-valley"), ("mechanic", "relationship-values")],
 "s003.3.0": [("game", "papers-please"), ("game", "princess-maker-2")],
 "s004.1.0": [("game", "rimworld")], "s004.2.0": [("mechanic", "adaptive-threat-scaling"), ("mechanic", "raid-defense")],
 "s004.3.0": [("game", "rimworld"), ("mechanic", "raid-defense")],
 "s005.1.0": [("game", "the-sims")], "s005.2.0": [("mechanic", "smart-objects"), ("mechanic", "needs-decay")],
 "s005.3.0": [("mechanic", "smart-objects")], "s005.4.0": [("game", "the-sims"), ("mechanic", "smart-objects")],
 "s006.1.0": [("game", "microsoft-flight-simulator-2020")], "s006.2.0": [("technique", "neural-rendering-shaders")],
 "s006.4.0": [("technique", "genie-world-models")],
 "s007.1.0": [("game", "factorio"), ("mechanic", "production-chain")], "s007.3.0": [("mechanic", "production-chain")],
 "s008.2.0": [("game", "cities-skylines")], "s008.3.0": [("game", "surviving-mars"), ("mechanic", "triggered-event-chains")],
 "s006.3.0": [("technique", "neural-rendering-shaders")],
 "s008.1.0": [("mechanic", "free-placement"), ("mechanic", "triggered-event-chains")],
 "s009.1.0": [("bet", "causal-why-query")], "s009.2.0": [("bet", "causal-why-query")], "s009.3.0": [("bet", "causal-why-query")],
 "s010.3.0": [("technique", "llm-game-master"), ("technique", "monte-carlo-tree-search")],
 "s010.1.0": [("technique", "monte-carlo-tree-search")], "s010.2.0": [("technique", "monte-carlo-tree-search")],
 "s011.2.0": [("bet", "causal-why-query")], "s011.3.0": [("bet", "causal-why-query")],
})
