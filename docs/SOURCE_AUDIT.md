# Primary-source and scope audit

Paper: **Compositional Behavioral Semantics for State Abstraction in
Reinforcement Learning**, by Yivan Zhang, Ziyan Luo, and Manuel Baltieri.

- arXiv: [2606.25357](https://arxiv.org/abs/2606.25357)
- ICML submission: `kovefbSXbQ`
- Public TeX source audited: Sections `systems.tex`, `semantics.tex`, and
  `abstraction.tex`, together with the public appendices
- Retrieved source hashes retained in the release report: ar5iv
  `aed1b2a2746d622e320cf34b8302381f0fa8edd0fbba0f8b4e937f67fba8987a` and
  arXiv TeX `49b5caabba01904db0c268d7528c3785bc20175791feefea22d4896c8ec5039a`

This is a theory paper. The selected claims do not depend on unavailable model
weights, benchmark data, or GPU execution.

| ID | Exact primary-source anchor | Claim route | Evidence produced |
| --- | --- | --- | --- |
| C1 | Definition 3.1 and the Section 2 coalgebra/system definition | `Formalization/Core.lean`, `definition_certificates.py` | Generic bundle/coalgebra totality theorems and finite definition checks |
| C2 | Definitions 3.8–3.9 | `Formalization/Core.lean`, `definition_certificates.py` | Exact closure equation and fixed-to-post-fixed theorem |
| C3 | Theorems 3.12–3.13 | `Formalization/SafeTransfer.lean`, `proof_certificates.py` | Surjective pullback reflection and homomorphic pushforward preservation under explicit compatibility premises |
| C4 | Theorem 3.14 and the commutative lifting appendix | `Formalization/LogicQuant.lean`, `logic_quant_certificate.py` | Structural induction over leaf, combinator, aggregator, and barycenter constructors |
| C5 | Propositions 4.1–4.3 | `Formalization/RL.lean`, `rl_proposition_certificates.py` | Next-observation, model-irrelevance factorization, and quotient/bisimulation proofs |
| C6 | Example 2.9 and naturality Definition 2.8 | `Formalization/Policy.lean`, `definition_certificates.py` | Policy-dependent naturality square for every state map |

## Exact contracts

1. **C1 — bundle and coalgebra types.** For arbitrary arity `n`, sets `X` and
   `V`, and functor `F`, the bundle is a total map `X^n → V` and the system is
   a map `X → F X`.
2. **C2 — behavioral structure.** For `T_X = t_X* ∘ λ_X`, a bundle is
   behavioral when it is post-fixed or fixed under the paper's preorder/equality
   definitions.
3. **C3 — safe transfer.** Under a coalgebra homomorphism, the stated closure
   compatibility assumptions, and surjectivity where required, pullback
   reflects and pushforward preserves post-fixedness.
4. **C4 — logical/quantitative relation.** If the zero predicate is an algebra
   homomorphism for the combinator, indexed aggregator, and probability
   barycenter, it commutes with the induced liftings.
5. **C5 — RL abstraction.** The formalization checks the paper's next-observation,
   model-irrelevance, and quotient/bisimulation implications under their stated
   Set/MDP assumptions.
6. **C6 — policy naturality.** A fixed stationary policy yields the claimed
   natural transformation for every set map `f : X → Y`.

## Fidelity boundary

The Lean layer quantifies over arbitrary types and maps for the selected
contracts. The finite Python checks are separate implementation diagnostics;
they cannot establish the paper's universal scope. The repository does not
formalize every categorical construction or every appendix lemma. Claim 3
keeps the lifting-compatibility lemmas as premises, and Claim 5 states the
standard nonempty-MDP extension used for unused representation states.
