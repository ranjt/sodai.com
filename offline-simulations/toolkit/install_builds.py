"""
Copy built simulations into both site folders and regenerate the catalog pages.

Usage (from the repository root):
  python3 offline-simulations/toolkit/install_builds.py WORKDIR [sim-id ...]

For each sim (default: every sim in catalog.py) copies
  WORKDIR/<sim>/build/inquirymind/<sim>_en_inquirymind.html
to
  <folder>/sims/<sim>.html                                   (amrarbazar.com copy)
  offline-simulations/inquirymind-site/<folder>/sims/<sim>.html   (InquiryMind copy)
where <folder> is simulations/ (math) or science-simulations/ (science).
Thumbnails are not touched; make new ones with test/check_sims.js --thumbnails.
"""
import os
import shutil
import sys

import catalog

work = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else sys.exit(__doc__)
wanted = set(sys.argv[2:])
missing, copied = [], 0
for key, cat in catalog.CATALOGS.items():
    for sim in cat['sims']:
        sid = sim[0]
        if wanted and sid not in wanted:
            continue
        built = os.path.join(work, sid, 'build', 'inquirymind', f'{sid}_en_inquirymind.html')
        if not os.path.exists(built):
            missing.append(sid)
            continue
        for root in catalog.SITE_ROOTS.values():
            dest = os.path.join(catalog.REPO, root, cat['folder'], 'sims')
            os.makedirs(dest, exist_ok=True)
            shutil.copy(built, os.path.join(dest, f'{sid}.html'))
        copied += 1

catalog.write_pages()
print(f'copied {copied} simulation(s) into both sites')
if missing:
    print('NOT BUILT (skipped):', ' '.join(missing))
