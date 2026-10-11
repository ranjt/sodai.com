"""Hand-drawn style icons for the thinking routine templates (original InquiryMind drawings, black and grey).
Each function returns an <svg> in a 100 x 100 box."""
import math
import os
import re

INK, GREY, LIGHT = '#111', '#cfcfcf', '#ececec'


def _svg(body):
    return (f'<svg class="rt-icon" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg" fill="none" stroke="{INK}" '
            f'stroke-width="4" stroke-linecap="round" stroke-linejoin="round">{body}</svg>')


def _sparkle(x, y, r=7):
    return (f'<path d="M{x},{y - r} Q{x + r * .18},{y - r * .18} {x + r},{y} Q{x + r * .18},{y + r * .18} {x},{y + r} '
            f'Q{x - r * .18},{y + r * .18} {x - r},{y} Q{x - r * .18},{y - r * .18} {x},{y - r} Z" fill="{INK}" stroke-width="1.5"/>')


def see():
    """An eye inside a magnifying glass: look closely."""
    return _svg(
        f'<line x1="63" y1="63" x2="88" y2="88" stroke-width="12"/><line x1="66" y1="66" x2="86" y2="86" stroke="{GREY}" stroke-width="5"/>'
        f'<circle cx="42" cy="42" r="29" fill="white"/><circle cx="42" cy="42" r="23" stroke="{LIGHT}" stroke-width="6"/>'
        f'<path d="M20,42 Q42,22 64,42 Q42,62 20,42 Z" fill="white" stroke-width="3.5"/>'
        f'<circle cx="42" cy="42" r="9" fill="{GREY}" stroke-width="3"/><circle cx="42" cy="42" r="4" fill="{INK}" stroke="none"/>'
        f'<circle cx="45" cy="39" r="1.8" fill="white" stroke="none"/>' + _sparkle(84, 16, 8) + _sparkle(16, 86, 5))


def think():
    """A light bulb with a turning gear inside: ideas at work."""
    rays = ''.join(f'<line x1="{50 + 36 * math.cos(math.radians(a)):.1f}" y1="{38 + 36 * math.sin(math.radians(a)):.1f}" '
                   f'x2="{50 + 45 * math.cos(math.radians(a)):.1f}" y2="{38 + 45 * math.sin(math.radians(a)):.1f}" stroke-width="4"/>'
                   for a in (-160, -125, -90, -55, -20))
    teeth = ''.join(f'<line x1="{50 + 9 * math.cos(math.radians(a)):.1f}" y1="{38 + 9 * math.sin(math.radians(a)):.1f}" '
                    f'x2="{50 + 13.5 * math.cos(math.radians(a)):.1f}" y2="{38 + 13.5 * math.sin(math.radians(a)):.1f}" stroke-width="5"/>'
                    for a in range(0, 360, 45))
    return _svg(
        rays + '<path d="M50,10 C31,10 21,25 23,40 C25,52 35,57 37,68 L63,68 C65,57 75,52 77,40 C79,25 69,10 50,10 Z" fill="white"/>'
        f'<path d="M50,16 C36,16 29,26 29,38" stroke="{LIGHT}" stroke-width="5"/>'
        + teeth + f'<circle cx="50" cy="38" r="9" fill="{GREY}" stroke-width="3.5"/><circle cx="50" cy="38" r="3" fill="white" stroke-width="2.5"/>'
        f'<rect x="37" y="71" width="26" height="7" rx="3" fill="{GREY}" stroke-width="3.5"/>'
        f'<rect x="39" y="80" width="22" height="7" rx="3" fill="{GREY}" stroke-width="3.5"/><path d="M44,90 Q50,95 56,90" stroke-width="3.5"/>')


