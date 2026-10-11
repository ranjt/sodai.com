"""
Line-art illustrations (SVG) for black-and-white printing. All drawings are original.
Conventions: black strokes (#111), white or light-grey fills, Andika text. Numbered markers
(marker/callout) are used by ws.Label for "label the diagram" questions; pass labels=[...]
to the same drawing to get a fully labelled version for articles and answer keys.
"""
import math

INK = '#111'
GREY = '#d9d9d9'
LIGHT = '#eeeeee'
SW = 1.6


def svg(w, h, body, width=None, cls=''):
    style = f'width:{width};' if width else 'width:100%;'
    return (f'<svg class="{cls}" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" style="{style}height:auto" '
            f'font-family="Andika, sans-serif" font-size="11" stroke-linecap="round" stroke-linejoin="round">{body}</svg>')


def text(x, y, s, size=11, anchor='middle', weight='normal', italic=False, fill=INK):
    st = ' font-style="italic"' if italic else ''
    return (f'<text x="{x}" y="{y}" font-size="{size}" text-anchor="{anchor}" font-weight="{weight}" '
            f'fill="{fill}"{st}>{s}</text>')


def line(x1, y1, x2, y2, w=SW, dash=None, color=INK):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{w}"{d}/>'


def path(d, fill='none', w=SW, dash=None):
    ds = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<path d="{d}" fill="{fill}" stroke="{INK}" stroke-width="{w}"{ds}/>'


def circle(cx, cy, r, fill='white', w=SW, dash=None):
    ds = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="{INK}" stroke-width="{w}"{ds}/>'


def ellipse(cx, cy, rx, ry, fill='white', w=SW, rot=0):
    t = f' transform="rotate({rot} {cx} {cy})"' if rot else ''
    return f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{fill}" stroke="{INK}" stroke-width="{w}"{t}/>'


def rect(x, y, w, h, r=0, fill='white', sw=SW, dash=None):
    ds = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{INK}" stroke-width="{sw}"{ds}/>'


def arrow(x1, y1, x2, y2, w=SW, head=7, dash=None, color=INK):
    ang = math.atan2(y2 - y1, x2 - x1)
    bx, by = x2 - head * math.cos(ang), y2 - head * math.sin(ang)
    p1 = (bx + head * 0.5 * math.sin(ang), by - head * 0.5 * math.cos(ang))
    p2 = (bx - head * 0.5 * math.sin(ang), by + head * 0.5 * math.cos(ang))
    return (line(x1, y1, bx, by, w, dash, color) +
            f'<polygon points="{x2},{y2} {p1[0]:.1f},{p1[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}" fill="{color}"/>')


def curved_arrow(x1, y1, cx, cy, x2, y2, w=SW, head=7, dash=None):
    """Quadratic curve from (x1,y1) to (x2,y2) with control (cx,cy), arrowhead at the end."""
    ang = math.atan2(y2 - cy, x2 - cx)
    bx, by = x2 - head * math.cos(ang), y2 - head * math.sin(ang)
    p1 = (bx + head * 0.5 * math.sin(ang), by - head * 0.5 * math.cos(ang))
    p2 = (bx - head * 0.5 * math.sin(ang), by + head * 0.5 * math.cos(ang))
    return (path(f'M{x1},{y1} Q{cx},{cy} {bx:.1f},{by:.1f}', w=w, dash=dash) +
            f'<polygon points="{x2},{y2} {p1[0]:.1f},{p1[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}" fill="{INK}"/>')


def marker(n, x, y, r=8):
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="white" stroke="{INK}" stroke-width="1.4"/>'
            f'<text x="{x}" y="{y + 3.8}" font-size="10.5" font-weight="bold" text-anchor="middle" '
            f'font-family="Fredoka, sans-serif">{n}</text>')


def callout(i, tx, ty, px, py, labels=None, anchor=None):
    """Leader line from a part (px,py) to a label position (tx,ty).
    labels=None -> numbered marker i (for label-the-diagram); labels=[...] -> the word labels[i-1]."""
    out = line(px, py, tx, ty, 1)
    out += f'<circle cx="{px}" cy="{py}" r="1.8" fill="{INK}"/>'
    if labels:
        a = anchor or ('end' if tx < px else 'start')
        dx = -4 if a == 'end' else 4
        out += text(tx + dx, ty + 4, labels[i - 1], 11, a)
    else:
        out += marker(i, tx + (-9 if tx < px else 9), ty)
    return out


def face(mood, size=22):
    mouth = {'sad': 'M7,15.5 Q11,12 15,15.5', 'meh': 'M7,14.5 L15,14.5', 'happy': 'M7,13 Q11,17.5 15,13'}[mood]
    return (f'<svg class="face" viewBox="0 0 22 22" width="{size}" height="{size}">'
            f'<circle cx="11" cy="11" r="9.5" fill="white" stroke="{INK}" stroke-width="1.4"/>'
            f'<circle cx="8" cy="9" r="1.2" fill="{INK}"/><circle cx="14" cy="9" r="1.2" fill="{INK}"/>'
            f'<path d="{mouth}" fill="none" stroke="{INK}" stroke-width="1.4" stroke-linecap="round"/></svg>')


# ------------------------------------------------------------------ graphs
def graph(labels, values, ylabel, xlabel, ymax, step, kind='bar', series_names=None, w=150, h=82, plot=False,
          blank_axes=False):
    """Graph paper with axes, in mm-like units (viewBox scaled to page width)."""
    W, H = w * 4, h * 4
    L, R, T, B = 52, 14, 14, 50
    pw, ph = W - L - R, H - T - B
    out = ''
    # grid
    nsteps = int(round(ymax / step))
    for i in range(nsteps + 1):
        y = T + ph - ph * i / nsteps
        out += line(L, y, L + pw, y, 0.6, color='#aaa')
        if not blank_axes:
            out += text(L - 6, y + 4, f'{i * step:g}', 11, 'end')
    minor = 4
    for i in range(nsteps * minor + 1):
        y = T + ph - ph * i / (nsteps * minor)
        out += line(L, y, L + pw, y, 0.3, color='#ccc')
    n = len(labels)
    slot = pw / n
    for i in range(n * 2 + 1):
        x = L + pw * i / (n * 2)
        out += line(x, T, x, T + ph, 0.3, color='#ccc')
    out += line(L, T, L, T + ph, 1.8) + line(L, T + ph, L + pw, T + ph, 1.8)
    if not blank_axes:
        for i, lab in enumerate(labels):
            out += text(L + slot * (i + 0.5), T + ph + 16, lab, 11)
    out += text(L + pw / 2, H - 10, xlabel, 12, weight='bold')
    out += f'<text transform="translate(16 {T + ph / 2}) rotate(-90)" text-anchor="middle" font-size="12" font-weight="bold">{ylabel}</text>'
    if plot:
        series = values if values and isinstance(values[0], (list, tuple)) else [values]
        fills = ['#555', 'white', '#bbb']
        for si, s in enumerate(series):
            pts = []
            for i, v in enumerate(s):
                if v is None:
                    continue
                cx = L + slot * (i + 0.5)
                cy = T + ph - ph * v / ymax
                if kind == 'bar':
                    bw = slot * 0.6 / len(series)
                    bx = L + slot * i + slot * 0.2 + bw * si
                    out += rect(bx, cy, bw, T + ph - cy, 0, fills[si % 3], 1.4)
                else:
                    pts.append((cx, cy))
            if kind == 'line' and pts:
                out += path('M' + ' L'.join(f'{x:.1f},{y:.1f}' for x, y in pts), w=1.6, dash=None if si == 0 else '5 3')
                for x, y in pts:
                    out += (circle(x, y, 3.2, '#111' if si == 0 else 'white', 1.3))
        if series_names:
            for si, name in enumerate(series_names):
                lx = L + 10 + si * 120
                sample = rect(lx, 4, 14, 9, 0, fills[si % 3], 1.2) if kind == 'bar' else \
                    line(lx, 9, lx + 16, 9, 1.6, None if si == 0 else '5 3') + circle(lx + 8, 9, 3, '#111' if si == 0 else 'white', 1.2)
                out += sample + text(lx + 20, 13, name, 11, 'start')
    return f'<div class="fig">{svg(W, H, out, width=f"{w}mm")}</div>'


# ------------------------------------------------------------------ plants
def leaf(x, y, length, angle, fill='white', vein=True):
    """A simple leaf from (x,y) pointing at angle (degrees)."""
    a = math.radians(angle)
    tx, ty = x + length * math.cos(a), y + length * math.sin(a)
    nx, ny = -math.sin(a) * length * 0.32, math.cos(a) * length * 0.32
    mx, my = (x + tx) / 2, (y + ty) / 2
    d = f'M{x},{y} Q{mx + nx:.1f},{my + ny:.1f} {tx:.1f},{ty:.1f} Q{mx - nx:.1f},{my - ny:.1f} {x},{y} Z'
    out = path(d, fill, 1.4)
    if vein:
        out += line(x, y, x + (tx - x) * 0.85, y + (ty - y) * 0.85, 0.8)
    return out


def flower_section(labels=None, numbered=True, w='100%'):
    """Half-flower (longitudinal section). Parts in marker order:
    1 petal, 2 anther, 3 filament, 4 stigma, 5 style, 6 ovary, 7 ovule, 8 sepal, 9 stem (flower stalk)."""
    b = ''
    # stem + receptacle
    b += path('M196,330 C196,300 194,280 196,262 M212,330 C212,300 214,280 212,262', w=1.6)
    b += path('M170,262 Q204,276 238,262 Q230,248 204,246 Q178,248 170,262 Z', fill=LIGHT)
    # sepals
    b += path('M176,258 Q140,262 120,236 Q150,232 182,248 Z', fill=GREY, w=1.4)
    b += path('M232,258 Q268,262 288,236 Q258,232 226,248 Z', fill=GREY, w=1.4)
    # petals (large, cut)
    b += path('M182,246 C120,230 80,150 110,90 C140,120 170,190 192,236 Z', fill='white', w=1.6)
    b += path('M226,246 C288,230 328,150 298,90 C268,120 238,190 216,236 Z', fill='white', w=1.6)
    b += path('M110,90 C125,108 140,140 150,170', w=0.7) + path('M298,90 C283,108 268,140 258,170', w=0.7)
    # carpel: ovary, ovules, style, stigma
    b += path('M188,246 C178,226 182,200 204,194 C226,200 230,226 220,246 Z', fill='white', w=1.6)
    for oy in (208, 222, 234):
        b += ellipse(204, oy, 6, 4.2, fill=GREY, w=1.1)
    b += path('M200,196 L198,120 M208,196 L210,120', w=1.4)
    b += path('M190,120 Q204,96 218,120 Q211,113 204,116 Q197,113 190,120 Z', fill=GREY, w=1.4)
    # stamens
    for (fx, fy, ax, ay, rot) in ((178, 240, 150, 140, -18), (230, 240, 258, 140, 18), (186, 240, 170, 152, -8), (222, 240, 238, 152, 8)):
        b += path(f'M{fx},{fy} Q{(fx + ax) / 2 + (6 if ax < 204 else -6)},{(fy + ay) / 2} {ax},{ay + 12}', w=1.3)
        b += ellipse(ax, ay, 6.5, 13, fill=GREY, w=1.3, rot=rot)
    pts = [(1, 60, 150, 116, 150), (2, 60, 104, 145, 132), (3, 60, 200, 166, 196), (8, 60, 250, 132, 244),
           (9, 60, 315, 196, 312), (4, 348, 100, 212, 112), (5, 348, 150, 209, 156), (6, 348, 222, 222, 228),
           (7, 348, 196, 210, 208)]
    for n, tx, ty, px, py in pts:
        b += callout(n, tx, ty, px, py, labels)
    return svg(408, 340, b, width=w)


