# Environment and reproduction boundary

## Locked inputs

- Python: `3.12` via [`uv.lock`](uv.lock)
- Lean: `4.32.0` via [`lean-toolchain`](lean-toolchain)
- Lake project: [`lakefile.toml`](lakefile.toml)
- Python package setup: [`pyproject.toml`](pyproject.toml)

Run the committed local checks with:

```bash
uv sync --frozen
uv run --frozen python repro/src/verify.py
uv run --frozen python repro/src/publication_gate.py
```

The formal release used one Lean worker on Hugging Face `cpu-upgrade`; no GPU
or random seed was used. The release record reports 64 visible logical CPUs
and a 29.088961-second formal verifier run; the aggregate machine-readable
record also retains a later 14.300909-second run.

## Formal scope

The Lean layer checks 11 generic theorems and reports zero project-declared
axioms. Individual Lean theorems may use standard foundational mechanisms such
as `Classical.choice`, `propext`, or `Quot.sound`; those are reported rather
than hidden. Six deliberately broken proof variants are required to fail.

Finite Python checks are deterministic implementation diagnostics. They do not
establish the paper’s universal categorical scope by themselves. Claim 3 keeps
the lifting-compatibility lemmas as premises, and Claim 5 states the standard
nonempty-MDP extension for unused representation states.
