"""Checks for the visual vocabulary and the Frame lines that use it (ADR-0006), called by scripts/validate.py.

E040 frame-line   every **Frame.** line in media scripts parses, sits under a Picture line in its scene, names ids that
                  resolve (icons in media/visual/vocab.yaml, live games and mechanics, families, rubric fields), finds its
                  at="..." phrase in the scene's narration, and states no number that the record it cites lacks.
E041 visual-icon  every vocab.yaml entry has a valid icon file in the SVG subset and every icon file has an entry; ids are
                  unique and of a known kind; dataset-kind ids exist; no id, label, or alias is a game's id, name, or alias.
W108 visual-coverage  mechanics, families, subgenres, and technique categories with no icon yet (warning until phase 4).
"""
from __future__ import annotations

import re
from pathlib import Path

from . import frames as FR
from . import raster

ROOT = Path(__file__).resolve().parents[2]
VISUAL = ROOT / "media" / "visual"
SCRIPT_DIRS = ("media/episodes", "media/shorts", "media/mega")
KINDS = ("mechanic", "family", "subgenre", "technique", "technique-category", "noun", "term")
SCENE = re.compile(r"^## (\d+)\. (.+?)(?: \((.+?)\))?\s*$|^## (\d+:\d\d) to (\d+:\d\d)\. (.+?)\s*$")
TOKEN = re.compile(r"\{\{[^}]*\}\}")
CITE = re.compile(r"\s?\[@src-[^\]]+\]")
LINK = re.compile(r"\[\[[a-z0-9-]+\|([^\]]+)\]\]|\[\[([a-z0-9-]+)\]\]")


def plain(s: str) -> str:
    s = TOKEN.sub("", s)
    s = CITE.sub("", s)
    s = LINK.sub(lambda m: m.group(1) or m.group(2).replace("-", " "), s)
    return re.sub(r"\s+", " ", s.replace("**", "").replace("*", "")).strip()


def scenes(path: Path) -> list[dict]:
    """Scenes of a source script: [{n, line, blocks: [(kind, text, line)]}]; stops at the film's Film wording section."""
    out, cur = [], None
    for no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if line.startswith("## ") and not SCENE.match(line):
            cur = None
            continue
        if SCENE.match(line):
            cur = {"n": len(out) + 1, "line": no, "blocks": []}
            out.append(cur)
            continue
        if cur is None:
            continue
        for kind, lab in (("picture", "**Picture.**"), ("voice", "**Voice.**"), ("onscreen", "**On screen.**"), ("frame", FR.LABEL)):
            if line.startswith(lab):
                cur["blocks"].append((kind, line[len(lab):].strip(), no))
    return out


def record_text(game: dict | None, mechanic: dict | None, gid: str, mid: str) -> str:
    """The text a Frame may draw numbers from: the game's note on its use of the mechanic, and the mechanic's own text."""
    parts = []
    if game:
        parts += [u.get("note") or "" for u in game.get("mechanics", []) if u.get("id") == mid]
        parts.append(game.get("design_notes") or "")
    if mechanic:
        for k in ("definition", "summary"):
            parts.append(str(mechanic.get(k) or ""))
        parts += [str(x) for x in mechanic.get("failure_modes") or []]
    return " ".join(parts)


