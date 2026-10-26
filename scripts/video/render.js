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
  await p.evaluate(([v, dir, vis]) => { if (v) document.body.classList.add('v'); FIGDIR = dir; VISDIR = vis; }, [!!vert, path.resolve(figDir), path.resolve(figDir, '..', '..', 'visual')]);
  await p.evaluate(() => document.fonts.ready);
  // the fonts are vendored (media/fonts); stop rather than render in a fallback face
  const faces = ['400 20px "IBM Plex Sans"', '500 20px "IBM Plex Sans"', '600 20px "IBM Plex Sans"', '400 20px "IBM Plex Mono"', '500 20px "IBM Plex Mono"'];
  await p.evaluate(fs => Promise.all(fs.map(f => document.fonts.load(f))), faces);
  const missing = await p.evaluate(fs => fs.filter(f => !document.fonts.check(f) || ![...document.fonts].some(x => x.status === 'loaded' && f.includes(x.family.replace(/"/g, '')))), faces);
  if (missing.length) throw new Error('fonts not loaded: ' + missing.join(', '));
  const grid = JSON.parse(fs.readFileSync(gridFile, 'utf8'));
  await p.evaluate(g => { GRID = g; NCOL = g.ncol; NGAME = g.rows.length; MAXN = g.maxn; }, grid);
  let prev = null, n = 0; const list = [];
  for (let i = 0; i < states.length; i++) {
    const s = states[i]; const sig = JSON.stringify({ ...s, dur: 0 });
    if (sig === prev && list.length) { list[list.length - 1].dur += s.dur; continue; }
    prev = sig;
    await p.evaluate(x => show(x), s);
    await p.waitForFunction(() => [...document.images].every(im => im.complete));
    const broken = await p.evaluate(() => [...document.images].filter(im => !im.naturalWidth).map(im => im.src));
    if (broken.length) throw new Error('missing images: ' + broken.slice(0, 3).join(', '));
    const f = path.join(outDir, `s${String(n).padStart(5, '0')}.png`);
    await p.screenshot({ path: f }); list.push({ f, dur: s.dur }); n++;
  }
  let txt = ''; for (const x of list) txt += `file '${x.f}'\nduration ${Math.max(x.dur, 0.04).toFixed(3)}\n`;
  txt += `file '${list[list.length - 1].f}'\n`;
  fs.writeFileSync(path.join(outDir, 'concat.txt'), txt);
  console.log('stills', n, 'seconds', list.reduce((a, x) => a + x.dur, 0).toFixed(1));
  await b.close();
})();
