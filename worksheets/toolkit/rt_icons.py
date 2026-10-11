"""Hand-drawn style icons for the thinking routine templates (original InquiryMind drawings, black and grey).
Each function returns an <svg> in a 100 x 100 box."""
import math

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


ICONS = {'see': see, 'think': think, 'wonder': wonder}
