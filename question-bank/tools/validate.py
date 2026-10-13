"""Check question-bank files. Usage (from the repository root):
    python3 question-bank/tools/validate.py                         # every file
    python3 question-bank/tools/validate.py question-bank/questions/grade-3   # one folder or file
Prints every problem; exit code 1 if there are errors. Warnings do not fail the run."""
import glob
import importlib.util
import json
import os
import re
import sys

QB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT = os.path.dirname(QB)
IMAGES = os.path.join(QB, 'images')

GRADES = {0: 'kg', 1: 'grade-1', 2: 'grade-2', 3: 'grade-3', 4: 'grade-4', 5: 'grade-5'}
ID_PREFIX = {0: 'kg', 1: 'g1', 2: 'g2', 3: 'g3', 4: 'g4', 5: 'g5'}
STRANDS = {'skills', 'living', 'earth', 'physical'}
MODES = {'core', 'picture', 'real-life', 'simulation', 'olympiad'}
TYPES = {'mcq', 'multi', 'truefalse', 'fill', 'match', 'sort', 'order', 'short'}
BLOOM = {'remember', 'understand', 'apply', 'analyse', 'evaluate', 'create'}


def sim_ids():
    spec = importlib.util.spec_from_file_location('catalog', os.path.join(ROOT, 'offline-simulations', 'toolkit', 'catalog.py'))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return {s[0] for s in m.CATALOGS['science']['sims']}


SIMS = sim_ids()


class Report:
    def __init__(self):
        self.errors, self.warnings = [], []

    def err(self, where, msg):
        self.errors.append(f'ERROR {where}: {msg}')

    def warn(self, where, msg):
        self.warnings.append(f'warn  {where}: {msg}')


def image_ok(src):
    return isinstance(src, str) and os.path.isfile(os.path.join(IMAGES, src))


def check_choice(c, where, r, what='option'):
    """A choice is text, or {"text": ..., "image": ...} (image relative to question-bank/images)."""
    if isinstance(c, str):
        if not c.strip():
            r.err(where, f'empty {what}')
        return c.strip().lower()
    if isinstance(c, dict):
        if not (c.get('text') or c.get('image')):
            r.err(where, f'{what} needs text or image')
        if c.get('image') and not image_ok(c['image']):
            r.err(where, f'{what} image not found: {c["image"]}')
        return (c.get('text') or c.get('image')).strip().lower()
    r.err(where, f'{what} must be text or {{text, image}}')
    return ''


