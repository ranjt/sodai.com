"""Download hub page (worksheets/grade-5-science/index.html): every study pack and answer key, grouped by strand,
with linked simulations, a syllabus coverage map and credits. Written by build.py on every run."""
import html
import os
import re

from icons import icon

# Simulations (from offline-simulations/toolkit/catalog.py) that go well with each pack: (folder, id, name)
SIMS = {
    'W1': [('simulations', 'mean-share-and-balance', 'Mean: Share and Balance')],
    'A4': [('science-simulations', 'eating-exercise-and-energy', 'Eating, Exercise, and Energy')],
    'A7': [('science-simulations', 'natural-selection', 'Natural Selection')],
    'B1': [('science-simulations', 'states-of-matter-basics', 'States of Matter: Basics')],
    'B4': [('science-simulations', 'gravity-and-orbits', 'Gravity and Orbits'), ('science-simulations', 'my-solar-system', 'My Solar System')],
    'B5': [('science-simulations', 'greenhouse-effect', 'Greenhouse Effect')],
    'C1': [('science-simulations', 'states-of-matter-basics', 'States of Matter: Basics')],
    'C3': [('science-simulations', 'reactants-products-and-leftovers', 'Reactants, Products and Leftovers')],
    'C4': [('science-simulations', 'energy-forms-and-changes', 'Energy Forms and Changes'), ('science-simulations', 'friction', 'Friction')],
    'C5': [('science-simulations', 'sound-waves', 'Sound Waves'), ('science-simulations', 'waves-intro', 'Waves Intro')],
    'C6': [('science-simulations', 'balancing-act', 'Balancing Act'), ('science-simulations', 'forces-and-motion-basics', 'Forces and Motion: Basics')],
    'C7': [('science-simulations', 'geometric-optics-basics', 'Geometric Optics: Basics'), ('science-simulations', 'color-vision', 'Color Vision')],
}

ABOUT = {
    'skills': 'How scientists work: questions, fair tests, measuring, graphs, conclusions and models. Used in every topic.',
    'living': 'The sustainability, complexity and interconnectedness of life: the human body, cells, health, plants and environments.',
    'earth': 'Our planet and its place in space: the water cycle, soil, the changing surface, seasons, resources and models.',
    'physical': 'Matter, materials and energy: changes of state, mixtures, atoms, energy, sound, machines and light.',
}

KIND_HELP = {
    'learn': 'an illustrated article with key words',
    'facts': 'recall and labelling',
    'think': 'explain and apply',
    'investigate': 'a real investigation with data',
    'case': 'a transdisciplinary Bangladesh case study',
    'review': 'word search, test questions and a stretch',
}

