# Grade 5 Science study packs (InquiryMind)

22 print-ready, black-and-white study packs that cover the whole Grade 5 science syllabus (PHIS Science
continuum 2025, IB PYP Phase 4) and the topics of Cambridge Primary Science Stage 5. Each pack has its own
answer key. Everything is original InquiryMind material: articles, questions, case studies and line drawings.

- Live (after merging to `main`): **https://amrarbazar.com/worksheets/grade-5-science/**
- InquiryMind copy: `offline-simulations/inquirymind-site/worksheets/grade-5-science/`
  (copy the `worksheets` folder into the Firebase `public/` folder → `https://www.inquirymind.org/worksheets/grade-5-science/`)

## 1. What's where

```
worksheets/
├── README.md                    this guide
├── grade-5-science/             GENERATED: the website folder (do not edit by hand)
│   ├── index.html               download page: packs by strand, PDFs, answer keys, syllabus coverage map
│   ├── pdf/<slug>-study-pack.pdf    learner pack (cover, 6 worksheets, self-check)
│   ├── pdf/<slug>-answer-key.pdf    teacher answer key (same pages, answers filled in)
│   ├── print/<slug>-*.html      the same packs as web pages (open, then Ctrl+P)
│   ├── downloads/               all study packs (zip) and all answer keys (zip)
│   └── assets/                  logo, fonts (OFL), stylesheet
└── toolkit/                     SOURCE: edit here, then rebuild
    ├── build.py                 builds HTML + PDF + zips + download page + InquiryMind copy
    ├── topics/<code>_*.py       ONE FILE PER PACK: all text, questions and answers
    ├── ws.py                    worksheet building blocks (questions, tables, graphs, word search …)
    ├── art.py                   all illustrations, drawn as SVG line art
    ├── hub.py                   the download page (also: which simulations link to which pack)
    ├── styles.css               A4 print design
    ├── icons/                   Tabler icons used (MIT)
    └── assets/                  fonts, logo (colour and black-and-white)
```

## 2. The packs

Every pack has the same six worksheets, in the order a class would use them:

| Sheet | Stars | What learners do |
|---|---|---|
| **Learn it** | ★ | Read an illustrated article with key words, "Did you know?", "From the past" and Bangladesh boxes |
| **Fact check** | ★ | Label diagrams, fill gaps, sort, match, true/false |
| **Think it through** | ★★ | Explain and apply: "why…?", diagrams, predictions |
| **Investigate** | ★★ | A real investigation: variables, results table, graph to draw, pattern, conclusion |
| **Real-world case study** | ★★★ | A transdisciplinary Bangladesh case (science + health, maths, economics, ethics…) with data and viewpoints |
| **Review and challenge** | ★★★ | Word search, test-style questions, a design task and a stretch question |

The study pack ends with a self-check ("Not yet / Nearly / Got it!"). The answer key has every sheet except
Learn it, with answers in handwriting-style font and plotted graphs. Every sheet starts on a new page, so a
single sheet can be printed on its own.

| Code | Pack | Investigation | Case study | Pages (pack + key) |
|---|---|---|---|---|
| W1 | The Scientist's Toolkit | Which fabric soaks up the most water? | Two Boses: scientists from Bengal | 13 + 9 |
| A1 | Human Body Systems | How does exercise change my pulse? | Dhaka's air and our lungs | 13 + 10 |
| A2 | Cells, Tissues and Organs | Looking at cells with a microscope | Giving blood: cells that save lives | 13 + 9 |
| A3 | Staying Healthy | How well do we wash our hands? | Dengue: a city fights a mosquito | 12 + 9 |
| A4 | Eating for Health | How much sugar is in our drinks? | From panta bhat to pizza: changing plates | 11 + 8 |
| A5 | Plants: Seeds, Germination and Growth | Does light affect plant growth? | Floating gardens: farming on flood water | 15 + 11 |
| A6 | Flowering Plants: Reproduction and Life Cycles | Spinning seeds: a paper helicopter test | Bees, mustard and honey | 15 + 11 |
| A7 | Living Things in Their Environment | Comparing two habitats | The Sundarbans: a forest that protects us | 12 + 9 |
| B1 | Water for Life and the Water Cycle | Make a solar still | Too much water, not enough to drink | 13 + 9 |
| B2 | Soil and the Living Earth | Which soil holds the most water? | Worms that make money: vermicompost | 12 + 9 |
| B3 | Earth's Changing Surface | Do plants stop soil erosion? | Ready for the storm: saving lives from cyclones | 13 + 10 |
| B4 | Earth, Sun and Moon: Days, Years and Seasons | How does day length change through the year? | Six seasons, one planet | 13 + 9 |
| B5 | Resources and Sustainability | Our class rubbish audit | Saving the hilsa | 12 + 8 |
| B6 | Systems, Models and Technologies | Does a windcatcher model cool a room? | Bringing back Dhaka muslin | 11 + 6 |
| C1 | States of Matter | Does surface area affect evaporation? | Salt from the sun: Cox's Bazar salt farmers | 13 + 9 |
| C2 | Mixtures, Solutions and Changes | Does warm water dissolve sugar faster? | Khejur gur: winter sweetness and a hidden danger | 11 + 8 |
| C3 | Matter, Atoms and Conservation | Is mass conserved? | Energy from atoms: Rooppur | 12 + 8 |
| C4 | Energy and Its Transformations | Which wrapping keeps tea hottest? | Power from the sun: solar home systems | 11 + 8 |
| C5 | Sound | Ruler twang: length and pitch | Too loud! Noise in Dhaka | 12 + 9 |
| C6 | Mechanical Systems | How does distance from the pivot change the effort? | The rickshaw: a city on three wheels | 11 + 8 |
| C7 | Light: Sources, Reflection and Refraction | Investigating mirrors: angles of reflection | Healthy eyes in a screen world | 14 + 10 |
| C8 | Light: Shadows and Intensity | How does distance from the torch change shadow size? | A brighter, cooler classroom | 13 + 8 |

