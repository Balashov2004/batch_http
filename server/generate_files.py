
import os
import random

os.makedirs("files", exist_ok=True)

sizes = [10_000_00, 100_000, 1_000_000, 5_000_000_0]

for i in range(800):
    size = random.choice(sizes)
    with open(f"files/file_{i}.bin", "wb") as f:
        f.write(os.urandom(size))