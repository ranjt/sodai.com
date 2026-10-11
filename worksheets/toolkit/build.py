"""
Build the Grade 5 Science worksheet packs.

Usage (from the repository root):
  python3 worksheets/toolkit/build.py            # HTML + PDF for every topic, hub page, zips, InquiryMind copy
  python3 worksheets/toolkit/build.py A6 C1      # only these topics (hub page still lists all)
  python3 worksheets/toolkit/build.py --no-pdf   # HTML only (fast preview)

Needs Python 3, Node.js and (once) `npm install --prefix worksheets/toolkit`.
Chromium: set CHROME_PATH, or run `npx playwright install chromium` once.
Output: worksheets/grade-5-science/  (copied to offline-simulations/inquirymind-site/worksheets/grade-5-science/)
"""
import glob
import importlib.util
import json
import os
import shutil
import subprocess
import sys
import zipfile

TOOLKIT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, TOOLKIT)
import ws  # noqa: E402
from icons import icon  # noqa: E402

REPO = os.path.dirname(os.path.dirname(TOOLKIT))
OUT = os.path.join(REPO, 'worksheets', 'grade-5-science')
IM_COPY = os.path.join(REPO, 'offline-simulations', 'inquirymind-site', 'worksheets', 'grade-5-science')

STRANDS = {
    'skills': ('Working scientifically', 'microscope'),
    'living': ('Living things', 'leaf'),
    'earth': ('Earth and space', 'planet'),
    'physical': ('Physical and chemical science', 'atom'),
}
KINDS = {
    'learn': ('book', 'Learn it'),
    'facts': ('list-check', 'Fact check'),
    'think': ('bulb', 'Think it through'),
    'investigate': ('flask', 'Investigate'),
    'case': ('world', 'Real-world case study'),
    'review': ('trophy', 'Review and challenge'),
}


class Sheet:
    def __init__(self, kind, title, blocks, level=1, goals=()):
        self.kind, self.title, self.blocks, self.level, self.goals = kind, title, blocks, level, goals


class Topic:
    def __init__(self, code, strand, title, subtitle, outcomes, sheets, selfcheck, cover_art='', cambridge=(),
                 slug=None, short=None):
        self.code, self.strand, self.title, self.subtitle = code, strand, title, subtitle
        self.short = short or title
        self.outcomes, self.sheets, self.selfcheck = outcomes, sheets, selfcheck
        self.cover_art, self.cambridge = cover_art, cambridge
        self.slug = slug or f'{code.lower()}-' + ''.join(c if c.isalnum() else '-' for c in title.lower()).strip('-')
        while '--' in self.slug:
            self.slug = self.slug.replace('--', '-')


def stars(level):
    return '★' * level + '☆' * (3 - level)


def head(topic, sheet, key):
    ic, kind = KINDS[sheet.kind]
    goals = ''.join(f'<li>{ws.rich(g)}</li>' for g in sheet.goals)
    goal_box = f'<div class="goal">{icon("target-arrow")}<div><b>Learning goals</b><ul>{goals}</ul></div></div>' if goals else ''
    return (f'<div class="key-banner">ANSWER KEY</div>'
            f'<div class="ws-head"><img class="logo" src="../assets/inquirymind-logo-bw.png" alt="InquiryMind">'
            f'<div class="title"><div class="kind">{kind} · {topic.code} · {ws.esc(topic.short)}</div><h1>{ws.rich(sheet.title)}</h1></div>'
            f'<div class="badge">{icon(ic)}<div class="stars" title="Challenge level">{stars(sheet.level)}</div>'
            f'<div class="code">Grade 5</div></div></div>'
            f'<div class="name-line"><span>Name:</span><span>Class:</span><span>Date:</span></div>{goal_box}')


def cover(topic):
    strand, sic = STRANDS[topic.strand]
    items = ''.join(f'<li>{icon(KINDS[s.kind][0])} <b>{KINDS[s.kind][1]}:</b> {ws.rich(s.title)} '
                    f'<span class="muted">{stars(s.level)}</span></li>' for s in topic.sheets)
    camb = (f'<p class="small muted">Also covers Cambridge Primary Science Stage 5: {ws.esc("; ".join(topic.cambridge))}.</p>'
            if topic.cambridge else '')
    return (f'<section class="cover"><div class="brand"><img src="../assets/inquirymind-logo-bw.png" alt="InquiryMind">'
            f'<div class="fredoka" style="text-align:right">Grade 5 Science<br><span class="muted small">Study pack {topic.code}</span></div></div>'
            f'<div class="strand">{icon(sic)} {strand}</div><h1>{ws.rich(topic.title)}</h1>'
            f'<div class="subtitle">{ws.rich(topic.subtitle)}</div>'
            f'<div class="art">{topic.cover_art}</div>'
            f'<div class="contents"><h3 style="margin-top:2px">In this pack</h3><ul style="list-style:none;padding:0;margin:0">{items}</ul></div>'
            f'{camb}'
            f'<div class="owner"><div>This pack belongs to:</div><div>Class:</div></div>'
            f'<div class="credit">© InquiryMind · Original learning material for Grade 5 (PHIS Science continuum, IB PYP Phase 4, and Cambridge Primary Science Stage 5) · Illustrations drawn for InquiryMind · Print in black and white on A4 · Challenge: ★ core ★★ deeper ★★★ stretch</div></section>')


