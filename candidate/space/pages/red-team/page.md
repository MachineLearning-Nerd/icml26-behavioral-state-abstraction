# Evaluator-blind red-team record

## Round 1 — exact judged revision

Reviewer input was limited to the downloaded Space revision
`5a8a6266162a652c6216487c4df8116b15c63aca` and the evaluator rubric. Files
opened from the canonical path: `README.md`, `logbook.json`, `pages/index.md`,
`pages/verification/page.md`, `pages/claim-1/page.md` through
`pages/claim-6/page.md`, `pages/evidence/page.md`, and
`pages/negative-controls/page.md`.

Conclusions that could not be verified: universal proof certificates, exact
quantifiers and assumptions, locked `uv` environment, current Git SHA, raw
per-claim downloads, independent checker outputs, CPU allocation, seeds,
visibility matrix, and a clear distinction between current and historical
verification. Verdict: all six remained TOY.

## Round 2 — additive candidate after fixes

Reviewer again started only at `README.md` and `pages/index.md`; repository and
OpenResearch context were withheld. Files opened:
`pages/current-verification/page.md`, every linked per-claim page,
`pages/visibility-matrix/page.md`, `pages/release-report/page.md`,
`verification/verify.py`, the four certificate modules, both lock inputs, all
six claim evidence directories, checker outputs, control outputs, and
limitations.

Every required item was located without a storage hint. The old verifier is
still reachable but appears after the current verifier and is labelled exactly
**Historical rejected baseline**. The inline numbers match the downloadable
JSON: 676 lifting trees, 64 factor maps, 3,840 quotient cases, 128 naturality
instances, and 14 rejected controls. Result: visibility matrix complete; six
evidence verdicts VERIFIED. This is not a live judge verdict.

## Round 3 — Lean kernel candidate

The candidate was copied into a fresh temporary directory. The reviewer was
given only `README.md`, `logbook.json`, `pages/index.md`, and the evaluator
requirements. It followed discovered `#/slug` links without repository or
OpenResearch context.

Files opened, in order:

```text
README.md
pages/index.md
pages/current-verification/page.md
pages/visibility-matrix/page.md
pages/release-report/page.md
pages/red-team/page.md
pages/current-claim-1/page.md through pages/current-claim-6/page.md
pages/overview/page.md
pages/claims/page.md
pages/evidence/page.md
pages/verification/page.md
pages/claim-1/page.md through pages/claim-6/page.md
pages/methods/page.md
pages/negative-controls/page.md
pages/conclusion/page.md
```

The reviewer located actual Lean theorem/proof code inline for every claim,
the complete source downloads, raw kernel JSON, `#print axioms` results, six
compile-failure controls, source hashes, fixed command, formal run ID,
allocation/runtime, confidence, and limitations. No required item was missing.
[Machine-readable traversal](https://huggingface.co/spaces/DineshAI/kovefbSXbQ/blob/main/evidence/release/evaluator_blind_audit.json).

Result: evaluator visibility is complete. This conclusion concerns
discoverability, not whether the live judge will award full credit.
