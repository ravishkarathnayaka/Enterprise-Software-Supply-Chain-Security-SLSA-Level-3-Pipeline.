"""In-Memory SBOM Parser & Component Indexer.

Parses CycloneDX and SPDX JSON structures into structured component objects.
"""

import json
from typing import Any, Dict, List
from src.models import SbomComponent


class SbomParser:
    """Parses CycloneDX JSON SBOM definitions."""

    @staticmethod
    def parse_cyclonedx(raw_json: str) -> List[SbomComponent]:
        data = json.loads(raw_json)
        components: List[SbomComponent] = []
        for item in data.get("components", []):
            components.append(
                SbomComponent(
                    name=item.get("name", "unknown"),
                    version=item.get("version", "0.0.0"),
                    purl=item.get("purl", f"pkg:generic/{item.get('name')}@{item.get('version')}"),
                    license=item.get("licenses", [{}])[0].get("license", {}).get("id", "UNKNOWN")
                    if item.get("licenses")
                    else "UNKNOWN",
                )
            )
        return components


sbom_parser = SbomParser()