def check_question(q, f, ctx, r, seen):
    qid = q.get('id', '?')
    where = f'{os.path.relpath(f, QB)} {qid}'
    want = f'{ID_PREFIX[ctx["grade"]]}-{ctx["topic"].lower()}-'
    if not re.fullmatch(re.escape(want) + r'\d{3}', qid or ''):
        r.err(where, f'id must look like {want}001')
    if qid in seen:
        r.err(where, f'duplicate id (also in {seen[qid]})')
    seen[qid] = os.path.relpath(f, QB)
    for key, allowed in (('mode', MODES), ('type', TYPES), ('bloom', BLOOM)):
        if q.get(key) not in allowed:
            r.err(where, f'{key} must be one of {sorted(allowed)}')
    if q.get('difficulty') not in (1, 2, 3):
        r.err(where, 'difficulty must be 1, 2 or 3')
    stem = q.get('stem', '')
    if not isinstance(stem, str) or len(stem.strip()) < 3:
        r.err(where, 'stem missing')
    if not isinstance(q.get('explanation'), str) or len(q['explanation'].strip()) < 8:
        r.err(where, 'explanation missing (feedback shown after answering)')
    if q.get('image'):
        if not image_ok(q['image']):
            r.err(where, f'image not found: {q["image"]}')
        if not q.get('image_alt'):
            r.err(where, 'image_alt required with image')
    if q.get('mode') == 'picture' and not (q.get('image') or any(isinstance(o, dict) and o.get('image') for o in
                                                                q.get('options', []) + [x for p in q.get('pairs', []) for x in p] + [i[0] for i in q.get('items', [])] + q.get('sequence', []))):
        r.err(where, 'picture questions need an image (question image or picture options)')
    if q.get('mode') == 'simulation':
        sim = q.get('sim') or {}
        if sim.get('id') not in SIMS:
            r.err(where, f'sim.id must be a science simulation id, got {sim.get("id")!r}')
        if not sim.get('task'):
            r.err(where, 'sim.task (what to do in the simulation) required')
    elif q.get('sim'):
        r.warn(where, 'sim given but mode is not simulation')
    t = q.get('type')
    if t in ('mcq', 'multi'):
        opts = q.get('options')
        if not isinstance(opts, list) or not 2 <= len(opts) <= 6:
            r.err(where, 'options: 2 to 6 choices')
            return
        keys = [check_choice(o, where, r) for o in opts]
        if len(set(keys)) != len(keys):
            r.err(where, 'options must be different')
        a = q.get('answer')
        if t == 'mcq':
            if not isinstance(a, int) or not 0 <= a < len(opts):
                r.err(where, 'answer must be the index (0-based) of the right option')
            if ctx['grade'] > 0 and len(opts) < 3:
                r.warn(where, 'mcq with only 2 options (use truefalse?)')
        else:
            if not isinstance(a, list) or not a or len(set(a)) != len(a) or not all(isinstance(i, int) and 0 <= i < len(opts) for i in a):
                r.err(where, 'answer must be a list of right option indexes')
            elif len(a) == len(opts):
                r.err(where, 'multi: not every option can be right')
        for o in opts:
            if isinstance(o, str) and o.strip().lower() in ('all of the above', 'none of the above', 'both a and b'):
                r.warn(where, 'avoid "all/none of the above"')
    elif t == 'truefalse':
        if not isinstance(q.get('answer'), bool):
            r.err(where, 'truefalse answer must be true or false')
    elif t == 'fill':
        blanks = q.get('blanks')
        n = stem.count('___')
        if not isinstance(blanks, list) or len(blanks) != n or n == 0:
            r.err(where, f'fill: stem has {n} ___ but blanks has {len(blanks) if isinstance(blanks, list) else 0} entries')
        else:
            for b in blanks:
                if not isinstance(b, list) or not b or not all(isinstance(x, str) and x.strip() for x in b):
                    r.err(where, 'each blank is a list of accepted answers')
            bank = q.get('bank')
            if bank is not None:
                low = [x.lower() for x in bank]
                for b in blanks:
                    if b and b[0].lower() not in low:
                        r.err(where, f'bank must contain the answer {b[0]!r}')
                if len(bank) < n + 1:
                    r.warn(where, 'bank has no extra (distractor) word')
    elif t == 'match':
        pairs = q.get('pairs')
        if not isinstance(pairs, list) or not 3 <= len(pairs) <= 6 or not all(isinstance(p, list) and len(p) == 2 for p in pairs):
            r.err(where, 'match: 3 to 6 pairs [left, right]')
        else:
            lefts = [check_choice(p[0], where, r, 'left') for p in pairs]
            rights = [check_choice(p[1], where, r, 'right') for p in pairs]
            if len(set(lefts)) != len(lefts) or len(set(rights)) != len(rights):
                r.err(where, 'match sides must be different')
    elif t == 'sort':
        cats, items = q.get('categories'), q.get('items')
        if not isinstance(cats, list) or not 2 <= len(cats) <= 4:
            r.err(where, 'sort: 2 to 4 categories')
            return
        if not isinstance(items, list) or not 4 <= len(items) <= 10:
            r.err(where, 'sort: 4 to 10 items [item, category]')
            return
        for it in items:
            if not isinstance(it, list) or len(it) != 2 or it[1] not in cats:
                r.err(where, f'sort item {it!r} must be [item, one of the categories]')
            else:
                check_choice(it[0], where, r, 'item')
        used = {it[1] for it in items if isinstance(it, list) and len(it) == 2}
        if used != set(cats):
            r.err(where, 'every category needs at least one item')
    elif t == 'order':
        seq = q.get('sequence')
        if not isinstance(seq, list) or not 3 <= len(seq) <= 7:
            r.err(where, 'order: 3 to 7 items in the right order')
        else:
            keys = [check_choice(s, where, r, 'step') for s in seq]
            if len(set(keys)) != len(keys):
                r.err(where, 'order steps must be different')
    elif t == 'short':
        if not q.get('model_answer'):
            r.err(where, 'short: model_answer required')
        kw = q.get('keywords')
        if not isinstance(kw, list) or not kw or not all(isinstance(g, list) and g and all(isinstance(x, str) for x in g) for g in kw):
            r.err(where, 'short: keywords is a list of synonym lists, e.g. [["vibrate", "vibration"], ["ear"]]')
        elif not isinstance(q.get('min_keywords', 1), int) or not 1 <= q.get('min_keywords', 1) <= len(kw):
            r.err(where, 'short: min_keywords between 1 and the number of keyword groups')
        if ctx['grade'] == 0:
            r.warn(where, 'short written answers are hard in KG')
    if ctx['grade'] <= 1 and q.get('read_aloud') is not True:
        r.warn(where, 'KG and Grade 1 questions should have "read_aloud": true')
    if ctx['grade'] == 0 and len(stem.split()) > 16:
        r.warn(where, 'KG stem longer than 16 words')


