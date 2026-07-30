# Primary-source retrieval and exact claim audit

Retrieved on 2026-07-30 with User-Agent
`OpenResearch-Reproduction/1.0 (contact: local-user)`.

| Source | SHA-256 |
|---|---|
| `https://ar5iv.labs.arxiv.org/html/2606.25357` | `aed1b2a2746d622e320cf34b8302381f0fa8edd0fbba0f8b4e937f67fba8987a` |
| `https://export.arxiv.org/e-print/2606.25357` (redirected to `/src/2606.25357`) | `49b5caabba01904db0c268d7528c3785bc20175791feefea22d4896c8ec5039a` |

The arXiv response identifies the archive as `arXiv-2606.25357v1.tar.gz`.
The HTML and TeX source agree on all anchors below.

## Exact contracts and quantifiers

1. **Definition 3.1 — bundle** (`#S3.Thmtheorem1`, TeX
   `sections/semantics.tex:14-17`). Given arbitrary arity `n ∈ ℕ`, set `V`,
   and set `X`, an `n`-ary bundle is exactly a total map `h_X : X^n → V`.
   This is a definition, not an empirical performance claim. Claim 1 also
   relies on Section 2's definition of a system: for an arbitrary functor `F`,
   an `F`-coalgebra is a set `X` and map `t_X : X → F X`.

2. **Definitions 3.8–3.9 — closure and behavioral structure**
   (`#S3.Thmtheorem8`, `#S3.Thmtheorem9`, TeX
   `sections/semantics.tex:193-205`). For an arbitrary `F`-coalgebra
   `t_X : X → F X` and bundle lifting `λ_X`, `T_X = t_X* ∘ λ_X`.
   For every bundle `h_X : X^n → V` and every tuple `x_1,…,x_n ∈ X`,
   `T_X(h_X)(x_1,…,x_n) = λ_X(h_X)(t_X(x_1),…,t_X(x_n))`.
   A behavioral structure is defined to satisfy
   `h_X ⪯ T_X(h_X)` or `h_X = T_X(h_X)`.

3. **Theorems 3.12–3.13 — safe transfer** (`#S3.Thmtheorem12`,
   `#S3.Thmtheorem13`, TeX `sections/semantics.tex:269-306`).
   Context: two systems, liftings constructed with the same operators,
   induced closure operators, and a coalgebra homomorphism.
   Safe verification additionally assumes a surjective encoder. For every
   abstract bundle `h_Z : Z^n → V`,
   `φ*h_Z ⪯ T_S(φ*h_Z) ⇒ h_Z ⪯ T_Z(h_Z)`.
   Safe construction requires only a homomorphic encoder. For every concrete
   bundle `h_S : S^n → V`,
   `h_S ⪯ T_S(h_S) ⇒ φ_*h_S ⪯ T_Z(φ_*h_S)`.
   The pushforward assumes the relevant fiber joins exist, including empty
   fibers.

4. **Theorem 3.14 — logical/quantitative relation**
   (`#S3.Thmtheorem14`, TeX `sections/semantics.tex:314-328`).
   For arbitrary `X`, arity `n`, and quantitative bundle
   `h_X : X^n → [0,∞]`, let `z(x) ≡ (x=0)`. The quantitative and logical
   liftings must use Table 2 operators for which `z` is an algebra
   homomorphism for all three building blocks: combinator, `A`-indexed
   aggregator, and probability barycenter. Under exactly those assumptions,
   the pointwise identity
   `z ∘ λ_X^quant(h_X) = λ_X^truth(z ∘ h_X)` holds.

5. **Propositions 4.1–4.3 — RL instantiations** (`#S4.Thmtheorem1`,
   `#S4.Thmtheorem2`, `#S4.Thmtheorem3`, TeX
   `sections/abstraction.tex:5-95`). Proposition 4.1 quantifies over every
   state `x ∈ X` and action `a ∈ A`: an `F_Moore` homomorphism implies equality
   of pushed-forward next-observation distributions. Proposition 4.2 states
   an exact equivalence between model-irrelevance abstraction and the
   coalgebra-homomorphism condition. Proposition 4.3 quantifies over an
   arbitrary equivalence `r` on an arbitrary `F`-coalgebra: its quotient map
   is a homomorphism iff `r` is post-fixed under the stated kernel closure.

6. **Example 2.9 — policy-dependent natural transformation**
   (`#S2.Thmtheorem9`, TeX `sections/systems.tex:275-337`). For a fixed
   stationary policy `π : O → A`, the family `α_X^π` selects the distribution
   `p(·|π(o))` and preserves `o`. Naturality means that for every map
   `f : X → Y`, `α_Y^π ∘ F_Moore f = F_Markov f ∘ α_X^π`. The example states
   this construction and says the equality can be verified; it is not a
   benchmark-scale empirical claim.

## Calibration consequence

Claims 1, 2, and 6 are definitional/constructional. Claims 3–5 contain
universal mathematical statements. Finite examples, regardless of state
count, cannot establish their universal scope. Full-credit evidence therefore
requires proof-level certificates or a valid assumption-satisfying
counterexample; scale-up alone is rejected as circular or merely
corroborative.

