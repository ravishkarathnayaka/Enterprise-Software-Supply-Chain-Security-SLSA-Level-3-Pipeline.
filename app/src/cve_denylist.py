"""Emergency Zero-Day CVE Denylist Filter.

Blocks deployments containing immediate-threat zero-day vulnerabilities prior to CVE feed sync.
"""

from typing import Any, Dict, List, Set


class CVEDenylistFilter:
    """Evaluates component CVE identifiers against active emergency blocklists."""

    DENYLIST: Set[str] = {
        "CVE-2021-44228",  # Log4Shell
        "CVE-2022-22965",  # Spring4Shell
        "CVE-2023-38606",  # Kernel local privilege escalation
        "CVE-2024-3094",   # XZ Utils backdoor
    }

    @classmethod
    def check_cves(cls, cve_list: List[str]) -> Dict[str, Any]:
        blocked = [cve for cve in cve_list if cve in cls.DENYLIST]
        return {
            "rejected": len(blocked) > 0,
            "blocked_count": len(blocked),
            "blocked_cves": blocked,
        }


cve_denylist_filter = CVEDenylistFilter()
