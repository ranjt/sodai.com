#!/usr/bin/env bash
# Recreate the PhET build environment used for these simulations.
#
# Usage:  offline-simulations/toolkit/setup_phet.sh WORKDIR
#
# - clones every phetsims repo listed in source-commits.txt at its exact commit
#   (PhET emptied its public repos on 2026-10-09; the old commits are still in their history)
# - adds the InquiryMind brand and registers it with PhET's build tool (chipper)
# - installs build dependencies and compiles the shared code once
# Needs: git, node 18+ (tested with node 22), npm, internet access to github.com and registry.npmjs.org.
# Takes ~5 minutes and ~7 GB of disk. Safe to re-run (skips repos that are already cloned).
set -euo pipefail

TOOLKIT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORK="${1:?usage: setup_phet.sh WORKDIR}"
mkdir -p "$WORK"
WORK="$(cd "$WORK" && pwd)"
cd "$WORK"

echo "== 1/5 Cloning repos at pinned commits into $WORK"
clone_one() {
  local repo=$1 sha=$2 src=$1
  [ "$repo" = perennial-alias ] && src=perennial   # perennial-alias is a second copy of perennial
  if [ ! -d "$repo/.git" ]; then
    git clone -q --filter=blob:none --no-checkout "https://github.com/phetsims/$src.git" "$repo"
  fi
  git -C "$repo" -c advice.detachedHead=false checkout -q "$sha"
}
export -f clone_one
xargs -P 8 -L 1 bash -c 'clone_one "$0" "$1" || echo "FAILED: $0"' < "$TOOLKIT/source-commits.txt"

# chipper runs `git rev-parse HEAD` in the parent directory, so WORKDIR itself must be a git repo with a commit
if [ ! -d .git ]; then
  git init -q && git -c user.email=build@local -c user.name=build commit -q --allow-empty -m "build root"
fi

echo "== 2/5 Adding the inquirymind brand"
rm -rf brand/inquirymind
cp -r "$TOOLKIT/brand/inquirymind" brand/inquirymind

echo "== 3/5 Registering the brand with chipper and the simulations"
sed -i.bak "s/BRANDS: \[ 'phet', 'phet-io', 'adapted-from-phet' \]/BRANDS: [ 'phet', 'phet-io', 'adapted-from-phet', 'inquirymind' ]/" \
  chipper/js/common/ChipperConstants.ts && rm -f chipper/js/common/ChipperConstants.ts.bak
grep -q "'inquirymind'" chipper/js/common/ChipperConstants.ts || { echo "Could not patch ChipperConstants.ts"; exit 1; }
node -e "
const fs = require('fs');
const b = JSON.parse(fs.readFileSync('chipper/build.json', 'utf8'));
b.inquirymind = { preload: [ '../brand/inquirymind/js/inquirymind-splash.js' ] };
fs.writeFileSync('chipper/build.json', JSON.stringify(b, null, 2) + '\n');
for (const sim of process.argv.slice(1)) {
  const p = sim + '/package.json';
  if (!fs.existsSync(p)) { console.log('missing sim repo: ' + sim); continue; }
  const j = JSON.parse(fs.readFileSync(p, 'utf8'));
  const brands = j.phet.supportedBrands || (j.phet.supportedBrands = []);
  if (!brands.includes('inquirymind')) brands.push('inquirymind');
  fs.writeFileSync(p, JSON.stringify(j, null, 2) + '\n');
}" $(python3 "$TOOLKIT/catalog.py" ids)

echo "== 4/5 Installing build dependencies (chipper, perennial-alias)"
(cd chipper && npm install --no-audit --no-fund --loglevel=error)
(cd perennial-alias && npm install --no-audit --no-fund --loglevel=error)

echo "== 5/5 Compiling shared code once (builds then use --transpile=false)"
REPOS=$(for d in */; do d=${d%/}; [ -d "$d/.git" ] && echo "$d"; done | paste -sd, -)
(cd chipper && npx grunt transpile --clean --repos="$REPOS")

echo "Done. Next: offline-simulations/toolkit/build_sims.sh $WORK"
