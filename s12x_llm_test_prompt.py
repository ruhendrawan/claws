from anyio import Path
import os
from openai import OpenAI
from dotenv import load_dotenv

from s10x_settings import PROMPT_OUTPUT_PATH
load_dotenv()

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def execute_prompt(prompt_file):
  with open(prompt_file, "r") as f:
    PROMPT = f.read()

  # print(PROMPT)
  # exit()

  response = client.responses.create(
    model="gpt-4.1-mini",
    input=[
      {
        "role": "system",
        "content": [
          {
            "type": "input_text",
            "text": PROMPT
          }
        ]
      }
    ],
    text={
      "format": {
        "type": "text"
      }
    },
    reasoning={},
    tools=[],
    temperature=0,
    max_output_tokens=32768,
    top_p=0.1,
    store=True
  )
  return response


def test_execute_prompt():
  response = execute_prompt(Path(PROMPT_OUTPUT_PATH) / "001-001.txt")
  content = response.output_text
  print(content)


if __name__ == "__main__":
  test_execute_prompt()