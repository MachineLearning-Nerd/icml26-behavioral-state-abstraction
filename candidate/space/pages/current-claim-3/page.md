# Current Claim 3 — safe verification and construction

**Status: VERIFIED. Confidence: HIGH.**

Theorems 3.12–3.13 are proved for every source/target type, arity, value
preorder, bundle and closure operator. Surjectivity is used constructively to
prove that pullback is order-reflecting; the two closure compatibility
inequalities are exactly Lemma 3.11 in the paper's proof.

```lean
theorem pullBundle_order_reflecting
    {S Z : Type u} {n : Nat} {V : Type v} [LE V]
    (encoder : S → Z)
    (surjective : Function.Surjective encoder)
    {h k : Bundle Z n V}
    (pulled : BundleLE (pullBundle encoder h) (pullBundle encoder k)) :
    BundleLE h k := by
  classical
  intro zs
  let ss : Tuple S n := fun i => Classical.choose (surjective (zs i))
  have mapped : pullTuple encoder ss = zs := by
    funext i
    exact Classical.choose_spec (surjective (zs i))
  have pointwise := pulled ss
  change h (pullTuple encoder ss) ≤ k (pullTuple encoder ss) at pointwise
  rw [mapped] at pointwise
  exact pointwise

theorem claim3_safe_verification
    {S Z : Type u} {n : Nat} {V : Type v} [LE V]
    (le_transitive : ∀ {a b c : V}, a ≤ b → b ≤ c → a ≤ c)
    (encoder : S → Z)
    (surjective : Function.Surjective encoder)
    (concreteClosure : Bundle S n V → Bundle S n V)
    (abstractClosure : Bundle Z n V → Bundle Z n V)
    (closureOplax : ∀ h, BundleLE
      (concreteClosure (pullBundle encoder h))
      (pullBundle encoder (abstractClosure h)))
    (h : Bundle Z n V)
    (concretePostfixed :
      PostFixed concreteClosure (pullBundle encoder h)) :
    PostFixed abstractClosure h := by
  apply pullBundle_order_reflecting encoder surjective
  intro ss
  exact le_transitive (concretePostfixed ss) (closureOplax h ss)

theorem claim3_safe_construction
    {S Z : Type u} {n : Nat} {V : Type v} [LE V]
    (le_transitive : ∀ {a b c : V}, a ≤ b → b ≤ c → a ≤ c)
    (pushforward : Bundle S n V → Bundle Z n V)
    (concreteClosure : Bundle S n V → Bundle S n V)
    (abstractClosure : Bundle Z n V → Bundle Z n V)
    (pushforwardMonotone : ∀ {h k}, BundleLE h k →
      BundleLE (pushforward h) (pushforward k))
    (closureLax : ∀ h, BundleLE
      (pushforward (concreteClosure h))
      (abstractClosure (pushforward h)))
    (h : Bundle S n V)
    (concretePostfixed : PostFixed concreteClosure h) :
    PostFixed abstractClosure (pushforward h) := by
  intro zs
  exact le_transitive
    (pushforwardMonotone concretePostfixed zs)
    (closureLax h zs)
```

The negative control uses `Empty→Unit`; Lean rejects the required
surjectivity because `Nonempty Empty` cannot be synthesized. Thus the
reflection theorem cannot pass after deleting its decisive hypothesis.

[Complete source](https://huggingface.co/spaces/DineshAI/kovefbSXbQ/blob/main/verification/Formalization/SafeTransfer.lean) ·
[raw kernel/checker output](https://huggingface.co/spaces/DineshAI/kovefbSXbQ/blob/main/results/lean_verification.json) ·
[mutation](https://huggingface.co/spaces/DineshAI/kovefbSXbQ/blob/main/verification/Formalization/Mutants/Claim3MissingSurjectivity.lean) ·
[source contract](https://huggingface.co/spaces/DineshAI/kovefbSXbQ/tree/main/evidence/claim_3).

Limitation: Lemma 3.11's lifting-to-closure inequalities are explicit theorem
premises here. This verifies the exact transfer arguments of Theorems
3.12–3.13, not every separate appendix proof establishing those inequalities
for every listed lifting.