def check_file(f, r, seen, stems):
    try:
        data = json.load(open(f, encoding='utf-8'))
    except Exception as e:  # noqa: BLE001
        r.err(os.path.relpath(f, QB), f'not valid JSON: {e}')
        return 0
    where = os.path.relpath(f, QB)
    for k in ('grade', 'topic', 'title', 'strand', 'questions'):
        if k not in data:
            r.err(where, f'missing {k}')
            return 0
    if data['grade'] not in GRADES:
        r.err(where, 'grade must be 0 (KG) to 5')
        return 0
    if os.path.basename(os.path.dirname(f)) != GRADES[data['grade']]:
        r.err(where, f'file should be in questions/{GRADES[data["grade"]]}/')
    if data['strand'] not in STRANDS:
        r.err(where, f'strand must be one of {sorted(STRANDS)}')
    if not re.fullmatch(r'[WABC]\d{1,2}', data['topic']):
        r.err(where, 'topic code like A1, C10, W1')
    if data.get('worksheet') and not os.path.isfile(os.path.join(ROOT, data['worksheet'])):
        r.err(where, f'worksheet not found: {data["worksheet"]}')
    qs = data['questions']
    if not isinstance(qs, list) or not qs:
        r.err(where, 'questions must be a non-empty list')
        return 0
    for q in qs:
        check_question(q, f, data, r, seen)
        key = (data['grade'], re.sub(r'\W+', ' ', str(q.get('stem', '')).lower()).strip(), json.dumps(q.get('options'), sort_keys=True))
        if key in stems:
            r.warn(f'{where} {q.get("id")}', f'same stem and options as {stems[key]}')
        stems[key] = q.get('id')
    modes = {m: sum(1 for q in qs if q.get('mode') == m) for m in MODES}
    types = {t: sum(1 for q in qs if q.get('type') == t) for t in TYPES}
    if modes['picture'] < 3:
        r.warn(where, f'only {modes["picture"]} picture questions')
    if modes['real-life'] < 2:
        r.warn(where, f'only {modes["real-life"]} real-life questions')
    if modes['olympiad'] < 1:
        r.warn(where, 'no olympiad (challenge) question')
    if len(qs) and types['mcq'] / len(qs) > 0.5:
        r.warn(where, f'{types["mcq"]} of {len(qs)} are mcq: mix the types more')
    return len(qs)


def main(paths):
    files = []
    for p in paths or [os.path.join(QB, 'questions')]:
        files += [p] if p.endswith('.json') else sorted(glob.glob(os.path.join(p, '**', '*.json'), recursive=True))
    r = Report()
    seen, stems = {}, {}
    n = sum(check_file(f, r, seen, stems) for f in files)
    for line in r.errors + r.warnings:
        print(line)
    print(f'{len(files)} files, {n} questions, {len(r.errors)} errors, {len(r.warnings)} warnings')
    return 1 if r.errors else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
