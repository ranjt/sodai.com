"""Grade 4 illustrations: SVG line art plus OpenMoji pictures (art.pic). Shared primitives come from art.py."""
import math

from art import (INK, GREY, LIGHT, svg, text, line, path, circle, ellipse, rect, arrow, curved_arrow, marker, callout,
                 pic, sun_icon, cloud)


def wrap(s, n):
    """Split a label into lines of at most about n characters."""
    words, lines, cur = s.split(), [], ''
    for wd in words:
        if cur and len(cur) + 1 + len(wd) > n:
            lines.append(cur)
            cur = wd
        else:
            cur = f'{cur} {wd}'.strip()
    return lines + [cur] if cur else lines


def mtext(x, y, s, size=11, n=18, anchor='middle', weight='normal', italic=False, lh=1.2):
    """Multi-line text centred on (x, y) as the first baseline."""
    return ''.join(text(x, y + i * size * lh, ln, size, anchor, weight, italic) for i, ln in enumerate(wrap(s, n)))


# ------------------------------------------------------------------ living things
def key_tree(tree, leaf_w=96, level_h=78, pic_size=40, w='100%', show_labels=True):
    """Dichotomous (branching) key. tree = ('question?', yes_branch, no_branch); a leaf = (openmoji name, label)."""
    leaves, boxes, links = [], [], []

    def depth(n):
        return 0 if len(n) == 2 else 1 + max(depth(n[1]), depth(n[2]))

    d_max = depth(tree)

    def lay(n, d):
        if len(n) == 2:
            x = len(leaves) * leaf_w + leaf_w / 2
            leaves.append((x, n))
            return x, d_max * level_h + 10
        xl, yl = lay(n[1], d + 1)
        xr, yr = lay(n[2], d + 1)
        x, y = (xl + xr) / 2, d * level_h + 10
        boxes.append((x, y, n[0]))
        links.append((x, y + 38, xl, yl, 'yes'))
        links.append((x, y + 38, xr, yr, 'no'))
        return x, y

    lay(tree, 0)
    W = len(leaves) * leaf_w
    o = ''
    for x1, y1, x2, y2, lab in links:
        o += path(f'M{x1},{y1} L{x1},{y1 + 10} L{x2},{y1 + 10} L{x2},{y2}', w=1.3)
        o += text((x1 + x2) / 2, y1 + 6, lab, 9.5, italic=True)
    for x, y, q in boxes:
        bw = min(170, leaf_w * 1.8)
        o += rect(x - bw / 2, y, bw, 38, 7, 'white', 1.5) + mtext(x, y + 15, q, 10, int(bw / 6.2))
    for x, (name, label) in leaves:
        y = d_max * level_h + 10
        o += pic(name, x - pic_size / 2, y, pic_size)
        if show_labels:
            o += text(x, y + pic_size + 13, label, 10.5, weight='bold')
        else:
            o += line(x - 34, y + pic_size + 15, x + 34, y + pic_size + 15, 1, '2 2')
    return svg(W, d_max * level_h + 10 + pic_size + 22, o, width=w)


def _stage(kind, x, y, s):
    """Small drawings for life-cycle stages that have no OpenMoji picture. (x, y) is the centre."""
    if kind == 'frogspawn':
        o = ''
        for dx, dy in ((-12, -6), (0, -10), (12, -5), (-6, 6), (8, 8), (-16, 6), (18, 6)):
            o += circle(x + dx * s, y + dy * s, 7 * s, 'white', 1.1) + circle(x + dx * s, y + dy * s, 2.2 * s, INK, 0)
        return o
    if kind == 'tadpole':
        return (ellipse(x - 8 * s, y, 10 * s, 7 * s, GREY, 1.3)
                + path(f'M{x + 1 * s},{y} q{8 * s},{-8 * s} {14 * s},0 t{14 * s},0', w=1.6))
    if kind == 'froglet':
        return pic('frog', x - 18 * s, y - 18 * s, 36 * s) + path(f'M{x + 10 * s},{y + 14 * s} q{8 * s},{4 * s} {16 * s},0', w=1.5)
    if kind == 'chrysalis':
        return (line(x, y - 24 * s, x, y - 16 * s, 1.4) + path(
            f'M{x},{y - 16 * s} C{x + 12 * s},{y - 8 * s} {x + 10 * s},{y + 14 * s} {x},{y + 22 * s} '
            f'C{x - 10 * s},{y + 14 * s} {x - 12 * s},{y - 8 * s} {x},{y - 16 * s} Z', LIGHT, 1.4)
            + line(x - 8 * s, y, x + 8 * s, y, 0.9) + line(x - 7 * s, y + 8 * s, x + 7 * s, y + 8 * s, 0.9))
    if kind == 'butterfly eggs':
        return ''.join(ellipse(x + dx * s, y + dy * s, 3.4 * s, 4.6 * s, 'white', 1.1) for dx, dy in ((-8, 0), (0, -4), (8, 1), (-3, 7), (5, 8)))
    if kind == 'leaf':
        return path(f'M{x - 22 * s},{y + 8 * s} C{x - 10 * s},{y - 22 * s} {x + 18 * s},{y - 18 * s} {x + 24 * s},{y - 10 * s} '
                    f'C{x + 12 * s},{y + 14 * s} {x - 8 * s},{y + 16 * s} {x - 22 * s},{y + 8 * s} Z', 'white', 1.3)
    raise ValueError(kind)


