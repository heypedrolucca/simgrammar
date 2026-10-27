"""Small deterministic simulations of a rule a record states, drawn in the vocabulary's dither (toysim frames).

Each sim returns three snapshots (start, later, much later) as 0..1 darkness fields at one value per dpx. Parameters
that are numbers in the record (Factorio's 2 % diffusion above 15 units) come from the Frame line, and E040 checks
that the record text states them. Nothing here is random.
"""
from __future__ import annotations

import numpy as np


def heat(w: int = 160, h: int = 90, tick: float = 0.2, steps=(0, 400, 4000)) -> list[np.ndarray]:
    """Every tile trades heat with its four neighbours each tick, in proportion to the difference and the conductivity
    of the pair (Oxygen Not Included's rule). A generator room at the left holds its heat; an insulated wall with a door
    slows the flow out of it; the rest of the base starts cool."""
    T = np.full((h, w), 0.12)
    k = np.full((h, w), 1.0)
    y0, y1, x0, x1 = h // 2 - 16, h // 2 + 16, 10, 46
    room = (slice(y0 + 2, y1 - 1), slice(x0 + 2, x1 - 1))
    k[y0, x0:x1 + 1] = k[y1, x0:x1 + 1] = 0.03        # insulated walls around the generator room
    k[y0:y1 + 1, x0] = k[y0:y1 + 1, x1] = 0.03
    k[h // 2 - 4:h // 2 + 5, x1] = 1.0                # the door
    k[:, :2] = k[:, -2:] = k[:2, :] = k[-2:, :] = 0.0  # the map edge holds no heat flow
    shots, t = [], 0
    rate = tick * 1.2
    for target in steps:
        while t < target:
            T[room] = 1.0
            kp_x = np.minimum(k[:, 1:], k[:, :-1])
            kp_y = np.minimum(k[1:, :], k[:-1, :])
            fx = kp_x * (T[:, 1:] - T[:, :-1])
            fy = kp_y * (T[1:, :] - T[:-1, :])
            dT = np.zeros_like(T)
            dT[:, :-1] += fx
            dT[:, 1:] -= fx
            dT[:-1, :] += fy
            dT[1:, :] -= fy
            T = T + rate * dT
            t += 1
        T[room] = 1.0
        snap = T.copy()
        snap[k == 0.0] = 1.0                           # the map edge solid
        snap[(k > 0.0) & (k < 0.05)] = 0.0             # insulation drawn as a paper line
        shots.append(np.clip(snap, 0, 1))
    return shots


def chunks(cw: int = 32, ch: int = 18, size: int = 5, rate: float = 0.02, threshold: float = 15.0, steps=(1, 200, 900)) -> list[np.ndarray]:
    """Factorio's chunk rule: machines emit into their chunk; a chunk holding more than `threshold` sends `rate` of its
    pollution to each cardinal neighbour every update; ground and trees absorb a little everywhere."""
    P = np.zeros((ch, cw))
    src = [(9, 8), (9, 9), (10, 8)]
    absorb = 0.12 + 0.10 * ((np.arange(cw)[None, :] * 7 + np.arange(ch)[:, None] * 11) % 5 == 0)
    shots, t = [], 0
    for target in steps:
        while t < target:
            for y, x in src:
                P[y, x] += 12.0
            over = P > threshold
            out = np.where(over, P * rate, 0.0)
            Q = P - 4 * out
            Q[1:, :] += out[:-1, :]
            Q[:-1, :] += out[1:, :]
            Q[:, 1:] += out[:, :-1]
            Q[:, :-1] += out[:, 1:]
            Q[0, :] += out[0, :]
            Q[-1, :] += out[-1, :]
            Q[:, 0] += out[:, 0]
            Q[:, -1] += out[:, -1]
            P = np.maximum(Q - absorb, 0.0)
            t += 1
        v = np.log1p(P) / np.log1p(400.0)
        field = np.kron(np.clip(v, 0, 1), np.ones((size, size)))
        field[::size, :] = 0.0                                   # chunk borders
        field[:, ::size] = 0.0
        shots.append(field)
    return shots


def flow(levels: int = 7, steps=(30, 160, 600)) -> list[np.ndarray]:
    """Dwarf Fortress's water rule, drawn in side view: each tile holds 0 to `levels` units, falls into the tile below when
    it has room, and otherwise spreads sideways toward a lower neighbour. A river at the top left keeps flowing into a
    tunnel the miner just opened; the tunnel leads down to a cistern, a hall, and a row of rooms."""
    cell, cw, ch = 4, 40, 22
    rock = np.ones((ch, cw), bool)
    def dig(y0, y1, x0, x1):
        rock[y0:y1, x0:x1] = False
    dig(1, 4, 0, 9)          # the river
    dig(3, 5, 8, 20)         # the tunnel, its last tile cut
    dig(5, 9, 18, 21)        # a shaft down
    dig(8, 11, 12, 30)       # the cistern and dining hall
    dig(11, 16, 27, 30)      # a stairwell
    dig(15, 18, 4, 38)       # the bedroom corridor
    for x in range(6, 36, 6):
        dig(18, 21, x, x + 4)  # bedrooms
    W = np.zeros((ch, cw), int)
    shots, t = [], 0
    for target in steps:
        while t < target:
            W[1:4, 0:2] = levels                         # the river keeps coming
            for y in range(ch - 2, -1, -1):              # fall first, bottom up
                for x in range(cw):
                    if W[y, x] and not rock[y + 1, x] and W[y + 1, x] < levels:
                        m = min(W[y, x], levels - W[y + 1, x]); W[y, x] -= m; W[y + 1, x] += m
            for y in range(ch):                          # then spread toward lower neighbours, alternating sides
                xs = range(cw) if t % 2 == 0 else range(cw - 1, -1, -1)
                for x in xs:
                    for dx in ((1, -1) if t % 2 == 0 else (-1, 1)):
                        nx = x + dx
                        if 0 <= nx < cw and not rock[y, nx] and W[y, x] - W[y, nx] >= 2:
                            W[y, x] -= 1; W[y, nx] += 1
            t += 1
        f = np.where(rock, 0.1, 0.0) + np.where(W > 0, 0.3 + 0.7 * W / levels, 0.0)
        shots.append(np.kron(np.clip(f, 0, 1), np.ones((cell, cell))))
    return shots


def life(gens: int = 1103, steps=None, view=(92, 50), cell: int = 2) -> list[np.ndarray]:
    """Conway's rule (a dead cell with three live neighbours is born, a live one with two or three survives) run from the
    five-cell R-pentomino on a board large enough that nothing reaches its edge; the view is centred on where the pattern
    settles, one cell per dpx."""
    steps = steps or (0, 120, gens)
    n = 640
    B = np.zeros((n, n), np.uint8)
    c = n // 2
    for y, x in ((0, 1), (0, 2), (1, 0), (1, 1), (2, 1)):
        B[c - 1 + y, c - 1 + x] = 1
    shots, t = [], 0
    vw, vh = view
    cy, cx = c + 6, c + 12
    for target in steps:
        while t < target:
            P = np.pad(B, 1)
            N = P[:-2, :-2] + P[:-2, 1:-1] + P[:-2, 2:] + P[1:-1, :-2] + P[1:-1, 2:] + P[2:, :-2] + P[2:, 1:-1] + P[2:, 2:]
            B = ((N == 3) | ((B == 1) & (N == 2))).astype(np.uint8)
            t += 1
        crop = B[cy - vh // 2:cy + vh - vh // 2, cx - vw // 2:cx + vw - vw // 2].astype(float)
        shots.append(np.kron(crop, np.ones((cell, cell))))
    return shots


def sand(w: int = 160, h: int = 90, steps=(0, 45, 400)) -> list[np.ndarray]:
    """Falling sand: every pixel is a material. A grain moves down into an empty pixel, else down to one side, alternating
    sides each step; stone never moves. A shelf of sand loses its support and collapses into the room below."""
    STONE, SAND = 2, 1
    M = np.zeros((h, w), np.uint8)
    M[-4:, :] = STONE
    M[:, :3] = STONE
    M[:, -3:] = STONE
    M[30:34, 20:140] = STONE
    M[30:34, 60:100] = 0                                  # the support gives way here
    M[8:30, 40:120] = SAND
    M[60:86, 100:106] = STONE                             # a pillar in the room below
    shots, t = [], 0
    for target in steps:
        while t < target:
            side = 1 if t % 2 else -1
            for y in range(h - 2, -1, -1):
                row = np.nonzero(M[y] == SAND)[0]
                for x in (row if side > 0 else row[::-1]):
                    if M[y + 1, x] == 0:
                        M[y, x], M[y + 1, x] = 0, SAND
                    elif 0 < x + side < w and M[y + 1, x + side] == 0:
                        M[y, x], M[y + 1, x + side] = 0, SAND
                    elif 0 < x - side < w and M[y + 1, x - side] == 0:
                        M[y, x], M[y + 1, x - side] = 0, SAND
            t += 1
        shots.append(np.where(M == STONE, 0.85, np.where(M == SAND, 0.4, 0.0)))
    return shots


def wfc(cw: int = 20, ch: int = 11, cell: int = 8, steps=(0.0, 0.35, 1.0)) -> list[np.ndarray]:
    """Wave-function collapse on a tile grid: every cell starts able to be water, sand, or grass; the cell with the fewest
    options left is fixed next (ties to the first), and its neighbours drop the options that can't sit beside it
    (water only touches water and sand, grass only grass and sand). Choices come from a fixed hash, so the same first
    tile always gives the same map."""
    WATER, SANDT, GRASS = 0, 1, 2
    ok = {WATER: {WATER, SANDT}, SANDT: {WATER, SANDT, GRASS}, GRASS: {SANDT, GRASS}}
    opts = [[{WATER, SANDT, GRASS} for _ in range(cw)] for _ in range(ch)]
    fixed = {}
    order = []
    def prop(y, x):
        stack = [(y, x)]
        while stack:
            y, x = stack.pop()
            for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ny, nx = y + dy, x + dx
                if 0 <= ny < ch and 0 <= nx < cw:
                    allowed = set().union(*(ok[v] for v in opts[y][x]))
                    new = opts[ny][nx] & allowed
                    if new != opts[ny][nx]:
                        opts[ny][nx] = new or {SANDT}
                        stack.append((ny, nx))
    opts[5][4] = {WATER}; fixed[(5, 4)] = WATER; order.append((5, 4)); prop(5, 4)   # the one placed tile
    while len(fixed) < cw * ch:
        y, x = min(((y, x) for y in range(ch) for x in range(cw) if (y, x) not in fixed), key=lambda p: (len(opts[p[0]][p[1]]), p))
        choices = sorted(opts[y][x])
        v = choices[(y * 31 + x * 17 + len(fixed) * 7) % len(choices)]
        opts[y][x] = {v}; fixed[(y, x)] = v; order.append((y, x)); prop(y, x)
    tone = {WATER: 0.75, SANDT: 0.2, GRASS: 0.45}
    shots = []
    for s in steps:
        k = int(round(s * len(order)))
        f = np.zeros((ch, cw))
        for (y, x) in order[:max(1, k)]:
            f[y, x] = tone[fixed[(y, x)]]
        big = np.kron(f, np.ones((cell, cell)))
        big[::cell, :] = np.minimum(big[::cell, :], 0.08)   # the tile grid
        big[:, ::cell] = np.minimum(big[:, ::cell], 0.08)
        shots.append(big)
    return shots
