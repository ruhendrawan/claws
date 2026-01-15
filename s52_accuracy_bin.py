import csv
import ast
import os
import re
from pathlib import Path
import sys
from typing import Any, Dict, Set, Tuple, List

from s10x_settings import *
from s50x_utils import *



def _err(msg: str) -> None:
    print(f"[ERROR] {msg}", file=sys.stderr)
def _warn(msg: str) -> None:
    print(f"[WARN]  {msg}", file=sys.stderr)
def ensure_parent_dir(path: Path) -> None:
    os.makedirs(path.parent, exist_ok=True)



def scores_to_predicted_leaves(
    scores: Dict[str, Dict[Tuple[str, str, str], int]],
    threshold: int = 1,
    gold_view: str = "parser",
) -> Dict[str, Set[str]]:
    pred: Dict[str, Set[str]] = {}
    for ex, pair_scores in scores.items():
        present = {
            leaf
            for (_parent, leaf, _ontology), s in pair_scores.items()
            if isinstance(s, (int, float)) and s >= threshold and _ontology == gold_view
        }
        pred[ex] = present
    return pred



def _prf(tp: int, fp: int, fn: int) -> Tuple[float, float, float]:
    precision = tp / (tp + fp) if (tp + fp) else 0.0
    recall    = tp / (tp + fn) if (tp + fn) else 0.0
    f1        = (2 * precision * recall / (precision + recall)) if (precision + recall) else 0.0
    return precision, recall, f1



def evaluate_against_gold_sets(
    pred_leaves: Dict[str, Set[str]],
    gold_sets: Dict[str, Set[str]],
) -> Tuple[List[Dict[str, Any]], Dict[str, float], Dict[str, float]]:

    exercises = sorted(gold_sets.keys())
    rows: List[Dict[str, Any]] = []

    total_tp = total_fp = total_fn = 0
    exact_sum = 0.0
    jacc_sum = 0.0


    missing = [ex for ex in exercises if ex not in pred_leaves]
    if missing:
        _warn(f"Predictions missing for {len(missing)} exercises")
    for ex in missing:
        _warn(f"  {ex}")

    for ex in exercises:

        if ex not in pred_leaves:
            _warn(f"Predictions missing for exercise '{ex}'; treating as empty set.")

        pred = pred_leaves.get(ex, set())
        gold = gold_sets.get(ex, set())

        tp = len(pred & gold)
        fp = len(pred - gold)
        fn = len(gold - pred)

        p, r, f = _prf(tp, fp, fn)

        denom_union = (tp + fp + fn)
        jacc = tp / denom_union if denom_union > 0 else 1.0
        exact = 1.0 if pred == gold else 0.0

        rows.append({
            "exercise_name": ex,
            "pred_count": len(pred),
            "gold_count": len(gold),
            "tp": tp, "fp": fp, "fn": fn,
            "precision": p, "recall": r, "f1": f,
            "jaccard": jacc,
            "accuracy_exact": exact,
        })

        total_tp += tp
        total_fp += fp
        total_fn += fn
        exact_sum += exact
        jacc_sum += jacc

    n = len(rows) or 1
    macro = {
        "precision": sum(r["precision"] for r in rows) / n,
        "recall":    sum(r["recall"]    for r in rows) / n,
        "f1":        sum(r["f1"]        for r in rows) / n,
        "jaccard":   jacc_sum / n,
        "accuracy_exact": exact_sum / n,
    }
    micro_p, micro_r, micro_f = _prf(total_tp, total_fp, total_fn)
    micro_j = (total_tp / (total_tp + total_fp + total_fn)) if (total_tp + total_fp + total_fn) else 1.0
    micro = {"precision": micro_p, "recall": micro_r, "f1": micro_f, "jaccard": micro_j}

    return rows, micro, macro


_BIN_PAIR_RE = re.compile(r"([A-Za-z0-9_]+_bin)=([^/\\]+)")

_NUM_TO_WORD = {
    "length_lines_bin": {"0": "short", "1": "long"},
    "chars_bin":        {"0": "short", "1": "long"},
    "comments_bin":     {"0": "low",   "1": "high"},
}

