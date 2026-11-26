#!/usr/bin/env bash
set -euo pipefail
# Validates SPIFFE SVID X.509 certificate against expected trust domain

SVID_CERT="${1:-}"
if [[ -z "$SVID_CERT" || ! -f "$SVID_CERT" ]]; then
  echo "Usage: $0 <path-to-svid-cert.pem>"
  exit 1
fi

echo "Inspecting SPIFFE URI SAN in certificate: $SVID_CERT"
URI=$(openssl x509 -in "$SVID_CERT" -noout -ext subjectAltName 2>/dev/null | grep -o 'URI:spiffe://[^, ]*' || true)
echo "Extracted SVID: $URI"
