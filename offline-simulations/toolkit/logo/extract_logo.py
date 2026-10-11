"""
How logo-on-dark.png and logo-on-light.png were made from inquirymind-logo-original.png
(the 512x122 logo on a purple background). Kept for reference; it is tuned to that one image.
For a new logo, ask for transparent PNGs (or an SVG) instead and pass them to make_brand.py.

Usage: python3 offline-simulations/toolkit/logo/extract_logo.py   (writes the two PNGs next to this file)
"""
import os
from collections import deque

from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
src = Image.open(os.path.join(HERE, 'inquirymind-logo-original.png')).convert('RGBA')
W, H = src.size
px = src.load()
BG = (61, 37, 196)
ICON_X1 = 126  # icon occupies x 32..123 in the source
def dist(c): return max(abs(c[i] - BG[i]) for i in range(3))
def c2a(c):
    a = 0.0
    for i in range(3):
        if c[i] > BG[i]: a = max(a, (c[i] - BG[i]) / (255 - BG[i]))
        elif c[i] < BG[i]: a = max(a, (BG[i] - c[i]) / BG[i])
    if a < 0.06: return (0, 0, 0, 0)
    a = min(1.0, a)
    return tuple(max(0, min(255, round(BG[i] + (c[i] - BG[i]) / a))) for i in range(3)) + (round(a * 255),)
# icon: flood fill from the border so the purple ring inside the icon stays opaque
inbg = set()
q = deque([(x, y) for x in range(ICON_X1) for y in (0, H-1)] + [(0, y) for y in range(H)] + [(ICON_X1-1, y) for y in range(H)])
while q:
    x, y = q.popleft()
    if not (0 <= x < ICON_X1 and 0 <= y < H) or (x, y) in inbg: continue
    if dist(px[x, y]) > 200: continue
    inbg.add((x, y))
    if dist(px[x, y]) < 60: q.extend([(x+1, y), (x-1, y), (x, y+1), (x, y-1)])
out = Image.new('RGBA', (W, H)); op = out.load()
for x in range(W):
    for y in range(H):
        c = px[x, y][:3]
        if x < ICON_X1 and (x, y) not in inbg: op[x, y] = c + (255,)
        else: op[x, y] = c2a(c)
# remove the decorative dots: left edge dot, and the dot right of "Mind" (top line only)
for x in range(0, 20):
    for y in range(H): op[x, y] = (0, 0, 0, 0)
TOP = 75
cols = [x for x in range(ICON_X1, W) if any(op[x, y][3] > 40 for y in range(TOP))]
runs, s = [], cols[0]
for a, b in zip(cols, cols[1:]):
    if b != a + 1: runs.append((s, a)); s = b
runs.append((s, cols[-1]))
print('top runs', runs[-3:])
dx0, dx1 = runs[-1]
if dx1 - dx0 < 14:
    for x in range(dx0 - 1, W):
        for y in range(TOP): op[x, y] = (0, 0, 0, 0)
for x in range(W - 12, W):
    for y in range(H): op[x, y] = (0, 0, 0, 0)
bb = out.split()[3].point(lambda v: 255 if v > 10 else 0).getbbox()
logo = out.crop(bb); logo.save(os.path.join(HERE, 'logo-on-dark.png')); print('size', logo.size, 'bbox', bb)
# version for white backgrounds: white/lavender text -> brand purple (outside the icon)
lw = logo.copy(); lp = lw.load(); icon_w = ICON_X1 - bb[0]
for x in range(icon_w, lw.size[0]):
    for y in range(lw.size[1]):
        r, g, b, a = lp[x, y]
        if a and min(r, g, b) > 170 and not (r > 200 and g > 150 and b < 140):  # whitish, not yellow
            lp[x, y] = (61, 37, 196, a)
lw.save(os.path.join(HERE, 'logo-on-light.png'))
