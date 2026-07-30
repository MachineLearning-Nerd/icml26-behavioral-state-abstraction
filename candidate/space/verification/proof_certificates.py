#!/usr/bin/env python3
"""Small proof kernel for the abstract order arguments in Theorems 3.12–3.13."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CERTIFICATE = ROOT / ".openresearch" / "artifacts" / "claim_3" / "certificate.json"
OUTPUT = ROOT / "outputs" / "proof_certificates.json"


class ProofError(ValueError):
    pass


def expression(value):
    if isinstance(value, str):
        return value
    if not isinstance(value, list) or len(value) != 2:
        raise ProofError(f"invalid expression: {value!r}")
    return value[0], expression(value[1])


def inequality(value):
    if not isinstance(value, list) or len(value) != 2:
        raise ProofError(f"invalid inequality: {value!r}")
    return expression(value[0]), expression(value[1])


def apply(operator, value):
    return operator, value


def verify_proof(proof, properties):
    assumptions = {inequality(item) for item in proof["assumptions"]}
    goal = inequality(proof["goal"])
    if goal in assumptions:
        raise ProofError("circular certificate: goal appears as an assumption")

    derived = {}
    for step in proof["steps"]:
        conclusion = inequality(step["conclusion"])
        rule = step["rule"]
        if rule == "assumption":
            if conclusion not in assumptions:
                raise ProofError(f"{step['id']}: unlisted assumption")
        elif rule == "transitivity":
            first, second = (derived[item] for item in step["premises"])
            if first[1] != second[0] or conclusion != (first[0], second[1]):
                raise ProofError(f"{step['id']}: invalid transitivity")
        elif rule == "monotonicity":
            premise = derived[step["premises"][0]]
            operator = step["operator"]
            expected = apply(operator, premise[0]), apply(operator, premise[1])
            if operator not in properties["monotone"] or conclusion != expected:
                raise ProofError(f"{step['id']}: invalid monotonicity")
        elif rule == "order_reflection":
            premise = derived[step["premises"][0]]
            operator = step["operator"]
            if operator not in properties["order_reflecting"]:
                raise ProofError(f"{step['id']}: operator is not order-reflecting")
            if premise[0][0] != operator or premise[1][0] != operator:
                raise ProofError(f"{step['id']}: reflection premise has wrong operator")
            expected = premise[0][1], premise[1][1]
            if conclusion != expected:
                raise ProofError(f"{step['id']}: invalid order reflection")
        else:
            raise ProofError(f"{step['id']}: unknown rule {rule}")
        derived[step["id"]] = conclusion

    if not proof["steps"] or derived[proof["steps"][-1]["id"]] != goal:
        raise ProofError("last step does not prove the goal")
    return {"goal": proof["goal"], "steps_checked": len(proof["steps"])}


def independent_graph_check(proof, properties):
    facts = {inequality(item) for item in proof["assumptions"]}
    relevant = facts | {inequality(proof["goal"])}
    relevant.update(inequality(step["conclusion"]) for step in proof["steps"])
    changed = True
    while changed:
        changed = False
        additions = set()
        for left, middle in facts:
            for middle_2, right in facts:
                if middle == middle_2:
                    additions.add((left, right))
        for operator in properties["monotone"]:
            additions.update((apply(operator, left), apply(operator, right))
                             for left, right in facts)
        for left, right in facts:
            if (isinstance(left, tuple) and isinstance(right, tuple)
                    and left[0] == right[0]
                    and left[0] in properties["order_reflecting"]):
                additions.add((left[1], right[1]))
        additions.intersection_update(relevant)
        if not additions.issubset(facts):
            facts.update(additions)
            changed = True
    goal = inequality(proof["goal"])
    if goal not in facts:
        raise ProofError("independent closure checker could not derive goal")
    return {"goal_derived": True, "closure_facts": len(facts)}


def expected_rejection(proof, properties, error_fragment):
    try:
        verify_proof(proof, properties)
    except ProofError as error:
        if error_fragment not in str(error):
            raise
        return {"rejected": True, "reason": str(error)}
    raise ProofError("negative control unexpectedly passed")


def run():
    certificate = json.loads(CERTIFICATE.read_text())
    properties = certificate["properties"]
    verified = {}
    independent = {}
    for proof in certificate["proofs"]:
        verified[proof["id"]] = verify_proof(proof, properties)
        independent[proof["id"]] = independent_graph_check(proof, properties)

    missing_surjectivity = {
        "monotone": properties["monotone"],
        "order_reflecting": [],
    }
    reversed_compatibility = json.loads(json.dumps(certificate["proofs"][0]))
    reversed_compatibility["assumptions"][1].reverse()
    controls = {
        "missing_surjectivity": expected_rejection(
            certificate["proofs"][0], missing_surjectivity, "not order-reflecting"
        ),
        "reversed_compatibility": expected_rejection(
            reversed_compatibility, properties, "unlisted assumption"
        ),
    }
    result = {
        "claim": 3,
        "status": "VERIFIED",
        "scope": "Universal abstract preorder proof schema under the paper's stated assumptions.",
        "proofs": verified,
        "independent_checker": independent,
        "negative_controls": controls,
        "limitations": (
            "The checker verifies the order-theoretic transfer step. "
            "The paper's separately stated lifting-compatibility lemmas remain premises."
        ),
    }
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))
    return result


if __name__ == "__main__":
    run()
