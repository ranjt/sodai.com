"""
Regenerate the InquiryMind brand images used inside the simulations.

Usage (from the repository root; needs Python 3 + Pillow: pip install pillow):
  python3 offline-simulations/toolkit/make_brand.py
  python3 offline-simulations/toolkit/make_brand.py --dark new-logo-white-text.png --light new-logo-dark-text.png

Inputs (transparent PNGs, wide logo; defaults are in toolkit/logo/):
  --dark   logo for dark backgrounds (light text)  -> loading screen + navbar on black
  --light  logo for light backgrounds (dark text)  -> navbar when a sim uses a white navbar
Outputs in toolkit/brand/inquirymind/images/:
  logo.png, logoOnWhite.png   navbar: logo | "adapted from PhET" text credit (no PhET logo graphic)
  splash.svg                  loading-screen logo
  *_png.ts, splash_svg.ts     the same images as modules the PhET build imports
Then rebuild: setup_phet.sh copies the brand into WORKDIR (or copy brand/inquirymind yourself), then build_sims.sh.

Optional fonts: --font-regular / --font-bold (TTF/OTF). Defaults to Inter, then DejaVu Sans / Arial.
"""
import argparse
import base64
import os

from PIL import Image, ImageDraw, ImageFont

TOOLKIT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(TOOLKIT, 'brand', 'inquirymind', 'images')

REGULAR_FONTS = ['/usr/share/fonts/opentype/inter/Inter-Medium.otf', 'Inter-Medium.otf', 'DejaVuSans.ttf',
                 '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 'arial.ttf', '/Library/Fonts/Arial.ttf']
BOLD_FONTS = ['/usr/share/fonts/opentype/inter/Inter-Bold.otf', 'Inter-Bold.otf', 'DejaVuSans-Bold.ttf',
              '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 'arialbd.ttf', '/Library/Fonts/Arial Bold.ttf']


def load_font(explicit, candidates, size):
    for name in ([explicit] if explicit else []) + candidates:
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            continue
    raise SystemExit('No usable font found; pass --font-regular/--font-bold')


def navbar_logo(logo_file, divider, small_col, big_col, out, f_small, f_big):
    """Logo, a thin divider, then a two-line 'adapted from / PhET' text credit, on a transparent 160px-high canvas."""
    H, lh, gap = 160, 140, 30
    logo = Image.open(logo_file).convert('RGBA')
    logo = logo.resize((round(logo.size[0] * lh / logo.size[1]), lh), Image.LANCZOS)
    t1, t2 = 'adapted from', 'PhET'
    tw = max(f_small.getbbox(t1)[2], f_big.getbbox(t2)[2])
    im = Image.new('RGBA', (logo.size[0] + gap + 3 + gap + tw + 4, H), (0, 0, 0, 0))
    im.alpha_composite(logo, (0, (H - lh) // 2))
    d = ImageDraw.Draw(im)
    x = logo.size[0] + gap
    d.rectangle([x, 28, x + 2, H - 28], fill=divider)
    x += 3 + gap
    b1, b2 = f_small.getbbox(t1), f_big.getbbox(t2)
    h1, h2, spacing = b1[3] - b1[1], b2[3] - b2[1], 12
    top = (H - (h1 + spacing + h2)) // 2
    d.text((x, top - b1[1]), t1, font=f_small, fill=small_col)
    d.text((x, top + h1 + spacing - b2[1]), t2, font=f_big, fill=big_col)
    im.save(out)
    print('wrote', os.path.relpath(out, TOOLKIT), im.size)


def splash_svg(dark_logo, out):
    """273x130 SVG (the size PhET's loading screen expects) with the logo embedded as a PNG."""
    logo = Image.open(dark_logo)
    b64 = base64.b64encode(open(dark_logo, 'rb').read()).decode()
    vw, vh, lw = 273, 130, 253
    lh = lw * logo.size[1] / logo.size[0]
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{vw}px" '
           f'height="{vh}px" viewBox="0 0 {vw} {vh}"><image x="{(vw - lw) / 2:.1f}" y="{(vh - lh) / 2 + 8:.1f}" '
           f'width="{lw}" height="{lh:.1f}" href="data:image/png;base64,{b64}" xlink:href="data:image/png;base64,{b64}"/></svg>')
    open(out, 'w').write(svg)
    print('wrote', os.path.relpath(out, TOOLKIT))


def image_module(path, mime):
    """Same format as PhET's generated *_png.ts / *_svg.ts image modules."""
    b64 = base64.b64encode(open(path, 'rb').read()).decode()
    module = ("/* eslint-disable */\n/* @formatter:off */\n\n"
              "import asyncLoader from '../../../phet-core/js/asyncLoader.js';\n\n"
              "const image = new Image();\nconst unlock = asyncLoader.createLock( image );\nimage.onload = unlock;\n"
              f"image.src = 'data:{mime};base64,{b64}';\nexport default image;")
    base, ext = os.path.splitext(path)
    with open(f'{base}_{ext[1:]}.ts', 'w') as f:
        f.write(module)


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--dark', default=os.path.join(TOOLKIT, 'logo', 'logo-on-dark.png'))
    ap.add_argument('--light', default=os.path.join(TOOLKIT, 'logo', 'logo-on-light.png'))
    ap.add_argument('--font-regular')
    ap.add_argument('--font-bold')
    a = ap.parse_args()
    os.makedirs(OUT, exist_ok=True)
    small, big = load_font(a.font_regular, REGULAR_FONTS, 33), load_font(a.font_bold, BOLD_FONTS, 62)
    navbar_logo(a.dark, (120, 120, 130, 255), (190, 190, 200, 255), (255, 255, 255, 255), f'{OUT}/logo.png', small, big)
    navbar_logo(a.light, (170, 170, 180, 255), (90, 90, 100, 255), (40, 40, 48, 255), f'{OUT}/logoOnWhite.png', small, big)
    splash_svg(a.dark, f'{OUT}/splash.svg')
    image_module(f'{OUT}/logo.png', 'image/png')
    image_module(f'{OUT}/logoOnWhite.png', 'image/png')
    image_module(f'{OUT}/splash.svg', 'image/svg+xml')
    print('Brand images updated. Rebuild the simulations to use them (see toolkit/README.md).')
