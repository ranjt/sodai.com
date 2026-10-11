# Offline Simulations: start here

All 56 K–6 simulations (28 math, 28 science), adapted from **PhET Interactive Simulations,
University of Colorado Boulder** and branded for **InquiryMind**, plus everything needed to use,
publish, change and rebuild them.

- [1. What's where](#1-whats-where)
- [2. Use them offline (classroom / USB)](#2-use-them-offline-classroom--usb)
- [3. Publish on inquirymind.org (Firebase)](#3-publish-on-inquirymindorg-firebase)
- [4. Publish on amrarbazar.com (GitHub Pages)](#4-publish-on-amrarbazarcom-github-pages)
- [5. Embed or link one simulation](#5-embed-or-link-one-simulation)
- [6. All 56 simulations](#6-all-56-simulations)
- [7. Credit and license rules](#7-credit-and-license-rules)
- [8. Common changes](#8-common-changes)
- [9. Troubleshooting](#9-troubleshooting)
- [10. Working with Claude using fewer tokens](#10-working-with-claude-using-fewer-tokens)

---

## 1. What's where

```
sodai.com/                               (this repository)
├── CLAUDE.md                            short project map that Claude reads automatically
├── index.html                           Amrar Bazar shop (unrelated to the simulations)
├── simulations/                         math   → amrarbazar.com/simulations/          (live)
├── science-simulations/                 science → amrarbazar.com/science-simulations/  (live)
└── offline-simulations/                 ← THIS FOLDER
    ├── README.md                        this guide
    ├── inquirymind-site/                ready to copy into the InquiryMind Firebase site
    │   ├── simulations/                 math catalog page (InquiryMind style) + 28 sims
    │   ├── science-simulations/         science catalog page (InquiryMind style) + 28 sims
    │   └── worksheets/                  Grade 4 and Grade 5 science study packs + answer keys (see worksheets/README.md)
    └── toolkit/                         rebuild / rebrand / add sims (see toolkit/README.md)
```

Each simulation folder (`simulations/`, `science-simulations/`, in either site) is **self-contained**:

| Path | What it is |
|---|---|
| `index.html` | Catalog page: grade filter (K–2, 3–5, 6), search, Open and Download buttons |
| `sims/<id>.html` | One complete simulation in one file (2.7–8 MB, English). Works with no internet. |
| `thumbnails/<id>.png` | 600×394 preview images for the catalog |
| `inquirymind-logo.png` | Page header logo (InquiryMind copy only) |
| `README.md`, `BUILD-SOURCES.txt` | Credits/license and the exact PhET source commits used |

The simulation files are **identical** in the Amrar Bazar and InquiryMind copies; only the catalog
pages differ (Amrar Bazar green style with "Back to shop" vs. InquiryMind purple style with the logo).
Sizes: math 97 MB, science 107 MB.

**Get this folder onto your computer:** on GitHub open the repository, click **Code → Download ZIP**,
unzip, and use `offline-simulations/`. Or: `git clone https://github.com/ranjt/sodai.com.git`.

## 2. Use them offline (classroom / USB)

1. Copy `offline-simulations/inquirymind-site/` (or just one of its two folders) to the computer or a USB stick.
2. Double-click `simulations/index.html` or `science-simulations/index.html`. It opens in the browser and works
   without internet. (Without internet the page uses the system font instead of DM Sans; nothing else changes.)
3. Or open any single simulation directly: `sims/<id>.html`. The **Download** button on a card saves that
   one file, which can be shared on its own (e.g. by email, WhatsApp or a learning platform).

Works in current Chrome, Edge, Firefox and Safari, on desktops, laptops, Chromebooks and tablets.
The Math/Science/Worksheets tabs on the catalog pages link to `../simulations/`, `../science-simulations/` and
`../worksheets/`, so keep the folders side by side if you want the tabs to work.

## 3. Publish on inquirymind.org (Firebase)

You need the Firebase project folder for inquirymind.org on your computer (the folder with `firebase.json`)
and the Firebase CLI (`npm install -g firebase-tools`, then `firebase login`).

1. Find the public folder: open `firebase.json` and look at `"hosting": { "public": "..." }` (usually `public`).
2. Copy **all three** folders from `offline-simulations/inquirymind-site/` into it:
   ```
   public/
   ├── index.html                 (your existing site)
   ├── simulations/               ← copy
   ├── science-simulations/       ← copy
   └── worksheets/                ← copy (Grade 4 and 5 science study packs)
   ```
3. Deploy: `firebase deploy --only hosting`
4. Check: https://www.inquirymind.org/simulations/, https://www.inquirymind.org/science-simulations/ and
   https://www.inquirymind.org/worksheets/
5. Add links from your site's menu or pages:
   ```html
   <a href="/simulations/">Math Simulations</a>
   <a href="/science-simulations/">Science Simulations</a>
   <a href="/worksheets/">Science Worksheets</a>
   ```

Notes:
- The "← InquiryMind home" link on the catalog pages goes to `/`.
- If `firebase.json` has a catch-all rewrite (`"source": "**"` → `/index.html`, common for single-page apps),
  that is fine: Firebase serves real files before applying rewrites.
- Optional, faster repeat visits: cache the large files for a week by adding this inside `"hosting"`:
  ```json
  "headers": [
    { "source": "**/sims/**", "headers": [ { "key": "Cache-Control", "value": "public, max-age=604800" } ] },
    { "source": "**/thumbnails/**", "headers": [ { "key": "Cache-Control", "value": "public, max-age=604800" } ] }
  ]
  ```
- **Free-plan bandwidth:** Firebase Hosting's free (Spark) plan includes 10 GB storage but only about
  **360 MB of downloads per day**. Each simulation is 1.5–3 MB after compression, so roughly 120–250
  simulation opens per day fit in the free plan. For whole classes, switch to the pay-as-you-go (Blaze)
  plan, which keeps the free amount and charges a small fee per extra GB. Check current numbers at
  https://firebase.google.com/pricing.

## 4. Publish on amrarbazar.com (GitHub Pages)

The `simulations/` and `science-simulations/` folders at the repository root are already live at
https://amrarbazar.com/simulations/ and https://amrarbazar.com/science-simulations/. The worksheets
(`worksheets/`) are live at https://amrarbazar.com/worksheets/ (Grade 4 and Grade 5) once merged.
Any change merged into the `main` branch is published automatically by
`.github/workflows/static.yml` (about one minute; check the **Actions** tab on GitHub).

There is no link to the simulations from the shop page yet; add one to `index.html` if you want it.
GitHub Pages limits: site up to 1 GB, about 100 GB of downloads per month (soft limit).

## 5. Embed or link one simulation

Link (opens full screen):
```html
<a href="/science-simulations/sims/forces-and-motion-basics.html" target="_blank">Forces and Motion: Basics</a>
```

Embed in a page (16:10 box that scales on phones):
```html
<div style="position:relative;width:100%;max-width:960px;aspect-ratio:16/10">
  <iframe src="/simulations/sims/make-a-ten.html" title="Make a Ten"
          style="position:absolute;inset:0;width:100%;height:100%;border:0" allowfullscreen></iframe>
</div>
```

Useful link options (add after `.html`):

| Option | Effect |
|---|---|
| `?screens=2` | Open screen 2 directly, without the home screen (`?screens=1,3` keeps only screens 1 and 3) |
| `?audio=disabled` | No sound |

The credit (InquiryMind logo + "adapted from PhET") is inside every simulation, so embedded sims stay credited.

## 6. All 56 simulations

`<folder>` is `simulations` (math) or `science-simulations` (science). Grade "K" = Kindergarten;
"stretch" = leans toward Grades 6–8. This table is generated by `python3 offline-simulations/toolkit/catalog.py table`.

| Subject | Group | Simulation | File (`<folder>/sims/…`) | Grade | Topics |
|---|---|---|---|---|---|
| Math | Kindergarten – Grade 2 | Number Play | `simulations/sims/number-play.html` | K–2 | Counting 1–20, ten frames, recognizing small amounts at a glance |
| Math | Kindergarten – Grade 2 | Make a Ten | `simulations/sims/make-a-ten.html` | K–2 | Place value, adding by making tens |
| Math | Kindergarten – Grade 2 | Number Compare | `simulations/sims/number-compare.html` | K–2 | Comparing numbers, greater than and less than |
| Math | Kindergarten – Grade 2 | Number Pairs | `simulations/sims/number-pairs.html` | K–2 | Splitting numbers into parts, addition facts |
| Math | Grades 3 – 5 | Arithmetic | `simulations/sims/arithmetic.html` | 3–5 | Multiplication, division and factoring practice |
| Math | Grades 3 – 5 | Area Builder | `simulations/sims/area-builder.html` | 3–5 | Area and perimeter with unit squares |
| Math | Grades 3 – 5 | Area Model Introduction | `simulations/sims/area-model-introduction.html` | 3–4 | Area as multiplication |
| Math | Grades 3 – 5 | Area Model Multiplication | `simulations/sims/area-model-multiplication.html` | 4–5 | Multi-digit multiplication, partial products |
| Math | Grades 3 – 5 | Fractions: Intro | `simulations/sims/fractions-intro.html` | 3–5 | What a fraction is, different ways to show one |
| Math | Grades 3 – 5 | Fractions: Equality | `simulations/sims/fractions-equality.html` | 3–5 | Equivalent fractions |
| Math | Grades 3 – 5 | Fractions: Mixed Numbers | `simulations/sims/fractions-mixed-numbers.html` | 4–5 | Improper fractions and mixed numbers |
| Math | Grades 3 – 5 | Fraction Comparison | `simulations/sims/fraction-comparison.html` | 3–4 | Comparing fractions |
| Math | Grades 3 – 5 | Build a Fraction | `simulations/sims/build-a-fraction.html` | 3–5 | Building fractions with shapes and numbers |
| Math | Grades 3 – 5 | Fraction Matcher | `simulations/sims/fraction-matcher.html` | 3–5 | Matching equal fractions (game) |
| Math | Grades 3 – 5 | Estimation | `simulations/sims/estimation.html` | 3–5 | Estimating length, area and volume |
| Math | Grades 3 – 5 | Function Builder: Basics | `simulations/sims/function-builder-basics.html` | 3–5 | Input and output patterns, early algebra |
| Math | Grades 5 – 6 | Area Model Decimals | `simulations/sims/area-model-decimals.html` | 5–6 | Multiplying decimals |
| Math | Grades 5 – 6 | Mean: Share and Balance | `simulations/sims/mean-share-and-balance.html` | 5–6 | Introduction to the mean (average) |
| Math | Grades 5 – 6 | Equality Explorer: Basics | `simulations/sims/equality-explorer-basics.html` | 5–6 | Balance-scale equations, finding unknowns |
| Math | Grades 5 – 6 | Ratio and Proportion | `simulations/sims/ratio-and-proportion.html` | 5–6 | Ratios |
| Math | Grades 5 – 6 | Unit Rates | `simulations/sims/unit-rates.html` | 6 | Unit price and rates |
| Math | Grades 5 – 6 | Proportion Playground | `simulations/sims/proportion-playground.html` | 6 | Proportional reasoning |
| Math | Grades 5 – 6 | Number Line: Integers | `simulations/sims/number-line-integers.html` | 6 | Negative numbers, absolute value |
| Math | Grades 5 – 6 | Number Line: Operations | `simulations/sims/number-line-operations.html` | 6 | Adding and subtracting on a number line |
| Math | Grades 5 – 6 | Number Line: Distance | `simulations/sims/number-line-distance.html` | 6 | Distance between points |
| Math | Grades 5 – 6 | Quadrilateral | `simulations/sims/quadrilateral.html` | 5–6 | Properties of four-sided shapes |
| Math | Grades 5 – 6 | Expression Exchange | `simulations/sims/expression-exchange.html` | 6 | Combining like terms |
| Math | Grades 5 – 6 | Center and Variability | `simulations/sims/center-and-variability.html` | 6 | Median, mean and spread |
| Science | Physics | Forces and Motion: Basics | `science-simulations/sims/forces-and-motion-basics.html` | K–5 | Pushes and pulls, friction, speed |
| Science | Physics | Balancing Act | `science-simulations/sims/balancing-act.html` | 3–6 | Balance and levers |
| Science | Physics | Friction | `science-simulations/sims/friction.html` | 3–6 | How rubbing surfaces make heat |
| Science | Physics | Balloons and Static Electricity | `science-simulations/sims/balloons-and-static-electricity.html` | 3–6 | Static charge, attraction and repulsion |
| Science | Physics | John Travoltage | `science-simulations/sims/john-travoltage.html` | 3–6 | Static shocks |
| Science | Physics | Magnet and Compass | `science-simulations/sims/magnet-and-compass.html` | 3–6 | Magnetic fields and compasses |
| Science | Physics | Magnets and Electromagnets | `science-simulations/sims/magnets-and-electromagnets.html` | 3–6 | Bar magnets and electromagnets |
| Science | Physics | Circuit Construction Kit: DC | `science-simulations/sims/circuit-construction-kit-dc.html` | 4–6 | Simple circuits, conductors and insulators |
| Science | Physics | Energy Forms and Changes | `science-simulations/sims/energy-forms-and-changes.html` | 4–6 | Energy transfer and heat |
| Science | Physics | Energy Skate Park: Basics | `science-simulations/sims/energy-skate-park-basics.html` | 4–6 | Motion and stored energy |
| Science | Physics | Waves Intro | `science-simulations/sims/waves-intro.html` | 4–6 | Water, sound and light waves |
| Science | Physics | Sound Waves | `science-simulations/sims/sound-waves.html` | 4–6 | Vibration, pitch and loudness |
| Science | Physics | Color Vision | `science-simulations/sims/color-vision.html` | 4–6 | Light and colour |
| Science | Physics | Buoyancy: Basics | `science-simulations/sims/buoyancy-basics.html` | 5–6 | Floating and sinking |
| Science | Physics | Gravity Force Lab: Basics | `science-simulations/sims/gravity-force-lab-basics.html` | 5–6 | Gravity between objects |
| Science | Physics | Geometric Optics: Basics | `science-simulations/sims/geometric-optics-basics.html` | 6 (stretch) | Lenses and mirrors |
| Science | Physics | Masses and Springs: Basics | `science-simulations/sims/masses-and-springs-basics.html` | 6 (stretch) | Springs and stretching |
| Science | Physics | Density | `science-simulations/sims/density.html` | 6 (stretch) | Mass, volume and density |
| Science | Physics | Under Pressure | `science-simulations/sims/under-pressure.html` | 6 (stretch) | Water and air pressure |
| Science | Chemistry | States of Matter: Basics | `science-simulations/sims/states-of-matter-basics.html` | 5–6 | Solids, liquids and gases |
| Science | Chemistry | Reactants, Products and Leftovers | `science-simulations/sims/reactants-products-and-leftovers.html` | 5–6 | Matter is conserved (sandwich “recipes”) |
| Science | Chemistry | pH Scale: Basics | `science-simulations/sims/ph-scale-basics.html` | 6 (stretch) | Acids and bases in everyday liquids |
| Science | Chemistry | Gases Intro | `science-simulations/sims/gases-intro.html` | 6 (stretch) | Gas pressure and temperature |
| Science | Biology | Natural Selection | `science-simulations/sims/natural-selection.html` | 3–6 | Traits, adaptation and survival |
| Science | Biology | Eating, Exercise, and Energy | `science-simulations/sims/eating-exercise-and-energy.html` | 5–6 | Food energy and a healthy body |
| Science | Earth and Space | Gravity and Orbits | `science-simulations/sims/gravity-and-orbits.html` | 5–6 | Sun, Earth and Moon orbits |
| Science | Earth and Space | My Solar System | `science-simulations/sims/my-solar-system.html` | 6 (stretch) | Planet orbits |
| Science | Earth and Space | Greenhouse Effect | `science-simulations/sims/greenhouse-effect.html` | 6 (stretch) | Climate, sunlight and heat |

## 7. Credit and license rules

- The simulations are © PhET Interactive Simulations, University of Colorado Boulder. PhET's build tool marks every
  simulation file **CC BY-NC 4.0**: free to use, share and adapt for **non-commercial** purposes, with credit near
  where it is used. **Commercial use needs a license** from the University of Colorado Boulder:
  https://phet.colorado.edu/en/licensing (contact: phethelp@colorado.edu). Decide for each website whether its use
  is non-commercial (for example: free, no ads, not promoting a business). If unsure, ask PhET.
- Keep the credits that are already in place: the corner credit on the loading screen, "adapted from PhET" in each
  simulation's bottom bar, the About box text, and the Credits section on the catalog pages.
- Do not use the PhET logo, and do not suggest PhET endorses InquiryMind or Amrar Bazar. These are not official
  PhET releases. Do not edit the license comment at the top of each simulation file.
- Source code: GPLv3 (simulations) and MIT (most libraries), from https://github.com/phetsims.

## 8. Common changes

Run these from the repository root. After any change: commit and push, then merge to `main` for amrarbazar.com,
and copy the changed folder(s) to Firebase for inquirymind.org (section 3).

| I want to… | Do this |
|---|---|
| Change a sim's name, grade, topics or group | Edit the lists in `toolkit/catalog.py`, then `python3 offline-simulations/toolkit/catalog.py pages` |
| Remove a sim | Delete its row in `catalog.py`, run the command above, delete `sims/<id>.html` and `thumbnails/<id>.png` in both copies |
| Change catalog page text, colours or header | Edit `SITES` / `CATALOGS` / `TEMPLATE` in `catalog.py`, then run the command above (never edit `index.html` by hand; it is regenerated) |
| Use a better logo | `toolkit/README.md` → "Change the logo" (needs a rebuild) |
| Add another PhET simulation | `toolkit/README.md` → "Add a simulation" |
| Rebuild everything | `toolkit/README.md` → "Rebuild everything" |

**Publish changes** (command line):
```bash
git add -A && git commit -m "Describe the change" && git push
```
Then open a pull request on GitHub and merge it into `main`.

## 9. Troubleshooting

| Problem | Fix |
|---|---|
| Catalog page shows no thumbnails | The page must sit next to its `thumbnails/` folder; copy the whole folder. |
| Math/Science tab gives "not found" | Copy both `simulations/` and `science-simulations/` side by side. |
| Simulation page stays purple / blank | Open the browser console (F12). If a rebuilt sim shows "Class extends value…", it was built with parallel re-compiling; rebuild it with `toolkit/build_sims.sh` (which avoids this). |
| A new upload doesn't show | Hard refresh (Ctrl+Shift+R / Cmd+Shift+R); with the caching headers above, wait or rename. |
| Firebase site stops loading sims late in the day | Free-plan daily bandwidth used up (section 3); move to the Blaze plan. |
| `setup_phet.sh` fails to clone | PhET may have removed its old repos. The built files here are then the only copy; keep backups of this folder. |

## 10. Working with Claude using fewer tokens

- `CLAUDE.md` in the repository root is read automatically at the start of every Claude Code session. It
  tells Claude where everything is, so it doesn't need to explore.
- Name the exact file or command in your request, for example:
  - "In `offline-simulations/toolkit/catalog.py`, change the grade of Friction to 4–6 and regenerate the pages."
  - "Add a link to `/simulations/` in the menu of `index.html`."
  - "Follow `offline-simulations/toolkit/README.md` to add the sim `pendulum-lab` under Physics."
- Ask Claude **not to open** `sims/*.html` files: each is several MB of minified code and burns tokens. Everything
  about a sim (name, grade, topics) is in `catalog.py`.
- A full rebuild takes ~40 minutes of machine time but few tokens if you say "run the toolkit rebuild steps in
  `offline-simulations/toolkit/README.md`".
- Cloud sessions can't open phet.colorado.edu, amrarbazar.com or inquirymind.org unless you add those domains
  to the environment's allowed network domains.
