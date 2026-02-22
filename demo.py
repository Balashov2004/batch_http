
from batch_client import BatchClient
from sequential_client import SequentialClient
from request import BatchRequest
import time

URLS = [
    # f"http://localhost:8000/file_{i}.bin"
    f"https://chatgpt.alexbers.com/small/{i}.txt"
    for i in range(1, 1001)
]

batch_requests = [BatchRequest("GET", url) for url in URLS]

# Асинхронный
async_client = BatchClient(max_concurrency=500)

start = time.perf_counter()
responses = async_client.execute(batch_requests)
end = time.perf_counter()

for response in responses:
    if response.error:
        print(f"ERROR: {response.error}")
    else:
        print(response.body)

print("Async:", end - start)

# Последовательный
seq_client = SequentialClient()
start = time.perf_counter()
seq_client.execute(batch_requests)
print("Sequential:", time.perf_counter() - start)
