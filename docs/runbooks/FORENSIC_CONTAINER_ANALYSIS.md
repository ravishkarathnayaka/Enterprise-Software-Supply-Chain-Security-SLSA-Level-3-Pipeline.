# Operational Runbook: Live Container Forensic Acquisition

## 1. Trigger
High-severity Falco alert indicating suspicious process execution or binary tampering in a running pod.

---

## 2. Live Acquisition Workflow
1. **Pause Container**: Prevent state changes while acquiring volatile memory:
   ```bash
   crictl pause <container-id>
   ```
2. **Checkpoint State**: Create container checkpoint using containerd CRI:
   ```bash
   crictl checkpoint --export=/tmp/forensic-checkpoint.tar <container-id>
   ```
3. **Capture Memory**: Extract `/proc/<pid>/mem` to secure evidence storage.
