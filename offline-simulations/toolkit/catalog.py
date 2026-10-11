"""
Single source of truth for the simulation catalogs, and generator for the four catalog pages.

Each simulation row is: (id, display name, group, lowest grade, highest grade, topics)
  - id = PhET repo name = file name in sims/ and thumbnails/
  - grades: 0 = Kindergarten; a highest grade above 6 marks a "Stretch" sim (leans toward Grades 6-8)

Usage (from the repository root):
  python3 offline-simulations/toolkit/catalog.py pages        # rewrite all 4 index.html files
  python3 offline-simulations/toolkit/catalog.py ids [math|science]   # print sim ids (default: all)
  python3 offline-simulations/toolkit/catalog.py table        # print a Markdown table of every sim
"""
import json
import os
import sys

TOOLKIT = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(TOOLKIT))

# Where each site's copy lives, relative to the repository root
SITE_ROOTS = {
    'amrarbazar': '.',                                  # published on amrarbazar.com by GitHub Pages
    'inquirymind': 'offline-simulations/inquirymind-site',  # copy these folders into the Firebase public/ dir
}

SITES = {
    'amrarbazar': {
        'name': 'Amrar Bazar',
        'brand_html': '<a class="brand" href="../">Amrar Bazar</a>',
        'back_html': '<a class="back" href="../">← Back to shop</a>',
        'theme': """
  --primary:#1a6b3a;
  --primary-soft:#e8f5ee;
  --accent:#f4752a;
  --accent-hover:#e0661f;
  --focus:#f8cf48;
  --hero:linear-gradient(135deg,#4d8447 0%,#6da34c 60%,#a9c873 100%);
  --bg:linear-gradient(180deg,#fffdf8 0%,#f8f4ea 100%);
  --topbar:rgba(255,253,248,.92);
  --ink:#19231c;
  --muted:#6b756f;
  --line:#e7dfd2;""",
    },
    'inquirymind': {
        'name': 'InquiryMind',
        'brand_html': '<a class="brand" href="/"><img src="inquirymind-logo.png" alt="InquiryMind" width="150" height="33"></a>',
        'back_html': '<a class="back" href="/">← InquiryMind home</a>',
        'theme': """
  --primary:#3d25c4;
  --primary-soft:#ece9fb;
  --accent:#ef7d4f;
  --accent-hover:#dd6a3c;
  --focus:#f6c752;
  --hero:linear-gradient(135deg,#3d25c4 0%,#5a3fd6 55%,#8a6ff0 100%);
  --bg:linear-gradient(180deg,#fbfaff 0%,#f1eefc 100%);
  --topbar:rgba(251,250,255,.92);
  --ink:#1d1840;
  --muted:#686385;
  --line:#e2def3;""",
    },
}