Codes follow the syllabus strands: **W** Working scientifically, **A** Living things, **B** Earth and space,
**C** Physical and chemical science. The download page has a coverage map listing every syllabus outcome
(quoted from the continuum) under the pack that teaches it, plus the Cambridge Stage 5 Learner's Book units
(1 Plants → A5, 2 Life cycles → A6, 3 States of matter → C1/B1/C2, 4 The way we see things → C7,
5 Shadows → C8, 6 Earth's movements → B4).

## 3. Printing

- Print the PDFs on **A4, black and white, double-sided** ("flip on long edge"), scale 100 % / "actual size".
- For one sheet only, print its page range (the page numbers are in each footer), or open the print view
  (`print/<slug>-study-pack.html`) and print from the browser.
- Teachers: print answer keys separately; they have "ANSWER KEY" at the top of every sheet.

## 4. Change or add content

You need Python 3 and Node.js. Once: `npm install --prefix worksheets/toolkit` (installs `playwright-core`).
Chromium: set `CHROME_PATH` to a Chrome/Chromium binary, or run `npx playwright install chromium` once.

1. Open the pack's file, e.g. `worksheets/toolkit/topics/c5_sound.py`. Each worksheet is a `Sheet(...)` with a list
   of blocks; each question is `Q('prompt', <answer block>, marks=N)` and **the answer is written next to the
   question**, so the learner pack and the answer key always match.
2. Rebuild that pack (fast, ~3 s): `python3 worksheets/toolkit/build.py C5`
3. Check `worksheets/grade-5-science/pdf/c5-sound-study-pack.pdf` and `…-answer-key.pdf`.
4. Before publishing, rebuild everything (also remakes the zips and download page): `python3 worksheets/toolkit/build.py`

Common building blocks (all in `ws.py`):

| Block | Use |
|---|---|
| `P('text')`, `H('heading', 3)`, `Bullets([...])`, `Box('fact'/'bd'/'history'/'safety'/'tip', P(...))` | article text; `**bold**`, `*italic*`, `CO~2~`, `cm^2^` |
| `Lines(n, 'model answer')` | answer lines |
| `Blanks('Water boils at [100] °C.', extra=['50'])` | gap fill with a word bank |
| `MCQ(['a', 'b', 'c'], 1)`, `TrueFalse([('statement', True), ('statement', False, 'correction')])` | quick checks |
| `Match([(left, right), ...])`, `Sort([cat1, cat2], [(item, cat), ...])`, `Order([...in correct order])` | matching, sorting, sequencing |
| `Table(headers, rows)` with `Ans('answer')` cells | tables to complete |
| `Label(art.ear(), art.EAR_PARTS)` | label a diagram |
| `Graph(labels, values, 'y label', 'x label', ymax=…, step=…, kind='bar'/'line')` | empty axes for learners; plotted in the key |
| `Draw('40mm', 'caption', 'model answer')`, `WordSearch([...])`, `Part('a) …', answer)` | drawing box, word search, lettered parts |

To add a new pack, copy a topic file, change `code`, `strand`, `title`, `outcomes` and the sheets, and build.
New illustrations go in `art.py` (SVG line art); new icons: copy from `@tabler/icons` into `toolkit/icons/`.

## 5. Copyright and credits

- All text, questions, case studies and drawings are original InquiryMind material. The packs follow the
  syllabus and the Cambridge Stage 5 topic order, but **no text or pictures from the Cambridge books were
  copied** (they are copyright Cambridge University Press). Case-study facts come from public sources named
  on each sheet; data marked "example" is illustrative.
- Fonts: Andika, Fredoka, Patrick Hand (SIL Open Font License 1.1; licence files in `assets/`).
  Icons: Tabler Icons (MIT). Linked simulations: PhET Interactive Simulations, CC BY-NC 4.0.
- Photos: none are used, so the packs print cleanly in black and white. Wikimedia Commons images could be
  added later (each needs its own author/licence credit printed beside it).

## 6. Working with Claude using fewer tokens

- Say exactly which pack and sheet: "In `worksheets/toolkit/topics/b2_soil.py`, case study sheet, add a question
  about…, then run `python3 worksheets/toolkit/build.py B2`."
- Never ask Claude to open files in `worksheets/grade-5-science/` (generated; PDFs and print pages are large).
- To check layout, ask for low-resolution page images of one pack (`pdftoppm -r 40`), not the whole set.
