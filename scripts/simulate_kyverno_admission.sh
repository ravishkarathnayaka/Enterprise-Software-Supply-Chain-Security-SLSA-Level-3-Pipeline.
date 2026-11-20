#!/usr/bin/env bash
# ==============================================================================
# Local Kyverno Policy CLI Pre-Commit Simulator
# ==============================================================================
set -euo pipefail

echo "Executing Kyverno CLI policy dry-run tests..."
kyverno apply kubernetes/policies/ \
  --resource kubernetes/manifests/deployment.yaml \
  --table

echo "[SUCCESS] Local Kyverno policy evaluation complete."
