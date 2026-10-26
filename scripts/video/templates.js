// Frame templates for render.html (ADR-0006). Each takes the frame resolved by framedata.py, the ids that are current,
// and the stage size, and returns HTML. Pictures are pre-dithered icons from dist/visual at 3 px per dither pixel (16:9)
// or 4 px (9:16); text stays vector. Nothing here computes a number: framedata.py read them from the dataset.
let VISDIR = "";
const VERT = () => document.body.classList.contains("v");
const PX = () => (VERT() ? 4 : 3);
const ic = (e, on, cls = "") => e && e.icon
  ? `<img class="f-ic ${cls}" src="${VISDIR}/icons/${e.icon}${on ? ".accent" : ""}@${PX()}x.png" width="${e.size * PX()}" height="${e.size * PX()}" alt="">`
  : `<div class="f-ic f-missing" style="width:${48 * PX()}px;height:${48 * PX()}px"></div>`;
const isOn = (cur, id) => (cur || []).includes(id);
const bar = (n, N, on) => `<span class="f-bar${on ? " on" : ""}"><i style="width:${Math.max(2, 100 * n / N).toFixed(1)}%"></i></span>`;
const games = (n, N) => `${n} of ${N} games`;

const T = {};

T.anatomy = (f, cur, W, H) => {
  const n = f.parts.length;
  if (VERT()) {
    const parts = f.parts.map(p => `<div class="f-prow">${ic(p, isOn(cur, p.id))}<div><div class="f-lab${isOn(cur, p.id) ? " acc" : ""}">${esc(p.label)}</div><div class="f-mono">${games(p.n, f.N)}</div>${bar(p.n, f.N, isOn(cur, p.id))}</div></div>`).join("");
    return `<div class="f-anat v"><div class="f-subjrow">${ic({ icon: f.subject, size: 96 }, false)}<div><div class="f-name">${esc(f.name)}</div><div class="f-mono">${esc(f.meta)}</div><div class="f-mono ink">${esc(f.counts)}</div></div></div><div class="f-pgrid">${parts}</div></div>`;
  }
  const parts = f.parts.map(p => `<div class="f-part">${ic(p, isOn(cur, p.id))}<div class="f-lab${isOn(cur, p.id) ? " acc" : ""}">${esc(p.label)}</div><div class="f-mono">${games(p.n, f.N)}</div>${bar(p.n, f.N, isOn(cur, p.id))}<div class="f-tick${isOn(cur, p.id) ? " on" : ""}"></div></div>`).join("");
  return `<div class="f-anat"><div class="f-parts">${parts}</div><div class="f-bus" style="left:${50 / n}%;right:${50 / n}%"></div><div class="f-stem"></div>
  <div class="f-subj">${ic({ icon: f.subject, size: 96 }, false)}<div class="f-subjtext"><div class="f-name">${esc(f.name)}</div><div class="f-mono">${esc(f.meta)}</div><div class="f-mono ink">${esc(f.counts)}</div></div>
  <div class="f-key f-mono">core: a different game without it<br>bar: share of the ${f.N} catalog games</div></div></div>`;
};

