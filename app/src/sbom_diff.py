"""Software Bill of Materials (SBOM) Diff & Drift Detection Engine.

Compares two lists of package components to identify added, removed, or version-bumped packages.
"""

from typing import Any, Dict, List, Set


class SbomDiffer:
    """Computes architectural drift between SBOM component snapshots."""

    @staticmethod
    def compare_components(
        baseline: List[Dict[str, str]],
        candidate: List[Dict[str, str]],
    ) -> Dict[str, Any]:
        base_map = {item["name"]: item["version"] for item in baseline}
        cand_map = {item["name"]: item["version"] for item in candidate}

        added = [pkg for pkg in cand_map if pkg not in base_map]
        removed = [pkg for pkg in base_map if pkg not in cand_map]
        modified = [
            {"name": pkg, "old": base_map[pkg], "new": cand_map[pkg]}
            for pkg in base_map
            if pkg in cand_map and base_map[pkg] != cand_map[pkg]
        ]

        return {
            "drift_detected": len(added) > 0 or len(removed) > 0 or len(modified) > 0,
            "added_count": len(added),
            "removed_count": len(removed),
            "modified_count": len(modified),
            "added": added,
            "removed": removed,
            "modified": modified,
        }


sbom_differ = SbomDiffer()
