"""Grade 2 and 3 illustrations: simple SVG line art plus OpenMoji pictures. Primitives come from art.py."""
import math

from art import INK, GREY, LIGHT, svg, text, line, path, circle, ellipse, rect, arrow, curved_arrow, callout, pic, sun_icon, cloud, thermometer
from art4 import mtext

BODY_PARTS = ['head', 'neck', 'shoulder', 'arm', 'elbow', 'hand', 'chest', 'tummy', 'leg', 'knee', 'foot']


def body_outline(labels=None, w='100%'):
    """A simple standing child with callouts to 11 external body parts (numbered when labels is None)."""
    o = circle(150, 46, 28, 'white', 1.8)
    o += path('M140,74 L140,86 M160,74 L160,86', w=1.8)
    o += path('M112,92 Q150,80 188,92 L184,196 L116,196 Z', 'white', 1.8)
    o += path('M112,92 L92,150 L88,206', w=1.8) + path('M188,92 L208,150 L212,206', w=1.8)
    o += ellipse(87, 214, 8, 10, 'white', 1.6) + ellipse(213, 214, 8, 10, 'white', 1.6)
    o += path('M124,196 L122,262 L120,324', w=1.8) + path('M176,196 L178,262 L180,324', w=1.8)
    o += path('M120,324 L100,332 L124,334 Z', 'white', 1.6) + path('M180,324 L200,332 L176,334 Z', 'white', 1.6)
    o += circle(140, 42, 2.4, INK, 0) + circle(160, 42, 2.4, INK, 0) + path('M140,58 Q150,64 160,58', w=1.4)
    pts = [(150, 18, 250, 20), (150, 80, 250, 66), (186, 94, 250, 104), (200, 128, 262, 140), (208, 150, 270, 172),
           (213, 214, 270, 214), (150, 112, 40, 100), (150, 170, 40, 168), (178, 236, 250, 250), (178, 262, 256, 284), (196, 330, 254, 330)]
    for i, (px, py, tx, ty) in enumerate(pts):
        o += callout(i + 1, tx, ty, px, py, labels)
    return svg(340, 346, o, width=w)


def human_growth(w='100%'):
    """Baby, child, teenager/adult, older adult with arrows."""
    from art import pic_row
    return pic_row(['baby', 'child', 'adult', 'older person'], ['baby', 'child', 'adult', 'older adult'], 64, 60, 12, w, arrows=True)


LANDFORMS = ['mountain', 'hill', 'valley', 'cave', 'plain (flatland)', 'island']


