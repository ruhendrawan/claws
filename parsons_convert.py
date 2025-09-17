import json
import sys
from pathlib import Path


def convert_to_snippet(name: str, item: dict) -> str:
    exercise_type = "ps"
    description = item.get("instructions") # + "; " + item.get("description", "")
    code = item.get("initial", "")

    snippet = []
    snippet.append("#CODE_SNIPPET")
    snippet.append(f"#exercise type: {exercise_type.lower()}")
    snippet.append(f"#exercise name: {name}")
    snippet.append(f"#problem description: {description.strip()}")
    snippet.append(code.strip())  # actual code
    return "\n".join(snippet)



def main(input_file: str, output_file: str = None):
    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    results = []
    for name, item in data.items():
        snippet = convert_to_snippet(name, item)
        results.append(snippet)

    output_text = "\n\n\n\n".join(results)

    if output_file:
        Path(output_file).write_text(output_text, encoding="utf-8")
        print(f"- Snippets written to {output_file}")
    else:
        print(output_text)


if __name__ == "__main__":
    input_file = "data/python-basics.txt"
    output_file = "data/parsons_with_prob_description.py"
    main(input_file, output_file)
