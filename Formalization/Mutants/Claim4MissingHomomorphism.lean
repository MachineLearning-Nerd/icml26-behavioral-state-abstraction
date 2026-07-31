import Formalization.LogicQuant

open BehavioralSemantics

def quantitative : QuantitativeOperators Nat Unit where
  combinator := Nat.add
  aggregator := fun values => values ()
  barycenter := fun values => values ()

def logical : LogicalOperators Bool Unit where
  combinator := Bool.and
  aggregator := fun values => values ()
  barycenter := fun values => values ()

example :
    ∀ expression,
      decide (evalQuantitative quantitative expression = 0) =
        evalLogical logical (fun value => decide (value = 0)) expression :=
  claim4_zero_predicate_commutes quantitative logical
    (fun value => decide (value = 0))
