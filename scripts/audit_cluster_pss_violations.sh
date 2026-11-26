#!/usr/bin/env bash
set -euo pipefail
# Audits all active namespaces for missing Pod Security Standards labels

echo "Auditing cluster namespaces for pod-security.kubernetes.io/enforce=restricted..."
kubectl get namespaces -o json | jq -r '.items[] | select(.metadata.labels["pod-security.kubernetes.io/enforce"] != "restricted") | .metadata.name' || true
echo "Audit completed."