T.hub = (f, cur, W, H) => {
  const v = VERT(), S = PX() * 48;
  const cx = W / 2, cy = H * (f.spokes.length <= 2 ? (v ? 0.58 : 0.62) : 0.5);
  const pos = f.spokes.length <= 2
    ? (v ? [[0.25, 0.22], [0.75, 0.22]] : [[0.2, 0.3], [0.8, 0.3]])
    : (v ? [[0.24, 0.2], [0.76, 0.2], [0.24, 0.8], [0.76, 0.8]] : [[0.17, 0.22], [0.83, 0.22], [0.17, 0.78], [0.83, 0.78]]);
  const maxw = Math.max(...f.spokes.map(s => s.w));
  let lines = "", items = "";
  f.spokes.forEach((s, k) => {
    const [px, py] = pos[k % pos.length]; const x = px * W, y = py * H;
    const dx = x - cx, dy = y - cy, d = Math.hypot(dx, dy), ux = dx / d, uy = dy / d;
    const on = isOn(cur, s.id), w = 2 + 14 * (s.w / maxw) ** 2;
    lines += `<line x1="${cx + ux * (S * 0.75)}" y1="${cy + uy * (S * 0.75)}" x2="${x - ux * S * 0.72}" y2="${y - uy * S * 0.72}" stroke="${on ? "#0550ae" : "#3d3d38"}" stroke-width="${w.toFixed(1)}" stroke-linecap="round"/>`;
    const up = py < 0.5;
    const txt = `<div class="f-lab${on ? " acc" : ""}">${esc(s.label)}</div><div class="f-mono${on ? " acc" : ""}">advertises ${esc(s.need)}</div>`;
    items += `<div class="f-spoke" style="left:${x - 170}px;top:${up ? y - S / 2 - (v ? 112 : 92) : y - S / 2}px">${up ? txt : ""}${ic(s, on)}${up ? "" : txt}</div>`;
  });
  return `<div class="f-hub" style="width:${W}px;height:${H}px"><svg width="${W}" height="${H}">${lines}</svg>${items}
  <div class="f-hubc" style="left:${cx - S / 2}px;top:${cy - S / 2}px">${ic(f.hub, false)}</div>
  ${f.weights ? `<div class="f-mono faint f-wnote" style="left:${cx - 150}px;top:${cy + S / 2 + 16}px">${esc(f.weights)}</div>` : ""}</div>`;
};

T.blank = (f, cur, W, H) => {
  const slots = Array.from({ length: f.slots }, () => `<div class="f-part"><div class="f-slot" style="width:${48 * PX()}px;height:${48 * PX()}px"></div><div class="f-mono">a part</div><div class="f-mono faint">core or supporting<br>games using it</div><div class="f-tick"></div></div>`).join("");
  return `<div class="f-anat"><div class="f-parts">${slots}</div><div class="f-bus" style="left:${50 / f.slots}%;right:${50 / f.slots}%"></div><div class="f-stem"></div>
  <div class="f-subj"><div class="f-slot" style="width:${96 * PX()}px;height:${96 * PX() * 0.75}px"></div><div class="f-subjtext"><div class="f-name faint">${esc(f.label)}</div><div class="f-mono">list its parts · mark the core ones · count the games</div></div></div></div>`;
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
  const node = (nd) => {
    const on = isOn(cur, nd.id);
    return `<div class="f-node${two ? " sm" : ""}">${ic(nd, on)}<div class="f-ntext"><div class="f-lab${on ? " acc" : ""}">${esc(nd.label)}</div>${nd.note && !two ? `<div class="f-mono f-note">${esc(nd.note)}</div>` : ""}${nd.n != null ? `<div class="f-mono ink">${nd.mname ? esc(nd.mname.toLowerCase()) + " · " : ""}in ${nd.n} of ${f.N} games</div>` : ""}</div></div>`;
  };
  const link = (lk, on) => `<div class="f-link">${lk.verb ? `<div class="f-mono${on ? " acc" : ""} f-verb">${esc(lk.verb)}</div>` : ""}<div class="f-arrow">${arrow(v ? 76 : 0, on, v)}${lk.sign ? `<span class="f-sign${on ? " on" : ""}">${esc(lk.sign)}</span>` : ""}</div></div>`;
  const rows = f.rows.map(r => {
    let h = "";
    r.nodes.forEach((nd, k) => {
      h += node(nd);
      if (k < r.nodes.length - 1) h += link(r.links[k], isOn(cur, r.nodes[k + 1].id));
    });
    const lp = r.loop ? `<div class="f-loop"><div class="f-loopline"></div><div class="f-mono ink">${r.loop === "R" ? "reinforcing loop" : "balancing loop"}${r.links[r.nodes.length - 1] && r.links[r.nodes.length - 1].sign ? ` <span class="f-sign sm">${esc(r.links[r.nodes.length - 1].sign)}</span>` : ""}${r.links[r.nodes.length - 1] && r.links[r.nodes.length - 1].verb ? ` · ${esc(r.links[r.nodes.length - 1].verb)}` : ""}</div></div>` : "";
    return `<div class="f-crow">${h}</div>${lp}`;
  }).join("");
  return `<div class="f-chain${v ? " v" : ""}${two ? " two" : ""}">${strip}${title}<div class="f-rows">${rows}</div>${f.rows.some(r => r.links.some(l => l.sign)) ? `<div class="f-mono faint f-legend">signs: + same direction · − opposite direction</div>` : ""}</div>`;
};

