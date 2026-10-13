# Publishing the worksheets on inquirymind.org

Everything in this folder is **finished and ready to upload**: the pages already have the InquiryMind design (logo,
purple colours, fonts, tabs) and every worksheet is already a print-ready PDF. To publish you only **copy the folders**.
Nothing needs to be recreated, so it costs no Claude tokens.

```
offline-simulations/inquirymind-site/
├── publish.sh                     one-command copy (and deploy) into your Firebase project
├── PUBLISH-WORKSHEETS.md          this guide
├── CLAUDE-INQUIRYMIND.md          short instructions to paste into your InquiryMind project as CLAUDE.md
├── simulations/                   28 math simulations       → inquirymind.org/simulations/
├── science-simulations/           28 science simulations    → inquirymind.org/science-simulations/
└── worksheets/                    → inquirymind.org/worksheets/
    ├── index.html                 grade chooser (KG to Grade 5) + thinking routines card
    ├── kg-science/                KG (KG 1 and KG 2): 12 packs
    ├── grade-1-science/ … grade-5-science/   Grades 1–5: 11, 12, 14, 20 and 24 packs
    │   each: index.html (download page), pdf/ (study packs + answer keys), print/, downloads/ (zips), assets/
    └── thinking-routines/         34 Visible Thinking Routine organisers + download page
└── question-bank/                 science practice questions KG–Grade 5 → inquirymind.org/question-bank/
    ├── README.md                  question format, practice-card mapping, marking rules
    ├── dist/                      manifest.json, all-questions.json, kg.json, grade-1.json … grade-5.json
    ├── images/                    diagrams and OpenMoji pictures used by the questions
    └── preview/                   demo page (play every question) + qb-player.js / qb-player.css
```

The question bank is data for your **Practice** section. Copying it publishes the files; to show the questions inside
Practice, give Claude the prompt in `INQUIRYMIND-INTEGRATION-PROMPT.md` (in the root of this repository).

## One-time setup on your Mac

1. Install Node.js from https://nodejs.org (LTS), then in Terminal:
   `npm install -g firebase-tools` and `firebase login`.
2. Have your InquiryMind Firebase project folder on the Mac (the folder that contains `firebase.json`).
3. Download this repository: https://github.com/ranjt/sodai.com → **Code → Download ZIP**, then unzip it
   (or `git clone https://github.com/ranjt/sodai.com.git`).

## Publish (every time there are new worksheets)

```bash
cd ~/Downloads/sodai.com-main/offline-simulations/inquirymind-site
bash publish.sh ~/path/to/your/inquirymind-project            # copy, then check locally
bash publish.sh ~/path/to/your/inquirymind-project --deploy   # copy and go live
```

- Only the worksheets: `bash publish.sh ~/path/to/project --only worksheets --deploy`
- The script only replaces the `simulations/`, `science-simulations/`, `worksheets/` and `question-bank/` folders inside your hosting
  folder. Your own pages (home page, about, contact…) are never touched.
- After new worksheets are made, download the repository again (or `git pull`) and run the same command.

## Link them from your InquiryMind pages

```html
<a href="/worksheets/">Science worksheets (KG–Grade 5)</a>
<a href="/worksheets/thinking-routines/">Thinking routines</a>
<a href="/simulations/">Math simulations</a>
<a href="/science-simulations/">Science simulations</a>
```

Link straight to one grade or one PDF:

```html
<a href="/worksheets/kg-science/">KG science packs</a>
<a href="/worksheets/grade-3-science/pdf/c2-sound-study-pack.pdf" download>Grade 3 Sound (PDF)</a>
<a href="/worksheets/thinking-routines/pdf/r01-see-think-wonder.pdf" download>See, Think, Wonder (PDF)</a>
```

Show a whole download page inside one of your own pages:

```html
<iframe src="/worksheets/grade-1-science/" style="width:100%;height:900px;border:0" title="Grade 1 science worksheets"></iframe>
```

The full list of every PDF and its path is in `worksheets/ALL-WORKSHEETS.md` in the repository.

## Notes

- The pages work offline too: open `worksheets/index.html` on any computer.
- All PDFs are A4, black and white, so they are cheap to print.
- Credits shown on the pages (Project Zero for the thinking routines, OpenMoji pictures, PhET simulations, fonts)
  must stay; they are part of the licences.
- Firebase free plan: about 360 MB of downloads per day. PDFs are small (0.1–0.4 MB each), but the zips are 2–7 MB.
  For heavy use, switch to the pay-as-you-go (Blaze) plan.
