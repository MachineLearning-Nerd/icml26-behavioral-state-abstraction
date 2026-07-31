# Method

Primary evidence is `verification/Formalization/SafeTransfer.lean`. It proves
order reflection by choosing a preimage for every tuple coordinate, then
derives Theorems 3.12–3.13 from the exact closure inequalities in the paper's
Lemma 3.11. `lean_gate.py` kernel-builds the proof and requires
`Claim3MissingSurjectivity.lean` to fail.
