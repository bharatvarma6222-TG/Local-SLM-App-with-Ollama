## Benchmark Findings

This project compared local CPU-only inference performance of Phi-3 and Mistral using Ollama on consumer Windows hardware.

### Summary Results

| Model | Avg Latency | Min Latency | Max Latency | Avg Response Length |
|---|---:|---:|---:|---:|
| mistral | 156.05 s | 9.37 s | 237.96 s | 1418.6 |
| phi3 | 74.61 s | 3.72 s | 153.50 s | 900.0 |

### Key Insights

- Phi-3 achieved substantially lower average latency than Mistral.
- Mistral generally produced longer responses, which may indicate more detailed outputs at the cost of speed.
- Very short prompts were handled much faster than long-form explanatory prompts.
- CPU-only local deployment is strong for privacy and zero API cost, but introduces major latency tradeoffs on mid-range hardware.