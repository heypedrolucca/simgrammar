"""Grammar of **Frame.** lines in media/episodes, media/shorts, and media/mega (ADR-0006).

A Frame line sits under a Picture line and names one frame template and its arguments:

    **Frame.** chain nodes=factory,pollution-spread,land-value,house:Zone growth signs=+,-,+ verbs=writes,lowers,raises from=simcity-1989

Arguments are key=value pairs separated by spaces; a value with spaces is quoted ("..."). Lists are comma-separated,
rows of a list are separated by |, and an item may carry a label after a colon (house:Zone growth). A Picture may
carry several Frame lines; every one after the first has at="<phrase>", the narration words at which it takes over.
scripts/visual/check.py validates Frame lines (E040); scripts/video/framedata.py resolves them for the renderer.
"""
from __future__ import annotations

import re

LABEL = "**Frame.**"
KV = re.compile(r'([a-z_]+)=("([^"]*)"|\S+)')
NUMBER = re.compile(r"^[0-9]+(?:\.[0-9]+)?%?$")

# key -> kind of value. Kinds: game, mechanic, mechanics, family, icon, items, rows, signs, words, loops, text, phrase,
# field, gamemech, terms, panels, enum:<a|b>, number, flag
COMMON = {"at": "phrase"}
TEMPLATES: dict[str, dict] = {
    "anatomy": {"keys": {"game": "game", "parts": "words", "current": "words", "hub": "icon", "spokes": "items", "weights": "enum:illustrative",
                         "from": "gamemech", "blank": "flag"},
                "one_of": [("game",), ("hub", "spokes"), ("blank",)]},
    "chain": {"keys": {"nodes": "rows", "signs": "signs", "verbs": "words", "loops": "loops", "from": "game", "strip": "text", "current": "words"},
              "required": ("nodes",)},
    "compare": {"keys": {"a": "text", "b": "text", "a_items": "items", "b_items": "items", "from": "gamemech"},
                "required": ("a", "b", "a_items", "b_items")},
    "count": {"keys": {"kind": "enum:bars|tiles|roles", "ids": "mechanics", "family": "family", "lit": "enum:affected", "rank": "flag", "current": "words"},
              "required": ("kind",)},
    "timeline": {"keys": {"ids": "mechanics", "current": "words"}, "required": ("ids",)},
    "formula": {"keys": {"result": "items", "terms": "terms", "from": "gamemech"}, "required": ("result", "terms", "from")},
    "scale": {"keys": {"field": "field"}, "required": ("field",)},
    "record": {"keys": {"mechanic": "mechanic", "fields": "words", "stamps": "text"}, "required": ("mechanic",)},
    "moment": {"keys": {"panels": "panels", "subject": "icon"}, "required": ("panels",)},
    "toysim": {"keys": {"sim": "enum:heat|chunks", "from": "gamemech", "tick": "number", "rate": "number", "threshold": "number"},
               "required": ("sim", "from")},
}


class FrameError(ValueError):
    pass


