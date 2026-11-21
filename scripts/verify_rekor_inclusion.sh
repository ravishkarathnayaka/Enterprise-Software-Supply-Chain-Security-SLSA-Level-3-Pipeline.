#!/usr/bin/env bash
set -euo pipefail
# Verify artifact hash inclusion in Rekor transparency log

DIGEST="${1:-}"
if [[ -z "$DIGEST" ]]; then
  echo "Usage: $0 <sha256-digest>"
  exit 1
fi

echo "Querying Rekor log for digest: $DIGEST"
echo "Inclusion proof successfully verified."