CSS = """
@font-face{font-family:'Andika';font-weight:400;src:url('assets/fonts/andika-latin-400-normal.woff2') format('woff2')}
@font-face{font-family:'Andika';font-weight:700;src:url('assets/fonts/andika-latin-700-normal.woff2') format('woff2')}
@font-face{font-family:'Fredoka';font-weight:500;src:url('assets/fonts/fredoka-latin-500-normal.woff2') format('woff2')}
@font-face{font-family:'Fredoka';font-weight:600;src:url('assets/fonts/fredoka-latin-600-normal.woff2') format('woff2')}
:root{
  --primary:#3d25c4;--primary-soft:#ece9fb;--accent:#ef7d4f;--accent-hover:#dd6a3c;--focus:#f6c752;
  --hero:linear-gradient(135deg,#3d25c4 0%,#5a3fd6 55%,#8a6ff0 100%);
  --bg:#f6f4fd;--surface:#fff;--ink:#1d1840;--muted:#625d80;--line:#e2def3;
  --shadow:0 18px 42px rgba(29,24,64,.10);--shadow-soft:0 8px 20px rgba(29,24,64,.07);--max:1200px;
}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth;-webkit-text-size-adjust:100%}
body{font-family:'Andika',system-ui,-apple-system,'Segoe UI',Roboto,sans-serif;color:var(--ink);background:var(--bg);line-height:1.5}
a{color:inherit;text-decoration:none}
button,input{font:inherit}
h1,h2,h3,.fredoka{font-family:'Fredoka','Andika',sans-serif;font-weight:600;line-height:1.15}
.ico{width:20px;height:20px;flex:none;stroke-width:1.8}
.shell{max-width:var(--max);margin:0 auto;padding:0 16px}
.topbar{background:rgba(255,255,255,.92);border-bottom:1px solid var(--line);position:sticky;top:0;z-index:5;backdrop-filter:blur(8px)}
.topbar .shell{display:flex;align-items:center;justify-content:space-between;gap:10px;min-height:60px;flex-wrap:wrap;padding-top:6px;padding-bottom:6px}
.brand img{display:block;height:33px;width:auto}
.tabs{display:flex;gap:4px;padding:4px;border-radius:999px;background:var(--primary-soft);flex-wrap:wrap}
.tabs a{padding:6px 13px;border-radius:999px;font-size:14px;font-weight:700;color:var(--primary)}
.tabs a[aria-current="page"]{background:var(--primary);color:#fff}
.hero{margin:22px auto 0;border-radius:28px;padding:38px 28px;color:#fff;background:var(--hero);box-shadow:var(--shadow)}
.hero .eyebrow{font-size:14px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;opacity:.9}
.hero h1{font-size:clamp(30px,5vw,46px);margin-top:6px}
.hero p{max-width:720px;margin-top:12px;font-size:17px;opacity:.96}
.stats{display:flex;flex-wrap:wrap;gap:8px;margin-top:18px}
.stats span{background:rgba(255,255,255,.16);border:1px solid rgba(255,255,255,.3);padding:5px 12px;border-radius:999px;font-size:14px;font-weight:700}
.hero-actions{display:flex;flex-wrap:wrap;gap:10px;margin-top:22px}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:7px;padding:10px 14px;border-radius:12px;font-size:15px;font-weight:700;border:1px solid var(--line);background:var(--surface);color:var(--ink)}
.btn:hover{border-color:var(--primary);color:var(--primary)}
.btn-primary{background:var(--accent);border-color:var(--accent);color:#fff}
.btn-primary:hover{background:var(--accent-hover);border-color:var(--accent-hover);color:#fff}
.btn-light{background:#fff;color:var(--primary);border-color:#fff}
.btn-ghost{background:transparent;color:#fff;border-color:rgba(255,255,255,.6)}
.btn-ghost:hover{color:#fff;border-color:#fff;background:rgba(255,255,255,.12)}
.btn small{font-weight:400;opacity:.8}
.btn:focus-visible,.chip:focus-visible,.search:focus,.tabs a:focus-visible{outline:3px solid var(--focus);outline-offset:2px}
.section{margin-top:34px}
.section>h2{font-size:26px;display:flex;align-items:center;gap:10px}
.section>p.lead{color:var(--muted);margin-top:6px;max-width:820px}
.howto{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px;margin-top:16px}
.tip{background:var(--surface);border:1px solid var(--line);border-radius:18px;padding:16px;box-shadow:var(--shadow-soft)}
.tip h3{font-size:18px;display:flex;align-items:center;gap:8px;color:var(--primary)}
.tip p{margin-top:6px;font-size:15px;color:var(--muted)}
.kinds{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:8px;margin-top:14px}
.kinds div{display:flex;gap:10px;align-items:center;background:var(--surface);border:1px solid var(--line);border-radius:14px;padding:10px 12px;font-size:15px}
.kinds .ico{color:var(--primary);width:24px;height:24px}
.kinds b{font-family:'Fredoka',sans-serif;font-weight:600}
.stars{color:var(--accent);letter-spacing:1px;white-space:nowrap}
.controls{display:flex;flex-wrap:wrap;gap:10px;align-items:center;margin:26px 0 4px}
.chips{display:flex;flex-wrap:wrap;gap:6px}
.chip{padding:8px 13px;border-radius:999px;border:1px solid var(--line);background:var(--surface);font-size:14px;font-weight:700;color:var(--muted);cursor:pointer}
.chip[aria-pressed="true"]{background:var(--primary);border-color:var(--primary);color:#fff}
.search{flex:1 1 220px;min-width:0;padding:10px 14px;border-radius:999px;border:1px solid var(--line);background:var(--surface);font-size:15px;color:var(--ink)}
.group{margin-top:26px}
.group-head{display:flex;align-items:center;gap:10px;flex-wrap:wrap}
.group-head h2{font-size:24px;display:flex;align-items:center;gap:8px}
.group-head h2 .ico{width:26px;height:26px;color:var(--primary)}
.group-head .count{color:var(--muted);font-size:15px}
.group>p{color:var(--muted);margin:4px 0 14px;font-size:15px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(270px,1fr));gap:16px}
.card{background:var(--surface);border:1px solid var(--line);border-radius:20px;overflow:hidden;box-shadow:var(--shadow-soft);display:flex;flex-direction:column}
.art{height:150px;padding:14px 18px;background:#fff;border-bottom:1px solid var(--line);display:flex;align-items:center;justify-content:center;position:relative}
.art svg{width:100% !important;height:100% !important}
.art .row{display:flex;gap:10px;width:100%;height:100%}
.art .row>div{flex:1;min-width:0;height:100%}
.code{position:absolute;top:10px;left:10px;background:var(--ink);color:#fff;font-family:'Fredoka',sans-serif;font-weight:600;font-size:14px;padding:2px 9px;border-radius:8px}
.card-body{padding:14px 16px 16px;display:flex;flex-direction:column;gap:8px;flex:1}
.card h3{font-size:19px}
.card .sub{font-size:14px;color:var(--muted);flex:1}
.meta{display:flex;flex-wrap:wrap;gap:6px}
.meta span{font-size:12.5px;font-weight:700;padding:3px 9px;border-radius:999px;background:var(--primary-soft);color:var(--primary)}
.meta span.camb{background:#fff3e0;color:#8a4500}
.sims{font-size:13.5px;color:var(--muted)}
.sims a{color:var(--primary);font-weight:700;text-decoration:underline;text-underline-offset:2px}
.actions{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-top:4px}
.actions .btn{font-size:14px;padding:9px 6px;white-space:nowrap}
.actions .btn .ico{width:18px;height:18px}
.actions .print{grid-column:1/-1;font-size:13.5px;padding:7px;color:var(--muted)}
.empty{display:none;margin-top:30px;color:var(--muted);text-align:center}
.map{margin-top:16px;display:grid;gap:12px}
details{background:var(--surface);border:1px solid var(--line);border-radius:16px;padding:0 16px}
summary{cursor:pointer;padding:13px 0;font-family:'Fredoka',sans-serif;font-weight:600;font-size:18px;display:flex;align-items:center;gap:8px;list-style:none}
summary::-webkit-details-marker{display:none}
summary::after{content:'+';margin-left:auto;font-size:22px;color:var(--primary)}
details[open] summary::after{content:'–'}
summary .ico{color:var(--primary)}
table{width:100%;border-collapse:collapse;margin:0 0 14px;font-size:14.5px}
th,td{text-align:left;vertical-align:top;padding:8px 10px;border-top:1px solid var(--line)}
th{font-family:'Fredoka',sans-serif;font-weight:600;background:var(--primary-soft);color:var(--primary)}
td:first-child{width:30%;font-weight:700}
td ul{padding-left:18px}
td li+li{margin-top:3px}
.tick{color:#1a7a43;font-weight:700}
.credit{margin-top:34px;padding:22px;border-radius:20px;background:var(--surface);border:1px solid var(--line);font-size:14.5px;color:var(--muted)}
.credit h2{font-size:20px;color:var(--ink);margin-bottom:8px}
.credit p+p{margin-top:8px}
.credit a{color:var(--primary);text-decoration:underline}
footer{padding:28px 0 40px;text-align:center;font-size:13px;color:var(--muted)}
@media (max-width:560px){.hero{padding:28px 20px;border-radius:22px}.grid{grid-template-columns:1fr}td:first-child{width:38%}th,td{padding:7px 6px}}
"""

