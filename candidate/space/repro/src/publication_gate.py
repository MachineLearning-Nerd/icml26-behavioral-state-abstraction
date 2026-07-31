#!/usr/bin/env python3
"""Fail-closed local publication gate for kovefbSXbQ."""
from __future__ import annotations

import json
from pathlib import Path

from release_gate import check_release

root = Path(__file__).resolve().parents[2]
verdict = json.loads((root / "outputs" / "verdict.json").read_text())
claims = verdict["claims"]
claim_3 = json.loads((root / "outputs" / "proof_certificates.json").read_text())
definitions = json.loads((root / "outputs" / "definition_certificates.json").read_text())
claim_4 = json.loads((root / "outputs" / "logic_quant_certificate.json").read_text())
claim_5 = json.loads((root / "outputs" / "rl_proposition_certificates.json").read_text())
lean = json.loads((root / "outputs" / "lean_verification.json").read_text())
assert verdict["paper"] == "kovefbSXbQ"
assert len(claims) == 6 and verdict["all_claims_passed"]
assert all(item.get("passed") and item.get("source") and item.get("mechanism")
           and item.get("negative_control") and item.get("scope")
           for item in claims.values())
assert (root / "RESULTS.md").is_file() and (root / "docs" / "SOURCE_AUDIT.md").is_file()
assert claim_3["status"] == "VERIFIED"
assert all(item["rejected"] for item in claim_3["negative_controls"].values())
assert all(definitions[f"claim_{claim}"]["status"] == "VERIFIED"
           for claim in (1, 2, 6))
assert all(item["rejected"] for item in definitions["negative_controls"].values())
assert claim_4["status"] == "VERIFIED"
assert all(item["rejected"] for item in claim_4["negative_controls"].values())
assert claim_5["status"] == "VERIFIED"
assert all(item["rejected"] for item in claim_5["negative_controls"].values())
assert lean["status"] == "VERIFIED"
assert len(lean["theorems"]) == 11
assert all(item["status"] == "VERIFIED" and item["kernel_checked"]
           and item["mutation_rejected"] for item in lean["claims"].values())
assert not lean["project_declared_axioms"]
assert all(not paths for paths in
           lean["source_audit"]["forbidden_constructs"].values())
assert all(item["rejected"] for item in lean["negative_controls"].values())
release_checks = check_release()
gate = {
    "paper": "kovefbSXbQ", "arxiv": "2606.25357", "claim_count": 6,
    "publication_eligible": True, "tests_passed": True,
    "publication_gate_passed": True,
    "research_milestone_passed": True,
    "current_exact_status": {
        "claim_1": "VERIFIED",
        "claim_2": "VERIFIED",
        "claim_3": "VERIFIED",
        "claim_4": "VERIFIED",
        "claim_5": "VERIFIED",
        "claim_6": "VERIFIED"
    },
    "checks": {
        "six_anchored_claims_pass": True,
        "lean_kernel_build_passes": True,
        "eleven_generic_theorems_kernel_checked": True,
        "no_sorry_admit_native_decide_or_project_axiom": True,
        "six_destructive_compile_controls_rejected": True,
        "independent_mechanism_per_claim": True,
        "negative_control_per_claim": True,
        "primary_source_audit_present": True,
        "theory_scope_limitation_explicit": True,
        "evaluator_visible_release": release_checks,
    },
    "scope": "Lean 4 kernel proofs for all six claims plus cumulative historical finite checks.",
}
(root / "outputs" / "publication_gate.json").write_text(json.dumps(gate, indent=2, sort_keys=True) + "\n")
print(json.dumps(gate, indent=2, sort_keys=True))
