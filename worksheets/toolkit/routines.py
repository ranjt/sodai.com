"""
Build the InquiryMind thinking routine templates: one simple, printable A4 organiser per thinking routine,
for teachers to download and use with any picture, object, story or topic.

Usage (from the repository root):
  python3 worksheets/toolkit/routines.py           # every routine: HTML + PDF (+ copy to the InquiryMind site)
  python3 worksheets/toolkit/routines.py R01       # only these routines
  python3 worksheets/toolkit/routines.py --no-pdf  # HTML only (fast preview)
Output: worksheets/thinking-routines/ (pdf/, print/, assets/)

The routines themselves were developed by Project Zero (Harvard Graduate School of Education); every template is an
original InquiryMind design (layout, wording, icons) and gives Project Zero a small credit line.
"""
import os
import shutil
import sys

TOOLKIT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, TOOLKIT)
import ws  # noqa: E402
from build import WS, IM_WS, REPO, TAGLINE, MISSION, copy_assets, render_pdfs  # noqa: E402
from rt_icons import ICONS  # noqa: E402

OUT = os.path.join(WS, 'thinking-routines')


class Part:
    """One section of an organiser: an icon (rt_icons.ICONS key), a big word ("I see"), and a short prompt."""
    def __init__(self, icon, word, prompt):
        self.icon, self.word, self.prompt = icon, word, prompt


class Routine:
    def __init__(self, code, name, parts, layout='columns', focus='Our picture, object or topic:'):
        self.code, self.name, self.parts, self.layout, self.focus = code, name, parts, layout, focus
        self.slug = f'{code.lower()}-' + ''.join(c if c.isalnum() else '-' for c in name.lower()).strip('-')
        while '--' in self.slug:
            self.slug = self.slug.replace('--', '-')


ROUTINES = [
    Routine('R01', 'See, Think, Wonder', [
        Part('see', 'I see', 'What do I notice? Only what I can really see.'),
        Part('think', 'I think', 'What might be going on? What makes me say that?'),
        Part('wonder', 'I wonder', 'What questions do I have now?'),
    ]),
]


def columns(r):
    cols = ''.join(f'<div class="rt-col"><div class="rt-col-head"><span class="rt-num">{i}</span>{ICONS[p.icon]()}'
                   f'<div class="rt-word">{ws.esc(p.word)}</div><div class="rt-prompt">{ws.esc(p.prompt)}</div></div>'
                   f'<div class="rt-space"></div></div>' for i, p in enumerate(r.parts, 1))
    return f'<div class="rt-cols" style="--n:{len(r.parts)}">{cols}</div>'


def page(r):
    title = ' · '.join(r.name.split(', '))
    return (f'<section class="rt-page"><header class="rt-top"><img class="rt-logo" src="../assets/inquirymind-logo-bw.png" alt="InquiryMind">'
            f'<h1 class="rt-title">{ws.esc(title)}</h1><div class="rt-name"><span>Name</span><span>Date</span></div></header>'
            f'<div class="rt-focus">{ws.esc(r.focus)}<span></span></div>{columns(r)}'
            f'<footer class="rt-foot"><span><b>InquiryMind</b> · {TAGLINE} · {MISSION}.</span>'
            f'<span>Thinking routine: Project Zero, Harvard Graduate School of Education</span></footer></section>')


def document(r):
    return (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">'
            f'<title>{ws.esc(r.name)} | InquiryMind Thinking Routines</title><link rel="stylesheet" href="../assets/styles.css">'
            f'<style>@page {{ size: A4 landscape; margin: 9mm; @bottom-left {{ content: none; }} @bottom-right {{ content: none; }} }}</style>'
            f'</head><body class="routine"><div class="doc rt-doc">{page(r)}</div></body></html>')


def main(argv):
    only = [a.upper() for a in argv if not a.startswith('--')]
    for d in ('print', 'pdf'):
        os.makedirs(os.path.join(OUT, d), exist_ok=True)
    copy_assets(OUT)
    jobs = []
    for r in ROUTINES:
        if only and r.code not in only:
            continue
        p = os.path.join(OUT, 'print', r.slug + '.html')
        with open(p, 'w', encoding='utf-8') as f:
            f.write(document(r))
        jobs.append({'html': p, 'pdf': os.path.join(OUT, 'pdf', r.slug + '.pdf')})
        print('built', r.code, r.name)
    if '--no-pdf' not in argv and jobs:
        render_pdfs(jobs)
    if os.path.isdir(os.path.dirname(IM_WS)):
        shutil.rmtree(os.path.join(IM_WS, 'thinking-routines'), ignore_errors=True)
        shutil.copytree(OUT, os.path.join(IM_WS, 'thinking-routines'))
        print('copied to', os.path.relpath(os.path.join(IM_WS, 'thinking-routines'), REPO))


if __name__ == '__main__':
    main(sys.argv[1:])
