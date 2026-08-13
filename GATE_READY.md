# Release gate

The local publication gate passes for the selected six-claim evidence bundle:

- all six source-anchored claim contracts are present and `VERIFIED`;
- every claim has an independent mechanism and a negative control;
- the Lean build checks 11 generic theorems;
- the axiom audit reports no project-declared axioms;
- all six proof-breaking mutations are rejected;
- the theory-scope limitation and primary-source audit are explicit.

This marker describes local reproducibility readiness. It does not replace the
historical external score of 6/12 or imply that the current Lean revision has
already been re-evaluated.
