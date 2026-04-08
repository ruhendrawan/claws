import csv
import json
import os
import sys
import statistics
from collections import defaultdict
from typing import Dict, List, Tuple, Set

from pathlib import Path
from s10x_settings import (
    PROMPT_INPUT_SNIPPET,
    LEAVES_PYTHON_FILE,
    LEAVES_EDUCATION_FILE,
    load_batch_ids,
    # PROMPT_SESSION_ID,  # not used directly; we override per session
    # SNIPPET_TYPE,       # we set explicitly below
)

# -----------------------------
# Sessions & batches config
# -----------------------------
SESSION_IDS = [
    "window_5",
    "window_10",
    "no_window",
]
batch_records = dict()
SNIPPET_TYPE = "code_with_problems"
batch_records[SNIPPET_TYPE] = dict()
for sid in SESSION_IDS:
    PROMPT_SESSION_ID = sid
    PROMPT_OUTPUT_PATH = f"output/{PROMPT_SESSION_ID}/{SNIPPET_TYPE}/prompts"
    BATCH_FILE = Path(PROMPT_OUTPUT_PATH) / "class_bulk_batch.jsonl"
    batch_records[SNIPPET_TYPE][sid] = load_batch_ids(BATCH_FILE)

def _warn(msg: str) -> None:
    print(f"[WARN]  {msg}", file=sys.stderr)

def _info(msg: str) -> None:
    print(f"[INFO]  {msg}")

