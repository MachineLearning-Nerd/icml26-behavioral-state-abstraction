# STATUS — kovefbSXbQ

**State: PUBLICATION QUEUED — six source-anchored claims verified locally.**

- Pinned primary source: arXiv `2606.25357` public TeX archive.
- All six anchored claims map to Sections 2--4 and public appendices; there is
  no unavailable data, model, or GPU requirement.
- `python3 repro/src/verify.py` exhausts the finite construction tests and
  writes `outputs/verdict.json`.
- `python3 repro/src/publication_gate.py` is fail-closed: it requires all six
  claims, a source/evidence bundle, and one negative control per claim.
- Public GitHub evidence: `MachineLearning-Nerd/icml26-repro-kovefbSXbQ-behavioral-state-abstraction`
  at commit `bec2dc4`.
- Atomically queued through `enqueue_backlog.py`; the shared HF drain is the
  sole publisher.  It is currently waiting for the account Space-creation
  quota, so no direct publish is attempted here.