def check(F, ents: dict, vocabs: dict) -> None:
    import yaml

    vpath = VISUAL / "vocab.yaml"
    if not vpath.exists():
        return
    voc = yaml.safe_load(vpath.read_text(encoding="utf-8")) or {}
    games = {e.id: e.data for e in ents.get("game", []) if not e.data.get("deprecated")}
    mechs = {e.id: e.data for e in ents.get("mechanic", []) if not e.data.get("deprecated")}
    runs = {e.id for e in ents.get("run", [])}
    dataset_ids = {e.id for lst in ents.values() for e in lst}
    terms = {name: {str(t["id"]) for t in v.get("terms", [])} for name, v in vocabs.items() if name != "rubrics"}
    game_names = set()
    for g in games.values():
        game_names.add(g["id"].lower())
        game_names.add(str(g.get("name", "")).lower())
        game_names.update(str(a).lower() for a in g.get("aliases") or [])
    icons = {}

    # ---- E041: the icon set
    if voc.get("run") and voc["run"] not in runs:
        F.add("E041", vpath, f"run '{voc['run']}' is not in log/runs/")
    for e in voc.get("icons") or []:
        i = str(e.get("id", ""))
        if i in icons:
            F.add("E041", vpath, f"icon '{i}' is listed twice")
            continue
        icons[i] = e
        kind = e.get("kind")
        if kind not in KINDS:
            F.add("E041", vpath, f"icon '{i}': kind '{kind}' is not one of {', '.join(KINDS)}")
        if kind == "mechanic" and i not in mechs:
            F.add("E041", vpath, f"icon '{i}': no live mechanic has this id")
        if kind == "family" and i not in terms.get("mechanic_family", set()):
            F.add("E041", vpath, f"icon '{i}': not a mechanic_family term")
        if kind == "subgenre" and i not in terms.get("subgenre", set()):
            F.add("E041", vpath, f"icon '{i}': not a subgenre term")
        if kind == "technique-category" and i not in terms.get("technique_category", set()):
            F.add("E041", vpath, f"icon '{i}': not a technique_category term")
        if kind == "technique" and i not in {x.id for x in ents.get("technique", [])}:
            F.add("E041", vpath, f"icon '{i}': no technique has this id")
        if kind in ("noun", "term"):
            if not e.get("label"):
                F.add("E041", vpath, f"icon '{i}': a {kind} needs a label")
            if i in dataset_ids:
                F.add("E041", vpath, f"icon '{i}': a {kind} id cannot reuse a dataset id")
        if e.get("run") and e["run"] not in runs:
            F.add("E041", vpath, f"icon '{i}': run '{e['run']}' is not in log/runs/")
        for name in [i, str(e.get("label") or "")] + [str(a) for a in e.get("aliases") or []]:
            if name and name.lower() in game_names:
                F.add("E041", vpath, f"icon '{i}': '{name}' names a game; icons draw generic subjects only")
        src = VISUAL / "icons" / f"{i}.svg"
        if not src.exists():
            F.add("E041", vpath, f"icon '{i}' has no file media/visual/icons/{i}.svg")
            continue
        try:
            raster.parse(src)
        except raster.IconError as err:
            F.add("E041", src, str(err))
    for p in sorted((VISUAL / "icons").glob("*")):
        if p.suffix != ".svg" or p.stem not in icons:
            F.add("E041", p, "file has no entry in media/visual/vocab.yaml" if p.suffix == ".svg" else "only .svg icon sources belong here")

    # ---- W108: coverage
    have = set(icons)
    gaps = {"mechanics": sorted(set(mechs) - have), "families": sorted(terms.get("mechanic_family", set()) - have),
            "subgenres": sorted(terms.get("subgenre", set()) - have), "technique categories": sorted(terms.get("technique_category", set()) - have)}
    missing = [f"{len(v)} {k}" for k, v in gaps.items() if v]
    if missing:
        F.add("W108", vpath, "no icon yet for " + ", ".join(missing))

    # ---- E040: Frame lines
    rubric_fields = set((vocabs.get("rubrics") or {}).get("scales", {}))
    for d in SCRIPT_DIRS:
        for path in sorted((ROOT / d).glob("*.md")):
            for sc in scenes(path):
                voice = " ".join(plain(t) for k, t, _ in sc["blocks"] if k == "voice")
                seen_picture = False
                for kind, text, line in sc["blocks"]:
                    if kind == "picture":
                        seen_picture = True
                    if kind != "frame":
                        continue
                    if not seen_picture:
                        F.add("E040", path, f"line {line}: a Frame line must follow a Picture line in its scene")
                    try:
                        t, args = FR.parse(text)
                    except FR.FrameError as err:
                        F.add("E040", path, f"line {line}: {err}")
                        continue
                    bad = lambda msg: F.add("E040", path, f"line {line}: {msg}")
                    refs = FR.icon_refs(t, args)
                    if t == "anatomy" and args.get("game") in games and args.get("parts", "core") in ("core", "all"):
                        refs += [u["id"] for u in games[args["game"]].get("mechanics", []) if args.get("parts", "core") == "all" or u.get("role") == "core"]
                    for ref in refs:
                        if ref not in icons:
                            bad(f"'{ref}' has no icon in media/visual/vocab.yaml")
                    if "game" in args and args["game"] not in games:
                        bad(f"no live game '{args['game']}'")
                    if t == "chain" and "from" in args and args["from"] not in games:
                        bad(f"no live game '{args['from']}'")
                    for k in ("ids",):
                        if k in args:
                            for i, _ in FR.items(args[k]):
                                if i not in mechs:
                                    bad(f"no live mechanic '{i}'")
                    if "mechanic" in args and args["mechanic"] not in mechs:
                        bad(f"no live mechanic '{args['mechanic']}'")
                    if "family" in args and args["family"] not in terms.get("mechanic_family", set()):
                        bad(f"'{args['family']}' is not a mechanic_family term")
                    if "field" in args:
                        mid, _, fld = args["field"].partition(".")
                        if mid not in mechs or fld not in rubric_fields or fld not in mechs.get(mid, {}):
                            bad(f"'{args['field']}' is not a rubric-scored field of a live mechanic")
                    gid = mid = ""
                    if "from" in args and t != "chain":
                        gid, _, mid = args["from"].partition(":")
                        if gid not in games:
                            bad(f"no live game '{gid}' in from={args['from']}")
                        elif mid and mid not in [u.get("id") for u in games[gid].get("mechanics", [])]:
                            bad(f"'{gid}' does not use '{mid}' (from={args['from']})")
                    nums = FR.constants(t, args)
                    if nums:
                        text_ = record_text(games.get(gid), mechs.get(mid), gid, mid)
                        for n in nums:
                            if not re.search(r"(?<![0-9.])" + re.escape(n) + r"(?![0-9])", text_):
                                bad(f"the number {n} is not in the record text it cites ({args.get('from')})")
                    if "at" in args and args["at"] not in voice:
                        bad(f"at=\"{args['at']}\" is not in this scene's narration")
