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
