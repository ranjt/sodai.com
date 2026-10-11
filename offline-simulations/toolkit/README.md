# Toolkit: rebuild, rebrand or add simulations

Everything needed to rebuild the 56 InquiryMind-branded PhET simulations from source.
You only need this to **change** the simulations (new logo, more sims, fixes). To **use** them,
see `../README.md`.

## What's here

| File | What it does |
|---|---|
| `catalog.py` | **Single source of truth**: every sim's id, name, group, grades and topics. Also writes the 4 catalog pages. |
| `setup_phet.sh` | Recreates the PhET build environment in a work folder (clone repos at pinned commits, add brand, install, compile). |
| `build_sims.sh` | Builds sims with the InquiryMind brand (3 at a time). |
| `install_builds.py` | Copies built sims into both site folders and regenerates the catalog pages. |
| `add_sim.sh` | Adds another PhET sim (and the libraries it needs) to the work folder. |
| `make_brand.py` | Regenerates the brand images (navbar logo with "adapted from PhET" credit, loading-screen logo). |
| `test/check_sims.js` | Opens every sim in headless Chromium, fuzz-tests it, and optionally makes thumbnails. |
| `source-commits.txt` | Exact commit of every phetsims repo used (`repo sha` per line). |
| `brand/inquirymind/` | The custom PhET brand (logo images, About-box text, purple loading screen with corner credit). |
| `logo/` | Original logo, the transparent versions used by the brand, and the script that made them. |

## Requirements

- Linux or macOS (on Windows use WSL), `git`, `bash`, Python 3 with Pillow (`pip install pillow`),
  Node.js 18+ (tested with 22) and npm.
- Internet access to `github.com` and `registry.npmjs.org`. About 7 GB free disk for the work folder.
- For testing and thumbnails: Chromium or Chrome (`CHROME_PATH=/path/to/chrome`) or `npx playwright install chromium`.

Run all commands **from the repository root**. `WORK` is any empty folder outside the repo, for example `~/phet-work`.

## Rebuild everything (about 40 minutes)

```bash
offline-simulations/toolkit/setup_phet.sh ~/phet-work            # ~5 min
offline-simulations/toolkit/build_sims.sh ~/phet-work            # ~30 min for all 56 (OK/FAIL per sim)
python3 offline-simulations/toolkit/install_builds.py ~/phet-work
npm install --prefix offline-simulations/toolkit/test            # once
node offline-simulations/toolkit/test/check_sims.js --thumbnails \
  simulations science-simulations                                 # ~15 min; every line should be OK
cp simulations/thumbnails/* offline-simulations/inquirymind-site/simulations/thumbnails/
cp science-simulations/thumbnails/* offline-simulations/inquirymind-site/science-simulations/thumbnails/
```

Then commit and push (see `../README.md`, "Publish changes").

## Rebuild only some sims

```bash
offline-simulations/toolkit/build_sims.sh ~/phet-work make-a-ten balancing-act
python3 offline-simulations/toolkit/install_builds.py ~/phet-work make-a-ten balancing-act
```

## Change the logo

1. Get the new logo as **transparent PNGs**: one with light text (for dark backgrounds) and, ideally,
   one with dark text (for light backgrounds). Wide format, at least 900 px wide.
2. Save them over `logo/logo-on-dark.png` and `logo/logo-on-light.png`, or pass them directly:
   `python3 offline-simulations/toolkit/make_brand.py --dark dark.png --light light.png`
3. Also replace `inquirymind-logo.png` (the catalog page header logo) in both folders under
   `offline-simulations/inquirymind-site/` with the light-background version.
4. Rebuild everything (section above). `setup_phet.sh` copies the updated brand; if your work folder
   already exists, run: `rm -rf ~/phet-work/brand/inquirymind && cp -r offline-simulations/toolkit/brand/inquirymind ~/phet-work/brand/`
   and then re-compile: `(cd ~/phet-work/chipper && npx grunt transpile --repos=brand)`.

Loading-screen colour and corner credit text: `brand/inquirymind/js/inquirymind-splash.js`.
About-box name, license text and links: `brand/inquirymind/js/Brand.ts`. Re-compile + rebuild after editing.

## Add a simulation

```bash
offline-simulations/toolkit/add_sim.sh ~/phet-work pendulum-lab   # clones it + libraries, records commits
# add a row to the math or science 'sims' list in catalog.py, e.g.
#   ('pendulum-lab', 'Pendulum Lab', 'physics', 6, 8, 'Pendulums, period and energy'),
offline-simulations/toolkit/build_sims.sh ~/phet-work pendulum-lab
python3 offline-simulations/toolkit/install_builds.py ~/phet-work pendulum-lab
node offline-simulations/toolkit/test/check_sims.js --thumbnails science-simulations
cp science-simulations/thumbnails/pendulum-lab.png offline-simulations/inquirymind-site/science-simulations/thumbnails/
```

## Change names, grades, topics or groups (no rebuild)

Edit the lists in `catalog.py`, then `python3 offline-simulations/toolkit/catalog.py pages`.

## Things that will bite you

- **Never let parallel builds re-compile shared code.** `build_sims.sh` passes `--transpile=false`; the
  shared code is compiled once by `setup_phet.sh` / `add_sim.sh`. Without this, parallel builds corrupt each
  other and some sims fail with errors like "Class extends value ... is not a constructor".
- **PhET's main branches are empty since 2026-10-09** (they moved to a private monorepo). The pinned commits
  in `source-commits.txt` still work because old history is kept. If PhET ever deletes those repos, the built
  files in this repository are the only copy, so keep backups.
- `phet-io` and other private repos are not needed; "skipping repo (not checked out)" messages are normal.
- Builds print "Missing or incorrect build-local.json" and "Browserslist ... old": harmless.
- Each sim's `package.json` must list `inquirymind` in `supportedBrands` (setup and add_sim do this), or
  the build fails with "Unsupported brand".
- Brand id `inquirymind` is registered in `chipper/js/common/ChipperConstants.ts` and its loading-screen
  script in `chipper/build.json` (both patched by `setup_phet.sh`).
