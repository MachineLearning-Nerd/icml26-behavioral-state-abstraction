universe u

namespace BehavioralSemantics

structure ProbabilityFunctor (P : Type u → Type u) where
  map : {X Y : Type u} → (X → Y) → P X → P Y
  map_id : ∀ {X : Type u} (distribution : P X),
    map (fun x => x) distribution = distribution
  map_comp : ∀ {X Y Z : Type u}
    (f : X → Y) (g : Y → Z) (distribution : P X),
    map g (map f distribution) = map (fun x => g (f x)) distribution

structure MooreSystem
    (P : Type u → Type u)
    (Action Observation State : Type u) where
  transition : State → Action → P State
  observation : State → Observation

def mooreImage
    {P : Type u → Type u}
    {Action Observation Source Target : Type u}
    (probability : ProbabilityFunctor P)
    (encoder : Source → Target)
    (source : MooreSystem P Action Observation Source)
    (state : Source) :
    (Action → P Target) × Observation :=
  (fun action => probability.map encoder (source.transition state action),
   source.observation state)

def MooreHomomorphism
    {P : Type u → Type u}
    {Action Observation Source Target : Type u}
    (probability : ProbabilityFunctor P)
    (encoder : Source → Target)
    (source : MooreSystem P Action Observation Source)
    (target : MooreSystem P Action Observation Target) : Prop :=
  ∀ state,
    mooreImage probability encoder source state =
      (target.transition (encoder state), target.observation (encoder state))

def ModelIrrelevant
    {P : Type u → Type u}
    {Action Observation Source Target : Type u}
    (probability : ProbabilityFunctor P)
    (encoder : Source → Target)
    (source : MooreSystem P Action Observation Source) : Prop :=
  ∀ left right,
    encoder left = encoder right →
      mooreImage probability encoder source left =
        mooreImage probability encoder source right

theorem factors_through_of_kernel_inclusion
    {Source Target Output : Type u} [Nonempty Output]
    (encoder : Source → Target)
    (observable : Source → Output)
    (fiberConstant :
      ∀ left right, encoder left = encoder right →
        observable left = observable right) :
    ∃ factor : Target → Output,
      ∀ state, factor (encoder state) = observable state := by
  classical
  let fallback : Output := Classical.choice (inferInstance : Nonempty Output)
  let factor : Target → Output := fun target =>
    if witness : ∃ state, encoder state = target then
      observable (Classical.choose witness)
    else
      fallback
  refine ⟨factor, ?_⟩
  intro state
  simp only [factor]
  split
  next witness =>
    apply fiberConstant (Classical.choose witness) state
    exact Classical.choose_spec witness
  next missing =>
    exact False.elim (missing ⟨state, rfl⟩)

theorem kernel_inclusion_of_factors_through
    {Source Target Output : Type u}
    (encoder : Source → Target)
    (observable : Source → Output)
    (factor : Target → Output)
    (factors : ∀ state, factor (encoder state) = observable state) :
    ∀ left right, encoder left = encoder right →
      observable left = observable right := by
  intro left right sameFiber
  rw [← factors left, ← factors right, sameFiber]

theorem claim5_model_irrelevance_iff_homomorphism
    {P : Type u → Type u}
    {Action Observation Source Target : Type u}
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
        encoder
        (mooreImage probability encoder source)
        irrelevant
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
      (fun state =>
        (target.transition state, target.observation state))
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
  have transitionEquality :
      probability.map encoder (source.transition state action) =
        target.transition (encoder state) action :=
    congrArg (fun pair => pair.1 action) (homomorphism state)
  have observationEquality :
      source.observation state = target.observation (encoder state) :=
    congrArg Prod.snd (homomorphism state)
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

def QuotientPostfixed
    {F : Type u → Type u} {State : Type u}
    (mapF : {X Y : Type u} → (X → Y) → F X → F Y)
    (relation : Setoid State)
    (transition : State → F State) : Prop :=
  ∀ left right,
    relation.r left right →
      mapF (Quotient.mk' : State → Quotient relation) (transition left) =
        mapF (Quotient.mk' : State → Quotient relation) (transition right)

def QuotientHomomorphismExists
    {F : Type u → Type u} {State : Type u}
    (mapF : {X Y : Type u} → (X → Y) → F X → F Y)
    (relation : Setoid State)
    (transition : State → F State) : Prop :=
  ∃ quotientTransition : Quotient relation → F (Quotient relation),
    ∀ state,
      mapF (Quotient.mk' : State → Quotient relation) (transition state) =
        quotientTransition (Quotient.mk' state)

theorem claim5_bisimulation_quotient_iff_postfixed
    {F : Type u → Type u} {State : Type u}
    (mapF : {X Y : Type u} → (X → Y) → F X → F Y)
    (relation : Setoid State)
    (transition : State → F State) :
    QuotientPostfixed mapF relation transition ↔
      QuotientHomomorphismExists mapF relation transition := by
  constructor
  · intro postfixed
    let quotientTransition : Quotient relation → F (Quotient relation) :=
      fun quotient =>
        Quotient.liftOn quotient
          (fun state =>
            mapF (Quotient.mk' : State → Quotient relation)
              (transition state))
          (fun left right related => postfixed left right related)
    refine ⟨quotientTransition, ?_⟩
    intro state
    rfl
  · rintro ⟨quotientTransition, homomorphism⟩
    intro left right related
    calc
      mapF (Quotient.mk' : State → Quotient relation) (transition left) =
          quotientTransition (Quotient.mk' left) := homomorphism left
      _ = quotientTransition (Quotient.mk' right) :=
        congrArg quotientTransition (Quotient.sound related)
      _ = mapF (Quotient.mk' : State → Quotient relation)
          (transition right) := (homomorphism right).symm

end BehavioralSemantics
