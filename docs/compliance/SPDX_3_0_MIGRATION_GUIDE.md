# SPDX 3.0 Model Migration Roadmap

## 1. Motivation
SPDX 3.0 shifts from flat document structures to a graph-based core object model, separating software packages, licensing, security, and build profiles into modular profiles.

---

## 2. Migration Phases
- **Phase 1**: Dual generation of SPDX 2.3 and CycloneDX 1.5 JSON (Current).
- **Phase 2**: Ingest and index SPDX 3.0 JSON-LD graphs via Syft.
- **Phase 3**: Enforce SPDX 3.0 security profiles in Kyverno admission policies.
