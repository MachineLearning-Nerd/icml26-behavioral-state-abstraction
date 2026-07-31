import Std

universe u v

namespace BehavioralSemantics

abbrev Tuple (X : Type u) (n : Nat) := Fin n → X

abbrev Bundle (X : Type u) (n : Nat) (V : Type v) := Tuple X n → V

structure Coalgebra (F : Type u → Type u) (X : Type u) where
  transition : X → F X

structure BundleLifting
    (F : Type u → Type u) (n : Nat) (V : Type v) where
  lift : {X : Type u} → Bundle X n V → Bundle (F X) n V

def pullTuple {X Y : Type u} {n : Nat}
    (f : X → Y) (xs : Tuple X n) : Tuple Y n :=
  fun i => f (xs i)

def pullBundle {X Y : Type u} {n : Nat} {V : Type v}
    (f : X → Y) (h : Bundle Y n V) : Bundle X n V :=
  fun xs => h (pullTuple f xs)

def closure {F : Type u → Type u} {X : Type u} {n : Nat} {V : Type v}
    (system : Coalgebra F X)
    (lifting : BundleLifting F n V)
    (h : Bundle X n V) : Bundle X n V :=
  fun xs => lifting.lift h (fun i => system.transition (xs i))

def BundleLE {X : Type u} {n : Nat} {V : Type v} [LE V]
    (h k : Bundle X n V) : Prop :=
  ∀ xs, h xs ≤ k xs

def PostFixed {X : Type u} {n : Nat} {V : Type v} [LE V]
    (operator : Bundle X n V → Bundle X n V)
    (h : Bundle X n V) : Prop :=
  BundleLE h (operator h)

def Fixed {X : Type u} {n : Nat} {V : Type v}
    (operator : Bundle X n V → Bundle X n V)
    (h : Bundle X n V) : Prop :=
  h = operator h

def BehavioralStructure {X : Type u} {n : Nat} {V : Type v} [LE V]
    (operator : Bundle X n V → Bundle X n V)
    (h : Bundle X n V) : Prop :=
  PostFixed operator h ∨ Fixed operator h

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

theorem claim2_closure_pointwise
    {F : Type u → Type u} {X : Type u} {n : Nat} {V : Type v}
    (system : Coalgebra F X)
    (lifting : BundleLifting F n V)
    (h : Bundle X n V) (xs : Tuple X n) :
    closure system lifting h xs =
      lifting.lift h (fun i => system.transition (xs i)) :=
  rfl

theorem claim2_fixed_is_postfixed
    {X : Type u} {n : Nat} {V : Type v} [LE V]
    (operator : Bundle X n V → Bundle X n V)
    (h : Bundle X n V)
    (le_refl : ∀ value : V, value ≤ value)
    (fixed : Fixed operator h) :
    PostFixed operator h := by
  intro xs
  rw [congrFun fixed xs]
  exact le_refl (operator h xs)

end BehavioralSemantics
