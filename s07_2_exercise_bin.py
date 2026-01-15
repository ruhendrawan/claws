import csv
from pathlib import Path
from statistics import median

from s10x_settings import *



MARKER = "#CODE_SNIPPET"

def split_code_exercises(input_file: str):
    text = Path(input_file).read_text(encoding="utf-8")
    parts = [p.strip() for p in text.split(MARKER) if p.strip()]
    return parts

def parse_exercise_name(snippet: str) -> str | None:
    for line in snippet.splitlines():
        s = line.strip()
        if s.lower().startswith("#exercise name:"):
            return s.split(":", 1)[1].strip()
    return None

def count_comment_lines(snippet: str, comment_prefix: str = "#") -> int:
    return sum(1 for line in snippet.splitlines() if line.strip().startswith(comment_prefix))

def write_list(path: Path, items: list[str]):
    path.write_text("\n".join(items) + ("\n" if items else ""), encoding="utf-8")



def process_exercises_to_indexes(
    input_file: str,
    out_file: str,
    length_lines_threshold: int | None = None,
    comment_threshold: int | None = None,
    length_chars_threshold: int | None = None,
    comment_prefix: str = "#",
):
    snippets = split_code_exercises(input_file)

    records = []
    for idx, snippet in enumerate(snippets, start=1):
        ex_id = parse_exercise_name(snippet) or f"ex_{idx:04d}"
        length_lines = snippet.count("\n") + 1 if snippet else 0
        comment_lines = count_comment_lines(snippet, comment_prefix=comment_prefix)
        length_chars = len(snippet)
        records.append({
            "index": idx,
            "exercise_name": ex_id,
            "length_lines": length_lines,
            "comment_lines": comment_lines,
            "length_chars": length_chars,
        })

    if not records:
        (out_file).write_text("exercise_name,index,length_lines,comment_lines,length_chars,length_lines_bin,comments_bin,chars_bin\n", encoding="utf-8")
        for name in ["length_short","length_long","comments_low","comments_high","chars_short","chars_long"]:
            write_list(out / f"{name}.txt", [])
        return {"out_dir": str(out.resolve()), "total": 0}

    # Thresholds default to medians
    if length_lines_threshold is None:
        length_lines_threshold = int(median(r["length_lines"] for r in records))
    if comment_threshold is None:
        comment_threshold = int(median(r["comment_lines"] for r in records))
    if length_chars_threshold is None:
        length_chars_threshold = int(median(r["length_chars"] for r in records))

    for r in records:
        if r["length_lines"] <= length_lines_threshold:
            r["length_lines_bin"] = "0"
        else:
            r["length_lines_bin"] = "1"

        if r["comment_lines"] <= comment_threshold:
            r["comments_bin"] = "0"
        else:
            r["comments_bin"] = "1"

        if r["length_chars"] <= length_chars_threshold:
            r["chars_bin"] = "0"
        else:
            r["chars_bin"] = "1"

    exercise_bin_path = Path(out_file)

    with exercise_bin_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "index",
                "exercise_name",
                "length_lines",
                "comment_lines",
                "length_chars",
                "length_lines_bin",
                "comments_bin",
                "chars_bin",
            ],
        )
        writer.writeheader()
        writer.writerows(records)

    return {
        "length_lines_threshold": length_lines_threshold,
        "comment_threshold": comment_threshold,
        "length_chars_threshold": length_chars_threshold,
        "total": len(records),
    }



if __name__ == "__main__":

    # DON'T FORGET TO SET THE PARAMETERS IN s10x_settings.py


    BIN_FILE = "data/exercise_bins/all_exercise_snippet_with_prob_description.csv"

    process_exercises_to_indexes(PROMPT_INPUT_SNIPPET, out_file=BIN_FILE)