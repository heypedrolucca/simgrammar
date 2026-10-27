"""Subtitle cues to SRT, timed from an episode script's scene timings.

A subtitle source (media/subtitles/<lang>/<episode>.md) has one `## <scene number>` heading per scene and one cue per
line beneath it; a line in ［brackets］ translates on-screen text. Each scene's narration is assumed to start half a
second into the scene and to run at the script's 135 words a minute; cues share that window in proportion to their
length, and on-screen cues add two seconds each. Scenes with no narration show their cues across the scene. The result
is a first timing for editors, to be retimed against the recorded voice.
"""
from __future__ import annotations

import re

WPM = 135
SCENE = re.compile(r"^## (\d+)\. .*?\((\d+):(\d\d) to (\d+):(\d\d)\)\s*$", re.M)
VOICE = re.compile(r"^\*\*Voice\.\*\* (.+)$", re.M)


def _scenes(script: str) -> dict[int, tuple[float, float, int]]:
    out = {}
    heads = list(SCENE.finditer(script))
    for i, m in enumerate(heads):
        end = heads[i + 1].start() if i + 1 < len(heads) else len(script)
        body = script[m.end():end].split("\n## Sources")[0]
        words = sum(len(v.split()) for v in VOICE.findall(body))
        out[int(m.group(1))] = (int(m.group(2)) * 60 + int(m.group(3)), int(m.group(4)) * 60 + int(m.group(5)), words)
    return out


def _cues(src: str) -> dict[int, list[str]]:
    out: dict[int, list[str]] = {}
    cur = None
    for line in src.splitlines():
        m = re.match(r"^## (\d+)\s*$", line)
        if m:
            cur = int(m.group(1))
            out[cur] = []
        elif cur is not None and line.strip() and not line.startswith("#") and not line.startswith("*Dataset"):
            out[cur].append(line.strip())
    return out


def _ts(t: float) -> str:
    ms = int(round(t * 1000))
    h, ms = divmod(ms, 3_600_000)
    m, ms = divmod(ms, 60_000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def srt(script: str, src: str) -> str:
    scenes, cues = _scenes(script), _cues(src)
    lines, n = [], 0
    for k in sorted(cues):
        if k not in scenes or not cues[k]:
            continue
        t0, t1, words = scenes[k]
        screen = sum(1 for c in cues[k] if c.startswith("［"))
        start = t0 + 0.5
        end = t1 - 0.5 if words == 0 else min(t1 - 0.3, start + words / WPM * 60 + 2 * screen)
        weights = [max(len(c), 8) for c in cues[k]]
        total = sum(weights)
        t = start
        for c, w in zip(cues[k], weights):
            d = max(1.2, (end - start) * w / total)
            n += 1
            lines += [str(n), f"{_ts(t)} --> {_ts(min(t + d, t1))}", c, ""]
            t = min(t + d, t1)
    return "\n".join(lines)
