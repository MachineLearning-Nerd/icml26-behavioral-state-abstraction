# Current Claim 5 — RL abstraction propositions

**Status: VERIFIED. Confidence: MEDIUM.**

Proposition 4.1 quantifies over every state/action and follows from
transition/observation homomorphism rewrites. Proposition 4.2 is proved in both
directions via kernel factorization. Proposition 4.3 is proved in both
directions for an arbitrary equivalence and its surjective quotient. Five
symbolic derivations close in three steps each.

```json
{"proof_paths":5,"kernel_maps_checked":64,"quotient_cases":3840,"status":"VERIFIED"}
```

Independent checkers validate 64 maps and 3,840 quotient/bisimulation cases.
Removing observation preservation, target extension, or equivalence rejects.

[Code](https://huggingface.co/spaces/DineshAI/kovefbSXbQ/blob/main/verification/rl_proposition_certificates.py) ·
[certificate, contract, raw data, checkers, controls, limitations](https://huggingface.co/spaces/DineshAI/kovefbSXbQ/tree/main/evidence/claim_5) ·
[command and source hashes](#/current-verification).

Limitation: the reverse Proposition 4.2 direction uses the standard nonempty-MDP
extension from the encoder image to unused representation states. The old
four-state MDP is [Historical rejected baseline](#/claim-5).
