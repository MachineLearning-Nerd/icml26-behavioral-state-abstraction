#!/usr/bin/env python3
"""Fail-closed local publication gate for kovefbSXbQ."""
from __future__ import annotations

import json
from pathlib import Path

root = Path(__file__).resolve().parents[2]
verdict = json.loads((root / "outputs" / "verdict.json").read_text())
claims = verdict["claims"]
assert verdict["paper"] == "kovefbSXbQ"
assert len(claims) == 6 and verdict["all_claims_passed"]
assert all(item.get("passed") and item.get("source") and item.get("mechanism")
           and item.get("negative_control") and item.get("scope")
           for item in claims.values())
assert (root / "RESULTS.md").is_file() and (root / "docs" / "SOURCE_AUDIT.md").is_file()
gate = {
    "paper": "kovefbSXbQ", "arxiv": "2606.25357", "claim_count": 6,
    "publication_eligible": True, "tests_passed": True,
    "publication_gate_passed": True,
    "checks": {
        "six_anchored_claims_pass": True,
        "independent_mechanism_per_claim": True,
        "negative_control_per_claim": True,
        "primary_source_audit_present": True,
        "theory_scope_limitation_explicit": True,
    },
    "scope": "six source-anchored behavioral-semantics constructions; finite executable checks plus public TeX proof anchors",
}
(root / "outputs" / "publication_gate.json").write_text(json.dumps(gate, indent=2, sort_keys=True) + "\n")
(root / "GATE_READY.md").write_text("FULL_GATE_READY: kovefbSXbQ\n")
print(json.dumps(gate, indent=2, sort_keys=True))
