from __future__ import annotations
from typing import Dict, List, Set
import csv
import sys

from s10x_settings import *



def _err(msg: str) -> None:
    print(f"[ERROR] {msg}", file=sys.stderr)
def _warn(msg: str) -> None:
    print(f"[WARN]  {msg}", file=sys.stderr)
def ensure_dir(p: Path) -> None:
    os.makedirs(p, exist_ok=True)

def read_csv_dicts(path: Path) -> List[Dict[str, str]]:
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def write_csv_dicts(path: Path, rows: List[Dict[str, str]], fieldnames: List[str]) -> None:
    ensure_dir(path.parent)
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)



def load_bins(bin_csv: Path) -> Dict[str, Dict[str, Set[str]]]:
    rows = read_csv_dicts(bin_csv)
    if not rows:
        return {}

    cols = rows[0].keys()
    if "exercise_id" in cols:
        key_col = "exercise_id"
    elif "exercise_name" in cols:
        key_col = "exercise_name"
    else:
        raise ValueError("Bin CSV must contain 'exercise_id' or 'exercise_name' column.")

    bin_cols = [c for c in cols if c.endswith("_bin")]
    if not bin_cols:
        raise ValueError("No *_bin columns found in bin CSV (e.g., 'length_lines_bin', 'comments_bin', 'chars_bin').")

    bins: Dict[str, Dict[str, Set[str]]] = {}
    for c in bin_cols:
        bins[c] = {}

    for r in rows:
        ex_id = r[key_col].strip()
        if not ex_id:
            continue
        for c in bin_cols:
            val = (r.get(c) or "").strip()
            if not val:
                continue
            bins[c].setdefault(val, set()).add(ex_id)

    return bins


def index_combined_by_exname(combined_csv: Path) -> (List[Dict[str, str]], Dict[str, List[int]]):
    rows = read_csv_dicts(combined_csv)
    if not rows:
        return [], {}

    if "exercise_name" not in rows[0]:
        raise ValueError("Combined CSV must contain 'exercise_name' column.")

    by_name: Dict[str, List[int]] = {}
    for i, r in enumerate(rows):
        name = (r.get("exercise_name") or "").strip()
        if not name:
            _warn(f"Row {i} missing exercise_name; skipping index for this row.")
            continue
        by_name.setdefault(name, []).append(i)

    return rows, by_name


def filter_rows_by_names(rows: List[Dict[str, str]], by_name: Dict[str, List[int]], names: Set[str]) -> List[Dict[str, str]]:
    out: List[Dict[str, str]] = []
    for n in names:
        idxs = by_name.get(n)
        if not idxs:
            _warn(f"exercise_name '{n}' present in bins but not found in combined stats.")
            continue
        for i in idxs:
            out.append(rows[i])
    return out


def split_combined_by_bins(
    combined_csv: Path,
    bin_csv: Path,
    out_dir: Path,
) -> None:
    ensure_dir(out_dir)

    bins = load_bins(bin_csv)
    rows, by_name = index_combined_by_exname(combined_csv)

    if not rows:
        _warn("Combined CSV has no rows; nothing to split.")
        return

    fieldnames = list(rows[0].keys())

    summary_lines: List[str] = []
    for bin_col, val2names in bins.items():
        for bin_val, name_set in val2names.items():
            subset = filter_rows_by_names(rows, by_name, name_set)
            out_path = out_dir / f"{bin_col}={bin_val}.csv"
            write_csv_dicts(out_path, subset, fieldnames)
            summary_lines.append(f"{bin_col}={bin_val}: {len(subset)} rows -> {out_path}")

    with open((out_dir / "SPLIT_SUMMARY.txt"), "w", encoding="utf-8") as f:
        f.write("Split results (by *_bin columns from bin CSV)\n"
        "=============================================\n"
        + "\n".join(summary_lines) + "\n")





if __name__ == "__main__":

    # DON'T FORGET TO SET CONFIGURATIONS IN s10x_settings.py


    BIN_CSV = Path("data/exercise_bins/all_exercise_snippet_with_prob_description.csv")

    scores_dir = Path(CLAWS_OUTPUT_PATH) / "scores"

    COMBINED_STATS_CSV = scores_dir / f"{COMBINED_STATS_ID}.csv"
    OUT_SPLIT_DIR = scores_dir / f"splits_{SESSION_TAG}"


    split_combined_by_bins(
        combined_csv=COMBINED_STATS_CSV,
        bin_csv=BIN_CSV,
        out_dir=OUT_SPLIT_DIR,
    )

    print(f"Based on snippets of type '{SNIPPET_TYPE}' and prompt window size {PROMPT_WINDOW_SIZE}.")
    print(f"Using combined stats from: {COMBINED_STATS_CSV}")
    print(f"Using bins from: {BIN_CSV}")
    print(f"Split CSVs written in: {OUT_SPLIT_DIR}")
    print(f"Log summary in: {OUT_SPLIT_DIR / 'SPLIT_SUMMARY.txt'}")
