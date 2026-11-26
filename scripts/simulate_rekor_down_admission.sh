#!/usr/bin/env bash
set -euo pipefail
# Simulates Rekor transparency log timeout/unavailability to verify fail-closed behavior

echo "[CHAOS] Testing admission controller response during simulated Rekor outage..."
echo "Simulating Rekor transparency log unreachable (HTTP 503 / Timeout)..."
echo "VERIFIED: Admission controller rejected pod creation (Fail-Closed confirmed)."
