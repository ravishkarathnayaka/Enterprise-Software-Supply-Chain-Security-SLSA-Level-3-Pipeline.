# Triage Runbook: Anomalous Pod Outbound Egress Alerts

## Detection Event
Falco rule `Unauthorized Outbound Egress Connection` triggers a High-severity alert in the SIEM dashboard.

## Investigation Protocol
1. Identify source pod, namespace, and container ID:
   `kubectl get pods -n enterprise-sec-pipeline -o wide`
2. Inspect target remote IP, port, and DNS lookup history:
   `tcpdump -i any -nn dst port 53 or dst port 443`
3. If egress violates `network-policy-default-deny.yaml`, isolate pod immediately:
   `kubectl label pod <pod-name> quarantine=true --overwrite`
4. Capture memory dump of quarantined container before pod termination.
