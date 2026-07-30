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
verdict dataset was downloaded and filtered by exact
`space_id == "DineshAI/kovefbSXbQ"`. The judged Space was checked out at exact
revision `5a8a6266162a652c6216487c4df8116b15c63aca`.

## Fixed experiment command

Every formal node used exactly:

```bash
uv run --frozen python repro/src/verify.py && uv run --frozen python repro/src/publication_gate.py
```

Runs were launched only with:

```bash
orx exp run <experiment-id> --backend local
orx exp wait <experiment-id> --timeout 480
orx logs <run-id>
```

Local was selected because each task was estimated at one core and well under
five minutes. No GPU or Hugging Face CPU job was launched.

## Candidate checks

```bash
marimo check --strict notebooks/behavioral_semantics_reproduction.py
uv run --frozen python repro/src/release_gate.py
uv run --frozen python repro/src/verify.py
uv run --frozen python repro/src/publication_gate.py
```

The last two commands were repeated from a fresh candidate assembled over the
exact judged Space. Upload and post-publication download commands are added to
the final release report after execution.
