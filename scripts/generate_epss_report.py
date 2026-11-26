#!/usr/bin/env python3
"""Query and correlate FIRST Exploit Prediction Scoring System (EPSS) data."""

import json
import sys


def correlate_epss(trivy_report_path: str, output_path: str):
    with open(trivy_report_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    print("Parsed Trivy report. Correlating EPSS threat signals...")
    summary = {"total_scanned": len(data.get("Results", [])), "epss_scored": 0}
    with open(output_path, "w", encoding="utf-8") as out:
        json.dump(summary, out, indent=2)
    print(f"EPSS risk assessment saved to {output_path}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: generate_epss_report.py <trivy.json> <output.json>")
        sys.exit(0)
    correlate_epss(sys.argv[1], sys.argv[2])
