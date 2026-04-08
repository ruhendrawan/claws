import json
import os
from pathlib import Path



# SNIPPET_TYPE = "code_only"
# PROMPT_INPUT_SNIPPET = "all_exercise_snippet.py"


SNIPPET_TYPE = "code_with_problems"
PROMPT_INPUT_SNIPPET = "data/all_exercise_snippet_with_prob_description.py"



# PROMPT_SESSION_ID = "window_5"
# PROMPT_WINDOW_SIZE = 5

# PROMPT_SESSION_ID = "window_10"
# PROMPT_WINDOW_SIZE = 10

# PROMPT_SESSION_ID = "window_25"
# PROMPT_WINDOW_SIZE = 25

# PROMPT_SESSION_ID = "window_50"
# PROMPT_WINDOW_SIZE = 50

PROMPT_SESSION_ID = "no_window"
PROMPT_WINDOW_SIZE = -1



# SNIPPET_TYPE = "data/parsons_with_problems"
# PROMPT_INPUT_SNIPPET = "data/parsons_with_prob_description.py"

#
# PROMPT_SESSION_ID = "parsons_window_10"
# PROMPT_WINDOW_SIZE = 10

# PROMPT_SESSION_ID = "parsons_window_5"
# PROMPT_WINDOW_SIZE = 5



PROMPT_OUTPUT_PATH = f"output/{PROMPT_SESSION_ID}/{SNIPPET_TYPE}/prompts"
CLAWS_OUTPUT_PATH = f"output/{PROMPT_SESSION_ID}/{SNIPPET_TYPE}/output"





LEAVES_PYTHON_FILE = "ontology/hierarchy_python_leaves.csv"
LEAVES_EDUCATION_FILE = "ontology/hierarchy_educational_python_leaves.csv"

GOLD_FILE = "data/FINAL_exercise_annotation.csv"



BATCH_FILE = Path(PROMPT_OUTPUT_PATH) / "class_bulk_batch.jsonl"

def load_batch_ids(batch_file = BATCH_FILE):
    batch_data = []
    if not os.path.exists(batch_file):
        print(f"Batch file not found: {batch_file}")
        exit(1)
    with open(batch_file, "r", encoding="utf-8") as f:
        for line in f:
            try:
                batch_json = json.loads(line)
            except json.JSONDecodeError as e:
                print(f"JSON decode error: {e} in line: {line}")
                continue
            batch_id = batch_json.get("id")
            if not batch_id:
                print(f"Batch ID not found in line: {line}")
                continue
            batch_data.append(batch_id)
    return batch_data

def load_batch_split_ids():
    batch_splits = [
        f"splits_{PROMPT_SESSION_ID}_{SNIPPET_TYPE}/chars_bin=0",
        f"splits_{PROMPT_SESSION_ID}_{SNIPPET_TYPE}/chars_bin=1",
        f"splits_{PROMPT_SESSION_ID}_{SNIPPET_TYPE}/comments_bin=0",
        f"splits_{PROMPT_SESSION_ID}_{SNIPPET_TYPE}/comments_bin=1",
        f"splits_{PROMPT_SESSION_ID}_{SNIPPET_TYPE}/length_lines_bin=0",
        f"splits_{PROMPT_SESSION_ID}_{SNIPPET_TYPE}/length_lines_bin=1"
    ]
    return batch_splits


SESSION_TAG = f"{PROMPT_SESSION_ID}_{SNIPPET_TYPE}"
COMBINED_STATS_ID = f"combined_stats_{SESSION_TAG}"
