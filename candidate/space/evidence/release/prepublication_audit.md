# Pre-publication evaluator-visible audit

Date: 2026-07-31

The candidate overlays the exact protected Space lineage without deleting any
remote path. Thirteen historical Markdown pages, including the old verifier
and six old claim pages, are hash-identical to judged revision
`5a8a6266162a652c6216487c4df8116b15c63aca`. Nine static assets remain
unchanged on the existing Space. Only `README.md`, `logbook.json`, and
`pages/index.md` are replaced to put current evidence first.

## Gates

- Formal HF run `081c66c6-86a4-420f-ada5-354de4cb7e6c`: passed.
- Lean 4.32.0 generic theorems kernel-checked: 11.
- `sorry`, `admit`, `native_decide`, project-declared axioms: 0.
- Claim-specific proof-breaking mutations rejected: 6/6.
- Historical controls retained: 14.
- Visibility matrix: 6/6 rows complete.
- Candidate text allowlist: 227 files.
- SHA-256 payload manifest: 226 entries; the manifest excludes only itself.
- Protected judged paths accounted for: 25/25.
- Hash-identical historical pages uploaded: 13.
- JSON parse and secret-pattern scan: pass.
- Five SVG figures: XML parse pass.
- `uv run --frozen marimo check notebooks/behavioral_semantics_reproduction.py`: exit 0.

## Evaluator-blind traversal

A fresh temporary copy was reviewed from only `README.md`, `logbook.json`, and
`pages/index.md`. Link traversal opened every current page before historical
evidence and located, without repository knowledge: exact contracts and
quantifiers, actual Lean source inline, complete downloadable source, raw
kernel JSON, axiom output, six failing mutations, fixed command and lock
inputs, source hashes, Git SHA, run ID, CPU/runtime, confidence, and
limitations. No required cell was missing. The machine-readable file list is
`evidence/release/evaluator_blind_audit.json`.

This audit establishes discoverability and release integrity, not a live judge
score.