FLOWER_PARTS = ['petal', 'anther', 'filament', 'stigma', 'style', 'ovary', 'ovule', 'sepal', 'flower stalk']


def bee(x, y, s=1.0):
    t = f'translate({x} {y}) scale({s})'
    b = (ellipse(0, 0, 16, 10, 'white', 1.4) + path('M-6,-9 Q-4,0 -6,9 M2,-10 Q4,0 2,10', w=1.4) +
         f'<path d="M-6,-9 Q-4,0 -6,9 L2,10 Q4,0 2,-10 Z" fill="{GREY}"/>' +
         circle(-20, -2, 7, 'white', 1.4) + circle(-22, -4, 1.4, INK) +
         path('M-24,-8 Q-30,-18 -26,-20 M-20,-9 Q-22,-20 -17,-21', w=1) +
         ellipse(2, -16, 10, 6, 'white', 1.2, -20) + ellipse(10, -14, 8, 5, 'white', 1.2, 10) +
         path('M16,0 L22,1', w=1.4))
    return f'<g transform="{t}">{b}</g>'


def seedling(x, y, h=40, leaves=2):
    b = path(f'M{x},{y} Q{x - 3},{y - h / 2} {x},{y - h}', w=1.6)
    b += leaf(x, y - h, h * 0.45, -150) + leaf(x, y - h, h * 0.45, -30)
    if leaves > 2:
        b += leaf(x, y - h * 0.55, h * 0.4, -160) + leaf(x, y - h * 0.55, h * 0.4, -20)
    return b


def roots(x, y, depth=18):
    return (path(f'M{x},{y} Q{x + 2},{y + depth / 2} {x},{y + depth}', w=1.3) +
            path(f'M{x},{y + depth * 0.4} Q{x - 6},{y + depth * 0.6} {x - 9},{y + depth * 0.8}', w=1) +
            path(f'M{x},{y + depth * 0.55} Q{x + 6},{y + depth * 0.75} {x + 9},{y + depth * 0.95}', w=1))


def simple_flower(x, y, r=11, petals=6, fill='white'):
    b = ''
    for i in range(petals):
        a = 2 * math.pi * i / petals
        b += ellipse(x + r * math.cos(a), y + r * math.sin(a), r * 0.75, r * 0.45, fill, 1.2, math.degrees(a))
    return b + circle(x, y, r * 0.45, GREY, 1.2)


def flowering_plant(x, y, h=90):
    b = path(f'M{x},{y} C{x - 4},{y - h * 0.4} {x + 4},{y - h * 0.7} {x},{y - h}', w=1.8)
    b += leaf(x, y - h * 0.3, h * 0.32, -160) + leaf(x, y - h * 0.45, h * 0.3, -25) + leaf(x, y - h * 0.62, h * 0.26, -150)
    b += simple_flower(x, y - h - 8, 10)
    return b


def life_cycle(labels=None, numbered=False, w='100%'):
    """Flowering-plant life cycle wheel. Stage order: 1 seed, 2 germination, 3 young plant, 4 flowering,
    5 pollination, 6 fertilisation & fruit, 7 seed dispersal."""
    cx, cy, R, r = 345, 215, 140, 36
    out = ''
    pos = []
    for i in range(7):
        a = -math.pi / 2 + 2 * math.pi * i / 7
        pos.append((cx + R * math.cos(a), cy + R * math.sin(a), a))
    # straight arrows from the edge of one stage circle to the next
    for i in range(7):
        x1, y1, _ = pos[i]
        x2, y2, _ = pos[(i + 1) % 7]
        d = math.hypot(x2 - x1, y2 - y1)
        ux, uy = (x2 - x1) / d, (y2 - y1) / d
        out += arrow(x1 + ux * (r + 6), y1 + uy * (r + 6), x2 - ux * (r + 6), y2 - uy * (r + 6), 2, 10)
    pics = [
        lambda x, y: ellipse(x, y, 13, 9, GREY, 1.4) + path(f'M{x - 4},{y - 6} Q{x + 2},{y} {x - 3},{y + 6}', w=1),
        lambda x, y: ellipse(x, y + 6, 12, 8, GREY, 1.4) + roots(x + 4, y + 10, 14) + path(f'M{x + 2},{y} Q{x + 8},{y - 12} {x + 4},{y - 18}', w=1.4),
        lambda x, y: seedling(x, y + 20, 36, 4),
        lambda x, y: flowering_plant(x, y + 30, 46),
        lambda x, y: simple_flower(x - 6, y + 2, 13) + bee(x + 22, y - 14, 0.62),
        lambda x, y: ellipse(x, y, 18, 22, 'white', 1.6) + ellipse(x - 5, y - 4, 4, 3, GREY, 1) + ellipse(x + 5, y + 2, 4, 3, GREY, 1) + ellipse(x - 2, y + 9, 4, 3, GREY, 1) + path(f'M{x},{y - 22} L{x},{y - 30}', w=1.6),
        lambda x, y: dandelion_seed(x - 10, y + 12, 0.85) + dandelion_seed(x + 14, y - 2, 0.7) + wind_lines(x - 34, y - 18),
    ]
    for i, (px, py, a) in enumerate(pos):
        out += circle(px, py, r, 'white', 1.8)
        out += f'<g>{pics[i](px, py)}</g>'
        lx, ly = px + (r + 16) * math.cos(a), py + (r + 16) * math.sin(a)
        anchor = 'middle' if abs(math.cos(a)) < 0.3 else ('start' if math.cos(a) > 0 else 'end')
        if labels:
            dy = -6 if math.sin(a) < -0.5 else (14 if math.sin(a) > 0.5 else 4)
            out += text(lx, ly + dy, labels[i], 13, anchor, 'bold')
        elif numbered:
            out += marker(i + 1, px + (r + 2) * math.cos(a - 0.9), py + (r + 2) * math.sin(a - 0.9))
    return svg(690, 430, out, width=w)


LIFE_CYCLE_STAGES = ['seed', 'germination', 'young plant', 'flowering', 'pollination', 'fertilisation and fruit',
                     'seed dispersal']


def wind_lines(x, y):
    return (path(f'M{x},{y} q14,-6 26,0 t26,0', w=1.1) + path(f'M{x + 6},{y + 10} q12,-5 22,0 t22,0', w=1.1))


def dandelion_seed(x, y, s=1.0):
    t = f'translate({x} {y}) scale({s})'
    b = ellipse(0, 10, 2.2, 6, GREY, 1.2) + line(0, 4, 0, -16, 1)
    for i in range(9):
        a = math.radians(-160 + i * 17.5)
        b += line(0, -16, 14 * math.cos(a), -16 + 14 * math.sin(a), 0.8)
    return f'<g transform="{t}">{b}</g>'


def dispersal_icons():
    """Six seed types (for sorting by dispersal method): dandelion, sycamore, coconut, burr, berry, pea pod."""
    items = []
    # dandelion (wind)
    items.append(dandelion_seed(50, 55, 1.6))
    # sycamore (wind, wings)
    items.append(ellipse(42, 62, 7, 5, GREY, 1.4) + path('M47,58 C70,40 92,28 96,40 C92,50 72,56 49,64 Z', 'white', 1.4)
                 + path('M37,58 C14,40 0,32 2,44 C8,52 22,58 35,64 Z', 'white', 1.4))
    # coconut (water)
    items.append(path('M20,70 C10,40 30,18 50,18 C78,18 92,46 82,70 C74,86 30,88 20,70 Z', GREY, 1.6)
                 + circle(46, 34, 3, INK) + circle(56, 32, 3, INK) + circle(51, 42, 3, INK)
                 + path('M0,86 q12,-6 24,0 t24,0 t24,0 t24,0', w=1.2))
    # burr (animal fur, hooks)
    burr = circle(50, 50, 18, GREY, 1.4)
    for i in range(16):
        a = 2 * math.pi * i / 16
        x1, y1 = 50 + 18 * math.cos(a), 50 + 18 * math.sin(a)
        x2, y2 = 50 + 30 * math.cos(a), 50 + 30 * math.sin(a)
        burr += line(x1, y1, x2, y2, 1.1) + path(f'M{x2:.1f},{y2:.1f} q{3 * math.cos(a + 1.6):.1f},{3 * math.sin(a + 1.6):.1f} {1.5 * math.cos(a + 3):.1f},{1.5 * math.sin(a + 3):.1f}', w=1)
    items.append(burr)
    # berries (eaten by animals)
    items.append(path('M50,10 Q52,24 48,30 M50,16 Q62,8 74,14 Q62,22 51,18', w=1.4)
                 + circle(38, 50, 14, GREY, 1.4) + circle(62, 52, 14, GREY, 1.4) + circle(50, 74, 14, GREY, 1.4)
                 + path('M48,30 L38,36 M48,30 L60,38 M48,30 L50,60', w=1))
    # pea pod (bursts open)
    items.append(path('M8,58 C20,30 70,24 92,34 C80,52 30,70 8,58 Z', 'white', 1.6)
                 + path('M8,58 C26,44 62,36 92,34', w=1)
                 + ''.join(circle(28 + 14 * i, 50 - 4 * i, 6, GREY, 1.2) for i in range(4))
                 + path('M96,30 l8,-6 M98,38 l10,-1 M94,24 l4,-9', w=1.2))
    return items


def dispersal_strip(numbered=True, names=None, w='100%'):
    icons = dispersal_icons()
    out = ''
    for i, ic in enumerate(icons):
        x = 10 + i * 118
        out += rect(x, 6, 108, 108, 12, 'white', 1.4)
        out += f'<g transform="translate({x + 4} {10})">{ic}</g>'
        if names:
            out += text(x + 54, 132, names[i], 12, weight='bold')
        elif numbered:
            out += text(x + 54, 132, chr(65 + i), 14, weight='bold')
    return svg(720, 140, out, width=w)


