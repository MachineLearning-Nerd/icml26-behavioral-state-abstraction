# Method

Primary evidence is `verification/Formalization/Core.lean`, built by
`verification/lean_gate.py`. The gate scans for forbidden proof shortcuts,
runs `lake build`, audits theorem dependencies, and requires the wrong-arity
mutation to fail. Fixed command:
`uv run --frozen python repro/src/verify.py && uv run --frozen python repro/src/publication_gate.py`.
