# Method

The verifier checks the symbolic composition, pointwise expansion, and both
behavioral-structure alternatives. It rejects reversed composition and a
fixed-point-only substitution.

Command: `uv run --frozen python repro/src/verify.py && uv run --frozen python repro/src/publication_gate.py`

