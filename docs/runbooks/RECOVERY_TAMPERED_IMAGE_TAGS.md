# Remediation Guide: Registry Image Tag Poisoning & Tampering Recovery

## Overview
Image tags (e.g., `:latest`, `:v1.0.0`) are mutable pointers. If an adversary overwrites a tag with malicious layers, admission verification must catch and block deployment.

## Recovery Steps
1. **Audit Failed Admission Logs**: Query Kyverno admission logs for signature verification failures.
2. **Re-pin Deployment to Immutable Digest**: Update Kubernetes Deployment spec from mutable tag to `@sha256:...`.
3. **Lock Registry Immutability**: Enable tag immutability settings in GitHub Packages / AWS ECR.
4. **Trigger Post-Mortem**: Document root cause in incident tracking system.
