#!/usr/bin/env python3
"""Check the published documentation and repository identity surfaces."""

import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parent
EXPECTED_STATUS = (
    "ALL_SIX_CLAIMS_VERIFIED_SCOPED_LEAN_KERNEL_11_THEOREMS_NO_PROJECT_AXIOMS_HISTORICAL_SCORE_6_OF_12_NO_CURRENT_SCORE"
)
EXPECTED_BRANCHES = 9
EXPECTED_COMMITS = 23
CANONICAL_IDENTITY = "MachineLearning-Nerd <MachineLearning-Nerd@users.noreply.github.com>"


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def load(name: str) -> dict:
    return json.loads((ROOT / name).read_text())


def branch_names() -> set[str]:
    refs = git(
        "for-each-ref",
        "--format=%(refname)",
        "refs/heads",
        "refs/remotes/origin",
    ).splitlines()
    names = set()
    for ref in refs:
        if ref.endswith("/HEAD"):
            continue
        names.add(ref.removeprefix("refs/heads/").removeprefix("refs/remotes/origin/"))
    return names


def main() -> None:
    manifest = load("EVIDENCE_MANIFEST.json")
    missing = [path for path in manifest["required_evidence"] if not (ROOT / path).exists()]
    if missing:
        raise SystemExit(f"missing evidence: {', '.join(missing)}")

    claims = load("claims.json")
    verdicts = load("reproduction_verdicts.json")
    if claims["overall_status"] != EXPECTED_STATUS or verdicts["overall_status"] != EXPECTED_STATUS:
        raise SystemExit("overall status is inconsistent")
    if set(verdicts["claims"]) != {"C1", "C2", "C3", "C4", "C5", "C6"}:
        raise SystemExit("claim set is incomplete")
    accepted = {"VERIFIED_SCOPED_MEDIUM_CONFIDENCE", "VERIFIED_SCOPED_HIGH_CONFIDENCE"}
    if any(status not in accepted for status in verdicts["claims"].values()):
        raise SystemExit("a claim is not marked verified scoped")
    formal = verdicts["formal_release"]
    if formal["lean_version"] != "4.32.0" or formal["kernel_checked_theorems"] != 11:
        raise SystemExit("formal release record is inconsistent")
    if formal["project_declared_axioms"] != 0 or formal["proof_breaking_mutations_rejected"] != 6:
        raise SystemExit("axiom or mutation audit is inconsistent")
    score = verdicts["historical_live_score"]
    if score["points"] != 6 or score["total"] != 12 or score["current_score_claim"] is not False:
        raise SystemExit("historical score record is inconsistent")
    if verdicts["candidate"]["publication_gate_passed"] is not True:
        raise SystemExit("publication gate is not recorded as passed")
    if verdicts["publication_allowed"] is not False or verdicts["official_author_endorsement"] is not False:
        raise SystemExit("publication or endorsement boundary is inconsistent")

    lean = load("outputs/lean_verification.json")
    if lean.get("project_declared_axioms") != []:
        raise SystemExit("outputs/lean_verification.json reports project axioms")

    names = branch_names()
    if len(names) != EXPECTED_BRANCHES or "main" not in names or any(name.startswith("orx/") for name in names):
        raise SystemExit(f"unexpected branches: {sorted(names)}")
    commits = int(git("rev-list", "--all", "--count"))
    if commits != EXPECTED_COMMITS:
        raise SystemExit(f"expected {EXPECTED_COMMITS} reachable commits, found {commits}")

    identities = set(git("log", "--all", "--format=%an <%ae> | %cn <%ce>").splitlines())
    expected = f"{CANONICAL_IDENTITY} | {CANONICAL_IDENTITY}"
    if identities != {expected}:
        raise SystemExit(f"non-canonical commit identities: {sorted(identities)}")

    print(
        "FINAL_AUDIT=VERIFIED"
        f" branches={len(names)}"
        f" commits={commits}"
        " claims=C1:C6_verified_scoped"
        " formal=lean4.32.0_kernel_theorems=11_project_axioms=0_mutations_rejected=6"
        " historical_score=6/12"
        " current_score_claim=false"
        " publication_allowed=false"
    )


if __name__ == "__main__":
    main()
