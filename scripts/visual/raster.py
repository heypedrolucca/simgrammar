"""Draw an icon from the SVG subset in media/visual/icons into a tone map.

An icon is a flat list of rect, circle, ellipse, line, polyline, and polygon elements in a square viewBox of 48 (or
96 for hero subjects) dither pixels (dpx). Colours name tones, so the file previews in a browser as flat greys:

    #c8c8c2 25 % ink   #8c8c86 50 %   #55554f 75 %   #171717 ink   #fafaf7 knockout (opaque paper)
    #a9c2e6 #6f93cf #3a6ab8 #0550ae   the same four levels in the accent, for a part that is always accent

Strokes are 1, 2, or 3 dpx and centred on the geometry, as in SVG. Shapes are drawn in document order at 4x with no
antialiasing and sampled at the centre of each dpx, so the same file always gives the same tones.
"""
from __future__ import annotations

import re
import xml.etree.ElementTree as ET
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw

SS = 4
NS = "{http://www.w3.org/2000/svg}"
TONES = {"#c8c8c2": 1, "#8c8c86": 2, "#55554f": 3, "#171717": 4, "#a9c2e6": 5, "#6f93cf": 6, "#3a6ab8": 7, "#0550ae": 8, "#fafaf7": 9}
KNOCKOUT = 9
SIZES = (48, 96)
WIDTHS = (1, 2, 3)
GEOMETRY = {
    "rect": ("x", "y", "width", "height", "rx"),
    "circle": ("cx", "cy", "r"),
    "ellipse": ("cx", "cy", "rx", "ry"),
    "line": ("x1", "y1", "x2", "y2"),
    "polyline": ("points",),
    "polygon": ("points",),
}
STYLE = ("fill", "stroke", "stroke-width")
ALLOWED_TOP = ("xmlns", "viewBox", "width", "height")


class IconError(ValueError):
    pass


def _num(v: str, what: str, n: int) -> float:
    try:
        x = float(v)
    except ValueError:
        raise IconError(f"{what} '{v}' is not a number")
    if abs(x * 2 - round(x * 2)) > 1e-9:
        raise IconError(f"{what} {v} is off the half-dpx grid")
    if not -0.0 <= x <= n:
        raise IconError(f"{what} {v} is outside the {n}-dpx box")
    return x


def _points(v: str, n: int) -> list[tuple[float, float]]:
    nums = [p for p in re.split(r"[\s,]+", v.strip()) if p]
    if len(nums) % 2 or len(nums) < 4:
        raise IconError(f"points '{v}' is not a list of x,y pairs")
    xs = [_num(p, "point", n) for p in nums]
    return list(zip(xs[0::2], xs[1::2]))


def _tone(v: str | None, what: str) -> int | None:
    if v is None or v == "none":
        return None
    t = TONES.get(v.lower())
    if t is None:
        raise IconError(f"{what} '{v}' is not a tone of the palette")
    return t


