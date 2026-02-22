
import time
from concurrent.futures import ThreadPoolExecutor

import matplotlib.pyplot as plt

from batch_client import BatchClient
from fast_http_v2 import worker
from request import BatchRequest
from sequential_client import SequentialClient
from bay.fast_http_demo import run

URLS = [
    # f"http://localhost:8000/file_{i}.bin"
    f"https://chatgpt.alexbers.com/small/{i}.txt"
    for i in range(1, 1001)
]

batch_requests = [BatchRequest("GET", url) for url in URLS]

def run_async():
    async_client = BatchClient(max_concurrency=500)
    start = time.perf_counter()
    async_client.execute(batch_requests)
    return time.perf_counter() - start

def run_sequential():
    seq_client = SequentialClient()
    start = time.perf_counter()
    seq_client.execute(batch_requests)
    return time.perf_counter() - start

def run_socket():
    return run()

TOTAL_REQUESTS = 1000
CONNECTIONS = 10
def run_multy_socket():
    start = time.perf_counter()

    chunk = TOTAL_REQUESTS // CONNECTIONS

    with ThreadPoolExecutor(max_workers=CONNECTIONS) as executor:
        futures = []

        for i in range(CONNECTIONS):
            start_i = i * chunk + 1
            end_i = (i + 1) * chunk if i != CONNECTIONS - 1 else TOTAL_REQUESTS

            futures.append(executor.submit(worker, start_i, end_i))

        for f in futures:
            f.result()

    end = time.perf_counter()
    return end - start


async_time = run_async()
seq_time = run_sequential()
socket_time = run_socket()
multy_socket_time = run_multy_socket()

print(f"Async time: {async_time:.4f} sec")
print(f"Sequential time: {seq_time:.4f} sec")
print(f"Multy_socket: {multy_socket_time:.4f} sec")
print(f"One_Socket time: {socket_time:.4f} sec")

implementations = ["Sequential","Async", "Socket", "Multi-socket"]
times = [seq_time, async_time, socket_time, multy_socket_time]

plt.figure()
bars = plt.bar(implementations, times)

plt.xlabel("Implementation")
plt.ylabel("Execution Time (seconds)")
plt.title("Performance Comparison of HTTP Client Implementations")

for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.3f} s",
        ha='center',
        va='bottom'
    )

plt.show()