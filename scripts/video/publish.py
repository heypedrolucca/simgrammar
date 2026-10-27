"""Publish rendered videos to the website: write media/published.yaml from video-out and stage the files for a release.

    make build && python scripts/video/assemble.py all        (the renders in video-out/final, their states in video-out/out)
    python scripts/video/publish.py --release shorts-2026-10-27
    gh release create shorts-2026-10-27 video-out/publish/*    (the files are not committed; the release holds them)

Only the shorts are published for now; episodes and the film stay off the site. Each entry names the video file and its
sha256, its length, a poster frame (a JPEG taken at 2.5 s) and its sha256, and the records the video shows: the frame
elements and cards in its rendered states.json that are records, most shown first, at most twelve. The site reads this
file (scripts/web.py), and the Pages workflow fetches the files from the release and checks every sha256
(scripts/video/fetch_published.py). Re-run it after re-rendering and publish under a new release name.
"""
import argparse
import hashlib
import json
import os
import shutil
import subprocess
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
V = Path(os.environ.get('SIMGRAMMAR_VIDEO_OUT', ROOT / 'video-out'))
FFMPEG = os.environ.get('SIMGRAMMAR_FFMPEG', 'ffmpeg')
KEYS = ('id', 'icon', 'of', 'current')
SHOWS_MAX = 12
POSTER_AT = '2.5'


def records():
    out = {}
    for f in sorted((ROOT / 'dist' / 'entities').glob('*.json')):
        for r in json.loads(f.read_text(encoding='utf-8')):
            if r['type'] != 'source':
                out[r['id']] = r['type']
    return out


def shows(states, recs):
    c = Counter()

    def walk(o, acc):
        if isinstance(o, dict):
            for k, v in o.items():
                if k in KEYS and isinstance(v, str) and v in recs:
                    acc.add(v)
                walk(v, acc)
        elif isinstance(o, list):
            for v in o:
                walk(v, acc)
    for s in states:
        seen = set()
        walk(s, seen)
        c.update(seen)
    return [i for i, _ in sorted(c.items(), key=lambda kv: (-kv[1], kv[0]))][:SHOWS_MAX]


def sha256(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def seconds(p):
    out = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', str(p)], capture_output=True, text=True, check=True)
    return round(float(out.stdout), 1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--release', required=True, help='GitHub release tag that will hold the files')
    a = ap.parse_args()
    recs = records()
    stage = V / 'publish'
    if stage.exists():
        shutil.rmtree(stage)
    stage.mkdir(parents=True)
    rows = []
    for i, script in enumerate(sorted((ROOT / 'media' / 'shorts').glob('*.md')), 1):
        key = f'short-{i:02d}'
        mp4 = V / 'final' / f'{key}.mp4'
        states = json.loads((V / 'out' / key / 'states.json').read_text(encoding='utf-8'))
        poster = stage / f'{key}.jpg'
        shutil.copy2(mp4, stage / mp4.name)
        subprocess.run([FFMPEG, '-y', '-v', 'error', '-ss', POSTER_AT, '-i', str(mp4), '-frames:v', '1', '-vf', 'scale=540:-2', '-q:v', '3', str(poster)], check=True)
        rows.append({'key': key, 'script': script.name, 'file': mp4.name, 'sha256': sha256(mp4), 'seconds': seconds(mp4),
                     'poster': poster.name, 'poster_sha256': sha256(poster), 'shows': shows(states, recs)})
    head = ('# Videos published on the website (scripts/web.py). The files are not in git: they are assets of the GitHub release\n'
            '# named here, which the Pages workflow fetches and checks against each sha256 (scripts/video/fetch_published.py).\n'
            '# Written by scripts/video/publish.py from the renders in video-out; shows lists the records each video puts on screen.\n')
    body = f'release: {a.release}\nshorts:\n' + ''.join(
        f'  - {{key: {r["key"]}, script: {r["script"]}, file: {r["file"]}, seconds: {r["seconds"]},\n'
        f'     sha256: {r["sha256"]},\n     poster: {r["poster"]}, poster_sha256: {r["poster_sha256"]},\n'
        f'     shows: [{", ".join(r["shows"])}]}}\n' for r in rows)
    (ROOT / 'media' / 'published.yaml').write_text(head + body, encoding='utf-8')
    print(f'media/published.yaml: {len(rows)} shorts for release {a.release}; files staged in {stage}')


if __name__ == '__main__':
    main()
