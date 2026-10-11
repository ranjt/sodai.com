"""
Worksheet building blocks. Every block renders itself with html(key):
  key=False -> learner version (blanks empty)
  key=True  -> answer key (answers written in, in a handwriting font)
Questions are written once, with their answers, so the learner sheet and the answer key always match.
"""
import html as _html
import random
import re

from icons import icon


def esc(s):
    return _html.escape(str(s), quote=True)


def rich(s):
    """Minimal inline markup: **bold**, *italic*, ^sup^, ~sub~. Everything else is escaped."""
    s = esc(s)
    s = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)
    s = re.sub(r'\*(.+?)\*', r'<i>\1</i>', s)
    s = re.sub(r'\^(.+?)\^', r'<sup>\1</sup>', s)
    s = re.sub(r'~(.+?)~', r'<sub>\1</sub>', s)
    return s


def render(blocks, key):
    return ''.join(b if isinstance(b, str) else b.html(key) for b in blocks)


class Block:
    def html(self, key):
        raise NotImplementedError


# ---------------------------------------------------------------- text & layout
class P(Block):
    def __init__(self, text, cls=''):
        self.text, self.cls = text, cls

    def html(self, key):
        return f'<p class="{self.cls}">{rich(self.text)}</p>'


class H(Block):
    def __init__(self, text, level=2):
        self.text, self.level = text, level

    def html(self, key):
        return f'<h{self.level}>{rich(self.text)}</h{self.level}>'


class Raw(Block):
    def __init__(self, markup):
        self.markup = markup

    def html(self, key):
        return self.markup


class Bullets(Block):
    def __init__(self, items, ordered=False):
        self.items, self.ordered = items, ordered

    def html(self, key):
        tag = 'ol' if self.ordered else 'ul'
        return f'<{tag}>' + ''.join(f'<li>{rich(i)}</li>' for i in self.items) + f'</{tag}>'


BOX_STYLES = {
    'fact': ('bulb', 'Did you know?'),
    'bd': ('map-pin', 'Bangladesh connection'),
    'vocab': ('vocabulary', 'Key words'),
    'think': ('microscope', 'Think like a scientist'),
    'safety': ('alert-triangle', 'Stay safe'),
    'world': ('world', 'Around the world'),
    'history': ('hourglass', 'From the past'),
    'link': ('arrows-shuffle', 'Subject links'),
    'tip': ('pencil', 'Remember'),
    'need': ('package', 'You will need'),
}


class Box(Block):
    def __init__(self, kind, *content, title=None):
        self.kind, self.content, self.title = kind, content, title

    def html(self, key):
        ic, default = BOX_STYLES.get(self.kind, ('info-circle', ''))
        title = self.title or default
        return (f'<div class="box {self.kind}"><div class="bt">{icon(ic)}{rich(title)}</div>'
                f'{render(self.content, key)}</div>')


class Vocab(Block):
    def __init__(self, words, title='Key words'):
        self.words, self.title = words, title

    def html(self, key):
        rows = ''.join(f'<dt>{rich(w)}</dt><dd>{rich(d)}</dd>' for w, d in self.words)
        return f'<div class="box vocab"><div class="bt">{icon("vocabulary")}{esc(self.title)}</div><dl>{rows}</dl></div>'


class Fig(Block):
    """A figure. span=True makes it run across both columns inside Cols."""
    def __init__(self, svg, caption='', width=None, span=False):
        self.svg, self.caption, self.width, self.span = svg, caption, width, span

    def html(self, key):
        style = f' style="width:{self.width};margin-left:auto;margin-right:auto"' if self.width else ''
        cap = f'<figcaption>{rich(self.caption)}</figcaption>' if self.caption else ''
        return f'<figure class="fig{" span" if self.span else ""}"{style}>{self.svg}{cap}</figure>'


