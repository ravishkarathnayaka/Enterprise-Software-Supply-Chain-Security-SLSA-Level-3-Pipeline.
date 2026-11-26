package supplychain.spiffe

default allow = false

expected_trust_domain := "enterprise.supplychain.net"

allow if {
    input.trust_domain == expected_trust_domain
    startswith(input.spiffe_id, "spiffe://enterprise.supplychain.net/ns/")
}