DISPERSAL_NAMES = ['dandelion', 'sycamore', 'coconut', 'burdock burr', 'berries', 'pea pod']


def bean_seed(labels=None, w='100%'):
    """Bean seed outside + opened inside. 1 seed coat, 2 scar, 3 food store, 4 embryo root, 5 embryo shoot."""
    o = '<g transform="translate(70 0)">'
    o += path('M40,40 C10,40 10,120 50,130 C90,140 120,110 104,84 C96,72 82,80 80,64 C78,44 66,40 40,40 Z', GREY, 1.8)
    o += ellipse(86, 70, 4, 7, 'white', 1.3, 30)
    o += path('M200,40 C170,40 170,120 210,130 C250,140 280,110 264,84 C256,72 242,80 240,64 C238,44 226,40 200,40 Z', 'white', 1.8)
    o += path('M206,46 C182,50 182,118 214,124 C244,128 262,108 252,90 C246,80 236,84 234,70 C232,54 222,46 206,46 Z', LIGHT, 1.2)
    o += path('M236,72 Q246,84 240,96 Q236,86 232,80 Z', 'white', 1.3) + path('M238,74 Q228,64 236,58 Q240,66 238,74', w=1.2)
    o += leaf(236, 60, 10, -100, 'white', False)
    o += text(64, 158, 'outside', 11, italic=True) + text(220, 158, 'inside (opened)', 11, italic=True)
    o += '</g>'
    for n, tx, ty, px, py in ((1, 50, 30, 104, 44), (2, 50, 110, 158, 72), (3, 230, 152, 270, 106), (4, 370, 116, 308, 92), (5, 370, 36, 308, 58)):
        o += callout(n, tx, ty, px, py, labels)
    return svg(500, 165, f'<g transform="translate(30 0)">{o}</g>', width=w)


BEAN_PARTS = ['seed coat', 'scar', 'food store', 'embryo root', 'embryo shoot']


def germination_strip(numbered=False, w='100%'):
    """Five stages of a germinating bean in soil, left to right."""
    out = rect(0, 70, 640, 90, 6, LIGHT, 0)
    out += line(0, 70, 640, 70, 1.6)
    for i in range(70):
        out += circle(8 + (i * 37) % 630, 80 + (i * 23) % 72, 1.1, '#999', 0)
    for i in range(5):
        x = 64 + i * 128
        seed = ellipse(x, 104, 14 - i * 1.2, 10 - i, GREY, 1.4)
        stage = seed
        if i >= 1:
            stage += roots(x + 6, 110, 10 + i * 7)
        if i >= 2:
            stage += path(f'M{x},{96} Q{x - 8},{80} {x - 2},{70 - (i - 2) * 16}', w=1.6)
        if i == 2:
            stage += path(f'M{x - 2},74 q-6,6 -4,10', w=1.3)
        if i >= 3:
            stage += leaf(x - 2, 70 - (i - 2) * 16, 14 + (i - 3) * 6, -150) + leaf(x - 2, 70 - (i - 2) * 16, 14 + (i - 3) * 6, -30)
        out += stage
        if numbered:
            out += marker(chr(65 + i), x, 150)
    return svg(640, 165, out, width=w)


def insect_flower(w='100%', title=True):
    """Big-petalled, scented flower with nectar and a visiting bee."""
    o = path('M100,190 Q98,150 100,118', w=1.8) + leaf(100, 165, 34, -150) + leaf(100, 150, 30, -30)
    for i in range(5):
        a = math.radians(-90 + i * 72)
        o += ellipse(100 + 30 * math.cos(a), 92 + 30 * math.sin(a), 26, 17, 'white', 1.6, math.degrees(a))
    o += circle(100, 92, 13, GREY, 1.4)
    for i in range(6):
        a = math.radians(i * 60)
        o += line(100, 92, 100 + 18 * math.cos(a), 92 + 18 * math.sin(a), 1) + circle(100 + 19 * math.cos(a), 92 + 19 * math.sin(a), 2.2, INK, 0)
    o += bee(160, 50, 0.9)
    o += path('M58,52 q-6,-8 0,-14 q6,-6 0,-12', w=1, dash='2 3') + path('M140,30 q-6,-8 0,-14', w=1, dash='2 3')
    if title:
        o += text(100, 212, 'insect-pollinated', 13, weight='bold')
    return svg(200, 220, o, width=w)


def wind_flower(w='100%', title=True):
    """Grass-type flower: small dull flowers, dangling anthers, feathery stigmas, pollen blowing away."""
    o = path('M100,200 Q96,140 104,40', w=1.8) + leaf(100, 180, 60, -120, 'white') + leaf(101, 150, 54, -55, 'white')
    for i, y in enumerate(range(48, 120, 14)):
        side = -1 if i % 2 else 1
        bx, by = 102 + side * 4, y
        o += ellipse(bx + side * 10, by, 9, 5, GREY, 1.2, side * 25)
        o += line(bx + side * 16, by + 2, bx + side * 22, by + 14, 1) + ellipse(bx + side * 23, by + 18, 2.4, 5, 'white', 1)
        o += path(f'M{bx + side * 14},{by - 3} q{side * 8},-6 {side * 6},-12 M{bx + side * 14},{by - 3} q{side * 12},-2 {side * 14},-8', w=0.9)
    for i in range(14):
        o += circle(140 + (i * 13) % 50, 60 + (i * 17) % 70, 1.6, INK, 0)
    o += wind_lines(130, 40)
    if title:
        o += text(100, 214, 'wind-pollinated', 13, weight='bold')
    return svg(200, 220, o, width=w)


def pollen_tube(labels=None, w='100%'):
    """Carpel with a pollen grain on the stigma growing a tube down to an ovule.
    1 pollen grain, 2 stigma, 3 pollen tube, 4 style, 5 ovule, 6 ovary."""
    o = path('M120,250 C80,240 78,186 120,176 C162,186 160,240 120,250 Z', 'white', 1.8)
    o += ellipse(120, 214, 10, 7, GREY, 1.3) + ellipse(104, 232, 8, 6, GREY, 1.2) + ellipse(136, 232, 8, 6, GREY, 1.2)
    o += path('M114,178 L112,60 M126,178 L128,60', w=1.6)
    o += path('M96,60 Q120,22 144,60 Q132,50 120,54 Q108,50 96,60 Z', GREY, 1.4)
    o += circle(116, 40, 7, 'white', 1.4) + circle(114, 38, 1.2, INK, 0) + circle(119, 42, 1.2, INK, 0)
    o += path('M118,46 C122,80 116,120 121,160 C123,180 118,196 120,207', w=1.4, dash='4 3')
    for n, tx, ty, px, py in ((1, 40, 30, 110, 38), (2, 200, 50, 140, 56), (3, 200, 120, 121, 120), (4, 40, 120, 113, 110),
                              (5, 200, 214, 129, 214), (6, 40, 236, 90, 230)):
        o += callout(n, tx, ty, px, py, labels)
    return svg(330, 260, f'<g transform="translate(45 0)">{o}</g>', width=w)


POLLEN_TUBE_PARTS = ['pollen grain', 'stigma', 'pollen tube', 'style', 'ovule', 'ovary']


def paper_helicopter(w='100%'):
    """Template for a paper helicopter (model sycamore seed) with fold and cut lines."""
    o = rect(60, 10, 120, 300, 0, 'white', 1.6)
    o += line(120, 10, 120, 130, 1.4, dash='7 4')
    o += line(60, 130, 90, 130, 1.4, dash='7 4') + line(150, 130, 180, 130, 1.4, dash='7 4')
    o += line(90, 130, 90, 310, 1.2, dash='2 3') + line(150, 130, 150, 310, 1.2, dash='2 3')
    o += text(90, 70, 'wing A', 12, weight='bold') + text(150, 70, 'wing B', 12, weight='bold')
    o += text(120, 230, 'body', 12, weight='bold') + text(120, 300, '+ paper clip', 10, italic=True)
    o += path('M196,10 L196,130', w=1) + line(190, 10, 202, 10, 1) + line(190, 130, 202, 130, 1)
    o += text(214, 74, 'wing', 11, 'start') + text(214, 88, 'length', 11, 'start')
    o += text(10, 150, '- - - cut', 10, 'start') + text(10, 166, '· · · fold', 10, 'start')
    return svg(260, 320, o, width=w)


def mustard_plant(x=0, y=0, s=1.0):
    o = path('M60,200 C58,150 62,110 60,40', w=1.8)
    for (yy, side) in ((170, -1), (140, 1), (110, -1)):
        o += leaf(60, yy, 34, -150 if side < 0 else -30, 'white')
    for (bx, by, ang) in ((60, 40, -90), (60, 60, -140), (60, 66, -40), (60, 85, -150), (60, 90, -30)):
        a = math.radians(ang)
        ex, ey = bx + 22 * math.cos(a), by + 22 * math.sin(a)
        o += line(bx, by, ex, ey, 1.1) + simple_flower(ex, ey, 5.5, 4, 'white')
    for (sx, sy, ang) in ((60, 120, -160), (60, 128, -20)):
        a = math.radians(ang)
        o += line(sx, sy, sx + 26 * math.cos(a), sy + 26 * math.sin(a), 2.6)
    return f'<g transform="translate({x} {y}) scale({s})">{o}</g>'


def mustard_field(w='100%'):
    o = line(0, 200, 545, 200, 1.6)
    for i, x in enumerate((0, 55, 110, 330, 385, 440)):
        o += mustard_plant(x, 0 if i % 2 else 10, 0.95)
    o += rect(220, 120, 80, 80, 4, LIGHT, 1.6) + rect(214, 112, 92, 12, 3, 'white', 1.6)
    for i in range(4):
        o += line(226, 140 + i * 14, 294, 140 + i * 14, 0.8)
    o += rect(254, 186, 14, 8, 1, INK, 0)
    o += text(260, 222, 'bee box (hive)', 12, italic=True)
    o += bee(200, 70, 0.8) + bee(330, 50, 0.7) + bee(290, 90, 0.6)
    o += path('M214,78 q30,-30 60,-10 q20,14 40,-20', w=1, dash='3 4')
    return svg(545, 230, o, width=w)


def pot(x, y, w=60, h=46):
    return (path(f'M{x - w / 2},{y} L{x + w / 2},{y} L{x + w / 2 - 8},{y + h} L{x - w / 2 + 8},{y + h} Z', LIGHT, 1.6)
            + rect(x - w / 2 - 4, y - 8, w + 8, 10, 2, 'white', 1.6))


