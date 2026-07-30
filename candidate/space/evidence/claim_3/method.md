# Method

`repro/src/proof_certificates.py` checks a proof object using four explicit
rules: assumption, transitivity, monotonicity, and order reflection. The
certificate encodes the paper's abstract inequalities, not a finite MDP.

A second checker ignores the listed proof steps and computes the closure of
the assumptions under the permitted rules. It must independently derive each
goal. Controls remove pullback order reflection or reverse the closure
compatibility inequality; both must be rejected for the intended reason.

Fixed command:

```bash
uv run --frozen python repro/src/verify.py && uv run --frozen python repro/src/publication_gate.py
```

The run is deterministic and uses no random seed.

