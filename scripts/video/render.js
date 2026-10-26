// node render.js states.json outdir figdir grid.json [v]
const { chromium } = require('playwright'); const fs = require('fs'); const path = require('path');
(async () => {
  const [ , , statesFile, outDir, figDir, gridFile, vert] = process.argv;
  const states = JSON.parse(fs.readFileSync(statesFile, 'utf8'));
  fs.mkdirSync(outDir, { recursive: true });
  const b = await chromium.launch();
  const W = vert ? 1080 : 1920, H = vert ? 1920 : 1080;
  const p = await b.newPage({ viewport: { width: W, height: H } });
  await p.goto('file://' + path.resolve(__dirname, 'render.html'), { waitUntil: 'networkidle' });
  await p.evaluate(([v, dir, vis, sized]) => { if (v) document.body.classList.add('v'); FIGDIR = dir; VISDIR = vis; SIZEDIR = sized; },
    [!!vert, path.resolve(figDir), path.resolve(figDir, '..', '..', 'visual'), path.resolve(path.dirname(gridFile), 'visual', 'icons')]);
  await p.evaluate(() => document.fonts.ready);
  // the fonts are vendored (media/fonts); stop rather than render in a fallback face
  const faces = ['400 20px "IBM Plex Sans"', '500 20px "IBM Plex Sans"', '600 20px "IBM Plex Sans"', '400 20px "IBM Plex Mono"', '500 20px "IBM Plex Mono"'];
  await p.evaluate(fs => Promise.all(fs.map(f => document.fonts.load(f))), faces);
  const missing = await p.evaluate(fs => fs.filter(f => !document.fonts.check(f) || ![...document.fonts].some(x => x.status === 'loaded' && f.includes(x.family.replace(/"/g, '')))), faces);
  if (missing.length) throw new Error('fonts not loaded: ' + missing.join(', '));
  const grid = JSON.parse(fs.readFileSync(gridFile, 'utf8'));
  await p.evaluate(g => { GRID = g; NCOL = g.ncol; NGAME = g.rows.length; MAXN = g.maxn; }, grid);
  // Motion (ADR-0006): a new frame builds in, a changed frame or a moved highlight cross-dissolves. The steps are 1/30 s
  // stills taken out of the start of the state's own duration, so the cut points and the total length do not move.
  const STEP = 1 / 30, MOTION = !process.env.SIMGRAMMAR_NO_MOTION;   // SIMGRAMMAR_NO_MOTION=1: final stills only, for previews
  let prev = null, prevState = null, n = 0; const list = [];
  const shot = async (dur) => {
    await p.waitForFunction(() => [...document.images].every(im => im.complete));
    const broken = await p.evaluate(() => [...document.images].filter(im => !im.naturalWidth).map(im => im.src));
    if (broken.length) throw new Error('missing images: ' + broken.slice(0, 3).join(', '));
    const f = path.join(outDir, `s${String(n).padStart(5, '0')}.png`);
    await p.screenshot({ path: f }); list.push({ f, dur }); n++;
  };
  const merged = [];
  for (const s of states) {
    const sig = JSON.stringify({ ...s, dur: 0 });
    if (merged.length && sig === merged[merged.length - 1].sig) { merged[merged.length - 1].s.dur += s.dur; continue; }
    merged.push({ sig, s: { ...s } });
  }
  let steps = 0;
  for (const { s } of merged) {
    let mode = null;
    if (s.frame) {
      const pf = prevState && prevState.frame;
      if (!pf) mode = 'build';
      else if (JSON.stringify(pf) !== JSON.stringify(s.frame)) mode = pf.t === s.frame.t ? 'xfade' : 'build';
      else if (JSON.stringify(prevState.current) !== JSON.stringify(s.current)) mode = 'xfade';
    }
    const maxK = Math.floor((s.dur - 0.25) / STEP);
    if (mode === 'xfade') await p.evaluate(() => keepOld());
    await p.evaluate(x => show(x), s);
    let K = 0;
    if (MOTION && mode && maxK >= 3) {
      await p.waitForFunction(() => [...document.images].every(im => im.complete));
      K = await p.evaluate(([m, k]) => transPrep(m, k), [mode, maxK]);
      for (let k = 0; k < K; k++) { await p.evaluate(k => transStep(k), k); await shot(STEP); }
    }
    await p.evaluate(() => transEnd());
    await shot(K ? s.dur - K * STEP : s.dur);
    steps += K; prevState = s;
  }
  let txt = ''; for (const x of list) txt += `file '${x.f}'\nduration ${(x.dur === STEP ? x.dur : Math.max(x.dur, 0.04)).toFixed(6)}\n`;
  txt += `file '${list[list.length - 1].f}'\n`;
  fs.writeFileSync(path.join(outDir, 'concat.txt'), txt);
  console.log('stills', n, 'motion steps', steps, 'seconds', list.reduce((a, x) => a + x.dur, 0).toFixed(1));
  await b.close();
})();
