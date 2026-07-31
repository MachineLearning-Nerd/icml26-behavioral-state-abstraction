import Formalization.RL

universe u

namespace BehavioralSemantics

def mooreMap
    {P : Type u → Type u} {Action Observation X Y : Type u}
    (probability : ProbabilityFunctor P)
    (f : X → Y)
    (system : (Action → P X) × Observation) :
    (Action → P Y) × Observation :=
  (fun action => probability.map f (system.1 action), system.2)

def markovMap
    {P : Type u → Type u} {Observation X Y : Type u}
    (probability : ProbabilityFunctor P)
    (f : X → Y)
    (system : P X × Observation) :
    P Y × Observation :=
  (probability.map f system.1, system.2)

def policyTransition
    {P : Type u → Type u} {Action Observation X : Type u}
    (policy : Observation → Action)
    (system : (Action → P X) × Observation) :
    P X × Observation :=
  (system.1 (policy system.2), system.2)

theorem claim6_policy_transition_natural
    {P : Type u → Type u} {Action Observation X Y : Type u}
    (probability : ProbabilityFunctor P)
    (policy : Observation → Action)
    (f : X → Y)
    (system : (Action → P X) × Observation) :
    policyTransition policy (mooreMap probability f system) =
      markovMap probability f (policyTransition policy system) := by
  rfl

end BehavioralSemantics