def parse(path: Path) -> tuple[int, list[dict]]:
    """Read an icon file; raise IconError on anything outside the subset (the E041 grid lint)."""
    try:
        root = ET.parse(path).getroot()
    except ET.ParseError as e:
        raise IconError(f"not well-formed XML: {e}")
    if root.tag not in ("svg", NS + "svg"):
        raise IconError("root element is not <svg>")
    for k in root.attrib:
        if k not in ALLOWED_TOP:
            raise IconError(f"<svg> attribute '{k}' is not allowed")
    vb = (root.get("viewBox") or "").split()
    if len(vb) != 4 or vb[:2] != ["0", "0"] or vb[2] != vb[3] or int(float(vb[2])) not in SIZES:
        raise IconError(f"viewBox must be '0 0 48 48' or '0 0 96 96', not '{root.get('viewBox')}'")
    n = int(float(vb[2]))
    shapes = []
    for el in root:
        tag = el.tag.replace(NS, "")
        if tag == "title":
            continue
        if tag not in GEOMETRY:
            raise IconError(f"<{tag}> is not in the subset (rect, circle, ellipse, line, polyline, polygon)")
        for k in el.attrib:
            if k not in GEOMETRY[tag] + STYLE:
                raise IconError(f"<{tag}> attribute '{k}' is not allowed")
        if len(el):
            raise IconError(f"<{tag}> has children; icons are flat")
        s = {"tag": tag, "fill": _tone(el.get("fill"), "fill"), "stroke": _tone(el.get("stroke"), "stroke")}
        if tag in ("line", "polyline") and s["fill"] is not None:
            raise IconError(f"<{tag}> cannot be filled")
        if tag not in ("line", "polyline") and el.get("fill") is None:
            raise IconError(f"<{tag}> needs an explicit fill (a tone or none)")
        w = el.get("stroke-width")
        if s["stroke"] is not None:
            if w is None or w not in {str(x) for x in WIDTHS}:
                raise IconError(f"<{tag}> stroke-width must be 1, 2, or 3, not '{w}'")
            s["w"] = int(w)
        elif w is not None:
            raise IconError(f"<{tag}> has a stroke-width but no stroke")
        if s["fill"] is None and s["stroke"] is None:
            raise IconError(f"<{tag}> draws nothing")
        for k in GEOMETRY[tag]:
            if k == "points":
                s["points"] = _points(el.get("points") or "", n)
            elif k == "rx" and tag == "rect":
                s["rx"] = _num(el.get("rx"), "rx", n) if el.get("rx") else 0.0
            else:
                if el.get(k) is None:
                    raise IconError(f"<{tag}> lacks '{k}'")
                s[k] = _num(el.get(k), k, n)
        shapes.append(s)
    if not shapes:
        raise IconError("no shapes")
    return n, shapes


def tones(path: Path) -> np.ndarray:
    """Tone-index array, one value per dpx: 0 clear, 1-4 ink, 5-8 accent, 9 knockout."""
    n, shapes = parse(path)
    im = Image.new("L", (n * SS, n * SS), 0)
    d = ImageDraw.Draw(im)
    S = lambda v: v * SS
    for s in shapes:
        t, f, st = s["tag"], s["fill"], s["stroke"]
        w = s.get("w", 0)
        h = w / 2
        if t == "rect":
            x0, y0, x1, y1 = s["x"], s["y"], s["x"] + s["width"], s["y"] + s["height"]
            r = s.get("rx", 0)
            if f is not None:
                box = [S(x0), S(y0), S(x1) - 1, S(y1) - 1]
                (d.rounded_rectangle(box, S(r), fill=f) if r else d.rectangle(box, fill=f))
            if st is not None:
                box = [S(x0 - h), S(y0 - h), S(x1 + h) - 1, S(y1 + h) - 1]
                (d.rounded_rectangle(box, S(r + h), outline=st, width=S(w)) if r else d.rectangle(box, outline=st, width=S(w)))
        elif t in ("circle", "ellipse"):
            rx = s["r"] if t == "circle" else s["rx"]
            ry = s["r"] if t == "circle" else s["ry"]
            cx, cy = s["cx"], s["cy"]
            if f is not None:
                d.ellipse([S(cx - rx), S(cy - ry), S(cx + rx) - 1, S(cy + ry) - 1], fill=f)
            if st is not None:
                d.ellipse([S(cx - rx - h), S(cy - ry - h), S(cx + rx + h) - 1, S(cy + ry + h) - 1], outline=st, width=S(w))
        elif t == "line":
            d.line([(S(s["x1"]), S(s["y1"])), (S(s["x2"]), S(s["y2"]))], fill=st, width=S(w))
        else:
            pts = [(S(x), S(y)) for x, y in s["points"]]
            if t == "polygon" and f is not None:
                d.polygon(pts, fill=f)
            if st is not None:
                d.line(pts + ([pts[0]] if t == "polygon" else []), fill=st, width=S(w), joint="curve")
    return np.array(im.resize((n, n), Image.NEAREST))
