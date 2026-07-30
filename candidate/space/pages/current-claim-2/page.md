# Current Claim 2 — closure and behavioral structures

**Status: VERIFIED.**

For arbitrary coalgebra `t_X:X→FX`, lifting `λ_X`, bundle `h_X:X^n→V`, and
tuple in `X^n`, Definitions 3.8–3.9 require
`T_X=t_X*∘λ_X`, its pointwise expansion, and either `h_X⪯T_X(h_X)` or equality.
The typed normalizer accepts precisely this order. Reversed composition and a
fixed-only replacement are rejected.

```json
{"closure":"t_X* o lambda_X","pointwise":"lambda_X(h_X)(t_X(x_1),...,t_X(x_n))","alternatives":2,"status":"VERIFIED"}
```

[Code](https://huggingface.co/spaces/DineshAI/kovefbSXbQ/blob/main/verification/definition_certificates.py) ·
[contract, raw data, checker, controls, limitations](https://huggingface.co/spaces/DineshAI/kovefbSXbQ/tree/main/evidence/claim_2) ·
[environment and runtime](#/current-verification).

Limitation: these are exact definition schemas rather than empirical fixed-point
iteration. The old three-state count remains [Historical rejected baseline](#/claim-2).
