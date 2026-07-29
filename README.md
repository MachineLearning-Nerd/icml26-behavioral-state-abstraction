# Compositional Behavioral Semantics for State Abstraction in Reinforcement Learning

Source-faithful CPU reproduction for ICML 2026 paper `kovefbSXbQ`,
*Compositional Behavioral Semantics for State Abstraction in Reinforcement
Learning* (arXiv `2606.25357`).

This CPU-only reproduction executes six source-anchored finite-set
constructions: bundles and closure/post-fixed points, safe pullback
verification, safe pushforward construction, logical/quantitative
zero-predicate transfer, RL abstraction/bisimulation, and policy-dependent
naturality.

Run the complete verification:

```bash
python3 repro/src/verify.py
python3 repro/src/publication_gate.py
```

The primary-source anchors and exact scope are in
[`docs/SOURCE_AUDIT.md`](docs/SOURCE_AUDIT.md); machine-readable evidence is
in [`outputs/verdict.json`](outputs/verdict.json).
