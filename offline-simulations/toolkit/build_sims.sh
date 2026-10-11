#!/usr/bin/env bash
# Build simulations with the InquiryMind brand.
#
# Usage:  offline-simulations/toolkit/build_sims.sh WORKDIR [sim-id ...]
#         (no sim ids = every sim in catalog.py)
#
# Run setup_phet.sh first. Builds 3 sims at a time (~1 minute each).
# Output: WORKDIR/<sim>/build/inquirymind/<sim>_en_inquirymind.html ; logs in WORKDIR/logs/
#
# IMPORTANT: builds use --transpile=false. Letting parallel builds re-compile the shared code makes them
# overwrite each other's files and produces broken simulations. If you change any PhET source file,
# re-run the transpile step (step 5 of setup_phet.sh) before building.
set -euo pipefail

TOOLKIT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORK="$(cd "${1:?usage: build_sims.sh WORKDIR [sim-id ...]}" && pwd)"
shift
SIMS=("$@")
[ ${#SIMS[@]} -eq 0 ] && read -r -a SIMS <<< "$(python3 "$TOOLKIT/catalog.py" ids)"
mkdir -p "$WORK/logs"

build_one() {
  local work=$1 sim=$2
  cd "$work/$sim" || { echo "FAIL $sim (repo not cloned)"; return; }
  rm -rf build/inquirymind
  npm install --no-audit --no-fund --loglevel=error > /dev/null 2>&1
  if npx grunt build --brands=inquirymind --locales=en --transpile=false > "$work/logs/$sim.log" 2>&1 &&
     [ -f "build/inquirymind/${sim}_en_inquirymind.html" ]; then
    echo "OK   $sim"
  else
    echo "FAIL $sim (see $work/logs/$sim.log)"
  fi
}
export -f build_one

printf '%s\n' "${SIMS[@]}" | xargs -P 3 -I{} bash -c 'build_one "$0" "$1"' "$WORK" {}
echo "Next: python3 offline-simulations/toolkit/install_builds.py $WORK"
