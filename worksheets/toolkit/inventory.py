"""Write worksheets/ALL-WORKSHEETS.md: every study pack, answer key and thinking routine organiser, with links and page counts.
Runs at the end of build.py and routines.py; run it on its own with: python3 worksheets/toolkit/inventory.py"""
import os
import sys

TOOLKIT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, TOOLKIT)
from hub import gname, gslug, pdf_pages  # noqa: E402

WS = os.path.dirname(TOOLKIT)
STRAND = {'skills': 'Working scientifically', 'living': 'Living things', 'earth': 'Earth and space', 'physical': 'Physical and chemical science'}


def write():
    import build
    import routines
    grades = {g: build.load_topics(g) for g in sorted(build.GRADES)}
    n_packs = sum(len(ts) for ts in grades.values())
    out = [
        '# All InquiryMind worksheets',
        '',
        f'{n_packs} science study packs (each with an answer key) for KG to Grade 5, and {len(routines.ROUTINES)} Visible Thinking Routine',
        'organisers. This list is written automatically by `worksheets/toolkit/inventory.py` every time the worksheets are built.',
        '',
        '## Open them on a Mac',
        '',
        '1. Get the files: on https://github.com/ranjt/sodai.com click **Code → Download ZIP** and double-click the zip in',
        '   Downloads (or, in Terminal: `git clone https://github.com/ranjt/sodai.com.git`).',
        '2. In Finder open `sodai.com-main/worksheets/` (or `sodai.com/worksheets/` if you cloned).',
        '3. Double-click `index.html` to browse everything in Safari or Chrome, offline, exactly as on the website.',
        '   Or open a PDF straight from a `pdf/` folder below (Preview prints them on A4).',
        '',
        'The same files are copied for the InquiryMind website in `offline-simulations/inquirymind-site/worksheets/`',
        '(see `offline-simulations/inquirymind-site/PUBLISH-WORKSHEETS.md`).',
        '',
        '## Folder map',
        '',
        '```',
        'worksheets/',
        '├── index.html                       grade chooser (open in a browser)',
        '├── ALL-WORKSHEETS.md                this list',
    ]
    for g, ts in grades.items():
        out.append(f'├── {gslug(g)}-science/'.ljust(37) + f'{gname(g)}: {len(ts)} packs')
        out.append(f'│   ├── index.html                   download page')
        out.append(f'│   ├── pdf/                         {len(ts)} study packs + {len(ts)} answer keys')
        out.append(f'│   ├── print/                       the same packs as web pages')
        out.append(f'│   └── downloads/                   {gslug(g)}-science-all-study-packs.zip, …-all-answer-keys.zip')
    out += [
        f'├── thinking-routines/               {len(routines.ROUTINES)} thinking routine organisers (pdf/, previews/, downloads/)',
        '└── toolkit/                         source code (edit here, then rebuild)',
        '```',
        '',
    ]
    for g, ts in grades.items():
        folder = f'{gslug(g)}-science'
        out += [f'## {gname(g)} science ({len(ts)} packs)', '', '| Code | Pack | Strand | Study pack | Answer key | Pages |', '|---|---|---|---|---|---|']
        for t in ts:
            sp, ak = f'{folder}/pdf/{t.slug}-study-pack.pdf', f'{folder}/pdf/{t.slug}-answer-key.pdf'
            pages = f'{pdf_pages(os.path.join(WS, sp))} + {pdf_pages(os.path.join(WS, ak))}'
            out.append(f'| {t.code} | {t.title} | {STRAND[t.strand]} | [PDF]({sp}) | [PDF]({ak}) | {pages} |')
        out.append('')
    out += [f'## Visible Thinking Routines ({len(routines.ROUTINES)} organisers)', '', '| Code | Routine | Organiser |', '|---|---|---|']
    for r in routines.ROUTINES:
        out.append(f'| {r.code} | {r.title} | [PDF](thinking-routines/pdf/{r.slug}.pdf) |')
    out.append('')
    with open(os.path.join(WS, 'ALL-WORKSHEETS.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(out))
    print('wrote worksheets/ALL-WORKSHEETS.md')


if __name__ == '__main__':
    write()
