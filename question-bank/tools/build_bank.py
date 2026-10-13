"""Build the question bank (run from the repository root):
    python3 question-bank/tools/build_bank.py
1. validates every file in question-bank/questions/ (stops on errors);
2. writes question-bank/dist/: all-questions.json, <grade>.json per grade, manifest.json (counts per grade, strand,
   topic, mode and type) and questions.js (for the preview page);
3. copies question-bank/ (dist, images, preview, README) to offline-simulations/inquirymind-site/question-bank/.
Open question-bank/preview/index.html in a browser to see every question with its answer."""
import glob
import json
import os
import shutil
import subprocess
import sys

QB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT = os.path.dirname(QB)
DIST = os.path.join(QB, 'dist')
GRADE_SLUG = {0: 'kg', 1: 'grade-1', 2: 'grade-2', 3: 'grade-3', 4: 'grade-4', 5: 'grade-5'}
GRADE_NAME = {0: 'KG', 1: 'Grade 1', 2: 'Grade 2', 3: 'Grade 3', 4: 'Grade 4', 5: 'Grade 5'}
STRAND_NAME = {'skills': 'Working scientifically', 'living': 'Living things', 'earth': 'Earth and space', 'physical': 'Physical and chemical science'}
SITE_CODE = {'skills': 'W', 'living': 'L', 'earth': 'E', 'physical': 'P'}
MODE_NAME = {'core': 'Mixed review', 'picture': 'Picture quiz', 'real-life': 'Real-life choices', 'simulation': 'Simulation questions',
             'olympiad': 'Olympiad challenge'}
ORDER = {'skills': 0, 'living': 1, 'earth': 2, 'physical': 3}


def load():
    topics = []
    for f in sorted(glob.glob(os.path.join(QB, 'questions', '*', '*.json'))):
        d = json.load(open(f, encoding='utf-8'))
        d['file'] = os.path.relpath(f, QB)
        topics.append(d)
    return sorted(topics, key=lambda d: (d['grade'], ORDER[d['strand']], d['topic'][0], int(d['topic'][1:])))


def main():
    rc = subprocess.run([sys.executable, os.path.join(QB, 'tools', 'validate.py')], capture_output=True, text=True)
    print(rc.stdout.strip().splitlines()[-1] if rc.stdout.strip() else rc.stderr)
    if rc.returncode:
        print('\n'.join(line for line in rc.stdout.splitlines() if line.startswith('ERROR'))[:4000])
        sys.exit('fix the errors above first')
    topics = load()
    os.makedirs(DIST, exist_ok=True)
    flat, manifest = [], {'title': 'InquiryMind science question bank', 'grades': [], 'totals': {}, 'modes': MODE_NAME,
                          'strands': {k: {'name': v, 'site_code': SITE_CODE[k]} for k, v in STRAND_NAME.items()}}
    per_grade = {}
    for d in topics:
        g = d['grade']
        site_strand_index = sum(1 for t in topics if t['grade'] == g and t['strand'] == d['strand'] and
                                (ORDER[t['strand']], t['topic'][0], int(t['topic'][1:])) < (ORDER[d['strand']], d['topic'][0], int(d['topic'][1:]))) + 1
        info = {'grade': g, 'grade_name': GRADE_NAME[g], 'topic': d['topic'], 'title': d['title'], 'strand': d['strand'],
                'site_skill': f'{SITE_CODE[d["strand"]]}{site_strand_index}', 'worksheet': d.get('worksheet')}
        for q in d['questions']:
            flat.append({**info, **q})
        per_grade.setdefault(g, []).append({**info, 'file': d['file'], 'count': len(d['questions']),
                                            'modes': {m: sum(1 for q in d['questions'] if q['mode'] == m) for m in MODE_NAME},
                                            'types': {}})
        for q in d['questions']:
            per_grade[g][-1]['types'][q['type']] = per_grade[g][-1]['types'].get(q['type'], 0) + 1
    for g, ts in sorted(per_grade.items()):
        qs = [q for q in flat if q['grade'] == g]
        with open(os.path.join(DIST, f'{GRADE_SLUG[g]}.json'), 'w', encoding='utf-8') as f:
            json.dump({'grade': g, 'grade_name': GRADE_NAME[g], 'questions': qs}, f, ensure_ascii=False, indent=1)
        manifest['grades'].append({'grade': g, 'grade_name': GRADE_NAME[g], 'file': f'dist/{GRADE_SLUG[g]}.json', 'questions': len(qs),
                                   'modes': {m: sum(1 for q in qs if q['mode'] == m) for m in MODE_NAME}, 'topics': ts})
    manifest['totals'] = {'questions': len(flat), 'topics': len(topics),
                          'modes': {m: sum(1 for q in flat if q['mode'] == m) for m in MODE_NAME},
                          'types': {t: sum(1 for q in flat if q['type'] == t) for t in sorted({q['type'] for q in flat})}}
    with open(os.path.join(DIST, 'all-questions.json'), 'w', encoding='utf-8') as f:
        json.dump({'questions': flat}, f, ensure_ascii=False, indent=1)
    with open(os.path.join(DIST, 'manifest.json'), 'w', encoding='utf-8') as f:
        json.dump(manifest, f, ensure_ascii=False, indent=1)
    with open(os.path.join(DIST, 'questions.js'), 'w', encoding='utf-8') as f:
        f.write('window.QB = ' + json.dumps({'manifest': manifest, 'questions': flat}, ensure_ascii=False) + ';\n')
    print(f'{len(flat)} questions in {len(topics)} topics → question-bank/dist/')
    im = os.path.join(ROOT, 'offline-simulations', 'inquirymind-site', 'question-bank')
    if os.path.isdir(os.path.dirname(im)):
        shutil.rmtree(im, ignore_errors=True)
        for sub in ('dist', 'images', 'preview'):
            shutil.copytree(os.path.join(QB, sub), os.path.join(im, sub))
        shutil.copy(os.path.join(QB, 'README.md'), im)
        print('copied to', os.path.relpath(im, ROOT))


if __name__ == '__main__':
    main()