def page_style(topic, key):
    label = f'InquiryMind · Grade 5 Science · {topic.code} {topic.title}' + (' · Answer key' if key else '')
    return f'<style>@page {{ @bottom-left {{ content: "{label}"; }} }}</style>'


def document(topic, key):
    ws.Q.counter = 0
    body = ''
    if not key:
        body += cover(topic)
    sheets = [s for s in topic.sheets if not (key and s.kind == 'learn')]
    for i, s in enumerate(sheets):
        ws.Q.counter = 0
        extra = ''
        if i == len(sheets) - 1 and not key:
            extra = ws.SelfCheck(topic.selfcheck).html(False)
        body += f'<section class="sheet">{head(topic, s, key)}{ws.render(s.blocks, key)}{extra}</section>'
    title = f'{topic.code} {topic.title}' + (' – Answer key' if key else ' – Study pack')
    return (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">'
            f'<title>{ws.esc(title)} | InquiryMind Grade 5 Science</title>'
            f'<link rel="stylesheet" href="../assets/styles.css">{page_style(topic, key)}</head>'
            f'<body class="{"answer-key" if key else "learner"}"><div class="doc">{body}</div></body></html>')


def load_topics():
    topics = []
    for f in sorted(glob.glob(os.path.join(TOOLKIT, 'topics', '*.py'))):
        if os.path.basename(f).startswith('_'):
            continue
        spec = importlib.util.spec_from_file_location(os.path.basename(f)[:-3], f)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        topics.append(mod.TOPIC)
    order = {'skills': 0, 'living': 1, 'earth': 2, 'physical': 3}
    return sorted(topics, key=lambda t: (order[t.strand], t.code))


def copy_assets():
    a = os.path.join(OUT, 'assets')
    os.makedirs(os.path.join(a, 'fonts'), exist_ok=True)
    shutil.copy(os.path.join(TOOLKIT, 'styles.css'), a)
    for f in glob.glob(os.path.join(TOOLKIT, 'assets', '*')):
        if os.path.isfile(f):
            shutil.copy(f, a)
    for f in glob.glob(os.path.join(TOOLKIT, 'assets', 'fonts', '*')):
        shutil.copy(f, os.path.join(a, 'fonts'))


def render_pdfs(jobs):
    listing = os.path.join(OUT, '.pdf-jobs.json')
    json.dump(jobs, open(listing, 'w'))
    try:
        subprocess.run(['node', os.path.join(TOOLKIT, 'render_pdf.js'), listing], check=True)
    finally:
        os.remove(listing)


def main(argv):
    only = [a.upper() for a in argv if not a.startswith('--')]
    make_pdf = '--no-pdf' not in argv
    topics = load_topics()
    os.makedirs(os.path.join(OUT, 'print'), exist_ok=True)
    os.makedirs(os.path.join(OUT, 'pdf'), exist_ok=True)
    copy_assets()
    jobs = []
    for t in topics:
        if only and t.code not in only:
            continue
        for key in (False, True):
            name = t.slug + ('-answer-key' if key else '-study-pack')
            html_path = os.path.join(OUT, 'print', name + '.html')
            with open(html_path, 'w', encoding='utf-8') as f:
                f.write(document(t, key))
            jobs.append({'html': html_path, 'pdf': os.path.join(OUT, 'pdf', name + '.pdf')})
        print('built', t.code, t.title)
    if make_pdf and jobs:
        render_pdfs(jobs)
    if make_pdf and not only:
        make_zips(topics)
    import hub
    hub.write(topics, OUT, STRANDS, KINDS)
    if os.path.isdir(os.path.dirname(os.path.dirname(IM_COPY))):
        shutil.rmtree(IM_COPY, ignore_errors=True)
        shutil.copytree(OUT, IM_COPY)
        print('copied to', os.path.relpath(IM_COPY, REPO))


def make_zips(topics):
    d = os.path.join(OUT, 'downloads')
    os.makedirs(d, exist_ok=True)
    for kind, suffix in (('study-packs', '-study-pack.pdf'), ('answer-keys', '-answer-key.pdf')):
        zpath = os.path.join(d, f'grade-5-science-all-{kind}.zip')
        with zipfile.ZipFile(zpath, 'w', zipfile.ZIP_DEFLATED) as z:
            for t in topics:
                p = os.path.join(OUT, 'pdf', t.slug + suffix)
                if os.path.exists(p):
                    z.write(p, f'grade-5-science-{kind}/{t.slug}{suffix}')
        print('zip', os.path.relpath(zpath, REPO), round(os.path.getsize(zpath) / 1e6, 1), 'MB')


if __name__ == '__main__':
    main(sys.argv[1:])