def _extract_bin_filters_from_batch_id(batch_id: str) -> List[Tuple[str, str]]:
    return _BIN_PAIR_RE.findall(batch_id)

def _normalize_bin_value(bin_col: str, raw_val: str) -> str:
    val = raw_val.strip()
    mapping = _NUM_TO_WORD.get(bin_col)
    if mapping and val in mapping:
        return mapping[val]
    return val



def get_allowed_exercises_for_batch(bin_csv_path: str, batch_id: str) -> Set[str]:

    pairs = _extract_bin_filters_from_batch_id(batch_id)
    if not pairs:
        raise ValueError(f"No '<bin_col>=<bin_val>' pattern found in batch_id: {batch_id}")

    filters: List[Tuple[str, str]] = [(col, _normalize_bin_value(col, val)) for col, val in pairs]

    with open(bin_csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None:
            raise ValueError(f"Bin CSV has no header: {bin_csv_path}")

        headers = set(reader.fieldnames)
        if "exercise_name" in headers:
            id_col = "exercise_name"
        elif "exercise_id" in headers:
            id_col = "exercise_id"
        else:
            raise ValueError("Bin CSV must include 'exercise_name' or 'exercise_id' column.")

        for col, _ in filters:
            if col not in headers:
                raise ValueError(f"Bin column '{col}' not found in {bin_csv_path}. "
                    f"Available: {sorted(headers)}")

        allowed: Set[str] = set()
        for row in reader:
            ex_id = (row.get(id_col) or "").strip()
            if not ex_id:
                continue

            ok = True
            for col, want in filters:
                got = (row.get(col) or "").strip()
                got_norm = _normalize_bin_value(col, got)
                if got_norm != want:
                    ok = False
                    break

            if ok:
                allowed.add(ex_id)

    return allowed






def filter_gold_to_exercises(
    gold_all: Dict[str, Dict[str, Set[str]]],
    allowed_exercises: Set[str],
    view: str,
) -> Dict[str, Set[str]]:
    filtered: Dict[str, Set[str]] = {}
    for ex in allowed_exercises:
        if ex in gold_all:
            filtered[ex] = gold_all[ex].get(view, set())
        else:
            # If gold is missing for an allowed exercise, treat as empty target set.
            filtered[ex] = set()
            _warn(f"Gold missing for exercise '{ex}'; using empty set.")
    return filtered


def filter_scores_to_exercises(
    scores: Dict[str, Dict[Tuple[str, str, str], int]],
    allowed_exercises: Set[str],
) -> Dict[str, Dict[Tuple[str, str, str], int]]:
    return {ex: pairs for ex, pairs in scores.items() if ex in allowed_exercises}



def filter_gold_by_type(
    gold_all: Dict[str, Dict[str, Set[str]]],
    view: str = "parser",
) -> Dict[str, Set[str]]:
    return {ex: v.get(view, set()) for ex, v in gold_all.items()}



def run_final_metrics(
    batch_id: str,
    scores: Dict[str, Dict[Tuple[str, str, str], int]],
    gold_csv_path: str,
    gold_view: str = "parser",
    threshold: int = 1,
    allowed_exercises: Set[str] | None = None,
    CLAWS_OUTPUT_PATH: str = ".",
    PROMPT_SESSION_ID: str = "window_unknown",
) -> None:

    gold_all = read_gold_lists(gold_csv_path)

    # if allowed_exercises is not None:
    #     scores = filter_scores_to_exercises(scores, allowed_exercises)
    #     gold_sets = filter_gold_to_exercises(gold_all, allowed_exercises, gold_view)
    # else:
    #     gold_sets = {ex: v.get(gold_view, set()) for ex, v in gold_all.items()}


    gold_sets = filter_gold_by_type(gold_all, gold_view)

    pred_gold_view = gold_view
    if gold_view=="educational":
        pred_gold_view="education"
    pred_sets = scores_to_predicted_leaves(scores, threshold=threshold, gold_view=pred_gold_view)


    # print(scores)
    # print()
    # print(gold_sets)
    # print()
    # print(pred_sets)
    # exit()

    per, micro, macro = evaluate_against_gold_sets(pred_sets, gold_sets)

    out_csv_path = Path(CLAWS_OUTPUT_PATH) / f"scores/accuracy_{batch_id}_{gold_view}_{threshold}.csv"
    ensure_parent_dir(out_csv_path)
    with open(out_csv_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "exercise_name","pred_count","gold_count","tp","fp","fn",
            "precision","recall","f1","jaccard","accuracy_exact"
        ])
        for r in per:
            writer.writerow([
                r["exercise_name"], r["pred_count"], r["gold_count"],
                r["tp"], r["fp"], r["fn"],
                f"{r['precision']:.4f}", f"{r['recall']:.4f}", f"{r['f1']:.4f}",
                f"{r['jaccard']:.4f}", f"{r['accuracy_exact']:.4f}"
            ])
    print(f"Saved detailed accuracy per exercise to {out_csv_path}")

    summary_csv_path = f"output/accuracy_summary.csv"
    summary_exists = os.path.exists(summary_csv_path)
    # ensure_parent_dir(summary_csv_path)
    with open(summary_csv_path, "a", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        if not summary_exists:
            writer.writerow([
                "batch_id", "gold_view", "threshold",
                "precision_macro", "recall_macro", "f1_macro", "jaccard_macro", "exact_accuracy_macro",
                "precision_micro", "recall_micro", "f1_micro", "jaccard_micro"
            ])
        writer.writerow([
            batch_id, gold_view, threshold,
            f"{macro['precision']:.4f}", f"{macro['recall']:.4f}", f"{macro['f1']:.4f}",
            f"{macro['jaccard']:.4f}", f"{macro['accuracy_exact']:.4f}",
            f"{micro['precision']:.4f}", f"{micro['recall']:.4f}", f"{micro['f1']:.4f}", f"{micro['jaccard']:.4f}"
        ])
    print(f"Summary added to {summary_csv_path}")



def load_scores_csv(path: str) -> Dict[str, Dict[Tuple[str, str, str], int]]:
    scores: Dict[str, Dict[Tuple[str, str, str], int]] = {}
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            ex = row["exercise_name"].strip()
            p  = row["parent"].strip()
            l  = row["leaf"].strip()
            v  = int(row["score"])
            o  = row["ontology"].strip()
            scores.setdefault(ex, {})[(p, l, o)] = v
    return scores



if __name__ == "__main__":

    # DON'T FORGET TO SET CONFIGURATIONS IN s10x_settings.py


    BIN_FILE = "data/exercise_bins/all_exercise_snippet_with_prob_description.csv"



    THRESHOLDS = [5, 4, 3]
    # batch_data = [
    #     "combined_stats_window_5_code_with_problems",
    #     "combined_stats_window_10_code_with_problems",
    #     "combined_stats_no_window_code_with_problems",
    # ]
    # CLAWS_OUTPUT_PATHS = [
    #     "output/window_5/code_with_problems/output/",
    #     "output/window_10/code_with_problems/output/",
    #     "output/no_window/code_with_problems/output/",
    # ]



    # batch_data = load_batch_split_ids()
    batch_data = load_batch_ids()



    for idx, batch_id in enumerate(batch_data):
        # CLAWS_OUTPUT_PATH = CLAWS_OUTPUT_PATHS[idx]
        SCORES_CSV_FILE = Path(CLAWS_OUTPUT_PATH) / f"scores/{batch_id}.csv"

        allowed_exercises = ()
        # allowed_exercises = get_allowed_exercises_for_batch(BIN_FILE, batch_id)
        # print(f"[INFO] Bin '{batch_id}': {len(allowed_exercises)} exercises")

        scores_all = load_scores_csv(str(SCORES_CSV_FILE))

        for THRESHOLD in THRESHOLDS:
            print(f"[INFO] Running final metrics for batch '{batch_id}' with threshold {THRESHOLD}...")
            run_final_metrics(
                batch_id=batch_id,
                scores=scores_all,
                gold_csv_path=GOLD_FILE,
                gold_view="parser",
                # gold_view="educational",
                threshold=THRESHOLD,
                allowed_exercises=allowed_exercises,
                CLAWS_OUTPUT_PATH=CLAWS_OUTPUT_PATH,
                PROMPT_SESSION_ID=PROMPT_SESSION_ID,
            )
