// Frame templates for render.html (ADR-0006). Each takes the frame resolved by framedata.py, the ids that are current,
// and the stage size, and returns HTML. Pictures are pre-dithered icons at 3 px per dither pixel (16:9) or 4 px (9:16):
// the icon's own size comes from dist/visual, larger draws (72 to 144 dpx, redrawn from the vector) from the render's
// icon cache. Text stays vector. Nothing here computes a number: framedata.py read them from the dataset.
//
// Layout units carry class f-u: render.html snaps each unit so its first icon sits on the 8-dpx grid (the Bayer pattern
// repeats every 8 dpx, so neighbouring sprites line up), and builds units in document order (motion, render.js).
let VISDIR = "", SIZEDIR = "";
const VERT = () => document.body.classList.contains("v");
const PX = () => (VERT() ? 4 : 3);
const G = () => 8 * PX();
const ic = (e, on, dpx, cls = "") => {
  if (!e || !e.icon) return tile(e, on, dpx, cls);
  const n = dpx || e.size, acc = on ? ".accent" : "";
  const src = n === e.size ? `${VISDIR}/icons/${e.icon}${acc}@${PX()}x.png` : `${SIZEDIR}/${e.icon}${acc}.${n}@${PX()}x.png`;
  return `<img class="f-ic ${cls}" src="${src}" width="${n * PX()}" height="${n * PX()}" alt="">`;
};
// an element with no icon yet is a type tile of the same size, never a broken picture
const tile = (e, on, dpx, cls = "") => {
  const n = (dpx || 48) * PX();
  return `<div class="f-ic f-tic ${cls}${on ? " on" : ""}" style="width:${n}px;height:${n}px"><span>${esc(e ? e.label || e.id || "" : "")}</span></div>`;
};
const isOn = (cur, id) => (cur || []).includes(id);
const bar = (n, N, on) => `<span class="f-bar${on ? " on" : ""}"><i data-w="${Math.max(2, 100 * n / N).toFixed(1)}" style="width:${Math.max(2, 100 * n / N).toFixed(1)}%"></i></span>`;
const cnt = (n) => `<span class="f-cnt" data-n="${n}">${n}</span>`;
const games = (n, N) => `${cnt(n)} of ${N} games`;
// draw size for n items in a row of width w: the largest of 144..48 dpx that leaves room for labels
const fit = (n, w, opts = {}) => {
  const max = opts.max || 96, min = opts.min || 48, pad = opts.pad || 0.72;
  for (const d of [144, 120, 96, 72, 48]) if (d <= max && d >= min && n * d * PX() <= w * pad) return d;
  return min;
};

// the first option whose layout fits, else the last
const pick = (opts, fits) => opts.find(fits) || opts[opts.length - 1];

const T = {};

T.anatomy = (f, cur, W, H) => {
  const n = f.parts.length, v = VERT();
  const yr = p => f.dates && p.year ? `<div class="f-mono">${p.year}${p.first ? " · " + esc(p.first) : ""}</div>` : `<div class="f-mono">${games(p.n, f.N)}</div>`;
  if (v) {
    const P = PX();
    const [d, sd] = pick([[72, 96], [72, 72], [48, 96], [48, 72], [42, 72], [42, 48]].filter(([d]) => d < 72 || n <= 4), ([d, sd]) => {
      const rows = d >= 72 ? n : Math.ceil(n / 2);
      return sd * P + 40 + rows * d * P + (rows - 1) * (d >= 72 ? 28 : 34) <= H;
    });
    const parts = f.parts.map(p => `<div class="f-prow f-u">${ic(p, isOn(cur, p.id), d)}<div><div class="f-lab${isOn(cur, p.id) ? " acc" : ""}">${esc(p.label)}</div>${yr(p)}${f.dates ? "" : bar(p.n, f.N, isOn(cur, p.id))}</div></div>`).join("");
    return `<div class="f-anat v${d >= 72 ? " one" : ""}"><div class="f-subjrow f-u">${ic({ icon: f.subject, size: 96, label: f.name }, false, sd)}<div><div class="f-name">${esc(f.name)}</div><div class="f-mono">${esc(f.meta)}</div><div class="f-mono ink">${esc(f.counts)}</div></div></div><div class="f-pgrid">${parts}</div></div>`;
  }
  const d = n <= 8 ? 72 : 48;
  const parts = f.parts.map(p => `<div class="f-part f-u">${ic(p, isOn(cur, p.id), d)}<div class="f-lab${isOn(cur, p.id) ? " acc" : ""}">${esc(p.label)}</div>${yr(p)}${f.dates ? "" : bar(p.n, f.N, isOn(cur, p.id))}<div class="f-tick${isOn(cur, p.id) ? " on" : ""}"></div></div>`).join("");
  return `<div class="f-anat${d === 72 ? " f-big" : ""}"><div class="f-parts">${parts}</div><div class="f-bus" style="left:${50 / n}%;right:${50 / n}%"></div><div class="f-stem"></div>
  <div class="f-subj"><div class="f-u">${ic({ icon: f.subject, size: 96, label: f.name }, false, 96)}</div><div class="f-subjtext f-u"><div class="f-name">${esc(f.name)}</div><div class="f-mono">${esc(f.meta)}</div><div class="f-mono ink">${esc(f.counts)}</div></div>
  <div class="f-key f-mono">${f.dates ? "year: first catalog game to use the part" : `core: a different game without it<br>bar: share of the ${f.N} catalog games`}</div></div></div>`;
};

