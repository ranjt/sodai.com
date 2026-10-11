# Science study packs (InquiryMind): Grade 4 and Grade 5

Print-ready, black-and-white study packs that cover the whole science syllabus of each grade (PHIS Science continuum
2025: Grade 4 = IB PYP Phase 3, Grade 5 = IB PYP Phase 4) and the topics of Cambridge Primary Science Stage 4 / Stage 5.
Every pack has its own answer key. Everything is original InquiryMind material: articles, questions, case studies and
line drawings, plus open-licensed OpenMoji pictures in the Grade 4 packs.

| Grade | Packs | Live page (after merging to `main`) |
|---|---|---|
| all grades | grade chooser | **https://amrarbazar.com/worksheets/** |
| Grade 4 | 20 packs (W1, A1–A6, B1–B4, C1–C9) | https://amrarbazar.com/worksheets/grade-4-science/ |
| Grade 5 | 22 packs (W1, A1–A7, B1–B6, C1–C8) | https://amrarbazar.com/worksheets/grade-5-science/ |

InquiryMind copy: `offline-simulations/inquirymind-site/worksheets/` (copy the `worksheets` folder into the Firebase
`public/` folder → `https://www.inquirymind.org/worksheets/`).

## 1. What's where

```
worksheets/
├── README.md                    this guide
├── index.html                   GENERATED: grade chooser page
├── grade-4-science/             GENERATED: Grade 4 website folder (do not edit by hand)
├── grade-5-science/             GENERATED: Grade 5 website folder (do not edit by hand)
│   ├── index.html               download page: packs by strand, PDFs, answer keys, syllabus coverage map
│   ├── pdf/<slug>-study-pack.pdf    learner pack (cover, 6 worksheets, self-check)
│   ├── pdf/<slug>-answer-key.pdf    teacher answer key (same pages, answers filled in)
│   ├── print/<slug>-*.html      the same packs as web pages (open, then Ctrl+P)
│   ├── downloads/               all study packs (zip) and all answer keys (zip)
│   └── assets/                  logo, fonts (OFL), stylesheet
└── toolkit/                     SOURCE: edit here, then rebuild
    ├── build.py                 builds HTML + PDF + zips + download pages + InquiryMind copy
    ├── topics/grade4/<code>_*.py    ONE FILE PER PACK: all text, questions and answers (Grade 4)
    ├── topics/grade5/<code>_*.py    the same for Grade 5
    ├── ws.py                    worksheet building blocks (questions, tables, graphs, pictures, word search …)
    ├── art.py, art4.py          illustrations drawn as SVG line art (art4 = Grade 4 drawings)
    ├── openmoji.py, openmoji/   OpenMoji pictures (names → files; fetch script); CC BY-SA 4.0
    ├── hub.py                   the download pages (also: which simulations link to which pack)
    ├── styles.css               A4 print design (Grade 4 has larger print: body class g4)
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

### Grade 4

Grade 4 packs use larger print, more writing space and many more pictures (OpenMoji line art) for younger readers.

| Code | Pack | Investigation | Case study | Pages (pack + key) |
|---|---|---|---|---|
| W1 | Science Detectives: Working Scientifically | Does a higher drop make a higher bounce? | Dr Firdausi Qadri: science that saves lives | 13 + 8 |
| A1 | Animals of Bangladesh: Diversity and Classification | Minibeast hunt in the school garden | Winter visitors: the birds of Tanguar Haor | 14 + 9 |
| A2 | Plants of Bangladesh: Diversity and Adaptation | Does a waxy coat stop leaves drying out? | Water hyacinth: a problem or a gift? | 14 + 9 |
| A3 | Life Cycles, Growth and Inheritance | What do seeds need to grow? | Rajshahi silk: the life cycle of the silkworm | 13 + 9 |
| A4 | Ecosystems and Interactions | Do snails prefer damp or dry places? | Rice and fish: farming partners | 13 + 8 |
| A5 | Food Chains and Food Webs | Counting a rice field food chain | When the vultures disappeared | 14 + 10 |
| A6 | Humans and the Environment | Our school litter survey | The golden fibre: can jute beat plastic? | 11 + 8 |
| B1 | Weather and Climate | A week at our weather station | Harvest before the flood: forecasts for haor farmers | 14 + 10 |
| B2 | Storms, Cyclones and Climate Change | Track a cyclone | Ready for the storm: a family cyclone plan | 13 + 9 |
| B3 | Changing Landscapes | Does a windbreak stop sand blowing away? | Living with a moving river | 13 + 8 |
| B4 | Earth's Resources and Sustainability | How much water does a dripping tap waste? | Catching the rain on the coast | 10 + 7 |
| C1 | Matter: States, Elements and Compounds | The melting race | Ice for the fishing boats | 12 + 7 |
| C2 | Mixtures and Separation | Which filter cleans muddy water best? | The SONO filter: clean water from a Bangladeshi invention | 12 + 8 |
| C3 | Atoms and Their Structure | Build and compare atom models | How did we find out about atoms? | 11 + 8 |
| C4 | Forces and Motion | Which surface has the most friction? | Kabaddi and tug-of-war: the forces in our games | 12 + 8 |
| C5 | Floating and Flying | Foil boats: which shape holds most? | Safe on the water: boats and launches | 11 + 8 |
| C6 | Electricity and Circuits | Does wire length change brightness? | Lights for every home | 13 + 9 |
| C7 | Magnets and Electromagnets | How strong are our magnets? | Giant magnets in the ship-breaking yards | 12 + 8 |
| C8 | Energy and Work | Rubber band launcher | Cooking with cow dung: biogas | 11 + 7 |
| C9 | Light and Sound | Which material muffles sound best? | The music of the Bauls | 13 + 7 |

### Grade 5

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
(quoted from the continuum) under the pack that teaches it, plus the Cambridge Learner's Book units.
Grade 4 (Stage 4): 1 Humans and animals → A1, A3; 2 Living things and environments → A1, A4, A6, B4;
3 Solids, liquids and gases → C1; 4 Sound → C9; 5 Electricity and magnetism → C6, C7.
Grade 5 (Stage 5): 1 Plants → A5; 2 Life cycles → A6; 3 States of matter → C1, B1, C2; 4 The way we see things → C7;
5 Shadows → C8; 6 Earth's movements → B4.

## 3. Printing

- Print the PDFs on **A4, black and white, double-sided** ("flip on long edge"), scale 100 % / "actual size".
- For one sheet only, print its page range (the page numbers are in each footer), or open the print view
  (`print/<slug>-study-pack.html`) and print from the browser.
- Teachers: print answer keys separately; they have "ANSWER KEY" at the top of every sheet.

## 4. Change or add content

You need Python 3 and Node.js. Once: `npm install --prefix worksheets/toolkit` (installs `playwright-core`).
Chromium: set `CHROME_PATH` to a Chrome/Chromium binary, or run `npx playwright install chromium` once.

1. Open the pack's file, e.g. `worksheets/toolkit/topics/grade5/c5_sound.py` (or `topics/grade4/…`). Each worksheet is a `Sheet(...)` with a list
   of blocks; each question is `Q('prompt', <answer block>, marks=N)` and **the answer is written next to the
   question**, so the learner pack and the answer key always match.
2. Rebuild that pack (fast, ~3 s): `python3 worksheets/toolkit/build.py --grade 5 C5`
3. Check `worksheets/grade-5-science/pdf/c5-sound-study-pack.pdf` and `…-answer-key.pdf`.
4. Before publishing, rebuild everything (all grades, zips, download pages, InquiryMind copy):
   `python3 worksheets/toolkit/build.py` (or one grade: `--grade 4`).

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
| `Pics([('tiger', 'mammal'), ('frog', Ans('amphibian'))], cols=5)` | picture cards (OpenMoji names); `Ans` = blank to fill in |
| `KeyFig(learner_svg, key_svg)`, `Wide(block)` | a different drawing in the answer key; a full-width block inside `Cols` |
| `Box('try', …)`, `Box('check', …)` | "Try this at home" and "Quick check" boxes |
| `art.pic('tiger', x, y, size)`, `art.pic_row([...])` | OpenMoji pictures inside your own drawings or in a row |

To add a new pack, copy a topic file, change `code`, `strand`, `title`, `outcomes` and the sheets, and build.
New illustrations go in `art.py` / `art4.py` (SVG line art); new icons: copy from `@tabler/icons` into `toolkit/icons/`.
New pictures: add a name and hex code to `NAMES` in `openmoji.py` (codes at https://openmoji.org/library/), then run
`python3 worksheets/toolkit/openmoji.py fetch` (downloads from the pinned OpenMoji release on GitHub).

## 5. Copyright and credits

- All text, questions, case studies and drawings are original InquiryMind material. The packs follow the
  syllabus and the Cambridge Stage 4/5 topic order, but **no text or pictures from the Cambridge books were
  copied** (they are copyright Cambridge University Press). Case-study facts come from public sources named
  on each sheet; data marked "example" is illustrative.
- Fonts: Andika, Fredoka, Patrick Hand (SIL Open Font License 1.1; licence files in `assets/`).
  Icons: Tabler Icons (MIT). Linked simulations: PhET Interactive Simulations, CC BY-NC 4.0.
- Pictures (Grade 4): **OpenMoji** (https://openmoji.org, open-source emoji and icons on GitHub), licence
  **CC BY-SA 4.0**; the credit is printed on every pack cover that uses them and on the download page.
- No photos are used, so the packs print cleanly in black and white. Wikimedia Commons images could be added
  later (each needs its own author/licence credit), if upload.wikimedia.org is allowed in the cloud environment.

## 6. Working with Claude using fewer tokens

- Say exactly which grade, pack and sheet: "In `worksheets/toolkit/topics/grade4/b2_storms_cyclones.py`, case study
  sheet, add a question about…, then run `python3 worksheets/toolkit/build.py --grade 4 B2`."
- Never ask Claude to open files in `worksheets/grade-*-science/` (generated; PDFs and print pages are large).
- Start a new Claude session for each new task; `CLAUDE.md` gives Claude the project map, so old chats are not needed.
- To check layout, ask for low-resolution page images of one pack (`pdftoppm -r 40`), not the whole set.
