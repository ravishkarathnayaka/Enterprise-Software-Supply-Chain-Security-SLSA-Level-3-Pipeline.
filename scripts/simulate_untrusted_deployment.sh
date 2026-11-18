#!/usr/bin/env bash
# ==============================================================================
# Adversary Simulation: Attempt Deployment of Unsigned & Untrusted Pod
# ==============================================================================
set -euo pipefail

echo "Attempting to deploy untrusted/unsigned alpine image into secure namespace..."
if kubectl run attacker-shell \
  --image=alpine:latest \
  --namespace=secure-supply-chain \
  --restart=Never 2>&1 | grep -i "blocked by policy"; then
    echo "[PASS] Kyverno admission controller successfully blocked untrusted image."
else
    echo "[FAIL] Untrusted pod was not blocked!"
    kubectl delete pod attacker-shell -n secure-supply-chain --ignore-not-found=true
fi
