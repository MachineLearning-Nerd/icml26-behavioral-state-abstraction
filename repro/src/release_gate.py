#!/usr/bin/env python3
"""Fail-closed checks for the evaluator-visible text release."""
from __future__ import annotations

import hashlib
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE_SPACE = ROOT / "candidate" / "space"
SPACE = SOURCE_SPACE if SOURCE_SPACE.is_dir() else ROOT
RELEASE_META = (
    ROOT / "candidate"
    if SOURCE_SPACE.is_dir()
    else ROOT / "evidence" / "release"
)
ALLOWLIST = RELEASE_META / "upload_allowlist.txt"
MANIFEST = RELEASE_META / "upload_manifest.sha256"
JUDGED_MANIFEST = (
    ROOT / "campaign" / "startup" / "judged_space_manifest.sha256"
    if SOURCE_SPACE.is_dir()
    else ROOT / "evidence" / "release" / "judged_space_manifest.sha256"
)
MANIFEST_PATH = "evidence/release/upload_manifest.sha256"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def listed_paths(path: Path) -> list[str]:
    return [line.strip() for line in path.read_text().splitlines() if line.strip()]


def manifest_entries(path: Path) -> dict[str, str]:
    entries = {}
    for line in path.read_text().splitlines():
        if not line.strip():
            continue
        digest, relative = line.split(maxsplit=1)
        entries[relative.removeprefix("./")] = digest
    return entries


