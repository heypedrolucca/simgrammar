"""Put the videos media/published.yaml lists into a built site under media/shorts/, checking every sha256.

    python scripts/video/fetch_published.py _site                               from the GitHub release (the Pages workflow)
    python scripts/video/fetch_published.py dist/web --from video-out/publish   from local files, to preview the site

Fails if a file is missing or its sha256 differs, so the site never links a video it does not carry.
"""
import argparse
import hashlib
import shutil
import sys
import urllib.request
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('site', type=Path)
    ap.add_argument('--from', dest='src', type=Path, help='copy from this folder instead of downloading the release')
    a = ap.parse_args()
    pub = yaml.safe_load((ROOT / 'media' / 'published.yaml').read_text(encoding='utf-8'))
    repo = yaml.safe_load((ROOT / 'report' / 'meta.yaml').read_text(encoding='utf-8'))['site']['repo']
    out = a.site / 'media' / 'shorts'
    out.mkdir(parents=True, exist_ok=True)
    bad = []
    for s in pub.get('shorts', []):
        for name, want in ((s['file'], s['sha256']), (s['poster'], s['poster_sha256'])):
            dest = out / name
            if a.src:
                shutil.copy2(a.src / name, dest)
            else:
                urllib.request.urlretrieve(f'{repo}/releases/download/{pub["release"]}/{name}', dest)
            got = hashlib.sha256(dest.read_bytes()).hexdigest()
            if got != want:
                bad.append(f'{name}: sha256 {got[:12]}, media/published.yaml says {want[:12]}')
    if bad:
        sys.exit('fetch_published: ' + '; '.join(bad))
    print(f'fetch_published: {2 * len(pub.get("shorts", []))} files from {a.src or pub["release"]} into {out}')


if __name__ == '__main__':
    main()