def landforms(names=True, w='100%'):
    o = ''
    for i in range(6):
        x0 = (i % 3) * 170
        y0 = (i // 3) * 140
        o += rect(x0, y0, 158, 110, 10, 'white', 1.3)
    # mountain
    o += path('M10,100 L60,20 L80,46 L96,30 L150,100 Z', LIGHT, 1.5) + path('M50,36 L60,20 L70,36 L64,32 L58,38 Z', 'white', 1.2)
    # hill
    o += path('M172,100 Q250,30 326,100 Z', LIGHT, 1.5) + pic('deciduous tree', 236, 36, 26)
    # valley with river
    o += path('M342,30 Q380,40 410,96 L430,96 Q456,40 496,30 L496,100 L342,100 Z', LIGHT, 1.5) + path('M410,96 q10,-4 20,0', w=2)
    # cave
    o += path('M12,240 L12,190 Q40,150 90,160 Q140,166 150,240 Z', LIGHT, 1.5) + path('M50,240 Q50,200 80,200 Q108,200 108,240 Z', INK, 0)
    # plain
    o += line(176, 230, 322, 230, 1.6)
    for k in range(7):
        o += pic('rice plant', 180 + k * 20, 206, 22)
    o += pic('sun', 290, 150, 26)
    # island
    o += rect(342, 210, 154, 38, 0, LIGHT, 0) + path('M342,210 q15,-5 30,0 t30,0 t30,0 t30,0 t34,0', w=1.2)
    o += path('M380,212 Q420,180 462,212 Z', GREY, 1.4) + pic('palm tree', 404, 168, 30)
    for i, n in enumerate(LANDFORMS if names else list('ABCDEF')):
        o += text((i % 3) * 170 + 79, (i // 3) * 140 + 128, n, 12, weight='bold')
    return svg(500, 270, o, width=w)


ROCKS = ['granite', 'sandstone', 'marble', 'slate', 'chalk']


def rock_types(names=True, w='100%'):
    o = ''
    shapes = ['M10,60 L20,22 L60,12 L88,30 L84,66 L40,76 Z', 'M110,62 L118,24 L170,16 L188,40 L178,70 L130,74 Z',
              'M212,56 L220,20 L262,14 L288,36 L280,70 L236,74 Z', 'M310,64 L316,30 L380,22 L388,50 L374,72 L330,74 Z',
              'M412,60 L420,26 L466,18 L486,44 L476,70 L432,74 Z']
    for i, d in enumerate(shapes):
        o += path(d, 'white', 1.8)
    for x, y in ((30, 40), (46, 30), (60, 50), (40, 58), (70, 40), (26, 54), (54, 36), (36, 46)):
        o += circle(x, y, 2.6, INK, 0)
    for k in range(4):
        o += path(f'M{118 + k * 2},{32 + k * 10} q30,-6 64,0', w=0.9)
    for x, y in ((140, 40), (160, 52), (130, 58), (170, 30)):
        o += circle(x, y, 1, INK, 0)
    o += path('M226,30 Q248,46 262,30 T284,46', w=0.9) + path('M230,58 Q250,44 276,60', w=0.9)
    for k in range(5):
        o += line(318, 36 + k * 8, 384, 30 + k * 8, 1.2)
    o += path('M440,40 q6,-6 12,0', w=1) + path('M456,54 q5,-5 10,0', w=1)
    labels = ROCKS if names else list('ABCDE')
    for i, x in enumerate((50, 150, 250, 350, 450)):
        o += text(x, 96, labels[i], 12, weight='bold')
    return svg(500, 104, o, width=w)


def rock_to_soil(w='100%'):
    o = ''
    o += path('M10,80 L20,30 L70,20 L96,44 L90,84 Z', GREY, 1.6)
    o += path('M140,84 L144,40 L176,30 L200,48 L196,84 Z', GREY, 1.6) + path('M168,32 L162,58 L176,84', w=1.6) + pic('herb', 150, 4, 26)
    for x, y in ((240, 70), (262, 56), (284, 72), (258, 80), (300, 60)):
        o += path(f'M{x - 8},{y + 6} L{x - 4},{y - 6} L{x + 8},{y - 4} L{x + 8},{y + 6} Z', GREY, 1.2)
    for k in range(40):
        o += circle(340 + (k * 37) % 70, 50 + (k * 23) % 34, 1.6, INK, 0)
    o += rect(436, 56, 80, 30, 4, GREY, 1.2) + pic('seedling', 458, 14, 40)
    for x in (100, 214, 316, 420):
        o += arrow(x, 56, x + 26, 56, 1.6, 7)
    for x, t in ((52, 'big rock'), (172, 'cracks'), (270, 'small stones'), (374, 'sand'), (476, 'soil')):
        o += text(x, 108, t, 12, weight='bold')
    o += text(260, 128, 'Rain, heat, ice and plant roots break rock into smaller and smaller pieces.', 10.5, italic=True)
    return svg(520, 136, o, width=w)


ARM_PARTS = ['bone', 'biceps (contracts)', 'triceps (relaxes)', 'elbow joint']


def arm_muscles(labels=None, w='100%'):
    """A bent arm: biceps contracts (shortens) to pull the lower arm up."""
    o = path('M60,40 L60,170 L190,170', w=10).replace(INK, '#bbb', 1) + path('M60,40 L60,170 L190,170', w=1.4)
    o += ellipse(60, 170, 10, 10, 'white', 1.6)
    o += path('M70,60 C100,80 104,140 80,160', LIGHT, 1.8) + path('M50,60 C24,90 26,140 46,160', 'white', 1.6)
    o += path('M190,170 l14,-8 m-14,8 l14,8', w=1.6) + arrow(160, 156, 160, 120, 2, 9)
    for i, (px, py, tx, ty) in enumerate(((120, 170, 160, 200), (92, 110, 150, 80), (32, 110, 6, 60), (60, 178, 20, 210))):
        o += callout(i + 1, tx, ty, px, py, labels)
    return svg(400, 220, f'<g transform="translate(110 0)">{o}</g>', width=w)


MOON_PHASES = ['new moon', 'waxing crescent', 'first quarter', 'waxing gibbous', 'full moon', 'waning gibbous', 'last quarter', 'waning crescent']
_MOON_PICS = ['new moon', 'waxing crescent moon', 'first quarter moon', 'waxing gibbous moon', 'full moon', 'waning gibbous moon',
              'last quarter moon', 'waning crescent moon']


def moon_phases(names=True, w='100%'):
    o = ''
    for i, p in enumerate(_MOON_PICS):
        x = i * 76
        o += pic(p, x + 6, 0, 56)
        lab = MOON_PHASES[i] if names else str(i + 1)
        o += mtext(x + 34, 74, lab, 10.5, 12, weight='bold')
    o += arrow(10, 112, 590, 112, 1.4, 8) + text(300, 126, 'about 29½ days from one new moon to the next', 10.5, italic=True)
    return svg(608, 132, o, width=w)


HEAT_WAYS = ['conduction', 'convection', 'radiation']


def heat_transfer(names=True, w='100%'):
    o = ''
    for i in range(3):
        o += rect(i * 170, 0, 158, 140, 10, 'white', 1.3)
    # conduction: spoon in a hot cup
    o += path('M30,70 L40,124 L100,124 L110,70 Z', 'white', 1.6) + rect(32, 80, 76, 42, 0, LIGHT, 0) + line(70, 100, 132, 24, 3)
    for k in range(3):
        o += arrow(84 + k * 14, 82 - k * 17, 94 + k * 14, 70 - k * 17, 1.2, 6)
    # convection: pot of water over a flame
    o += path('M200,40 L206,104 L296,104 L302,40', 'white', 1.6) + rect(204, 52, 94, 50, 0, LIGHT, 0)
    o += curved_arrow(236, 96, 230, 60, 250, 58, 1.4, 7) + curved_arrow(266, 58, 290, 64, 268, 96, 1.4, 7)
    o += pic('fire', 232, 104, 36)
    # radiation: sun to hands
    o += sun_icon(380, 40, 18)
    for k in range(3):
        o += arrow(402 + k * 4, 52 + k * 10, 450 - k * 6, 96 + k * 8, 1.2, 6, '4 3')
    o += pic('hand', 440, 84, 44)
    labels = HEAT_WAYS if names else list('ABC')
    sub = ['heat travels through solids', 'warm liquid or air rises', 'heat travels as rays']
    for i in range(3):
        o += text(i * 170 + 79, 160, labels[i], 12.5, weight='bold')
        if names:
            o += text(i * 170 + 79, 175, sub[i], 10, italic=True)
    return svg(500, 182 if names else 166, o, width=w)


def pulley_gears(w='100%'):
    """A pulley lifting a bucket from a well, and two gears turning."""
    o = line(20, 20, 140, 20, 3) + line(80, 20, 80, 34, 1.6) + circle(80, 48, 14, 'white', 1.8) + circle(80, 48, 2.5, INK, 0)
    o += line(66, 48, 66, 150, 1.4) + line(94, 48, 94, 110, 1.4) + pic('bucket', 78, 106, 34)
    o += path('M40,180 L40,150 L130,150 L130,180', w=2) + arrow(66, 120, 66, 160, 1.6, 7) + text(42, 136, 'pull down', 10, 'end', italic=True)
    o += arrow(112, 120, 112, 96, 1.6, 7) + text(116, 92, 'bucket goes up', 10, 'start', italic=True)
    for cx, cy, r, n, a0 in ((260, 90, 42, 12, 0), (338, 90, 28, 8, 22)):
        teeth = ''
        for k in range(n):
            t = math.radians(a0 + k * 360 / n)
            teeth += line(cx + r * math.cos(t), cy + r * math.sin(t), cx + (r + 9) * math.cos(t), cy + (r + 9) * math.sin(t), 5)
        o += teeth + circle(cx, cy, r, 'white', 1.8) + circle(cx, cy, 4, INK, 0)
    o += curved_arrow(230, 40, 260, 26, 290, 40, 1.6, 8) + curved_arrow(320, 140, 338, 150, 358, 140, 1.6, 8)
    o += text(80, 200, 'pulley', 12, weight='bold') + text(300, 200, 'gears', 12, weight='bold')
    return svg(430, 208, f'<g transform="translate(26 0)">{o}</g>', width=w)


def celery_stem(w='100%'):
    """A white flower stem in coloured water: the colour travels up the stem."""
    o = path('M40,90 L46,190 L110,190 L116,90', 'white', 1.8) + rect(44, 130, 68, 58, 0, GREY, 0) + line(42, 130, 114, 130, 1.2)
    o += line(78, 186, 82, 50, 4) + line(78, 186, 82, 50, 1.5).replace(INK, '#777', 1)
    for k in range(6):
        a = math.radians(k * 60)
        o += ellipse(82 + 12 * math.cos(a), 40 + 12 * math.sin(a), 8, 5, LIGHT, 1.2, k * 60)
    o += circle(82, 40, 5, GREY, 1.2)
    o += arrow(102, 160, 102, 70, 1.6, 8) + text(124, 110, 'coloured water moves up the stem', 10.5, 'start', italic=True)
    o += text(104, 30, 'after one day the petals are coloured', 10.5, 'start', italic=True)
    return svg(330, 200, o, width=w)


DECIBELS = [('leaves in wind', 'leaves rustling', 20), ('bird', 'birds singing', 40), ('mouth', 'talking', 60),
            ('bus', 'busy traffic', 80), ('loudspeaker', 'loud music', 100), ('airplane', 'plane taking off', 120)]


def decibel_scale(values=True, w='100%'):
    """A 0-140 dB scale with everyday sounds; above 85 dB is shaded as harmful to hearing."""
    x0, x1, y = 30, 610, 120
    def X(db):
        return x0 + db / 140 * (x1 - x0)
    o = rect(X(85), y - 8, X(140) - X(85), 16, 0, GREY, 0) + rect(x0, y - 8, x1 - x0, 16, 0, 'none', 1.4)
    for db in range(0, 141, 10):
        o += line(X(db), y + 8, X(db), y + 14, 1) + text(X(db), y + 26, str(db), 9)
    o += text((x0 + x1) / 2, y + 42, 'loudness in decibels (dB)', 11, weight='bold')
    o += text((X(85) + X(140)) / 2, y + 4, 'can damage hearing', 9.5, weight='bold')
    for name, label, db in DECIBELS:
        o += pic(name, X(db) - 20, 10, 40) + text(X(db), 66, label, 10, weight='bold')
        o += text(X(db), 80, f'{db} dB' if values else '___ dB', 10) + line(X(db), 86, X(db), y - 9, 0.9, '2 2')
    return svg(640, 170, o, width=w)


def bottle_pitch(numbered=False, w='100%'):
    """Four bottles with different amounts of water, tapped with a spoon."""
    o = ''
    for i, lvl in enumerate((20, 45, 70, 95)):
        x = 30 + i * 110
        o += rect(x + 6, 150 - lvl, 48, lvl, 0, GREY, 0)
        o += path(f'M{x + 20},20 L{x + 20},42 Q{x},54 {x},76 L{x},150 Q{x},154 {x + 4},154 L{x + 56},154 Q{x + 60},154 {x + 60},150 '
                  f'L{x + 60},76 Q{x + 60},54 {x + 40},42 L{x + 40},20 Z', w=1.6)
        o += text(x + 30, 176, chr(65 + i) if numbered else ['highest note', 'high', 'low', 'lowest note'][i], 11, weight='bold')
    o += line(392, 60, 446, 18, 3) + ellipse(386, 64, 9, 6, 'white', 1.6, -38)
    o += text(450, 36, 'tap', 10, 'start', italic=True)
    return svg(480, 186, o, width=w)


def thermometers(values=(5, 25, 40), lo=0, hi=50, numbered=True, w='100%'):
    """A row of thermometers for reading temperatures."""
    o = ''
    for i, v in enumerate(values):
        x = 40 + i * 110
        o += thermometer(x, 30, v, lo, hi, 170, 10) + (text(x, 238, chr(65 + i), 13, weight='bold') if numbered else '')
    return svg(len(values) * 110 + 20, 246, o, width=w)


def current_model(w='100%'):
    """Particle model of an electric current: particles flow all the way round a complete circuit."""
    L, T, R, B = 40, 30, 340, 170
    o = line(L, T, R, T, 6) + line(R, T, R, B, 6) + line(R, B, L, B, 6) + line(L, B, L, T, 6)
    o = o.replace(INK, '#bbb')
    o += line(L, T, R, T, 0.8) + line(R, T, R, B, 0.8) + line(R, B, L, B, 0.8) + line(L, B, L, T, 0.8)
    o += rect(L - 16, 86, 32, 28, 0, 'white', 0) + line(L - 8, 92, L + 8, 92, 4) + line(L - 14, 108, L + 14, 108, 2)
    o += rect(170, T - 18, 40, 36, 0, 'white', 0) + circle(190, T, 16, 'white', 1.8) + line(179, T - 11, 201, T + 11, 1.6) + line(179, T + 11, 201, T - 11, 1.6)
    for k in range(5):
        o += circle(70 + k * 20, T, 3.5, INK, 0) + circle(230 + k * 22, T, 3.5, INK, 0) + circle(80 + k * 52, B, 3.5, INK, 0)
        o += circle(R, 52 + k * 26, 3.5, INK, 0)
    o += arrow(250, T - 14, 300, T - 14, 1.4, 7) + arrow(R + 14, 80, R + 14, 130, 1.4, 7) + arrow(290, B + 14, 240, B + 14, 1.4, 7)
    o += text(L - 22, 102, 'cell', 11, 'end', weight='bold') + text(190, T + 32, 'lamp', 11, weight='bold')
    o += text(190, 110, 'tiny particles flow all the way', 10.5, italic=True) + text(190, 124, 'round the circuit', 10.5, italic=True)
    return svg(400, 196, o, width=w)


def ramp_lift(w='100%'):
    """Lifting a box straight up needs more force than pulling it up a ramp."""
    o = line(10, 170, 470, 170, 1.4)
    o += rect(70, 120, 46, 50, 3, LIGHT, 1.6) + arrow(93, 116, 93, 46, 2.4, 10)
    o += text(93, 32, 'lift straight up', 11, weight='bold') + text(93, 18, '10 N', 12, weight='bold')
    o += path('M200,170 L440,170 L440,90 Z', LIGHT, 1.6)
    o += f'<g transform="rotate(-18.4 330 133)">{rect(306, 92, 46, 38, 3, "white", 1.6)}</g>'
    o += arrow(360, 108, 420, 88, 2.4, 10)
    o += text(340, 62, 'pull up the ramp', 11, weight='bold') + text(340, 48, '4 N', 12, weight='bold')
    o += text(320, 190, 'longer path, less force', 10.5, italic=True)
    return svg(480, 198, o, width=w)
