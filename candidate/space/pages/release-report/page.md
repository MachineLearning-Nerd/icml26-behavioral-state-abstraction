# Release report

- Previous live judged score: `6/12`
- Conservative projected score range after the proposed change: **8–12/12**
- Best-supported possible new score: **12/12 forecast, not a judge result**

| Claim | Current points | Possible points | Confidence | Evidence status | Basis and remaining risk |
|---|---:|---:|---|---|---|
| 1 | 1 | 2 | HIGH | VERIFIED | Exact arbitrary-parameter definition schema; residual risk is evaluator interpretation of executable type certificates |
| 2 | 1 | 2 | HIGH | VERIFIED | Exact typed composition, expansion, and both Definition 3.9 alternatives |
| 3 | 1 | 2 | MEDIUM | VERIFIED | Universal preorder derivations close; separately stated lifting-compatibility lemmas remain premises |
| 4 | 1 | 2 | HIGH | VERIFIED | Constructor-complete structural induction plus 676-tree independent normalizer |
| 5 | 1 | 2 | MEDIUM | VERIFIED | Five symbolic proposition paths; reverse Prop. 4.2 uses an explicit standard extension convention |
| 6 | 1 | 2 | HIGH | VERIFIED | Arbitrary-map naturality normalization plus 128-case checker |

Current total score: **6/12**. Conservative projected total: **8–12/12**.
Best-supported possible total: **12/12 forecast**. All six claims changed from
TOY evidence to internal VERIFIED evidence. No claim is BLOCKED; Claims 3 and 5
retain the material interpretation risks shown above.

Publication action: upload only the SHA-256-manifested text allowlist to the
existing Space `DineshAI/kovefbSXbQ` through the Hugging Face API, then download
that exact revision, recheck every hash, and repeat entrypoint-only traversal.
The paper will remain marked awaiting judge.

Baseline HF Head and Judge Head:
`5a8a6266162a652c6216487c4df8116b15c63aca`. Winning scientific branch:
`orx/c5-rl-proposition-proof-certificates`, SHA
`766eb2ccc6e0dfc7b33bd813f5deb2a95fd02e5c`. All CPU runs were local,
single-process, approximately 5 s per OpenResearch run, total cost $0.
