import Formalization.Core

universe u v

namespace BehavioralSemantics

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
    (closureOplax :
      ∀ h, BundleLE
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
    (pushforwardMonotone :
      ∀ {h k}, BundleLE h k →
        BundleLE (pushforward h) (pushforward k))
    (closureLax :
      ∀ h, BundleLE
        (pushforward (concreteClosure h))
        (abstractClosure (pushforward h)))
    (h : Bundle S n V)
    (concretePostfixed : PostFixed concreteClosure h) :
    PostFixed abstractClosure (pushforward h) := by
  intro zs
  exact le_transitive
    (pushforwardMonotone concretePostfixed zs)
    (closureLax h zs)

end BehavioralSemantics
