"""Vulnerability Exploitability eXchange (VEX) Evaluator.

Parses VEX statements and determines real-world exploitability of reported CVEs.
"""

from enum import Enum
from typing import Dict, List, Optional
from pydantic import BaseModel, Field


class VexStatus(str, Enum):
    NOT_AFFECTED = "not_affected"
    AFFECTED = "affected"
    FIXED = "fixed"
    UNDER_INVESTIGATION = "under_investigation"


class VexStatement(BaseModel):
    vulnerability_id: str = Field(..., description="CVE ID (e.g., CVE-2026-1188)")
    status: VexStatus
    justification: Optional[str] = Field(None, description="VEX justification code")
    remediation_notes: Optional[str] = None


class VexEvaluator:
    """Evaluates software bill of materials against active VEX advisories."""

    def __init__(self) -> None:
        self._statements: Dict[str, VexStatement] = {}

    def register_statement(self, stmt: VexStatement) -> None:
        self._statements[stmt.vulnerability_id.upper()] = stmt

    def evaluate_cve(self, vulnerability_id: str) -> Dict[str, str]:
        cve_key = vulnerability_id.upper()
        if cve_key in self._statements:
            stmt = self._statements[cve_key]
            return {
                "cve": cve_key,
                "status": stmt.status.value,
                "action": "ALLOW" if stmt.status == VexStatus.NOT_AFFECTED else "BLOCK",
            }
        return {
            "cve": cve_key,
            "status": "unassessed",
            "action": "BLOCK_BY_DEFAULT",
        }


vex_evaluator = VexEvaluator()
