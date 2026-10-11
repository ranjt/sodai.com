"""Download hub page for the worksheet packs (placeholder; full page written later)."""
import os


def write(topics, out, strands, kinds):
    rows = ''.join(f'<li>{t.code} {t.title}: <a href="pdf/{t.slug}-study-pack.pdf">study pack</a> · '
                   f'<a href="pdf/{t.slug}-answer-key.pdf">answer key</a></li>' for t in topics)
    open(os.path.join(out, 'index.html'), 'w').write(f'<!doctype html><meta charset="utf-8"><ul>{rows}</ul>')
