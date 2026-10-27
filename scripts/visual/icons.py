"""Build dist/visual from media/visual (called by scripts/build.py, so the icons are part of every build and of I11).

    visual/icons/<id>@3x.png, <id>@4x.png                  3 px per dpx for 16:9 frames, 4 px for 9:16 frames
    visual/icons/<id>.accent@3x.png, <id>.accent@4x.png    the same icon in the accent, for the element a sentence is about
    visual/icons.json                                      id -> kind, label, aliases, size in dpx
    visual/sheet.html                                      contact sheet for review
"""
from __future__ import annotations

import json
from pathlib import Path

from . import dither, raster

ROOT = Path(__file__).resolve().parents[2]
VISUAL = ROOT / "media" / "visual"
SCALES = (3, 4)
SIZES = (42, 48, 72, 96, 120, 144)   # the video's draw sizes (42 is the compact size for crowded 9:16 frames)


def load_vocab(path: Path | None = None) -> dict:
    import yaml

    return yaml.safe_load((path or VISUAL / "vocab.yaml").read_text(encoding="utf-8")) or {}


def outputs() -> dict[str, bytes | str]:
    voc = load_vocab()
    outs: dict[str, bytes | str] = {}
    meta = {}
    for e in sorted(voc.get("icons") or [], key=lambda e: e["id"]):
        src = VISUAL / "icons" / f"{e['id']}.svg"
        t = raster.tones(src)
        for accent in (False, True):
            a = dither.rgba(t, accent=accent)
            for s in SCALES:
                outs[f"visual/icons/{e['id']}{'.accent' if accent else ''}@{s}x.png"] = dither.png(a, s)
        meta[e["id"]] = {"kind": e["kind"], "size": int(t.shape[0]), **({"label": e["label"]} if e.get("label") else {}),
                         **({"aliases": e["aliases"]} if e.get("aliases") else {})}
    outs["visual/icons.json"] = json.dumps(meta, indent=1, sort_keys=True, ensure_ascii=False) + "\n"
    rows = []
    for kind in ("mechanic", "family", "subgenre", "technique-category", "technique", "noun", "term"):
        ids = [i for i, m in meta.items() if m["kind"] == kind]
        if not ids:
            continue
        cells = "".join(f'<figure><img src="icons/{i}@3x.png" width="{meta[i]["size"] * 3}" height="{meta[i]["size"] * 3}" alt="">'
                        f'<img src="icons/{i}.accent@3x.png" width="{meta[i]["size"] * 3}" height="{meta[i]["size"] * 3}" alt="">'
                        f'<figcaption>{i}</figcaption></figure>' for i in ids)
        rows.append(f"<h2>{kind} ({len(ids)})</h2><div>{cells}</div>")
    outs["visual/sheet.html"] = ("<!doctype html><meta charset=utf-8><title>visual vocabulary</title><style>body{background:#fafaf7;color:#171717;"
                                 "font:14px ui-monospace,monospace;margin:32px}div{display:flex;flex-wrap:wrap;gap:24px}figure{margin:0}img{image-rendering:pixelated;"
                                 "margin-right:6px}figcaption{margin-top:6px}h2{font-weight:500;font-size:16px;margin:28px 0 12px}</style>"
                                 f"<h1 style='font-weight:500;font-size:18px'>visual vocabulary · {len(meta)} icons · ink and accent at 3 px per dpx</h1>" + "".join(rows) + "\n")
    return outs


def sized(out_dir: Path) -> Path:
    """Write every icon at each of SIZES but its own into out_dir (the video renderer's cache, not dist): <id>[.accent].<dpx>@<px>x.png.

    The vector is redrawn at the bigger size (raster.tones size=), so the dither grain stays one dpx. A manifest of source
    hashes skips icons that have not changed since the last call.
    """
    import hashlib

    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    man = out_dir / "manifest.json"
    old = json.loads(man.read_text()) if man.exists() else {}
    new = {}
    for e in load_vocab().get("icons") or []:
        src = VISUAL / "icons" / f"{e['id']}.svg"
        h = hashlib.sha256(src.read_bytes()).hexdigest()
        new[e["id"]] = h
        native = raster.parse(src)[0]
        if old.get(e["id"]) == h and all((out_dir / f"{e['id']}.{n}@4x.png").exists() for n in SIZES if n != native):
            continue
        for n in SIZES:
            if n == native:
                continue
            t = raster.tones(src, n)
            for accent in (False, True):
                a = dither.rgba(t, accent=accent)
                for s in SCALES:
                    (out_dir / f"{e['id']}{'.accent' if accent else ''}.{n}@{s}x.png").write_bytes(dither.png(a, s))
    man.write_text(json.dumps(new, indent=0, sort_keys=True))
    return out_dir