T.compare = (f, cur, W, H) => {
  const col = (c) => `<div class="f-col"><div class="f-ctitle">${esc(c.title)}</div><div class="f-citems">${c.items.map(e => `<div class="f-citem">${ic(e, isOn(cur, e.id))}<div class="f-lab${isOn(cur, e.id) ? " acc" : ""}">${esc(e.label)}</div></div>`).join("")}</div></div>`;
  return `<div class="f-compare${VERT() ? " v" : ""}"><div class="f-cols">${col(f.a)}<div class="f-vrule"></div>${col(f.b)}</div>${f.note ? `<div class="f-mono f-cnote">record: ${esc(f.note)}</div>` : ""}</div>`;
};

T.bars = (f, cur, W, H) => {
  const items = f.items.map(e => {
    const on = isOn(cur, e.id);
    return `<div class="f-bitem">${f.rank ? `<div class="f-rank${on ? " acc" : ""}">${e.rank}</div>` : ""}${ic(e, on)}<div class="f-btext"><div class="f-lab${on ? " acc" : ""}">${esc(e.label)}</div><div class="f-num${on ? " acc" : ""}">${e.n}<small> of ${f.N} games</small></div>${bar(e.n, f.N, on)}</div></div>`;
  }).join("");
  return `<div class="f-bars${VERT() ? " v" : ""}">${items}</div>`;
};

T.tiles = (f, cur, W, H) => `<div class="f-tiles${VERT() ? " v" : ""}"><div class="f-thead">${ic({ icon: f.icon, size: 48 }, false)}<div><div class="f-name">${esc(f.family)}</div><div class="f-mono ink">${esc(f.summary)}</div></div></div>
  <div class="f-tgrid">${f.tiles.map(t => `<div class="f-tile${t.lit ? " lit" : ""}"><div class="f-tl">${esc(t.label)}</div><div class="f-mono">${t.lit ? "a technique points here" : "none"} · ${t.n} games</div></div>`).join("")}</div></div>`;

T.roles = (f, cur, W, H) => {
  const max = Math.max(...f.hist.core, ...f.hist.supporting);
  const hist = (k, title) => `<div class="f-hist"><div class="f-lab">${title}</div><div class="f-mono">${f.uses[k]} uses · median ${f.med[k]} games</div><div class="f-hbars">${f.hist[k].map((c, i) => `<div class="f-hcol"><div class="f-mono ink">${c}</div><div class="f-hbar${k === "core" ? " on" : ""}" style="height:${(330 * c / max).toFixed(0)}px"></div><div class="f-mono">${f.bins[i]}</div></div>`).join("")}</div><div class="f-mono faint">games using the mechanic</div></div>`;
  return `<div class="f-roles">${hist("core", "Core parts")}${hist("supporting", "Supporting parts")}</div>`;
};

T.timeline = (f, cur, W, H) => {
  const x = y => 120 + (W - 240) * (y - f.lo) / (f.hi - f.lo);
  const groups = [];
  [...f.items].sort((a, b) => a.year - b.year).forEach(e => { const g = groups.find(g => g.year === e.year); g ? g.items.push(e) : groups.push({ year: e.year, items: [e] }); });
  let ticks = "";
  for (let y = f.lo; y <= f.hi; y += 10) ticks += `<div class="f-ttick" style="left:${x(y)}px"><span class="f-mono">${y}</span></div>`;
  const ends = [], laneH = Math.min(260, (H - 170) / 2);
  const html = groups.map(g => {
    const w = g.items.length * 200, left = Math.min(Math.max(x(g.year) - w / 2, 0), W - w);
    let lane = 0; while (ends[lane] !== undefined && left < ends[lane] + 20) lane++;
    ends[lane] = left + w;
    const on = g.items.some(e => isOn(cur, e.id));
    const firsts = [...new Set(g.items.map(e => e.first))].join(", ");
    return `<div class="f-tgroup" style="left:${left}px;width:${w}px;bottom:${150 + lane * laneH}px;z-index:${10 - lane}"><div class="f-tgi">${g.items.map(e => `<div class="f-titem">${ic(e, isOn(cur, e.id))}<div class="f-lab sm${isOn(cur, e.id) ? " acc" : ""}">${esc(e.label)}</div></div>`).join("")}</div>
      <div class="f-mono${on ? " acc" : " ink"}">${g.year} · ${esc(firsts)}</div><div class="f-tpin${on ? " on" : ""}" style="left:${x(g.year) - left}px;height:${lane * laneH + 40}px"></div></div>`;
  }).join("");
  return `<div class="f-timeline" style="width:${W}px;height:${H}px"><div class="f-axis" style="left:120px;width:${W - 240}px"></div>${ticks}${html}<div class="f-mono faint f-tcap">first catalog game to use each part</div></div>`;
};

