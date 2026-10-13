# Prompt for the InquiryMind Claude project

Use this when you give the downloaded `sodai.com` folder to Claude in your InquiryMind website project.

1. On GitHub open https://github.com/ranjt/sodai.com → **Code → Download ZIP**, and unzip it next to your InquiryMind
   project (or `git clone https://github.com/ranjt/sodai.com.git`).
2. Open Claude Code in your InquiryMind project folder (the one with `firebase.json`).
3. Copy everything inside the box below, change the two paths in the first lines if yours are different, and paste it
   as your message.

````text
You are working in my InquiryMind website project (Firebase, inquirymind.org). Next to it is a folder called sodai.com
that holds FINISHED learning resources made in another project:
  - sodai.com folder: ~/Downloads/sodai.com-main        (change if different)
  - this project:      the current folder (has firebase.json)
Your job: put all of these resources on my website, in my existing InquiryMind design, without recreating any of them.

WHAT IS IN THE FOLDER (everything ready to publish is inside sodai.com/offline-simulations/inquirymind-site/)
  simulations/            28 math simulations (PhET, InquiryMind loading screen), catalog page index.html
  science-simulations/    28 science simulations, catalog page index.html, sims/<id>.html, thumbnails/<id>.png
  worksheets/             science worksheets: index.html (grade chooser), kg-science/ and grade-1-science/ …
                          grade-5-science/ (download page, pdf/ study packs + answer keys, downloads/ zips),
                          thinking-routines/ (34 Visible Thinking Routine organisers, PDFs, previews, zip)
  question-bank/          science practice questions KG–Grade 5 (copied there by the build):
                          dist/manifest.json, dist/all-questions.json, dist/kg.json, dist/grade-1.json … grade-5.json,
                          images/ (diagrams + OpenMoji pictures), preview/ (qb-player.js + qb-player.css + demo page),
                          README.md (the question format, practice-card mapping and marking rules: READ THIS FIRST)
  publish.sh              copies these folders into my hosting folder (and deploys with --deploy)
  PUBLISH-WORKSHEETS.md   the publishing guide
  CLAUDE-INQUIRYMIND.md   short rules to add to this project's CLAUDE.md
Indexes you can read instead of opening files: sodai.com/worksheets/ALL-WORKSHEETS.md (every PDF and its path),
question-bank/dist/manifest.json (every grade, topic, count), sodai.com/offline-simulations/README.md (all simulations).

