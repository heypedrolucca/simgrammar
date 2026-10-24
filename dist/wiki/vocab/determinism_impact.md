# Vocabulary: determinism_impact

Effect on reproducibility, replays, lockstep multiplayer, and save integrity when used at runtime.

| id | label | definition |
|---|---|---|
| `preserves` | Preserves | Deterministic given seed and inputs, or used only offline. |
| `mitigable` | Mitigable | Non-deterministic but can be made reproducible via caching, logging outputs, or fixed seeds. |
| `breaks` | Breaks | Outputs cannot be reproduced reliably; replays and lockstep sync require recording the outputs themselves. |
