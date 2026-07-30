# Method

The verifier checks one compositional path proof for Proposition 4.1, two
kernel-factorization directions for Proposition 4.2, and two quotient
directions for Proposition 4.3. Each rewrite has a named prerequisite.

Independent direct checkers exhaust 64 small kernel-factorization pairs and
3,840 quotient/transition cases. These check implementation agreement, not
the universal primary proof.

Command: `uv run --frozen python repro/src/verify.py && uv run --frozen python repro/src/publication_gate.py`

