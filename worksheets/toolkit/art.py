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
