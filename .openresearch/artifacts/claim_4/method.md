# Method

The certificate lists every constructor in the lifting grammar and the exact
premise needed for its induction step. The verifier checks complete coverage,
then a recursive proof function discharges any admitted syntax tree. A
separate normalizer compares both theorem sides for all 676 syntax trees of
depth at most three. This bounded enumeration checks the implementation only;
the primary evidence is structural induction.

Command: `uv run --frozen python repro/src/verify.py && uv run --frozen python repro/src/publication_gate.py`

