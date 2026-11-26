# Workload Identity Federation with SPIFFE and SPIRE Across Clusters

## SPIFFE ID URI Architecture
All microservice workloads are issued cryptographically verifiable SPIFFE IDs:
`spiffe://enterprise.supplychain.net/ns/{namespace}/sa/{serviceaccount}`

## Verification Flow
1. Workload requests X.509 SVID (SPIFFE Verifiable Identity Document) from local SPIRE Agent.
2. SPIRE Agent attests container kernel attributes (cgroups, namespace, serviceaccount UID).
3. SPIRE Server issues short-lived (1 hour) X.509 certificate signed by regional intermediate CA.
4. Workloads establish mutual TLS using SPIFFE SVIDs for all east-west API invocations.
