"""Unit tests for Prometheus metrics collector."""

from src.metrics import SupplyChainMetrics


def test_metrics_collection_and_export():
    m = SupplyChainMetrics()
    m.inc_request("/healthz", 200)
    m.inc_request("/healthz", 200)
    m.inc_verification()
    m.inc_violation()

    output = m.export_prometheus()
    assert 'supply_chain_requests_total{endpoint="/healthz",status="200"} 2' in output
    assert "supply_chain_verifications_total 1" in output
    assert "supply_chain_security_violations_total 1" in output
