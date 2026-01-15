# ## Code Snippets

# Extract every code snippet. Store the snippets in a list. In the next phase, feed each snippet to the LLM to pull out its knowledge components (KCs).


def split_code_exercises(input_file):
  with open(input_file, 'r') as f:
    code_exercises = f.read()
  code_snippets = code_exercises.split('#CODE_SNIPPET')
  for idx, snippet in enumerate(code_snippets):
    snippet = snippet.strip()
  code_snippets = [s.strip() for s in code_snippets if s.strip()]
  return code_snippets

def test_split_code_exercises():
  # input_file = "data/all_exercise_snippet.py"
  input_file = "data/all_exercise_snippet_with_prob_description.py"
  code_snippets = split_code_exercises(input_file)
  print(len(code_snippets))
  print(code_snippets[0])



# ## Batch Generation Classification with Window Sliding (CLAWS)

from glob import glob
import os
from pathlib import Path
import shutil
import csv
import json

from s10x_settings import *

### Generate Prompt from Templates


def get_code_exercises(input_file):
  snippets = split_code_exercises(input_file)
  return snippets



def chunk_list(lst, chunk_size):
  if chunk_size <= 0:
    return [lst]
  return [lst[i:i+chunk_size] for i in range(0, len(lst), chunk_size)]


def get_ontology_classes(window_size):
  print(f"Window Size = {window_size}")

  t = open("ontology/hierarchy_python_leaves.csv", "r").readlines()
  t = t[1:]
  print(f"Python Classes = {len(t)}")
  python_csv_lines = chunk_list(t, window_size)
  print(f"Educational Chunks Num. of Windows = {len(python_csv_lines)}")

  t = open("ontology/hierarchy_educational_python_leaves.csv", "r").readlines()
  t = t[1:]
  print(f"Educational Python Classes = {len(t)}")
  educational_python_csv_lines = chunk_list(t, window_size)
  print(f"Educational Python Num. of Windows = {len(educational_python_csv_lines)}")

  csv_lines = python_csv_lines + educational_python_csv_lines

  return csv_lines



PROMPT_TEMPLATE = """
You are an annotation assistant.
Given a code snippet, evaluate all rows in the ontology classes CSV.
Provide a reason for how the class is being used in the snippet/ problem, evaluate, and give a usage score.

## Output
Respond as long as possible.
Score is between 0-5.
Return as a CSV (exercise_name,parent,leaf,reason,score).

## INPUT: Ontology Classes
```csv(parent,leaf,description)
{ontology}
```

## INPUT: Code Snippet
```code
{snippet}
```
"""



def generate_prompts(snippet_file, window_size, output_dir):
    shutil.rmtree(output_dir, ignore_errors=True)
    os.makedirs(output_dir, exist_ok=True)
    snippets = split_code_exercises(snippet_file)
    print(f"Total code snippets: {len(snippets)}")
    class_windows = get_ontology_classes(window_size)
    print(f"Total class windows: {len(class_windows)}")
    print(f"Generating prompts in {output_dir} ...")
    for code_idx, snippet in enumerate(snippets, start=1):
        for class_idx, csv_data in enumerate(class_windows, start=1):
            ontology = "\n".join([line.strip() for line in csv_data])
            prompt = PROMPT_TEMPLATE.format(ontology=ontology, snippet=snippet)

            # print(prompt)
            # break

            fname = f"{class_idx:03d}-{code_idx:03d}.txt"
            with open(Path(output_dir) / fname, "w", encoding="utf-8") as f:
                f.write(prompt)
    print(f"Generated {len(snippets)} code snippets x {len(class_windows)} ontology batches")
    print(f"Output path: {output_dir}")



### Prepare Batch Completions (OpenAI)


def create_jsonl_from_prompts(prompt_dir, jsonl_out):
    entries = []
    for prompt_file in sorted(glob(prompt_dir + "/*.txt")):
        class_idx, code_idx = prompt_file.split("-")
        with open(prompt_file, "r", encoding="utf-8") as f:
            prompt = f.read()
        entries.append({
            "custom_id": f"{class_idx}-{code_idx}",
            "method": "POST",
            "url": "/v1/chat/completions",
            "body": {
                "model": "gpt-4.1-mini",
                "messages": [
                    {"role": "system", "content": prompt}
                ],
                "max_tokens": 32768,
                "temperature": 0,
                "top_p": 0.1,
                "store": True
            }
        })
    with open(jsonl_out, "w", encoding="utf-8") as f:
        for item in entries:
            f.write(json.dumps(item) + "\n")
    print(f"JSONL file created: {jsonl_out}")


def preview_file(filename, num_chars=100):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            lines_count = len(content.split('\n'))
            print(f"File '{filename}' has {lines_count} lines.")
            print(content[:num_chars])
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")






if __name__ == "__main__":

    # DON'T FORGET TO SET CONFIGURATIONS IN s10x_settings.py


    # test_split_code_exercises()

    print(f"Settings: {PROMPT_SESSION_ID}, {SNIPPET_TYPE}, Window Size={PROMPT_WINDOW_SIZE}")
    print(f"Output Paths: {PROMPT_OUTPUT_PATH}, {CLAWS_OUTPUT_PATH}")
    print()

    # exit() # Dry run config

    generate_prompts(
        PROMPT_INPUT_SNIPPET,
        PROMPT_WINDOW_SIZE,
        PROMPT_OUTPUT_PATH
    )
    print()

    create_jsonl_from_prompts(
      PROMPT_OUTPUT_PATH,
      Path(PROMPT_OUTPUT_PATH) / "class_bulk.jsonl"
    )
    print()

    preview_file(Path(PROMPT_OUTPUT_PATH) / "class_bulk.jsonl")
