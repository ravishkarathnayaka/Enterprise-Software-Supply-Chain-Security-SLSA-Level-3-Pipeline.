"""Prometheus Metrics Instrumentation for SLSA Supply Chain Pipeline.

Provides thread-safe counters, gauges, and exposition in OpenMetrics/Prometheus format.
"""

import threading
from typing import Dict


class SupplyChainMetrics:
    """Collects runtime operational and security metrics."""

    def __init__(self) -> None:
        self._lock = threading.Lock()
        self._requests_total: Dict[str, int] = {}
        self._verifications_total: int = 0
        self._violations_total: int = 0

    def inc_request(self, endpoint: str, status_code: int) -> None:
        key = f"{endpoint}:{status_code}"
        with self._lock:
            self._requests_total[key] = self._requests_total.get(key, 0) + 1

    def inc_verification(self) -> None:
        with self._lock:
            self._verifications_total += 1

    def inc_violation(self) -> None:
        with self._lock:
            self._violations_total += 1

    def export_prometheus(self) -> str:
        """Exports metrics in standard Prometheus line protocol."""
        with self._lock:
            lines = [
                "# HELP supply_chain_requests_total Total HTTP requests handled.",
                "# TYPE supply_chain_requests_total counter",
            ]
            for key, count in self._requests_total.items():
                endpoint, status_code = key.split(":")
                lines.append(
                    f'supply_chain_requests_total{{endpoint="{endpoint}",status="{status_code}"}} {count}'
                )

            lines.extend([
                "# HELP supply_chain_verifications_total Total artifact integrity verifications passed.",
                "# TYPE supply_chain_verifications_total counter",
                f"supply_chain_verifications_total {self._verifications_total}",
                "# HELP supply_chain_security_violations_total Total security validation violations blocked.",
                "# TYPE supply_chain_security_violations_total counter",
                f"supply_chain_security_violations_total {self._violations_total}",
            ])
            return "\n".join(lines) + "\n"


metrics = SupplyChainMetrics()