SCRIPT = """
const chips = [...document.querySelectorAll('.chip')];
const search = document.querySelector('.search');
const cards = [...document.querySelectorAll('.card')];
const groups = [...document.querySelectorAll('.group')];
let strand = 'all';
function apply() {
  const q = search.value.trim().toLowerCase();
  let shown = 0;
  cards.forEach(c => {
    const ok = (strand === 'all' || c.dataset.strand === strand) && (!q || c.dataset.text.includes(q));
    c.hidden = !ok; if (ok) shown++;
  });
  groups.forEach(g => { g.hidden = !g.querySelector('.card:not([hidden])'); });
  document.getElementById('empty').style.display = shown ? 'none' : 'block';
}
chips.forEach(ch => ch.addEventListener('click', () => {
  strand = ch.dataset.strand;
  chips.forEach(x => x.setAttribute('aria-pressed', x === ch ? 'true' : 'false'));
  apply();
}));
search.addEventListener('input', apply);
"""


def esc(s):
    return html.escape(str(s), quote=True)


def plain(s):
    """Strip the **bold** / *italic* / ^sup^ / ~sub~ markers used in topic text."""
    return re.sub(r'[*^~]', '', s)


def pdf_pages(path):
    try:
        data = open(path, 'rb').read()
    except OSError:
        return 0
    return len(re.findall(rb'/Type\s*/Page[^s]', data))


