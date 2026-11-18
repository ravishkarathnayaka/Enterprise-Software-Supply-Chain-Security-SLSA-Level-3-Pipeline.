#!/usr/bin/env bash
# ==============================================================================
# Admission Webhook Latency Benchmarking
# ==============================================================================
set -euo pipefail

echo "Measuring Kyverno admission verification latency over 10 test admissions..."
for i in {1..10}; do
    START=$(date +%s%N)
    kubectl apply -f kubernetes/manifests/deployment.yaml --dry-run=server > /dev/null
    END=$(date +%s%N)
    DURATION=$(( (END - START) / 1000000 ))
    echo "  Iteration $i: ${DURATION} ms"
done
