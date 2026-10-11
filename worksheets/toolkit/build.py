"""
Build the InquiryMind science worksheet packs (one folder of topics per grade: topics/grade4/, topics/grade5/).

Usage (from the repository root):
  python3 worksheets/toolkit/build.py                  # every grade: HTML + PDF, hub pages, zips, InquiryMind copy
  python3 worksheets/toolkit/build.py --grade 4        # one grade only
  python3 worksheets/toolkit/build.py --grade 4 A1 C2  # only these packs of that grade (hub page still lists all)
  python3 worksheets/toolkit/build.py --no-pdf         # HTML only (fast preview)

Needs Python 3, Node.js and (once) `npm install --prefix worksheets/toolkit`.
Chromium: set CHROME_PATH, or run `npx playwright install chromium` once.
Output: worksheets/grade-<N>-science/ and worksheets/index.html (copied to offline-simulations/inquirymind-site/worksheets/)
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
import art  # noqa: E402
import ws  # noqa: E402
from icons import icon  # noqa: E402

OPENMOJI_CREDIT = ' · Pictures from OpenMoji (openmoji.org), CC BY-SA 4.0'
TAGLINE = 'Learn · Play · Wonder'
MISSION = ('Free resources for everyone, bringing quality and equity to education '
           'and helping teachers build concepts and make learning visible')

REPO = os.path.dirname(os.path.dirname(TOOLKIT))
WS = os.path.join(REPO, 'worksheets')
IM_WS = os.path.join(REPO, 'offline-simulations', 'inquirymind-site', 'worksheets')
GRADES = {
    2: {'phase': 'IB PYP Phase 2', 'stage': 'Stages 2–3'},
    3: {'phase': 'IB PYP Phase 3', 'stage': 'Stages 3–4'},
    4: {'phase': 'IB PYP Phase 3', 'stage': 'Stage 4'},
    5: {'phase': 'IB PYP Phase 4', 'stage': 'Stage 5'},
}


def out_dir(grade):
    return os.path.join(WS, f'grade-{grade}-science')

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
            f'<div class="code">Grade {topic.grade}</div></div></div>'
            f'<div class="name-line"><span>Name:</span><span>Class:</span><span>Date:</span></div>{goal_box}')


def cover(topic, om=False):
    strand, sic = STRANDS[topic.strand]
    items = ''.join(f'<li>{icon(KINDS[s.kind][0])} <b>{KINDS[s.kind][1]}:</b> {ws.rich(s.title)} '
                    f'<span class="muted">{stars(s.level)}</span></li>' for s in topic.sheets)
    return (f'<section class="cover"><div class="brand"><img src="../assets/inquirymind-logo-bw.png" alt="InquiryMind">'
            f'<div class="fredoka" style="text-align:right">Grade {topic.grade} Science<br><span class="muted small">Study pack {topic.code}</span></div></div>'
            f'<div class="strand">{icon(sic)} {strand}</div><h1>{ws.rich(topic.title)}</h1>'
            f'<div class="subtitle">{ws.rich(topic.subtitle)}</div>'
            f'<div class="art">{topic.cover_art}</div>'
            f'<div class="contents"><h3 style="margin-top:2px">In this pack</h3><ul style="list-style:none;padding:0;margin:0">{items}</ul></div>'
            f'<div class="owner"><div>This pack belongs to:</div><div>Class:</div></div>'
            f'<div class="credit">© InquiryMind · {TAGLINE} · {MISSION} · Illustrations drawn for InquiryMind{OPENMOJI_CREDIT if om else ""} · Print in black and white on A4 · Challenge: ★ core ★★ deeper ★★★ stretch</div></section>')


def page_style(topic, key):
    label = f'InquiryMind · {TAGLINE} · Grade {topic.grade} Science · {topic.code} {topic.title}' + (' · Answer key' if key else '')
    return f'<style>@page {{ @bottom-left {{ content: "{label}"; }} }}</style>'


def document(topic, key):
    ws.Q.counter = 0
    body = ''
    sheets = [s for s in topic.sheets if not (key and s.kind == 'learn')]
    for i, s in enumerate(sheets):
        ws.Q.counter = 0
        extra = ''
        if i == len(sheets) - 1 and not key:
            extra = ws.SelfCheck(topic.selfcheck).html(False)
        body += f'<section class="sheet">{head(topic, s, key)}{ws.render(s.blocks, key)}{extra}</section>'
    if not key:
        body = cover(topic, art.OM_MARK in body or art.OM_MARK in topic.cover_art) + body
    title = f'{topic.code} {topic.title}' + (' – Answer key' if key else ' – Study pack')
    return (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">'
            f'<title>{ws.esc(title)} | InquiryMind Grade {topic.grade} Science</title>'
            f'<link rel="stylesheet" href="../assets/styles.css">{page_style(topic, key)}</head>'
            f'<body class="{"answer-key" if key else "learner"} g{topic.grade}"><div class="doc">{body}</div></body></html>')


def load_topics(grade):
    topics = []
    for f in sorted(glob.glob(os.path.join(TOOLKIT, 'topics', f'grade{grade}', '*.py'))):
        if os.path.basename(f).startswith('_'):
            continue
        spec = importlib.util.spec_from_file_location(f'g{grade}_' + os.path.basename(f)[:-3], f)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        mod.TOPIC.grade = grade
        topics.append(mod.TOPIC)
    order = {'skills': 0, 'living': 1, 'earth': 2, 'physical': 3}
    return sorted(topics, key=lambda t: (order[t.strand], t.code[0], int(t.code[1:])))


def copy_assets(out):
    a = os.path.join(out, 'assets')
    os.makedirs(os.path.join(a, 'fonts'), exist_ok=True)
    shutil.copy(os.path.join(TOOLKIT, 'styles.css'), a)
    for f in glob.glob(os.path.join(TOOLKIT, 'assets', '*')):
        if os.path.isfile(f):
            shutil.copy(f, a)
    for f in glob.glob(os.path.join(TOOLKIT, 'assets', 'fonts', '*')):
        shutil.copy(f, os.path.join(a, 'fonts'))


def render_pdfs(jobs):
    listing = os.path.join(WS, '.pdf-jobs.json')
    json.dump(jobs, open(listing, 'w'))
    try:
        subprocess.run(['node', os.path.join(TOOLKIT, 'render_pdf.js'), listing], check=True)
    finally:
        os.remove(listing)


def main(argv):
    grades = sorted(GRADES)
    if '--grade' in argv:
        grades = [int(argv[argv.index('--grade') + 1])]
        argv = argv[:argv.index('--grade')] + argv[argv.index('--grade') + 2:]
    only = [a.upper() for a in argv if not a.startswith('--')]
    make_pdf = '--no-pdf' not in argv
    import hub
    for grade in grades:
        out = out_dir(grade)
        topics = load_topics(grade)
        os.makedirs(os.path.join(out, 'print'), exist_ok=True)
        os.makedirs(os.path.join(out, 'pdf'), exist_ok=True)
        copy_assets(out)
        jobs = []
        for t in topics:
            if only and t.code not in only:
                continue
            for key in (False, True):
                name = t.slug + ('-answer-key' if key else '-study-pack')
                html_path = os.path.join(out, 'print', name + '.html')
                with open(html_path, 'w', encoding='utf-8') as f:
                    f.write(document(t, key))
                jobs.append({'html': html_path, 'pdf': os.path.join(out, 'pdf', name + '.pdf')})
            print('built', f'G{grade}', t.code, t.title)
        if make_pdf and jobs:
            render_pdfs(jobs)
        if make_pdf and not only:
            make_zips(topics, out, grade)
        hub.write(topics, out, STRANDS, KINDS, grade)
    hub.write_landing(WS, {g: load_topics(g) for g in sorted(GRADES)})
    if os.path.isdir(os.path.dirname(IM_WS)):
        for grade in grades:
            shutil.rmtree(os.path.join(IM_WS, f'grade-{grade}-science'), ignore_errors=True)
            shutil.copytree(out_dir(grade), os.path.join(IM_WS, f'grade-{grade}-science'))
        shutil.copy(os.path.join(WS, 'index.html'), os.path.join(IM_WS, 'index.html'))
        print('copied to', os.path.relpath(IM_WS, REPO))


def make_zips(topics, out, grade):
    d = os.path.join(out, 'downloads')
    os.makedirs(d, exist_ok=True)
    for kind, suffix in (('study-packs', '-study-pack.pdf'), ('answer-keys', '-answer-key.pdf')):
        zpath = os.path.join(d, f'grade-{grade}-science-all-{kind}.zip')
        with zipfile.ZipFile(zpath, 'w', zipfile.ZIP_DEFLATED) as z:
            for t in topics:
                p = os.path.join(out, 'pdf', t.slug + suffix)
                if os.path.exists(p):
                    z.write(p, f'grade-{grade}-science-{kind}/{t.slug}{suffix}')
        print('zip', os.path.relpath(zpath, REPO), round(os.path.getsize(zpath) / 1e6, 1), 'MB')


if __name__ == '__main__':
    main(sys.argv[1:])