T.hub = (f, cur, W, H) => {
  const v = VERT(), d = 72, S = PX() * d;
  const two = f.spokes.length <= 2;
  const cx = W / 2, cy = H * (two ? (v ? 0.68 : 0.64) : 0.5);
  const pos = two
    ? (v ? [[0.25, 0.2], [0.75, 0.2]] : [[0.2, 0.28], [0.8, 0.28]])
    : (v ? [[0.24, 0.18], [0.76, 0.18], [0.24, 0.84], [0.76, 0.84]] : [[0.17, 0.2], [0.83, 0.2], [0.17, 0.8], [0.83, 0.8]]);
  const maxw = Math.max(...f.spokes.map(s => s.w));
  let lines = "", items = "";
  f.spokes.forEach((s, k) => {
    const [px, py] = pos[k % pos.length]; const x = px * W, y = py * H;
    const dx = x - cx, dy = y - cy, dd = Math.hypot(dx, dy), ux = dx / dd, uy = dy / dd;
    const on = isOn(cur, s.id), w = 3 + 15 * (s.w / maxw) ** 2;
    lines += `<line class="f-draw" x1="${(cx + ux * S * 0.72).toFixed(1)}" y1="${(cy + uy * S * 0.72).toFixed(1)}" x2="${(x - ux * S * 0.7).toFixed(1)}" y2="${(y - uy * S * 0.7).toFixed(1)}" stroke="${on ? "#0550ae" : "#3d3d38"}" stroke-width="${w.toFixed(1)}" stroke-linecap="round"/>`;
    const up = py < 0.5;
    const txt = `<div class="f-lab${on ? " acc" : ""}">${esc(s.label)}</div><div class="f-mono${on ? " acc" : ""}">advertises ${esc(s.need)}</div>`;
    const th = v ? 112 : 96;
    items += `<div class="f-spoke f-u" style="left:${x - 200}px;top:${up ? y - S / 2 - th : y - S / 2}px">${up ? txt : ""}${ic(s, on, d)}${up ? "" : txt}</div>`;
  });
  return `<div class="f-hub" style="width:${W}px;height:${H}px"><svg width="${W}" height="${H}">${lines}</svg>${items}
  <div class="f-hubc f-u" style="left:${cx - S / 2}px;top:${cy - S / 2}px">${ic(f.hub, false, d)}</div>
  ${f.weights ? `<div class="f-mono faint f-wnote" style="left:${cx - 200}px;top:${cy + S / 2 + 18}px">${esc(f.weights)}</div>` : ""}</div>`;
};

