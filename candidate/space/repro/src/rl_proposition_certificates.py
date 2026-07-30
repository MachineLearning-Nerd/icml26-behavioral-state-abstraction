#!/usr/bin/env python3
"""Symbolic proof certificates for Propositions 4.1–4.3."""
from __future__ import annotations

import itertools
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CERTIFICATE = ROOT / ".openresearch" / "artifacts" / "claim_5" / "certificate.json"
OUTPUT = ROOT / "outputs" / "rl_proposition_certificates.json"


class CertificateError(ValueError):
    pass


PATH_REWRITES = {
    "transition_homomorphism": (("f", "t_Y"), ("t_X", "P_f")),
    "probability_functoriality": (("P_f", "P_oY"), ("P_(oY_after_f)",)),
    "observation_homomorphism": (("P_(oY_after_f)",), ("P_oX",)),
}

LOGIC_REWRITES = {
    "unfold_model_irrelevance": (
        "model_irrelevance",
        "ker(f) <= ker(pair(P_f_after_tS,oS))",
        None,
    ),
    "kernel_factorization_forward": (
        "ker(f) <= ker(pair(P_f_after_tS,oS))",
        "exists tZ. pair(P_f_after_tS,oS) = tZ_after_f",
        "target_extension",
    ),
    "homomorphism_definition_forward": (
        "exists tZ. pair(P_f_after_tS,oS) = tZ_after_f",
        "f_is_F_Moore_homomorphism",
        None,
    ),
    "homomorphism_definition_backward": (
        "f_is_F_Moore_homomorphism",
        "exists tZ. pair(P_f_after_tS,oS) = tZ_after_f",
        None,
    ),
    "kernel_factorization_backward": (
        "exists tZ. pair(P_f_after_tS,oS) = tZ_after_f",
        "ker(f) <= ker(pair(P_f_after_tS,oS))",
        None,
    ),
    "fold_model_irrelevance": (
        "ker(f) <= ker(pair(P_f_after_tS,oS))",
        "model_irrelevance",
        None,
    ),
    "unfold_postfixed_quotient": (
        "r_postfixed",
        "ker(q_r) <= ker(F_qr_after_tX)",
        "r_equivalence",
    ),
    "quotient_factorization_forward": (
        "ker(q_r) <= ker(F_qr_after_tX)",
        "exists tq. F_qr_after_tX = tq_after_qr",
        "quotient_surjective",
    ),
    "quotient_homomorphism_forward": (
        "exists tq. F_qr_after_tX = tq_after_qr",
        "q_r_is_homomorphism",
        None,
    ),
    "quotient_homomorphism_backward": (
        "q_r_is_homomorphism",
        "exists tq. F_qr_after_tX = tq_after_qr",
        None,
    ),
    "quotient_factorization_backward": (
        "exists tq. F_qr_after_tX = tq_after_qr",
        "ker(q_r) <= ker(F_qr_after_tX)",
        None,
    ),
    "fold_postfixed_quotient": (
        "ker(q_r) <= ker(F_qr_after_tX)",
        "r_postfixed",
        "r_equivalence",
    ),
}


def replace_subsequence(path, old, new):
    for index in range(len(path) - len(old) + 1):
        if path[index:index + len(old)] == old:
            return path[:index] + new + path[index + len(old):]
    raise CertificateError(f"rewrite source {old} not present")


def check_path_proof(proof, properties):
    current = tuple(proof["start"])
    for step in proof["steps"]:
        rule = step["rule"]
        if rule not in properties:
            raise CertificateError(f"missing property {rule}")
        old, new = PATH_REWRITES[rule]
        current = replace_subsequence(current, old, new)
        if current != tuple(step["result"]):
            raise CertificateError(f"{step['id']}: recorded result is not the rewrite result")
    if current != tuple(proof["goal"]):
        raise CertificateError("path proof does not reach its goal")
    return {"steps_checked": len(proof["steps"]), "goal": proof["goal"]}


def check_logic_proof(proof, properties):
    current = proof["start"]
    for step in proof["steps"]:
        before, after, requirement = LOGIC_REWRITES[step["rule"]]
        if current != before:
            raise CertificateError(f"{step['id']}: rule does not apply")
        if requirement and requirement not in properties:
            raise CertificateError(f"missing property {requirement}")
        current = after
        if current != step["result"]:
            raise CertificateError(f"{step['id']}: recorded result is wrong")
    if current != proof["goal"]:
        raise CertificateError("logic proof does not reach its goal")
    return {"steps_checked": len(proof["steps"]), "goal": proof["goal"]}


