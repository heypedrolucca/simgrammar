"""Turn a parsed script into timed visual states and an audio plan.

States are snapshots between change points: header, figure, on-screen text, cards, caption. Scene length is
lead + narration audio + tail; inside a scene, text positions map linearly onto the narration's duration."""
import json, re, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from entities import load, find
from figmap import FIG, CARDS

LEAD, TAIL, SILENT = 0.5, 0.8, 4.0
WPS = 135 / 60.0

def prefix(key):
    b = os.path.basename(key)
    return 'th' if b.startswith('the-film') else b[:2] if key.startswith('episodes') else 's' + b[:3]

def sentences(text):
    parts = re.split(r'(?<=[.!?])\s+(?=[A-Z0-9"“‘])', text.strip())
    out = []
    for p in parts:
        while len(p) > 120:
            cut = max((p.rfind(sep, 40, 110) for sep in (', ', '; ', ': ')), default=-1)
            if cut < 0: break
            out.append(p[:cut + 1]); p = p[cut + 2:]
        out.append(p)
    return [x for x in out if x]

def scene_plan(E, key, sc, dur_audio, LEAD=LEAD, TAIL=TAIL, SILENT=SILENT):
    pfx = prefix(key)
    blocks = sc['blocks']
    voices = [b['text'] for b in blocks if b['kind'] == 'voice']
    full = '\n\n'.join(voices)
    if voices:
        est = len(' '.join(voices).split()) / WPS
        A = dur_audio if dur_audio else est
        T = LEAD + A + TAIL
    else:
        A, T = 0.0, SILENT
    C = max(len(full), 1)
    tpos = lambda ch: LEAD + A * ch / C
    events = []   # (t, kind, payload)
    offs, pos = [], 0
    for v in voices: offs.append(pos); pos += len(v) + 2
    vi = 0
    pending = []  # picture/onscreen blocks waiting for the next voice paragraph
    def flush(t):
        for i, b in pending:
            pid = f"{pfx}.{sc['n']}.{i}"
            if b['kind'] == 'picture':
                events.append((t, 'picture', {'fig': FIG.get(pid), 'pid': pid}))
                for (p, k, eid) in find(E, b['text']):
                    if k == 'game': events.append((t + 0.001, 'card', (k, eid)))
                for k, eid in CARDS.get(pid, []): events.append((t + 0.002, 'card', (k, eid)))
            else:
                events.append((t, 'onscreen', b['text']))
        pending.clear()
    for i, b in enumerate(blocks):
        if b['kind'] == 'voice':
            t0 = tpos(offs[vi]); flush(t0 if vi else 0.0)
            # captions and mentions
            text = b['text']; base = offs[vi]
            cpos = 0
            for s in sentences(text):
                j = text.find(s, cpos); j = cpos if j < 0 else j
                events.append((tpos(base + j), 'caption', s)); cpos = j + len(s)
            for (p, k, eid) in find(E, text):
                events.append((tpos(base + p), 'card', (k, eid)))
            vi += 1
        else:
            pending.append((i, b))
    flush(tpos(C) if voices else 0.0)
    events.append((T - (TAIL * 0.6 if voices else 0), 'caption', ''))
    return T, sorted(events, key=lambda e: e[0])

def build(key, script, durs=None, header=None, drop_title=False, drop_last=False, maxcards=3, only=None, lead=LEAD, tail=TAIL, silent=SILENT):
    E = load()
    states, audio = [], []
    scenes = script['scenes']
    if drop_title: scenes = [s for s in scenes if not (s['n'] == 2 and not any(b['kind'] == 'voice' for b in s['blocks']))]
    if drop_last: scenes = scenes[:-1]
    if only: scenes = [s for s in scenes if s['n'] in only]
    for sc in scenes:
        skey = f"{key}#{sc['n']}"
        da = (durs or {}).get(skey)
        T, ev = scene_plan(E, key, sc, da, lead, tail, silent)
        st = {'header': header or script['title'], 'scene': sc['title'], 'fig': None, 'onscreen': '', 'cards': [], 'active': None, 'caption': '',
              'slate': not any(b['kind'] == 'voice' for b in sc['blocks'])}
        cur_t, snaps = 0.0, []
        for t, kind, p in ev:
            t = min(max(t, 0.0), T)
            if t > cur_t + 1e-3: snaps.append((cur_t, t, json.loads(json.dumps(st)))); cur_t = t
            if kind == 'picture':
                st['fig'] = p['fig']; st['onscreen'] = ''
                if p['fig']: st['cards'] = []; st['active'] = None
            elif kind == 'onscreen': st['onscreen'] = p
            elif kind == 'caption': st['caption'] = p
            elif kind == 'card':
                if st['fig']: continue
                k, eid = p
                ent = E[k][eid]; cid = f"{k}:{eid}"
                ids = [c['cid'] for c in st['cards']]
                if cid in ids: st['active'] = cid; continue
                st['cards'].append(dict(ent, cid=cid)); st['cards'] = st['cards'][-maxcards:]; st['active'] = cid
        if T > cur_t + 1e-3: snaps.append((cur_t, T, st))
        for a, b, s in snaps: states.append(dict(s, dur=round(b - a, 3)))
        audio.append({'key': skey, 'has_voice': any(b['kind'] == 'voice' for b in sc['blocks']), 'T': T, 'lead': lead, 'A': da or 0})
    return states, audio

if __name__ == '__main__':
    S = json.load(open(os.path.join(os.environ.get('SIMGRAMMAR_VIDEO_OUT', os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'video-out')), 'scripts.json')))
    k = 'episodes/01-same-parts.md'
    st, au = build(k, S[k])
    print(len(st), round(sum(s['dur'] for s in st), 1))
    for s in st[:12]: print(s['dur'], s['fig'], [c['cid'] for c in s['cards']], s['onscreen'][:40], '|', s['caption'][:60])
