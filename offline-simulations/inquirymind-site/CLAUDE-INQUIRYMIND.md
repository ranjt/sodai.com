# InquiryMind learning resources (paste into your InquiryMind project as CLAUDE.md)

Simulations, science worksheets (KG–Grade 5), thinking routine organisers and the science practice question bank are
**made in another repository** and are already finished: https://github.com/ranjt/sodai.com, folder
`offline-simulations/inquirymind-site/`.
In this project they live in the hosting folder as `simulations/`, `science-simulations/`, `worksheets/` and
`question-bank/`. First-time setup prompt: `INQUIRYMIND-INTEGRATION-PROMPT.md` in sodai.com.

Rules (save tokens):
- Never recreate, edit or open the generated files in `simulations/`, `science-simulations/`, `worksheets/` or
  `question-bank/` (large PDFs, minified HTML, big JSON). They are replaced as whole folders.
- To update them: download or `git pull` the sodai.com repository, then run
  `bash <sodai.com>/offline-simulations/inquirymind-site/publish.sh <this project folder> --deploy`
  (`--only worksheets` or `--only question-bank` to update one folder). Guide: `PUBLISH-WORKSHEETS.md` in the same folder.
- New worksheet content is written in the sodai.com repository (`worksheets/toolkit/`, see its CLAUDE.md), never here.
- Practice section: questions come from `question-bank/dist/` (format, card mapping and marking rules in
  `question-bank/README.md`). Ids are stable: re-importing updates by id. Read `dist/manifest.json` for counts; inspect
  `dist/all-questions.json` with a script, never whole. New questions are written in sodai.com (`question-bank/questions/`).
- Linking: `/worksheets/` (grade chooser), `/worksheets/kg-science/`, `/worksheets/grade-<N>-science/`,
  `/worksheets/thinking-routines/`, `/simulations/`, `/science-simulations/`, `/question-bank/preview/` (demo of every question). Full PDF list:
  `worksheets/ALL-WORKSHEETS.md` in sodai.com.
- Keep the credits on those pages (Project Zero, OpenMoji, PhET, fonts): they are licence requirements. Practice pages
  that show question pictures need the line "Pictures: OpenMoji (openmoji.org), CC BY-SA 4.0".