def potted_plant(x, y, state='healthy', label=''):
    """state: healthy | wilted (no water) | dark (grown without light: tall, thin, pale) | small (cold)."""
    o = pot(x, y)
    if state == 'healthy':
        o += path(f'M{x},{y - 8} C{x - 3},{y - 40} {x + 3},{y - 70} {x},{y - 96}', w=1.8)
        for (yy, ang, ln) in ((-30, -160, 30), (-42, -20, 30), (-58, -150, 28), (-70, -30, 26), (-84, -140, 22), (-90, -40, 20)):
            o += leaf(x, y + yy, ln, ang, GREY)
        o += simple_flower(x, y - 104, 9)
    elif state == 'wilted':
        o += path(f'M{x},{y - 8} C{x - 2},{y - 40} {x + 2},{y - 60} {x + 4},{y - 70} C{x + 14},{y - 80} {x + 26},{y - 70} {x + 28},{y - 56}', w=1.8)
        for (px, py, ang) in ((x, y - 30, 130), (x + 1, y - 45, 60), (x + 4, y - 64, 110), (x + 20, y - 76, 70)):
            o += leaf(px, py, 22, ang, 'white')
        o += circle(x + 28, y - 50, 6, 'white', 1.3)
    elif state == 'dark':
        o += path(f'M{x},{y - 8} C{x - 2},{y - 60} {x + 2},{y - 110} {x},{y - 150}', w=1.1)
        for (yy, ang) in ((-70, -150), (-110, -30), (-148, -140)):
            o += leaf(x, y + yy, 14, ang, 'white')
    elif state == 'small':
        o += path(f'M{x},{y - 8} L{x},{y - 40}', w=1.6) + leaf(x, y - 30, 16, -150, GREY) + leaf(x, y - 38, 16, -30, GREY)
    if label:
        o += text(x, y + 64, label, 12, weight='bold')
    return o


def plant_needs(w='100%'):
    o = potted_plant(70, 150, 'healthy', 'light, water, warmth, air')
    o += potted_plant(230, 150, 'wilted', 'no water')
    o += potted_plant(390, 150, 'dark', 'no light')
    o += potted_plant(550, 150, 'small', 'too cold')
    return svg(620, 225, o, width=w)


def plant_parts(labels=None, w='100%'):
    """Whole plant with soil line. 1 flower, 2 leaf, 3 stem, 4 roots, 5 fruit."""
    o = rect(0, 190, 330, 90, 0, LIGHT, 0) + line(0, 190, 330, 190, 1.6)
    o += path('M160,190 C156,140 164,100 160,40', w=2)
    for (yy, ang, ln) in ((160, -155, 46), (140, -25, 46), (110, -150, 40), (88, -30, 38)):
        o += leaf(160, yy, ln, ang, GREY)
    o += simple_flower(160, 30, 13)
    o += line(160, 118, 190, 112, 1.4) + ellipse(200, 116, 12, 9, 'white', 1.4)
    # roots
    o += path('M160,190 Q158,220 162,262 M160,204 Q140,220 120,236 M161,214 Q186,230 204,246 M159,232 Q140,246 132,262 M162,240 Q178,252 182,268', w=1.4)
    for n, tx, ty, px, py in ((1, 260, 26, 172, 30), (2, 40, 120, 128, 150), (3, 40, 64, 160, 70), (4, 260, 250, 190, 242), (5, 260, 100, 208, 114)):
        o += callout(n, tx, ty, px, py, labels)
    return svg(330, 280, o, width=w)


PLANT_PARTS = ['flower', 'leaf', 'stem', 'roots', 'fruit']


def floating_garden(w='100%'):
    """A floating garden (dhap/baira): raft of water hyacinth and straw, with vegetables, on flood water."""
    o = ''
    for i in range(7):
        o += path(f'M{i * 90},212 q22,-8 45,0 t45,0', w=1.2)
    o += path('M40,182 L520,182 L500,206 L60,206 Z', GREY, 1.8)
    for i in range(24):
        o += path(f'M{60 + i * 19},{186 + (i % 3) * 5} q6,-4 12,0', w=0.9)
    for x in (110, 200, 290, 380, 460):
        o += seedling(x, 182, 40, 4)
    o += simple_flower(200, 130, 7) + simple_flower(380, 132, 7)
    o += path('M520,170 Q560,140 590,150 M590,150 L600,120', w=1.6)
    o += path('M560,190 L620,190 L612,206 L566,206 Z', 'white', 1.6)
    o += text(300, 236, 'flood water', 11, italic=True)
    o += text(300, 170 - 70, '', 11)
    return svg(640, 245, o, width=w)


# ------------------------------------------------------------------ human body
def body_outline():
    """Front view of head and torso (simple, friendly outline)."""
    o = ellipse(160, 52, 34, 40, 'white', 1.8)
    o += path('M146,90 L146,104 M174,90 L174,104', w=1.8)
    o += path('M146,104 C110,108 84,118 78,140 L66,250 Q64,262 74,262 L84,262 L96,160 '
              'L100,330 Q100,350 120,360 L200,360 Q220,350 220,330 L224,160 L236,262 L246,262 Q256,262 254,250 '
              'L242,140 C236,118 210,108 174,104', 'white', 1.8)
    return o


def organs(which='all'):
    """Organs drawn inside body_outline. which: 'all' or a set of names."""
    show = lambda n: which == 'all' or n in which
    o = ''
    if show('brain'):
        o += path('M134,46 C130,24 150,16 162,22 C176,14 192,26 188,44 C192,56 178,64 166,58 C154,64 136,60 134,46 Z', GREY, 1.4)
        o += path('M150,30 q6,8 0,16 M168,28 q-6,10 2,18 M176,40 q-8,4 -4,12', w=0.9)
    if show('spinal cord'):
        o += line(160, 62, 160, 300, 2.4) + line(160, 62, 160, 300, 0.8, color='white')
    if show('nerves'):
        for (x1, y1, x2, y2) in ((160, 150, 92, 200), (160, 150, 228, 200), (160, 260, 120, 340), (160, 260, 200, 340), (160, 200, 110, 250), (160, 200, 210, 250)):
            o += path(f'M{x1},{y1} Q{(x1 + x2) / 2},{y1 + 10} {x2},{y2}', w=0.9)
    if show('windpipe'):
        o += path('M156,88 L156,128 M164,88 L164,128', w=1.4)
        for y in range(92, 128, 6):
            o += line(156, y, 164, y, 0.7)
    if show('lungs'):
        o += path('M154,128 C130,120 112,140 110,170 C108,196 118,206 140,204 C152,202 154,180 154,128 Z', LIGHT, 1.5)
        o += path('M166,128 C190,120 208,140 210,170 C212,196 202,206 180,204 C168,202 166,180 166,128 Z', LIGHT, 1.5)
    if show('heart'):
        o += path('M168,150 C176,140 192,146 188,160 C186,172 176,180 170,188 C164,180 154,172 152,162 C150,148 162,144 168,150 Z', GREY, 1.6)
    if show('diaphragm'):
        o += path('M108,210 Q160,190 212,210', w=1.4, dash='5 3')
    if show('oesophagus'):
        o += path('M160,90 L160,212 Q160,220 168,222', w=1.4)
    if show('liver'):
        o += path('M104,216 C120,206 164,210 168,224 C160,240 128,246 108,240 C100,234 100,222 104,216 Z', GREY, 1.4)
    if show('stomach'):
        o += path('M168,222 C190,210 214,218 212,238 C210,258 186,262 176,252 C170,246 178,236 168,232 Z', LIGHT, 1.5)
    if show('kidneys'):
        o += path('M122,250 C112,250 110,272 122,276 C128,276 126,266 130,262 C132,256 128,250 122,250 Z', 'white', 1.3)
        o += path('M198,250 C208,250 210,272 198,276 C192,276 194,266 190,262 C188,256 192,250 198,250 Z', 'white', 1.3)
    if show('large intestine'):
        o += path('M118,330 L118,262 Q118,252 128,252 L192,252 Q202,252 202,262 L202,322 Q202,332 190,334 L172,336 L168,350', w=7)
        o += path('M118,330 L118,262 Q118,252 128,252 L192,252 Q202,252 202,262 L202,322 Q202,332 190,334 L172,336 L168,350', w=4.4, dash=None).replace(f'stroke="{INK}"', 'stroke="white"')
    if show('small intestine'):
        o += path('M136,268 q12,-8 24,0 t24,0 M134,282 q14,8 26,0 t26,0 M136,296 q12,-8 24,0 t24,0 M134,310 q14,8 26,0 t24,0 M140,322 q10,-6 20,0 t20,0', w=1.6)
    if show('bladder'):
        o += ellipse(160, 344, 13, 9, LIGHT, 1.4)
        if show('kidneys'):
            o += path('M124,276 Q132,320 152,340 M196,276 Q188,320 168,340', w=1)
    return o


def body_systems(which='all', points=(), labels=None, w='100%'):
    """Body outline with chosen organs. points: [(n, tx, ty, px, py)] callouts."""
    o = body_outline() + organs(which)
    for n, tx, ty, px, py in points:
        o += callout(n, tx, ty, px, py, labels)
    return svg(540, 370, f'<g transform="translate(100 0)">{o}</g>', width=w)


ORGANS = ['brain', 'lungs', 'heart', 'liver', 'stomach', 'kidneys', 'small intestine', 'large intestine', 'bladder']
ORGAN_POINTS = [(1, 0, 40, 150, 40), (2, 0, 150, 122, 170), (3, 320, 140, 178, 160), (4, 0, 225, 116, 226),
                (5, 320, 230, 196, 236), (6, 320, 268, 200, 262), (7, 320, 300, 170, 296), (8, 0, 300, 118, 300),
                (9, 0, 344, 150, 344)]
ORGAN_SET = {'brain', 'windpipe', 'lungs', 'heart', 'liver', 'stomach', 'kidneys', 'small intestine', 'large intestine', 'bladder'}


def organ_diagram(labels=None, w='100%'):
    return body_systems(ORGAN_SET, ORGAN_POINTS, labels, w)


