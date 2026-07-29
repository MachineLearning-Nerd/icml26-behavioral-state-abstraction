# Results

Run the complete CPU verification with:

```bash
python3 repro/src/verify.py
python3 repro/src/publication_gate.py
```

All six anchored construction claims pass.  The structured evidence is in
[`outputs/verdict.json`](outputs/verdict.json).

| Claim | Executable construction audit | Necessary-hypothesis control |
|---|---|---|
| C1 — behavioral bundles and closure | Enumerates all Boolean predicates of a 3-state system and evaluates the pullback-of-lifting closure | Omitting current-state safety makes an unsafe state appear post-fixed |
| C2 — post-fixed behavioral structure | Checks fixed versus post-fixed predicates under Definitions 3.8–3.9 | The same omitted-safety construction changes the result |
| C3 — safe verification/construction | Exhaustively checks pullback reflection under a surjective homomorphism and pushforward preservation for every concrete post-fixed predicate | Non-surjectivity breaks reflection; a non-homomorphism breaks pushforward preservation |
| C4 — logical/quantitative zero predicate | Exhausts nonnegative tuples for sum, max, and uniform expectation zero laws | Subtraction violates the required zero relation |
| C5 — RL state abstraction and quotient | Checks observation preservation, transition pushforward, kernel/bisimulation, and policy closure on a finite stochastic Moore quotient | An observation mismatch breaks the homomorphism |
| C6 — policy-dependent transition | Checks that state-distribution pushforward commutes with the policy-selected transition | An incompatible abstract action breaks the naturality square |

## Scope

This is a source-faithful theory reproduction.  Finite executions establish
the exact constructions and exhibit why their hypotheses matter; they are not
presented as a new proof of the paper’s universal categorical theorems.  The
general quantifiers and categorical arguments remain anchored to the public
primary-source TeX proofs listed in the source audit.
