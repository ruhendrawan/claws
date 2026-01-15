import csv
import json
import os
from anyio import Path
from openai import OpenAI
from openai.types import Batch, BatchRequestCounts
from dotenv import load_dotenv

from s10x_settings import CLAWS_OUTPUT_PATH, load_batch_ids
load_dotenv()

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))


def view_batch(openai_client, batch_id):
    return openai_client.batches.retrieve(batch_id)
def cancel_batch(openai_client, batch_id):
    return openai_client.batches.cancel(batch_id)

def download_batch_result(openai_client, output_file_id, output_path):
    content = openai_client.files.content(output_file_id)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content.text)
    print(f"Downloaded to: {output_path}")



def combine_results_to_csv(jsonl_file, csv_out):
    rows = []
    with open(jsonl_file, "r", encoding="utf-8") as f:
        count = 0
        for line in f:
            count += 1
            data = json.loads(line)
            custom_id = data.get("custom_id")
            content = data.get("response", {}).get("body", {}).get("choices", [{}])[0].get("message", {}).get("content", "")
            try:
                for row in csv.reader(content.splitlines()):
                    if row and row[0] != "exercise_name":
                        rows.append(row)
            except csv.Error as e:
                print(f"CSV parsing error in entry {count}: {e}")
                continue
    with open(csv_out, "w", encoding="utf-8", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["exercise_name", "parent", "leaf_class", "reason", "score"])
        writer.writerows(rows)
    print(f"Combined CSV saved to: {csv_out}")





if __name__ == "__main__":

    # DON'T FORGET TO SET CONFIGURATIONS IN s10x_settings.py


    os.makedirs(CLAWS_OUTPUT_PATH, exist_ok=True)
    os.makedirs(Path(CLAWS_OUTPUT_PATH) / "batch_openai", exist_ok=True)
    os.makedirs(Path(CLAWS_OUTPUT_PATH) / "result", exist_ok=True)


    # Manually set the batch ID from the uploaded batch
    # batch_data = batch_openai[SNIPPET_TYPE][PROMPT_SESSION_ID]:

    batch_data = load_batch_ids()
    for batch_id in batch_data:
        print()
        print(f"Processing batch ID: {batch_id}")

        batch_view = view_batch(client, batch_id)
        print(batch_view)

        OUTPUT_FILE = Path(CLAWS_OUTPUT_PATH) / f"batch_openai/{batch_id}_output.jsonl"
        if os.path.exists(OUTPUT_FILE):
            print(f"- File exists {OUTPUT_FILE}, skipping download.")
            continue

        if batch_view.status == "completed":
            download_batch_result(
                client,
                batch_view.output_file_id,
                OUTPUT_FILE
            )
            combine_results_to_csv(
                OUTPUT_FILE,
                Path(CLAWS_OUTPUT_PATH) / f"result/{batch_id}.csv"
            )