T.blank = (f, cur, W, H) => {
  const v = VERT(), d = v ? 48 : 72;
  if (v) {
    const slots = Array.from({ length: f.slots }, () => `<div class="f-prow f-u"><div class="f-slot" style="width:${d * PX()}px;height:${d * PX()}px"></div><div><div class="f-lab faint">a part</div><div class="f-mono faint">core or supporting · games using it</div></div></div>`).join("");
    return `<div class="f-anat v"><div class="f-subjrow f-u"><div class="f-slot" style="width:${96 * PX()}px;height:${72 * PX()}px"></div><div><div class="f-name faint">${esc(f.label)}</div><div class="f-mono">list its parts · mark the core ones · count the games</div></div></div><div class="f-pgrid">${slots}</div></div>`;
  }
  const slots = Array.from({ length: f.slots }, () => `<div class="f-part f-u"><div class="f-slot" style="width:${d * PX()}px;height:${d * PX()}px"></div><div class="f-lab faint">a part</div><div class="f-mono faint">core or supporting<br>games using it</div><div class="f-tick"></div></div>`).join("");
  return `<div class="f-anat f-big"><div class="f-parts">${slots}</div><div class="f-bus" style="left:${50 / f.slots}%;right:${50 / f.slots}%"></div><div class="f-stem"></div>
  <div class="f-subj"><div class="f-slot f-u" style="width:${96 * PX()}px;height:${72 * PX()}px"></div><div class="f-subjtext f-u"><div class="f-name faint">${esc(f.label)}</div><div class="f-mono">list its parts · mark the core ones · count the games</div></div></div></div>`;
};

const arrow = (len, on, vert) => {   // len = 0: stretch to fill the link
  const c = on ? " on" : "";
  return vert ? `<div class="f-arr v${c}" style="${len ? `height:${len}px` : ""}"><i></i><b></b></div>` : `<div class="f-arr${c}" style="${len ? `width:${len}px` : ""}"><i></i><b></b></div>`;
};

T.chain = (f, cur, W, H) => {
  const v = VERT();
  const strip = f.strip && f.strip.length ? `<div class="f-strip">${f.strip.map(x => `<span class="${x.on ? "acc" : "faint"}">${esc(x.text)}</span>`).join('<span class="f-dot"> · </span>')}</div>` : "";
  const title = f.title ? `<div class="f-mono ink f-title">${esc(f.title)}</div>` : "";
  const two = f.rows.length > 1;
  const most = Math.max(...f.rows.map(r => r.nodes.length));
  const nn = f.rows.reduce((a, r) => a + r.nodes.length, 0);
  const avail = H - (strip ? 80 : 0) - (title ? 44 : 0) - (f.rows.some(r => r.links.some(l => l.sign)) ? 56 : 0) - f.rows.filter(r => r.loop).length * 60;
  const [d, lh] = v ? pick([[72, 96], [48, 96], [48, 72], [42, 64], [42, 52]], ([d, lh]) => nn * d * PX() + (nn - f.rows.length) * lh <= avail) : [two || most > 4 ? 48 : 72, 0];
  const node = (nd) => {
    const on = isOn(cur, nd.id);
    return `<div class="f-node f-u${two ? " sm" : ""}">${ic(nd, on, d)}<div class="f-ntext"><div class="f-lab${on ? " acc" : ""}">${esc(nd.label)}</div>${nd.note && !two && !(v && d < 72 && nn > 3) ? `<div class="f-mono f-note">${esc(nd.note)}</div>` : ""}${nd.n != null ? `<div class="f-mono ink">${nd.mname ? esc(nd.mname.toLowerCase()) + " · " : ""}in ${cnt(nd.n)} of ${f.N} games</div>` : ""}</div></div>`;
  };
  const link = (lk, on) => `<div class="f-link"${v ? ` style="height:${lh}px;padding-left:${d * PX() / 2 - 12}px"` : ""}>${lk.verb ? `<div class="f-mono${on ? " acc" : ""} f-verb">${esc(lk.verb)}</div>` : ""}<div class="f-arrow">${arrow(v ? lh - 24 : 0, on, v)}${lk.sign ? `<span class="f-sign${on ? " on" : ""}">${esc(lk.sign)}</span>` : ""}</div></div>`;
  const rows = f.rows.map(r => {
    let h = "";
    r.nodes.forEach((nd, k) => {
      h += node(nd);
      if (k < r.nodes.length - 1) h += link(r.links[k], isOn(cur, r.nodes[k + 1].id));
    });
    const lp = r.loop ? `<div class="f-loop f-u"><div class="f-loopline"></div><div class="f-mono ink">${r.loop === "R" ? "reinforcing loop" : "balancing loop"}${r.links[r.nodes.length - 1] && r.links[r.nodes.length - 1].sign ? ` <span class="f-sign sm">${esc(r.links[r.nodes.length - 1].sign)}</span>` : ""}${r.links[r.nodes.length - 1] && r.links[r.nodes.length - 1].verb ? ` · ${esc(r.links[r.nodes.length - 1].verb)}` : ""}</div></div>` : "";
    return `<div class="f-crow">${h}</div>${lp}`;
  }).join("");
  return `<div class="f-chain${v ? " v" : ""}${two ? " two" : ""}${d > 48 ? " f-big" : ""}">${strip}${title}<div class="f-rows">${rows}</div>${f.rows.some(r => r.links.some(l => l.sign)) ? `<div class="f-mono faint f-legend">signs: + same direction · − opposite direction</div>` : ""}</div>`;
};

