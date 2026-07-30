# Current Claim 1 — bundles and coalgebras

**Status: VERIFIED.**

Definition 3.1 quantifies over arbitrary `n∈ℕ` and sets `X,V`: an `n`-ary
bundle is exactly a total map `h_X:X^n→V`. Section 2 supplies arbitrary functor
`F` and coalgebra `t_X:X→FX`. The executable schema accepts both declarations;
an independent malformed-schema checker rejects `X^(n+1)`.

```json
{"bundle":["function",["power","X","n"],"V"],"coalgebra":["function","X",["apply","F","X"]],"status":"VERIFIED"}
```

[Code](https://huggingface.co/spaces/DineshAI/kovefbSXbQ/blob/main/verification/definition_certificates.py) ·
[contract, method, raw data, checker, control, limitations](https://huggingface.co/spaces/DineshAI/kovefbSXbQ/tree/main/evidence/claim_1) ·
[canonical command and CPU record](#/current-verification).

Limitation: this verifies the exact universally parameterized definition; it
does not claim a benchmark or learned behavior. The original 3-state example
remains at [Historical rejected baseline](#/claim-1).
