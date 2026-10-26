"""Resolve a **Frame.** line into what render.html's templates draw (ADR-0006).

Every number a frame shows is read here from dist/entities, dist/analysis/stats.json, or vocab/rubrics.yaml, and every
frame carries a source line saying where. Labels the script gives (a panel caption, "Zone growth") are prose and are
linted with the script. The grammar is scripts/visual/frames.py; scripts/visual/check.py validates the same lines (E040).
"""
import json, os, re, sys, hashlib
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'scripts'))
from visual import frames as FR, toysim, dither  # noqa: E402
import yaml  # noqa: E402

DIST = os.path.join(ROOT, 'dist')
_cache = {}


def data():
    if 'd' not in _cache:
        live = lambda n: {x['id']: x for x in json.load(open(os.path.join(DIST, 'entities', n), encoding='utf-8')) if not x.get('deprecated')}
        voc = lambda n: {str(t['id']): t for t in yaml.safe_load(open(os.path.join(ROOT, 'vocab', n + '.yaml'), encoding='utf-8'))['terms']}
        _cache['d'] = {
            'G': live('games.json'), 'M': live('mechanics.json'), 'T': live('techniques.json'),
            'stats': json.load(open(os.path.join(DIST, 'analysis', 'stats.json'), encoding='utf-8')),
            'icons': json.load(open(os.path.join(DIST, 'visual', 'icons.json'), encoding='utf-8')),
            'rubrics': yaml.safe_load(open(os.path.join(ROOT, 'vocab', 'rubrics.yaml'), encoding='utf-8'))['scales'],
            'family': voc('mechanic_family'), 'subgenre': voc('subgenre'),
        }
    return _cache['d']


def label(i):
    D = data(); ic = D['icons'].get(i, {})
    if ic.get('label'):
        return ic['label']
    if i in D['M']:
        return D['M'][i]['name']
    for k in ('family', 'subgenre'):
        if i in D[k]:
            return D[k][i].get('label', i)
    return i


def names(i, extra=()):
    """Words in narration that point at element i (its label, record name and aliases, the vocab aliases)."""
    D = data(); out = {label(i)} | set(extra)
    if i in D['M']:
        out |= {D['M'][i]['name']} | {a for a in D['M'][i].get('aliases') or [] if len(a) >= 5}
    out |= set(D['icons'].get(i, {}).get('aliases') or [])
    from entities import EXTRA, STOP_ALIASES
    out |= {k for k, (kind, eid) in EXTRA.items() if eid == i}
    return sorted(n for n in out if n and n.lower() not in STOP_ALIASES)


def el(i, lab='', **kw):
    D = data()
    m = D['M'].get(i)
    return dict({'id': i, 'icon': i if i in D['icons'] else None, 'label': lab or label(i), 'size': D['icons'].get(i, {}).get('size', 48),
                 'mname': m['name'] if m and lab and lab != m['name'] else ''}, **kw)


def game_meta(g):
    D = data()
    sub = D['subgenre'].get(g.get('subgenre'), {}).get('label', g.get('subgenre', '')).lower()
    return f"{g.get('year')} · {str(g.get('developer', '')).lower()} · {sub}"


def chip_game(gid):
    g = data()['G'][gid]
    core = sum(1 for u in g['mechanics'] if u.get('role') == 'core')
    return f"game · {g['name']} · {game_meta(g)} · {len(g['mechanics'])} parts, {core} core"


def chip_mech(mid):
    D = data(); m = D['M'][mid]
    return f"mechanic · {m['name']} · {D['family'][m['family']]['label'].lower()} · in {m['_derived'].get('prevalence', 0)} of {len(D['G'])} games"


def use_note(gid, mid):
    g = data()['G'].get(gid) or {}
    for u in g.get('mechanics', []):
        if u['id'] == mid:
            return u.get('note') or ''
    return ''


