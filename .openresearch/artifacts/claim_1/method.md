# Method

The symbolic verifier checks the source-transcribed function types using
uninterpreted parameters `X`, `n`, `V`, and `F`. The independent source audit
checks the ar5iv and TeX anchors. A malformed `X^(n+1)` domain is rejected.

Command: `uv run --frozen python repro/src/verify.py && uv run --frozen python repro/src/publication_gate.py`

