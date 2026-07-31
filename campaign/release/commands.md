# Reproduction and release command ledger

No secret values or generated wrappers are recorded.

## Source and state audit

```bash
orx skill
orx skill orx-experiment-tree
orx skill orx-evidence
orx skill orx-git
orx skill orx-compute
orx skill orx-reports
orx projects --json
orx runs be98825b-855c-41fb-885e-65bd9da5b093
git status --short
git rev-parse HEAD
git branch -a
df -h .
curl -L -A 'OpenResearch-Reproduction/1.0 (contact: local-user)' https://ar5iv.labs.arxiv.org/html/2606.25357
curl -L -A 'OpenResearch-Reproduction/1.0 (contact: local-user)' https://export.arxiv.org/e-print/2606.25357
```

Environment-variable names, never values, were inspected separately. The live
verdict dataset was filtered by exact
`space_id == "DineshAI/kovefbSXbQ"`. The judged Space was downloaded at exact
revision `5a8a6266162a652c6216487c4df8116b15c63aca`.

## Fixed experiment command

Every node inherited exactly:

```bash
uv run --frozen python repro/src/verify.py && uv run --frozen python repro/src/publication_gate.py
```

The Lean run used:

```bash
orx exp run 7624ee40-f964-46f3-abbe-fd0d9c8cc8d7 --flavor cpu-upgrade --timeout 2h
orx exp run 7624ee40-f964-46f3-abbe-fd0d9c8cc8d7 --flavor cpu-upgrade --image ghcr.io/astral-sh/uv:python3.12-bookworm --timeout 2h
orx exp wait 7624ee40-f964-46f3-abbe-fd0d9c8cc8d7 --timeout 480
orx logs 081c66c6-86a4-420f-ada5-354de4cb7e6c --bytes 50000
```

The first launch failed before science because `uv` was absent; the second
passed. Estimate: 2 cores. Actual: HF `cpu-upgrade`, 64 visible logical CPUs,
one Lean worker, 29.088961-second verifier runtime. No GPU.

## Candidate checks

```bash
python3 repro/src/blind_audit.py
python3 repro/src/build_release_manifest.py
python3 repro/src/release_gate.py
uv run --frozen marimo check notebooks/behavioral_semantics_reproduction.py
python3 -m py_compile repro/src/lean_gate.py repro/src/build_release_manifest.py repro/src/release_gate.py repro/src/verify.py repro/src/publication_gate.py
git diff --check
```

Upload and exact-revision post-publication commands are appended after the
release action.
