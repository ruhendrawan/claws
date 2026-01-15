from statistics import mean, stdev
from pathlib import Path
import sys
import asyncio
from collections import defaultdict, Counter
from typing import Dict, Tuple, List
import csv

from s10x_settings import *



def _err(msg: str) -> None:
    print(f"[ERROR] {msg}", file=sys.stderr)
def _warn(msg: str) -> None:
    print(f"[WARN]  {msg}", file=sys.stderr)
def ensure_parent_dir(path: Path) -> None:
    os.makedirs(path.parent, exist_ok=True)



def _mode_with_tiebreak(values: List[int]) -> int:
    c = Counter(values)
    max_freq = max(c.values())
    candidates = [v for v, f in c.items() if f == max_freq]
    return max(candidates)



def combine_batch_scores_to_stats(
    batch_ids: List[str],
    scores_dir: Path,
) -> Dict[Tuple[str, str, str], Dict[List[int], str]]:
    agg: Dict[Tuple[str, str, str], Dict[List[int], str]] = defaultdict(list)

    for bid in batch_ids:
        fpath = scores_dir / f"{bid}.csv"
        if not os.path.exists(fpath):
            _warn(f"Missing batch scores file: {fpath}")
            continue
        with open(fpath, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                ex = row["exercise_name"].strip()
                p  = row["parent"].strip()
                l  = row["leaf"].strip()
                try:
                    v  = int(row["score"])
                    o = row.get("ontology", "").strip()
                except Exception:
                    _warn(f"Non-integer score in {fpath}: {row.get('score')!r} for {(ex,p,l)}. Skipping.")
                    continue
                agg[(ex, p, l)].append((v, o))
    return agg

def write_combined_stats_and_mode(
    agg: Dict[Tuple[str, str, str], Dict[List[int], str]],
    out_stats_path: Path
) -> None:
    ensure_parent_dir(out_stats_path)
    with open(out_stats_path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow([
            "exercise_name","parent","leaf","ontology","n","min","max","mode","mean","stddev","score"
        ])
        for (ex, p, l), d in agg.items():
            o = d[0][1] if d else ""
            vals = [v for v, o in d]
            n = len(vals)
            mn = min(vals)
            mx = max(vals)
            md = _mode_with_tiebreak(vals)
            mu = mean(vals)
            sd = stdev(vals) if n >= 2 else 0.0  # sample stddev; fallback 0 for n==1
            w.writerow([ex, p, l, o, n, mn, mx, md, f"{mu:.6f}", f"{sd:.6f}", md])





# ---- Combine all batch CSVs into one (stats + majority vote)
if __name__ == "__main__":

    # DON'T FORGET TO SET THE PARAMETERS IN s10x_settings.py


    scores_dir = Path(CLAWS_OUTPUT_PATH) / "scores"
    agg = combine_batch_scores_to_stats(
        batch_ids=load_batch_ids(),
        scores_dir=scores_dir,
    )

    out_stats = scores_dir / f"{COMBINED_STATS_ID}.csv"

    write_combined_stats_and_mode(
        agg=agg,
        out_stats_path=out_stats
    )

    print(f"Combined stats saved to {out_stats}")
