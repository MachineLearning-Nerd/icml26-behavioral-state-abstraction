# Claim-to-evidence ledger

This repository audits six selected source-anchored contracts from
*Compositional Behavioral Semantics for State Abstraction in Reinforcement
Learning*. The primary evidence is a Lean 4 formalization checked by the Lean
kernel. Finite Python enumerations and independent checkers are supporting
diagnostics; they do not replace the paper’s universal assumptions or proofs.

| Claim | Paper anchor | How the result is produced | Evidence and negative control | Scope and confidence |
| --- | --- | --- | --- | --- |
| C1 — bundle and coalgebra types | Definition 3.1 and Section 2 system definition | `Formalization/Core.lean` proves total bundle and coalgebra schemas for arbitrary types, arity, and functor; `repro/src/definition_certificates.py` checks the representation. | `Formalization/Mutants/Claim1WrongArity.lean` rejects the wrong domain. | Generic definition-level contract; finite enumeration is secondary. **VERIFIED_SCOPED — MEDIUM** |
| C2 — closure and behavioral structure | Definitions 3.8–3.9 | `Formalization/Core.lean` proves `T_X = t_X* ∘ λ_X`, its pointwise form, and fixed implies post-fixed; the checker compares the symbolic schemas. | Reversed composition and fixed-point-only mutations are rejected. | Generic definition-level contract; evaluator interpretation remains material. **VERIFIED_SCOPED — MEDIUM** |
| C3 — safe transfer | Theorems 3.12–3.13 | `Formalization/SafeTransfer.lean` kernel-checks pullback reflection and homomorphic pushforward preservation under the stated compatibility, surjectivity, and join premises. | Missing surjectivity and reversed compatibility controls are rejected; the compatibility lemmas remain explicit assumptions. | Universal proof schema under the paper’s assumptions. **VERIFIED_SCOPED — HIGH** |
| C4 — zero predicate and liftings | Theorem 3.14 and commutative lifting appendix | `Formalization/LogicQuant.lean` performs structural induction over leaf, combinator, aggregator, and barycenter constructors; an independent normalizer checks 676 syntax trees. | Removing any combinator, aggregator, or barycenter homomorphism makes the proof fail. | Constructor-complete structural proof for the selected lifting grammar. **VERIFIED_SCOPED — HIGH** |
| C5 — RL abstraction propositions | Propositions 4.1–4.3 | `Formalization/RL.lean` proves next-observation preservation, model-irrelevance factorization, and quotient/bisimulation equivalences; independent factorization and quotient checkers corroborate them. | Missing observation preservation, target extension, or equivalence controls are rejected. | Set/MDP assumptions are explicit; Proposition 4.2 uses the stated nonempty-MDP extension. **VERIFIED_SCOPED — HIGH** |
| C6 — policy naturality | Example 2.9 and naturality Definition 2.8 | `Formalization/Policy.lean` normalizes the policy-selected transition square for every set map `f : X → Y`; direct finite cases are a checker. | An incompatible abstract policy produces a different normal form and is rejected. | Generic symbolic naturality contract. **VERIFIED_SCOPED — HIGH** |

## Reading the evidence

- `Formalization/` is the primary proof surface. `Formalization/AxiomAudit.lean`
  records standard foundational dependencies; the project itself declares no
  new axioms.
- `.openresearch/artifacts/claim_1/` through `claim_6/` contain contracts,
  methods, source audits, proof objects, independent outputs, controls, and
  limitations.
- `candidate/space/` is the evaluator-visible package. Its current pages are
  separate from the preserved historical finite baseline.
- `outputs/verdict.json`, `outputs/lean_verification.json`, and
  `outputs/publication_gate.json` are the machine-readable source records.

## Overall result

`ALL_SIX_CLAIMS_VERIFIED_SCOPED_LEAN_KERNEL_11_THEOREMS_NO_PROJECT_AXIOMS_HISTORICAL_SCORE_6_OF_12_NO_CURRENT_SCORE`

The historical external judge scored the earlier finite candidate `6/12` and
called all six checks toy-scale. The Lean release is stronger internal
evidence, but no new live score is claimed.
