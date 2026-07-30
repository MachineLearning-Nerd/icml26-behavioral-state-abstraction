# Environment and compute

- Fixed command: `uv run --frozen python repro/src/verify.py && uv run --frozen python repro/src/publication_gate.py`
- Python: 3.12.11, repository `uv.lock`, standard library only
- Core estimate before run: 1
- Selected compute: authorized local CPU; no `cpu-upgrade` flavor needed
- Actual allocation: one Python process on a host exposing 8 logical CPUs; no worker pool
- Runtime: approximately 5 s OpenResearch orchestration
- Seed: none; the verifier is deterministic
- Scientific Git SHA: `2c1464ef685441abcfee84af3dc1722594a6dd3d`
