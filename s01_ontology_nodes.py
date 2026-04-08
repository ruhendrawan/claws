# ## Ontology

# Generate list of leave nodes as CSV for LLM Prompt Context.


import argparse
import csv
import json
from pathlib import Path

import pandas as pd
from rdflib import RDF, RDFS, Graph


def clean_uri(uri):
    return uri.split("#")[-1] if "#" in uri else uri.split("/")[-1]


def build_class_hierarchy(rdf_file_path, format="xml"):
    g = Graph()
    g.parse(rdf_file_path, format=format)

    hierarchy = {}
    class_labels = set()
    comments = {}

    for s, p, o in g:
        if p == RDFS.subClassOf:
            child = clean_uri(str(s))
            parent = clean_uri(str(o))

            class_labels.add(child)
            class_labels.add(parent)

            if parent not in hierarchy:
                hierarchy[parent] = []
            hierarchy[parent].append(child)

        if p == RDFS.comment:
            # Some classes have multiple rdfs:comment values; RDF triple iteration
            # order can be non-deterministic, so pick a stable "best" description.
            label = clean_uri(str(s))
            candidate = str(o)
            existing = comments.get(label)
            if (
                existing is None
                or len(candidate) > len(existing)
                or (len(candidate) == len(existing) and candidate > existing)
            ):
                comments[label] = candidate

    for label in class_labels:
        hierarchy.setdefault(label, [])

    return hierarchy, comments


def save_dict_to_text(data, output_file_path):
    with open(output_file_path, "w", encoding="utf-8") as f:
        f.write(json.dumps(data, indent=2))


def extract_subtree(hierarchy, root):
    subtree = {}

    def dfs(node):
        if node not in hierarchy:
            return
        subtree[node] = hierarchy[node]
        for child in hierarchy[node]:
            dfs(child)

    dfs(root)
    return subtree


def extract_leaves_with_parents(subtree):
    leaves_with_parents = []
    for parent, children in subtree.items():
        for child in children:
            if child in subtree and not subtree[child]:
                leaves_with_parents.append((parent, child))
    return leaves_with_parents


code_patterns = {
    "IfCheckingInForLoop": "refers to an if statement inside a for loop",
    "IfElifCheckingInForLoop": "refers to an if-elif statement inside a for loop",
    "IfElifElseCheckingInForLoop": "refers to an if-elif-else statement inside a for loop",
    "IfElseCheckingInForLoop": "refers to an if-else statement inside a for loop",
    "IfCheckingInWhileLoop": "refers to an if statement inside a while loop",
    "IfElifCheckingInWhileLoop": "refers to an if-elif statement inside a while loop",
    "IfElifElseCheckingInWhileLoop": "refers to an if-elif-else statement inside a while loop",
    "IfElseCheckingInWhileLoop": "refers to an if-else statement inside a while loop",
    "IfChecking": "refers to an if statement which is not placed inside any loop",
    "IfElifChecking": "refers to an if-elif statement which is not placed inside any loop",
    "IfElifElseChecking": "refers to an if-elif-else statement which is not placed inside any loop",
    "IfElseChecking": "refers to an if-else statement which is not placed inside any loop",
    "NestedIfChecking": "refers to an if inside another if",
    "ListReferencing": "refers to the code in which one list is set equal to another, and a change to one of the lists causes the same change in the other list. ListReferencing should only be marked as present if a list is explicitly assigned to another list variable (e.g., list2 = list1).",
    "AccessingDictionary": "includes any operation that retrieves values from a dictionary, including direct indexing (dict[key]) and methods like .get(), .items(), .keys(), and .values().",
    "MixedNestedLoopIteration": "refers to nested loop such that a while-loop inside a for-loop or a for-loop inside a while-loop",
    "NestedForLoopIteration": "refers to nested loop such that a for-loop is inside another for-loop",
    "NestedWhileLoopIteration": "refers to nested loop such that a while-loop is inside another while-loop",
    "SingleForLoopIteration": "refers to a single use use of a for-loop that has no nested structure",
    "SingleWhileLoopIteration": "refers to a single use of a while-loop that has no nested structure",
    "CallingFunctionLibrary": "refers to ANY use of built-in Python functions (print, len, replace, etc.) and built-in methods of objects (like list.append() or string.replace(), etc.).",
    "CallingNestedFunction": "refers to calling a function that was defined inside another user-defined function, but the call itself can happen anywhere (inside or outside the enclosing function).",
    "DefiningNestedFunction": "refers to defining a function inside another user-defined function.",
    "CallingRecursiveFunction": "refers to calling a function that calls itself (recursion)",
    "DefiningRecursiveFunction": "refers to defining a function that calls itself within its own body (recursion).",
    "NestedFunctionCall": "refers to when one function call is placed as an argument to another function call (e.g., f(g(x)))",
    "DefiningStandardFunction": "refers to defining a function that: 1) Does not call any other user-defined functions 2) Is not nested inside another function 3) Does not call itself (not recursive) Note: A standard function may still call built-in functions. Additionally, DefiningStandardFunction can still be later called in nested patterns (NestedFunctionCall).",
    "CallingStandardFunction": "refers to calling a function that meets all the 3 following criteria:1) Does not call any other user-defined functions 2) Is not nested inside another function 3) Does not call itself (not recursive) Note: A standard function may still call built-in functions.",
}


