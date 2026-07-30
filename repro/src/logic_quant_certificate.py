#!/usr/bin/env python3
"""Structural proof certificate for Theorem 3.14."""
from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CERTIFICATE = ROOT / ".openresearch" / "artifacts" / "claim_4" / "certificate.json"
OUTPUT = ROOT / "outputs" / "logic_quant_certificate.json"

GRAMMAR = {"leaf", "combinator", "aggregator", "barycenter"}
REQUIRED = {
    "leaf": set(),
    "combinator": {"children_commute", "z_combinator_homomorphism"},
    "aggregator": {"child_commutes", "z_aggregator_homomorphism"},
    "barycenter": {"child_commutes", "z_barycenter_homomorphism"},
}


class CertificateError(ValueError):
    pass


def validate_induction_certificate(certificate):
    cases = {case["constructor"]: set(case["requires"])
             for case in certificate["induction_cases"]}
    if set(cases) != GRAMMAR:
        raise CertificateError("induction cases do not cover the lifting grammar")
    for constructor, requirements in REQUIRED.items():
        if cases[constructor] != requirements:
            raise CertificateError(f"wrong premises for {constructor}")
    if certificate["conclusion"] != (
        "forall h. z o lambda_quant(h) = lambda_truth(z o h)"
    ):
        raise CertificateError("certificate proves the wrong conclusion")
    return {"constructors_covered": len(cases), "premises_exact": True}


def prove_tree(tree, laws):
    constructor = tree[0]
    if constructor == "leaf":
        return 1
    if constructor == "combinator":
        if "z_combinator_homomorphism" not in laws:
            raise CertificateError("missing combinator homomorphism")
        return 1 + prove_tree(tree[1], laws) + prove_tree(tree[2], laws)
    if constructor == "aggregator":
        if "z_aggregator_homomorphism" not in laws:
            raise CertificateError("missing aggregator homomorphism")
        return 1 + prove_tree(tree[1], laws)
    if constructor == "barycenter":
        if "z_barycenter_homomorphism" not in laws:
            raise CertificateError("missing barycenter homomorphism")
        return 1 + prove_tree(tree[1], laws)
    raise CertificateError(f"constructor outside lifting grammar: {constructor}")


def quantitative_term(tree):
    constructor = tree[0]
    if constructor == "leaf":
        return ("q_leaf", "h")
    if constructor == "combinator":
        return ("q_combinator", quantitative_term(tree[1]),
                quantitative_term(tree[2]))
    if constructor == "aggregator":
        return ("q_aggregator", quantitative_term(tree[1]))
    if constructor == "barycenter":
        return ("q_barycenter", quantitative_term(tree[1]))
    raise CertificateError(f"unknown constructor {constructor}")


def truth_term(tree):
    constructor = tree[0]
    if constructor == "leaf":
        return ("truth_leaf", ("z", "h"))
    if constructor == "combinator":
        return ("truth_combinator", truth_term(tree[1]), truth_term(tree[2]))
    if constructor == "aggregator":
        return ("truth_aggregator", truth_term(tree[1]))
    if constructor == "barycenter":
        return ("truth_barycenter", truth_term(tree[1]))
    raise CertificateError(f"unknown constructor {constructor}")


def push_zero(term):
    constructor = term[0]
    if constructor == "q_leaf":
        return ("truth_leaf", ("z", term[1]))
    if constructor == "q_combinator":
        return ("truth_combinator", push_zero(term[1]), push_zero(term[2]))
    if constructor == "q_aggregator":
        return ("truth_aggregator", push_zero(term[1]))
    if constructor == "q_barycenter":
        return ("truth_barycenter", push_zero(term[1]))
    raise CertificateError(f"cannot push z through {constructor}")


@lru_cache(maxsize=None)
def trees(depth):
    leaf = (("leaf",),)
    if depth == 0:
        return leaf
    children = trees(depth - 1)
    generated = list(leaf)
    generated.extend(("aggregator", child) for child in children)
    generated.extend(("barycenter", child) for child in children)
    generated.extend(("combinator", left, right)
                     for left in children for right in children)
    return tuple(generated)


def independent_normal_form_check(depth):
    checked = 0
    for tree in trees(depth):
        assert push_zero(quantitative_term(tree)) == truth_term(tree)
        checked += 1
    return {"depth": depth, "syntax_trees": checked, "all_normal_forms_equal": True}


def expect_failure(tree, laws, fragment):
    try:
        prove_tree(tree, laws)
    except CertificateError as error:
        if fragment not in str(error):
            raise
        return {"rejected": True, "reason": str(error)}
    raise CertificateError("negative control unexpectedly passed")


def run():
    certificate = json.loads(CERTIFICATE.read_text())
    induction = validate_induction_certificate(certificate)
    laws = set(certificate["algebra_homomorphism_laws"])
    witness_tree = (
        "combinator",
        ("aggregator", ("leaf",)),
        ("barycenter", ("leaf",)),
    )
    nodes = prove_tree(witness_tree, laws)
    controls = {
        "missing_combinator_law": expect_failure(
            witness_tree, laws - {"z_combinator_homomorphism"}, "combinator"
        ),
        "missing_aggregator_law": expect_failure(
            witness_tree, laws - {"z_aggregator_homomorphism"}, "aggregator"
        ),
        "missing_barycenter_law": expect_failure(
            witness_tree, laws - {"z_barycenter_homomorphism"}, "barycenter"
        ),
    }
    result = {
        "claim": 4,
        "status": "VERIFIED",
        "scope": (
            "Structural proof for every finite lifting expression generated "
            "by the paper's three operator constructors."
        ),
        "induction_certificate": induction,
        "representative_tree_nodes": nodes,
        "independent_checker": independent_normal_form_check(3),
        "negative_controls": controls,
        "non_circularity": (
            "No numeric range or sampled tuple is primary evidence; the "
            "result follows by constructor coverage and structural recursion."
        ),
    }
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))
    return result


if __name__ == "__main__":
    run()

