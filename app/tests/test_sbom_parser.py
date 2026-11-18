"""Unit tests for CycloneDX SbomParser."""

import json
from src.sbom_parser import SbomParser


def test_cyclonedx_parser():
    sample_cyclonedx = json.dumps({
        "bomFormat": "CycloneDX",
        "specVersion": "1.5",
        "components": [
            {
                "name": "cryptography",
                "version": "42.0.5",
                "purl": "pkg:pypi/cryptography@42.0.5",
                "licenses": [{"license": {"id": "Apache-2.0"}}],
            }
        ],
    })
    components = SbomParser.parse_cyclonedx(sample_cyclonedx)
    assert len(components) == 1
    assert components[0].name == "cryptography"
    assert components[0].license == "Apache-2.0"
