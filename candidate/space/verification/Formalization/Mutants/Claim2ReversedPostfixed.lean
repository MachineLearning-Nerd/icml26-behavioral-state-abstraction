import Formalization.Core

open BehavioralSemantics

def alwaysOne : Bundle Unit 1 Nat :=
  fun _ => 1

def collapseToZero : Bundle Unit 1 Nat → Bundle Unit 1 Nat :=
  fun _ _ => 0

example : PostFixed collapseToZero alwaysOne := by
  intro tuple
  exact Nat.le_refl 1