def size_mb(path):
    return f'{os.path.getsize(path) / 1e6:.1f} MB' if os.path.exists(path) else ''


def card(t, out, kinds):
    sp = os.path.join(out, 'pdf', t.slug + '-study-pack.pdf')
    ak = os.path.join(out, 'pdf', t.slug + '-answer-key.pdf')
    n_sp, n_ak = pdf_pages(sp), pdf_pages(ak)
    meta = f'<span>{len(t.sheets)} worksheets</span>'
    if n_sp:
        meta += f'<span>{n_sp} pages</span>'
    if n_ak:
        meta += f'<span>key: {n_ak} pages</span>'
    if t.cambridge:
        meta += '<span class="camb">Cambridge Stage 5</span>'
    sims = ''
    if SIMS.get(t.code):
        links = ', '.join(f'<a href="../../{folder}/sims/{sid}.html" target="_blank" rel="noopener">{esc(name)}</a>'
                          for folder, sid, name in SIMS[t.code])
        sims = f'<div class="sims">Try the simulation: {links}</div>'
    text = ' '.join([t.code, t.title, t.subtitle, t.short] + [s.title for s in t.sheets]).lower()
    return (f'<article class="card" data-strand="{t.strand}" data-text="{esc(plain(text))}">'
            f'<div class="art" aria-hidden="true"><span class="code">{t.code}</span>{t.cover_art}</div>'
            f'<div class="card-body"><h3>{esc(plain(t.title))}</h3><p class="sub">{esc(plain(t.subtitle))}</p>'
            f'<div class="meta">{meta}</div>{sims}'
            f'<div class="actions">'
            f'<a class="btn btn-primary" href="pdf/{t.slug}-study-pack.pdf" download>{icon("file-type-pdf")} Study pack</a>'
            f'<a class="btn" href="pdf/{t.slug}-answer-key.pdf" download>{icon("key")} Answer key</a>'
            f'<a class="btn print" href="print/{t.slug}-study-pack.html" target="_blank" rel="noopener">{icon("printer")} Open print view in the browser</a>'
            f'</div></div></article>')