RULES (they save tokens and avoid breaking things)
  - Never open, read, grep or edit sims/*.html (2–8 MB minified each), PDFs or zips. Never rewrite worksheet PDFs,
    simulation files or questions: they are finished. If something is wrong in them, tell me; it is fixed in sodai.com.
  - Do not read dist/all-questions.json whole (it is large). Inspect it with a small script (python/jq/node).
  - Copy folders with publish.sh, not by hand: bash <sodai.com>/offline-simulations/inquirymind-site/publish.sh . 
    (it replaces only simulations/, science-simulations/, worksheets/ and question-bank/ in my hosting folder).
  - Keep every credit line: PhET Interactive Simulations (University of Colorado Boulder, CC BY-NC 4.0), OpenMoji
    (CC BY-SA 4.0) on pages that show its pictures, Project Zero (Harvard) on the thinking routines, the font licences.
    Never use the PhET logo. Worksheets show only InquiryMind branding.
  - Keep my site's look (colours, fonts, header, footer, navigation). Plan first, show me the plan, then build.

STEP 1: LOOK BEFORE CHANGING
  Read this project's CLAUDE.md, firebase.json, and find how the site is built (plain HTML or a framework) and how the
  Practice section works today: where its questions live (JSON files, JS, Firestore…), their fields, how the Science /
  Mathematics tabs, the grade buttons, the five practice cards (Mixed review, Picture quiz, Real-life choices, Simulation
  questions, Olympiad challenge), the strands and skills (L1, E1…), question counts, mastery and teacher
  assignments work. Then read question-bank/README.md. Tell me in a short table how my current format maps to the new one,
  and anything that does not fit.

STEP 2: PUBLISH THE FILES
  Run publish.sh without --deploy (copy only). Add links in my navigation and resource pages:
    /science-simulations/ and /simulations/ (catalogs), /worksheets/ (grade chooser KG–Grade 5),
    /worksheets/kg-science/ … /worksheets/grade-5-science/, /worksheets/thinking-routines/ (VTR).
  If my site has its own pages for simulations, worksheets or routines, link to or embed these pages (an iframe of the
  download page is fine) rather than rebuilding them.

STEP 3: ADD THE QUESTION BANK TO PRACTICE (Science tab)
  - Grades: add a KG button before Grade 1 (grade 0 = KG). Grades 1–5 get the new questions too.
  - Strands and skills: each question has strand (skills → Working scientifically, living → Living things, earth →
    Earth and space, physical → Physical science), site_skill (W1, L1, L2, E1, P1 …), title (skill name), topic (worksheet
    code) and subskill. If my site already has a skill with the same meaning, put the questions under it; otherwise add the
    skill. Never merge two different topics.
  - Practice cards: mode core → Mixed review, picture → Picture quiz, real-life → Real-life choices, simulation →
    Simulation questions, olympiad → Olympiad challenge. Mixed review may also mix all modes of a skill.
  - Keep my existing questions. Add the new ones with their own ids (e.g. g3-c2-013): ids are stable, so assignments
    and progress keep working when the bank is updated. Re-importing must update by id, never duplicate.
  - Storage: prefer loading the static files /question-bank/dist/<grade>.json from hosting (free, fast, no database
    reads). Only if my Practice section must use Firestore, write an idempotent import script (Admin SDK, batches of at
    most 500 writes, upsert by id) and tell me how many reads a practice session will cost.
  - Rendering and marking: the eight types are mcq, multi, truefalse, fill, match, sort, order, short. Use
    question-bank/preview/qb-player.js (+ qb-player.css) directly if my site is plain JS, or port it to my framework
    keeping exactly the marking rules in README.md (fill ignores case/punctuation, match/sort/order give a share score,
    short answers are keyword-marked and always show the model answer for teacher review). Show `explanation` after every
    answer, `hint` on request, a read-aloud button when read_aloud is true (KG, Grade 1), images from
    /question-bank/images/<path> with image_alt as alt text, and for simulation questions the sim.task plus a button to
    /science-simulations/sims/<sim.id>.html (opens in a new tab).
  - Shuffle options for mcq/multi only when no option is a single letter or number (some refer to labels in a diagram);
    always shuffle match (right side), sort items and order steps.
  - Counts and mastery: take question counts from manifest.json; use difficulty (1–3) and subskill for mastery and
    teacher reports. Teacher assignment: let teachers pick grade → skill → card (and difficulty), then assign.
  - Add the OpenMoji credit line on Practice pages: "Pictures: OpenMoji (openmoji.org), CC BY-SA 4.0".

STEP 4: CHECK, THEN PUBLISH
  - firebase serve (or my usual local preview). Check: every grade KG–5 shows its skills and the counts match
    manifest.json; play one question of each type and each card; a KG question reads aloud; pictures load; a simulation
    button opens the simulation; a worksheet PDF and a thinking-routine PDF download; old questions and assignments still
    work; pages work on a phone.
  - Show me what you checked, then deploy only when I say yes:
    bash <sodai.com>/offline-simulations/inquirymind-site/publish.sh . --deploy   (or firebase deploy --only hosting)
  - Add the rules from CLAUDE-INQUIRYMIND.md to this project's CLAUDE.md, plus a short note on where the Practice import
    code lives and how to re-run it.

LATER UPDATES
  When I download a newer sodai.com: run publish.sh again; if the questions changed, re-run the import (it updates by id).
  New content is always made in sodai.com, never in this project.
````

## Short version (for later updates)

```text
I downloaded a newer sodai.com to ~/Downloads/sodai.com-main. Run its offline-simulations/inquirymind-site/publish.sh
into this project (copy only), re-run the question-bank import if dist/manifest.json changed, check the Practice page
counts against the manifest, then show me before deploying. Do not open the sims, PDFs or zips.
```
