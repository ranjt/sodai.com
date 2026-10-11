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
- `worksheets/` — 22 InquiryMind Grade 5 Science study packs + answer keys (guide: `worksheets/README.md`).
  Source: `worksheets/toolkit/topics/<code>_*.py` (one pack per file; codes W1, A1–A7, B1–B6, C1–C8), components
  `ws.py`, SVG art `art.py`, download page `hub.py`. Output (generated): `worksheets/grade-5-science/`, live at
  amrarbazar.com/worksheets/grade-5-science/, copied to `offline-simulations/inquirymind-site/worksheets/`.

## Rules (save tokens, avoid breakage)
- Never open, grep or diff `**/sims/*.html` (2.7–8 MB minified each). Sim metadata (id, name, grade, topics,
  group) lives only in `offline-simulations/toolkit/catalog.py`.
- Never hand-edit the four catalog `index.html` files; edit `catalog.py`, then run
  `python3 offline-simulations/toolkit/catalog.py pages` (rewrites all four).
- Sim files must stay identical in `simulations/`, `science-simulations/` and their copies in
  `offline-simulations/inquirymind-site/`; `toolkit/install_builds.py` updates both.
- Rebuilding needs the PhET work folder (`toolkit/setup_phet.sh`, ~7 GB, ~5 min) and always `--transpile=false`
  builds (`toolkit/build_sims.sh`); parallel re-transpiling corrupts builds.
- Never open or hand-edit `worksheets/grade-5-science/**` (generated). Edit a topic file, then
  `python3 worksheets/toolkit/build.py C5` (one pack, ~3 s) or no codes (all packs + zips + hub + IM copy).
  Needs `CHROME_PATH` and `npm install --prefix worksheets/toolkit` once. Check layout with `pdftoppm -r 40`.
- Worksheet content is original: never copy text/images from the Cambridge books the user uploaded (copyright).
- License: PhET builds are CC BY-NC 4.0 (non-commercial). Keep all PhET credits; never use the PhET logo; never
  edit the license header in sim files.

## Facts that are expensive to rediscover
- PhET emptied its GitHub repos on 2026-10-09 (private monorepo). Builds use pinned pre-sunset commits in
  `offline-simulations/toolkit/source-commits.txt`.
- Custom brand `inquirymind`: `toolkit/brand/inquirymind/` (Brand.ts = About box; inquirymind-splash.js = purple
  loading screen + corner credit; images from `toolkit/make_brand.py`).
- Cloud sessions: phet.colorado.edu, amrarbazar.com and inquirymind.org are blocked by the network policy;
  github.com and registry.npmjs.org work. Chromium for tests: `CHROME_PATH=$(ls -d /opt/pw-browsers/chromium-*/chrome-linux/chrome | head -1)`.
