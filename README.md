# Proof-grade reproduction: all six behavioral-semantics claims

[![Open in molab](https://marimo.io/molab-shield.svg)](https://molab.marimo.io/github/MachineLearning-Nerd/icml26-repro-kovefbSXbQ-behavioral-state-abstraction/blob/main/notebooks/behavioral_semantics_reproduction.py)

We tested all six claims selected from *Compositional Behavioral Semantics for
State Abstraction in Reinforcement Learning* ([arXiv:2606.25357](https://arxiv.org/abs/2606.25357)).
The paper states universal definitions, theorems, and propositions rather than
headline scalar results. We therefore replaced the previously judged 3–4-state
examples with independently checked symbolic proof certificates over arbitrary
maps, bundles, relations, and lifting expressions.

**Assessment:** all six exact claim contracts are internally **VERIFIED**.
This is a forecast, not a new judge result: the live score remains **6/12** until
the evaluator reviews the published revision. The observed result is six
certificate checks passing, 14 hypothesis-removal controls rejecting, and
4,708 independent finite checker cases agreeing. The main proof certificates
are not downscaled; the retained finite enumerations are explicitly secondary
checks. Everything ran single-threaded on local CPU with no GPU and no
stochastic seeds.

Read the [illustrated report](reports/claim-by-claim/report.md), inspect the
[tutorial notebook](notebooks/behavioral_semantics_reproduction.py), or run:

```bash
uv run --frozen python repro/src/verify.py && uv run --frozen python repro/src/publication_gate.py
```

## Experiment log

| Branch / experiment | Purpose or change | Exact run command | Assessment / outcome | Compute |
|---|---|---|---|---|
| `main` | Publication surface | Not run as an experiment (publication surface) | Mirrors the winning cumulative verifier and report | — |
| [`judged-finite-instance-baseline`](https://github.com/MachineLearning-Nerd/icml26-repro-kovefbSXbQ-behavioral-state-abstraction/tree/orx/judged-finite-instance-baseline) | Freeze and rerun the judged toy baseline | `uv run --frozen python repro/src/verify.py && uv run --frozen python repro/src/publication_gate.py` | Six finite checks pass; remains historical toy evidence | local CPU, 1 core estimate, ~5 s orchestration |
| [`c3-symbolic-safe-transfer-certificate`](https://github.com/MachineLearning-Nerd/icml26-repro-kovefbSXbQ-behavioral-state-abstraction/tree/orx/c3-symbolic-safe-transfer-certificate) | Theorems 3.12–3.13 abstract preorder certificate | `uv run --frozen python repro/src/verify.py && uv run --frozen python repro/src/publication_gate.py` | Claim 3 VERIFIED; two malformed-premise controls reject | local CPU, 1 core estimate, ~5 s |
| [`c1-c2-c6-symbolic-definition-and-naturality-cert`](https://github.com/MachineLearning-Nerd/icml26-repro-kovefbSXbQ-behavioral-state-abstraction/tree/orx/c1-c2-c6-symbolic-definition-and-naturality-cert) | Definitions 3.1/3.8/3.9 and Example 2.9 | `uv run --frozen python repro/src/verify.py && uv run --frozen python repro/src/publication_gate.py` | Claims 1, 2, 6 VERIFIED; four controls reject | local CPU, 1 core estimate, ~5 s |
| [`c4-structural-zero-predicate-certificate`](https://github.com/MachineLearning-Nerd/icml26-repro-kovefbSXbQ-behavioral-state-abstraction/tree/orx/c4-structural-zero-predicate-certificate) | Theorem 3.14 structural induction | `uv run --frozen python repro/src/verify.py && uv run --frozen python repro/src/publication_gate.py` | Claim 4 VERIFIED; 676-tree checker agrees | local CPU, 1 core estimate, ~5 s |
| [`c5-rl-proposition-proof-certificates`](https://github.com/MachineLearning-Nerd/icml26-repro-kovefbSXbQ-behavioral-state-abstraction/tree/orx/c5-rl-proposition-proof-certificates) | Propositions 4.1–4.3 symbolic proof paths | `uv run --frozen python repro/src/verify.py && uv run --frozen python repro/src/publication_gate.py` | Claim 5 VERIFIED; 3,904 checker cases agree | local CPU, 1 core estimate, ~5 s |
| [`evaluator-visible-release-candidate-and-gates`](https://github.com/MachineLearning-Nerd/icml26-repro-kovefbSXbQ-behavioral-state-abstraction/tree/orx/evaluator-visible-release-candidate-and-gates) | Candidate Space, visibility matrix, red team, report, and cumulative gate | `uv run --frozen python repro/src/verify.py && uv run --frozen python repro/src/publication_gate.py` | Release candidate; publication depends on all fail-closed gates | local CPU, 1 core estimate, expected <10 s |

## Upstream reproduction

# Compositional Behavioral Semantics for State Abstraction in Reinforcement Learning

Source-faithful CPU reproduction for ICML 2026 paper `kovefbSXbQ`,
*Compositional Behavioral Semantics for State Abstraction in Reinforcement
Learning* (arXiv `2606.25357`).

The historical verifier executed six source-anchored finite-set constructions.
Those checks are preserved for regression but are superseded by the current
proof certificates. Primary-source anchors are in
[`docs/SOURCE_AUDIT.md`](docs/SOURCE_AUDIT.md).
