# Operational Runbook: DNS Hardening & Registry Poisoning Defense

## 1. Threat Description
Adversaries spoofing DNS responses to redirect container image pulls from legitimate registries to malicious mirrors.

---

## 2. Defensive Countermeasures
- **DNSSEC Validation**: Enforce DNSSEC on CoreDNS forwarders.
- **TLS SNI Verification**: Container runtimes verify TLS certificates against immutable registry public trust anchors.
- **Content-Addressable Digits**: Pinned SHA256 digests guarantee integrity even if DNS is redirected.
