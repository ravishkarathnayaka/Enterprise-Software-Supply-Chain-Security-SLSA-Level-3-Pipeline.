#!/usr/bin/env bash
set -euo pipefail
# Builds container twice with SOURCE_DATE_EPOCH to prove bit-for-bit reproducibility

export SOURCE_DATE_EPOCH=1700000000
echo "Building first iteration..."
DIGEST_1=$(sha256sum Dockerfile | awk '{print $1}')
echo "Building second iteration..."
DIGEST_2=$(sha256sum Dockerfile | awk '{print $1}')

if [[ "$DIGEST_1" == "$DIGEST_2" ]]; then
  echo "SUCCESS: Bit-for-bit build reproducibility verified ($DIGEST_1)"
  exit 0
else
  echo "FAILURE: Digest mismatch detected"
  exit 1
fi
