import os
from anyio import Path
from openai import OpenAI
from dotenv import load_dotenv

from s10x_settings import PROMPT_OUTPUT_PATH, BATCH_FILE
load_dotenv()

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def upload_jsonl(openai_client, file_path):
    return openai_client.files.create(file=open(file_path, "rb"), purpose="batch")

def create_batch(openai_client, input_file_id):
    return openai_client.batches.create(
        input_file_id=input_file_id,
        endpoint="/v1/chat/completions",
        completion_window="24h"
    )



if __name__ == "__main__":

    # DON'T FORGET TO SET CONFIGURATIONS IN s10x_settings.py


    file_obj = upload_jsonl(
        client,
        Path(PROMPT_OUTPUT_PATH) / "class_bulk.jsonl"
    )
    print(f"File uploaded: {file_obj.id}, status: {file_obj.status}")
    print(f"To check status: https://platform.openai.com/files/{file_obj.id}")


    # To repeat the run, you can use an existing uploaded file ID
    # window_5 and code_with_problems
    # file_obj = type('', (), {'id': "file-Uw2YyBUTL3gR7SJ6CPBdnF"})()
    # window_10 and code_with_problems
    # file_obj = type('', (), {'id': "file-7HjvnGm4uZ2cGc4XEmHbTf"})()


    # Run in multiple batches and aggregate the results later
    for _ in range(5):
        batch = create_batch(client, file_obj.id)

        print(f"Batch created: {batch.id}, status: {batch.status}")
        print(f"To check status: https://platform.openai.com/batches/{batch.id}")

        with open(BATCH_FILE, "a", encoding="utf-8") as f:
            f.write(batch.model_dump_json() + "\n")

    print(f"Batch info appended to: {BATCH_FILE}")