# in-toto ITE-6: Generic In-Toto Attestation Specification

## 1. Overview
In-toto Enhancement Proposal 6 (**ITE-6**) defines the generalized envelope format for software attestations across arbitrary metadata formats (SLSA, SPDX, CycloneDX, VEX).

---

## 2. Envelope Structure
```
DSSE Envelope {
  payloadType: "application/vnd.in-toto+json",
  payload: Base64(Statement {
    _type: "https://in-toto.io/Statement/v0.1",
    subject: [{name, digest}],
    predicateType: "<URI>",
    predicate: {...}
  }),
  signatures: [{keyid, sig}]
}
```
