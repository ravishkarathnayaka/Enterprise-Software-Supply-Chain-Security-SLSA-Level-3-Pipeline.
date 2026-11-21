# SIEM & SOAR Integration Architecture for Supply Chain Telemetry

## 1. Telemetry Ingestion Pipeline
Kyverno admission webhook audit records, Falco runtime alerts, and Cosign verification failures stream to centralized SIEM:
```
Kyverno Webhook ──► FluentBit / OpenTelemetry ──► Splunk / Elasticsearch ──► Automated SOAR Playbook
```

---

## 2. Alert Priority Mappings
- **SEV-1**: Signature mismatch on production deployment attempt.
- **SEV-2**: Build provenance lacking SLSA Level 3 builder claims.
- **SEV-3**: Expired VEX vulnerability exemption.
