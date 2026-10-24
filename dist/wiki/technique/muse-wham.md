# Muse World and Human Action Model (WHAM)

*Technique* · `muse-wham` · status: **sourced**

Microsoft Research's WHAM is a transformer trained on seven years of Bleeding Edge play that generates both future frames and the player's controller actions, aimed at gameplay ideation, with a real-time Quake II follow-up (WHAMM).

| field | value |
|---|---|
| aliases | Muse, WHAM, WHAMM, World and Human Action Model |
| category | Generative world model |
| year | 2025 |
| maturity | Prototype |
| trl | 6 |
| runtime | Design assist, Server real-time |
| determinism impact | Breaks |
| horizon | 3-5 years |
| risks | Consistency / hallucination, Compute cost, Controllability, Labor displacement, Player trust / reception |
| affects count *(computed)* | 3 |

## Summary

Microsoft Research's WHAM is a transformer trained on seven years of Bleeding Edge play that generates both future frames and the player's controller actions, aimed at gameplay ideation, with a real-time Quake II follow-up (WHAMM).

## Mechanism

Frames are encoded into discrete image tokens and controller inputs into action tokens; a decoder-only transformer models the interleaved sequence, so it predicts both how the world evolves and what a human player is likely to do next. Prompting with a few frames yields many plausible continuations (diversity); a designer can edit a frame, such as inserting a character, and the model carries the edit forward (persistency). WHAM-1.6B produces about one frame per second at 300x180. WHAMM replaces token-by-token decoding with MaskGIT-style parallel prediction (a 500M backbone plus a 250M refiner) to reach more than 10 fps at 640x360 on Quake II.

## Limitations

- WHAM-1.6B generates about one image per second at 300x180, too slow and too small for play; WHAMM trades data scope (one level section) for speed.
- Needs years of recorded human play with consent terms for a single game; few studios hold such datasets.
- Context of under a second (WHAMM) means objects out of view are forgotten.
- Counts, damage, and other exact quantities are unreliable in generated frames.

## Relations

**affects**

- [Direct avatar control](../mechanic/direct-avatar.md) (Replaces substrate): In WHAMM the avatar's movement and camera are rendered by the model from controller input, at 10+ fps with a 0.9 second context.
- [Rigid-body physics](../mechanic/rigid-body-physics.md) (Replaces substrate): Movement and collisions follow learned game dynamics; the Nature paper's consistency criterion is that generated play respects controller input and the game's physics, which is measured statistically rather than enforced.
- [Generative content on demand](../mechanic/generative-content.md) (Enables new form): Designers insert an object or character into a frame and the model generates plausible gameplay around it (persistency), giving a preview of how a content change might play before it is built.

## Claims

- The Nature paper (February 2025) frames consistency, diversity, and persistency of user modifications as the three capabilities generative models need to support game ideation, and shows WHAM provides them. *(confidence: high)* [[228](../source/src-kanervisto-2025-wham.md)]
- WHAM was trained on more than 1 billion images and controller actions, over 7 years of continuous play, from Bleeding Edge matches recorded under the game's EULA; model weights, sample data, and the WHAM Demonstrator were released on Azure AI Foundry. *(confidence: high)* [[229](../source/src-microsoft-2025-muse-blog.md)]
- WHAMM ran a playable section of one Quake II level at 10+ fps and 640x360 after training on one week of gameplay data; enemies were blurry, damage could be wrong, context was 0.9 seconds, and health counters were unreliable. *(confidence: high)* [[230](../source/src-microsoft-2025-whamm.md)]

## Sources

- [World and Human Action Models towards gameplay ideation](../source/src-kanervisto-2025-wham.md)
- [Introducing Muse: Our first generative AI model designed for gameplay ideation](../source/src-microsoft-2025-muse-blog.md)
- [WHAMM real-time Quake II world model (Microsoft Research blog)](../source/src-microsoft-2025-whamm.md)

---
Provenance: created in run `2026-10-24-techniques-world-models`.
