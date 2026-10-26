"""Parse rendered scripts (dist/media) into scenes with ordered blocks: picture, voice, onscreen."""
import re, json, glob, os
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, '..', '..', 'dist', 'media')
OUT = os.path.join(HERE, '..', '..', 'dist', 'video')
SCENE = re.compile(r"^## (\d+)\. (.+?)(?: \((.+?)\))?\s*$")
SHORT = re.compile(r"^## (\d+:\d\d) to (\d+:\d\d)\. (.+?)\s*$")

def clean(s):
    s = re.sub(r"<!--.*?-->", "", s)
    s = re.sub(r"\s*\[(?:\[\d+\]\(#ref-[^)]+\)(?:,\s*)?)+\]", "", s)       # citations
    s = re.sub(r"\[([^\]]+)\]\((?:[^)]+)\)", r"\1", s)                       # links
    s = re.sub(r"`([^`]+)`", r"\1", s)
    s = s.replace("**", "").replace("*", "")
    return re.sub(r"\s+", " ", s).strip()

def parse(path):
    txt = open(path, encoding='utf-8').read().split("\n## Sources")[0]
    title = re.search(r"^# (.+)$", txt, re.M).group(1)
    scenes, cur = [], None
    for line in txt.splitlines():
        m2 = SHORT.match(line)
        if m2:
            cur = {"n": len(scenes) + 1, "title": m2.group(3), "time": f"{m2.group(1)} to {m2.group(2)}", "blocks": []}
            scenes.append(cur); continue
        m = SCENE.match(line)
        if m:
            cur = {"n": int(m.group(1)), "title": m.group(2), "time": m.group(3) or "", "blocks": []}
            scenes.append(cur); continue
        if cur is None: continue
        for kind, lab in (("picture", "**Picture.**"), ("voice", "**Voice.**"), ("onscreen", "**On screen.**")):
            if line.startswith(lab):
                cur["blocks"].append({"kind": kind, "text": clean(line[len(lab):])})
    return {"file": os.path.basename(path), "title": title, "scenes": scenes}

def parse_all():
    out = {}
    for p in sorted(glob.glob(ROOT + "/episodes/*.md")) + [ROOT + "/mega/the-film.md"] + sorted(glob.glob(ROOT + "/shorts/*.md")):
        d = parse(p); out[os.path.relpath(p, ROOT)] = d
    os.makedirs(OUT, exist_ok=True)
    json.dump(out, open(os.path.join(OUT, "scripts.json"), "w"), ensure_ascii=False, indent=1)
    return out

if __name__ == "__main__":
    out = parse_all()
    for k, d in out.items():
        nv = sum(1 for s in d["scenes"] for b in s["blocks"] if b["kind"] == "voice")
        w = sum(len(b["text"].split()) for s in d["scenes"] for b in s["blocks"] if b["kind"] == "voice")
        print(f"{k:45s} scenes={len(d['scenes']):3d} voice={nv:3d} words={w}")
