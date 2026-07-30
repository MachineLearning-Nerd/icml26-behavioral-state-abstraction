# Pre-publication evaluator-visible audit

Date: 2026-07-30

Candidate construction started from a fresh copy of exact judged Space revision
`5a8a6266162a652c6216487c4df8116b15c63aca`, then overlaid only paths listed in
`candidate/upload_allowlist.txt`.

## Gates

- Fixed command exited 0 in fresh assembled candidate.
- Six cumulative exact claim statuses: VERIFIED.
- Fourteen malformed-certificate controls: rejected.
- Visibility matrix: 6/6 rows complete.
- Candidate text allowlist: 172 files.
- SHA-256 payload manifest: 171 entries; the manifest intentionally cannot
  hash itself.
- Judged file subset: all 25 old paths present.
- Historical integrity: 22 unmodified old paths hash-identical; `README.md`,
  `logbook.json`, and `pages/index.md` are additive/current-navigation updates.
  The original index table remains verbatim below “Historical rejected
  baseline”.
- Existing claim, evidence, method, control, conclusion, and historical
  verification pages: hash-identical.
- JSON parse: pass.
- Secret-pattern scan: pass.
- Five SVG figures: XML parse pass; headline rendered through macOS Quick Look.
- `marimo check --strict notebooks/behavioral_semantics_reproduction.py`: exit 0.

## Evaluator-blind traversal

Round 1 opened only the exact judged `README.md`, `logbook.json`,
`pages/index.md`, historical verification, six claim pages, evidence, and
controls. Proof-grade quantifiers, source, raw data, locks, SHA, and CPU metadata
could not be found.

Round 2 opened only the assembled candidate's canonical entrypoint, followed
its navigation, and located current verification first; all six current claim
pages; code; lock inputs; per-claim contracts, raw data, checkers, controls and
limitations; visibility matrix; release report; and this red-team record.
No OpenResearch run log or unpublished repository path was used to fill a gap.
