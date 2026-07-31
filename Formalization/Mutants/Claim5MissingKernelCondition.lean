import Formalization.RL

open BehavioralSemantics

def constantEncoder : Bool → Unit :=
  fun _ => ()

example :
    ∃ factor : Unit → Bool,
      ∀ state, factor (constantEncoder state) = state :=
  factors_through_of_kernel_inclusion constantEncoder id