def skeleton(labels=None, w='100%'):
    """Simplified skeleton. 1 skull, 2 ribs, 3 spine (backbone), 4 pelvis, 5 femur (thigh bone), 6 arm bones."""
    o = ellipse(120, 40, 26, 30, 'white', 1.8) + circle(110, 38, 5, GREY, 1) + circle(130, 38, 5, GREY, 1) + path('M110,56 L130,56', w=1.4)
    o += path('M108,66 L132,66 L130,74 L110,74 Z', 'white', 1.3)
    for i in range(14):
        o += rect(115, 78 + i * 12, 10, 9, 2, LIGHT, 1.1)
    for i in range(6):
        y = 96 + i * 13
        o += path(f'M115,{y} C90,{y - 4} 80,{y + 10} 86,{y + 16}', w=1.4) + path(f'M125,{y} C150,{y - 4} 160,{y + 10} 154,{y + 16}', w=1.4)
    o += path('M90,86 L70,90 M150,86 L170,90', w=2)
    o += path('M68,92 L56,170 M60,170 L50,240 M172,92 L184,170 M180,170 L190,240', w=4) + path('M68,92 L56,170 M60,170 L50,240 M172,92 L184,170 M180,170 L190,240', w=1.6).replace(INK, 'white', 1)
    o += path('M92,250 C88,230 104,220 120,232 C136,220 152,230 148,250 C140,262 100,262 92,250 Z', LIGHT, 1.5)
    o += path('M104,260 L96,350 M136,260 L144,350 M96,352 L92,420 M144,352 L148,420', w=4.2) + path('M104,260 L96,350 M136,260 L144,350 M96,352 L92,420 M144,352 L148,420', w=1.6).replace(INK, 'white', 1)
    for (x, y) in ((56, 170), (184, 170), (96, 351), (144, 351)):
        o += circle(x, y, 4, 'white', 1.3)
    for n, tx, ty, px, py in ((1, 210, 30, 144, 34), (2, 210, 110, 150, 108), (3, 30, 130, 116, 140), (4, 210, 245, 146, 246),
                              (5, 210, 310, 140, 310), (6, 30, 205, 56, 205)):
        o += callout(n, tx, ty, px, py, labels)
    return svg(410, 430, f'<g transform="translate(80 0)">{o}</g>', width=w)


SKELETON_PARTS = ['skull', 'ribs', 'spine (backbone)', 'pelvis', 'thigh bone (femur)', 'arm bones']


def heart_lungs_loop(w='100%'):
    """Schematic double circulation: lungs (top), heart (centre), body (bottom)."""
    o = rect(120, 10, 160, 50, 12, LIGHT, 1.6) + text(200, 40, 'LUNGS', 13, weight='bold')
    o += rect(120, 250, 160, 50, 12, LIGHT, 1.6) + text(200, 280, 'BODY', 13, weight='bold')
    o += path('M200,110 C215,96 244,104 238,130 C234,150 214,162 200,178 C186,162 166,150 162,130 C156,104 185,96 200,110 Z', GREY, 1.8)
    o += text(200, 140, 'HEART', 12, weight='bold')
    o += curved_arrow(170, 108, 120, 80, 150, 62) + curved_arrow(250, 62, 280, 80, 232, 110)
    o += curved_arrow(176, 168, 110, 210, 150, 248) + curved_arrow(250, 248, 290, 210, 226, 168)
    o += text(90, 86, 'blood picks up', 10) + text(90, 99, 'oxygen', 10)
    o += text(318, 86, 'oxygen-rich', 10) + text(318, 99, 'blood returns', 10)
    o += text(80, 220, 'heart pumps', 10) + text(80, 233, 'blood to body', 10)
    o += text(322, 220, 'body uses oxygen;', 10) + text(322, 233, 'blood returns', 10)
    return svg(400, 310, o, width=w)


def pulse_check(w='100%'):
    """Two fingers on the wrist to find the pulse."""
    o = path('M20,90 C60,80 140,78 230,86 L232,120 C140,126 60,124 20,118 Z', 'white', 1.6)
    o += path('M120,40 C150,30 190,40 214,70 L224,90 L208,96 L194,72 C178,58 160,56 140,64 Z', 'white', 1.6)
    o += path('M140,60 C170,52 200,66 214,88', w=1)
    o += line(150, 98, 220, 98, 1, dash='3 3') + text(150, 145, 'feel the pulse here, below the thumb', 11)
    return svg(260, 150, o, width=w)


# ------------------------------------------------------------------ cells
def animal_cell(labels=None, w='100%'):
    """1 cell membrane, 2 cytoplasm, 3 nucleus."""
    o = path('M40,90 C30,40 90,14 150,22 C214,30 250,70 236,120 C224,170 160,186 100,176 C56,168 46,130 40,90 Z', LIGHT, 1.8)
    o += circle(140, 96, 26, GREY, 1.6) + circle(146, 92, 7, 'white', 1)
    for (x, y) in ((80, 70), (90, 130), (190, 140), (196, 70), (110, 150), (176, 50)):
        o += ellipse(x, y, 6, 3, 'white', 0.9)
    for n, tx, ty, px, py in ((1, 270, 40, 214, 50), (2, 270, 160, 190, 126), (3, 270, 100, 160, 96)):
        o += callout(n, tx, ty, px, py, labels)
    return svg(380, 195, o, width=w)


CELL_PARTS = ['cell membrane', 'cytoplasm', 'nucleus']


def specialised_cells(names=True, w='100%'):
    """Five specialised human cells side by side: red blood cell, nerve cell, muscle cell, fat cell, skin cells."""
    o = ''
    # red blood cell (top view + side view)
    o += circle(60, 70, 34, LIGHT, 1.6) + circle(60, 70, 15, 'white', 1.0)
    o += path('M32,128 C40,118 52,124 60,124 C68,124 80,118 88,128 C80,138 68,132 60,132 C52,132 40,138 32,128 Z', LIGHT, 1.3)
    # nerve cell
    nx = 180
    o += circle(nx, 50, 14, GREY, 1.5) + circle(nx, 50, 4, INK, 0)
    for a in range(0, 360, 50):
        r = math.radians(a)
        o += path(f'M{nx + 14 * math.cos(r):.1f},{50 + 14 * math.sin(r):.1f} l{12 * math.cos(r):.1f},{12 * math.sin(r):.1f} l{6 * math.cos(r + 0.6):.1f},{6 * math.sin(r + 0.6):.1f}', w=1)
    o += path(f'M{nx},64 C{nx + 6},90 {nx - 6},110 {nx},140', w=1.6)
    for y in (82, 98, 114):
        o += rect(nx - 4, y, 8, 10, 3, 'white', 1)
    o += path(f'M{nx},140 l-10,10 M{nx},140 l10,10 M{nx},140 l0,12', w=1)
    # muscle cell (long fibre with stripes)
    o += rect(250, 40, 110, 26, 13, LIGHT, 1.5)
    for x in range(262, 352, 8):
        o += line(x, 42, x, 64, 0.8)
    o += ellipse(290, 53, 5, 3, INK, 0) + ellipse(330, 53, 5, 3, INK, 0)
    o += rect(260, 90, 90, 22, 11, LIGHT, 1.3)
    for x in range(270, 344, 8):
        o += line(x, 92, x, 110, 0.8)
    # fat cell
    o += circle(440, 80, 42, 'white', 1.6) + circle(440, 84, 34, LIGHT, 1.0) + ellipse(410, 52, 9, 5, GREY, 1.2, -30)
    # skin cells (layers)
    for row in range(4):
        for col in range(4):
            o += rect(510 + col * 26 + (13 if row % 2 else 0), 36 + row * 20, 26, 20, 3, 'white' if row < 2 else LIGHT, 1.1)
            o += circle(523 + col * 26 + (13 if row % 2 else 0), 46 + row * 20, 2.5, INK, 0)
    if names:
        for x, nm in ((60, 'red blood cell'), (180, 'nerve cell'), (305, 'muscle cells'), (440, 'fat cell'), (570, 'skin cells')):
            o += text(x, 175, nm, 12, weight='bold')
    else:
        for i, x in enumerate((60, 180, 305, 440, 570)):
            o += text(x, 175, chr(65 + i), 14, weight='bold')
    return svg(640, 185, o, width=w)


def organisation_levels(labels=True, w='100%'):
    """cell -> tissue -> organ -> organ system -> organism (stepped boxes)."""
    names = ['cell', 'tissue', 'organ', 'organ system', 'organism']
    o = ''
    for i in range(5):
        x = 10 + i * 128
        o += rect(x, 20, 112, 112, 12, 'white', 1.6)
        cx, cy = x + 56, 76
        if i == 0:
            o += circle(cx, cy, 22, LIGHT, 1.4) + circle(cx + 4, cy - 2, 8, GREY, 1)
        elif i == 1:
            for r in range(3):
                for c in range(4):
                    o += rect(cx - 40 + c * 20, cy - 26 + r * 18, 20, 18, 3, LIGHT, 1) + circle(cx - 30 + c * 20, cy - 17 + r * 18, 2.2, INK, 0)
        elif i == 2:
            o += path(f'M{cx},{cy - 14} C{cx + 10},{cy - 30} {cx + 36},{cy - 22} {cx + 30},{cy + 2} C{cx + 26},{cy + 18} {cx + 10},{cy + 26} {cx},{cy + 36} C{cx - 10},{cy + 26} {cx - 26},{cy + 18} {cx - 30},{cy + 2} C{cx - 36},{cy - 22} {cx - 10},{cy - 30} {cx},{cy - 14} Z', GREY, 1.5)
        elif i == 3:
            o += path(f'M{cx},{cy - 6} C{cx + 6},{cy - 16} {cx + 20},{cy - 12} {cx + 16},{cy + 2} C{cx + 14},{cy + 10} {cx + 6},{cy + 14} {cx},{cy + 20} C{cx - 6},{cy + 14} {cx - 14},{cy + 10} {cx - 16},{cy + 2} C{cx - 20},{cy - 12} {cx - 6},{cy - 16} {cx},{cy - 6} Z', GREY, 1.3)
            o += path(f'M{cx - 10},{cy - 10} C{cx - 40},{cy - 40} {cx - 40},{cy + 40} {cx - 8},{cy + 18} M{cx + 10},{cy - 10} C{cx + 40},{cy - 40} {cx + 40},{cy + 40} {cx + 8},{cy + 18}', w=1.3)
            o += path(f'M{cx - 36},{cy - 34} L{cx - 36},{cy + 40} M{cx + 36},{cy - 34} L{cx + 36},{cy + 40}', w=0.9, dash='3 3')
        else:
            o += circle(cx, cy - 30, 10, 'white', 1.4) + line(cx, cy - 20, cx, cy + 12, 1.6)
            o += line(cx, cy - 12, cx - 18, cy + 4, 1.6) + line(cx, cy - 12, cx + 18, cy + 4, 1.6)
            o += line(cx, cy + 12, cx - 12, cy + 40, 1.6) + line(cx, cy + 12, cx + 12, cy + 40, 1.6)
        if i < 4:
            o += arrow(x + 113, 76, x + 127, 76, 1.8, 7)
        o += text(cx, 152, names[i] if labels else '', 13, weight='bold')
        if not labels:
            o += marker(i + 1, cx, 150)
    return svg(650, 165, o, width=w)