def cycle(stages, labels=True, r=96, size=46, w='100%', numbered=False):
    """A life cycle: stages = [(openmoji name or 'draw:kind', label), ...] placed round a circle, with arrows."""
    n = len(stages)
    cx, cy = r + 70, r + 40
    o = ''
    pts = []
    for i in range(n):
        a = -math.pi / 2 + 2 * math.pi * i / n
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    for i, ((name, lab), (x, y)) in enumerate(zip(stages, pts)):
        if name.startswith('draw:'):
            o += _stage(name[5:], x, y, size / 46)
        else:
            o += pic(name, x - size / 2, y - size / 2, size)
        if numbered:
            o += marker(i + 1, x - size / 2 - 4, y - size / 2)
        if labels:
            o += mtext(x, y + size / 2 + 12, lab, 10.5, 16, weight='bold')
        a1 = -math.pi / 2 + 2 * math.pi * (i + 0.32) / n
        a2 = -math.pi / 2 + 2 * math.pi * (i + 0.68) / n
        am = (a1 + a2) / 2
        o += curved_arrow(cx + r * math.cos(a1), cy + r * math.sin(a1), cx + (r + 18) * math.cos(am), cy + (r + 18) * math.sin(am),
                          cx + r * math.cos(a2), cy + r * math.sin(a2), 1.4, 7)
    return svg(2 * r + 140, 2 * r + 110, o, width=w)


FROG_CYCLE = [('draw:frogspawn', 'eggs (frogspawn)'), ('draw:tadpole', 'tadpole'), ('draw:froglet', 'froglet'), ('frog', 'adult frog')]
BUTTERFLY_CYCLE = [('draw:butterfly eggs', 'eggs on a leaf'), ('caterpillar', 'caterpillar (larva)'), ('draw:chrysalis', 'chrysalis (pupa)'),
                   ('butterfly', 'adult butterfly')]
CHICKEN_CYCLE = [('egg', 'egg'), ('hatching chick', 'hatching'), ('baby chick', 'chick'), ('chicken', 'adult hen')]
PLANT_CYCLE = [('draw:leaf', 'seed'), ('seedling', 'seedling'), ('potted plant', 'young plant'), ('sunflower', 'flowering plant')]


def food_chain(items, size=50, gap=46, w='100%', labels=True, roles=None):
    """items = [(openmoji name, label), ...]; arrows point from the food to the eater."""
    o = ''
    for i, (name, lab) in enumerate(items):
        x = i * (size + gap)
        o += pic(name, x, 0, size)
        if labels:
            o += text(x + size / 2, size + 14, lab, 11, weight='bold')
        if roles:
            o += text(x + size / 2, size + 28, roles[i], 9.5, italic=True)
        if i < len(items) - 1:
            o += arrow(x + size + 6, size / 2, x + size + gap - 6, size / 2, 1.8, 8)
    W = len(items) * (size + gap) - gap
    return svg(W + 90, size + (32 if roles else 20), f'<g transform="translate(45 0)">{o}</g>', width=w)


SUNDARBANS_WEB = {
    # name: (openmoji, x, y, label)
    'leaves': ('herb', 40, 250, 'mangrove leaves'),
    'algae': ('draw:algae', 300, 262, 'algae in water'),
    'deer': ('deer', 20, 140, 'spotted deer'),
    'monkey': ('monkey', 120, 140, 'monkey'),
    'crab': ('crab', 215, 150, 'crab'),
    'fish': ('fish', 320, 150, 'fish'),
    'tiger': ('tiger', 40, 20, 'tiger'),
    'kingfisher': ('bird', 230, 20, 'kingfisher'),
    'crocodile': ('crocodile', 360, 30, 'crocodile'),
}
SUNDARBANS_LINKS = [('leaves', 'deer'), ('leaves', 'monkey'), ('leaves', 'crab'), ('algae', 'crab'), ('algae', 'fish'),
                    ('deer', 'tiger'), ('monkey', 'tiger'), ('crab', 'kingfisher'), ('fish', 'kingfisher'), ('fish', 'crocodile'),
                    ('deer', 'crocodile')]


