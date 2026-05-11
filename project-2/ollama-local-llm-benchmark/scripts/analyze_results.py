import pandas as pd

df = pd.read_csv("evals/results.csv", encoding="utf-8")

df["latency"] = pd.to_numeric(df["latency"], errors="coerce")
df["response_length"] = pd.to_numeric(df["response_length"], errors="coerce")

if "status" in df.columns:
    df = df[df["status"] == "OK"].copy()

df = df.dropna(subset=["model", "prompt", "latency", "response_length"])

summary = df.groupby("model", as_index=False).agg(
    avg_latency=("latency", "mean"),
    min_latency=("latency", "min"),
    max_latency=("latency", "max"),
    avg_response_length=("response_length", "mean")
)

summary = summary.round({
    "avg_latency": 2,
    "min_latency": 2,
    "max_latency": 2,
    "avg_response_length": 2
})

print("\n=== Clean Summary ===")
print(summary)

summary.to_csv("evals/summary.csv", index=False, encoding="utf-8")
print("\nSaved summary to evals/summary.csv")
