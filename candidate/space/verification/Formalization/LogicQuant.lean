universe u v w

namespace BehavioralSemantics

inductive LiftingExpr (Q : Type u) (A : Type v) where
  | leaf : Q → LiftingExpr Q A
  | combinator : LiftingExpr Q A → LiftingExpr Q A → LiftingExpr Q A
  | aggregator : (A → LiftingExpr Q A) → LiftingExpr Q A
  | barycenter : (A → LiftingExpr Q A) → LiftingExpr Q A

structure QuantitativeOperators (Q : Type u) (A : Type v) where
  combinator : Q → Q → Q
  aggregator : (A → Q) → Q
  barycenter : (A → Q) → Q

structure LogicalOperators (B : Type w) (A : Type v) where
  combinator : B → B → B
  aggregator : (A → B) → B
  barycenter : (A → B) → B

def evalQuantitative
    {Q : Type u} {A : Type v}
    (operators : QuantitativeOperators Q A) :
    LiftingExpr Q A → Q
  | .leaf value => value
  | .combinator left right =>
      operators.combinator
        (evalQuantitative operators left)
        (evalQuantitative operators right)
  | .aggregator children =>
      operators.aggregator (fun index =>
        evalQuantitative operators (children index))
  | .barycenter children =>
      operators.barycenter (fun index =>
        evalQuantitative operators (children index))

def evalLogical
    {Q : Type u} {A : Type v} {B : Type w}
    (operators : LogicalOperators B A)
    (zero : Q → B) :
    LiftingExpr Q A → B
  | .leaf value => zero value
  | .combinator left right =>
      operators.combinator
        (evalLogical operators zero left)
        (evalLogical operators zero right)
  | .aggregator children =>
      operators.aggregator (fun index =>
        evalLogical operators zero (children index))
  | .barycenter children =>
      operators.barycenter (fun index =>
        evalLogical operators zero (children index))

structure ZeroHomomorphism
    {Q : Type u} {A : Type v} {B : Type w}
    (quantitative : QuantitativeOperators Q A)
    (logical : LogicalOperators B A)
    (zero : Q → B) where
  combinator :
    ∀ left right,
      zero (quantitative.combinator left right) =
        logical.combinator (zero left) (zero right)
  aggregator :
    ∀ values,
      zero (quantitative.aggregator values) =
        logical.aggregator (fun index => zero (values index))
  barycenter :
    ∀ values,
      zero (quantitative.barycenter values) =
        logical.barycenter (fun index => zero (values index))

theorem claim4_zero_predicate_commutes
    {Q : Type u} {A : Type v} {B : Type w}
    (quantitative : QuantitativeOperators Q A)
    (logical : LogicalOperators B A)
    (zero : Q → B)
    (homomorphism : ZeroHomomorphism quantitative logical zero) :
    ∀ expression,
      zero (evalQuantitative quantitative expression) =
        evalLogical logical zero expression := by
  intro expression
  induction expression with
  | leaf value =>
      rfl
  | combinator left right leftIH rightIH =>
      rw [evalQuantitative, evalLogical, homomorphism.combinator]
      rw [leftIH, rightIH]
  | aggregator children childrenIH =>
      rw [evalQuantitative, evalLogical, homomorphism.aggregator]
      congr
      funext index
      exact childrenIH index
  | barycenter children childrenIH =>
      rw [evalQuantitative, evalLogical, homomorphism.barycenter]
      congr
      funext index
      exact childrenIH index

end BehavioralSemantics
