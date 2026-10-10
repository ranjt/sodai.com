# Math Simulations K–6

Interactive math simulations for Kindergarten to Grade 6, adapted from
**PhET Interactive Simulations, University of Colorado Boulder**
(https://phet.colorado.edu).

## Using this folder

This folder is self-contained and works offline:

- `index.html`: the catalog page, grouped by grade, with Open and Download buttons
- `sims/<name>.html`: one complete simulation per file (English). Open it in any modern browser,
  even without an internet connection.
- `thumbnails/<name>.png`: preview images used by the catalog

To use it on another website (for example a Firebase Hosting site), copy the whole
`simulations/` folder into that site's public directory. To embed a single simulation
in another page, use an iframe:

```html
<iframe src="simulations/sims/make-a-ten.html" width="800" height="525"
        allowfullscreen title="Make a Ten"></iframe>
```

## Credits and license

- Simulations © PhET Interactive Simulations, University of Colorado Boulder, licensed under
  [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Keep this attribution wherever you use them.
- Built from PhET's open-source code at https://github.com/phetsims (GPLv3 for simulation code,
  MIT for most common libraries) using PhET's own build tool (chipper) with the
  `adapted-from-phet` brand.
- These are **not official PhET releases**, and PhET does not endorse this website. Don't use the
  PhET name or logo in a way that suggests otherwise. Official versions: https://phet.colorado.edu

## How these files were built

PhET moved development to a private monorepo on 9 October 2026 and emptied the main branches
of its public GitHub repositories. These builds use each repository's last commit before
that date (development versions, which may differ slightly from PhET's published releases).

```
grunt build --brands=adapted-from-phet --locales=en
```

The exact source commit of every repository used is listed in `BUILD-SOURCES.txt`.