class Cols(Block):
    """Newspaper-style two-column flow. A heading is kept together with the block after it."""
    def __init__(self, *content):
        self.content = content

    def html(self, key):
        out, items, i = '', list(self.content), 0
        while i < len(items):
            if isinstance(items[i], H) and i + 1 < len(items):
                out += f'<div class="keep">{items[i].html(key)}{items[i + 1].html(key)}</div>'
                i += 2
            else:
                out += items[i] if isinstance(items[i], str) else items[i].html(key)
                i += 1
        return f'<div class="cols">{out}</div>'


class Row(Block):
    """Side-by-side columns; each argument is a list of blocks (or a single block)."""
    def __init__(self, *columns, widths=None):
        self.columns, self.widths = columns, widths

    def html(self, key):
        out = []
        for i, col in enumerate(self.columns):
            col = col if isinstance(col, (list, tuple)) else [col]
            flex = f' style="flex:{self.widths[i]}"' if self.widths else ''
            out.append(f'<div{flex}>{render(col, key)}</div>')
        return f'<div class="row">{"".join(out)}</div>'


class Case(Block):
    """A reading passage (case study, news report, interview)."""
    def __init__(self, *paras, source=''):
        self.paras, self.source = paras, source

    def html(self, key):
        body = ''.join(f'<p>{rich(p)}</p>' if isinstance(p, str) else p.html(key) for p in self.paras)
        src = f'<div class="src">{rich(self.source)}</div>' if self.source else ''
        return f'<div class="case">{body}{src}</div>'


class Links(Block):
    def __init__(self, *subjects):
        self.subjects = subjects

    def html(self, key):
        return '<div class="links">' + ''.join(f'<span>{esc(s)}</span>' for s in self.subjects) + '</div>'


