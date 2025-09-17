from collections import defaultdict
import csv
import re
import sys
from typing import Dict, Iterable, List, Tuple, Set





def _err(msg: str) -> None:
    print(f"[ERROR] {msg}", file=sys.stderr)
def _warn(msg: str) -> None:
    print(f"[WARN]  {msg}", file=sys.stderr)



def read_leaves(path: str) -> List[Tuple[str, str]]:
    pairs: List[Tuple[str, str]] = []
    with open(path, "r") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            if not row:
                continue
            parent = row[0].strip()
            leaf = row[1].strip()
            if parent and leaf:
                pairs.append((parent, leaf))
    return pairs



def read_exercise_names(path: str) -> List[str]:
    names: List[str] = []
    seen: Set[str] = set()
    pat = re.compile(r"^\s*#\s*exercise\s+name\s*:\s*(.+)\s*$", re.IGNORECASE)
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            m = pat.match(line)
            if m:
                name = m.group(1).strip()
                if name and name not in seen:
                    seen.add(name)
                    names.append(name)
    return names



def _parse_score(raw: str):
    match = re.search(r"[-+]?\d*\.?\d+", raw)
    if match:
        num_str = match.group(0)
        return int(num_str) if num_str.isdigit() else float(num_str)
    return None



def read_llm_csv_linewise(path):
    with open(path, newline='') as f:
        for lineno, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue

            row = next(csv.reader([line]))

            if row[0].lower() == "exercise_name":
                continue

            if len(row) < 4:
                # print(f"- Skipping malformed line {lineno}: {row}")
                continue

            score = _parse_score(row[-1])
            if score not in [0, 1, 2, 3, 4, 5]:
                print(f"- Warning: Unexpected score '{row[-1]}' parsed as {score} on line {lineno}")
                continue

            yield {
                "lineno": lineno,
                "exercise_name": row[0],
                "parent": row[1],
                "leaf_class": row[2],
                "score": score,
            }


def validate_all_pairs_present(
    scores: Dict[str, Dict[Tuple[str, str], int]],
    exercise_names: Iterable[str],
    pairs: Iterable[Tuple[str, str]],
) -> Dict[str, List[Tuple[str, str]]]:
    required_pairs = list(pairs)
    missing: Dict[str, List[Tuple[str, str]]] = {}
    for ex in exercise_names:
        ex_pairs = scores.get(ex, {})
        miss = [p for p in required_pairs if p not in ex_pairs]
        if miss:
            missing[ex] = miss
    return missing



def save_scores_csv(scores: Dict[str, Dict[Tuple[str, str], int]], path: str) -> None:
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["exercise_name", "parent", "leaf", "score"])
        for ex, pairs in scores.items():
            for (p, l), v in pairs.items():
                writer.writerow([ex, p, l, v])



if __name__ == "__main__":

    LEAVES_PYTHON_FILE = "ontology/hierarchy_python_leaves.csv"
    LEAVES_EDUCATION_FILE = "ontology/hierarchy_educational_python_leaves.csv"

    # CODE_FILE = "data/all_exercise_snippet_with_prob_description.py"
    # LLM_OUTPUT_DIR = "output/window_5/data/code_with_problems/output/"
    # LLM_OUTPUT_DIR = "output/window_10/data/code_with_problems/output/"

    CODE_FILE = "data/parsons_with_prob_description.py"
    LLM_OUTPUT_DIR = "output/parsons_window_5/data/parsons_with_problems/output/"

    CSV_LLM_FILE = LLM_OUTPUT_DIR + "result.csv"
    SCORES_CSV_FILE = LLM_OUTPUT_DIR + "scores.csv"
    RETRY_PYTHON_CSV_FILE = LLM_OUTPUT_DIR + "retry_python.csv"
    RETRY_EDUCATION_CSV_FILE = LLM_OUTPUT_DIR + "retry_education.csv"

    leaves_python = read_leaves(LEAVES_PYTHON_FILE)
    leaves_education = read_leaves(LEAVES_EDUCATION_FILE)

    exercise_names = read_exercise_names(CODE_FILE)

    print(f"Loaded {len(leaves_python)} leaves from {LEAVES_PYTHON_FILE}")
    print(f"Loaded {len(leaves_education)} leaves from {LEAVES_EDUCATION_FILE}")

    print(f"Loaded {len(exercise_names)} exercise names from {CODE_FILE}")


    scores: Dict[str, Dict[Tuple[str, str], int]] = defaultdict(dict)
    for record in read_llm_csv_linewise(CSV_LLM_FILE):
        key = (record["parent"], record["leaf_class"])
        if key in scores[record["exercise_name"]]:
            _warn(f"Line {record['lineno']}: Duplicate pair for exercise '{record['exercise_name']}', {key}.")
            _warn(f"- Overwriting previous score {scores[record['exercise_name']][key]} with {record['score']}.")
        scores[record["exercise_name"]][key] = record["score"]


    save_scores_csv(scores, SCORES_CSV_FILE)
    print(f"Saved scores to {SCORES_CSV_FILE}")



    missing_python = validate_all_pairs_present(scores, exercise_names, leaves_python)
    print(f"Validation against {LEAVES_PYTHON_FILE}:"
          f" {len(missing_python)} exercises with missing pairs."
          f" {len(exercise_names) - len(missing_python)} complete.")
    with open(RETRY_PYTHON_CSV_FILE, "w") as f:
        writer = csv.writer(f)
        writer.writerow(["exercise_name", "parent", "leaf_class"])
        for ex, pairs in missing_python.items():
            for p in pairs:
                writer.writerow([ex, p[0], p[1]])

    missing_education = validate_all_pairs_present(scores, exercise_names, leaves_education)
    print(f"Validation against {LEAVES_EDUCATION_FILE}:"
          f" {len(missing_education)} exercises with missing pairs."
          f" {len(exercise_names) - len(missing_education)} complete.")
    with open(RETRY_EDUCATION_CSV_FILE, "w") as f:
        writer = csv.writer(f)
        writer.writerow(["exercise_name", "parent", "leaf_class"])
        for ex, pairs in missing_education.items():
            for p in pairs:
                writer.writerow([ex, p[0], p[1]])