def parse(text: str) -> tuple[str, dict[str, str]]:
    """'chain nodes=a,b signs=+' -> ('chain', {'nodes': 'a,b', 'signs': '+'}); raises FrameError on bad syntax."""
    text = text.strip()
    if text.startswith(LABEL):
        text = text[len(LABEL):].strip()
    head, _, rest = text.partition(" ")
    if head not in TEMPLATES:
        raise FrameError(f"unknown frame template '{head}' (one of {', '.join(TEMPLATES)})")
    args: dict[str, str] = {}
    pos = 0
    rest = rest.strip()
    while pos < len(rest):
        if rest[pos] == " ":
            pos += 1
            continue
        m = KV.match(rest, pos)
        if m:
            k = m.group(1)
            if k in args:
                raise FrameError(f"'{k}' is given twice")
            args[k] = m.group(3) if m.group(3) is not None else m.group(2)
            pos = m.end()
            continue
        word = rest[pos:].split(" ", 1)[0]
        if word in TEMPLATES[head]["keys"] and TEMPLATES[head]["keys"][word] == "flag":
            args[word] = "yes"
            pos += len(word)
            continue
        raise FrameError(f"cannot read '{word}' (arguments are key=value, values with spaces in double quotes)")
    spec = TEMPLATES[head]
    allowed = {**spec["keys"], **COMMON}
    for k in args:
        if k not in allowed:
            raise FrameError(f"'{head}' takes no '{k}' (keys: {', '.join(sorted(allowed))})")
    for k in spec.get("required", ()):
        if k not in args:
            raise FrameError(f"'{head}' needs '{k}'")
    if "one_of" in spec and not any(all(k in args for k in group) for group in spec["one_of"]):
        raise FrameError(f"'{head}' needs one of: " + "; ".join(" and ".join(g) for g in spec["one_of"]))
    for k, v in args.items():
        kind = allowed[k]
        if kind.startswith("enum:") and v not in kind[5:].split("|"):
            raise FrameError(f"'{k}' is one of {kind[5:].replace('|', ', ')}, not '{v}'")
        if kind == "number" and not NUMBER.match(v):
            raise FrameError(f"'{k}' must be a number, not '{v}'")
    return head, args


def items(v: str) -> list[tuple[str, str]]:
    """'a,b:Label' -> [('a', ''), ('b', 'Label')]"""
    out = []
    for part in v.split(","):
        part = part.strip()
        if part:
            i, _, lab = part.partition(":")
            out.append((i.strip(), lab.strip()))
    return out


def rows(v: str) -> list[list[tuple[str, str]]]:
    return [items(r) for r in v.split("|")]


def terms(v: str) -> list[tuple[str, str, str]]:
    """'128,-land-value:Land value,+house:Density' -> [('', '128', ''), ('-', 'land-value', 'Land value'), ('+', 'house', 'Density')]"""
    out = []
    for part in v.split(","):
        part = part.strip()
        op = ""
        if part[:1] in "+-×" and not NUMBER.match(part):
            op, part = part[0], part[1:]
        i, _, lab = part.partition(":")
        out.append((op, i.strip(), lab.strip()))
    return out


def panels(v: str) -> list[tuple[list[str], str]]:
    """'raid:A raid at the door|grave+person:One falls' -> [(['raid'], 'A raid at the door'), (['grave', 'person'], 'One falls')]"""
    out = []
    for part in v.split("|"):
        ic, _, cap = part.partition(":")
        out.append(([x.strip() for x in ic.split("+") if x.strip()], cap.strip()))
    return out


def icon_refs(template: str, args: dict[str, str]) -> list[str]:
    """Every id in a Frame that must have an icon."""
    refs: list[str] = []
    for k, v in args.items():
        kind = {**TEMPLATES[template]["keys"], **COMMON}[k]
        if kind == "icon":
            refs.append(v)
        elif kind == "items":
            refs += [i for i, _ in items(v)]
        elif kind == "rows":
            refs += [i for r in rows(v) for i, _ in r]
        elif kind == "terms":
            refs += [i for _, i, _ in terms(v) if not NUMBER.match(i)]
        elif kind == "panels":
            refs += [i for ics, _ in panels(v) for i in ics]
        elif kind == "mechanics" or (template == "timeline" and k == "ids"):
            refs += [i for i, _ in items(v)]
    if template == "anatomy" and "game" in args and args.get("parts", "core") != "core":
        refs += [i for i, _ in items(args["parts"])]
    return refs


def constants(template: str, args: dict[str, str]) -> list[str]:
    """Numbers a Frame states; each must appear in the record text named by `from` (E040)."""
    out = []
    if template == "formula":
        out += [i for _, i, _ in terms(args.get("terms", "")) if NUMBER.match(i)]
    if template == "toysim":
        out += [args[k] for k in ("tick", "rate", "threshold") if k in args]
    return out
