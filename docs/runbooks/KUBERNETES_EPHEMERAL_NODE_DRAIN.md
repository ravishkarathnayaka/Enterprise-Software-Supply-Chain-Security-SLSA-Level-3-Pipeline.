# Operational Runbook: Compromised Node Containment & Forensic Drain

## 1. Trigger
Alert received from Falco indicating container escape or unauthorized kernel module modification on worker node.

---

## 2. Immediate Containment Procedure
1. Cordon the node immediately to prevent new pod scheduling:
   ```bash
   kubectl cordon <node-name>
   ```
2. Isolate node network using Cloud Security Group / Calico GlobalNetworkPolicy:
   ```bash
   kubectl label node <node-name> security.enterprise.io/quarantine=true
   ```
3. Acquire volatile forensic evidence (RAM memory dump and container runtime state) before termination.
4. Drain remaining non-compromised pods:
   ```bash
   kubectl drain <node-name> --delete-emptydir-data --ignore-daemonsets --force
   ```
