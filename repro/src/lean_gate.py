#!/usr/bin/env python3
"""Kernel-check the generic Lean formalization and reject six mutations."""
from __future__ import annotations

import hashlib
import json
import os
import platform
import re
import shutil
import subprocess
import tarfile
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "outputs"
TOOLCHAIN = "leanprover/lean4:v4.32.0"
ELAN_VERSION = "4.2.3"
ELAN_URL = (
    "https://github.com/leanprover/elan/releases/download/"
    f"v{ELAN_VERSION}/elan-x86_64-unknown-linux-gnu.tar.gz"
)
ELAN_SHA256 = "df0b2b3a439961ffcbb3985214365ffe40f49bc871df04dff268c7d8e21ca8b2"
THEOREMS = (
    "claim1_bundle_total",
    "claim1_coalgebra_transition_total",
    "claim2_closure_pointwise",
    "claim2_fixed_is_postfixed",
    "claim3_safe_verification",
    "claim3_safe_construction",
    "claim4_zero_predicate_commutes",
    "claim5_next_observation_prediction",
    "claim5_model_irrelevance_iff_homomorphism",
    "claim5_bisimulation_quotient_iff_postfixed",
    "claim6_policy_transition_natural",
)
MUTANTS = {
    "claim_1_wrong_arity": (
        "Formalization/Mutants/Claim1WrongArity.lean",
        "expected to have type",
    ),
    "claim_2_reversed_postfixed": (
        "Formalization/Mutants/Claim2ReversedPostfixed.lean",
        "expected to have type",
    ),
    "claim_3_missing_surjectivity": (
        "Formalization/Mutants/Claim3MissingSurjectivity.lean",
        "nonempty empty",
    ),
    "claim_4_missing_homomorphism": (
        "Formalization/Mutants/Claim4MissingHomomorphism.lean",
        "zerohomomorphism",
    ),
    "claim_5_missing_kernel_condition": (
        "Formalization/Mutants/Claim5MissingKernelCondition.lean",
        "constantencoder left",
    ),
    "claim_6_incompatible_policy": (
        "Formalization/Mutants/Claim6IncompatiblePolicy.lean",
        "not definitionally equal",
    ),
}
ALLOWED_FOUNDATIONAL_AXIOMS = {"Classical.choice", "Quot.sound", "propext"}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def command(command: list[str], environment: dict[str, str]) -> dict:
    started = time.perf_counter()
    process = subprocess.run(
        command,
        cwd=ROOT,
        env=environment,
        text=True,
        capture_output=True,
        check=False,
    )
    return {
        "command": " ".join(command),
        "exit_code": process.returncode,
        "runtime_seconds": round(time.perf_counter() - started, 6),
        "stdout": process.stdout,
        "stderr": process.stderr,
    }


def install_lake(environment: dict[str, str]) -> Path:
    existing = shutil.which("lake", path=environment.get("PATH"))
    if existing:
        return Path(existing)
    if platform.system() != "Linux" or platform.machine() not in {"x86_64", "AMD64"}:
        raise RuntimeError("Lean bootstrap supports the evaluator's x86_64 Linux runner")
    lean_cache = ROOT / ".lean"
    archive = lean_cache / "elan.tar.gz"
    bootstrap = lean_cache / "bootstrap"
    elan_home = lean_cache / "elan-home"
    lean_cache.mkdir(exist_ok=True)
    if not archive.is_file() or sha256(archive) != ELAN_SHA256:
        urllib.request.urlretrieve(ELAN_URL, archive)
    if sha256(archive) != ELAN_SHA256:
        raise RuntimeError("Elan archive hash mismatch")
    if not (bootstrap / "elan-init").is_file():
        bootstrap.mkdir(exist_ok=True)
        with tarfile.open(archive, "r:gz") as bundle:
            bundle.extractall(bootstrap)
    installer = next(bootstrap.rglob("elan-init"))
    environment["ELAN_HOME"] = str(elan_home)
    environment["PATH"] = f"{elan_home / 'bin'}:{environment.get('PATH', '')}"
    setup = command(
        [
            str(installer),
            "-y",
            "--no-modify-path",
            "--default-toolchain",
            TOOLCHAIN,
        ],
        environment,
    )
    if setup["exit_code"]:
        raise RuntimeError(f"Elan setup failed: {setup['stderr'][-2000:]}")
    return elan_home / "bin" / "lake"


