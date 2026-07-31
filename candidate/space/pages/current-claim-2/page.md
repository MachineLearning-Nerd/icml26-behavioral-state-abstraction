# Current Claim 2 — closure and behavioral structures

**Status: VERIFIED. Confidence: MEDIUM.**

Definitions 3.8–3.9 are encoded for arbitrary `F,X,n,V`, without enumerating
states:

```lean
structure BundleLifting
    (F : Type u → Type u) (n : Nat) (V : Type v) where
  lift : {X : Type u} → Bundle X n V → Bundle (F X) n V

def closure
    (system : Coalgebra F X)
    (lifting : BundleLifting F n V)
    (h : Bundle X n V) : Bundle X n V :=
  fun xs => lifting.lift h (fun i => system.transition (xs i))

def PostFixed [LE V]
    (operator : Bundle X n V → Bundle X n V)
    (h : Bundle X n V) : Prop :=
  ∀ xs, h xs ≤ operator h xs

def Fixed
    (operator : Bundle X n V → Bundle X n V)
    (h : Bundle X n V) : Prop :=
  h = operator h

theorem claim2_closure_pointwise
    (system : Coalgebra F X)
    (lifting : BundleLifting F n V)
    (h : Bundle X n V) (xs : Tuple X n) :
    closure system lifting h xs =
      lifting.lift h (fun i => system.transition (xs i)) :=
  rfl

theorem claim2_fixed_is_postfixed [LE V]
    (operator : Bundle X n V → Bundle X n V)
    (h : Bundle X n V)
    (le_refl : ∀ value : V, value ≤ value)
    (fixed : Fixed operator h) :
    PostFixed operator h := by
  intro xs
  rw [congrFun fixed xs]
  exact le_refl (operator h xs)
```

The reversed-post-fixed mutation asks Lean to prove `1≤0`; compilation exits 1
with an expected-type mismatch. This prevents a vacuous “fixed point” pass.

[Complete source](https://huggingface.co/spaces/DineshAI/kovefbSXbQ/blob/main/verification/Formalization/Core.lean) ·
[raw result](https://huggingface.co/spaces/DineshAI/kovefbSXbQ/blob/main/results/lean_verification.json) ·
[mutation](https://huggingface.co/spaces/DineshAI/kovefbSXbQ/blob/main/verification/Formalization/Mutants/Claim2ReversedPostfixed.lean) ·
[contract and audit](https://huggingface.co/spaces/DineshAI/kovefbSXbQ/tree/main/evidence/claim_2).

Limitation: the paper calls `T_X` a closure operator; this page verifies its
stated construction and fixed/post-fixed characterization, not convergence of
an iterative numerical algorithm.
