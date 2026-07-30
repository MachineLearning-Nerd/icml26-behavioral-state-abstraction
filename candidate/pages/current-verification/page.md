# Current verification

This page supersedes the historical finite-instance verifier at judged Space
revision `5a8a6266162a652c6216487c4df8116b15c63aca`.

## Claim 3 — safe verification and construction

**Current status: VERIFIED.**

The exact quantified contract is the pair of universal implications in
Theorems 3.12–3.13, under coalgebra homomorphism, common-operator lifting
compatibility, the required joins, and (for reflection) encoder surjectivity.
The current verifier uses an abstract proof certificate rather than a larger
finite MDP.

Raw result:

```json
{
  "theorem_3_12": {"steps_checked": 4, "independent_goal_derived": true},
  "theorem_3_13": {"steps_checked": 4, "independent_goal_derived": true},
  "missing_surjectivity_control": "rejected",
  "reversed_compatibility_control": "rejected"
}
```

Run:

```bash
uv run --frozen python repro/src/verify.py && uv run --frozen python repro/src/publication_gate.py
```

Code: `repro/src/proof_certificates.py`. Contract, proof object, raw JSON,
independent output, controls, and limitations are in
`.openresearch/artifacts/claim_3/`.

The historical 4-state check remains preserved but is labeled
**Historical rejected baseline** and is not the current verifier.