def wonder():
    """A thought cloud with a big question mark: questions to explore."""
    return _svg(
        '<path d="M26,64 C11,64 9,44 23,41 C20,24 40,17 49,27 C55,12 79,14 79,32 C94,33 95,57 80,62 C78,70 64,72 58,66 '
        'C52,73 34,73 26,64 Z" fill="white"/>'
        f'<path d="M30,58 C22,57 19,50 24,46" stroke="{LIGHT}" stroke-width="4"/>'
        '<path d="M42,37 C42,27 61,27 61,37 C61,44 52,44 52,52" stroke-width="5.5"/><circle cx="52" cy="60" r="3.3" fill="#111" stroke="none"/>'
        '<circle cx="24" cy="78" r="5.5" fill="white" stroke-width="3.5"/><circle cx="13" cy="90" r="3.2" fill="white" stroke-width="3"/>'
        + _sparkle(88, 12, 8) + _sparkle(10, 22, 5))



def zoom(n):
    """A picture seen through a window that grows: 1 small peek ... 4 the whole picture."""
    pic = ('<circle cx="66" cy="32" r="8" fill="#cfcfcf" stroke-width="3"/><path d="M14,82 L38,46 L52,64 L64,50 L86,82 Z" fill="white" stroke-width="3.5"/>'
           '<path d="M30,82 L38,70 L46,82" stroke-width="3"/>')
    hole = {1: 9, 2: 17, 3: 27}.get(n)
    cover = (f'<path d="M14,14 H86 V86 H14 Z M{50 - hole},52 a{hole},{hole} 0 1 0 {2 * hole},0 a{hole},{hole} 0 1 0 {-2 * hole},0 Z" '
             f'fill="{GREY}" fill-rule="evenodd" stroke="none"/><circle cx="50" cy="52" r="{hole}" stroke-width="3" stroke-dasharray="5 4"/>') if hole else ''
    return _svg(f'<rect x="14" y="14" width="72" height="72" rx="8" fill="white"/>{pic}{cover}<rect x="14" y="14" width="72" height="72" rx="8"/>'
                + (_sparkle(90, 10, 7) if n == 4 else ''))


def traffic(n):
    """A traffic light with light n lit (1 top = red / stop, 2 middle = yellow / slow down)."""
    o = f'<rect x="31" y="6" width="38" height="88" rx="12" fill="white"/><line x1="50" y1="94" x2="50" y2="99" stroke-width="5"/>'
    for i, y in enumerate((26, 50, 74), 1):
        lit = i == n
        o += f'<circle cx="50" cy="{y}" r="9" fill="{INK if lit else LIGHT}" stroke-width="3.5"/>'
        if lit:
            for a in (-30, 0, 30, 150, 180, 210):
                t = math.radians(a)
                o += (f'<line x1="{50 + 23 * math.cos(t):.1f}" y1="{y + 23 * math.sin(t):.1f}" x2="{50 + 31 * math.cos(t):.1f}" '
                      f'y2="{y + 31 * math.sin(t):.1f}" stroke-width="3.5"/>')
    return _svg(o)


def compass_rose():
    o = f'<circle cx="50" cy="50" r="47" fill="white" stroke-width="3.5"/><circle cx="50" cy="50" r="31" stroke="{LIGHT}" stroke-width="5"/>'
    o += f'<path d="M50,20 L57,50 L50,80 L43,50 Z" fill="{GREY}" stroke-width="2.8"/><path d="M20,50 L50,43 L80,50 L50,57 Z" fill="white" stroke-width="2.8"/>'
    o += f'<path d="M50,20 L57,50 L43,50 Z" fill="{INK}" stroke-width="2.8"/><circle cx="50" cy="50" r="3.5" fill="white" stroke-width="2.5"/>'
    for t, x, y in (('N', 50, 14.5), ('E', 88, 53.5), ('S', 50, 92.5), ('W', 12, 53.5)):
        o += f'<text x="{x}" y="{y}" text-anchor="middle" font-family="Fredoka, sans-serif" font-weight="600" font-size="11" fill="{INK}" stroke="none">{t}</text>'
    return _svg(o)


