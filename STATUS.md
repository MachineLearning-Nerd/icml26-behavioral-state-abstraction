# Status — ICML 2026 behavioral state abstraction

**State: PUBLICATION QUEUED — six source-anchored claim contracts verified locally.**

- Paper: [arXiv:2606.25357](https://arxiv.org/abs/2606.25357)
- Authors: Yivan Zhang, Ziyan Luo, and Manuel Baltieri
- Local result: 6/6 claim contracts `VERIFIED`
- Formal result: 11 Lean kernel-checked theorems, 0 project axioms, 6/6 proof-breaking mutations rejected
- Historical live evaluator result: **6/12**, all six claims classified as valid but toy-scale
- Current Lean revision: not yet assigned a new live evaluator score
- Fixed command: `uv run --frozen python repro/src/verify.py && uv run --frozen python repro/src/publication_gate.py`
- Primary source audit: [`docs/SOURCE_AUDIT.md`](docs/SOURCE_AUDIT.md)
- Branch mapping: [`branch-audit.md`](branch-audit.md)

The current evidence is a Set-level Lean mechanization of the selected
definitions and implications. It does not formalize every appendix lemma or
the complete category-theory library. The 6/12 score remains the only external
judge result until a fresh evaluation is recorded.