# ---------------------------------------------------------------- answer widgets
class Lines(Block):
    """Answer lines. answer: model answer shown in the key (spills over lines if long)."""
    def __init__(self, n=2, answer=''):
        self.n, self.answer = n, answer

    def html(self, key):
        if key and self.answer:
            return (f'<div class="lines"><div class="ln multi"><span class="ans">{rich(self.answer)}</span></div>'
                    + '<div class="ln"></div>' * max(0, self.n - 1 - len(self.answer) // 85) + '</div>')
        return '<div class="lines">' + '<div class="ln"></div>' * self.n + '</div>'


class Blanks(Block):
    """Text with gaps written as [answer]. bank=True shows a shuffled word bank (with optional extra words)."""
    def __init__(self, text, bank=True, extra=(), seed=1, width=None):
        self.text, self.bank, self.extra, self.seed, self.width = text, bank, extra, seed, width

    def answers(self):
        return re.findall(r'\[(.+?)\]', self.text)

    def html(self, key):
        def gap(m):
            w = f' style="min-width:{self.width}"' if self.width else ''
            return f'<span class="blank"{w}><span class="ans">{esc(m.group(1))}</span></span>'
        parts = re.split(r'(\[.+?\])', self.text)
        body = ''.join(gap(re.match(r'\[(.+)\]', p)) if p.startswith('[') else rich(p) for p in parts)
        bank = ''
        if self.bank:
            words = sorted(set(self.answers()) | set(self.extra), key=lambda w: random.Random(self.seed + len(w)).random())
            bank = '<div class="bank"><span class="t">Word bank</span>' + ''.join(f'<span>{esc(w)}</span>' for w in words) + '</div>'
        return f'{bank}<div class="blanks-text">{body}</div>'


class Match(Block):
    """pairs: [(left, right)]. Right column is shuffled and lettered; learners write the letter."""
    def __init__(self, pairs, seed=3, left_title='', right_title=''):
        self.pairs, self.seed = pairs, seed
        self.left_title, self.right_title = left_title, right_title

    def html(self, key):
        rights = [r for _, r in self.pairs]
        order = list(range(len(rights)))
        random.Random(self.seed).shuffle(order)
        # avoid leaving any pair in its original row
        if len(order) > 1 and any(i == o for i, o in enumerate(order)):
            order = order[1:] + order[:1]
        letters = 'ABCDEFGHIJKL'
        letter_of = {orig: letters[pos] for pos, orig in enumerate(order)}
        out = ''
        if self.left_title or self.right_title:
            out += (f'<div class="fredoka">{esc(self.left_title)}</div><div></div>'
                    f'<div class="fredoka">{esc(self.right_title)}</div>')
        for i, (left, _) in enumerate(self.pairs):
            r_idx = order[i]
            out += (f'<div class="l"><span>{rich(left)}</span><span class="dot"></span></div>'
                    f'<div class="mid"><span class="ans">→ {letter_of[i]}</span></div>'
                    f'<div class="r"><span class="dot"></span><span class="letter">{letters[i]}</span>'
                    f'<span>{rich(rights[r_idx])}</span></div>')
        note = '<p class="small muted">Draw a line to match each pair, or write the letter.</p>'
        return f'{note}<div class="match">{out}</div>'


class TrueFalse(Block):
    """statements: [(text, True/False, correction-if-false)]"""
    def __init__(self, statements, correct=True):
        self.statements, self.correct = statements, correct

    def html(self, key):
        fix_head = '<th>If false, correct it</th>' if self.correct else ''
        rows = ''
        for i, st in enumerate(self.statements, 1):
            text, val = st[0], st[1]
            fix = st[2] if len(st) > 2 else ''
            fix_cell = f'<td class="fix"><span class="ans">{rich(fix)}</span></td>' if self.correct else ''
            rows += (f'<tr><td>{i}. {rich(text)}</td>'
                     f'<td class="box"><span class="ans">{"✔" if val else ""}</span></td>'
                     f'<td class="box"><span class="ans">{"" if val else "✔"}</span></td>{fix_cell}</tr>')
        return (f'<table class="tbl tf"><tr><th>Statement</th><th>True</th><th>False</th>{fix_head}</tr>'
                f'{rows}</table>')


class MCQ(Block):
    def __init__(self, options, answer, one_col=False):
        self.options, self.answer, self.one_col = options, answer, one_col

    def html(self, key):
        items = ''.join(f'<li class="{"right" if i == self.answer else ""}"><span class="bx"></span>'
                        f'<span>{rich(o)}</span></li>' for i, o in enumerate(self.options))
        return f'<ul class="mcq{" one" if self.one_col else ""}">{items}</ul>'


class Order(Block):
    """items given in correct order; shown shuffled with boxes to number."""
    def __init__(self, items, seed=7):
        self.items, self.seed = items, seed

    def html(self, key):
        idx = list(range(len(self.items)))
        random.Random(self.seed).shuffle(idx)
        if idx == sorted(idx):
            idx = idx[::-1]
        rows = ''.join(f'<div class="it"><span class="sq"><span class="ans">{i + 1}</span></span>'
                       f'<span>{rich(self.items[i])}</span></div>' for i in idx)
        return f'<div class="order">{rows}</div>'


class Ans:
    """A table cell the learner fills in."""
    def __init__(self, text):
        self.text = text


class Table(Block):
    def __init__(self, headers, rows, center=False, widths=None):
        self.headers, self.rows, self.center, self.widths = headers, rows, center, widths

    def html(self, key):
        def cell(c, i):
            w = f' style="width:{self.widths[i]}"' if self.widths and self.widths[i] else ''
            if isinstance(c, Ans):
                return f'<td class="blank-cell"{w}><span class="ans">{rich(c.text)}</span></td>'
            return f'<td{w}>{rich(c)}</td>'
        head = ''.join(f'<th>{rich(h)}</th>' for h in self.headers) if self.headers else ''
        body = ''.join('<tr>' + ''.join(cell(c, i) for i, c in enumerate(r)) + '</tr>' for r in self.rows)
        return f'<table class="tbl{" center" if self.center else ""}"><tr>{head}</tr>{body}</table>'


class Sort(Block):
    """Sort items into categories. items: [(item, category)]. Learner sees an empty table + item bank."""
    def __init__(self, categories, items, seed=5, rows=None):
        self.categories, self.items, self.seed, self.rows = categories, items, seed, rows

    def html(self, key):
        bank_items = [i for i, _ in self.items]
        random.Random(self.seed).shuffle(bank_items)
        bank = '<div class="bank"><span class="t">Sort these</span>' + ''.join(f'<span>{rich(b)}</span>' for b in bank_items) + '</div>'
        cols = {c: [i for i, cat in self.items if cat == c] for c in self.categories}
        n = self.rows or max(len(v) for v in cols.values())
        head = ''.join(f'<th>{rich(c)}</th>' for c in self.categories)
        body = ''
        for r in range(n):
            body += '<tr>' + ''.join(
                f'<td class="blank-cell"><span class="ans">{rich(cols[c][r]) if r < len(cols[c]) else ""}</span></td>'
                for c in self.categories) + '</tr>'
        return f'{bank}<table class="tbl center"><tr>{head}</tr>{body}</table>'


class Label(Block):
    """A diagram (svg with numbered markers, see art.marker) and numbered label lines.
    answers: list of label words in marker order. bank=True shows them shuffled."""
    def __init__(self, svg, answers, bank=True, cols=2, width=None, extra=()):
        self.svg, self.answers, self.bank, self.cols, self.width, self.extra = svg, answers, bank, cols, width, extra

    def html(self, key):
        bank = ''
        if self.bank:
            words = list(self.answers) + list(self.extra)
            random.Random(len(words)).shuffle(words)
            bank = '<div class="bank"><span class="t">Labels</span>' + ''.join(f'<span>{esc(w)}</span>' for w in words) + '</div>'
        style = f' style="width:{self.width};margin:0 auto"' if self.width else ''
        lbls = ''.join(f'<div class="lb"><span class="n">{i}</span><span class="w"><span class="ans">{esc(a)}</span></span></div>'
                       for i, a in enumerate(self.answers, 1))
        cls = 'labels three' if self.cols == 3 else 'labels'
        return f'{bank}<div class="fig"{style}>{self.svg}</div><div class="{cls}">{lbls}</div>'


class Draw(Block):
    def __init__(self, height='45mm', caption='', answer=''):
        self.height, self.caption, self.answer = height, caption, answer

    def html(self, key):
        cap = f'<span class="cap">{rich(self.caption)}</span>' if self.caption else ''
        ans = f'<div class="ans">{rich(self.answer)}</div>' if self.answer else ''
        return f'<div class="drawbox" style="min-height:{self.height}">{cap}{ans}</div>'


class Graph(Block):
    """Bar or line graph frame. Learners plot; the key shows the plotted data."""
    def __init__(self, labels, values, ylabel, xlabel='', ymax=None, step=None, kind='bar', series_names=None,
                 width=150, height=82, show_data_in_key=True, blank_axes=False, ymin=0):
        self.labels, self.values, self.ylabel, self.xlabel = labels, values, ylabel, xlabel
        self.kind, self.series_names = kind, series_names
        flat = [v for s in (values if values and isinstance(values[0], (list, tuple)) else [values]) for v in s]
        self.ymax = ymax or (max(flat) if flat else 10)
        self.step = step or max(1, round(self.ymax / 10))
        self.w, self.h, self.show, self.blank_axes, self.ymin = width, height, show_data_in_key, blank_axes, ymin

    def html(self, key):
        import art
        return art.graph(self.labels, self.values, self.ylabel, self.xlabel, self.ymax, self.step, self.kind,
                         self.series_names, self.w, self.h, plot=key and self.show, blank_axes=self.blank_axes, ymin=self.ymin)


class WordSearch(Block):
    def __init__(self, words, size=12, seed=11):
        self.words = [w.upper().replace(' ', '') for w in words]
        self.size, self.seed = size, seed
        self.grid, self.hits = self._build()

    def _build(self):
        rnd = random.Random(self.seed)
        n = self.size
        for _attempt in range(200):
            grid = [[''] * n for _ in range(n)]
            hits = set()
            ok = True
            for w in sorted(self.words, key=len, reverse=True):
                placed = False
                for _ in range(300):
                    dx, dy = rnd.choice([(1, 0), (0, 1), (1, 1)])
                    x, y = rnd.randrange(n), rnd.randrange(n)
                    if x + dx * (len(w) - 1) >= n or y + dy * (len(w) - 1) >= n:
                        continue
                    cells = [(x + dx * i, y + dy * i) for i in range(len(w))]
                    if all(grid[cy][cx] in ('', w[i]) for i, (cx, cy) in enumerate(cells)):
                        for i, (cx, cy) in enumerate(cells):
                            grid[cy][cx] = w[i]
                            hits.add((cx, cy))
                        placed = True
                        break
                if not placed:
                    ok = False
                    break
            if ok:
                letters = 'ABCDEFGHIJKLMNOPRSTUVWY'
                for yy in range(n):
                    for xx in range(n):
                        if not grid[yy][xx]:
                            grid[yy][xx] = rnd.choice(letters)
                return grid, hits
        raise ValueError('word search: could not place words; make the grid bigger')

    def html(self, key):
        rows = ''.join('<tr>' + ''.join(
            f'<td class="{"hit" if (x, y) in self.hits else ""}">{c}</td>' for x, c in enumerate(row)) + '</tr>'
            for y, row in enumerate(self.grid))
        words = ''.join(f'<span>{w.lower()}</span>' for w in sorted(self.words))
        return f'<table class="ws-grid">{rows}</table><div class="ws-words">{words}</div>'


class Part(Block):
    """A lettered sub-question inside Q: a), b)... (lettered in the order they are rendered)."""
    counter = 0

    def __init__(self, prompt, *answer_blocks):
        self.prompt, self.answer_blocks = prompt, answer_blocks

    def html(self, key):
        letter = 'abcdefghij'[Part.counter]
        Part.counter += 1
        return (f'<div class="part"><span class="lab">{letter})</span>{rich(self.prompt)}'
                f'{render(self.answer_blocks, key)}</div>')


class Q(Block):
    """A numbered question. Content: prompt text + any blocks (Lines, Blanks, Part, ...)."""
    counter = 0

    def __init__(self, prompt, *content, marks=None):
        self.prompt, self.content, self.marks = prompt, content, marks

    def html(self, key):
        Q.counter += 1
        Part.counter = 0
        marks = f'<span class="marks">[{self.marks}]</span>' if self.marks else ''
        return (f'<div class="q"><span class="num">{Q.counter}</span>{marks}'
                f'<div class="prompt">{rich(self.prompt)}</div>{render(self.content, key)}</div>')


class SelfCheck(Block):
    def __init__(self, statements):
        self.statements = statements

    def html(self, key):
        import art
        faces = ''.join(f'<th>{art.face(m)}<br>{t}</th>' for m, t in (('sad', 'Not yet'), ('meh', 'Nearly'), ('happy', 'Got it!')))
        rows = ''.join(f'<tr><td>{rich(s)}</td>' + '<td class="c"><svg width="18" height="18"><circle cx="9" cy="9" r="7.5" fill="none" stroke="#111" stroke-width="1.4"/></svg></td>' * 3 + '</tr>'
                       for s in self.statements)
        return (f'<div class="box think"><div class="bt">{icon("checklist")}How am I doing? Colour or tick a circle.</div>'
                f'<table class="selfcheck"><tr><th style="text-align:left">I can…</th>{faces}</tr>{rows}</table></div>')