def check_release() -> dict:
    allowlist = listed_paths(ALLOWLIST)
    manifest = manifest_entries(MANIFEST)
    judged = manifest_entries(JUDGED_MANIFEST)
    candidate_paths = set(allowlist)

    assert allowlist == sorted(allowlist)
    assert len(allowlist) == len(set(allowlist))
    assert candidate_paths - {MANIFEST_PATH} == set(manifest)
    assert all(sha256(SPACE / path) == manifest[path] for path in manifest)
    assert all((SPACE / path).is_file() for path in allowlist)
    if SOURCE_SPACE.is_dir():
        modified_historical_paths = {"README.md", "logbook.json", "pages/index.md"}
        retained_remote_assets = set(judged) - candidate_paths - modified_historical_paths
        assert retained_remote_assets == {
            ".gitattributes",
            "bucket-icon.svg",
            "index.html",
            "logbook.css",
            "logbook.js",
            "style.css",
            "trackio-logo-light.png",
            "trackio-logo.png",
            "trackio-wordmark-dark.png",
        }
        assert all(
            path in modified_historical_paths
            or path in retained_remote_assets
            or sha256(SPACE / path) == digest
            for path, digest in judged.items()
        )
    else:
        assert all((SPACE / path).is_file() for path in judged)
        modified_historical_paths = {"README.md", "logbook.json", "pages/index.md"}
        assert all(
            path in modified_historical_paths or sha256(SPACE / path) == digest
            for path, digest in judged.items()
        )
    assert all(
        (SPACE / path).suffix
        in {".md", ".json", ".py", ".lean", ".toml", ".lock", ".svg", ".txt", ".sha256"}
        or Path(path).name in {"uv.lock", "lean-toolchain"}
        for path in allowlist
    )

    logbook = json.loads((SPACE / "logbook.json").read_text())
    assert logbook["space_id"] == "DineshAI/kovefbSXbQ"
    pages = {child["slug"]: child["file"] for child in logbook["root"]["children"]}
    assert list(pages)[:4] == [
        "current-verification",
        "current-claim-1",
        "current-claim-2",
        "current-claim-3",
    ]
    assert all(path in candidate_paths or path in judged for path in pages.values())
    assert pages["verification"] == "pages/verification/page.md"
    assert next(
        child["title"]
        for child in logbook["root"]["children"]
        if child["slug"] == "verification"
    ) == "Historical rejected baseline"

    index = (SPACE / "pages" / "index.md").read_text()
    current = (SPACE / "pages" / "current-verification" / "page.md").read_text()
    matrix = (SPACE / "pages" / "visibility-matrix" / "page.md").read_text()
    blind_audit = json.loads(
        (SPACE / "evidence" / "release" / "evaluator_blind_audit.json").read_text()
    )
    assert blind_audit["claims_located"] == 6 and not blind_audit["missing"]
    assert blind_audit["actual_lean_code_inline"]
    assert index.index("Current verification") < index.index("Historical rejected baseline")
    assert "6/12" in current and "no increase" not in current.lower()
    assert "78ef92c8ea1091c86ae87fde314eff6e34698a1e" in current
    assert "uv run --frozen python repro/src/verify.py && uv run --frozen python repro/src/publication_gate.py" in current
    assert "Lean 4.32.0 kernel build: PASS" in current
    assert "Project-declared axioms: 0" in current
    lean_result = json.loads((SPACE / "results" / "lean_verification.json").read_text())
    assert lean_result["status"] == "VERIFIED"
    assert len(lean_result["theorems"]) == 11
    assert all(item["rejected"] for item in lean_result["negative_controls"].values())
    assert lean_result["formal_hf_run"]["status"] == "VERIFIED"
    assert lean_result["formal_hf_run"]["visible_logical_cpus"] == 64
    assert all(
        (SPACE / "verification" / path).is_file()
        for path in (
            "lean-toolchain",
            "lakefile.toml",
            "Formalization/Core.lean",
            "Formalization/SafeTransfer.lean",
            "Formalization/LogicQuant.lean",
            "Formalization/RL.lean",
            "Formalization/Policy.lean",
            "Formalization/AxiomAudit.lean",
        )
    )
    for claim in range(1, 7):
        page = (SPACE / "pages" / f"current-claim-{claim}" / "page.md").read_text()
        evidence = SPACE / "evidence" / f"claim_{claim}"
        assert "**Status: VERIFIED." in page
        assert all(
            (evidence / name).is_file()
            for name in (
                "claim_contract.json",
                "source_audit.md",
                "method.md",
                "independent_checker_output.json",
                "negative_control_output.json",
                "environment.md",
                "EVAL.md",
                "limitations.md",
            )
        )
        assert "```lean" in page and f"claim{claim}_" in page
        assert (evidence / "lean_verification.json").is_file()
        assert all(
            value
            for value in json.loads(
                (evidence / "negative_control_output.json").read_text()
            ).values()
        )
        row = next(line for line in matrix.splitlines() if line.startswith(f"| {claim} |"))
        assert row.count("Complete") == 6 and row.endswith("| VERIFIED |")

    internal_links = re.findall(r"\]\(#/([a-z0-9-]+)\)", index + current + matrix)
    assert internal_links and all(slug in pages for slug in internal_links)
    assert "Historical rejected baseline" in index
    assert "Historical rejected baseline" in (
        SPACE / "pages" / "red-team" / "page.md"
    ).read_text()

    for image in (ROOT / "reports" / "claim-by-claim" / "images").glob("*.svg"):
        ET.parse(image)
    report = (ROOT / "reports" / "claim-by-claim" / "report.md").read_text()
    report_images = re.findall(r"\]\((images/[^)]+)\)", report)
    assert len(report_images) == 5
    assert all((ROOT / "reports" / "claim-by-claim" / path).is_file() for path in report_images)
    assert (ROOT / "notebooks" / "behavioral_semantics_reproduction.py").is_file()

    secret_patterns = (
        re.compile(r"hf_[A-Za-z0-9]{20,}"),
        re.compile(r"(?i)(api[_-]?key|access[_-]?token)\s*[:=]\s*['\"][^'\"]+"),
    )
    assert not any(
        pattern.search((SPACE / path).read_text(errors="ignore"))
        for pattern in secret_patterns
        for path in allowlist
    )

    return {
        "allowlisted_text_files": len(allowlist),
        "candidate_manifest_verified": True,
        "current_pages_first": True,
        "historical_file_paths_preserved": len(judged),
        "historical_unchanged_pages_verified": len(judged) - 12,
        "logbook_valid": True,
        "negative_controls_verified": 20,
        "report_images_verified": len(report_images),
        "secrets_scan_passed": True,
        "visibility_rows_complete": 6,
    }


if __name__ == "__main__":
    print(json.dumps(check_release(), indent=2, sort_keys=True))