def food_web_pics(numbered=False, w='100%'):
    o = ''
    s = 46
    centre = {}
    for k, (name, x, y, lab) in SUNDARBANS_WEB.items():
        centre[k] = (x + s / 2, y + s / 2)
    for a, b in SUNDARBANS_LINKS:
        (x1, y1), (x2, y2) = centre[a], centre[b]
        d = math.hypot(x2 - x1, y2 - y1)
        o += arrow(x1 + (x2 - x1) * 30 / d, y1 + (y2 - y1) * 30 / d, x2 - (x2 - x1) * 30 / d, y2 - (y2 - y1) * 30 / d, 1.2, 7)
    for i, (k, (name, x, y, lab)) in enumerate(SUNDARBANS_WEB.items()):
        if name == 'draw:algae':
            o += ''.join(circle(x + 8 + (j % 5) * 8, y + 10 + (j // 5) * 8, 3, 'white', 1) for j in range(15))
        else:
            o += rect(x - 3, y - 3, s + 6, s + 6, 8, 'white', 0) + pic(name, x, y, s)
        if numbered:
            o += marker(i + 1, x - 6, y)
        else:
            o += rect(x + s / 2 - len(lab) * 2.9 - 3, y + s + 2, len(lab) * 5.8 + 6, 13, 3, 'white', 0)
            o += text(x + s / 2, y + s + 12, lab, 10, weight='bold')
    return svg(430, 320, o, width=w)


def pond_ecosystem(labels=None, w='100%'):
    """A pond with living and non-living parts, numbered 1-8 (labels=list to name them)."""
    o = rect(0, 0, 480, 300, 10, 'white', 1.4)
    o += path('M0,150 C80,140 160,158 240,150 C320,142 400,158 480,150 L480,290 Q480,300 470,300 L10,300 Q0,300 0,290 Z', LIGHT, 1.4)
    o += path('M0,262 C100,250 200,272 300,258 C380,248 440,266 480,256 L480,290 Q480,300 470,300 L10,300 Q0,300 0,290 Z', GREY, 1.2)
    for k in range(6):
        o += path(f'M{30 + k * 80},{185 + (k % 2) * 30} q10,-5 20,0 t20,0', w=1)
    o += sun_icon(420, 46, 18) + cloud(90, 40, 0.9)
    o += pic('duck', 260, 112, 46) + pic('fish', 120, 196, 44) + pic('frog', 330, 84, 44) + pic('lotus', 360, 116, 44)
    o += pic('herb', 30, 96, 52) + pic('rock', 380, 238, 40) + pic('snail', 210, 240, 30)
    parts = [(420, 46, 450, 96), (100, 40, 160, 16), (283, 135, 250, 90), (142, 218, 100, 180), (215, 205, 180, 175),
             (400, 258, 440, 230), (60, 122, 90, 80), (370, 112, 330, 60)]
    for i, (px, py, tx, ty) in enumerate(parts):
        o += callout(i + 1, tx, ty, px, py, labels)
    return svg(600, 300, f'<g transform="translate(40 0)">{o}</g>', width=w)


POND_PARTS = ['Sun (light and heat)', 'air and clouds', 'duck', 'fish', 'water', 'rock', 'water plants', 'frog']


def levels_big(w='100%'):
    """Organism -> population -> community -> ecosystem -> biosphere, with pictures."""
    o = ''
    cells = [('organism', [('deer', 22, 30, 50)]),
             ('population', [('deer', 2, 24, 38), ('deer', 40, 18, 38), ('deer', 22, 52, 38)]),
             ('community', [('deer', 2, 46, 34), ('tiger', 40, 50, 36), ('deciduous tree', 20, 4, 40), ('bird', 56, 10, 26)]),
             ('ecosystem', [('deer', 4, 52, 30), ('deciduous tree', 22, 8, 38), ('rock', 52, 60, 22), ('droplet', 60, 30, 20), ('sun', 4, 4, 22)]),
             ('biosphere', [('globe asia', 10, 18, 70)])]
    for i, (lab, items) in enumerate(cells):
        x0 = i * 118
        o += rect(x0, 0, 94, 100, 10, 'white', 1.4)
        for name, x, y, s in items:
            o += pic(name, x0 + x, y, s)
        o += text(x0 + 47, 120, lab, 12, weight='bold')
        if i < len(cells) - 1:
            o += arrow(x0 + 97, 50, x0 + 115, 50, 1.6, 7)
    return svg(5 * 118 - 24, 128, o, width=w)


def mangrove(labels=True, w='100%'):
    o = rect(0, 150, 360, 70, 0, LIGHT, 0) + path('M0,150 q30,-6 60,0 t60,0 t60,0 t60,0 t60,0 t60,0', w=1.2)
    o += path('M0,200 C90,192 180,206 270,198 C320,194 340,200 360,198 L360,220 L0,220 Z', GREY, 1.2)
    o += path('M170,40 C120,20 90,60 120,80 C80,90 110,130 160,118 C190,135 240,128 236,100 C280,96 270,50 230,52 C220,24 190,24 170,40 Z', 'white', 1.6)
    o += path('M176,118 L172,150', w=7) + path('M176,118 L172,150', w=4).replace(INK, 'white', 1)
    for sx, ex in ((172, 110), (174, 140), (176, 210), (178, 240)):
        o += path(f'M{sx},{150} Q{(sx + ex) / 2},{120} {ex},{200}', w=2.2)
    for x in (40, 62, 84, 262, 284, 306, 328):
        o += line(x, 200, x, 168, 2.6)
    if labels:
        o += text(60, 160 - 40, 'breathing roots', 11, weight='bold') + line(62, 126, 62, 166, 0.9)
        o += text(250, 140 - 6, 'prop roots', 11, weight='bold') + line(226, 140, 236, 168, 0.9)
        o += text(300, 214, 'salty mud', 10, italic=True) + text(40, 186, 'salty water', 10, italic=True)
    return svg(360, 222, o, width=w)


def water_hyacinth(labels=True, w='100%'):
    o = rect(0, 110, 300, 110, 0, LIGHT, 0) + path('M0,110 q25,-5 50,0 t50,0 t50,0 t50,0 t50,0 t50,0', w=1.2)
    for dx in (-40, -14, 14, 40):
        o += ellipse(150 + dx, 102, 11, 15, GREY, 1.3)
        o += path(f'M{150 + dx},{88} C{150 + dx * 1.6},{60} {150 + dx * 2.2},{50} {150 + dx * 2.4},{40} '
                  f'C{150 + dx * 2.8},{40} {150 + dx * 2.6},{70} {150 + dx},{88}', 'white', 1.3)
    o += line(150, 92, 150, 22, 1.6)
    for k in range(4):
        o += ellipse(150 + (k % 2) * 12 - 6, 26 + k * 12, 8, 6, 'white', 1.2)
    for dx in range(-30, 34, 8):
        o += path(f'M{150 + dx},{116} q{4},{30} {-2},{70}', w=0.9)
    if labels:
        o += text(255, 98, 'spongy stalks', 11, weight='bold') + text(255, 112, 'full of air', 10, italic=True) + line(200, 100, 214, 100, 0.9)
        o += text(70, 170, 'roots hang', 11, weight='bold') + text(70, 184, 'in the water', 10, italic=True)
        o += text(215, 30, 'flowers', 11, weight='bold') + line(160, 34, 192, 30, 0.9)
    return svg(300, 222, o, width=w)


def fern_moss(w='100%'):
    """A fern and a moss: plants that make spores, not flowers."""
    o = ''
    for k, a in enumerate((-60, -30, 0, 30, 60)):
        t = math.radians(a - 90)
        ex, ey = 90 + 80 * math.cos(t), 150 + 100 * math.sin(t)
        o += path(f'M90,150 Q{90 + 30 * math.cos(t)},{150 + 60 * math.sin(t)} {ex},{ey}', w=1.6)
        for j in range(1, 7):
            f = j / 7
            px, py = 90 + (ex - 90) * f, 150 + (ey - 150) * f
            o += line(px, py, px - 10 * math.sin(t) * (1 - f) - 6, py + 4, 1) + line(px, py, px + 10 * (1 - f) + 6, py + 4 * math.cos(t), 1)
    for j in range(0, 6):
        o += ellipse(84 + j * 3, 162, 3, 2, INK, 0)
    o += text(90, 182, 'fern', 12, weight='bold') + text(90, 197, 'spores under the leaves', 9.5, italic=True)
    o += path('M200,160 C210,130 260,128 280,160 Z', LIGHT, 1.3)
    for x in range(210, 276, 7):
        o += line(x, 160, x + 2, 140 + (x % 3) * 3, 1) + line(x + 2, 140 + (x % 3) * 3, x + 2, 120 + (x % 5) * 2, 0.8) + ellipse(x + 2, 118 + (x % 5) * 2, 2, 3, INK, 0)
    o += text(240, 182, 'moss', 12, weight='bold') + text(240, 197, 'spore capsules on stalks', 9.5, italic=True)
    return svg(320, 202, o, width=w)


def habitats_strip(w='100%'):
    """Where animals live: aerial, arboreal, aquatic, terrestrial, fossorial."""
    o = ''
    cells = [('aerial', 'in the air', [('eagle', 26, 14, 54)], None),
             ('arboreal', 'in trees', [('deciduous tree', 8, 6, 84), ('monkey', 44, 30, 36)], None),
             ('aquatic', 'in water', [('dolphin', 18, 34, 46), ('fish', 54, 70, 26)], 'water'),
             ('terrestrial', 'on land', [('tiger', 14, 34, 64)], 'ground'),
             ('fossorial', 'under the ground', [('worm', 30, 58, 40)], 'soil')]
    for i, (name, sub, items, base) in enumerate(cells):
        x0 = i * 116
        o += rect(x0, 0, 106, 110, 10, 'white', 1.4)
        if base == 'water':
            o += rect(x0 + 1, 30, 104, 79, 0, LIGHT, 0) + path(f'M{x0 + 1},30 q13,-5 26,0 t26,0 t26,0 t26,0', w=1)
        if base == 'ground':
            o += line(x0 + 4, 96, x0 + 102, 96, 1.4)
        if base == 'soil':
            o += rect(x0 + 1, 40, 104, 69, 0, GREY, 0) + line(x0 + 1, 40, x0 + 105, 40, 1.4) + pic('herb', x0 + 40, 6, 32)
        for nm, x, y, s in items:
            o += pic(nm, x0 + x, y, s)
        o += text(x0 + 53, 128, name, 12, weight='bold') + text(x0 + 53, 142, sub, 10, italic=True)
    return svg(5 * 116 - 10, 148, o, width=w)


def migration_map(w='100%'):
    """Simple map: ducks fly from cold northern lakes to Bangladesh wetlands for the winter."""
    o = rect(0, 0, 440, 230, 10, 'white', 1.4)
    o += path('M20,40 C120,20 260,30 420,50', w=1, dash='4 4') + text(330, 34, 'cold north (Siberia, Mongolia)', 10, italic=True)
    o += path('M260,170 C280,160 300,165 320,175 C330,190 310,205 290,200 C270,198 255,185 260,170 Z', GREY, 1.4)
    o += text(292, 222, 'Bangladesh: haors and beels', 10.5, weight='bold')
    o += pic('snowflake', 60, 50, 30) + pic('snowflake', 120, 60, 24) + pic('duck', 150, 50, 44)
    o += curved_arrow(190, 80, 300, 70, 288, 162, 2, 10) + text(316, 112, 'autumn: fly south', 10.5, 'start', italic=True)
    o += curved_arrow(250, 176, 150, 170, 120, 100, 1.4, 8, '5 4') + text(70, 176, 'spring: fly back to breed', 10.5, italic=True)
    o += pic('duck', 266, 160, 30)
    return svg(440, 232, o, width=w)


# ------------------------------------------------------------------ Earth and space
WEATHER_INSTRUMENTS = ['thermometer', 'rain gauge', 'wind vane', 'anemometer', 'barometer']
WEATHER_MEASURES = ['temperature (°C)', 'rainfall (mm)', 'wind direction', 'wind speed', 'air pressure']


def weather_instruments(names=True, w='100%'):
    from art import thermometer
    o = thermometer(50, 14, 31, 0, 50, 120, 10)
    # rain gauge: funnel on a measuring jar
    o += path('M140,30 L190,30 L172,52 L158,52 Z', 'white', 1.5) + rect(150, 52, 30, 84, 3, 'white', 1.5) + rect(152, 104, 26, 30, 0, LIGHT, 0)
    for k in range(6):
        o += line(150, 60 + k * 14, 158, 60 + k * 14, 0.9)
    # wind vane
    o += line(260, 136, 260, 48, 2) + path('M226,40 L280,40 L292,32 L292,48 L280,40', 'white', 1.5) + path('M226,40 L234,32 M226,40 L234,48', w=1.5)
    for t, dx, dy in (('N', 0, -30), ('S', 0, 30), ('E', 30, 0), ('W', -30, 0)):
        o += text(260 + dx, 82 + dy + 4, t, 11, weight='bold')
    o += line(238, 82, 282, 82, 1) + line(260, 60, 260, 104, 1)
    # anemometer: three cups on arms
    o += line(370, 136, 370, 58, 2)
    for a in (-90, 30, 150):
        t = math.radians(a)
        ex, ey = 370 + 36 * math.cos(t), 54 + 14 * math.sin(t)
        o += line(370, 54, ex, ey, 1.6) + path(f'M{ex - 8},{ey - 6} A8,8 0 0 0 {ex + 8},{ey - 6} Z', 'white', 1.4)
    # barometer dial
    o += circle(480, 76, 44, 'white', 1.8) + circle(480, 76, 3, INK, 0)
    for k in range(9):
        t = math.radians(150 + k * 30)
        o += line(480 + 34 * math.cos(t), 76 + 34 * math.sin(t), 480 + 41 * math.cos(t), 76 + 41 * math.sin(t), 1.1)
    o += text(452, 104, 'low', 8.5) + text(508, 104, 'high', 8.5) + text(480, 52, 'change', 8.5)
    o += line(480, 76, 500, 52, 2)
    labels = WEATHER_INSTRUMENTS if names else list('ABCDE')
    for i, x in enumerate((50, 165, 260, 370, 480)):
        o += text(x, 178, labels[i], 12, weight='bold')
    return svg(540, 196, f'<g transform="translate(0 12)">{o}</g>', width=w)


CLOUD_TYPES = [('cumulus', 'puffy heaps: fine weather'), ('stratus', 'flat grey sheet: dull, drizzle'),
               ('cirrus', 'high thin wisps: weather may change'), ('cumulonimbus', 'tall storm tower: heavy rain, thunder')]


def cloud_types(names=True, w='100%'):
    o = ''
    for i in range(4):
        x0 = i * 150
        o += rect(x0, 0, 140, 130, 10, 'white', 1.3)
    o += cloud(44, 58, 0.62) + cloud(84, 80, 0.45)
    o += path('M162,70 C200,58 250,62 282,70 L282,86 L162,86 Z', GREY, 1.3)
    for k in range(4):
        o += path(f'M{310 + k * 12},{30 + k * 9} q30,-10 70,4', w=1.3)
    o += path('M480,110 L486,60 C470,56 466,36 490,30 C478,14 520,6 532,22 C560,14 584,22 580,30 L520,32 C540,40 536,58 528,62 L532,110 Z', LIGHT, 1.4)
    for k in range(5):
        o += line(488 + k * 9, 112, 484 + k * 9, 124, 1)
    o += path('M506,64 L498,84 L508,84 L500,104', w=1.6)
    for i, (n, d) in enumerate(CLOUD_TYPES):
        x = i * 150 + 70
        o += text(x, 148, n if names else chr(65 + i), 12, weight='bold')
        if names:
            o += mtext(x, 162, d, 9.5, 24, italic=True)
    return svg(590, 186 if names else 156, o, width=w)


def sea_breeze(w='100%'):
    """Daytime sea breeze: warm land heats the air, which rises; cooler air from the sea moves in."""
    o = sun_icon(60, 34, 16)
    o += path('M0,170 L230,170 C240,168 250,172 260,170 L460,170 L460,200 L0,200 Z', LIGHT, 1.3)
    o += path('M230,170 L230,200', w=1.2) + rect(230, 160, 230, 40, 0, GREY, 1.3)
    o += text(110, 192, 'sea (cooler)', 11, weight='bold') + text(345, 190, 'land (warmer)', 11, weight='bold')
    o += arrow(340, 150, 340, 70, 2, 9) + text(352, 110, 'warm air rises', 10, 'start', italic=True)
    o += arrow(330, 56, 140, 56, 1.6, 8, '5 4')
    o += arrow(120, 70, 120, 140, 1.6, 8, '5 4') + text(108, 106, 'cool air sinks', 10, 'end', italic=True)
    o += arrow(140, 152, 320, 152, 2.2, 10) + text(230, 144, 'sea breeze', 11, weight='bold')
    return svg(460, 204, o, width=w)


CYCLONE_PARTS = ['eye: calm, clear sky', 'eye wall: strongest winds and rain', 'rain bands', 'winds spin anticlockwise']


def cyclone_diagram(labels=None, w='100%'):
    o = ''
    cx, cy = 170, 130
    for k in range(4):
        r0 = 30 + k * 22
        o += path(f'M{cx + r0},{cy} A{r0},{r0 * 0.92} 0 0 0 {cx - r0 * 0.8},{cy - r0 * 0.6} '
                  f'Q{cx - r0 * 1.4},{cy + r0 * 0.4} {cx - r0 * 0.4},{cy + r0 * 1.1}', w=4 - k * 0.6)
        o += path(f'M{cx - r0},{cy} A{r0},{r0 * 0.92} 0 0 0 {cx + r0 * 0.8},{cy + r0 * 0.6} '
                  f'Q{cx + r0 * 1.4},{cy - r0 * 0.4} {cx + r0 * 0.4},{cy - r0 * 1.1}', w=4 - k * 0.6)
    o += circle(cx, cy, 13, 'white', 1.6)
    o += curved_arrow(cx + 110, cy - 40, cx + 70, cy - 120, cx - 10, cy - 116, 1.8, 9)
    parts = [(cx, cy, 330, 130), (cx + 22, cy - 10, 330, 80), (cx + 70, cy + 64, 330, 200), (cx + 60, cy - 100, 330, 30)]
    for i, (px, py, tx, ty) in enumerate(parts):
        o += callout(i + 1, tx, ty, px, py, labels)
    return svg(560, 250, o, width=w)


COAST = [(78, 10), (79.8, 10.3), (80.3, 13.1), (82.2, 16.6), (83.3, 17.7), (85.5, 19.6), (86.8, 20.6), (87.5, 21.5), (88.5, 21.6),
         (89.5, 21.9), (90.5, 22.1), (91.5, 22.5), (91.9, 21.5), (92.3, 20.8), (92.6, 20.5), (93.5, 19), (94.3, 17.5), (94.5, 16),
         (96, 15.5), (96, 25), (78, 25)]
SIDR_TRACK = [('11 Nov', 11.5, 92.0), ('12 Nov', 13.0, 90.0), ('13 Nov', 15.0, 89.5), ('14 Nov', 17.5, 89.3), ('15 Nov', 21.0, 89.6),
              ('16 Nov', 24.0, 90.8)]


def cyclone_map(track=None, plotted=False, w='100%'):
    """Bay of Bengal grid map (latitude 10-25 N, longitude 78-96 E) for plotting a cyclone's track."""
    X = lambda lon: 50 + (lon - 78) * 26  # noqa: E731
    Y = lambda lat: 12 + (25 - lat) * 26  # noqa: E731
    o = rect(X(78), Y(25), X(96) - X(78), Y(10) - Y(25), 0, 'white', 1.4)
    o += path('M' + ' L'.join(f'{X(a):.0f},{Y(b):.0f}' for a, b in COAST) + ' Z', GREY, 1.4)
    for lat in range(10, 26):
        o += line(X(78), Y(lat), X(96), Y(lat), 0.6 if lat % 5 else 0.9, None if lat % 5 == 0 else '2 3')
        if lat % 5 == 0 or lat in (12, 18, 22):
            o += text(X(78) - 6, Y(lat) + 4, f'{lat}°N', 9, 'end')
    for lon in range(78, 97):
        o += line(X(lon), Y(25), X(lon), Y(10), 0.6 if lon % 2 else 0.9, None if lon % 2 == 0 else '2 3')
        if lon % 2 == 0:
            o += text(X(lon), Y(10) + 14, f'{lon}°E', 9)
    o += text(X(91.4), Y(24.4), 'BANGLADESH', 10, 'start', weight='bold') + text(X(82), Y(21.5), 'INDIA', 11, weight='bold')
    o += text(X(95), Y(21), 'MYANMAR', 9, weight='bold') + text(X(86.5), Y(14), 'Bay of Bengal', 13, italic=True)
    o += circle(X(90.4), Y(23.8), 3, INK, 0) + text(X(90.4) - 6, Y(23.8) + 3, 'Dhaka', 8.5, 'end')
    if plotted and track:
        pts = [(X(lon), Y(lat)) for _, lat, lon in track]
        o += path('M' + ' L'.join(f'{x:.0f},{y:.0f}' for x, y in pts), w=2)
        for (d, lat, lon), (x, y) in zip(track, pts):
            o += circle(x, y, 4, INK, 0) + text(x + 7, y + 4, d, 9, 'start', weight='bold')
    return svg(X(96) + 20, Y(10) + 22, o, width=w)


EROSION_FIXES = ['plant trees and grass', 'build an embankment', 'place geo-bags', 'make terraces']


def erosion_fixes(names=True, w='100%'):
    o = ''
    for i in range(4):
        o += rect(i * 150, 0, 140, 120, 10, 'white', 1.3)
    # trees on a slope
    o += path('M6,110 L130,40 L134,110 Z', LIGHT, 1.2) + pic('deciduous tree', 40, 46, 34) + pic('deciduous tree', 82, 22, 34) + pic('herb', 20, 82, 20)
    for x, y in ((57, 80), (99, 56)):
        o += path(f'M{x},{y} l-8,10 M{x},{y} l8,10 M{x},{y} l0,12', w=0.9)
    # embankment beside a river
    o += rect(151, 80, 60, 39, 0, LIGHT, 0) + path('M151,80 q12,-5 24,0 t24,0 t12,0', w=1) + path('M211,119 L226,62 L262,62 L289,119 Z', GREY, 1.4)
    o += pic('house', 262, 30, 26)
    # geo-bags stacked on a river bank
    o += rect(301, 84, 60, 35, 0, LIGHT, 0) + path('M301,84 q12,-5 24,0 t24,0 t12,0', w=1) + path('M361,60 L439,60 L439,119 L380,119 Z', GREY, 1.2)
    for r, n in ((0, 4), (1, 3), (2, 2)):
        for k in range(n):
            o += rect(358 + r * 6 + k * 16, 104 - r * 14, 15, 13, 4, 'white', 1.2)
    # terraces
    for k in range(4):
        o += path(f'M{452 + k * 30},{116 - k * 22} L{452 + k * 30},{94 - k * 22} L{482 + k * 30},{94 - k * 22}', w=1.4)
        o += pic('rice plant', 458 + k * 30, 76 - k * 22, 18)
    labels = EROSION_FIXES if names else list('ABCD')
    for i in range(4):
        o += mtext(i * 150 + 70, 138, labels[i], 11, 20, weight='bold')
    return svg(590, 160, o, width=w)


# ------------------------------------------------------------------ physical science
def element_compound(w='100%'):
    """Particle pictures: an element, a compound, and a mixture."""
    o = ''
    boxes = [('element', 'one kind of atom (iron)'), ('compound', 'different atoms joined (water)'), ('mixture', 'not joined together')]
    for i, (n, d) in enumerate(boxes):
        o += rect(i * 160, 0, 140, 110, 6, 'white', 1.4)
        o += text(i * 160 + 70, 128, n, 12, weight='bold') + text(i * 160 + 70, 142, d, 9.5, italic=True)
    for r in range(4):
        for c in range(5):
            o += circle(20 + c * 25, 20 + r * 24, 10, GREY, 1.2)
    for k, (x, y) in enumerate(((190, 30), (240, 40), (290, 26), (200, 80), (260, 86), (300, 70))):
        o += circle(x, y, 11, GREY, 1.2) + circle(x - 12, y + 9, 6, 'white', 1.2) + circle(x + 12, y + 9, 6, 'white', 1.2)
    for k, (x, y) in enumerate(((350, 26), (400, 40), (440, 22), (370, 70), (420, 82), (450, 60), (346, 92))):
        o += circle(x, y, 9 if k % 2 else 6, GREY if k % 2 else 'white', 1.2)
    return svg(460, 148, o, width=w)


def forcemeter(reading, maxn=10, w='100%'):
    """A spring forcemeter (newton meter) holding a bag."""
    o = rect(40, 10, 40, 200, 6, 'white', 1.6) + line(60, 0, 60, 10, 2) + circle(60, 0, 5, 'white', 1.4)
    for v in range(maxn + 1):
        y = 30 + v * 15
        o += line(66, y, 78, y, 1) + text(84, y + 4, str(v), 9, 'start')
    y = 30 + reading * 15
    o += path(f'M60,14 ' + ' '.join(f'L{54 if k % 2 else 66},{14 + (y - 16) * (k + 1) / 12:.1f}' for k in range(12)), w=1.2)
    o += line(48, y, 72, y, 2.4) + line(60, y, 60, 222, 1.4) + path('M44,222 L76,222 L82,262 L38,262 Z', LIGHT, 1.4)
    o += text(102, 30, 'N', 10, 'start', weight='bold')
    return svg(130, 268, o, width=w)


FORCE_NAMES = ['push', 'pull', 'friction', 'gravity (weight)', 'upthrust', 'air resistance']


def force_arrows(w='100%'):
    """A box pulled along the floor: pull, friction, weight and support force."""
    o = line(0, 140, 420, 140, 1.6)
    for k in range(20):
        o += line(10 + k * 21, 140, 2 + k * 21, 150, 0.9)
    o += rect(150, 80, 110, 60, 4, LIGHT, 1.6) + text(205, 115, 'box', 12, weight='bold')
    o += arrow(262, 110, 380, 110, 2.6, 11) + text(330, 100, 'pull', 12, weight='bold')
    o += arrow(148, 132, 60, 132, 2.6, 11) + text(96, 124, 'friction', 12, weight='bold')
    o += arrow(205, 140, 205, 200, 2.6, 11) + text(212, 194, 'weight (gravity)', 11, 'start', weight='bold')
    o += arrow(205, 80, 205, 26, 2.6, 11) + text(212, 34, 'support from floor', 11, 'start', weight='bold')
    return svg(420, 206, o, width=w)


FLIGHT_FORCES = ['lift', 'weight', 'thrust', 'drag']


def flight_forces(labels=True, w='100%'):
    """Side view of a plane with the four forces of flight."""
    o = path('M110,124 C110,110 150,104 240,104 C290,104 318,112 330,124 C318,134 290,140 240,140 C160,140 110,136 110,124 Z', 'white', 1.8)
    o += path('M120,114 L96,80 L112,80 L150,108 Z', 'white', 1.6) + path('M190,126 L230,174 L250,174 L236,126 Z', LIGHT, 1.6)
    o += path('M300,114 C306,112 314,114 318,118', w=1.2)
    for k in range(6):
        o += circle(170 + k * 18, 118, 3, 'white', 1.1)
    pts = [((220, 102), (220, 22), 'lift', 'start', 12, 30), ((220, 146), (220, 226), 'weight', 'start', 12, 222),
           ((334, 124), (420, 124), 'thrust', 'end', 418, 112), ((106, 124), (20, 124), 'drag', 'start', 22, 112)]
    for i, ((x1, y1), (x2, y2), n, a, lx, ly) in enumerate(pts):
        o += arrow(x1, y1, x2, y2, 2.8, 12)
        if x1 == x2:
            lx = x2 + 12
        o += text(lx, ly, n if labels else str(i + 1), 13, a, weight='bold')
    return svg(440, 240, o, width=w)


def float_forces(w='100%'):
    o = rect(0, 100, 380, 90, 0, LIGHT, 0) + path('M0,100 q20,-5 40,0 t40,0 t40,0 t40,0 t40,0 t40,0 t40,0 t40,0 t40,0 t40,0', w=1.2)
    o += path('M120,80 L260,80 L240,124 L140,124 Z', 'white', 1.6) + line(190, 80, 190, 30, 1.6) + path('M190,32 L230,70 L190,70 Z', 'white', 1.3)
    o += arrow(160, 112, 160, 180, 2.6, 11) + text(168, 176, 'weight (down)', 11, 'start', weight='bold')
    o += arrow(220, 160, 220, 92, 2.6, 11) + text(228, 152, 'upthrust (up)', 11, 'start', weight='bold')
    o += text(40, 150, 'water pushes up', 10, italic=True) + text(40, 164, 'on the boat', 10, italic=True)
    return svg(380, 190, o, width=w)


def circuit_symbols(names=True, w='100%'):
    o = ''
    cells = ['cell', 'battery', 'lamp (bulb)', 'switch (open)', 'switch (closed)', 'buzzer', 'motor', 'wire']
    for i, n in enumerate(cells):
        x0, y0 = (i % 4) * 140, (i // 4) * 96
        cx, cy = x0 + 60, y0 + 36
        o += line(cx - 50, cy, cx + 50, cy, 1.6) if n == 'wire' else ''
        if n == 'cell':
            o += line(cx - 50, cy, cx - 6, cy, 1.6) + line(cx - 6, cy - 20, cx - 6, cy + 20, 2) + line(cx + 6, cy - 10, cx + 6, cy + 10, 4) + line(cx + 6, cy, cx + 50, cy, 1.6)
        if n == 'battery':
            o += line(cx - 50, cy, cx - 18, cy, 1.6) + line(cx + 18, cy, cx + 50, cy, 1.6)
            for dx in (-18, 6):
                o += line(cx + dx, cy - 20, cx + dx, cy + 20, 2) + line(cx + dx + 12, cy - 10, cx + dx + 12, cy + 10, 4)
            o += line(cx - 6, cy, cx + 6, cy, 1, '2 2')
        if n == 'lamp (bulb)':
            o += line(cx - 50, cy, cx - 16, cy, 1.6) + line(cx + 16, cy, cx + 50, cy, 1.6) + circle(cx, cy, 16, 'white', 1.8)
            o += line(cx - 11, cy - 11, cx + 11, cy + 11, 1.6) + line(cx - 11, cy + 11, cx + 11, cy - 11, 1.6)
        if n.startswith('switch'):
            o += line(cx - 50, cy, cx - 18, cy, 1.6) + circle(cx - 18, cy, 3, 'white', 1.4) + circle(cx + 18, cy, 3, 'white', 1.4) + line(cx + 18, cy, cx + 50, cy, 1.6)
            o += line(cx - 16, cy - 1, cx + 16, cy - (18 if 'open' in n else 1), 1.8)
        if n == 'buzzer':
            o += line(cx - 50, cy, cx - 14, cy, 1.6) + line(cx + 14, cy, cx + 50, cy, 1.6) + path(f'M{cx - 16},{cy - 4} A16,16 0 0 1 {cx + 16},{cy - 4} Z', 'white', 1.8)
            o += line(cx - 14, cy - 4, cx - 14, cy, 1.6) + line(cx + 14, cy - 4, cx + 14, cy, 1.6)
        if n == 'motor':
            o += line(cx - 50, cy, cx - 16, cy, 1.6) + line(cx + 16, cy, cx + 50, cy, 1.6) + circle(cx, cy, 16, 'white', 1.8) + text(cx, cy + 5, 'M', 14, weight='bold')
        o += text(cx, y0 + 80, n if names else chr(65 + i), 11.5, weight='bold')
    return svg(560, 186, o, width=w)


def circuit(parts=('cell', 'lamp', 'switch'), closed=True, w='100%'):
    """A series circuit diagram drawn as a rectangle loop with the given components."""
    o = ''
    L, T, R, B = 30, 30, 330, 170
    o += line(L, T, R, T, 1.6) + line(R, T, R, B, 1.6) + line(R, B, L, B, 1.6) + line(L, B, L, T, 1.6)
    slots = [((L + R) / 2, T, 'h'), (R, (T + B) / 2, 'v'), ((L + R) / 2, B, 'h'), (L, (T + B) / 2, 'v')]
    for (x, y, ori), p in zip(slots, parts):
        g = ''
        if p == 'cell':
            g = rect(-14, -24, 28, 48, 0, 'white', 0) + line(-6, -20, -6, 20, 2) + line(6, -10, 6, 10, 4)
        elif p == 'lamp':
            g = rect(-18, -18, 36, 36, 0, 'white', 0) + circle(0, 0, 16, 'white', 1.8) + line(-11, -11, 11, 11, 1.6) + line(-11, 11, 11, -11, 1.6)
        elif p == 'switch':
            g = rect(-22, -20, 44, 26, 0, 'white', 0) + circle(-18, 0, 3, 'white', 1.4) + circle(18, 0, 3, 'white', 1.4)
            g += line(-16, -1, 16, -1 if closed else -18, 1.8)
        elif p == 'buzzer':
            g = rect(-18, -18, 36, 20, 0, 'white', 0) + path('M-16,-4 A16,16 0 0 1 16,-4 Z', 'white', 1.8)
        elif p == 'motor':
            g = rect(-18, -18, 36, 36, 0, 'white', 0) + circle(0, 0, 16, 'white', 1.8) + text(0, 5, 'M', 14, weight='bold')
        rot = 0 if ori == 'h' else 90
        o += f'<g transform="translate({x} {y}) rotate({rot})">{g}</g>'
    return svg(360, 200, o, width=w)


def bar_magnets(w='100%'):
    """Like poles repel, unlike poles attract."""
    def mag(x, y, left):
        o = rect(x, y, 70, 26, 2, 'white', 1.6) + rect(x + 35, y, 35, 26, 0, GREY, 0) + rect(x, y, 70, 26, 2, 'none', 1.6)
        return o + text(x + 17, y + 18, left, 13, weight='bold') + text(x + 52, y + 18, 'S' if left == 'N' else 'N', 13, weight='bold')
    o = mag(10, 20, 'N') + mag(150, 20, 'N') + text(130, 70, 'S and N: attract (pull together)', 11, weight='bold')
    o += arrow(88, 27, 122, 27, 1.8, 7) + arrow(142, 40, 108, 40, 1.8, 7)
    o += mag(10, 100, 'S') + mag(170, 100, 'N') + text(130, 150, 'N and N: repel (push apart)', 11, weight='bold')
    o += arrow(118, 113, 88, 113, 1.8, 7) + arrow(122, 113, 162, 113, 1.8, 7)
    return svg(260, 160, o, width=w)


def electromagnet(w='100%'):
    o = rect(110, 60, 160, 22, 2, GREY, 1.6) + text(190, 52, 'iron nail', 10, italic=True)
    for k in range(12):
        o += ellipse(124 + k * 12, 71, 6, 16, 'none', 1.4)
    o += path('M124,87 C100,120 60,130 60,150', w=1.4) + path('M256,87 C280,120 300,130 300,150', w=1.4)
    o += rect(150, 140, 70, 30, 3, 'white', 1.6) + text(185, 160, 'battery', 10, weight='bold')
    o += path('M60,150 L60,155 L150,155', w=1.4) + path('M300,150 L300,155 L220,155', w=1.4)
    for k in range(4):
        o += rect(284 + k * 8, 50 - k * 2, 3, 16, 1, 'white', 1.1)
    o += text(300, 30, 'paper clips are attracted', 10, italic=True) + text(190, 112, 'coil of wire', 10, italic=True)
    return svg(380, 180, o, width=w)


def recycle_melt(w='100%'):
    from art import pic_row
    return pic_row(['plastic bottle', 'fire', 'droplet', 'package'],
                   ['used plastic', 'heat: it melts', 'pour into a mould', 'cools: new solid'], 50, 90, 10.5, w, arrows=True)
