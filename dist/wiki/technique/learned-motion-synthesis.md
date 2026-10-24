# Learned kinematic motion synthesis

*Technique* · `learned-motion-synthesis` · status: **sourced**

Neural networks generate or compress kinematic character animation, as in Ubisoft's learned motion matching, EA's HyperMotion, and inZOI's motion extraction from uploaded video.

| field | value |
|---|---|
| aliases | learned motion matching, HyperMotion, video-to-motion |
| category | Animation & motion |
| year | 2020 |
| maturity | Shipped (niche) |
| trl | 7 |
| runtime | Client real-time, Offline authoring, Design assist |
| determinism impact | Preserves |
| horizon | Now |
| risks | Controllability, Evaluation difficulty, Labor displacement |
| deployed in | [inZOI](../game/inzoi.md) |
| affects count *(computed)* | 2 |

## Summary

Neural networks generate or compress kinematic character animation, as in Ubisoft's learned motion matching, EA's HyperMotion, and inZOI's motion extraction from uploaded video.

## Mechanism

Motion matching picks the next pose by searching a database of mocap frames for the best match to a query of current pose and desired trajectory. Learned motion matching replaces the database with three small networks: a Decompressor that maps a feature vector to a full pose, a Stepper that advances features one frame, and a Projector that maps a query to the nearest valid features, giving nearly identical output at constant CPU cost. HyperMotion trains a model on frames of full-team match capture to generate transitions in real time. Video-to-motion tools estimate 3D poses from ordinary video and retarget them onto a game rig. No physics is simulated.

## Limitations

- Kinematic output ignores physics, so characters still clip or float when the environment differs from the training motion.
- Learned motion matching saves memory but not per-character CPU time, which still limits crowd counts.
- Video-to-motion quality depends on the uploaded footage; occlusion and camera motion produce artifacts that the game must filter or let players discard.

## Relations

**affects**

- [Direct avatar control](../mechanic/direct-avatar.md) (Deepens): Motion-matching-quality responsive locomotion fits in a few MB of weights, making it affordable on memory-constrained platforms and for more character types.
- [Generative content on demand](../mechanic/generative-content.md) (Deepens): Players author new character motions from their own video (inZOI), so the animation set available to life-sim characters is no longer fixed by the studio's mocap library.

**deployed in**

- [inZOI](../game/inzoi.md)

## Claims

- Learned motion matching shrank a 590 MB motion matching locomotion system to about 17 MB of weights (8.5 MB with 16-bit quantization), about 70 times smaller, with nearly identical output and constant CPU cost. *(confidence: high)* [[159](../source/src-ubisoft-2020-learned-motion-matching.md)]
- FIFA 22's HyperMotion used a machine learning algorithm over more than 8.7 million frames of 22-player match capture to generate player animation in real time, on PS5, Xbox Series X/S, and Stadia only. *(confidence: medium)* [[160](../source/src-wikipedia-fifa-22.md)]
- inZOI lets players create character motions by uploading video files, disclosed as an AI-assisted feature. *(confidence: high)* [[138](../source/src-steam-2025-inzoi.md)]
- Unreal Engine ships database motion matching through its Pose Search plugin, the non-learned baseline that learned motion matching compresses. *(confidence: high)* [[161](../source/src-epic-2026-motion-matching-docs.md)]

## Sources

- [Introducing Learned Motion Matching](../source/src-ubisoft-2020-learned-motion-matching.md)
- [FIFA 22](../source/src-wikipedia-fifa-22.md)
- [inZOI on Steam](../source/src-steam-2025-inzoi.md)
- [Motion Matching in Unreal Engine](../source/src-epic-2026-motion-matching-docs.md)

---
Provenance: created in run `2026-10-24-techniques-world-models`.
