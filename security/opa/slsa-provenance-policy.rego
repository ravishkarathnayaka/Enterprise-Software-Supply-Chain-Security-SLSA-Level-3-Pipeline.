package supplychain.slsa

default allow = false

# Allow only if predicateType is SLSA v0.2 or v1.0 and builder is GitHub Actions
allow {
    input.predicateType == "https://slsa.dev/provenance/v0.2"
    startswith(input.predicate.builder.id, "https://github.com/actions/runner")
}

allow {
    input.predicateType == "https://slsa.dev/provenance/v1"
    startswith(input.predicate.runDetails.builder.id, "https://github.com/actions/runner")
}