def source_audit() -> dict:
    proof_files = sorted(
        path
        for path in (ROOT / "Formalization").rglob("*.lean")
        if "Mutants" not in path.parts
    )
    forbidden = {
        "sorry": re.compile(r"\bsorry\b"),
        "admit": re.compile(r"\badmit\b"),
        "native_decide": re.compile(r"\bnative_decide\b"),
        "project_axiom": re.compile(r"(?m)^\s*axiom\s"),
    }
    hits = {
        name: [
            str(path.relative_to(ROOT))
            for path in proof_files
            if pattern.search(path.read_text())
        ]
        for name, pattern in forbidden.items()
    }
    assert not any(hits.values()), hits
    return {
        "files": {
            str(path.relative_to(ROOT)): sha256(path)
            for path in proof_files
        },
        "forbidden_constructs": hits,
    }


def parse_axioms(output: str) -> dict[str, list[str]]:
    blocks = re.findall(
        r"'BehavioralSemantics\.([^']+)'.*?(?=(?:'BehavioralSemantics\.)|\Z)",
        output,
        flags=re.S,
    )
    assert set(blocks) == set(THEOREMS), (blocks, THEOREMS)
    dependencies: dict[str, list[str]] = {}
    for theorem in THEOREMS:
        match = re.search(
            rf"'BehavioralSemantics\.{re.escape(theorem)}' "
            r"(does not depend on any axioms|depends on axioms: \[([^\]]*)\])",
            output,
            flags=re.S,
        )
        assert match, theorem
        dependencies[theorem] = (
            []
            if match.group(1) == "does not depend on any axioms"
            else re.findall(r"[A-Za-z][A-Za-z0-9_.]*", match.group(2))
        )
        assert set(dependencies[theorem]).issubset(ALLOWED_FOUNDATIONAL_AXIOMS)
    return dependencies


def run() -> dict:
    started = time.perf_counter()
    environment = dict(os.environ)
    environment["LEAN_NUM_THREADS"] = "1"
    lake = install_lake(environment)
    version = command([str(lake), "--version"], environment)
    assert version["exit_code"] == 0
    build = command([str(lake), "build"], environment)
    assert build["exit_code"] == 0, build
    audit = command(
        [str(lake), "env", "lean", "Formalization/AxiomAudit.lean"],
        environment,
    )
    assert audit["exit_code"] == 0, audit
    dependencies = parse_axioms(audit["stdout"] + audit["stderr"])
    mutations = {}
    for name, (path, expected_error) in MUTANTS.items():
        result = command([str(lake), "env", "lean", path], environment)
        combined = (result["stdout"] + result["stderr"]).lower()
        rejected = result["exit_code"] != 0 and expected_error in combined
        assert rejected, result
        mutations[name] = {
            "file": path,
            "expected_error": expected_error,
            "rejected": True,
            "exit_code": result["exit_code"],
            "runtime_seconds": result["runtime_seconds"],
            "output": result["stdout"] + result["stderr"],
        }
    claims = {
        f"claim_{claim}": {
            "status": "VERIFIED",
            "kernel_checked": True,
            "mutation_rejected": any(
                key.startswith(f"claim_{claim}_") and item["rejected"]
                for key, item in mutations.items()
            ),
        }
        for claim in range(1, 7)
    }
    result = {
        "paper": "2606.25357",
        "status": "VERIFIED",
        "toolchain": TOOLCHAIN,
        "lean_version_output": version["stdout"].strip(),
        "claims": claims,
        "theorems": list(THEOREMS),
        "source_audit": source_audit(),
        "foundational_dependencies": dependencies,
        "allowed_foundational_axioms": sorted(ALLOWED_FOUNDATIONAL_AXIOMS),
        "project_declared_axioms": [],
        "build": build,
        "axiom_audit": audit,
        "negative_controls": mutations,
        "execution": {
            "requested_backend": "hf",
            "selected_flavor": "cpu-upgrade",
            "estimated_required_cores": 2,
            "visible_logical_cpus": os.cpu_count(),
            "lean_worker_threads": 1,
            "runtime_seconds": round(time.perf_counter() - started, 6),
        },
        "limitations": (
            "This mechanizes the paper's Set-level definitions and the exact "
            "generic implications for the six judged claims. It does not "
            "formalize every appendix lemma or the whole category-theory library."
        ),
    }
    OUT.mkdir(exist_ok=True)
    (OUT / "lean_verification.json").write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n"
    )
    print(
        json.dumps(
            {
                "lean_status": result["status"],
                "theorem_count": len(THEOREMS),
                "mutations_rejected": len(mutations),
                "execution": result["execution"],
            },
            indent=2,
            sort_keys=True,
        )
    )
    return result


if __name__ == "__main__":
    run()
