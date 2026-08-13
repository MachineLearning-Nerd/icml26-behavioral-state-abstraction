# Branch audit

This file explains what each historical branch contributed. The old remote
names used the `orx/` prefix; clean names below are the publication names.
Branch history is provenance, not an additional claim-verification system.

| Historical branch | Clean branch | Role and canonical evidence |
| --- | --- | --- |
| `main` | `main` | Publication surface and README contract. |
| `orx/judged-finite-instance-baseline` | `audit/judged-finite-baseline` | Original finite 3–4-state checks; canonical for the historical 6/12 toy score, not universal proof. |
| `orx/c1-c2-c6-symbolic-definition-and-naturality-cert` | `audit/c1-c2-c6-symbolic-definition-naturality` | C1, C2, and C6 symbolic definition/naturality certificates. |
| `orx/c3-symbolic-safe-transfer-certificate` | `audit/c3-symbolic-safe-transfer` | C3 Theorems 3.12–3.13 order-theoretic proof route and premise controls. |
| `orx/c4-structural-zero-predicate-certificate` | `audit/c4-structural-zero-predicate` | C4 Theorem 3.14 structural-induction certificate. |
| `orx/c5-rl-proposition-proof-certificates` | `audit/c5-rl-proposition-certificates` | C5 Propositions 4.1–4.3, factorization, and quotient certificates. |
| `orx/evaluator-visible-release-candidate-and-gates` | `release/evaluator-visible-gates` | Candidate Space, visibility matrix, red-team checks, and cumulative release gate. |
| `orx/lean-4-kernel-proofs-for-all-six-claims` | `release/lean-kernel-six-claims` | Lean 4 formalization, kernel/axiom audit, and six proof-breaking mutations. |
| `orx/evaluator-visible-lean-proof-release` | `release/evaluator-visible-lean-proof` | Final evaluator-facing Lean source, raw outputs, report, and immutable candidate manifest. |

## Canonical claim routing

The claim numbers are stable across all branches:

- **C1:** `Formalization/Core.lean` and `repro/src/definition_certificates.py`.
- **C2:** `Formalization/Core.lean` and the same definition certificate route.
- **C3:** `Formalization/SafeTransfer.lean` and `repro/src/proof_certificates.py`.
- **C4:** `Formalization/LogicQuant.lean` and `repro/src/logic_quant_certificate.py`.
- **C5:** `Formalization/RL.lean` and `repro/src/rl_proposition_certificates.py`.
- **C6:** `Formalization/Policy.lean` and the definition certificate route.

The strongest current evidence is the Lean release branch and its mirrored
`main` files. The finite baseline remains useful for regression and historical
score interpretation only.
