"""Tone map -> RGBA through an 8x8 Bayer matrix (ordered dither), and PNG bytes.

Ordered dither keeps its pattern still when a picture changes: a 1/255 change in a tonal source flips well under 1 %
of pixels, where error diffusion re-flows about a quarter of them (ADR-0006). Icons use five tones; tonal sources
(toysim plates) use all 64 levels of the matrix.
"""
from __future__ import annotations

import io

import numpy as np
from PIL import Image

INK = (23, 23, 23)
ACCENT = (5, 80, 174)
PAPER = (250, 250, 247)
BAYER8 = np.array([
    [0, 32, 8, 40, 2, 34, 10, 42], [48, 16, 56, 24, 50, 18, 58, 26], [12, 44, 4, 36, 14, 46, 6, 38],
    [60, 28, 52, 20, 62, 30, 54, 22], [3, 35, 11, 43, 1, 33, 9, 41], [51, 19, 59, 27, 49, 17, 57, 25],
    [15, 47, 7, 39, 13, 45, 5, 37], [63, 31, 55, 23, 61, 29, 53, 21]])
COVER = {1: 16, 2: 32, 3: 48, 4: 64}
KNOCKOUT = 9


def threshold(h: int, w: int) -> np.ndarray:
    return BAYER8[np.arange(h)[:, None] % 8, np.arange(w)[None, :] % 8]


def rgba(t: np.ndarray, accent: bool = False) -> np.ndarray:
    """Tone indices -> RGBA at one pixel per dpx. accent=True draws every ink tone in the accent."""
    t = t.astype(np.int16)
    if accent:
        t = np.where((t >= 1) & (t <= 4), t + 4, t)
    th = threshold(*t.shape)
    level = np.where(t >= 5, t - 4, t)
    on = np.zeros(t.shape, bool)
    for lv, cov in COVER.items():
        on |= (level == lv) & (th < cov) & (t != KNOCKOUT)
    out = np.zeros(t.shape + (4,), np.uint8)
    shape = (t != 0)
    out[shape] = PAPER + (255,)                    # paper between the dots is opaque, so nothing behind shows through
    out[on & (t < 5)] = INK + (255,)
    out[on & (t >= 5) & (t != KNOCKOUT)] = ACCENT + (255,)
    return out


def tonal(v: np.ndarray, color=INK) -> np.ndarray:
    """A 0..1 darkness field -> RGBA on paper, with the full 64 Bayer levels (for toysim plates)."""
    th = threshold(*v.shape)
    on = (np.clip(v, 0, 1) * 64) > th
    out = np.zeros(v.shape + (4,), np.uint8)
    out[...] = PAPER + (255,)
    out[on] = tuple(color) + (255,)
    return out


def png(a: np.ndarray, scale: int) -> bytes:
    im = Image.fromarray(a, "RGBA").resize((a.shape[1] * scale, a.shape[0] * scale), Image.NEAREST)
    buf = io.BytesIO()
    im.save(buf, format="PNG", optimize=False, compress_level=9)
    return buf.getvalue()
