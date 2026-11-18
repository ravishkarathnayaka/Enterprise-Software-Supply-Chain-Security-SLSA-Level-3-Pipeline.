#!/usr/bin/env bash
# ==============================================================================
# Deterministic Build Reproducibility Verification
# ==============================================================================
set -euo pipefail

COMMIT_EPOCH=$(git log -1 --format=%ct)
echo "Rebuilding image with fixed SOURCE_DATE_EPOCH=${COMMIT_EPOCH}..."

docker build \
  --build-arg SOURCE_DATE_EPOCH="${COMMIT_EPOCH}" \
  -t app:reproduced \
  ./app

DIGEST=$(docker inspect --format='{{index .Id}}' app:reproduced)
echo "Reproduced image digest: ${DIGEST}"
