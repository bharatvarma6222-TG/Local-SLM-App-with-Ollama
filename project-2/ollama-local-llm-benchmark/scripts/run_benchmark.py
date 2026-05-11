import json
import csv
import os
from app.benchmarking.latency import measure_latency

models = ["phi3", "mistral"]
results_file = "evals/results.csv"

with open("evals/prompts.json", "r", encoding="utf-8") as f:
    prompts = json.load(f)

# Create CSV file with header if it doesn't exist or is empty
file_exists = os.path.exists(results_file)
file_empty = (not file_exists) or os.path.getsize(results_file) == 0

with open(results_file, "a", newline="", encoding="utf-8") as csvfile:
    writer = csv.DictWriter(
        csvfile,
        fieldnames=["model", "prompt", "latency",
                    "response_length", "response_preview", "status"]
    )

    if file_empty:
        writer.writeheader()

    for model in models:
        print(f"\n===== Testing model: {model} =====", flush=True)

        for i, prompt in enumerate(prompts, start=1):
            try:
                print(
                    f"[START] {model} | Prompt {i}/{len(prompts)}: {prompt}", flush=True)

                latency, response = measure_latency(model, prompt)

                row = {
                    "model": model,
                    "prompt": prompt,
                    "latency": round(latency, 2),
                    "response_length": len(response),
                    "response_preview": response[:120].replace("\n", " "),
                    "status": "OK"
                }

                writer.writerow(row)
                csvfile.flush()

                print(
                    f"[OK] {model} | Prompt {i}/{len(prompts)} | {latency:.2f}s", flush=True)

            except Exception as e:
                row = {
                    "model": model,
                    "prompt": prompt,
                    "latency": "",
                    "response_length": "",
                    "response_preview": str(e).replace("\n", " "),
                    "status": "FAILED"
                }

                writer.writerow(row)
                csvfile.flush()

                print(
                    f"[FAILED] {model} | Prompt {i}/{len(prompts)} | {e}", flush=True)

print("\nBenchmark completed. Results saved to evals/results.csv", flush=True)
