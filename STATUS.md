# Status — Compositional Behavioral Semantics for State Abstraction in Reinforcement Learning

**State: scoped Lean audit complete; candidate awaiting a fresh live evaluation.**

- Paper: [arXiv:2606.25357](https://arxiv.org/abs/2606.25357)
- ICML submission: `kovefbSXbQ`
- Authors: Yivan Zhang, Ziyan Luo, and Manuel Baltieri
- Overall audit: `ALL_SIX_CLAIMS_VERIFIED_SCOPED_LEAN_KERNEL_11_THEOREMS_NO_PROJECT_AXIOMS_HISTORICAL_SCORE_6_OF_12_NO_CURRENT_SCORE`
- Local result: 6/6 claim contracts `VERIFIED_SCOPED`
- Formal result: 11 Lean kernel-checked theorems, 0 project axioms, 6/6 proof-breaking mutations rejected
- Historical live evaluator result: **6/12**, all six claims classified as valid but toy-scale; historical only
- Current Lean revision: not assigned a new live evaluator score
- Current score claim: `false`
- Publication allowed: `false` until a fresh evaluator result exists
- Official author endorsement: `false` / not claimed
- Fixed command: `uv run --frozen python repro/src/verify.py && uv run --frozen python repro/src/publication_gate.py`
- Primary source audit: [`docs/SOURCE_AUDIT.md`](docs/SOURCE_AUDIT.md)
- Branch mapping: [`branch-audit.md`](branch-audit.md)
- Commit identity: all reachable history uses `MachineLearning-Nerd <MachineLearning-Nerd@users.noreply.github.com>`
- Recovery bundle SHA-256: `cd47e23fb7901042e7d6d8ddc3f320d8acc7287b5a23891f1168acb2b440ed96`

The current evidence is a Set-level Lean mechanization of the selected
definitions and implications. It does not formalize every appendix lemma or
the complete category-theory library. The 6/12 score remains the only external
judge result until a fresh evaluation is recorded.
