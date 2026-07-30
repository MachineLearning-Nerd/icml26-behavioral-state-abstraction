# Current Claim 3 — safe verification and construction

**Status: VERIFIED. Confidence: MEDIUM.**

Under common-operator lifting compatibility and a coalgebra homomorphism,
Theorem 3.12 universally reflects abstract post-fixedness from the pullback
when the encoder is surjective. Theorem 3.13 universally preserves concrete
post-fixedness under pushforward when the required fiber joins exist. Two
abstract preorder certificates close in four justified steps each; an
independent forward-chaining checker derives both goals from four facts.

```json
{"theorem_3_12":{"steps":4,"goal_derived":true},"theorem_3_13":{"steps":4,"goal_derived":true},"status":"VERIFIED"}
```

Removing surjectivity prevents order reflection; reversing the compatibility
direction supplies no applicable fact. Both controls reject.

[Code](https://huggingface.co/spaces/DineshAI/kovefbSXbQ/blob/main/verification/proof_certificates.py) ·
[proof object, contract, raw data, checker, controls, limitations](https://huggingface.co/spaces/DineshAI/kovefbSXbQ/tree/main/evidence/claim_3) ·
[command and source hashes](#/current-verification).

Limitation: the order-theoretic transfer is checked while the paper's separately
stated lifting-compatibility lemmas remain explicit premises. The four-state
example is [Historical rejected baseline](#/claim-3).
