#!/usr/bin/env bash
# Publish the InquiryMind learning resources to the inquirymind.org Firebase site.
#
# Copies the ready-made folders next to this script (simulations, science-simulations, worksheets with all grades
# and the thinking routines) into the "public" folder of your Firebase project, then optionally deploys.
# Nothing is rebuilt: the worksheets, PDFs and pages are used exactly as they are.
#
# Usage (on your Mac, in Terminal):
#   bash publish.sh ~/path/to/inquirymind-firebase-project               # copy only, check locally first
#   bash publish.sh ~/path/to/inquirymind-firebase-project --deploy      # copy and publish
#   bash publish.sh ~/path/to/inquirymind-firebase-project --only worksheets --deploy
#
# Needs: the Firebase CLI for --deploy (npm install -g firebase-tools, then firebase login once).
set -euo pipefail

SRC="$(cd "$(dirname "$0")" && pwd)"
PROJECT="${1:?Usage: bash publish.sh /path/to/firebase-project [--only worksheets] [--deploy]}"
shift
DEPLOY=0
FOLDERS="simulations science-simulations worksheets"
while [ $# -gt 0 ]; do
  case "$1" in
    --deploy) DEPLOY=1 ;;
    --only) FOLDERS="${2:?--only needs a folder name: simulations, science-simulations or worksheets}"; shift ;;
    *) echo "Unknown option: $1"; exit 1 ;;
  esac
  shift
done

[ -f "$PROJECT/firebase.json" ] || { echo "No firebase.json in $PROJECT - is this your Firebase project folder?"; exit 1; }

# The hosting folder named in firebase.json ("public" unless you changed it).
PUBLIC_DIR=$(sed -n 's/.*"public"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p' "$PROJECT/firebase.json" | head -1)
TARGET="$PROJECT/${PUBLIC_DIR:-public}"
mkdir -p "$TARGET"

for d in $FOLDERS; do
  [ -d "$SRC/$d" ] || { echo "Missing $SRC/$d"; exit 1; }
  # Replaces only this one folder, so the rest of your site is never touched.
  if command -v rsync >/dev/null 2>&1; then
    rsync -a --delete "$SRC/$d/" "$TARGET/$d/"
  else
    rm -rf "${TARGET:?}/${d:?}" && cp -R "$SRC/$d" "$TARGET/$d"
  fi
  echo "copied $d/ -> $TARGET/$d/"
done

if [ "$DEPLOY" = 1 ]; then
  (cd "$PROJECT" && firebase deploy --only hosting)
  echo "Live: https://www.inquirymind.org/worksheets/ and /worksheets/thinking-routines/"
else
  echo "Copied. Preview with: (cd \"$PROJECT\" && firebase serve) then open http://localhost:5000/worksheets/"
  echo "Publish with: bash publish.sh \"$PROJECT\" --deploy"
fi
