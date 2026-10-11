# InquiryMind learning resources (paste into your InquiryMind project as CLAUDE.md)

Simulations, science worksheets (KG–Grade 5) and thinking routine organisers are **made in another repository** and
are already finished: https://github.com/ranjt/sodai.com, folder `offline-simulations/inquirymind-site/`.
In this project they live in the hosting folder as `simulations/`, `science-simulations/` and `worksheets/`.

Rules (save tokens):
- Never recreate, edit or open the generated files in `simulations/`, `science-simulations/` or `worksheets/`
  (large PDFs and minified HTML). They are replaced as whole folders.
- To update them: download or `git pull` the sodai.com repository, then run
  `bash <sodai.com>/offline-simulations/inquirymind-site/publish.sh <this project folder> --deploy`
  (`--only worksheets` to update only the worksheets). Guide: `PUBLISH-WORKSHEETS.md` in the same folder.
- New worksheet content is written in the sodai.com repository (`worksheets/toolkit/`, see its CLAUDE.md), never here.
- Linking: `/worksheets/` (grade chooser), `/worksheets/kg-science/`, `/worksheets/grade-<N>-science/`,
  `/worksheets/thinking-routines/`, `/simulations/`, `/science-simulations/`. Full PDF list:
  `worksheets/ALL-WORKSHEETS.md` in sodai.com.
- Keep the credits on those pages (Project Zero, OpenMoji, PhET, fonts): they are licence requirements.
