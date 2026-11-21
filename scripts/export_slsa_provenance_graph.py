#!/usr/bin/env python3
"""Generate Graphviz DOT diagram from SLSA provenance materials."""

import json
import sys


def export_dot(provenance_path: str, dot_path: str):
    with open(provenance_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    builder = (
        data.get("predicate", {}).get("builder", {}).get("id", "UnknownBuilder")
    )
    subjects = [s.get("name", "artifact") for s in data.get("subject", [])]

    with open(dot_path, "w", encoding="utf-8") as f:
        f.write("digraph SLSA_Provenance {\n")
        f.write("  rankdir=LR;\n")
        f.write(f'  "{builder}" [shape=box, color=blue];\n')
        for s in subjects:
            f.write(f'  "{builder}" -> "{s}" [label="builds"];\n')
        f.write("}\n")
    print(f"Exported provenance graph to {dot_path}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(
            "Usage: export_slsa_provenance_graph.py <provenance.json> <output.dot>"
        )
        sys.exit(0)
    export_dot(sys.argv[1], sys.argv[2])
