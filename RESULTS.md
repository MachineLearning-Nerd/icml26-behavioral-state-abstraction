# Results

Run the fixed cumulative verifier with:

```bash
uv run --frozen python repro/src/verify.py && uv run --frozen python repro/src/publication_gate.py
```

Lean 4.32.0 kernel-checks 11 generic theorems spanning all six judged claims.
The gate finds no `sorry`, `admit`, `native_decide`, or project-declared axiom,
audits foundational dependencies with `#print axioms`, and requires six
claim-specific mutations to fail compilation.

| Claim | Primary formal evidence | Required failing control | Verdict |
|---|---|---|---|
| 1 | Generic bundle/coalgebra types and totality theorems | wrong tuple arity | VERIFIED |
| 2 | Generic closure and fixed-to-post-fixed theorem | reversed post-fixed inequality | VERIFIED |
| 3 | Surjective pullback order reflection and both transfer theorems | missing surjectivity | VERIFIED |
| 4 | Structural induction over all lifting-expression constructors | missing zero homomorphism | VERIFIED |
| 5 | Next-observation, kernel-factorization, and quotient theorems | missing kernel condition | VERIFIED |
| 6 | Arbitrary-map policy naturality by definitional equality | incompatible policy | VERIFIED |

Formal run `081c66c6-86a4-420f-ada5-354de4cb7e6c` used Hugging Face
`cpu-upgrade`: estimated 2 cores, 64 visible logical CPUs, one Lean worker,
29.088961-second verifier runtime, and no GPU. The live judge score remains
6/12 until it evaluates the published revision.

## Scope

This is a Set-level mechanization of the exact definitions and implications
needed by the six selected claims. It is not a formalization of the entire
paper or every appendix lemma. Historical finite checks remain secondary
regression evidence and are not described as theorem verification.
