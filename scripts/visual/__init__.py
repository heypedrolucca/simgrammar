"""The visual vocabulary: icons drawn as an SVG subset in media/visual/icons, dithered into dist/visual (ADR-0006).

    raster.py   SVG subset -> tone map (what the grid lint, E041, accepts is what this module can draw)
    dither.py   tone map -> RGBA through an 8x8 Bayer matrix, and PNG bytes
    icons.py    every icon at 3 px and 4 px per dither pixel, ink and accent, plus a contact sheet (for scripts/build.py)
    frames.py   the grammar of **Frame.** lines in media scripts: templates, their keys, and what each key names
    toysim.py   small deterministic simulations of a rule a record states, drawn in the same tones
    check.py    E040 (Frame lines), E041 (icons), W108 (coverage), called by scripts/validate.py
"""
