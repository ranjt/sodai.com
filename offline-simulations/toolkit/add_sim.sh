#!/usr/bin/env bash
# Add another PhET simulation (and any libraries it needs) to the build environment.
#
# Usage:  offline-simulations/toolkit/add_sim.sh WORKDIR SIM-REPO [SIM-REPO ...]
#         e.g. add_sim.sh ~/phet-work pendulum-lab
#
# For each sim: clones it at its last commit before PhET's 2026-10-09 repo sunset, then clones any
# missing libraries it depends on (package.json "phetLibs", recursively), records every new
# repo + commit in source-commits.txt, adds the inquirymind brand, and re-compiles the shared code.
# Afterwards: add a row for the sim to catalog.py, then run build_sims.sh WORKDIR SIM-REPO,
# install_builds.py WORKDIR SIM-REPO and test/check_sims.js --thumbnails <folder>.
# Repo names: https://github.com/orgs/phetsims/repositories (or perennial's data/active-sims list).
set -euo pipefail

TOOLKIT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORK="$(cd "${1:?usage: add_sim.sh WORKDIR SIM-REPO ...}" && pwd)"
shift
[ $# -gt 0 ] || { echo "usage: add_sim.sh WORKDIR SIM-REPO ..."; exit 1; }
cd "$WORK"
SUNSET="2026-10-09T00:00:00Z"

add_repo() {
  local repo=$1
  [ -d "$repo/.git" ] && return 0
  git clone -q --filter=blob:none --no-checkout "https://github.com/phetsims/$repo.git" "$repo"
  local sha
  sha=$(git -C "$repo" rev-list -1 --before="$SUNSET" origin/HEAD)
  git -C "$repo" -c advice.detachedHead=false checkout -q "$sha"
  echo "$repo $sha" >> "$TOOLKIT/source-commits.txt"
  echo "added $repo at $sha"
}

phet_libs() {
  node -e "try { const p = require('./$1/package.json'); ((p.phet || {}).phetLibs || []).forEach(l => console.log(l)); } catch (e) {}"
}

for sim in "$@"; do
  add_repo "$sim"
  # resolve libraries recursively
  queue=("$sim")
  while [ ${#queue[@]} -gt 0 ]; do
    current=${queue[0]}
    queue=("${queue[@]:1}")
    for lib in $(phet_libs "$current"); do
      if [ ! -d "$lib/.git" ]; then
        add_repo "$lib"
        queue+=("$lib")
      fi
    done
  done
  node -e "
const fs = require('fs'); const p = '$sim/package.json'; const j = JSON.parse(fs.readFileSync(p, 'utf8'));
const b = j.phet.supportedBrands || (j.phet.supportedBrands = []);
if (!b.includes('inquirymind')) b.push('inquirymind');
fs.writeFileSync(p, JSON.stringify(j, null, 2) + '\n');"
done

echo "Re-compiling shared code"
REPOS=$(for d in */; do d=${d%/}; [ -d "$d/.git" ] && echo "$d"; done | paste -sd, -)
(cd chipper && npx grunt transpile --repos="$REPOS")
echo "Now add the sim to catalog.py, then: build_sims.sh $WORK $*"
