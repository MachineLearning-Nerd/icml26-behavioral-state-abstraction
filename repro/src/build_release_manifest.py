#!/usr/bin/env python3
"""Regenerate the exact text-only candidate Space allowlist and manifest."""
from __future__ import annotations

import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CANDIDATE = ROOT / "candidate"
SPACE = CANDIDATE / "space"
ALLOWLIST_PATH = "evidence/release/upload_allowlist.txt"
MANIFEST_PATH = "evidence/release/upload_manifest.sha256"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def paths() -> list[str]:
    return sorted(
        str(path.relative_to(SPACE))
        for path in SPACE.rglob("*")
        if path.is_file()
    )


def main() -> None:
    allowlist = paths()
    assert ALLOWLIST_PATH in allowlist
    assert MANIFEST_PATH in allowlist
    allowlist_text = "\n".join(allowlist) + "\n"
    (CANDIDATE / "upload_allowlist.txt").write_text(allowlist_text)
    (SPACE / ALLOWLIST_PATH).write_text(allowlist_text)

    manifest = "\n".join(
        f"{sha256(SPACE / path)}  {path}"
        for path in paths()
        if path != MANIFEST_PATH
    ) + "\n"
    (CANDIDATE / "upload_manifest.sha256").write_text(manifest)
    (SPACE / MANIFEST_PATH).write_text(manifest)
    print(f"allowlisted_text_files={len(allowlist)}")


if __name__ == "__main__":
    main()