def safe_read_retry_csv(path: Path) -> List[Tuple[str, str, str]]:
    rows: List[Tuple[str, str, str]] = []
    if not os.path.exists(path):
        return rows
    with open(path, "r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        # Peek first row; skip header if present
        first = next(reader, None)
        if first is None:
            return rows
        header_like = (
            len(first) >= 3
            and str(first[0]).lower().strip() == "exercise_name"
            and str(first[1]).lower().strip() in {"parent", "ontology_parent", "p"}
            and str(first[2]).lower().strip() in {"leaf_class", "leaf", "l"}
        )
        if not header_like:
            # treat as data
            if len(first) >= 3:
                rows.append((first[0].strip(), first[1].strip(), first[2].strip()))
        # the rest
        for r in reader:
            if not r or len(r) < 3:
                continue
            rows.append((r[0].strip(), r[1].strip(), r[2].strip()))
    return rows

def write_csv(path: Path, fieldnames: List[str], rows: List[Dict]) -> None:
    os.makedirs(path.parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)



def count_from_retry_for_session(session_id: str, batches: List[str]) -> Dict[str, List[Dict]]:
    output_root = Path(f"output/{session_id}/{SNIPPET_TYPE}/output")
    retry_dir = output_root / "retry"
    out_dir = output_root / "non_compliance_from_retry"

    per_exercise_rows: List[Dict] = []
    per_batch_summary: List[Dict] = []

    for batch_id in sorted(set(batches)):
        py_file = retry_dir / f"python_{batch_id}.csv"
        ed_file = retry_dir / f"education_{batch_id}.csv"

        py_rows = safe_read_retry_csv(py_file)
        ed_rows = safe_read_retry_csv(ed_file)

        # Group by exercise
        ex_to_py_pairs: Dict[str, Set[Tuple[str, str]]] = defaultdict(set)
        ex_to_ed_pairs: Dict[str, Set[Tuple[str, str]]] = defaultdict(set)

        for ex, parent, leaf in py_rows:
            ex_to_py_pairs[ex].add((parent, leaf))
        for ex, parent, leaf in ed_rows:
            ex_to_ed_pairs[ex].add((parent, leaf))

        # Union of exercises appearing in either retry file
        exercises = sorted(set(ex_to_py_pairs.keys()) | set(ex_to_ed_pairs.keys()))
        if not exercises and (not py_rows and not ed_rows):
            _warn(f"[{session_id}] [{batch_id}] No retry rows found.")

        miss_py_counts = []
        miss_ed_counts = []
        miss_any_counts = []

        for ex in exercises:
            miss_py = ex_to_py_pairs.get(ex, set())
            miss_ed = ex_to_ed_pairs.get(ex, set())

            # "any" = unique by (parent, leaf) across both ontologies to avoid double counting overlaps
            miss_any = set(miss_py) | set(miss_ed)

            row = {
                "session": session_id,
                "batch_id": batch_id,
                "exercise_name": ex,
                "missing_python_count": len(miss_py),
                "missing_education_count": len(miss_ed),
                "missing_any_count": len(miss_any),
            }
            per_exercise_rows.append(row)

            miss_py_counts.append(len(miss_py))
            miss_ed_counts.append(len(miss_ed))
            miss_any_counts.append(len(miss_any))

        n = max(1, len(exercises))
        per_batch_summary.append({
            "session": session_id,
            "batch_id": batch_id,
            "num_exercises_considered": len(exercises),
            "missing_python_total": sum(miss_py_counts),
            "missing_education_total": sum(miss_ed_counts),
            "missing_any_total": sum(miss_any_counts),
            "avg_missing_python_per_exercise": round(sum(miss_py_counts) / n, 3),
            "avg_missing_education_per_exercise": round(sum(miss_ed_counts) / n, 3),
            "avg_missing_any_per_exercise": round(sum(miss_any_counts) / n, 3),
            "std_missing_python": round(statistics.pstdev(miss_py_counts), 3) if len(miss_py_counts) > 1 else 0.0,
            "std_missing_education": round(statistics.pstdev(miss_ed_counts), 3) if len(miss_ed_counts) > 1 else 0.0,
            "std_missing_any": round(statistics.pstdev(miss_any_counts), 3) if len(miss_any_counts) > 1 else 0.0,
        })

    py_row_counts = [r["missing_python_count"] for r in per_exercise_rows if r["session"] == session_id]
    ed_row_counts = [r["missing_education_count"] for r in per_exercise_rows if r["session"] == session_id]
    any_row_counts = [r["missing_any_count"] for r in per_exercise_rows if r["session"] == session_id]

    n_rows = max(1, len(py_row_counts))  # same length for ed/any lists by construction
    totals_py = sum(py_row_counts)
    totals_ed = sum(ed_row_counts)
    totals_any = sum(any_row_counts)

    avg_row_py = totals_py / n_rows
    avg_row_ed = totals_ed / n_rows
    avg_row_any = totals_any / n_rows

    std_row_py = statistics.pstdev(py_row_counts) if len(py_row_counts) > 1 else 0.0
    std_row_ed = statistics.pstdev(ed_row_counts) if len(ed_row_counts) > 1 else 0.0
    std_row_any = statistics.pstdev(any_row_counts) if len(any_row_counts) > 1 else 0.0

    bsum_rows = [b for b in per_batch_summary if b["session"] == session_id]

    py_totals = [b["missing_python_total"] for b in bsum_rows]
    ed_totals = [b["missing_education_total"] for b in bsum_rows]
    any_totals = [b["missing_any_total"] for b in bsum_rows]

    avg_batch_py = statistics.mean(py_totals) if py_totals else 0.0
    avg_batch_ed = statistics.mean(ed_totals) if ed_totals else 0.0
    avg_batch_any = statistics.mean(any_totals) if any_totals else 0.0

    std_batch_py = statistics.pstdev(py_totals) if len(py_totals) > 1 else 0.0
    std_batch_ed = statistics.pstdev(ed_totals) if len(ed_totals) > 1 else 0.0
    std_batch_any = statistics.pstdev(any_totals) if len(any_totals) > 1 else 0.0

    per_window_summary = [{
        "session": session_id,
        "num_batches": len(bsum_rows),
        "num_exercise_rows": len(py_row_counts),
        "missing_python_total": totals_py,
        "missing_education_total": totals_ed,
        "missing_any_total": totals_any,
        "avg_missing_python_per_row": round(avg_row_py, 3),
        "avg_missing_education_per_row": round(avg_row_ed, 3),
        "avg_missing_any_per_row": round(avg_row_any, 3),
        "std_missing_python_per_row": round(std_row_py, 3),
        "std_missing_education_per_row": round(std_row_ed, 3),
        "std_missing_any_per_row": round(std_row_any, 3),
        "avg_missing_python_per_batch": round(avg_batch_py, 3),
        "avg_missing_education_per_batch": round(avg_batch_ed, 3),
        "avg_missing_any_per_batch": round(avg_batch_any, 3),
        "std_missing_python_per_batch": round(std_batch_py, 3),
        "std_missing_education_per_batch": round(std_batch_ed, 3),
        "std_missing_any_per_batch": round(std_batch_any, 3),
    }]

    per_ex_csv = out_dir / "per_exercise_missing_from_retry.csv"
    per_batch_csv = out_dir / "per_batch_summary_from_retry.csv"
    per_window_csv = out_dir / "per_window_summary_from_retry.csv"

    write_csv(per_ex_csv, [
        "session", "batch_id", "exercise_name",
        "missing_python_count", "missing_education_count", "missing_any_count",
    ], per_exercise_rows)

    write_csv(per_batch_csv, [
        "session", "batch_id", "num_exercises_considered",
        "missing_python_total", "missing_education_total", "missing_any_total",
        "avg_missing_python_per_exercise", "avg_missing_education_per_exercise", "avg_missing_any_per_exercise",
        "std_missing_python", "std_missing_education", "std_missing_any",
    ], per_batch_summary)

    write_csv(per_window_csv, [
        "session", "num_batches", "num_exercise_rows",
        "missing_python_total", "missing_education_total", "missing_any_total",
        "avg_missing_python_per_row", "avg_missing_education_per_row", "avg_missing_any_per_row",
        "std_missing_python_per_row", "std_missing_education_per_row", "std_missing_any_per_row",
        "avg_missing_python_per_batch", "avg_missing_education_per_batch", "avg_missing_any_per_batch",
        "std_missing_python_per_batch", "std_missing_education_per_batch", "std_missing_any_per_batch",
    ], per_window_summary)

    _info(f"[{session_id}] Saved: {per_ex_csv}")
    _info(f"[{session_id}] Saved: {per_batch_csv}")
    _info(f"[{session_id}] Saved: {per_window_csv}")

    return {
        "per_exercise": per_exercise_rows,
        "per_batch_summary": per_batch_summary,
        "per_window_summary": per_window_summary,
    }

def main():
    for sid in SESSION_IDS:
        batches = batch_records.get(SNIPPET_TYPE, {}).get(sid, [])
        if not batches:
            _warn(f"[{sid}] No batch IDs found; skipping.")
            continue
        count_from_retry_for_session(sid, batches)

if __name__ == "__main__":
    main()