ORGANISATION = ['cell', 'tissue', 'organ', 'organ system', 'organism']


def microscope(w='100%'):
    o = path('M60,250 L180,250 L170,232 L70,232 Z', GREY, 1.6)
    o += path('M150,232 C170,180 170,120 130,80', w=10) + path('M150,232 C170,180 170,120 130,80', w=6).replace(INK, 'white', 1)
    o += rect(60, 150, 90, 8, 2, 'white', 1.6)
    o += path('M92,150 L100,110 L116,110 L124,150', 'white', 1.4)
    o += rect(96, 40, 26, 72, 4, 'white', 1.6) + rect(90, 30, 38, 12, 3, GREY, 1.4)
    o += circle(150, 120, 9, 'white', 1.4) + circle(150, 120, 3, INK, 0)
    o += ellipse(108, 200, 18, 5, LIGHT, 1.2)
    for n, tx, ty, px, py, lab in ((1, 210, 34, 128, 36, 'eyepiece lens'), (2, 210, 140, 116, 140, 'objective lens'),
                                   (3, 210, 156, 148, 154, 'stage (slide goes here)'), (4, 210, 120, 158, 120, 'focus knob'),
                                   (5, 210, 200, 126, 200, 'light / mirror')):
        o += callout(n, tx, ty, px, py, [lab] * 5)
    return svg(360, 260, o, width=w)


# ------------------------------------------------------------------ health
def mosquito_cycle(labels=True, w='100%'):
    """Aedes mosquito life cycle: egg -> larva -> pupa -> adult (water line)."""
    o = rect(0, 110, 560, 80, 0, LIGHT, 0) + path('M0,110 q20,-6 40,0 t40,0 t40,0 t40,0 t40,0 t40,0 t40,0 t40,0 t40,0 t40,0 t40,0 t40,0 t40,0 t40,0', w=1.4)
    # eggs on container wall
    o += rect(20, 60, 90, 130, 4, 'none', 1.6)
    for i in range(6):
        o += ellipse(40 + i * 10, 104, 3, 1.6, INK, 0.5)
    # larva
    o += path('M180,118 q6,14 0,28 q-6,14 0,28', w=4) + path('M180,118 l-6,-8 l12,0 Z', w=1.2)
    # pupa
    o += path('M300,120 C330,116 336,140 320,150 C312,160 300,154 298,146 C296,136 296,126 300,120 Z', GREY, 1.4)
    o += path('M322,150 q8,10 0,20', w=1.4)
    # adult mosquito
    ax, ay = 460, 60
    o += ellipse(ax, ay, 26, 6, GREY, 1.4) + circle(ax - 30, ay - 2, 6, 'white', 1.4) + line(ax - 36, ay - 2, ax - 56, ay + 6, 1.2)
    for dx in (-10, 0, 10):
        o += path(f'M{ax + dx},{ay + 4} l-10,26 M{ax + dx},{ay + 4} l12,26', w=1)
    o += ellipse(ax - 4, ay - 18, 22, 8, 'white', 1.2, -20) + ellipse(ax + 10, ay - 16, 20, 7, 'white', 1.2, 15)
    for i in range(5):
        o += line(ax - 18 + i * 9, ay - 4, ax - 18 + i * 9, ay + 4, 1.8)
    for x1, x2, y in ((112, 160, 150), (205, 285, 150), (338, 420, 120)):
        o += arrow(x1, y, x2, y, 1.8, 9)
    o += curved_arrow(430, 30, 230, -20, 70, 56, 1.4, 9, '6 4')
    if labels:
        for x, t in ((65, 'eggs'), (182, 'larva'), (318, 'pupa'), (460, 'adult')):
            o += text(x, 210, t, 13, weight='bold')
        o += text(250, 20, 'female lays eggs near water', 11, italic=True)
    return svg(560, 220, o, width=w)


def handwash_steps(w='100%'):
    """Six simple steps as numbered boxes with icons drawn as text-free hand shapes."""
    steps = ['Wet hands', 'Add soap', 'Rub palms, backs and between fingers', 'Scrub nails and thumbs', 'Rinse well', 'Dry with a clean cloth']
    o = ''
    for i, s in enumerate(steps):
        x = 6 + i * 104
        o += rect(x, 6, 96, 120, 10, 'white', 1.4) + marker(i + 1, x + 14, 20)
        o += path(f'M{x + 30},{80} C{x + 30},{56} {x + 66},{56} {x + 66},{80} L{x + 66},{96} L{x + 30},{96} Z', LIGHT, 1.3)
        for k in range(4):
            o += line(x + 34 + k * 9, 74, x + 34 + k * 9, 52, 3) + line(x + 34 + k * 9, 74, x + 34 + k * 9, 52, 1.2, color='white')
        if i in (0, 4):
            for k in range(3):
                o += path(f'M{x + 40 + k * 8},34 q-3,6 0,8 q3,-2 0,-8', LIGHT, 1)
        if i == 1:
            o += circle(x + 74, 40, 5, 'white', 1) + circle(x + 82, 32, 3, 'white', 1)
        words = s.split(' ')
        line1, line2 = ' '.join(words[:3]), ' '.join(words[3:])
        o += text(x + 48, 112, line1, 9.5) + (text(x + 48, 123, line2, 9.5) if line2 else '')
    return svg(630, 132, o, width=w)


