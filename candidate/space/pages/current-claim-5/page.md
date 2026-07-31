# Current Claim 5 — RL abstraction propositions

**Status: VERIFIED. Confidence: HIGH.**

The formalization uses arbitrary types, an abstract probability functor with
identity/composition laws, Moore systems, and arbitrary encoders.

```lean
structure ProbabilityFunctor (P : Type u → Type u) where
  map : {X Y : Type u} → (X → Y) → P X → P Y
  map_id : ∀ {X} (distribution : P X),
    map (fun x => x) distribution = distribution
  map_comp : ∀ {X Y Z} (f : X → Y) (g : Y → Z) (distribution : P X),
    map g (map f distribution) = map (fun x => g (f x)) distribution

def ModelIrrelevant
    {P : Type u → Type u}
    {Action Observation Source Target : Type u}
    (probability : ProbabilityFunctor P)
    (encoder : Source → Target)
    (source : MooreSystem P Action Observation Source) : Prop :=
  ∀ left right, encoder left = encoder right →
    mooreImage probability encoder source left =
      mooreImage probability encoder source right

theorem claim5_model_irrelevance_iff_homomorphism
    [Nonempty ((Action → P Target) × Observation)]
    (probability : ProbabilityFunctor P)
    (encoder : Source → Target)
    (source : MooreSystem P Action Observation Source) :
    ModelIrrelevant probability encoder source ↔
      ∃ target : MooreSystem P Action Observation Target,
        MooreHomomorphism probability encoder source target := by
  constructor
  · intro irrelevant
    obtain ⟨factor, factors⟩ :=
      factors_through_of_kernel_inclusion
        encoder (mooreImage probability encoder source) irrelevant
    let target : MooreSystem P Action Observation Target := {
      transition := fun state => (factor state).1
      observation := fun state => (factor state).2
    }
    refine ⟨target, ?_⟩
    intro state
    exact (factors state).symm
  · rintro ⟨target, homomorphism⟩
    exact kernel_inclusion_of_factors_through
      encoder
      (mooreImage probability encoder source)
      (fun state => (target.transition state, target.observation state))
      (fun state => (homomorphism state).symm)

theorem claim5_next_observation_prediction
    {P : Type u → Type u}
    {Action Observation Source Target : Type u}
    (probability : ProbabilityFunctor P)
    (encoder : Source → Target)
    (source : MooreSystem P Action Observation Source)
    (target : MooreSystem P Action Observation Target)
    (homomorphism : MooreHomomorphism probability encoder source target)
    (state : Source) (action : Action) :
    probability.map source.observation (source.transition state action) =
      probability.map target.observation
        (target.transition (encoder state) action) := by
  have transitionEquality :=
    congrArg (fun pair => pair.1 action) (homomorphism state)
  have observationFunctions :
      source.observation = fun x => target.observation (encoder x) := by
    funext x
    exact congrArg Prod.snd (homomorphism x)
  calc
    probability.map source.observation (source.transition state action) =
        probability.map (fun x => target.observation (encoder x))
          (source.transition state action) := by rw [observationFunctions]
    _ = probability.map target.observation
          (probability.map encoder (source.transition state action)) :=
        (probability.map_comp encoder target.observation
          (source.transition state action)).symm
    _ = probability.map target.observation
          (target.transition (encoder state) action) := by
        rw [transitionEquality]

theorem claim5_bisimulation_quotient_iff_postfixed
    (mapF : {X Y : Type u} → (X → Y) → F X → F Y)
    (relation : Setoid State)
    (transition : State → F State) :
    QuotientPostfixed mapF relation transition ↔
      QuotientHomomorphismExists mapF relation transition := by
  constructor
  · intro postfixed
    let quotientTransition : Quotient relation → F (Quotient relation) :=
      fun quotient => Quotient.liftOn quotient
        (fun state => mapF Quotient.mk' (transition state))
        (fun left right related => postfixed left right related)
    refine ⟨quotientTransition, ?_⟩
    intro state
    rfl
  · rintro ⟨quotientTransition, homomorphism⟩
    intro left right related
    calc
      mapF Quotient.mk' (transition left) =
          quotientTransition (Quotient.mk' left) := homomorphism left
      _ = quotientTransition (Quotient.mk' right) :=
        congrArg quotientTransition (Quotient.sound related)
      _ = mapF Quotient.mk' (transition right) :=
        (homomorphism right).symm
```

The mutation removes fiber constancy from Proposition 4.2. Lean exposes the
missing universal kernel condition and exits 1. The quotient proof uses Lean's
actual quotient type, not a finite partition table.

[Complete, directly executable source](https://huggingface.co/spaces/DineshAI/kovefbSXbQ/blob/main/verification/Formalization/RL.lean) ·
[raw result](https://huggingface.co/spaces/DineshAI/kovefbSXbQ/blob/main/results/lean_verification.json) ·
[mutation](https://huggingface.co/spaces/DineshAI/kovefbSXbQ/blob/main/verification/Formalization/Mutants/Claim5MissingKernelCondition.lean) ·
[contract and anchors](https://huggingface.co/spaces/DineshAI/kovefbSXbQ/tree/main/evidence/claim_5).

Limitation: Proposition 4.2 needs a nonempty output to define behavior on
representation states outside the encoder image. This is stated explicitly in
the Lean theorem and corresponds to extending the factor map off the image.