T.formula = (f, cur, W, H) => {
  const term = (x) => x.const ? `<div class="f-fterm"><div class="f-const">${esc(x.const)}</div></div>` : `<div class="f-fterm">${ic(x, isOn(cur, x.id))}<div class="f-lab${isOn(cur, x.id) ? " acc" : ""}">${esc(x.label)}</div></div>`;
  const parts = f.terms.map((x, k) => `${k || x.op ? `<div class="f-op">${esc(x.op || "+")}</div>` : ""}${term(x)}`).join("");
  return `<div class="f-formula${VERT() ? " v" : ""}"><div class="f-frow">${term(f.result)}<div class="f-op">=</div>${parts}</div>${f.note ? `<div class="f-mono f-cnote">record: ${esc(f.note)}</div>` : ""}</div>`;
};

T.scale = (f, cur, W, H) => `<div class="f-scale${VERT() ? " v" : ""}"><div class="f-thead">${ic(f.mech, true)}<div><div class="f-name">${esc(f.mech.label)}</div><div class="f-mono ink">${esc(f.field)}: ${f.value} of ${f.levels.length}</div><div class="f-mono">${esc(f.question)}</div></div></div>
  <div class="f-levels">${f.levels.map(l => `<div class="f-level${l.n === f.value ? " on" : ""}"><div class="f-ln">${l.n}</div><div class="f-lt">${esc(l.text)}</div></div>`).join("")}</div></div>`;

T.record = (f, cur, W, H) => `<div class="f-record${VERT() ? " v" : ""}"><div class="f-thead">${ic(f.mech, true)}<div><div class="f-mono">mechanic · ${esc(f.family)}</div><div class="f-name">${esc(f.mech.label)}</div></div></div>
  <div class="f-rrows">${f.rows.map(([k, vals]) => `<div class="f-rrow"><div class="f-mono f-rk">${esc(k)}</div><div class="f-rv">${vals.slice(0, 3).map(x => `<div>${esc(x)}</div>`).join("")}</div></div>`).join("")}</div>
  ${f.stamps.length ? `<div class="f-stamps">${f.stamps.map(s => `<div class="f-stamp">${esc(s.toLowerCase())}</div>`).join("")}</div>` : ""}</div>`;

T.moment = (f, cur, W, H) => `<div class="f-moment${VERT() ? " v" : ""}"><div class="f-mono faint f-mlabel">${esc(f.label)}</div><div class="f-panels">${f.panels.map((p, k) => `<div class="f-panel"><div class="f-mono">${k + 1}</div><div class="f-pics">${p.icons.map(e => ic(e, false)).join("")}</div><div class="f-pcap">${esc(p.caption)}</div></div>`).join('<div class="f-pnext">' + arrow(VERT() ? 40 : 56, false, VERT()) + "</div>")}</div></div>`;

T.toysim = (f, cur, W, H) => `<div class="f-toysim"><div class="f-thead">${ic(f.mech, true)}<div><div class="f-mono faint">${esc(f.label)}</div><div class="f-name">${esc(f.mech.label)}</div><div class="f-mono f-note3">record: ${esc(f.note)}</div></div></div>
  <div class="f-plates">${f.plates.map((p, k) => `<div class="f-plate"><img class="f-ic" src="${p}@${PX()}x.png" width="${f.w * PX()}" height="${f.h * PX()}" alt=""><div class="f-mono">${esc(f.caps[k] || "")}</div></div>`).join("")}</div></div>`;

function frameHTML(f, cur, W, H) { return (T[f.t] || (() => `<div class="f-mono">no template ${esc(f.t)}</div>`))(f, cur, W, H); }
