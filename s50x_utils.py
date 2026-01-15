import csv
from typing import Dict, Set


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
            edu_set    = _parse_list_naive(row.get("educational_list", ""))
            parser_set = _parse_list_naive(row.get("parser_list", ""))
            gold[ex] = {"educational": edu_set, "parser": parser_set}
    return gold