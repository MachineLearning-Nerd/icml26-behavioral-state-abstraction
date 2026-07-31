import Formalization.Policy

open BehavioralSemantics

def identityProbability : ProbabilityFunctor (fun X => X) where
  map := fun function value => function value
  map_id := by intros; rfl
  map_comp := by intros; rfl

def actionSystem : (Bool → Nat) × Unit :=
  (fun action => if action then 1 else 0, ())

example :
    policyTransition (P := fun X => X) (fun _ => true)
        (mooreMap identityProbability (id : Nat → Nat) actionSystem) =
      markovMap identityProbability (id : Nat → Nat)
        (policyTransition (P := fun X => X) (fun _ => false)
          actionSystem) := by
  rfl
