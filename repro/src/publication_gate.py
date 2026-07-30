#!/usr/bin/env python3
"""Fail-closed local publication gate for kovefbSXbQ."""
from __future__ import annotations

import json
from pathlib import Path

root = Path(__file__).resolve().parents[2]
verdict = json.loads((root / "outputs" / "verdict.json").read_text())
claims = verdict["claims"]
claim_3 = json.loads((root / "outputs" / "proof_certificates.json").read_text())
assert verdict["paper"] == "kovefbSXbQ"
assert len(claims) == 6 and verdict["all_claims_passed"]
assert all(item.get("passed") and item.get("source") and item.get("mechanism")
           and item.get("negative_control") and item.get("scope")
           for item in claims.values())
assert (root / "RESULTS.md").is_file() and (root / "docs" / "SOURCE_AUDIT.md").is_file()
assert claim_3["status"] == "VERIFIED"
assert all(item["rejected"] for item in claim_3["negative_controls"].values())
gate = {
    "paper": "kovefbSXbQ", "arxiv": "2606.25357", "claim_count": 6,
    "publication_eligible": False, "tests_passed": True,
    "publication_gate_passed": False,
    "research_milestone_passed": True,
    "current_exact_status": {
        "claim_1": "TOY",
        "claim_2": "TOY",
        "claim_3": "VERIFIED",
        "claim_4": "TOY",
        "claim_5": "TOY",
        "claim_6": "TOY"
    },
    "checks": {
        "six_anchored_claims_pass": True,
        "claim_3_symbolic_certificate_passes": True,
        "independent_mechanism_per_claim": True,
        "negative_control_per_claim": True,
        "primary_source_audit_present": True,
        "theory_scope_limitation_explicit": True,
    },
    "scope": "Claim 3 proof-grade abstract certificate plus cumulative historical finite checks.",
}
(root / "outputs" / "publication_gate.json").write_text(json.dumps(gate, indent=2, sort_keys=True) + "\n")
print(json.dumps(gate, indent=2, sort_keys=True))