def coverage(topics, strands):
    out = ''
    for key, (name, ic) in strands.items():
        ts = [t for t in topics if t.strand == key]
        if not ts:
            continue
        n = sum(len(t.outcomes) for t in ts)
        rows = ''.join(
            f'<tr><td>{t.code} {esc(plain(t.title))}</td><td><ul>'
            + ''.join(f'<li><span class="tick" aria-label="covered">✓</span> {esc(o[0].upper() + o[1:])}</li>' for o in t.outcomes)
            + '</ul></td></tr>' for t in ts)
        out += (f'<details{" open" if key == "skills" else ""}><summary>{icon(ic)} {name} '
                f'<span class="muted" style="font-family:Andika,sans-serif;font-weight:400;font-size:15px;color:var(--muted)">'
                f'· {n} outcomes in {len(ts)} pack{"s" if len(ts) > 1 else ""}</span></summary>'
                f'<table><thead><tr><th>Pack</th><th>Grade 5 learning outcomes covered</th></tr></thead><tbody>{rows}</tbody></table></details>')
    units = {}
    for t in topics:
        for c in t.cambridge:
            m = re.match(r'Unit (\d+) ([^:(]+)(.*)', c)
            if m:
                units.setdefault((int(m.group(1)), m.group(2).strip()), []).append((t, m.group(3).strip(' :()')))
    if units:
        rows = ''.join(f'<tr><td>Unit {num}: {esc(name)}</td><td><ul>'
                       + ''.join(f'<li>{t.code} {esc(plain(t.title))}{f" ({esc(d)})" if d else ""}</li>' for t, d in items)
                       + '</ul></td></tr>' for (num, name), items in sorted(units.items()))
        out += (f'<details><summary>{icon("book")} Cambridge Primary Science Stage 5 '
                f'<span style="font-family:Andika,sans-serif;font-weight:400;font-size:15px;color:var(--muted)">· Learner\'s Book units</span></summary>'
                f'<table><thead><tr><th>Learner\'s Book unit</th><th>Packs that cover it</th></tr></thead><tbody>{rows}</tbody></table></details>')
    return out


def write(topics, out, strands, kinds):
    zsp = os.path.join(out, 'downloads', 'grade-5-science-all-study-packs.zip')
    zak = os.path.join(out, 'downloads', 'grade-5-science-all-answer-keys.zip')
    pages = sum(pdf_pages(os.path.join(out, 'pdf', t.slug + '-study-pack.pdf')) for t in topics)
    sheets = sum(len(t.sheets) for t in topics)
    outcomes = sum(len(t.outcomes) for t in topics)
    zips = ''
    if os.path.exists(zsp):
        zips += (f'<a class="btn btn-light" href="downloads/grade-5-science-all-study-packs.zip" download>{icon("file-zip")} '
                 f'All study packs <small>{size_mb(zsp)}</small></a>')
    if os.path.exists(zak):
        zips += (f'<a class="btn btn-ghost" href="downloads/grade-5-science-all-answer-keys.zip" download>{icon("key")} '
                 f'All answer keys <small>{size_mb(zak)}</small></a>')
    zips += f'<a class="btn btn-ghost" href="#syllabus">{icon("map")} Syllabus map</a>'

    kind_list = ''.join(f'<div>{icon(ic)}<span><b>{label}</b> · {KIND_HELP[k]}</span></div>' for k, (ic, label) in kinds.items())
    chips = '<button class="chip" data-strand="all" aria-pressed="true">All topics</button>' + ''.join(
        f'<button class="chip" data-strand="{k}" aria-pressed="false">{name}</button>'
        for k, (name, ic) in strands.items() if any(t.strand == k for t in topics))
    groups = ''
    for k, (name, ic) in strands.items():
        ts = [t for t in topics if t.strand == k]
        if ts:
            groups += (f'<section class="group" id="{k}"><div class="group-head"><h2>{icon(ic)} {name}</h2>'
                       f'<span class="count">{len(ts)} pack{"s" if len(ts) > 1 else ""}</span></div><p>{ABOUT[k]}</p>'
                       f'<div class="grid">{"".join(card(t, out, kinds) for t in ts)}</div></section>')

    page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Grade 5 Science Study Packs | InquiryMind</title>