CATALOGS = {
    'math': {
        'folder': 'simulations',
        'title': 'Math Simulations K–6',
        'h1': 'Math Simulations for K–6',
        'bn': 'কিন্ডারগার্টেন থেকে ষষ্ঠ শ্রেণির গণিত সিমুলেশন',
        'intro': 'Free, interactive math activities for young learners: counting, place value, multiplication, '
                 'fractions, decimals, ratios and more. Every simulation works in the browser and can be downloaded '
                 'to use offline.',
        'description': 'Free interactive math simulations for Kindergarten to Grade 6, adapted from PhET Interactive '
                       'Simulations (University of Colorado Boulder). Works offline.',
        'search': 'Search: fractions, area, mean…',
        'groups': [
            ('k2', 'Kindergarten – Grade 2', 'Counting and early number sense'),
            ('g35', 'Grades 3 – 5', 'Operations, area and fractions'),
            ('g56', 'Grades 5 – 6', 'Decimals, ratios, integers and early statistics'),
        ],
        'sims': [
            ('number-play', 'Number Play', 'k2', 0, 2, 'Counting 1–20, ten frames, recognizing small amounts at a glance'),
            ('make-a-ten', 'Make a Ten', 'k2', 0, 2, 'Place value, adding by making tens'),
            ('number-compare', 'Number Compare', 'k2', 0, 2, 'Comparing numbers, greater than and less than'),
            ('number-pairs', 'Number Pairs', 'k2', 0, 2, 'Splitting numbers into parts, addition facts'),
            ('arithmetic', 'Arithmetic', 'g35', 3, 5, 'Multiplication, division and factoring practice'),
            ('area-builder', 'Area Builder', 'g35', 3, 5, 'Area and perimeter with unit squares'),
            ('area-model-introduction', 'Area Model Introduction', 'g35', 3, 4, 'Area as multiplication'),
            ('area-model-multiplication', 'Area Model Multiplication', 'g35', 4, 5, 'Multi-digit multiplication, partial products'),
            ('fractions-intro', 'Fractions: Intro', 'g35', 3, 5, 'What a fraction is, different ways to show one'),
            ('fractions-equality', 'Fractions: Equality', 'g35', 3, 5, 'Equivalent fractions'),
            ('fractions-mixed-numbers', 'Fractions: Mixed Numbers', 'g35', 4, 5, 'Improper fractions and mixed numbers'),
            ('fraction-comparison', 'Fraction Comparison', 'g35', 3, 4, 'Comparing fractions'),
            ('build-a-fraction', 'Build a Fraction', 'g35', 3, 5, 'Building fractions with shapes and numbers'),
            ('fraction-matcher', 'Fraction Matcher', 'g35', 3, 5, 'Matching equal fractions (game)'),
            ('estimation', 'Estimation', 'g35', 3, 5, 'Estimating length, area and volume'),
            ('function-builder-basics', 'Function Builder: Basics', 'g35', 3, 5, 'Input and output patterns, early algebra'),
            ('area-model-decimals', 'Area Model Decimals', 'g56', 5, 6, 'Multiplying decimals'),
            ('mean-share-and-balance', 'Mean: Share and Balance', 'g56', 5, 6, 'Introduction to the mean (average)'),
            ('equality-explorer-basics', 'Equality Explorer: Basics', 'g56', 5, 6, 'Balance-scale equations, finding unknowns'),
            ('ratio-and-proportion', 'Ratio and Proportion', 'g56', 5, 6, 'Ratios'),
            ('unit-rates', 'Unit Rates', 'g56', 6, 6, 'Unit price and rates'),
            ('proportion-playground', 'Proportion Playground', 'g56', 6, 6, 'Proportional reasoning'),
            ('number-line-integers', 'Number Line: Integers', 'g56', 6, 6, 'Negative numbers, absolute value'),
            ('number-line-operations', 'Number Line: Operations', 'g56', 6, 6, 'Adding and subtracting on a number line'),
            ('number-line-distance', 'Number Line: Distance', 'g56', 6, 6, 'Distance between points'),
            ('quadrilateral', 'Quadrilateral', 'g56', 5, 6, 'Properties of four-sided shapes'),
            ('expression-exchange', 'Expression Exchange', 'g56', 6, 6, 'Combining like terms'),
            ('center-and-variability', 'Center and Variability', 'g56', 6, 6, 'Median, mean and spread'),
        ],
    },
    'science': {
        'folder': 'science-simulations',
        'title': 'Science Simulations K–6',
        'h1': 'Science Simulations for K–6',
        'bn': 'কিন্ডারগার্টেন থেকে ষষ্ঠ শ্রেণির বিজ্ঞান সিমুলেশন',
        'intro': 'Free, interactive science activities: forces, energy, electricity, magnets, light, sound, matter, '
                 'living things and space. Every simulation works in the browser and can be downloaded to use offline. '
                 'Simulations marked “stretch” lean toward Grades 6–8.',
        'description': 'Free interactive science simulations (physics, chemistry, biology, earth and space) for '
                       'Kindergarten to Grade 6, adapted from PhET Interactive Simulations (University of Colorado '
                       'Boulder). Works offline.',
        'search': 'Search: magnets, circuits, energy…',
        'groups': [
            ('physics', 'Physics', 'Forces, energy, electricity, magnets, light and sound'),
            ('chemistry', 'Chemistry', 'Matter and how it changes'),
            ('biology', 'Biology', 'Living things and the human body'),
            ('earth', 'Earth and Space', 'Gravity, orbits and climate'),
        ],
        'sims': [
            ('forces-and-motion-basics', 'Forces and Motion: Basics', 'physics', 0, 5, 'Pushes and pulls, friction, speed'),
            ('balancing-act', 'Balancing Act', 'physics', 3, 6, 'Balance and levers'),
            ('friction', 'Friction', 'physics', 3, 6, 'How rubbing surfaces make heat'),
            ('balloons-and-static-electricity', 'Balloons and Static Electricity', 'physics', 3, 6, 'Static charge, attraction and repulsion'),
            ('john-travoltage', 'John Travoltage', 'physics', 3, 6, 'Static shocks'),
            ('magnet-and-compass', 'Magnet and Compass', 'physics', 3, 6, 'Magnetic fields and compasses'),
            ('magnets-and-electromagnets', 'Magnets and Electromagnets', 'physics', 3, 6, 'Bar magnets and electromagnets'),
            ('circuit-construction-kit-dc', 'Circuit Construction Kit: DC', 'physics', 4, 6, 'Simple circuits, conductors and insulators'),
            ('energy-forms-and-changes', 'Energy Forms and Changes', 'physics', 4, 6, 'Energy transfer and heat'),
            ('energy-skate-park-basics', 'Energy Skate Park: Basics', 'physics', 4, 6, 'Motion and stored energy'),
            ('waves-intro', 'Waves Intro', 'physics', 4, 6, 'Water, sound and light waves'),
            ('sound-waves', 'Sound Waves', 'physics', 4, 6, 'Vibration, pitch and loudness'),
            ('color-vision', 'Color Vision', 'physics', 4, 6, 'Light and colour'),
            ('buoyancy-basics', 'Buoyancy: Basics', 'physics', 5, 6, 'Floating and sinking'),
            ('gravity-force-lab-basics', 'Gravity Force Lab: Basics', 'physics', 5, 6, 'Gravity between objects'),
            ('geometric-optics-basics', 'Geometric Optics: Basics', 'physics', 6, 8, 'Lenses and mirrors'),
            ('masses-and-springs-basics', 'Masses and Springs: Basics', 'physics', 6, 8, 'Springs and stretching'),
            ('density', 'Density', 'physics', 6, 8, 'Mass, volume and density'),
            ('under-pressure', 'Under Pressure', 'physics', 6, 8, 'Water and air pressure'),
            ('states-of-matter-basics', 'States of Matter: Basics', 'chemistry', 5, 6, 'Solids, liquids and gases'),
            ('reactants-products-and-leftovers', 'Reactants, Products and Leftovers', 'chemistry', 5, 6, 'Matter is conserved (sandwich “recipes”)'),
            ('ph-scale-basics', 'pH Scale: Basics', 'chemistry', 6, 8, 'Acids and bases in everyday liquids'),
            ('gases-intro', 'Gases Intro', 'chemistry', 6, 8, 'Gas pressure and temperature'),
            ('natural-selection', 'Natural Selection', 'biology', 3, 6, 'Traits, adaptation and survival'),
            ('eating-exercise-and-energy', 'Eating, Exercise, and Energy', 'biology', 5, 6, 'Food energy and a healthy body'),
            ('gravity-and-orbits', 'Gravity and Orbits', 'earth', 5, 6, 'Sun, Earth and Moon orbits'),
            ('my-solar-system', 'My Solar System', 'earth', 6, 8, 'Planet orbits'),
            ('greenhouse-effect', 'Greenhouse Effect', 'earth', 6, 8, 'Climate, sunlight and heat'),
        ],
    },
}

TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<title>{title} | {site_name}</title>
<meta name="description" content="{description}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Hind+Siliguri:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
:root{{{theme}
  --surface:#fff;
  --shadow:0 18px 42px rgba(13,19,31,.10);
  --shadow-soft:0 8px 20px rgba(13,19,31,.08);
  --max:1240px;
}}
*{{box-sizing:border-box;margin:0;padding:0}}
html{{scroll-behavior:smooth;-webkit-text-size-adjust:100%}}
body{{
  font-family:'DM Sans',system-ui,-apple-system,'Segoe UI',Roboto,sans-serif;
  color:var(--ink);
  background:var(--bg);
  min-height:100vh;
}}
a{{color:inherit;text-decoration:none}}
button,input{{font:inherit}}
.shell{{max-width:var(--max);margin:0 auto;padding:0 16px}}
.bn{{font-family:'Hind Siliguri','DM Sans',sans-serif}}

.topbar{{border-bottom:1px solid var(--line);background:var(--topbar);position:sticky;top:0;z-index:5;backdrop-filter:blur(8px)}}
.topbar .shell{{display:flex;align-items:center;justify-content:space-between;gap:12px;min-height:60px;flex-wrap:wrap;padding-top:6px;padding-bottom:6px}}
.brand{{font-weight:800;color:var(--primary);font-size:18px;display:flex;align-items:center}}
.brand img{{display:block;height:33px;width:auto}}
.tabs{{display:flex;gap:4px;padding:4px;border-radius:999px;background:var(--primary-soft)}}
.tabs a{{padding:7px 14px;border-radius:999px;font-size:14px;font-weight:700;color:var(--primary)}}
.tabs a[aria-current="page"]{{background:var(--primary);color:#fff}}
.back{{font-size:14px;font-weight:600;color:var(--muted)}}
.back:hover{{color:var(--primary)}}

.hero{{
  margin:24px auto 0;
  border-radius:28px;
  padding:40px 28px;
  color:#fff;
  background:var(--hero);
  box-shadow:var(--shadow);
}}
.hero h1{{font-size:clamp(28px,5vw,44px);line-height:1.1;font-weight:800}}
.hero .bn{{display:block;font-size:clamp(18px,3vw,24px);font-weight:600;margin-top:6px;opacity:.95}}
.hero p{{max-width:680px;margin-top:14px;font-size:16px;line-height:1.55;opacity:.95}}

.controls{{display:flex;flex-wrap:wrap;gap:10px;align-items:center;margin:24px 0 8px}}
.chips{{display:flex;flex-wrap:wrap;gap:6px}}
.chip{{
  padding:9px 14px;border-radius:999px;border:1px solid var(--line);background:var(--surface);
  font-size:14px;font-weight:700;color:var(--muted);cursor:pointer;
}}
.chip[aria-pressed="true"]{{background:var(--primary);border-color:var(--primary);color:#fff}}
.search{{
  flex:1 1 220px;min-width:0;padding:10px 14px;border-radius:999px;border:1px solid var(--line);
  background:var(--surface);font-size:15px;color:var(--ink);
}}
.search:focus,.chip:focus-visible,.btn:focus-visible,.tabs a:focus-visible{{outline:3px solid var(--focus);outline-offset:2px}}

.group{{margin-top:28px}}
.group-head{{display:flex;align-items:baseline;gap:10px;flex-wrap:wrap;margin-bottom:14px}}
.group-head h2{{font-size:22px;font-weight:800}}
.group-head span{{color:var(--muted);font-size:15px}}

.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:16px}}
.card{{
  background:var(--surface);border:1px solid var(--line);border-radius:20px;overflow:hidden;
  box-shadow:var(--shadow-soft);display:flex;flex-direction:column;
}}
.thumb{{display:block;aspect-ratio:600/394;background:#111;overflow:hidden}}
.thumb img{{width:100%;height:100%;object-fit:cover;display:block;transition:transform .2s}}
.card:hover .thumb img{{transform:scale(1.03)}}
.card-body{{padding:14px 16px 16px;display:flex;flex-direction:column;gap:8px;flex:1}}
.card h3{{font-size:17px;font-weight:800}}
.tags{{display:flex;gap:6px;flex-wrap:wrap}}
.grade,.stretch{{font-size:12px;font-weight:800;padding:3px 9px;border-radius:999px}}
.grade{{background:var(--primary-soft);color:var(--primary)}}
.stretch{{background:#fff3e0;color:#9a4b00}}
.topics{{font-size:14px;color:var(--muted);line-height:1.45;flex:1}}
.actions{{display:flex;gap:8px;margin-top:4px}}
.btn{{
  flex:1;text-align:center;padding:9px 10px;border-radius:12px;font-size:14px;font-weight:700;
  border:1px solid var(--line);
}}
.btn-primary{{background:var(--accent);border-color:var(--accent);color:#fff}}
.btn-primary:hover{{background:var(--accent-hover)}}
.btn:not(.btn-primary):hover{{border-color:var(--primary);color:var(--primary)}}
.empty{{display:none;margin-top:32px;color:var(--muted);text-align:center}}

.credit{{
  margin:40px 0 0;padding:22px;border-radius:20px;background:var(--surface);border:1px solid var(--line);
  font-size:14px;line-height:1.6;color:var(--muted);
}}
.credit h2{{font-size:17px;color:var(--ink);margin-bottom:8px}}
.credit a{{color:var(--primary);text-decoration:underline}}
.credit p+p{{margin-top:8px}}
footer{{padding:28px 0 40px;text-align:center;font-size:13px;color:var(--muted)}}

@media (max-width:560px){{
  .hero{{padding:28px 20px;border-radius:22px}}
  .grid{{grid-template-columns:1fr}}
  .back{{display:none}}
}}
</style>
</head>
<body>

<header class="topbar">
  <div class="shell">
    {brand_html}
    <nav class="tabs" aria-label="Simulation subjects">
      <a href="../simulations/"{math_current}>Math</a>
      <a href="../science-simulations/"{science_current}>Science</a>
    </nav>
    {back_html}
  </div>
</header>

<main class="shell">
  <section class="hero">
    <h1>{h1}</h1>
    <span class="bn">{bn}</span>
    <p>{intro}</p>
  </section>

  <div class="controls">
    <div class="chips" role="group" aria-label="Filter by grade">
      <button class="chip" data-grade="all" aria-pressed="true">All grades</button>
      <button class="chip" data-grade="k2" aria-pressed="false">K – 2</button>
      <button class="chip" data-grade="g35" aria-pressed="false">Grades 3 – 5</button>
      <button class="chip" data-grade="g6" aria-pressed="false">Grade 6</button>
    </div>
    <input class="search" type="search" placeholder="{search}" aria-label="Search simulations">
  </div>

  <div id="catalog"></div>
  <p class="empty" id="empty">No simulations match your search.</p>

  <section class="credit" id="credits">
    <h2>Credits</h2>
    <p>These simulations are by <strong>PhET Interactive Simulations, University of Colorado Boulder</strong> (<a href="https://phet.colorado.edu" target="_blank" rel="noopener">phet.colorado.edu</a>), licensed under <a href="https://creativecommons.org/licenses/by-nc/4.0/" target="_blank" rel="noopener">CC BY-NC 4.0</a> (non-commercial use only).</p>
    <p>They were built from PhET's open-source code (<a href="https://github.com/phetsims" target="_blank" rel="noopener">github.com/phetsims</a>) and branded for InquiryMind: each one shows the InquiryMind logo with an “adapted from PhET” credit. They are not official PhET releases, and PhET does not endorse this website. For the official versions, visit <a href="https://phet.colorado.edu" target="_blank" rel="noopener">phet.colorado.edu</a>.</p>
  </section>
</main>

<footer>{site_name} · Simulations adapted from PhET Interactive Simulations, University of Colorado Boulder · CC BY-NC 4.0</footer>

<script>
const GROUPS = {groups_json};

// [id, name, group, lowest grade (0 = K), highest grade, topics]; highest grade above 6 marks a "stretch" sim
const SIMS = {sims_json}.map(([id, name, group, min, max, topics]) => ({{ id, name, group, min, max, topics }}));

const GRADE_FILTERS = {{
  all: () => true,
  k2: s => s.min <= 2,
  g35: s => s.min <= 5 && s.max >= 3,
  g6: s => s.max >= 6
}};

const catalog = document.getElementById('catalog');
const empty = document.getElementById('empty');
const search = document.querySelector('.search');
const chips = document.querySelectorAll('.chip');
let activeGrade = 'all';

function gradeLabel(s) {{
  const lo = s.min === 0 ? 'K' : String(s.min);
  const hi = Math.min(s.max, 6);
  return 'Grade ' + (lo === String(hi) ? lo : lo + '–' + hi);
}}

function el(tag, attrs, children) {{
  const node = document.createElement(tag);
  Object.entries(attrs || {{}}).forEach(([k, v]) => {{
    if (k === 'text') node.textContent = v; else node.setAttribute(k, v);
  }});
  (children || []).forEach(c => node.appendChild(c));
  return node;
}}

function card(sim) {{
  const file = 'sims/' + sim.id + '.html';
  const img = el('img', {{ src: 'thumbnails/' + sim.id + '.png', alt: sim.name + ' screenshot', loading: 'lazy' }});
  const tags = [el('span', {{ class: 'grade', text: gradeLabel(sim) }})];
  if (sim.max > 6) tags.push(el('span', {{ class: 'stretch', text: 'Stretch' }}));
  return el('article', {{ class: 'card' }}, [
    el('a', {{ class: 'thumb', href: file, target: '_blank', rel: 'noopener', 'aria-label': 'Open ' + sim.name }}, [img]),
    el('div', {{ class: 'card-body' }}, [
      el('div', {{ class: 'tags' }}, tags),
      el('h3', {{ text: sim.name }}),
      el('p', {{ class: 'topics', text: sim.topics }}),
      el('div', {{ class: 'actions' }}, [
        el('a', {{ class: 'btn btn-primary', href: file, target: '_blank', rel: 'noopener', text: 'Open' }}),
        el('a', {{ class: 'btn', href: file, download: sim.id + '.html', text: 'Download' }})
      ])
    ])
  ]);
}}

function render() {{
  const q = search.value.trim().toLowerCase();
  const gradeOk = GRADE_FILTERS[activeGrade];
  catalog.textContent = '';
  let shown = 0;
  GROUPS.forEach(([groupId, title, sub]) => {{
    const sims = SIMS.filter(s => s.group === groupId && gradeOk(s) &&
      (!q || (s.name + ' ' + s.topics).toLowerCase().includes(q)));
    if (!sims.length) return;
    shown += sims.length;
    catalog.appendChild(el('section', {{ class: 'group' }}, [
      el('div', {{ class: 'group-head' }}, [el('h2', {{ text: title }}), el('span', {{ text: sub }})]),
      el('div', {{ class: 'grid' }}, sims.map(card))
    ]));
  }});
  empty.style.display = shown ? 'none' : 'block';
}}

chips.forEach(chip => chip.addEventListener('click', () => {{
  activeGrade = chip.dataset.grade;
  chips.forEach(c => c.setAttribute('aria-pressed', String(c === chip)));
  render();
}}));
search.addEventListener('input', render);
render();
</script>
</body>
</html>
"""


def sims_json(sims):
    rows = ',\n  '.join(json.dumps(list(s), ensure_ascii=False) for s in sims)
    return '[\n  ' + rows + '\n]'


def page(site_key, catalog_key):
    site, cat = SITES[site_key], CATALOGS[catalog_key]
    return TEMPLATE.format(
        title=cat['title'], site_name=site['name'], description=cat['description'], theme=site['theme'],
        brand_html=site['brand_html'], back_html=site['back_html'],
        math_current=' aria-current="page"' if catalog_key == 'math' else '',
        science_current=' aria-current="page"' if catalog_key == 'science' else '',
        h1=cat['h1'], bn=cat['bn'], intro=cat['intro'], search=cat['search'],
        groups_json=json.dumps(cat['groups'], ensure_ascii=False),
        sims_json=sims_json(cat['sims']),
    )


def all_ids(catalog_key=None):
    keys = [catalog_key] if catalog_key else list(CATALOGS)
    return [sim[0] for key in keys for sim in CATALOGS[key]['sims']]


def write_pages():
    for site_key, root in SITE_ROOTS.items():
        for catalog_key, cat in CATALOGS.items():
            folder = os.path.join(REPO, root, cat['folder'])
            os.makedirs(folder, exist_ok=True)
            path = os.path.join(folder, 'index.html')
            with open(path, 'w', encoding='utf-8') as f:
                f.write(page(site_key, catalog_key))
            print('wrote', os.path.relpath(path, REPO))


def markdown_table():
    rows = ['| Subject | Group | Simulation | File (`<folder>/sims/…`) | Grade | Topics |', '|---|---|---|---|---|---|']
    for catalog_key, cat in CATALOGS.items():
        groups = {g[0]: g[1] for g in cat['groups']}
        for sid, name, group, lo, hi, topics in cat['sims']:
            grade = ('K' if lo == 0 else str(lo)) + ('' if lo == min(hi, 6) else f'–{min(hi, 6)}')
            grade += ' (stretch)' if hi > 6 else ''
            rows.append(f"| {catalog_key.title()} | {groups[group]} | {name} | `{cat['folder']}/sims/{sid}.html` | {grade} | {topics} |")
    return '\n'.join(rows)


if __name__ == '__main__':
    command = sys.argv[1] if len(sys.argv) > 1 else 'pages'
    if command == 'pages':
        write_pages()
    elif command == 'ids':
        print(' '.join(all_ids(sys.argv[2] if len(sys.argv) > 2 else None)))
    elif command == 'table':
        print(markdown_table())
    else:
        sys.exit(__doc__)