def resolve(text, scene_onscreen='', out_dir=None):
    t, a = FR.parse(text)
    D = data(); NG = len(D['G'])
    f = {'t': t, 'current': [], 'elements': [], 'chip': '', 'source': '', 'label': ''}
    cur = [i for i, _ in FR.items(a.get('current', ''))]
    prev = lambda i: D['M'][i]['_derived'].get('prevalence', 0)

    if t == 'anatomy' and 'game' in a:
        g = D['G'][a['game']]
        want = a.get('parts', 'core')
        ids = [u['id'] for u in g['mechanics'] if want == 'all' or (want == 'core' and u.get('role') == 'core')] if want in ('core', 'all') else [i for i, _ in FR.items(want)]
        f.update(t='anatomy', name=g['name'], meta=game_meta(g), N=NG,
                 counts=f"{len(g['mechanics'])} parts · {sum(1 for u in g['mechanics'] if u.get('role') == 'core')} core · {sum(1 for u in g['mechanics'] if u.get('role') != 'core')} supporting",
                 subject=g.get('subgenre') if g.get('subgenre') in D['icons'] else None,
                 parts=[el(i, n=prev(i)) for i in ids], chip=chip_game(a['game']),
                 source=f"counts: catalog games using each part · {a['game']} record")
        f['elements'] = ids
    elif t == 'anatomy' and 'hub' in a:
        sp = FR.items(a['spokes'])
        gid, _, mid = a.get('from', ':').partition(':')
        f.update(t='hub', hub=el(a['hub']), spokes=[el(i, label(i), need=lab, w=len(sp) - k) for k, (i, lab) in enumerate(sp)],
                 weights='line weight: offer × need (illustrative)' if a.get('weights') else '', note=use_note(gid, mid) if mid else '',
                 chip=chip_mech(mid) if mid in D['M'] else '', source=f"objects and needs: {gid} record, {mid}" if mid else '')
        f['elements'] = [i for i, _ in sp]
    elif t == 'anatomy':
        f.update(t='blank', slots=6, label='your game')
    elif t == 'chain':
        gid = a.get('from', '')
        rows = FR.rows(a['nodes'])
        sg = [r.split(',') for r in a.get('signs', '').split('|')] if a.get('signs') else [[] for _ in rows]
        verbs = [v for r in a.get('verbs', '').split('|') for v, _ in FR.items(r)]
        loops = [x for x, _ in FR.items(a.get('loops', ''))]
        vi = 0; out_rows = []
        for r, row in enumerate(rows):
            nodes = []
            for k, (i, lab) in enumerate(row):
                note = use_note(gid, i) if gid and i in D['M'] else ''
                nodes.append(el(i, lab, note=note, n=prev(i) if i in D['M'] else None))
            links = []
            for k in range(len(row) - 1 + (1 if r < len(loops) and loops[r] else 0)):
                s = (sg[r][k] if r < len(sg) and k < len(sg[r]) else '').strip()
                links.append({'sign': {'-': '−', '+': '+'}.get(s, s), 'verb': verbs[vi] if vi < len(verbs) else ''}); vi += 1
            out_rows.append({'nodes': nodes, 'links': links, 'loop': loops[r] if r < len(loops) else ''})
        strip = []
        if a.get('strip'):
            items = [x.strip().rstrip('.') for x in re.split(r'(?<=\.)\s+', scene_onscreen) if x.strip()]
            strip = [{'text': x.lower(), 'on': x.lower().startswith(a['strip'].lower())} for x in items]
        g = D['G'].get(gid)
        f.update(rows=out_rows, strip=strip, title=f"{g['name'].lower()} · {g['year']}" if g else '', N=NG,
                 chip=chip_game(gid) if g else '', source=(f"rules: {gid} record" + (" · counts: catalog games" if any(n['n'] for r in out_rows for n in r['nodes']) else '')) if g else 'counts: catalog games')
        f['elements'] = [n['id'] for r in out_rows for n in r['nodes']]
    elif t == 'compare':
        gid, _, mid = a.get('from', ':').partition(':')
        f.update(a={'title': a['a'], 'items': [el(i, lab) for i, lab in FR.items(a['a_items'])]},
                 b={'title': a['b'], 'items': [el(i, lab) for i, lab in FR.items(a['b_items'])]},
                 note=use_note(gid, mid) if mid else '', chip=chip_game(gid) if gid in D['G'] else '',
                 source=f"{gid} record, {mid}" if mid else '')
        f['elements'] = [i for i, _ in FR.items(a['a_items']) + FR.items(a['b_items'])]
    elif t == 'count' and a['kind'] == 'bars':
        ids = [i for i, _ in FR.items(a['ids'])]
        f.update(t='bars', N=NG, items=[el(i, n=prev(i), rank=D['M'][i]['_derived'].get('prevalence_rank')) for i in ids], rank=bool(a.get('rank')),
                 source='counts: catalog games using each mechanic · ranks: prevalence_rank')
        f['elements'] = ids
    elif t == 'count' and a['kind'] == 'tiles':
        fam = a['family']
        ms = sorted((m for m in D['M'].values() if m['family'] == fam), key=lambda m: (-prev(m['id']), m['id']))
        hit = {x['id'] for tq in D['T'].values() for x in tq.get('affects', [])}
        tiles = [{'label': m['name'], 'lit': m['id'] in hit, 'n': prev(m['id'])} for m in ms]
        f.update(t='tiles', family=D['family'][fam]['label'], icon=fam if fam in D['icons'] else None, tiles=tiles,
                 summary=f"{sum(1 for x in tiles if not x['lit'])} of {len(tiles)} have no AI technique pointed at them",
                 source='mechanics of the family, and the techniques whose affects edges name them')
    elif t == 'count' and a['kind'] == 'roles':
        prevs = {'core': [], 'supporting': []}
        for g in D['G'].values():
            for u in g['mechanics']:
                if u['id'] in D['M']:
                    prevs['core' if u.get('role') == 'core' else 'supporting'].append(prev(u['id']))
        bins = [(1, 5), (6, 10), (11, 20), (21, 40), (41, 999)]
        hist = {k: [sum(1 for p in v if lo <= p <= hi) for lo, hi in bins] for k, v in prevs.items()}
        med = {k: D['stats'][f'median_prevalence_{k}_uses'] for k in prevs}
        f.update(t='roles', bins=[f"{lo}–{hi}" if hi < 999 else f"{lo}+" for lo, hi in bins], hist=hist, med=med,
                 uses={k: len(v) for k, v in prevs.items()},
                 source='uses of each mechanic, by how many catalog games use it · medians: stats median_prevalence_core_uses, median_prevalence_supporting_uses')
    elif t == 'timeline':
        ids = [i for i, _ in FR.items(a['ids'])]
        items = []
        for i in ids:
            d = D['M'][i]['_derived']
            items.append(el(i, year=d.get('earliest_year'), first=D['G'].get(d.get('earliest_game'), {}).get('name', '')))
        ys = [x['year'] for x in items]
        f.update(items=items, lo=(min(ys) // 10) * 10, hi=(max(ys) // 10 + 1) * 10, source='first catalog game for each mechanic: earliest_year, earliest_game')
        f['elements'] = ids
    elif t == 'formula':
        gid, _, mid = a['from'].partition(':')
        r = FR.items(a['result'])[0]
        terms = [{'op': {'-': '−', '+': '+', '×': '×'}.get(op, op), 'const': i if FR.NUMBER.match(i) else '', **({} if FR.NUMBER.match(i) else el(i, lab))} for op, i, lab in FR.terms(a['terms'])]
        f.update(result=el(*r), terms=terms, note=use_note(gid, mid), chip=chip_game(gid) if gid in D['G'] else '', source=f"rule: {gid} record, {mid}")
        f['elements'] = [x['id'] for x in terms if x.get('id')] + [r[0]]
    elif t == 'scale':
        mid, _, fld = a['field'].partition('.')
        sc = D['rubrics'][fld]; m = D['M'][mid]
        f.update(mech=el(mid), field=fld.replace('_', ' '), question=sc['question'], value=m[fld],
                 levels=[{'n': int(k), 'text': v} for k, v in sorted(sc['levels'].items(), key=lambda kv: int(kv[0]))],
                 chip=chip_mech(mid), source=f"score: {mid} record, {fld} · anchors: vocab/rubrics.yaml")
    elif t == 'record':
        mid = a['mechanic']; m = D['M'][mid]
        fields = [x for x, _ in FR.items(a.get('fields', 'definition,design_levers'))]
        rows = []
        for fl in fields:
            v = m.get(fl)
            if isinstance(v, list):
                rows.append([fl.replace('_', ' '), v])
            elif v:
                rows.append([fl.replace('_', ' '), [re.split(r'(?<=\.)\s', str(v))[0]]])
        stamps = [x.strip().rstrip('.') for x in re.split(r'(?<=\.)\s+', a['stamps'] if a.get('stamps') and a['stamps'] != 'onscreen' else scene_onscreen) if x.strip()] if a.get('stamps') else []
        f.update(mech=el(mid), family=D['family'][m['family']]['label'].lower(), rows=rows, stamps=stamps, chip=chip_mech(mid), source=f"{mid} record: " + ", ".join(fields))
    elif t == 'moment':
        f.update(panels=[{'icons': [el(i) for i in ics], 'caption': cap} for ics, cap in FR.panels(a['panels'])],
                 subject=el(a['subject']) if a.get('subject') else None, label='drawn from the narration, not game footage')
    elif t == 'toysim':
        gid, _, mid = a['from'].partition(':')
        num = lambda k, d: float(a[k].rstrip('%')) / (100 if a[k].endswith('%') else 1) if k in a else d
        if a['sim'] == 'heat':
            shots = toysim.heat(tick=num('tick', 0.2))
        else:
            shots = toysim.chunks(rate=num('rate', 0.02), threshold=num('threshold', 15.0))
        files = []
        if out_dir:
            os.makedirs(out_dir, exist_ok=True)
            key = hashlib.sha256(text.encode()).hexdigest()[:12]
            for k, s in enumerate(shots):
                rgba = dither.tonal(s)
                for sc in (3, 4):
                    p = os.path.join(out_dir, f'{a["sim"]}-{key}-{k}@{sc}x.png')
                    open(p, 'wb').write(dither.png(rgba, sc))
                files.append(os.path.join(out_dir, f'{a["sim"]}-{key}-{k}'))
        f.update(plates=files, w=int(shots[0].shape[1]), h=int(shots[0].shape[0]), caps=['start', 'later', 'much later'],
                 mech=el(mid), note=use_note(gid, mid), chip=chip_game(gid) if gid in D['G'] else '',
                 source=f"rule: {gid} record, {mid} · drawn by a toy simulation of that rule, not the game",
                 label='toy simulation of the rule')
    f['current'] = cur or ([f['elements'][0]] if t in () else [])
    f['names'] = {i: names(i) for i in f['elements']}
    return f
