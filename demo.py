
from batch_client import BatchClient
from sequential_client import SequentialClient
from request import BatchRequest
import time

URLS = [
    f"http://localhost:8000/file_{i}.bin"
    for i in range(800)
]

batch_requests = [BatchRequest("GET", url) for url in URLS]

# Асинхронный
async_client = BatchClient(max_concurrency=50)
start = time.perf_counter()
async_client.execute(batch_requests)
print("Async:", time.perf_counter() - start)

# Последовательный
seq_client = SequentialClient()
start = time.perf_counter()
seq_client.execute(batch_requests)
print("Sequential:", time.perf_counter() - start)
