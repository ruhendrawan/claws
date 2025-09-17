import csv
import ast
import sys
from typing import Any, Dict, Set, Tuple, List





def _err(msg: str) -> None:
    print(f"[ERROR] {msg}", file=sys.stderr)
def _warn(msg: str) -> None:
    print(f"[WARN]  {msg}", file=sys.stderr)



def _parse_list_naive(raw: str) -> Set[str]:
    if raw is None:
        return set()
    s = raw.strip()
    if len(s) >= 2 and (s[0] == s[-1] == '"' or s[0] == s[-1] == "'"):
        s = s[1:-1].strip()
    if s.startswith("[") and s.endswith("]"):
        s = s[1:-1].strip()
    if not s:
        return set()
    parts = [p.strip() for p in s.split(",")]
    return {p for p in parts if p}


def read_gold_lists(path: str) -> Dict[str, Dict[str, Set[str]]]:
    gold: Dict[str, Dict[str, Set[str]]] = {}
    with open(path, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            ex = (row.get("exercise_name") or "").strip()
            if not ex:
                continue

            # def _as_set(field_name: str) -> Set[str]:
            #     raw = row.get(field_name, "")
            #     try:
            #         lst = ast.literal_eval(raw)
            #         # coerce to strings and strip whitespace
            #         return {str(x).strip() for x in lst if str(x).strip()}
            #     except Exception:
            #         _warn(f"Gold parse failed for {ex}::{field_name}: {raw!r}. Using empty set.")
            #         return set()
            # edu_set = _as_set("educational_list")
            # parser_set = _as_set("parser_list")

            edu_set   = _parse_list_naive(row.get("educational_list", ""))
            parser_set = _parse_list_naive(row.get("parser_list", ""))
            gold[ex] = {"educational": edu_set, "parser": parser_set}
    return gold


def scores_to_predicted_leaves(
    scores: Dict[str, Dict[Tuple[str, str], int]],
    threshold: int = 1
) -> Dict[str, Set[str]]:
    pred: Dict[str, Set[str]] = {}
    for ex, pair_scores in scores.items():
        present = {leaf for (_parent, leaf), s in pair_scores.items() if isinstance(s, (int, float)) and s >= threshold}
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

    exercises = sorted(set(pred_leaves.keys()) | set(gold_sets.keys()))
    rows: List[Dict[str, Any]] = []

    total_tp = total_fp = total_fn = 0
    exact_sum = 0.0

    for ex in exercises:
        pred = pred_leaves.get(ex, set())
        gold = gold_sets.get(ex, set())

        tp = len(pred & gold)
        fp = len(pred - gold)
        fn = len(gold - pred)

        p, r, f = _prf(tp, fp, fn)
        exact = 1.0 if pred == gold else 0.0

        rows.append({
            "exercise_name": ex,
            "pred_count": len(pred),
            "gold_count": len(gold),
            "tp": tp, "fp": fp, "fn": fn,
            "precision": p, "recall": r, "f1": f,
            "accuracy_exact": exact,
        })

        total_tp += tp
        total_fp += fp
        total_fn += fn
        exact_sum += exact

    # macro: mean of per-exercise metrics
    n = len(rows) or 1
    macro = {
        "precision": sum(r["precision"] for r in rows) / n,
        "recall":    sum(r["recall"]    for r in rows) / n,
        "f1":        sum(r["f1"]        for r in rows) / n,
        "accuracy_exact": exact_sum / n,
    }

    # micro: pooled counts
    micro_p, micro_r, micro_f = _prf(total_tp, total_fp, total_fn)
    micro = {"precision": micro_p, "recall": micro_r, "f1": micro_f}

    return rows, micro, macro



def run_final_metrics(
    scores: Dict[str, Dict[Tuple[str, str], int]],
    gold_csv_path: str,
    gold_view: str = "parser",   # choose "parser" or "educational"
    threshold: int = 1,          # score >= threshold ⇒ predicted leaf present
    print_per_exercise: bool = True
) -> None:

    gold_all = read_gold_lists(gold_csv_path)
    gold_sets: Dict[str, Set[str]] = {ex: v.get(gold_view, set()) for ex, v in gold_all.items()}

    pred_sets = scores_to_predicted_leaves(scores, threshold=threshold)

    per, micro, macro = evaluate_against_gold_sets(pred_sets, gold_sets)

    # Pretty print
    if print_per_exercise:
        print("exercise_name,pred_count,gold_count,tp,fp,fn,precision,recall,f1,accuracy_exact")
        for r in per:
            print("{exercise_name},{pred_count},{gold_count},{tp},{fp},{fn},{precision:.4f},{recall:.4f},{f1:.4f},{accuracy_exact:.4f}".format(**r))

    print("\n# Macro averages (mean over exercises)")
    print("precision={:.4f}, recall={:.4f}, f1={:.4f}, exact_accuracy={:.4f}".format(
        macro["precision"], macro["recall"], macro["f1"], macro["accuracy_exact"]
    ))

    print("# Micro (pooled)")
    print("precision={:.4f}, recall={:.4f}, f1={:.4f}".format(
        micro["precision"], micro["recall"], micro["f1"]
    ))



def load_scores_csv(path: str) -> Dict[str, Dict[Tuple[str, str], int]]:
    scores: Dict[str, Dict[Tuple[str, str], int]] = {}
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            ex = row["exercise_name"].strip()
            p = row["parent"].strip()
            l = row["leaf"].strip()
            v = int(row["score"])
            scores.setdefault(ex, {})[(p, l)] = v
    return scores





if __name__ == "__main__":

    GOLD_FILE = "data/FINAL_exercise_annotation.csv"
    # LLM_OUTPUT_DIR = "output/window_5/data/code_with_problems/output/"
    LLM_OUTPUT_DIR = "output/window_10/data/code_with_problems/output/"
    # LLM_OUTPUT_DIR = "output/parsons_window_5/data/parsons_with_problems/output/"
    SCORES_CSV_FILE = LLM_OUTPUT_DIR + "scores.csv"


    scores = load_scores_csv(SCORES_CSV_FILE)
    print(f"Loaded scores for {len(scores)} exercises from {SCORES_CSV_FILE}")

    run_final_metrics(
        scores=scores,
        gold_csv_path=GOLD_FILE,
        gold_view="parser",   # or "educational"
        threshold=4,          # score >= threshold means the leaf is predicted present
        print_per_exercise=True
    )