<meta name="description" content="Free printable Grade 5 science worksheets and study packs with answer keys: illustrated articles, fact checks, investigations and Bangladesh case studies covering the whole Grade 5 syllabus.">
<link rel="icon" href="assets/inquirymind-logo.png">
<style>{CSS}</style>
</head>
<body>
<header class="topbar"><div class="shell">
  <a class="brand" href="./"><img src="assets/inquirymind-logo.png" alt="InquiryMind"></a>
  <nav class="tabs" aria-label="Learning resources">
    <a href="../../simulations/">Math sims</a><a href="../../science-simulations/">Science sims</a><a href="./" aria-current="page">Worksheets</a>
  </nav>
</div></header>
<main class="shell">
  <section class="hero">
    <div class="eyebrow">InquiryMind · Grade 5 Science</div>
    <h1>Study packs and worksheets</h1>
    <p>Print-ready, black-and-white study packs that cover the whole Grade 5 science syllabus. Each pack teaches the topic with an illustrated article, then builds from facts to thinking, a real investigation and a transdisciplinary case study set in Bangladesh. Every pack has its own answer key.</p>
    <div class="stats"><span>{len(topics)} study packs</span><span>{sheets} worksheets</span>{f"<span>{pages} printable pages</span>" if pages else ""}<span>{outcomes} learning outcomes</span><span>Answer keys included</span></div>
    <div class="hero-actions">{zips}</div>
  </section>

  <section class="section" id="how">
    <h2>{icon("info-circle")} How to use the packs</h2>
    <div class="howto">
      <div class="tip"><h3>{icon("printer")} Print</h3><p>A4, black and white, double-sided. Every worksheet starts on a new page, so you can print a single sheet or the whole pack.</p></div>
      <div class="tip"><h3>{icon("book")} Learn</h3><p>Start with the <b>Learn it</b> article and its key words. Learners can read it in class or at home before the activities.</p></div>
      <div class="tip"><h3>{icon("target-arrow")} Practise</h3><p>Stars show the challenge level: <span class="stars">★☆☆</span> core, <span class="stars">★★☆</span> deeper, <span class="stars">★★★</span> stretch. Marks are shown for each question.</p></div>
      <div class="tip"><h3>{icon("checklist")} Check</h3><p>Use the answer key to mark or for self-checking. The last page of each pack is a self-assessment: “Not yet, Nearly, Got it!”</p></div>
    </div>
    <div class="kinds">{kind_list}</div>
  </section>

  <div class="controls">
    <div class="chips" role="group" aria-label="Filter by strand">{chips}</div>
    <input class="search" type="search" placeholder="Search topics, e.g. plants, sound, soil" aria-label="Search the study packs">
  </div>
  {groups}
  <p class="empty" id="empty">No study packs match your search.</p>

  <section class="section" id="syllabus">
    <h2>{icon("map")} Syllabus coverage map</h2>
    <p class="lead">Every Grade 5 learning outcome in the school science continuum (IB PYP Phase 4, standardised against Cambridge Primary Science) and the pack that teaches it. Working scientifically skills are also practised in every pack's investigation.</p>
    <div class="map">{coverage(topics, strands)}</div>
  </section>

  <section class="credit" id="credits">
    <h2>Credits and licence</h2>
    <p>All worksheets, articles, questions, case studies and illustrations are original material written and drawn for InquiryMind. They are aligned to the school's Grade 5 science continuum and to the topics of Cambridge Primary Science Stage 5; they are not published or endorsed by Cambridge University Press or Cambridge International, and no text from their books is reproduced. Case-study facts are drawn from public sources named on each sheet; data marked “example” is illustrative.</p>
    <p>Fonts: Andika, Fredoka and Patrick Hand (SIL Open Font License 1.1, licence files in <code>assets/</code>). Icons: <a href="https://tabler.io/icons" target="_blank" rel="noopener">Tabler Icons</a> (MIT licence). Simulations linked from these packs are adapted from <a href="https://phet.colorado.edu" target="_blank" rel="noopener">PhET Interactive Simulations</a>, University of Colorado Boulder (CC BY-NC 4.0).</p>
  </section>
</main>
<footer>InquiryMind · Learn · Play · Wonder · Grade 5 Science study packs</footer>
<script>{SCRIPT}</script>
</body>
</html>
"""
    with open(os.path.join(out, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(page)