def fruit():
    """An apple cut in half, with its layers numbered: 1 skin, 2 flesh, 3 core (Peel the Fruit)."""
    outer = 'M50,24 C38,11 10,14 9,43 C8,72 30,95 50,87 C70,95 92,72 91,43 C90,14 62,11 50,24 Z'
    o = f'<path d="M50,25 C50,15 52,9 56,4" stroke-width="4"/><path d="M55,11 C62,2 76,3 78,9 C70,15 61,15 55,11 Z" fill="white" stroke-width="3"/>'
    o += f'<path d="{outer}" fill="white" stroke-width="5.5"/>'
    o += f'<path d="{outer}" fill="{LIGHT}" stroke-width="2" stroke-dasharray="4 4" transform="translate(50 54) scale(.84) translate(-50 -54)"/>'
    o += f'<path d="M50,38 C55,46 64,48 64,56 C64,64 55,66 50,74 C45,66 36,64 36,56 C36,48 45,46 50,38 Z" fill="{GREY}" stroke-width="3"/>'
    for a in (-90, -18, 54, 126, 198):
        t = math.radians(a)
        x, y = 50 + 10 * math.cos(t), 56 + 10.5 * math.sin(t)
        o += f'<ellipse cx="{x:.1f}" cy="{y:.1f}" rx="1.8" ry="3.4" fill="{INK}" stroke="none" transform="rotate({a + 90} {x:.1f} {y:.1f})"/>'
    for n, x, y in (('1', 13, 22), ('2', 24, 64), ('3', 50, 56)):
        o += (f'<circle cx="{x}" cy="{y}" r="5.2" fill="{INK}" stroke="white" stroke-width="1.5"/><text x="{x}" y="{y + 3.3}" text-anchor="middle" '
              f'font-family="Fredoka, sans-serif" font-weight="600" font-size="9" fill="white" stroke="none">{n}</text>')
    return _svg(o)


def rope(w=1000, h=120):
    """A tug-of-war rope across the page with a centre marker and a scale for 'where I stand'."""
    y = h / 2
    o = f'<svg class="rt-rope" viewBox="0 0 {w} {h}" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg" fill="none" stroke="{INK}" stroke-linecap="round">'
    o += f'<rect x="20" y="{y - 9}" width="{w - 40}" height="18" rx="9" fill="white" stroke-width="3"/>'
    for x in range(34, w - 30, 16):
        o += f'<path d="M{x},{y + 8} L{x + 10},{y - 8}" stroke-width="2"/>'
    o += f'<rect x="{w / 2 - 7}" y="{y - 30}" width="14" height="60" rx="4" fill="{INK}" stroke="none"/>'
    for i in range(1, 10):
        x = 20 + i * (w - 40) / 10
        o += f'<line x1="{x}" y1="{y + 18}" x2="{x}" y2="{y + 30}" stroke-width="2.5"/>'
    return o + '</svg>'


_TABLER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'icons')


def badge(name, spark=(86, 14)):
    """A Tabler line icon (MIT) drawn large on a soft grey blob with a sparkle, to match the hand-drawn icons."""
    src = open(os.path.join(_TABLER, f'{name}.svg'), encoding='utf-8').read()
    inner = re.sub(r'<!--.*?-->', '', src, flags=re.S)
    inner = re.sub(r'^.*?<svg[^>]*>|</svg>\s*$', '', inner.strip(), flags=re.S)
    return _svg(f'<circle cx="54" cy="56" r="37" fill="{LIGHT}" stroke="none"/>'
                f'<g transform="translate(14 14) scale(3)" stroke-width="1.45">{inner}</g>' + _sparkle(*spark, 7))


def get(name):
    """Icon by name: a drawn icon (see, think, wonder, zoom1-4, red, yellow, compass, fruit) or any Tabler icon name."""
    drawn = {'see': see, 'think': think, 'wonder': wonder, 'red': lambda: traffic(1), 'yellow': lambda: traffic(2),
             'compass-rose': compass_rose, 'fruit': fruit}
    if name in drawn:
        return drawn[name]()
    if name.startswith('zoom') and name[4:].isdigit():
        return zoom(int(name[4:]))
    return badge(name)
