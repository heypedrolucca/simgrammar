/* simgrammar.js: progressive enhancement for the SimGrammar site.
   Every page is complete without this file. It adds: contents highlighting, sortable and
   filterable tables, and the hover, toggle, and readout layer of the paper's figures.
   Figures are fully laid out by scripts/viz.py; this file only toggles, highlights, and reads out.
   Labels come from the dataset and are inserted with textContent, never innerHTML. */
(function () {
  "use strict";
  var $ = function (sel, root) { return (root || document).querySelector(sel); };
  var $$ = function (sel, root) { return Array.prototype.slice.call((root || document).querySelectorAll(sel)); };

  function el(tag, attrs, text) {
    var n = document.createElement(tag);
    if (attrs) Object.keys(attrs).forEach(function (k) { n.setAttribute(k, attrs[k]); });
    if (text != null) n.textContent = text;
    return n;
  }
  function svgEl(tag, attrs) {
    var n = document.createElementNS("http://www.w3.org/2000/svg", tag);
    Object.keys(attrs || {}).forEach(function (k) { n.setAttribute(k, attrs[k]); });
    return n;
  }
  function svgPoint(svg, evt) {
    var p = svg.createSVGPoint();
    p.x = evt.clientX; p.y = evt.clientY;
    var m = svg.getScreenCTM();
    return m ? p.matrixTransform(m.inverse()) : { x: 0, y: 0 };
  }
  function link(type, id, text) {
    var a = el("a", { href: type + "/" + id + "/", "data-internal": "" }, text);
    return a;
  }
  // readout: a list of parts; strings become text nodes, nodes are appended as is
  function readout(fig, parts) {
    var r = $("[data-readout]", fig);
    if (!r) return;
    r.textContent = "";
    parts.forEach(function (p, i) {
      if (i) r.appendChild(document.createTextNode(" · "));
      if (typeof p === "string") r.appendChild(document.createTextNode(p));
      else r.appendChild(p);
    });
  }
  function bold(s) { return el("b", null, s); }
  function pressed(group, value) {
    $$("button", group).forEach(function (b) { b.setAttribute("aria-pressed", b.getAttribute("data-value") === value ? "true" : "false"); });
  }

  /* ---------------------------------------------------------------- contents */
  function toc() {
    var links = $$(".toc a[href^='#']");
    if (!links.length || !("IntersectionObserver" in window)) return;
    var map = {};
    links.forEach(function (a) { var t = document.getElementById(a.getAttribute("href").slice(1)); if (t) map[t.id] = a; });
    var obs = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting && map[e.target.id]) {
          links.forEach(function (a) { a.removeAttribute("aria-current"); });
          map[e.target.id].setAttribute("aria-current", "true");
        }
      });
    }, { rootMargin: "0px 0px -70% 0px" });
    Object.keys(map).forEach(function (id) { obs.observe(document.getElementById(id)); });
  }

  /* ---------------------------------------------------------------- tables */
  function tables() {
    $$("table[data-sortable]").forEach(function (table) {
      var ths = $$("thead th", table);
      ths.forEach(function (th, col) {
        th.setAttribute("tabindex", "0");
        th.style.cursor = "pointer";
        th.setAttribute("aria-sort", "none");
        var sort = function () {
          var asc = th.getAttribute("aria-sort") !== "ascending";
          ths.forEach(function (o) { o.setAttribute("aria-sort", "none"); });
          th.setAttribute("aria-sort", asc ? "ascending" : "descending");
          var body = table.tBodies[0];
          var rows = Array.prototype.slice.call(body.rows);
          var num = th.classList.contains("num");
          rows.sort(function (a, b) {
            var x = a.cells[col] ? a.cells[col].textContent.trim() : "";
            var y = b.cells[col] ? b.cells[col].textContent.trim() : "";
            if (num) { x = parseFloat(x); y = parseFloat(y); x = isNaN(x) ? -Infinity : x; y = isNaN(y) ? -Infinity : y; return asc ? x - y : y - x; }
            return asc ? x.localeCompare(y) : y.localeCompare(x);
          });
          rows.forEach(function (r) { body.appendChild(r); });
        };
        th.addEventListener("click", sort);
        th.addEventListener("keydown", function (e) { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); sort(); } });
      });
    });
    $$("[data-filter-controls]").forEach(function (c) {
      c.hidden = false;
      var input = $("[data-filter]", c);
      var table = $("table[data-filterable]");
      if (!input || !table) return;
      input.addEventListener("input", function () {
        var q = input.value.trim().toLowerCase();
        Array.prototype.forEach.call(table.tBodies[0].rows, function (r) { r.hidden = q && r.textContent.toLowerCase().indexOf(q) < 0; });
      });
    });
  }

  /* ---------------------------------------------------------------- figure: matrix */
  function matrix(fig, data, svg) {
    var mode = { rows: "cluster", cols: "family" };
    var cellRole = {};
    data.cells.forEach(function (c) { cellRole[c[0] * 1000 + c[1]] = c[2]; });
    var hlRow = $("[data-hl=row]", svg), hlCol = $("[data-hl=col]", svg);
    var rects = $$("rect[data-r]", svg);
    var pinned = false;
    function find(arr, v) {
      for (var i = 0; i < arr.length; i++) if (v >= arr[i] - 0.5 && v < arr[i] + data.pitch - 0.5) return i;
      return -1;
    }
    function apply() {
      rects.forEach(function (r) {
        r.setAttribute("x", data.colX[mode.cols][+r.getAttribute("data-c")]);
        r.setAttribute("y", data.rowY[mode.rows][+r.getAttribute("data-r")]);
      });
      ["cluster", "year"].forEach(function (m) { var g = $("[data-layer=rows-" + m + "]", svg); if (g) g.setAttribute("display", m === mode.rows ? "inline" : "none"); });
      ["family", "first"].forEach(function (m) { var g = $("[data-layer=cols-" + m + "]", svg); if (g) g.setAttribute("display", m === mode.cols ? "inline" : "none"); });
    }
    function show(r, c) {
      hlRow.setAttribute("display", r >= 0 ? "inline" : "none");
      hlCol.setAttribute("display", c >= 0 ? "inline" : "none");
      if (r >= 0) hlRow.setAttribute("y", data.rowY[mode.rows][r] - 0.5);
      if (c >= 0) hlCol.setAttribute("x", data.colX[mode.cols][c] - 0.5);
      if (r < 0 && c < 0) return;
      var parts = [];
      if (r >= 0) { var g = data.rows[r]; parts.push(link("game", g.id, g.name)); parts.push(String(g.year)); parts.push("cluster " + (g.cluster || "").toLowerCase()); }
      if (c >= 0) { var m = data.cols[c]; parts.push(link("mechanic", m.id, m.name)); parts.push(m.family.toLowerCase()); }
      if (r >= 0 && c >= 0) { var role = cellRole[r * 1000 + c]; parts.push(bold(role === 2 ? "core use" : role === 1 ? "supporting use" : "not used")); }
      readout(fig, parts);
    }
    svg.addEventListener("pointermove", function (e) {
      if (pinned) return;
      var p = svgPoint(svg, e);
      show(find(data.rowY[mode.rows], p.y), find(data.colX[mode.cols], p.x));
    });
    svg.addEventListener("click", function (e) { var p = svgPoint(svg, e); pinned = !pinned; if (!pinned) show(find(data.rowY[mode.rows], p.y), find(data.colX[mode.cols], p.x)); });
    $$("[data-controls=matrix] .segmented", fig).forEach(function (g) {
      g.addEventListener("click", function (e) {
        var b = e.target.closest("button"); if (!b) return;
        mode[b.getAttribute("data-set")] = b.getAttribute("data-value");
        pressed(g, b.getAttribute("data-value"));
        apply();
      });
    });
    readout(fig, ["hover a square to read it; click to pin"]);
  }

  /* ---------------------------------------------------------------- figure: strata */
  function strata(fig, data, svg) {
    var line = $("[data-hl=year]", svg);
    var range = $("[data-set=year]", fig);
    var span = data.right - data.left, n = data.y1 - data.y0 + 1;
    var activeLayer = null;
    function xOf(y) { return data.left + (y - data.y0) / n * span; }
    function setYear(y) {
      y = Math.max(data.y0, Math.min(data.y1, y));
      line.setAttribute("display", "inline");
      line.setAttribute("x1", xOf(y) + 1); line.setAttribute("x2", xOf(y) + 1);
      if (range) range.value = y;
      var total = data.total[data.years.indexOf(y)];
      var added = data.added[String(y)] || [];
      var parts = [bold(String(y)), total + " mechanics seen"];
      if (activeLayer) parts.unshift(activeLayer.getAttribute("data-label").toLowerCase() + ": " + activeLayer.getAttribute("data-count") + " mechanics, first in " + activeLayer.getAttribute("data-first"));
      if (added.length) {
        var games = {};
        added.forEach(function (a) { games[a[3]] = a[4]; });
        parts.push("+" + added.length + " new: " + added.slice(0, 6).map(function (a) { return a[1].toLowerCase(); }).join(", ") + (added.length > 6 ? ", …" : ""));
        var gs = Object.keys(games);
        parts.push(gs.length === 1 ? link("game", gs[0], games[gs[0]]) : "from " + gs.length + " games");
      } else parts.push("no new mechanics this year");
      readout(fig, parts);
    }
    svg.addEventListener("pointermove", function (e) {
      var p = svgPoint(svg, e);
      if (p.x < data.left || p.x > data.right) return;
      setYear(data.y0 + Math.floor((p.x - data.left) / span * n));
    });
    $$("path[data-family]", svg).forEach(function (pth) {
      pth.addEventListener("pointerenter", function () { activeLayer = pth; pth.setAttribute("data-fo", pth.getAttribute("fill-opacity")); pth.setAttribute("fill-opacity", "0.32"); });
      pth.addEventListener("pointerleave", function () { pth.setAttribute("fill-opacity", pth.getAttribute("data-fo")); activeLayer = null; });
    });
    $$("line[data-game]", svg).forEach(function (t) {
      t.style.cursor = "pointer";
      t.addEventListener("pointerenter", function () { var g = data.games[t.getAttribute("data-game")]; readout(fig, [link("game", t.getAttribute("data-game"), g[0]), String(g[1])]); });
    });
    if (range) range.addEventListener("input", function () { setYear(+range.value); });
    readout(fig, ["hover the layers or drag the year to read what each year added"]);
  }

  /* ---------------------------------------------------------------- figure: design map */
  function designMap(fig, data, svg) {
    var nodes = data.nodes;
    var rects = $$("rect[data-i]", svg);
    var hl = $("[data-hl=node]", svg);
    var links = $("[data-layer=links]", svg);
    var subLabel = {};
    data.subgenres.forEach(function (s) { subLabel[s[0]] = s[1]; });
    var pinned = false, current = -1, selected = "";
    function nearest(p) {
      var best = -1, bd = 22 * 22;
      for (var i = 0; i < nodes.length; i++) {
        var dx = nodes[i].x - p.x, dy = nodes[i].y - p.y, d = dx * dx + dy * dy;
        if (d < bd) { bd = d; best = i; }
      }
      return best;
    }
    function show(i) {
      current = i;
      while (links.firstChild) links.removeChild(links.firstChild);
      if (i < 0) { hl.setAttribute("display", "none"); if (!selected) readout(fig, ["hover a game to see its nearest neighbours; click to pin"]); return; }
      var n = nodes[i];
      hl.setAttribute("display", "inline"); hl.setAttribute("x", n.x - 6); hl.setAttribute("y", n.y - 6);
      n.n.forEach(function (j) { links.appendChild(svgEl("line", { x1: n.x, y1: n.y, x2: nodes[j].x, y2: nodes[j].y })); });
      var nb = el("span");
      n.n.forEach(function (j, k) { if (k) nb.appendChild(document.createTextNode(", ")); nb.appendChild(link("game", nodes[j].id, nodes[j].name)); });
      readout(fig, [link("game", n.id, n.name), String(n.year), (subLabel[n.sub] || n.sub).toLowerCase(), (n.cluster || "").toLowerCase() + " " + (data.clusters[n.cluster] || "").toLowerCase(), "nearest: ", nb]);
    }
    svg.addEventListener("pointermove", function (e) { if (!pinned) show(nearest(svgPoint(svg, e))); });
    svg.addEventListener("pointerleave", function () { if (!pinned) show(-1); });
    svg.addEventListener("click", function (e) { var i = nearest(svgPoint(svg, e)); pinned = i >= 0 && !(pinned && i === current); show(i); });
    var sel = $("[data-set=subgenre]", fig);
    if (sel) sel.addEventListener("change", function () {
      selected = sel.value;
      var counts = {};
      rects.forEach(function (r) {
        var n = nodes[+r.getAttribute("data-i")];
        var on = !selected || n.sub === selected;
        r.style.fill = selected && on ? "var(--accent)" : "";
        r.setAttribute("fill-opacity", on ? "1" : "0.18");
        if (selected && on) counts[n.cluster] = (counts[n.cluster] || 0) + 1;
      });
      if (!selected) { readout(fig, ["hover a game to see its nearest neighbours; click to pin"]); return; }
      var ks = Object.keys(counts).sort(function (a, b) { return counts[b] - counts[a] || (a < b ? -1 : 1); });
      var total = ks.reduce(function (s, k) { return s + counts[k]; }, 0);
      readout(fig, [bold((subLabel[selected] || selected).toLowerCase()), total + " games across " + ks.length + (ks.length === 1 ? " island" : " islands"),
        ks.map(function (k) { return k.toLowerCase() + " " + counts[k]; }).join(", ")]);
    });
    $$("[data-key]", svg).forEach(function (g) {
      var island = $("path[data-cluster='" + g.getAttribute("data-key") + "']", svg);
      g.addEventListener("pointerenter", function () { if (island) island.style.stroke = "var(--accent)"; });
      g.addEventListener("pointerleave", function () { if (island) island.style.stroke = ""; });
    });
    readout(fig, ["hover a game to see its nearest neighbours; click to pin"]);
  }

  /* ---------------------------------------------------------------- figure: vacant lots */
  function vacantLots(fig, data, svg) {
    var hl = $("[data-hl=lot]", svg);
    var lots = $$("[data-k]", svg);
    var pinned = false;
    function show(k) {
      if (!k) { hl.setAttribute("display", "none"); return; }
      var ij = k.split("-"), i = +ij[0], j = +ij[1], v = data.pairs[k];
      hl.setAttribute("display", "inline");
      hl.setAttribute("x", data.left + data.pos[j] - 2); hl.setAttribute("y", data.top + data.pos[i] - 2);
      var a = data.m[i], b = data.m[j];
      var status = v[3] ? "vacant, white-space rank " + v[4] : v[5] ? "in design tension" : v[2] >= 2 ? "built well above chance" : v[2] >= 1 ? "built about as often as chance" : "built less than chance";
      readout(fig, [link("mechanic", a[0], a[1]), link("mechanic", b[0], b[1]), "together in " + v[0] + " of " + data.N + " games", v[1] + " expected", "lift " + v[2], bold(status)]);
    }
    svg.addEventListener("pointermove", function (e) {
      if (pinned) return;
      var t = e.target.closest ? e.target.closest("[data-k]") : null;
      show(t ? t.getAttribute("data-k") : null);
    });
    svg.addEventListener("click", function (e) { var t = e.target.closest("[data-k]"); pinned = !!t && !pinned; show(t ? t.getAttribute("data-k") : null); });
    $$("[data-controls=vacant-lots] .segmented", fig).forEach(function (g) {
      g.addEventListener("click", function (e) {
        var b = e.target.closest("button"); if (!b) return;
        var only = b.getAttribute("data-value") === "vacant";
        pressed(g, b.getAttribute("data-value"));
        lots.forEach(function (r) { var v = data.pairs[r.getAttribute("data-k")]; r.style.opacity = only && !v[3] ? "0.12" : ""; });
      });
    });
    readout(fig, ["hover a lot to read the pair; click to pin"]);
  }

  /* ---------------------------------------------------------------- figure: technique flows */
  function flows(fig, data, svg) {
    var ribbons = $$("path[data-t]", svg);
    var mode = "edges";
    ribbons.forEach(function (r) { r.setAttribute("data-d1", r.getAttribute("d")); r.setAttribute("data-fo", r.getAttribute("fill-opacity")); });
    $$("[data-node]", svg).forEach(function (n) {
      if (n.hasAttribute("y")) n.setAttribute("data-y1", n.getAttribute("y"));
      if (n.hasAttribute("height")) n.setAttribute("data-h1", n.getAttribute("height"));
    });
    function match(r, key) {
      if (!key) return true;
      var kv = key.split(":"), k = kv[0], v = kv.slice(1).join(":");
      return r.getAttribute("data-" + k) === v;
    }
    function highlight(key, single) {
      ribbons.forEach(function (r) {
        var on = single ? r === single : match(r, key);
        r.setAttribute("fill-opacity", key || single ? (on ? "0.85" : "0.04") : r.getAttribute("data-fo"));
      });
    }
    function nodeReadout(key) {
      var kv = key.split(":"), k = kv[0], v = kv.slice(1).join(":"), info = data[k][v];
      var i = mode === "edges" ? 0 : 1;
      if (k === "t") readout(fig, [link("technique", v, info[0]), info[1].toLowerCase(), mode === "edges" ? info[2] + " affects edges" : "exposure " + info[3]]);
      else readout(fig, [bold(info[0].toLowerCase()), mode === "edges" ? info[1] + " affects edges" : "exposure " + info[2]]);
    }
    svg.addEventListener("pointerover", function (e) {
      var n = e.target.closest ? e.target.closest("[data-node]") : null;
      if (n) { highlight(n.getAttribute("data-node")); nodeReadout(n.getAttribute("data-node")); return; }
      var r = e.target.closest ? e.target.closest("path[data-t]") : null;
      if (r) {
        highlight(null, r);
        var t = r.getAttribute("data-t"), ef = r.getAttribute("data-e"), f = r.getAttribute("data-f");
        readout(fig, [link("technique", t, data.t[t][0]), data.e[ef][0].toLowerCase(), data.f[f][0].toLowerCase(),
          mode === "edges" ? r.getAttribute("data-v") + " edges" : "exposure " + r.getAttribute("data-v2")]);
      }
    });
    svg.addEventListener("pointerleave", function () { highlight(null); readout(fig, ["hover a technique, an effect, or a family"]); });
    $$("[data-controls=technique-flows] .segmented", fig).forEach(function (g) {
      g.addEventListener("click", function (e) {
        var b = e.target.closest("button"); if (!b) return;
        mode = b.getAttribute("data-value");
        pressed(g, mode);
        var two = mode === "exposure";
        ribbons.forEach(function (r) { r.setAttribute("d", r.getAttribute(two ? "data-d2" : "data-d1")); });
        $$("[data-node]", svg).forEach(function (n) {
          if (n.hasAttribute("data-y2")) n.setAttribute("y", n.getAttribute(two ? "data-y2" : "data-y1"));
          if (n.hasAttribute("data-h2")) n.setAttribute("height", n.getAttribute(two ? "data-h2" : "data-h1"));
          if (n.hasAttribute("data-v")) { var ts = n.querySelector("tspan"); if (ts) ts.textContent = n.getAttribute(two ? "data-v2" : "data-v"); }
        });
      });
    });
    readout(fig, ["hover a technique, an effect, or a family"]);
  }

  var FIGS = { "matrix": matrix, "strata": strata, "design-map": designMap, "vacant-lots": vacantLots, "technique-flows": flows };

  function figures() {
    $$("figure[data-viz]").forEach(function (fig) {
      var name = fig.getAttribute("data-viz");
      var script = document.getElementById("viz-data-" + name);
      var svg = $("svg", fig);
      if (!script || !svg || !FIGS[name]) return;
      var data;
      try { data = JSON.parse(script.textContent); } catch (err) { return; }
      $$("[data-viz-controls], [data-readout]", fig).forEach(function (n) { n.hidden = false; });
      try { FIGS[name](fig, data, svg); } catch (err) { if (window.console) console.error("simgrammar figure " + name, err); }
    });
  }

  function init() { toc(); tables(); figures(); }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init); else init();
})();