# ------------------------------------------------------------------ nutrition
def healthy_plate(labels=True, w='100%'):
    """Plate divided: half vegetables & fruit, quarter grains, quarter protein; glass of water and milk."""
    cx, cy, r = 190, 150, 120
    o = circle(cx, cy, r + 12, 'white', 1.6) + circle(cx, cy, r, 'white', 1.6)
    o += line(cx, cy - r, cx, cy + r, 1.6) + line(cx, cy, cx + r, cy, 1.6)
    o += f'<path d="M{cx},{cy - r} A{r},{r} 0 0 0 {cx},{cy + r} Z" fill="{LIGHT}"/>'
    o += circle(cx, cy, r, 'none', 1.6) + line(cx, cy - r, cx, cy + r, 1.6) + line(cx, cy, cx + r, cy, 1.6)
    # small drawings
    o += leaf(96, 176, 30, -40, GREY) + leaf(120, 206, 28, 200, 'white') + circle(150, 186, 13, 'white', 1.3) + circle(104, 222, 10, GREY, 1.2)
    for i in range(10):
        o += ellipse(225 + (i % 5) * 12, 74 + (i // 5) * 10, 5, 3, 'white', 0.9)
    o += path('M216,200 C236,186 276,188 286,204 C276,216 236,218 216,204 Z', 'white', 1.3) + circle(278, 202, 2, INK, 0) + path('M216,204 l-12,-8 l0,16 Z', 'white', 1.2)
    if labels:
        o += text(130, 100, 'Vegetables', 13, weight='bold') + text(130, 115, 'and fruit', 13, weight='bold') + text(130, 134, '(half the plate)', 10, italic=True)
        o += text(250, 112, 'Grains', 13, weight='bold') + text(250, 126, 'rice, roti', 11)
        o += text(250, 176, 'Protein', 13, weight='bold') + text(250, 232, 'fish, egg,', 10) + text(250, 244, 'dal, meat', 10)
    # glass of water + milk
    o += path('M360,60 L392,60 L388,130 L364,130 Z', 'white', 1.6) + path('M361,80 L391,80', w=1, dash='3 3')
    o += path('M410,80 L440,80 L436,140 L414,140 Z', LIGHT, 1.6)
    if labels:
        o += text(376, 150, 'water', 12, weight='bold') + text(425, 160, 'milk', 12, weight='bold')
    return svg(470, 290, o, width=w)


# ------------------------------------------------------------------ ecosystems
def food_web(numbered=False, w='100%'):
    """A Sundarbans food web as labelled boxes with arrows (arrow = 'is eaten by', energy flow)."""
    nodes = {
        'sun': (330, 24, 'Sun'), 'mangrove': (120, 290, 'mangrove leaves'), 'algae': (520, 290, 'algae (in water)'),
        'deer': (70, 170, 'spotted deer'), 'crab': (250, 200, 'crab'), 'shrimp': (450, 200, 'shrimp'),
        'fish': (560, 120, 'fish'), 'monkey': (200, 110, 'monkey'), 'tiger': (110, 40, 'tiger'),
        'kingfisher': (470, 60, 'kingfisher'), 'otter': (330, 120, 'otter'),
    }
    links = [('mangrove', 'deer'), ('mangrove', 'monkey'), ('mangrove', 'crab'), ('algae', 'shrimp'), ('algae', 'fish'),
             ('shrimp', 'fish'), ('crab', 'otter'), ('fish', 'otter'), ('fish', 'kingfisher'), ('shrimp', 'kingfisher'),
             ('deer', 'tiger'), ('monkey', 'tiger')]
    o = ''
    for a, b in links:
        x1, y1, _ = nodes[a]
        x2, y2, _ = nodes[b]
        d = math.hypot(x2 - x1, y2 - y1)
        ux, uy = (x2 - x1) / d, (y2 - y1) / d
        o += arrow(x1 + ux * 30, y1 + uy * 16, x2 - ux * 34, y2 - uy * 18, 1.5, 8)
    for k, (x, y, name) in nodes.items():
        if k == 'sun':
            continue
        wbox = max(70, len(name) * 7 + 16)
        o += rect(x - wbox / 2, y - 14, wbox, 28, 8, LIGHT if k in ('mangrove', 'algae') else 'white', 1.4)
        o += text(x, y + 4, name, 11.5, weight='bold')
    o += circle(330, 24, 14, 'white', 1.4)
    for a in range(0, 360, 45):
        r = math.radians(a)
        o += line(330 + 17 * math.cos(r), 24 + 17 * math.sin(r), 330 + 23 * math.cos(r), 24 + 23 * math.sin(r), 1.2)
    o += arrow(316, 34, 140, 272, 1, 7, '4 4') + arrow(344, 34, 506, 272, 1, 7, '4 4')
    o += text(330, 330, 'Arrows show the direction energy moves: from the food to the animal that eats it.', 11, italic=True)
    return svg(640, 340, o, width=w)


def quadrat(w='100%'):
    """A 1 m quadrat (frame) with plants counted inside."""
    o = rect(20, 20, 200, 200, 0, 'white', 2.4)
    for i in range(1, 4):
        o += line(20 + i * 50, 20, 20 + i * 50, 220, 0.6, '3 3') + line(20, 20 + i * 50, 220, 20 + i * 50, 0.6, '3 3')
    pts = [(50, 50), (80, 130), (150, 60), (190, 180), (60, 190), (120, 100), (170, 120)]
    for x, y in pts:
        o += simple_flower(x, y, 6, 5)
    for x, y in ((100, 40), (40, 110), (140, 180), (200, 80), (110, 160)):
        o += leaf(x, y, 16, -60, GREY, False) + leaf(x, y, 16, -120, GREY, False)
    o += text(120, 240, '1 metre × 1 metre quadrat', 11, italic=True)
    return svg(240, 250, o, width=w)


# ------------------------------------------------------------------ earth: water
def sun_icon(x, y, r=18):
    o = circle(x, y, r, 'white', 1.6)
    for a in range(0, 360, 30):
        t = math.radians(a)
        o += line(x + (r + 4) * math.cos(t), y + (r + 4) * math.sin(t), x + (r + 12) * math.cos(t), y + (r + 12) * math.sin(t), 1.4)
    return o


def cloud(x, y, s=1.0, fill='white'):
    return (f'<g transform="translate({x} {y}) scale({s})">' + path(
        'M-40,10 C-56,10 -56,-14 -38,-14 C-36,-32 -10,-36 0,-22 C10,-38 40,-32 38,-12 C56,-12 56,10 40,10 Z', fill, 1.6) + '</g>')


def water_cycle(labels=None, w='100%'):
    """1 evaporation, 2 condensation, 3 precipitation, 4 collection (run-off), 5 transpiration."""
    o = rect(0, 250, 300, 70, 0, LIGHT, 0)
    for i in range(8):
        o += path(f'M{i * 40},258 q10,-5 20,0 t20,0', w=1)
    o += path('M300,320 L300,240 L360,170 L420,120 L470,150 L520,110 L620,200 L620,320 Z', 'white', 1.6)
    o += path('M300,240 C320,250 360,262 300,270', w=1)
    o += path('M420,122 L432,140 L446,132 L470,150', w=1.2)
    o += path('M380,250 C420,240 460,250 520,236 C470,262 420,270 300,268', LIGHT, 1.2)
    o += sun_icon(60, 50)
    o += cloud(240, 70, 1.1, LIGHT) + cloud(470, 60, 1.0, LIGHT)
    for (x, y) in ((450, 85), (465, 95), (480, 85), (495, 95), (510, 85)):
        o += line(x, y, x - 6, y + 14, 1.2)
    o += seedling(360, 170, 30, 4)
    for x in (90, 140, 190):
        o += path(f'M{x},244 q-8,-20 0,-40 q8,-20 0,-40', w=1.2, dash='3 4')
    o += arrow(190, 120, 190, 104, 1.2, 7) + arrow(140, 128, 140, 112, 1.2, 7) + arrow(90, 120, 90, 104, 1.2, 7)
    o += arrow(300, 66, 400, 58, 1.8, 9)
    o += arrow(480, 120, 470, 190, 1.8, 9)
    o += curved_arrow(560, 210, 480, 260, 320, 262, 1.8, 9)
    o += path('M360,140 q-6,-14 0,-28', w=1, dash='3 3') + arrow(360, 116, 362, 104, 1, 6)
    for n, tx, ty, px, py in ((1, 30, 150, 90, 160), (2, 250, 18, 260, 60), (3, 560, 70, 488, 100), (4, 610, 290, 470, 250), (5, 300, 110, 358, 128)):
        o += callout(n, tx, ty, px, py, labels)
    return svg(820, 325, f'<g transform="translate(95 0)">{o}</g>', width=w)


WATER_CYCLE = ['evaporation', 'condensation', 'precipitation', 'collection', 'transpiration']


def solar_still(labels=None, w='100%'):
    """1 salty water, 2 plastic sheet, 3 small stone, 4 cup, 5 clean water, 6 sunlight."""
    o = path('M40,120 L60,200 L300,200 L320,120', 'white', 1.8)
    o += path('M48,150 L312,150 L300,198 L60,198 Z', LIGHT, 0)
    o += line(48, 150, 312, 150, 1.2)
    o += rect(150, 140, 60, 58, 3, 'white', 1.6) + rect(152, 176, 56, 20, 0, GREY, 0)
    o += path('M30,118 Q180,186 330,118', w=1.4) + circle(180, 152, 7, GREY, 1.3)
    for x in (100, 260):
        o += path(f'M{x},160 q-5,-10 0,-20', w=1, dash='2 3')
    for x in (130, 230):
        o += path(f'M{x},136 l18,10', w=1) + circle(x + 22, 148, 2.2, INK, 0)
    o += sun_icon(330, 40, 14)
    for n, tx, ty, px, py in ((1, 20, 190, 80, 180), (2, 20, 100, 70, 132), (3, 360, 110, 186, 150), (4, 360, 170, 210, 170), (5, 360, 200, 200, 188), (6, 360, 40, 314, 50)):
        o += callout(n, tx, ty, px, py, labels)
    return svg(560, 215, f'<g transform="translate(95 0)">{o}</g>', width=w)


SOLAR_STILL = ['salty water', 'clear plastic sheet', 'small stone', 'cup', 'clean water', 'sunlight']


# ------------------------------------------------------------------ earth: soil
def soil_layers(labels=None, w='100%'):
    """1 leaf litter/humus, 2 topsoil, 3 subsoil, 4 bedrock."""
    o = rect(60, 20, 260, 30, 0, GREY, 1.4)
    for i in range(12):
        o += leaf(72 + i * 20, 34 + (i % 2) * 6, 12, -20 + (i % 3) * 30, 'white', False)
    o += rect(60, 50, 260, 70, 0, LIGHT, 1.4)
    for i in range(40):
        o += circle(66 + (i * 37) % 250, 58 + (i * 23) % 56, 1.6, INK, 0)
    o += path('M140,70 q10,10 30,4 q16,-6 30,6', w=3.2)
    o += rect(60, 120, 260, 70, 0, 'white', 1.4)
    for i in range(14):
        o += ellipse(76 + (i * 41) % 236, 136 + (i * 17) % 46, 7, 5, 'white', 1)
    o += rect(60, 190, 260, 50, 0, GREY, 1.4)
    o += path('M60,210 L120,200 L180,214 L250,198 L320,212 M100,240 L140,214 M220,240 L250,198', w=1.2)
    o += path('M180,20 Q176,80 184,150', w=1.2) + path('M184,90 Q200,110 214,120 M182,60 Q166,74 158,92', w=1)
    for n, tx, ty, px, py in ((1, 340, 34, 300, 34), (2, 340, 84, 300, 84), (3, 340, 154, 300, 154), (4, 340, 216, 300, 216)):
        o += callout(n, tx, ty, px, py, labels)
    return svg(470, 250, o, width=w)


SOIL_LAYERS = ['leaf litter (humus)', 'topsoil', 'subsoil', 'bedrock']


def earthworm(x=0, y=0, s=1.0):
    o = path('M0,20 C20,0 40,40 60,20 C80,0 100,40 120,20', w=9) + path('M0,20 C20,0 40,40 60,20 C80,0 100,40 120,20', w=6).replace(INK, 'white', 1)
    for i in range(1, 12):
        t = i / 12
        xx = 120 * t
        yy = 20 + 14 * math.sin(t * 2 * math.pi * 1.5 + math.pi) * 0.9
        o += line(xx, yy - 3, xx + 1, yy + 3, 0.8)
    o += ellipse(34, 16, 7, 6, GREY, 1)
    return f'<g transform="translate({x} {y}) scale({s})">{o}</g>'


def funnel_test(names=('sand', 'garden soil', 'clay'), w='100%'):
    o = ''
    for i, nm in enumerate(names):
        x = 20 + i * 150
        o += path(f'M{x},20 L{x + 100},20 L{x + 58},76 L{x + 58},100 L{x + 42},100 L{x + 42},76 Z', 'white', 1.6)
        o += path(f'M{x + 10},30 L{x + 90},30 L{x + 56},70 L{x + 44},70 Z', GREY if i == 2 else LIGHT, 1)
        o += rect(x + 20, 104, 60, 80, 3, 'white', 1.6)
        lvl = (60, 40, 14)[i]
        o += rect(x + 22, 182 - lvl, 56, lvl, 0, LIGHT, 0) + line(x + 22, 182 - lvl, x + 78, 182 - lvl, 1)
        for k in range(4):
            o += line(x + 20, 120 + k * 16, x + 30, 120 + k * 16, 0.8)
        o += text(x + 50, 204, nm, 12, weight='bold')
    return svg(470, 212, o, width=w)


def soil_key(w='100%'):
    """Dichotomous key for five soil types."""
    def box(x, y, t1, t2=''):
        b = rect(x - 78, y - 18, 156, 38 if t2 else 28, 8, 'white', 1.4) + text(x, y + (0 if t2 else 2), t1, 11, weight='bold')
        if t2:
            b += text(x, y + 13, t2, 11, weight='bold')
        return b

    def leafbox(x, y, t):
        return rect(x - 60, y - 14, 120, 28, 14, LIGHT, 1.6) + text(x, y + 4, t, 12, weight='bold')
    o = box(330, 26, 'Is the soil gritty', 'when you rub it?')
    o += box(170, 104, 'Does it fizz with', 'vinegar? (pale, stony)') + box(490, 104, 'Is it sticky and', 'shiny when wet?')
    o += leafbox(90, 186, 'sandy soil') + leafbox(250, 186, 'chalky soil') + box(570, 186, 'Is it dark and full', 'of rotting leaves?') + leafbox(410, 186, 'clay soil')
    o += leafbox(500, 262, 'woodland soil') + leafbox(640, 262, 'garden topsoil')
    for (x1, y1, x2, y2, t) in ((300, 46, 200, 84, 'yes'), (360, 46, 460, 84, 'no'), (140, 124, 100, 170, 'no'), (200, 124, 240, 170, 'yes'),
                                (460, 124, 420, 170, 'yes'), (520, 124, 560, 166, 'no'), (540, 206, 510, 248, 'yes'), (600, 206, 630, 248, 'no')):
        o += arrow(x1, y1, x2, y2, 1.4, 7) + text((x1 + x2) / 2 + (-12 if x2 < x1 else 12), (y1 + y2) / 2, t, 10, italic=True)
    return svg(720, 280, o, width=w)


# ------------------------------------------------------------------ earth: surface
def river_landscape(labels=None, w='100%'):
    """Mountains to sea: 1 weathering of rock, 2 erosion by river, 3 deposition (delta), 4 sea."""
    o = line(0, 200, 470, 200, 1.4)
    o += path('M0,200 L50,90 L90,140 L150,40 L210,130 L250,170 L290,200 Z', 'white', 1.6)
    o += path('M136,60 L150,40 L166,62 L156,56 L146,64 Z', LIGHT, 1.2)
    for (x, y) in ((78, 124), (88, 132), (70, 132), (96, 140)):
        o += path(f'M{x},{y} l7,-5 l5,7 Z', GREY, 1)
    river = 'M160,70 C176,120 200,150 240,176 C280,200 330,190 380,212 C420,228 450,232 480,236'
    o += path(river, w=8) + path(river, w=4.6).replace(INK, 'white', 1)
    o += path('M470,200 L640,200 L640,270 L470,270 Z', LIGHT, 1.4)
    o += path('M476,232 C500,236 510,250 504,264 C520,256 540,246 556,232 C540,242 516,244 500,238', GREY, 1.3)
    for i in range(5):
        o += path(f'M{560 + i * 16},{222 + (i % 2) * 14} q6,-4 12,0', w=1)
    o += text(560, 290, '', 10)
    for n, tx, ty, px, py in ((1, 200, 26, 84, 128), (2, 300, 120, 236, 172), (3, 560, 150, 506, 244), (4, 610, 182, 600, 214)):
        o += callout(n, tx, ty, px, py, labels)
    return svg(720, 280, f'<g transform="translate(40 0)">{o}</g>', width=w)


RIVER_PARTS = ['weathering (rock breaks up)', 'erosion (river carries rock and soil)', 'deposition (delta forms)', 'sea']


def erosion_trays(w='100%'):
    """Two sloping trays of soil, one bare and one with grass, watered from a can; collecting cups."""
    o = ''
    for i, (title, grass) in enumerate((('bare soil', False), ('soil with grass', True))):
        x = 20 + i * 300
        o += path(f'M{x},120 L{x + 200},160 L{x + 200},176 L{x},136 Z', LIGHT, 1.6)
        o += path(f'M{x},120 L{x},146 L{x + 14},150', w=1.4)
        if grass:
            for k in range(16):
                gx = x + 6 + k * 12
                gy = 120 + (gx - x) * 0.2
                o += path(f'M{gx},{gy} l-2,-10 M{gx},{gy} l3,-11 M{gx},{gy} l7,-8', w=0.9)
        o += path(f'M{x + 10},60 L{x + 70},60 L{x + 64},96 L{x + 16},96 Z', 'white', 1.6) + path(f'M{x + 70},70 L{x + 100},52', w=3)
        for k in range(5):
            o += line(x + 100 + k * 4, 56 + k * 5, x + 96 + k * 4, 70 + k * 5, 1, dash='2 3')
        o += path(f'M{x + 204},170 L{x + 250},170 L{x + 244},210 L{x + 210},210 Z', 'white', 1.6)
        lvl = 28 if not grass else 10
        o += rect(x + 212, 208 - lvl, 30, lvl, 0, GREY if not grass else LIGHT, 0)
        o += text(x + 110, 240, title, 13, weight='bold')
    return svg(620, 250, o, width=w)


def cyclone_shelter(w='100%'):
    o = line(0, 200, 380, 200, 1.6)
    o += rect(110, 40, 160, 70, 4, 'white', 1.8) + path('M100,40 L190,10 L280,40 Z', LIGHT, 1.6)
    for x in (130, 170, 210, 240):
        o += rect(x, 58, 18, 22, 1, LIGHT, 1.2)
    for x in (120, 175, 225, 262):
        o += rect(x - 4, 110, 8, 90, 0, GREY, 1.4)
    o += path('M280,110 L340,200', w=1.6) + path('M290,110 L350,200', w=1.6)
    for k in range(6):
        o += line(282 + k * 10, 122 + k * 15, 292 + k * 10, 122 + k * 15, 1.2)
    o += path('M0,170 q20,-8 40,0 t40,0 t40,0 t40,0 t40,0 t40,0 t40,0 t40,0 t40,0 t40,0', w=1.2, dash='5 4')
    o += text(60, 160, 'flood water', 10, italic=True) + text(190, 130, 'open ground floor', 10, italic=True)
    return svg(380, 210, o, width=w)


# ------------------------------------------------------------------ earth: space
def earth_globe(x, y, r=40, night='right', axis_tilt=23.5, show_axis=True):
    o = circle(x, y, r, 'white', 1.6)
    if night == 'right':
        o += f'<path d="M{x},{y - r} A{r},{r} 0 0 1 {x},{y + r} Z" fill="{GREY}"/>'
    elif night == 'left':
        o += f'<path d="M{x},{y - r} A{r},{r} 0 0 0 {x},{y + r} Z" fill="{GREY}"/>'
    o += circle(x, y, r, 'none', 1.6)
    o += path(f'M{x - r * 0.6},{y - r * 0.3} q{r * 0.3},{-r * 0.3} {r * 0.5},{0} q{r * 0.1},{r * 0.4} {-r * 0.3},{r * 0.5} Z', LIGHT, 1)
    if show_axis:
        t = math.radians(axis_tilt)
        dx, dy = (r + 14) * math.sin(t), (r + 14) * math.cos(t)
        o += line(x - dx, y + dy, x + dx, y - dy, 1.2, dash='5 3')
    return o


def day_night(w='100%'):
    o = sun_icon(60, 110, 34)
    for k in range(5):
        o += arrow(110, 70 + k * 20, 230, 70 + k * 20, 1.2, 7)
    o += earth_globe(320, 110, 70, 'right')
    o += curved_arrow(250, 30, 320, 0, 390, 30, 1.6, 9)
    o += text(270, 112, 'DAY', 13, weight='bold') + text(372, 112, 'NIGHT', 13, weight='bold')
    o += text(320, 205, 'The Earth spins on its axis once every 24 hours.', 11, italic=True)
    return svg(440, 215, o, width=w)


def seasons_orbit(w='100%'):
    o = ellipse(320, 175, 250, 110, 'none', 1.2)
    o += sun_icon(320, 175, 26)
    pos = [(70, 175, 'June', 'left'), (320, 65, 'September', None), (570, 175, 'December', 'right'), (320, 285, 'March', None)]
    for (x, y, m, night) in pos:
        o += earth_globe(x, y, 26, night or 'none', 23.5)
        if y == 175:
            o += text(x, y - 44, m, 12, weight='bold')
        else:
            o += text(x + 62, y + 4, m, 12, weight='bold')
    o += text(70, 226, 'Northern half tilted', 10) + text(70, 239, 'towards the Sun:', 10) + text(70, 252, 'summer in Bangladesh', 10)
    o += text(570, 226, 'Northern half tilted', 10) + text(570, 239, 'away from the Sun:', 10) + text(570, 252, 'winter in Bangladesh', 10)
    o += curved_arrow(470, 84, 520, 100, 548, 140, 1.4, 8)
    return svg(640, 330, o, width=w)


def sun_path(w='100%'):
    """Apparent path of the Sun across the sky from east to west, with stick shadows."""
    o = line(20, 220, 620, 220, 1.6)
    o += path('M60,220 Q320,-40 580,220', w=1.2, dash='5 5')
    for (t, x, y) in (('morning', 120, 120), ('midday', 320, 92), ('evening', 520, 120)):
        o += sun_icon(x, y - 30 if t == 'midday' else y, 12) + text(x, (y - 30 if t == 'midday' else y) - 26, t, 11, italic=True)
    o += line(320, 220, 320, 180, 3)
    o += line(320, 220, 470, 226, 6).replace(INK, '#999', 1) + text(470, 244, 'morning shadow (long, points west)', 10)
    o += line(320, 220, 334, 222, 6).replace(INK, '#555', 1)
    o += line(320, 220, 170, 226, 6).replace(INK, '#bbb', 1) + text(170, 244, 'evening shadow (long, points east)', 10)
    o += text(40, 210, 'EAST', 12, weight='bold') + text(600, 210, 'WEST', 12, weight='bold')
    return svg(640, 255, o, width=w)


def solar_system(numbered=False, w='100%'):
    names = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    radii = [4, 7, 7.5, 5, 22, 18, 12, 12]
    o = f'<path d="M0,10 A90,90 0 0 1 0,170 Z" fill="{LIGHT}" stroke="{INK}" stroke-width="1.6"/>' + text(30, 94, 'Sun', 13, weight='bold')
    x = 70
    for i, (nm, r) in enumerate(zip(names, radii)):
        x += r + 16
        o += circle(x, 90, r, GREY if i in (2, 4) else 'white', 1.4)
        if nm == 'Saturn':
            o += ellipse(x, 90, r + 12, 5, 'none', 1.2, -15)
        o += text(x, 90 + (r + 22) * (1 if i % 2 == 0 else -1) + (0 if i % 2 == 0 else 8), nm if not numbered else str(i + 1), 11, weight='bold')
        x += r
    o += text(330, 172, 'Not to scale: the distances are really much, much bigger.', 10, italic=True)
    return svg(660, 180, o, width=w)


PLANETS = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']


# ------------------------------------------------------------------ technology
def shadoof(w='100%'):
    o = line(0, 210, 420, 210, 1.6)
    o += path('M0,210 L0,180 L120,180 L130,210', LIGHT, 1.2) + text(60, 200, 'river', 10, italic=True)
    o += line(240, 210, 230, 100, 3) + line(260, 210, 270, 100, 3) + line(220, 100, 280, 100, 3)
    o += line(130, 60, 380, 130, 3.2) + circle(250, 96, 5, 'white', 1.4)
    o += ellipse(380, 136, 22, 16, GREY, 1.6) + text(380, 172, 'counterweight', 10, italic=True)
    o += line(132, 62, 132, 150, 1.2) + path('M118,150 L146,150 L142,176 L122,176 Z', 'white', 1.4)
    o += text(250, 228, 'pivot (fulcrum)', 10, italic=True)
    return svg(430, 236, o, width=w)


def windcatcher(w='100%'):
    o = rect(60, 120, 220, 100, 0, 'white', 1.8) + rect(200, 20, 50, 100, 0, 'white', 1.8)
    o += rect(206, 30, 38, 20, 0, LIGHT, 1.2) + line(225, 50, 225, 120, 1, '3 3')
    for k in range(3):
        o += arrow(300 - k * 4, 30 + k * 10, 250, 40 + k * 4, 1.4, 7)
    o += arrow(225, 60, 225, 150, 1.6, 8) + curved_arrow(220, 160, 150, 200, 90, 150, 1.4, 8)
    o += rect(70, 140, 30, 40, 0, LIGHT, 1.2) + arrow(80, 150, 40, 130, 1.4, 7)
    o += text(320, 24, 'wind', 11, italic=True) + text(140, 236, 'cool air flows through the house', 10, italic=True)
    o += text(30, 120, 'warm air out', 10, italic=True)
    return svg(340, 245, o, width=w)
