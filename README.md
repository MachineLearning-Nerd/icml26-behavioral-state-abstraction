# Compositional Behavioral Semantics — ICML 2026 reproduction

Independent, source-anchored reproduction of **Compositional Behavioral
Semantics for State Abstraction in Reinforcement Learning** by Yivan Zhang,
Ziyan Luo, and Manuel Baltieri.

- Paper: [arXiv:2606.25357](https://arxiv.org/abs/2606.25357)
- ICML submission: `kovefbSXbQ`
- Repository: [MachineLearning-Nerd/icml26-behavioral-state-abstraction](https://github.com/MachineLearning-Nerd/icml26-behavioral-state-abstraction)
- Formal candidate: [DineshAI/kovefbSXbQ](https://huggingface.co/spaces/DineshAI/kovefbSXbQ)

## Current assessment

The local cumulative release marks all six selected claim contracts
**VERIFIED**. Lean 4.32.0 kernel checking covers 11 generic theorems, the
project declares no axioms, and six deliberately broken proof variants are
rejected. The previous live evaluator result remains **6/12**: all six finite
checks were judged valid but toy-scale. The Lean revision has not received a
new live score, so the 6/12 result remains authoritative.

This is a theory-paper reproduction. It does not claim that finite examples
prove universal theorems; the stronger evidence is the explicit Lean proof
layer, while finite enumeration is retained as an independent implementation
check.

## Reproduce the release

The pinned Python and Lean inputs are in `uv.lock`, `lakefile.toml`, and
`lean-toolchain`.

```bash
uv sync --frozen
uv run --frozen python repro/src/verify.py
uv run --frozen python repro/src/publication_gate.py
```

The formal run used one Lean worker on the HF `cpu-upgrade` flavor, exposed 64
logical CPUs, and completed in 29.088961 seconds. It used no GPU or random
seed. The publication gate is a local evidence gate; it is not a new external
judge result.

For the illustrated explanation, see
[`reports/claim-by-claim/report.md`](reports/claim-by-claim/report.md). The
same material is packaged for the candidate Space under `candidate/space/`.

## Claim-to-evidence ledger

Each claim below records the paper anchor, the route that produces the result,
and the control that should fail if a required premise is removed.

| Claim | Paper anchor and tested statement | Evidence route | Negative control and scope |
| --- | --- | --- | --- |
| C1 | Definition 3.1 and the system definition: an `n`-ary bundle is `X^n → V`, and an `F`-coalgebra is `X → F X`. | `Formalization/Core.lean`: `claim1_bundle_total`, `claim1_coalgebra_transition_total`; `repro/src/definition_certificates.py`. | `Formalization/Mutants/Claim1WrongArity.lean` rejects the wrong domain. The Lean proof is generic; finite bundle enumeration is secondary. |
| C2 | Definitions 3.8–3.9: `T_X = t_X* ∘ λ_X`; behavioral structures are post-fixed or fixed points. | `Formalization/Core.lean`: `closure`, `PostFixed`, `Fixed`, `claim2_closure_pointwise`, `claim2_fixed_is_postfixed`; `repro/src/definition_certificates.py`. | `Claim2ReversedPostfixed.lean` rejects the reversed inequality. The proof uses order reflexivity for fixed-to-post-fixed. |
| C3 | Theorems 3.12–3.13: surjective pullback reflects and homomorphic pushforward preserves behavioral structure under the paper's lifting-compatibility assumptions. | `Formalization/SafeTransfer.lean`: `claim3_safe_verification`, `claim3_safe_construction`; `repro/src/proof_certificates.py`. | Missing surjectivity and reversed compatibility are rejected. The compatibility lemmas remain explicit premises; they are not re-proved here. |
| C4 | Theorem 3.14: the zero predicate commutes with quantitative and logical liftings when combinator, aggregator, and barycenter laws are homomorphisms. | `Formalization/LogicQuant.lean`: `LiftingExpr`, evaluator definitions, and `claim4_zero_predicate_commutes`; `repro/src/logic_quant_certificate.py`. | Three missing-law controls reject. Structural induction covers all four expression constructors; 676 finite syntax trees are only an independent checker. |
| C5 | Propositions 4.1–4.3: next-observation preservation, model-irrelevance/homomorphism equivalence, and quotient/bisimulation characterization. | `Formalization/RL.lean`: five generic proposition theorems; `repro/src/rl_proposition_certificates.py`. | Missing observation preservation, target extension, and equivalence conditions reject. The Proposition 4.2 reverse direction uses the stated nonempty-MDP extension convention. |
| C6 | Example 2.9: a fixed stationary policy induces a natural transformation for every state map `f : X → Y`. | `Formalization/Policy.lean`: `claim6_policy_transition_natural`; `repro/src/definition_certificates.py`. | `Claim6IncompatiblePolicy.lean` rejects an incompatible policy. The symbolic proof is primary; 128 direct cases are a checker. |

The machine-readable summaries are `outputs/verdict.json`,
`outputs/lean_verification.json`, and `outputs/publication_gate.json`. The
primary-source anchors and fidelity boundary are collected in
[`docs/SOURCE_AUDIT.md`](docs/SOURCE_AUDIT.md).

## Branch organization

`main` is the publication surface. The historical work is grouped by intent;
the complete mapping, claim routing, and branch-history notes are in
[`branch-audit.md`](branch-audit.md).

| Clean branch | Purpose |
| --- | --- |
| `audit/judged-finite-baseline` | Preserve the original finite 3–4-state baseline and its 6/12 toy evaluation. |
| `audit/c1-c2-c6-symbolic-definition-naturality` | Definitions 3.1, 3.8–3.9, and Example 2.9 symbolic certificates. |
| `audit/c3-symbolic-safe-transfer` | Theorems 3.12–3.13 order-theoretic transfer certificate. |
| `audit/c4-structural-zero-predicate` | Theorem 3.14 structural zero-predicate induction. |
| `audit/c5-rl-proposition-certificates` | Propositions 4.1–4.3 proof and quotient certificates. |
| `audit/locked-baseline` | Locked finite baseline and startup evidence. |
| `release/evaluator-visible-gates` | Candidate Space, visibility matrix, red-team checks, and cumulative release gate. |
| `release/lean-kernel-six-claims` | Lean formalization, axiom audit, and all six destructive mutations. |
| `release/evaluator-visible-lean-proof` | Final evaluator-facing Lean source, raw outputs, and immutable release manifest. |

Branch names describe the evidence role, not separate scientific verdicts.

## Citation

```bibtex
@article{zhang2026compositional,
  title   = {Compositional Behavioral Semantics for State Abstraction in Reinforcement Learning},
  author  = {Zhang, Yivan and Luo, Ziyan and Baltieri, Manuel},
  journal = {arXiv preprint arXiv:2606.25357},
  year    = {2026}
}
```

## Thank you

Thank you to Yivan Zhang, Ziyan Luo, and Manuel Baltieri for developing a
clear compositional framework for behavioral semantics and state abstraction.
This repository is an independent reproduction and verification effort built
to make the paper's definitions, assumptions, proof routes, and limitations
easier to inspect.

## Attribution

Repository maintenance and reproduction commits are attributed to
**MachineLearning-Nerd**. The scientific claims, paper, and original ideas
belong to the cited authors.
