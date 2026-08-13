# Release report

- Previous live judged score: `6/12`
- Conservative projected score range after the proposed change: **8–12/12**
- Best-supported possible new score: **12/12 forecast, not a judge result**

| Claim | Current points | Possible points | Confidence | Evidence status | Basis and remaining risk |
|---|---:|---:|---|---|---|
| 1 | 1 | 2 | MEDIUM | VERIFIED | Kernel-checked universal bundle/coalgebra typing and totality; residual risk is whether the evaluator treats formal verification of a definition as sufficient for full credit |
| 2 | 1 | 2 | MEDIUM | VERIFIED | Generic closure construction and fixed/post-fixed implication; residual risk is the same definition-versus-theorem interpretation |
| 3 | 1 | 2 | HIGH | VERIFIED | Generic Lean proof of order reflection from surjectivity and both transfer implications; Lemma 3.11 compatibility inequalities are explicit assumptions, matching the paper's proof |
| 4 | 1 | 2 | HIGH | VERIFIED | Kernel-checked structural induction over all four expression constructors and all three homomorphism laws |
| 5 | 1 | 2 | HIGH | VERIFIED | Generic probability-functor/Moore proofs, kernel factorization, and actual Lean quotient construction; nonempty off-image extension is explicit |
| 6 | 1 | 2 | HIGH | VERIFIED | Natural transformation proved for arbitrary types, map, system, functor, and fixed policy; incompatible-policy mutation fails |

Current total score: **6/12**. Conservative projected total: **8–12/12**.
Best-supported possible total: **12/12 forecast**. All six claims changed from
the judge's TOY evidence to Lean kernel-checked internal VERIFIED evidence. No
claim is BLOCKED. Claims 1–2 retain material evaluator-interpretation risk.

Scientific branch:
`release/lean-kernel-six-claims`, formalization SHA
`78ef92c8ea1091c86ae87fde314eff6e34698a1e`. Successful formal run:
`081c66c6-86a4-420f-ada5-354de4cb7e6c`. Exact inherited command:

```bash
uv run --frozen python repro/src/verify.py && uv run --frozen python repro/src/publication_gate.py
```

Compute: Hugging Face `cpu-upgrade`, estimated 2 cores, 64 visible logical
CPUs, one Lean worker thread, 29.088961-second verifier runtime. The HF billing
amount is not exposed by the OpenResearch run record; no GPU was used. The
first launch consumed 16 seconds but ran no verifier because its base image
lacked `uv`; it is preserved as an environment failure.

Baseline HF Head and Judge Head:
`5a8a6266162a652c6216487c4df8116b15c63aca`. Latest live judged Space head:
`b6cc33294d21577e95c637a89816ccf307f1a144`, which retained the 6/12 verdict.

Publication action: after every release gate passes, upload only the
SHA-256-manifested text allowlist to the existing Space
`DineshAI/kovefbSXbQ` through the text-only Hugging Face API; download that
exact revision; verify every hash; repeat the canonical entrypoint traversal;
mirror the same text paths to GitHub main; and leave the paper awaiting judge.