def expect_failure(checker, proof, properties, fragment):
    try:
        checker(proof, properties)
    except CertificateError as error:
        if fragment not in str(error):
            raise
        return {"rejected": True, "reason": str(error)}
    raise CertificateError("negative control unexpectedly passed")


def kernel_included(f, g, source):
    return all(f[x] != f[y] or g[x] == g[y] for x in source for y in source)


def factors_through(f, g, source, target, outputs):
    return any(
        all(g[x] == dict(zip(target, values))[f[x]] for x in source)
        for values in itertools.product(outputs, repeat=len(target))
    )


def independent_factorization_check():
    source, target, outputs = range(3), range(2), range(2)
    checked = 0
    for f_values in itertools.product(target, repeat=len(source)):
        f = dict(zip(source, f_values))
        for g_values in itertools.product(outputs, repeat=len(source)):
            g = dict(zip(source, g_values))
            assert kernel_included(f, g, source) == factors_through(
                f, g, source, target, outputs
            )
            checked += 1
    return {"maps_checked": checked, "equivalence_holds": True}


def partitions(items):
    if not items:
        yield ()
        return
    first, *rest = items
    for partition in partitions(rest):
        yield ((first,),) + partition
        for index in range(len(partition)):
            yield partition[:index] + (
                tuple(sorted((first,) + partition[index])),
            ) + partition[index + 1:]


def canonical_partitions(items):
    unique = set()
    for partition in partitions(list(items)):
        canonical = tuple(sorted(tuple(sorted(block)) for block in partition))
        unique.add(canonical)
    return sorted(unique)


def independent_quotient_check():
    states = tuple(range(4))
    checked = 0
    for partition in canonical_partitions(states):
        block_of = {
            state: index
            for index, block in enumerate(partition)
            for state in block
        }
        for transition_values in itertools.product(states, repeat=len(states)):
            transition = dict(zip(states, transition_values))
            postfixed = all(
                block_of[x] != block_of[y]
                or block_of[transition[x]] == block_of[transition[y]]
                for x in states for y in states
            )
            quotient_homomorphism_exists = all(
                len({block_of[transition[x]] for x in block}) == 1
                for block in partition
            )
            assert postfixed == quotient_homomorphism_exists
            checked += 1
    return {
        "equivalences": len(canonical_partitions(states)),
        "transition_systems_per_equivalence": 4 ** 4,
        "cases": checked,
        "biconditional_holds": True,
    }


def run():
    certificate = json.loads(CERTIFICATE.read_text())
    properties = set(certificate["properties"])
    proofs = {}
    for proof in certificate["proofs"]:
        checker = check_path_proof if proof["kind"] == "path" else check_logic_proof
        proofs[proof["id"]] = checker(proof, properties)

    by_id = {proof["id"]: proof for proof in certificate["proofs"]}
    controls = {
        "missing_observation_preservation": expect_failure(
            check_path_proof,
            by_id["proposition_4_1"],
            properties - {"observation_homomorphism"},
            "observation_homomorphism",
        ),
        "missing_target_extension": expect_failure(
            check_logic_proof,
            by_id["proposition_4_2_forward"],
            properties - {"target_extension"},
            "target_extension",
        ),
        "non_equivalence_quotient": expect_failure(
            check_logic_proof,
            by_id["proposition_4_3_forward"],
            properties - {"r_equivalence"},
            "r_equivalence",
        ),
    }
    result = {
        "claim": 5,
        "status": "VERIFIED",
        "scope": "Universal symbolic proofs of Propositions 4.1–4.3 under their Set/MDP assumptions.",
        "proofs": proofs,
        "independent_checkers": {
            "kernel_factorization": independent_factorization_check(),
            "quotient_bisimulation": independent_quotient_check(),
        },
        "negative_controls": controls,
        "non_circularity": (
            "The primary proofs rewrite arbitrary morphism/kernel symbols. "
            "Finite enumeration checks the proof implementation only."
        ),
        "limitation": (
            "Proposition 4.2 uses the standard nonempty-MDP extension from "
            "the encoder image to unused representation states."
        ),
    }
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))
    return result


if __name__ == "__main__":
    run()

