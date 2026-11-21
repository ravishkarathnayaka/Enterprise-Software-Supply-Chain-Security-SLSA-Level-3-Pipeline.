# Operational Runbook: Continuous In-Cluster Image Pruning

## 1. Purpose
Prevents accumulation of dangling, unreferenced, or deprecated container images on Kubernetes worker nodes.

---

## 2. Automated Kubelet Garbage Collection Configuration
Worker nodes are configured with high and low watermarks for image disk utilization:
```yaml
imageGCHighThresholdPercent: 80
imageGCLowThresholdPercent: 65
imageMinimumGCAge: 2h
```
Workloads older than 30 days without active running pods are automatically pruned by cleanup cronjobs.
