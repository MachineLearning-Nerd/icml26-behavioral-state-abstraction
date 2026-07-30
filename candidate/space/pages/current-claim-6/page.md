# Current Claim 6 — policy-dependent naturality

**Status: VERIFIED.**

For a fixed stationary policy `π:O→A` and every set map `f:X→Y`, Example 2.9
requires `α_Y^π∘F_Moore f=F_Markov f∘α_X^π`. Independent symbolic evaluation
normalizes both sides to `(P f(p(π(o))),o)`.

```json
{"quantifier":"for every set map f : X -> Y","left_equals_right":true,"independent_cases":128,"status":"VERIFIED"}
```

A direct checker exhausts 128 two-state deterministic instances as secondary
evidence. Replacing the shared policy with an incompatible abstract policy
changes the normal form and rejects.

[Code](https://huggingface.co/spaces/DineshAI/kovefbSXbQ/blob/main/verification/definition_certificates.py) ·
[contract, raw data, checker, control, limitations](https://huggingface.co/spaces/DineshAI/kovefbSXbQ/tree/main/evidence/claim_6) ·
[command, seeds, CPU and runtime](#/current-verification).

Limitation: this is a constructional naturality identity, not a benchmark-scale
empirical result. The three-state square is [Historical rejected baseline](#/claim-6).
