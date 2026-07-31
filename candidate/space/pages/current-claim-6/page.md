# Current Claim 6 — policy-dependent naturality

**Status: VERIFIED. Confidence: HIGH.**

Example 2.9's natural transformation is proved for a fixed stationary
`π:O→A`, every set map `f:X→Y`, and an arbitrary probability functor:

```lean
def mooreMap
    (probability : ProbabilityFunctor P)
    (f : X → Y)
    (system : (Action → P X) × Observation) :
    (Action → P Y) × Observation :=
  (fun action => probability.map f (system.1 action), system.2)

def markovMap
    (probability : ProbabilityFunctor P)
    (f : X → Y)
    (system : P X × Observation) :
    P Y × Observation :=
  (probability.map f system.1, system.2)

def policyTransition
    (policy : Observation → Action)
    (system : (Action → P X) × Observation) :
    P X × Observation :=
  (system.1 (policy system.2), system.2)

theorem claim6_policy_transition_natural
    (probability : ProbabilityFunctor P)
    (policy : Observation → Action)
    (f : X → Y)
    (system : (Action → P X) × Observation) :
    policyTransition policy (mooreMap probability f system) =
      markovMap probability f (policyTransition policy system) := by
  rfl
```

The proof is `rfl` because the paper's naturality square commutes by
construction, for arbitrary types and maps—not because values were
enumerated. The mutation uses different concrete and abstract policies; Lean
reports that the sides are not definitionally equal and exits 1.

[Complete source](https://huggingface.co/spaces/DineshAI/kovefbSXbQ/blob/main/verification/Formalization/Policy.lean) ·
[raw result](https://huggingface.co/spaces/DineshAI/kovefbSXbQ/blob/main/results/lean_verification.json) ·
[mutation](https://huggingface.co/spaces/DineshAI/kovefbSXbQ/blob/main/verification/Formalization/Mutants/Claim6IncompatiblePolicy.lean) ·
[contract and source audit](https://huggingface.co/spaces/DineshAI/kovefbSXbQ/tree/main/evidence/claim_6).

Limitation: this is a naturality identity for the policy-closing construction,
not an empirical policy-learning or return claim.
