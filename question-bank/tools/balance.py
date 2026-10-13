"""Spread the right answers of multiple-choice questions evenly over the option positions (run from the repo root):
    python3 question-bank/tools/balance.py            # report only
    python3 question-bank/tools/balance.py --write    # rewrite the files
In each topic file the right option of every movable mcq is swapped with the option at a target position, so the
positions cycle A, B, C, D… in a shuffled order. Not moved: options that are labels or ordered values (A/B/C, 1/2/3,
numbers with units), because their order means something. Only the two swapped options change place."""
import glob
import json
import os
import random
import re
import sys

QB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ORDERED = re.compile(r'^\s*[-−]?[\d.,/½¼¾ ]+\s*(°C|°F|%|[a-zA-Z]{0,8}\.?)?\s*$|^[A-H]$|^[A-H] and [A-H]$|^\w+ ([A-H]|\d{1,2})$')


def text(o):
    return o if isinstance(o, str) else (o.get('text') or o.get('image') or '')


def movable(q):
    return q['type'] == 'mcq' and not all(ORDERED.match(text(o)) for o in q['options'])


def main(write):
    for f in sorted(glob.glob(os.path.join(QB, 'questions', '*', '*.json'))):
        d = json.load(open(f, encoding='utf-8'))
        rnd = random.Random(os.path.basename(f))
        qs = [q for q in d['questions'] if movable(q)]
        before = [q['answer'] for q in qs]
        slots = []
        for q in qs:
            n = len(q['options'])
            if not slots or not any(s < n for s in slots):
                slots = list(range(max(len(x['options']) for x in qs)))
                rnd.shuffle(slots)
            target = next(s for s in slots if s < n)
            slots.remove(target)
            a = q['answer']
            if target != a:
                q['options'][a], q['options'][target] = q['options'][target], q['options'][a]
                q['answer'] = target
        after = [q['answer'] for q in qs]
        count = lambda xs: '/'.join(str(xs.count(i)) for i in range(4))
        print(f'{os.path.relpath(f, QB):<55} {len(qs):>2} movable mcq  A/B/C/D before {count(before):<9} after {count(after)}')
        if write and before != after:
            with open(f, 'w', encoding='utf-8') as out:
                json.dump(d, out, ensure_ascii=False, indent=1)
                out.write('\n')


if __name__ == '__main__':
    main('--write' in sys.argv)
