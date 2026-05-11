import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("evals/summary.csv")

plt.figure(figsize=(8, 5))
plt.bar(df["model"], df["avg_latency"])
plt.title("Average Latency by Model")
plt.xlabel("Model")
plt.ylabel("Latency (seconds)")
plt.tight_layout()
plt.savefig("evals/avg_latency_chart.png")
print("Saved chart to evals/avg_latency_chart.png")
plt.show()
