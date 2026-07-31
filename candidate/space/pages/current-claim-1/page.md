# Current Claim 1 — bundles and coalgebras

**Status: VERIFIED. Confidence: MEDIUM.**

Definition 3.1 quantifies over arbitrary arity `n` and sets `X,V`; an `n`-ary
bundle is a total map `X^n→V`. Section 2 models a behavioral system as an
arbitrary `F`-coalgebra `X→F X`. The formalization retains those quantifiers:

```lean
abbrev Tuple (X : Type u) (n : Nat) := Fin n → X
abbrev Bundle (X : Type u) (n : Nat) (V : Type v) := Tuple X n → V

structure Coalgebra (F : Type u → Type u) (X : Type u) where
  transition : X → F X

theorem claim1_bundle_total
    {X : Type u} {n : Nat} {V : Type v}
    (h : Bundle X n V) (xs : Tuple X n) :
    ∃ value, h xs = value ∧
      ∀ other, h xs = other → other = value := by
  refine ⟨h xs, rfl, ?_⟩
  intro other equality
  exact equality.symm

theorem claim1_coalgebra_transition_total
    {F : Type u → Type u} {X : Type u}
    (system : Coalgebra F X) (x : X) :
    ∃ next, system.transition x = next ∧
      ∀ other, system.transition x = other → other = next := by
  refine ⟨system.transition x, rfl, ?_⟩
  intro other equality
  exact equality.symm
```

`lake build` kernel-checks both theorems. The mutation changes a unary tuple
into the input of a binary bundle and exits 1:

```text
Tuple Nat 1 ... expected ... Tuple Nat 2
```

[Complete source](https://huggingface.co/spaces/DineshAI/kovefbSXbQ/blob/main/verification/Formalization/Core.lean) ·
[raw kernel result](https://huggingface.co/spaces/DineshAI/kovefbSXbQ/blob/main/results/lean_verification.json) ·
[mutation](https://huggingface.co/spaces/DineshAI/kovefbSXbQ/blob/main/verification/Formalization/Mutants/Claim1WrongArity.lean) ·
[contract and source audit](https://huggingface.co/spaces/DineshAI/kovefbSXbQ/tree/main/evidence/claim_1).

Limitation: this claim is a formal definition, not an empirical performance
claim. The proof checks its universal typing and totality; it cannot establish
that this is the only useful behavioral formalization.
