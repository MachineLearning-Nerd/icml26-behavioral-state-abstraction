import Formalization.SafeTransfer

open BehavioralSemantics

def emptyEncoder : Empty → Unit :=
  fun impossible => nomatch impossible

example :
    Function.Surjective emptyEncoder := by
  intro target
  exact ⟨Classical.choice inferInstance, rfl⟩
