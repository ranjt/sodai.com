# CLAUDE.md

Static website repo. `main` is published by GitHub Pages (`.github/workflows/static.yml`, whole repo) to amrarbazar.com.

## Map
- `index.html` — Amrar Bazar clothing shop, single file (~3000 lines, inline CSS/JS, Bangla/English via `data-t`).
- `simulations/` (math) and `science-simulations/` (science) — 56 PhET-adapted, InquiryMind-branded K–6 simulations,
  live at amrarbazar.com/simulations/ and /science-simulations/. Each: `index.html` catalog, `sims/<id>.html`,
  `thumbnails/<id>.png`, `README.md`, `BUILD-SOURCES.txt`.
- `offline-simulations/README.md` — full user guide (deploy to Firebase/inquirymind.org, embed, license, sim table).
- `offline-simulations/inquirymind-site/` — same sims with InquiryMind-styled catalog pages, for the user's Firebase site.
- `offline-simulations/toolkit/` — rebuild/rebrand/add sims; steps in `toolkit/README.md`.
- `worksheets/` — InquiryMind science study packs + answer keys: KG (12 packs, KG1+KG2, grade 0 = `kg-science/`, `topics/kg/`),
  Grade 1 (11), 2 (12), 3 (14), 4 (20), 5 (24 incl. extras C9 heat transfer, C10 energy resources with sourced data). Guide:
  `worksheets/README.md`; every PDF listed in `worksheets/ALL-WORKSHEETS.md` (written by `inventory.py` on each build).
  Source: `worksheets/toolkit/topics/grade<N>/<code>_*.py` (one pack per file; codes W1, A*, B*, C*),
  components `ws.py`, SVG art `art.py` + `art4.py` (G4) + `art23.py` (G2–3), OpenMoji pictures `openmoji.py` (CC BY-SA), download pages `hub.py`.
  Output (generated): `worksheets/index.html` + `worksheets/grade-<N>-science/`, live at amrarbazar.com/worksheets/,
  copied to `offline-simulations/inquirymind-site/worksheets/`. KG/G1 picture blocks in `ws.py`: Choose, PicMatch, PicSort,
  Pictograph, Trace. Publishing to inquirymind.org: `offline-simulations/inquirymind-site/publish.sh` + `PUBLISH-WORKSHEETS.md`
  (copy-only, no rebuild); `CLAUDE-INQUIRYMIND.md` is the CLAUDE.md for the user's InquiryMind Firebase project.
- `worksheets/thinking-routines/` — Visible Thinking Routines (VTR) section: 34 one-page A4 landscape organisers (R01–R34,
  Project Zero routines, original InquiryMind design and icons, PZ credited in the footer) + download page, previews, zip.
  Source: `worksheets/toolkit/routines.py` (list `ROUTINES`, 10 layouts) + `rt_icons.py`; page `hub.write_routines`.
  Build `python3 worksheets/toolkit/routines.py [R01]`. "Thinking routines" tab is on every catalog/worksheet page.
  Worksheets show only InquiryMind branding, tagline and mission (no school continuum or Cambridge wording).
- `question-bank/` — science Practice questions KG–G5 for inquirymind.org (one JSON per worksheet topic in
  `questions/<kg|grade-N>/<code>-<name>.json`; modes core/picture/real-life/simulation/olympiad = the site's practice cards;
  8 types). Format + marking rules: `question-bank/README.md`. Check `python3 question-bank/tools/validate.py`, build
  `python3 question-bank/tools/build_bank.py` (→ `dist/`, copy in `offline-simulations/inquirymind-site/question-bank/`).
  Player/preview: `preview/qb-player.js`, `preview/index.html`. Pictures: `images/index.json` (`tools/images.py`).
  Never open `dist/*.json` whole. `INQUIRYMIND-INTEGRATION-PROMPT.md` = prompt for the user's InquiryMind Claude project.

## Rules (save tokens, avoid breakage)
- Never open, grep or diff `**/sims/*.html` (2.7–8 MB minified each). Sim metadata (id, name, grade, topics,
  group) lives only in `offline-simulations/toolkit/catalog.py`.
- Never hand-edit the four catalog `index.html` files; edit `catalog.py`, then run
  `python3 offline-simulations/toolkit/catalog.py pages` (rewrites all four).
- Sim files must stay identical in `simulations/`, `science-simulations/` and their copies in
  `offline-simulations/inquirymind-site/`; `toolkit/install_builds.py` updates both.
- Rebuilding needs the PhET work folder (`toolkit/setup_phet.sh`, ~7 GB, ~5 min) and always `--transpile=false`
  builds (`toolkit/build_sims.sh`); parallel re-transpiling corrupts builds.
- Never open or hand-edit `worksheets/index.html` or `worksheets/grade-*-science/**` (generated). Edit a topic file, then
  `python3 worksheets/toolkit/build.py --grade 4 C5` (one pack, ~3 s) or no args (all grades + zips + hubs + IM copy).
  Needs `CHROME_PATH` and `npm install --prefix worksheets/toolkit` once. Check layout with `pdftoppm -r 40`.
- Worksheet content is original: never copy text/images from the Cambridge books the user uploaded (copyright).
- License: PhET builds are CC BY-NC 4.0 (non-commercial). Keep all PhET credits; never use the PhET logo; never
  edit the license header in sim files.

## Facts that are expensive to rediscover
- PhET emptied its GitHub repos on 2026-10-09 (private monorepo). Builds use pinned pre-sunset commits in
  `offline-simulations/toolkit/source-commits.txt`.
- Custom brand `inquirymind`: `toolkit/brand/inquirymind/` (Brand.ts = About box; inquirymind-splash.js = purple
  loading screen + corner credit; images from `toolkit/make_brand.py`).
- Cloud sessions: phet.colorado.edu, amrarbazar.com, inquirymind.org, Wikimedia, Oak, NCTB and most OER sites are
  blocked by the network policy; github.com, raw.githubusercontent.com and registry.npmjs.org work. Chromium for tests: `CHROME_PATH=$(ls -d /opt/pw-browsers/chromium-*/chrome-linux/chrome | head -1)`.
