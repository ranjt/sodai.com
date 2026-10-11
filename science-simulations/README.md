# Science Simulations K–6

Interactive science simulations for Kindergarten to Grade 6, adapted from
**PhET Interactive Simulations, University of Colorado Boulder**
(https://phet.colorado.edu) and branded for InquiryMind.

## Using this folder

This folder is self-contained and works offline:

- `index.html`: the catalog page, with grade filters, search, and Open and Download buttons
- `sims/<name>.html`: one complete simulation per file (English). Open it in any modern browser,
  even without an internet connection.
- `thumbnails/<name>.png`: preview images used by the catalog

To use it on another website (for example a Firebase Hosting site), copy the whole folder
into that site's public directory. To embed a single simulation in another page, use an iframe:

```html
<iframe src="science-simulations/sims/forces-and-motion-basics.html" width="800" height="525"
        allowfullscreen title="Forces and Motion: Basics"></iframe>
```

## Branding

Each simulation uses a custom `inquirymind` brand (PhET's build tool supports custom brands):

- Loading screen: the InquiryMind logo on purple, with "Adapted from PhET Interactive Simulations,
  University of Colorado Boulder" in the bottom-right corner.
- Bottom-right of the simulation: the InquiryMind logo next to an "adapted from PhET" text credit.
- About box (menu at bottom-right): the full PhET credit, license, and links to InquiryMind and PhET.

## Credits and license

- Simulations © PhET Interactive Simulations, University of Colorado Boulder. PhET's build tool
  marks every simulation file as licensed under
  [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/): **non-commercial use only**,
  with attribution near the point of use. Commercial use needs a license from the University of
  Colorado Boulder (https://phet.colorado.edu/en/licensing). The license header inside each file is
  PhET's original and has not been changed.
- The PhET name and logo are trademarks of the University of Colorado. These files use the PhET name
  only as a text credit, not the PhET logo.
- Built from PhET's open-source code at https://github.com/phetsims (GPLv3 for simulation code,
  MIT for most common libraries).
- These are **not official PhET releases**, and PhET does not endorse this website.
  Official versions: https://phet.colorado.edu

## How these files were built

PhET moved development to a private monorepo on 9 October 2026 and emptied the main branches
of its public GitHub repositories. These builds use each repository's last commit before
that date (development versions, which may differ slightly from PhET's published releases).

```
grunt build --brands=inquirymind --locales=en
```

The exact source commit of every repository used is listed in `BUILD-SOURCES.txt`.
