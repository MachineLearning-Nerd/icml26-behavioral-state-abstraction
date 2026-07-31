#!/usr/bin/env python3
"""Audit discoverability using only a fresh copy and canonical entrypoints."""
from __future__ import annotations

import json
import re
import shutil
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "candidate" / "space"
OUTPUT = ROOT / "campaign" / "release" / "evaluator_blind_audit.json"


def main() -> dict:
    with tempfile.TemporaryDirectory() as directory:
        artifact = Path(directory) / "space"
        shutil.copytree(SOURCE, artifact)
        logbook = json.loads((artifact / "logbook.json").read_text())
        page_map = {
            child["slug"]: child["file"]
            for child in logbook["root"]["children"]
        }
        queue = ["README.md", logbook["root"]["file"]]
        opened: list[str] = []
        texts: dict[str, str] = {}
        while queue:
            relative = queue.pop(0)
            if relative in opened:
                continue
            text = (artifact / relative).read_text()
            opened.append(relative)
            texts[relative] = text
            for slug in re.findall(r"\]\(#/([a-z0-9-]+)\)", text):
                linked = page_map.get(slug)
                if linked and linked not in opened:
                    queue.append(linked)

        missing: list[str] = []
        current_path = page_map.get("current-verification")
        if not current_path or current_path not in opened:
            missing.append("canonical current verifier")
        else:
            current = texts[current_path]
            for required in (
                "Lean 4.32.0 kernel build: PASS",
                "Project-declared axioms: 0",
                "081c66c6-86a4-420f-ada5-354de4cb7e6c",
                "uv run --frozen python repro/src/verify.py",
                "29.088961",
                "SHA-256",
                "Honest limitation",
            ):
                if required not in current:
                    missing.append(f"current verifier: {required}")
        for claim in range(1, 7):
            path = page_map.get(f"current-claim-{claim}")
            if not path or path not in opened:
                missing.append(f"claim {claim} page")
                continue
            page = texts[path]
            for required in (
                "**Status: VERIFIED.",
                "```lean",
                f"claim{claim}_",
                "raw ",
                "mutation",
                "Limitation:",
            ):
                if required not in page:
                    missing.append(f"claim {claim}: {required}")
        assert not missing, missing
        result = {
            "entrypoints": ["README.md", "pages/index.md"],
            "files_opened": opened,
            "claims_located": 6,
            "actual_lean_code_inline": True,
            "raw_links_located": True,
            "compile_failure_controls_located": True,
            "limitations_located": True,
            "missing": [],
            "verdict": "visibility complete; scientific verdict remains separate",
        }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))
    return result


if __name__ == "__main__":
    main()