T.compare = (f, cur, W, H) => {
  const v = VERT();
  const most = Math.max(f.a.items.length, f.b.items.length);
  const d = v ? (most <= 3 ? 72 : 48) : (most <= 2 ? 96 : most <= 3 ? 72 : 48);
  const col = (c) => `<div class="f-col"><div class="f-ctitle f-u">${esc(c.title)}</div><div class="f-citems">${c.items.map(e => `<div class="f-citem f-u">${ic(e, isOn(cur, e.id), d)}<div class="f-lab${isOn(cur, e.id) ? " acc" : ""}">${esc(e.label)}</div></div>`).join("")}</div></div>`;
  return `<div class="f-compare${v ? " v" : ""}"><div class="f-cols">${col(f.a)}<div class="f-vrule"></div>${col(f.b)}</div>${f.note ? `<div class="f-mono f-cnote f-u">record: ${esc(f.note)}</div>` : ""}</div>`;
};

T.bars = (f, cur, W, H) => {
  const v = VERT(), d = v ? pick([72, 48, 42], d => f.items.length * (d * PX() + 20) <= H) : (f.items.length <= 4 ? 72 : 48);
  const items = f.items.map(e => {
    const on = isOn(cur, e.id);
    return `<div class="f-bitem f-u">${f.rank ? `<div class="f-rank${on ? " acc" : ""}">${e.rank}</div>` : ""}${ic(e, on, d)}<div class="f-btext"><div class="f-lab${on ? " acc" : ""}">${esc(e.label)}</div><div class="f-num${on ? " acc" : ""}">${cnt(e.n)}<small> of ${f.N} ${esc(f.of || "games")}</small></div>${bar(e.n, f.N, on)}</div></div>`;
  }).join("");
  return `<div class="f-bars${v ? " v" : ""}${f.items.length <= 4 ? " few" : ""}">${items}</div>`;
};

T.tiles = (f, cur, W, H) => `<div class="f-tiles${VERT() ? " v" : ""}"><div class="f-thead f-u">${ic({ icon: f.icon, size: 48, label: f.family }, false, 72)}<div><div class="f-name">${esc(f.family)}</div><div class="f-mono ink">${esc(f.summary)}</div></div></div>
  <div class="f-tgrid">${f.tiles.map(t => `<div class="f-tile f-u${t.lit ? " lit" : ""}"><div class="f-tl">${esc(t.label)}</div><div class="f-mono">${f.lits === false ? "" : (t.lit ? "a technique points here" : "none") + " · "}${t.n} games${t.year ? " · first " + t.year : ""}</div></div>`).join("")}</div></div>`;

T.roles = (f, cur, W, H) => {
  const max = Math.max(...f.hist.core, ...f.hist.supporting), hh = VERT() ? 380 : 420;
  const hist = (k, title) => `<div class="f-hist f-u"><div class="f-lab">${title}</div><div class="f-mono">${f.uses[k]} uses · median ${f.med[k]} games</div><div class="f-hbars" style="height:${hh}px">${f.hist[k].map((c, i) => `<div class="f-hcol"><div class="f-mono ink">${cnt(c)}</div><div class="f-hbar${k === "core" ? " on" : ""}" style="height:${(hh * 0.8 * c / max).toFixed(0)}px"></div><div class="f-mono">${f.bins[i]}</div></div>`).join("")}</div><div class="f-mono faint">games using the mechanic</div></div>`;
  return `<div class="f-roles${VERT() ? " v" : ""}">${hist("core", "Core parts")}${hist("supporting", "Supporting parts")}</div>`;
};

