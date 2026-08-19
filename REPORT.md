# Audit report

## Executive result

The repository provides scoped verification for six selected claims from
*Compositional Behavioral Semantics for State Abstraction in Reinforcement
Learning*. The primary route is Lean 4.32.0 kernel checking: 11 generic
theorems compile, the project declares no axioms, and six proof-breaking
mutations are rejected.

Overall status:

`ALL_SIX_CLAIMS_VERIFIED_SCOPED_LEAN_KERNEL_11_THEOREMS_NO_PROJECT_AXIOMS_HISTORICAL_SCORE_6_OF_12_NO_CURRENT_SCORE`

## Claim matrix

| Claim | Result | Primary route | Main boundary |
| --- | --- | --- | --- |
| C1 | `VERIFIED_SCOPED` | Lean type schemas for bundles and coalgebras | Definition-level evidence; evaluator interpretation remains material |
| C2 | `VERIFIED_SCOPED` | Lean closure composition and fixed/post-fixed proof | Definition-level evidence; not every theorem is formalized |
| C3 | `VERIFIED_SCOPED` | Lean abstract safe-transfer proof | Compatibility inequalities and joins are explicit premises |
| C4 | `VERIFIED_SCOPED` | Lean structural induction over lifting constructors | Scope is the selected lifting grammar |
| C5 | `VERIFIED_SCOPED` | Lean RL propositions and quotient/factorization proofs | Nonempty-MDP extension is explicit |
| C6 | `VERIFIED_SCOPED` | Lean policy naturality normalization | Fixed-policy contract only |

Open the [claim ledger](CLAIM_EVIDENCE.md) for exact files and controls, the
[source audit](SOURCE_AUDIT.md) for source anchors, and the
[release report](reports/claim-by-claim/report.md) for provenance and runtime.

## Score and publication boundary

The previous live evaluator result is **6/12**, with all six finite checks
classified as valid but toy-scale. The current Lean revision has not been
rescored. Its local publication gate passed, but internal verification is not
an external judge result:

- `current_score_claim`: `false`
- `publication_allowed`: `false`
- `official_author_endorsement`: `false`

This repository is an independent reproduction and does not imply endorsement
by the paper’s authors.
