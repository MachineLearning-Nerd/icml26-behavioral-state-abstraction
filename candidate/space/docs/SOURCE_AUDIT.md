# Primary-source and scope audit

Paper: **Compositional Behavioral Semantics for State Abstraction in
Reinforcement Learning**, ICML 2026 submission `kovefbSXbQ`, arXiv
[`2606.25357`](https://arxiv.org/abs/2606.25357).

Primary source audited: the paper’s public arXiv TeX source, including
`sections/systems.tex`, `sections/semantics.tex`, `sections/abstraction.tex`,
and the public appendices for the proofs.  This is a theory paper: no claimed
score-relevant experiment depends on unavailable model weights, benchmark
data, or GPU execution.

| ID | Exact primary-source anchor | Reproduced evidence |
|---|---|---|
| C1 | Definition 3.1: behavioral systems are `F`-coalgebras / n-ary bundles `X^n -> V` | Unary Boolean system and independent binary equality bundle |
| C2 | Definitions 3.8–3.9: behavioral structure is a post-fixed/fixed point of `T_X = t_X* o lambda_X` | Enumerated closure, fixed points, and post-fixed points |
| C3 | Theorems 3.12–3.13: surjective pullback reflects and pushforward preserves behavioral structure | Exhaustive surjective-homomorphism pullback/pushforward checks plus broken-hypothesis controls |
| C4 | Theorem 3.14: the zero predicate relates logical and quantitative behavior | Exact zero laws for nonnegative sum, max, and barycenter |
| C5 | Section 4 propositions: next-observation/model irrelevance and quotient/bisimulation state abstraction | Finite stochastic Moore homomorphism and kernel quotient |
| C6 | Example 2.9: policy-dependent transition is a natural transformation | Closed-loop distribution-pushforward naturality square |

## Fidelity boundary

The verifier uses the definitions and maps in the source rather than a
synthetic learning task.  Its finite models cannot establish the theorems for
every category or algebra; public appendices supply those universal proofs.
The controls deliberately remove a theorem hypothesis (safety, surjectivity,
homomorphism, nonnegativity, observation preservation, or compatible policy)
and verify the corresponding construction fails.
