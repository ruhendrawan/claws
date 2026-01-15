import csv
import os
from typing import Dict, Set, Tuple

from s10x_settings import *
from s50x_utils import *



def filter_positive_scores(
    scores: Dict[str, Dict[Tuple[str, str, str], int]],
    threshold: int = 1
) -> Dict[str, Dict[Tuple[str, str, str], int]]:
    filtered: Dict[str, Dict[Tuple[str, str, str], int]] = {}
    for ex, pairs in scores.items():
        pos = {(p, l, o): s for (p, l, o), s in pairs.items() if s >= threshold}
        if pos:  # skip exercises with no positives
            filtered[ex] = pos
    return filtered


def save_positive_scores_csv(
    scores: Dict[str, Dict[Tuple[str, str, str], int]],
    out_path: str,
) -> None:
    os.makedirs(Path(out_path).parent, exist_ok=True)
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["exercise_name", "parent", "leaf", "ontology", "score"])
        for ex, pairs in scores.items():
            for (p, l, o), s in pairs.items():
                writer.writerow([ex, p, l, o, s])

def load_scores_csv(path: str) -> Dict[str, Dict[Tuple[str, str, str], int]]:
    scores: Dict[str, Dict[Tuple[str, str, str], int]] = {}
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            ex = row["exercise_name"].strip()
            p = row["parent"].strip()
            l = row["leaf"].strip()
            v = int(row["score"])
            o = row["ontology"].strip()
            scores.setdefault(ex, {})[(p, l, o)] = v
    return scores




def denormalize_lists(
    positives: Dict[str, Dict[Tuple[str, str, str], int]],
    gold_lists: Dict[str, Dict[str, Set[str]]],
) -> Dict[str, Dict[str, Set[str]]]:
    merge: Dict[str, Dict[str, Set[str]]] = {}
    for ex, gold in gold_lists.items():
        merge[ex] = {
        }
    for ex, pairs in positives.items():
        parser_set: Set[str] = set()
        edu_set: Set[str] = set()
        for (parent, leaf, ontology), _score in pairs.items():
            if ontology.lower() == "parser":
                parser_set.add(parent)
                parser_set.add(leaf)
            elif ontology.lower() == "education":
                edu_set.add(parent)
                edu_set.add(leaf)
        if ex not in merge:
            # ignore exercises not in gold list
            continue
        else:
            merge[ex] = {
                "parser_list": parser_set,
                "educational_list": edu_set,
            }
    return merge


def _fmt_list_cell(items: Set[str]) -> str:
    if not items:
        return "[]"
    return "[" + ", ".join(sorted(items)) + "]"


def save_denormalized_csv(
    merged: Dict[str, Dict[str, Set[str]]],
    out_path: str,
) -> None:
    os.makedirs(Path(out_path).parent, exist_ok=True)
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["exercise_name", "educational_list", "parser_list"])
        for ex, buckets in merged.items():
            edu_cell = _fmt_list_cell(buckets.get("educational_list", set()))
            parser_cell = _fmt_list_cell(buckets.get("parser_list", set()))
            writer.writerow([ex, edu_cell, parser_cell])



if __name__ == "__main__":

    # DON'T CHANGE THESE, they are set in s10x_settings.py


    THRESHOLD = 4  # score >= threshold means the leaf is predicted present


    score_file = Path(CLAWS_OUTPUT_PATH) / f"scores/combined_stats_{PROMPT_SESSION_ID}_{SNIPPET_TYPE}.csv"


    scores = load_scores_csv(score_file)
    print(f"Loaded combined scores for {len(scores)} exercises from {score_file}")

    positives = filter_positive_scores(scores, threshold=THRESHOLD)

    out_pos_file = Path(CLAWS_OUTPUT_PATH) / f"scores/positive_labels_{PROMPT_SESSION_ID}_{SNIPPET_TYPE}_th{THRESHOLD}.csv"
    save_positive_scores_csv(positives, out_pos_file)
    print(f"Saved positives to {out_pos_file}")



    gold_list = read_gold_lists(GOLD_FILE)
    print(f"Loaded gold labels for {len(gold_list)} exercises from {GOLD_FILE}")

    denormalized = denormalize_lists(positives, gold_list)
    out_merge_file = Path(CLAWS_OUTPUT_PATH) / f"scores/positive_lists_{PROMPT_SESSION_ID}_{SNIPPET_TYPE}_th{THRESHOLD}.csv"
    save_denormalized_csv(denormalized, out_merge_file)
    print(f"Saved denormalized lists to {out_merge_file}")