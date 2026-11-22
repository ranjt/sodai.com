"""KG 2 'Magic Shapes' art sheets: one shape repeated in 6 boxes. Run: python3 make.py  (then render_pdf.js)"""
import json, os, re
HERE = os.path.dirname(os.path.abspath(__file__))
D = 'fill="none" stroke="#111" stroke-width="1" stroke-dasharray="2.4 2" stroke-linecap="round" stroke-linejoin="round"'
SHAPES = {
 'circles': ('Circles', 'circles', lambda s, dx, dy: f'<circle cx="{50+dx}" cy="{50+dy}" r="{s*0.36}" {D}/>', 'faces, a sun, a ball, a flower, a wheel, a clock, a fish ...'),
 'triangles': ('Triangles', 'triangles', lambda s, dx, dy: f'<path d="M{50+dx} {50+dy-s*.4} L{50+dx+s*.42} {50+dy+s*.3} H{50+dx-s*.42} Z" {D}/>', 'a hat, a mountain, a tent, a rocket, a tree, a bird ...'),
 'squares': ('Squares', 'squares', lambda s, dx, dy: f'<rect x="{50+dx-s*.34}" y="{50+dy-s*.34}" width="{s*.68}" height="{s*.68}" rx="2" {D}/>', 'a house, a robot, a window, a cake, a TV, a present ...'),
}
SIZES = [(100, 0, 0), (84, 0, 0), (92, 0, 0), (100, 0, 0), (88, 0, 0), (96, 0, 0)]
tpl = open(os.path.join(HERE, 'template.html'), encoding='utf-8').read()
head = tpl.split('<div class="frame big">')[0]
head = head.replace('.big{height:136mm}', '.grid{flex:1;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:repeat(3,1fr);gap:3.5mm;min-height:0}.grid .frame{height:auto}')
head = head.replace('.row{display:flex;gap:3.5mm}\n.row .frame{flex:1;height:70mm}\n', '')
tail = '<div class="foot">' + tpl.split('<div class="foot">')[1]
jobs = []
for key, (name, slug, f, ideas) in SHAPES.items():
    how = ('<div class="how"><div class="n">1</div><div>Look at the <b>%s</b>. <b>What can each one become?</b></div>'
           '<div class="n">2</div><div>Add <b>eyes, lines, legs</b> and <b>colours</b>. Make <b>every one different!</b></div></div>' % name.lower())
    h = re.sub(r'<div class="how">.*?</div>\n</div>\n', how + '\n', head, flags=re.S)
    h = h.replace('<h1>Magic Shapes!</h1>', f'<h1>Magic {name}!</h1>')
    boxes = ''.join(f'<div class="frame"><svg viewBox="0 0 100 100" preserveAspectRatio="xMidYMid meet">{f(s, dx, dy)}</svg></div>' for s, dx, dy in SIZES)
    page = h + f'<div class="grid">{boxes}</div>\n<p class="small">Ideas: {ideas}</p>\n' + tail
    out = os.path.join(HERE, f'kg2-magic-{slug}.html')
    open(out, 'w', encoding='utf-8').write(page)
    jobs.append({'html': out, 'pdf': os.path.join(HERE, f'KG2-Art-Magic-{name}.pdf')})
json.dump(jobs, open('/tmp/j.json', 'w'))
