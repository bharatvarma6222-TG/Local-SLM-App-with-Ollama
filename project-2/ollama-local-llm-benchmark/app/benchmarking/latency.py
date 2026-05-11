import time
from app.inference.ollama_client import query_model


def measure_latency(model, prompt):
    start = time.time()
    response = query_model(model, prompt)
    end = time.time()
    return end - start, response
