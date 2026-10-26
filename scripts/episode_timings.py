#!/usr/bin/env python3
"""Recompute scene timings in an episode script from its rendered narration length.

  python scripts/episode_timings.py media/episodes/01-same-parts.md   (run `make build` first)

Each scene's length is its narration words at WPM plus a beat of picture-only footage; the title card gets a shorter
beat. Headings of the form `## N. Title (m:ss to m:ss)` and the `Target runtime` sentence are rewritten in place.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WPM, BEAT, TITLE_BEAT = 135, 15, 10


def main(path: str) -> None:
    src = ROOT / path
    rendered = (ROOT / "dist" / path).read_text(encoding="utf-8")
    parts = re.split(r"^## (\d+)\. .*$", rendered, flags=re.M)
    words = {int(parts[i]): sum(len(x.split()) for x in re.findall(r"\*\*Voice\.\*\* (.+)", parts[i + 1])) for i in range(1, len(parts), 2)}
    t, spans = 0, {}
    for n in sorted(words):
        d = round(words[n] / WPM * 60) + (BEAT if words[n] else TITLE_BEAT)
        spans[n] = (t, t + d)
        t += d
    fmt = lambda x: f"{x // 60}:{x % 60:02d}"  # noqa: E731
    s = src.read_text(encoding="utf-8")
    s = re.sub(r"^## (\d+)\. (.*?) \(\d+:\d\d to \d+:\d\d\)$", lambda m: f"## {m.group(1)}. {m.group(2)} ({fmt(spans[int(m.group(1))][0])} to {fmt(spans[int(m.group(1))][1])})", s, flags=re.M)
    total = sum(words.values())
    s = re.sub(r"Target runtime about \d+ minutes: about [\d,]+ words of narration", f"Target runtime about {round(t / 60)} minutes: about {round(total, -1):,} words of narration", s)
    src.write_text(s, encoding="utf-8")
    print(f"{path}: {total} narration words, {fmt(t)}")


if __name__ == "__main__":
    main(sys.argv[1])