T.timeline = (f, cur, W, H) => {
  const v = VERT();
  const groups = [];
  [...f.items].sort((a, b) => a.year - b.year).forEach(e => { const g = groups.find(g => g.year === e.year); g ? g.items.push(e) : groups.push({ year: e.year, items: [e] }); });
  const firsts = g => [...new Set(g.items.map(e => e.first).filter(Boolean))].join(", ");
  if (v) {   // 9:16: a vertical axis, oldest at the top
    const d = f.items.length <= 5 ? 72 : 48;
    const rows = groups.map(g => {
      const on = g.items.some(e => isOn(cur, e.id));
      return `<div class="f-vtrow f-u"><div class="f-vty${on ? " acc" : ""}">${g.year}</div><div class="f-vtdot${on ? " on" : ""}"></div><div class="f-vtitems">${g.items.map(e => `<div class="f-vti">${ic(e, isOn(cur, e.id), d)}<div class="f-lab${isOn(cur, e.id) ? " acc" : ""}">${esc(e.label)}</div></div>`).join("")}${firsts(g) ? `<div class="f-mono">${esc(firsts(g))}</div>` : ""}</div></div>`;
    }).join("");
    return `<div class="f-vtimeline"><div class="f-vtaxis"></div>${rows}<div class="f-mono faint f-tcap2">${esc(f.cap || "first catalog game to use each part")}</div></div>`;
  }
  const x = y => 120 + (W - 240) * (y - f.lo) / (f.hi - f.lo);
  const d = f.items.length <= 5 && groups.length >= f.items.length - 1 ? 72 : 48, iw = d === 72 ? 240 : 200;
  let ticks = "";
  for (let y = f.lo; y <= f.hi; y += f.step || 10) ticks += `<div class="f-ttick" style="left:${x(y)}px"><span class="f-mono">${y}</span></div>`;
  const ends = [], laneH = Math.min(d === 72 ? 330 : 260, (H - 170) / 2);
  const html = groups.map(g => {
    const w = g.items.length * iw, left = Math.min(Math.max(x(g.year) - w / 2, 0), W - w);
    let lane = 0; while (ends[lane] !== undefined && left < ends[lane] + 20) lane++;
    ends[lane] = left + w;
    const on = g.items.some(e => isOn(cur, e.id));
    return `<div class="f-tgroup f-u" style="left:${left}px;width:${w}px;bottom:${150 + lane * laneH}px;z-index:${10 - lane}"><div class="f-tgi">${g.items.map(e => `<div class="f-titem" style="width:${iw}px">${ic(e, isOn(cur, e.id), d)}<div class="f-lab sm${isOn(cur, e.id) ? " acc" : ""}">${esc(e.label)}</div></div>`).join("")}</div>
      <div class="f-mono${on ? " acc" : " ink"}">${g.year}${firsts(g) ? " · " + esc(firsts(g)) : ""}</div><div class="f-tpin${on ? " on" : ""}" style="left:${x(g.year) - left}px;height:${lane * laneH + 40}px"></div></div>`;
  }).join("");
  return `<div class="f-timeline" style="width:${W}px;height:${H}px"><div class="f-axis" style="left:120px;width:${W - 240}px"></div>${ticks}${html}<div class="f-mono faint f-tcap">${esc(f.cap || "first catalog game to use each part")}</div></div>`;
};