leaf_filter = [
    # Python Parser
    "UnaryOperation",
    "IndexingExpression",
    "SlicingExpression",
    # Educational
    "IndexingDictionary",
    "IndexingList",
    "IndexingString",
    "IndexingTuple",
    "SlicingList",
    "SlicingTuple",
    "SlicingString",
    "WhileLoopWithListIndexing",
    "WhileLoopWith*=",
    "WhileLoopWith+=",
    "ForLoopWithListIndexing",
    "ForLoopWith*=",
    "ForLoopWith+=",
    "ReplacingDictionaryElement",
    "ReplacingListElement",
    "ReplacingElement2DArray",
]
leaf_filter = None


def save_leaves_with_parents_csv(leaves_with_parents, output_csv_path, comments):
    with open(output_csv_path, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Parent", "Leaf", "Description"])
        for parent, leaf in leaves_with_parents:
            if parent == "EducationalPython":
                parent = "Python"
            if parent == "Iteration":
                parent = "NonNestedIteration"
            if parent == "ModifyingStrigCase":
                parent = "ModifyingStringCase"
            if parent == "CallingStandardFunction" and leaf == "NestedCall":
                continue

            is_leaf_included = True
            if leaf_filter:
                is_leaf_included = leaf in leaf_filter

            if is_leaf_included:
                description = comments.get(leaf) or code_patterns.get(leaf, "")
                writer.writerow([parent, leaf, description])


if __name__ == "__main__":
    # WARNING: By default this overwrites files in `ontology/`.
    #
    # Historically, this script was run once to generate the ontology CSV files and
    # keep ordering consistent for comparison across experiments.

    parser = argparse.ArgumentParser(
        description="Generate ontology hierarchy + leaf CSVs from an OWL (RDF/XML) file."
    )
    parser.add_argument(
        "--rdf-file",
        default="data/final_ontology.owl",
        help="Path to OWL/RDF file to parse.",
    )
    parser.add_argument(
        "--rdf-format", default="xml", help="RDFLib parse format (default: xml)."
    )
    parser.add_argument(
        "--out-dir",
        default="ontology",
        help="Output directory for hierarchy and CSV files.",
    )
    args = parser.parse_args()

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    hierarchy, comments = build_class_hierarchy(args.rdf_file, format=args.rdf_format)

    save_dict_to_text(hierarchy, out_dir / "hierarchy.txt")

    educational_python_subtree = extract_subtree(hierarchy, "EducationalPython")
    python_subtree = extract_subtree(hierarchy, "Python")

    save_dict_to_text(
        educational_python_subtree, out_dir / "hierarchy_educational_python.txt"
    )
    save_dict_to_text(python_subtree, out_dir / "hierarchy_python.txt")

    educational_python_leaves = extract_leaves_with_parents(educational_python_subtree)
    python_leaves = extract_leaves_with_parents(python_subtree)

    save_leaves_with_parents_csv(
        educational_python_leaves,
        out_dir / "hierarchy_educational_python_leaves.csv",
        comments,
    )
    save_leaves_with_parents_csv(
        python_leaves,
        out_dir / "hierarchy_python_leaves.csv",
        comments,
    )

    print("CSV leaf outputs with parent and description saved:", str(out_dir))
