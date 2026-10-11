"""Inline Tabler icons (MIT, https://tabler.io/icons). Only the icons used are kept in toolkit/icons/.
To add one: copy node_modules/@tabler/icons/icons/outline/<name>.svg into toolkit/icons/."""
import os
import re

HERE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'icons')
_cache = {}


def icon(name, cls='ico', size=None):
    if name not in _cache:
        path = os.path.join(HERE, f'{name}.svg')
        if not os.path.exists(path):
            raise FileNotFoundError(f'icon {name!r} missing: copy it from @tabler/icons into {HERE}')
        svg = re.sub(r'<!--.*?-->', '', open(path).read(), flags=re.S)
        svg = re.sub(r'\s+', ' ', svg).strip()
        svg = re.sub(r'\s(class|width|height)="[^"]*"', '', svg, count=3)
        _cache[name] = svg
    attrs = f'class="{cls}"' + (f' width="{size}" height="{size}"' if size else '')
    return _cache[name].replace('<svg', f'<svg {attrs}', 1)
