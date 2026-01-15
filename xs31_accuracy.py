import csv
from pathlib import Path
import sys
from typing import Any, Dict, Set, Tuple, List

from s10x_settings import *



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
    scores: Dict[str, Dict[Tuple[str, str, str], int]],
    threshold: int = 1,
    gold_view: str = "parser",   # choose "parser" or "educational"
) -> Dict[str, Set[str]]:
    pred: Dict[str, Set[str]] = {}
    for ex, pair_scores in scores.items():
        present = {leaf for (_parent, leaf, _ontology), s in pair_scores.items() if isinstance(s, (int, float)) and s >= threshold and _ontology == gold_view}
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
    jacc_sum = 0.0

    for ex in exercises:
        pred = pred_leaves.get(ex, set())
        gold = gold_sets.get(ex, set())

        tp = len(pred & gold)
        fp = len(pred - gold)
        fn = len(gold - pred)

        p, r, f = _prf(tp, fp, fn)

        denom_union = (tp + fp + fn)
        if denom_union > 0:
            jacc = tp / denom_union
        else:
            # both sets empty → perfect agreement
            jacc = 1.0

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

    # macro: mean of per-exercise metrics
    n = len(rows) or 1
    macro = {
        "precision": sum(r["precision"] for r in rows) / n,
        "recall":    sum(r["recall"]    for r in rows) / n,
        "f1":        sum(r["f1"]        for r in rows) / n,
        "jaccard":   jacc_sum / n,
        "accuracy_exact": exact_sum / n,
    }

    # micro: pooled counts (jaccard_micro = TP / (TP+FP+FN))
    micro_p, micro_r, micro_f = _prf(total_tp, total_fp, total_fn)
    micro_j = (total_tp / (total_tp + total_fp + total_fn)) if (total_tp + total_fp + total_fn) else 1.0
    micro = {"precision": micro_p, "recall": micro_r, "f1": micro_f, "jaccard": micro_j}

    return rows, micro, macro



def ensure_parent_dir(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)

def run_final_metrics(
    batch_id: str,
    scores: Dict[str, Dict[Tuple[str, str], int]],
    gold_csv_path: str,
    gold_view: str = "parser",   # choose "parser" or "educational"
    threshold: int = 1           # score >= threshold ⇒ predicted leaf present
) -> None:

    gold_all = read_gold_lists(gold_csv_path)
    gold_sets: Dict[str, Set[str]] = {ex: v.get(gold_view, set()) for ex, v in gold_all.items()}

    pred_sets = scores_to_predicted_leaves(scores, threshold=threshold, gold_view=gold_view)

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

    # Macro averages (mean over exercises) + Micro (pooled)
    summary_csv_path = Path(CLAWS_OUTPUT_PATH) / f"scores/accuracy_summary_{PROMPT_SESSION_ID}.csv"
    ensure_parent_dir(summary_csv_path)
    summary_exists = summary_csv_path.exists()
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
    scores: Dict[str, Dict[Tuple[str, str], int]] = {}
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





if __name__ == "__main__":

    # DON'T FORGET TO SET THE PARAMETERS IN s10x_settings.py


    # score >= threshold means the leaf is predicted present
    THRESHOLD = 5
    # THRESHOLD = 4
    # THRESHOLD = 3


    batch_ids = load_batch_ids()
    batch_ids.append(COMBINED_STATS_ID)

    for batch_id in load_batch_ids():
        SCORES_CSV_FILE = Path(CLAWS_OUTPUT_PATH) / f"scores/{batch_id}.csv"

        scores = load_scores_csv(SCORES_CSV_FILE)
        print(f"Loaded scores for {len(scores)} exercises from {SCORES_CSV_FILE}")

        run_final_metrics(
            batch_id=batch_id,
            scores=scores,
            gold_csv_path=GOLD_FILE,
            gold_view="parser",   # or "educational"
            threshold=THRESHOLD
        )