T.formula = (f, cur, W, H) => {
  const v = VERT(), n = f.terms.length + 1, d = v ? (n <= 3 ? 72 : 48) : (n <= 4 ? 96 : 72);
  const term = (x) => x.const ? `<div class="f-fterm f-u"><div class="f-const" style="line-height:${d * PX()}px">${esc(x.const)}</div></div>` : `<div class="f-fterm f-u">${ic(x, isOn(cur, x.id), d)}<div class="f-lab${isOn(cur, x.id) ? " acc" : ""}">${esc(x.label)}</div></div>`;
  const parts = f.terms.map((x, k) => `${k || x.op ? `<div class="f-op" style="line-height:${d * PX()}px">${esc(x.op || "+")}</div>` : ""}${term(x)}`).join("");
  return `<div class="f-formula${v ? " v" : ""}"><div class="f-frow">${term(f.result)}<div class="f-op" style="line-height:${d * PX()}px">=</div>${parts}</div>${f.note ? `<div class="f-mono f-cnote f-u">record: ${esc(f.note)}</div>` : ""}</div>`;
};

T.scale = (f, cur, W, H) => {
  const v = VERT();
  return `<div class="f-scale${v ? " v" : ""}"><div class="f-thead f-u">${ic(f.mech, true, 72)}<div><div class="f-name">${esc(f.mech.label)}</div><div class="f-mono ink">${esc(f.field)}: ${f.value} of ${f.levels.length}</div><div class="f-mono">${esc(f.question)}</div></div></div>
  <div class="f-ruler"><div class="f-rail"></div>${f.levels.map(l => `<div class="f-level f-u${l.n === f.value ? " on" : ""}"><div class="f-ln">${l.n}</div><div class="f-lt">${esc(l.text)}</div></div>`).join("")}</div></div>`;
};

T.record = (f, cur, W, H) => `<div class="f-record${VERT() ? " v" : ""}"><div class="f-thead f-u">${ic(f.mech, true, 72)}<div><div class="f-mono">${esc(f.kicker || "mechanic · " + f.family)}</div><div class="f-name">${esc(f.mech.label)}</div></div></div>
  <div class="f-rrows">${f.rows.map(([k, vals]) => `<div class="f-rrow f-u"><div class="f-mono f-rk">${esc(k)}</div><div class="f-rv">${vals.slice(0, 3).map(x => `<div>${esc(x)}</div>`).join("")}</div></div>`).join("")}</div>
  ${f.stamps.length ? `<div class="f-stamps">${f.stamps.map(s => `<div class="f-stamp f-u">${esc(s.toLowerCase())}</div>`).join("")}</div>` : ""}</div>`;

T.moment = (f, cur, W, H) => {
  const v = VERT(), n = f.panels.length, most = Math.max(...f.panels.map(p => p.icons.length));
  const d = v ? pick(most > 1 ? [72, 48, 42] : [96, 72, 48, 42], d => (most > 1 && d * PX() * most + 16 * (most - 1) > W * 0.55 ? false : true) && n * d * PX() + (n - 1) * 72 <= H - 50)
    : (most > 1 ? (n <= 3 ? 72 : 48) : (n <= 3 ? 120 : 96));
  return `<div class="f-moment${v ? " v" : ""}"><div class="f-mono faint f-mlabel">${esc(f.label)}</div><div class="f-panels">${f.panels.map((p, k) => `<div class="f-panel f-u"><div class="f-mono f-pk">${k + 1}</div><div class="f-pics">${p.icons.map(e => ic(e, isOn(cur, e.id), d)).join("")}</div><div class="f-pcap">${esc(p.caption)}</div></div>`).join('<div class="f-pnext">' + arrow(v ? 48 : 64, false, v) + "</div>")}</div></div>`;
};

T.toysim = (f, cur, W, H) => `<div class="f-toysim${VERT() ? " v" : ""}"><div class="f-thead f-u">${ic(f.mech, true, 72)}<div><div class="f-mono faint">${esc(f.label)}</div><div class="f-name">${esc(f.mech.label)}</div><div class="f-mono f-note3">record: ${esc(f.note)}</div></div></div>
  <div class="f-plates">${f.plates.map((p, j) => `<div class="f-plate f-u"><img class="f-ic" src="${p}@${PX()}x.png" width="${f.w * PX()}" height="${f.h * PX()}" alt=""><div class="f-mono">${esc(f.caps[j] || "")}</div></div>`).join("")}</div></div>`;

function frameHTML(f, cur, W, H) { return (T[f.t] || (() => `<div class="f-mono">no template ${esc(f.t)}</div>`))(f, cur, W, H); }
