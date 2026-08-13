# Results

Run the fixed cumulative verifier with:

```bash
uv sync --frozen
uv run --frozen python repro/src/verify.py
uv run --frozen python repro/src/publication_gate.py
```

## Current local evidence

Lean 4.32.0 checks 11 generic theorems spanning the six selected claims. The
axiom audit finds no project-declared axioms and the six deliberate mutations
fail compilation for their intended missing premise or type condition.

| Claim | Primary formal evidence | Required failing control | Verdict |
| --- | --- | --- | --- |
| 1 | Generic bundle and coalgebra totality schemas | wrong tuple arity | VERIFIED |
| 2 | Generic closure and fixed-to-post-fixed theorem | reversed post-fixed inequality | VERIFIED |
| 3 | Surjective pullback reflection and homomorphic pushforward preservation | missing surjectivity / compatibility | VERIFIED |
| 4 | Structural induction over all lifting-expression constructors | missing zero-homomorphism law | VERIFIED |
| 5 | Next-observation, kernel-factorization, and quotient theorems | missing observation/kernel condition | VERIFIED |
| 6 | Policy-dependent naturality by symbolic equality | incompatible policy | VERIFIED |

The successful formal run used HF `cpu-upgrade`, an estimated two cores, 64
visible logical CPUs, one Lean worker, and 29.088961 seconds. It used no GPU
and no stochastic seed.

## External evaluation and scope

The previous live evaluator result is **6/12**. Its six verdicts were `toy`:
the finite checks were valid but did not establish universal mathematical
claims. The Lean release is stronger evidence but has not yet been rescored;
do not report a projected score as an observed result.

This repository mechanizes the selected Set-level statements and their stated
assumptions. It is not a formalization of the complete paper or every appendix
lemma. Claim 3 retains lifting-compatibility lemmas as premises, and Claim 5
records the nonempty-MDP extension convention explicitly.
