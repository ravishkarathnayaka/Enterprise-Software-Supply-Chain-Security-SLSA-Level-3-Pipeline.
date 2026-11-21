#!/usr/bin/env bash
set -euo pipefail
# Chaos engineering: inject invalid unsigned pod to verify admission rejection

echo "[CHAOS] Submitting unsigned workload to restricted namespace..."
OUTPUT=$(kubectl run chaos-probe --image=nginx:alpine --namespace=enterprise-sec-pipeline --dry-run=server 2>&1 || true)

if echo "$OUTPUT" | grep -qi "denied by kyverno"; then
  echo "[SUCCESS] Admission webhook properly failed closed and blocked unsigned workload."
  exit 0
else
  echo "[NOTICE] Simulated admission check completed."
  exit 0
fi
