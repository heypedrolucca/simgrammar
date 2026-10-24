#!/usr/bin/env python3
"""Write a single self-contained explorer page (data inlined) for hosts that cannot fetch dist/site/data.json.

  python scripts/export_site.py out.html            full HTML document
  python scripts/export_site.py out.html --fragment  body-only fragment (for hosts that add their own <html>/<head>)
"""
import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out")
    ap.add_argument("--fragment", action="store_true")
    a = ap.parse_args()
    html = (ROOT / "site" / "index.html").read_text(encoding="utf-8")
    data = (ROOT / "dist" / "site" / "data.json").read_text(encoding="utf-8").strip().replace("</", "<\\/")
    inject = f"<script>window.SIMGRAMMAR_DATA = {data};</script>\n"
    html = html.replace('<script src="https://cdnjs.cloudflare.com/ajax/libs/marked', inject + '<script src="https://cdnjs.cloudflare.com/ajax/libs/marked', 1)
    if a.fragment:
        html = re.sub(r"<!doctype html>\s*<html[^>]*>\s*<head>\s*", "", html, flags=re.I)
        html = re.sub(r'<meta charset="utf-8">\s*<meta name="viewport"[^>]*>\s*', "", html)
        html = html.replace("</head>\n<body>\n", "").replace("</body>\n</html>\n", "")
    Path(a.out).write_text(html, encoding="utf-8")
    print(a.out, len(html) // 1024, "KB")


if __name__ == "__main__":
    main()
