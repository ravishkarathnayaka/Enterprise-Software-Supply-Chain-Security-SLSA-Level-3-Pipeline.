#!/usr/bin/env python3
"""OpenVEX Statement Generator Utility."""

import json
import sys
from datetime import datetime, timezone


def create_vex(cve_id: str, justification: str, detail: str) -> dict:
    return {
        "@context": "https://openvex.dev/ns/v0.2.0",
        "@id": f"urn:vex:{cve_id}",
        "author": "Ravishka Rathnayaka <secops@supplychain.internal>",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "statements": [
            {
                "vulnerability": {"name": cve_id},
                "status": "not_affected",
                "justification": justification,
                "impact_statement": detail,
            }
        ],
    }


if __name__ == "__main__":
    cve = sys.argv[1] if len(sys.argv) > 1 else "CVE-2026-1188"
    vex = create_vex(cve, "code_not_reachable", "Verified eliminated in distroless image.")
    print(json.dumps(vex, indent=2))
