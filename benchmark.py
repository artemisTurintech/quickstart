"""Benchmark slow.py and write artemis_results.json (lower is better for every metric)."""
import json
import os
import random
import statistics
import time

import slow

REPEATS = 3
OUT = "artemis_results.json"

rng = random.Random(42)
TEXT = " ".join(rng.choice(["alpha", "beta", "gamma", "delta", "eps", "zeta"]) for _ in range(5000))
NUMS = [rng.randint(0, 2000) for _ in range(1500)]
XS = [rng.random() for _ in range(20000)]

CASES = {
    "word_frequencies_ms": lambda: slow.word_frequencies(TEXT),
    "find_duplicates_ms": lambda: slow.find_duplicates(NUMS),
    "primes_up_to_ms": lambda: slow.primes_up_to(5000),
    "fib_ms": lambda: slow.fib(27),
    "moving_average_ms": lambda: slow.moving_average(XS, 50),
}


def median_ms(fn):
    fn()  # warm-up
    times = []
    for _ in range(REPEATS):
        t0 = time.perf_counter()
        fn()
        times.append((time.perf_counter() - t0) * 1000)
    return statistics.median(times)


def main():
    if os.path.exists(OUT):
        os.remove(OUT)
    results = {name: round(median_ms(fn), 3) for name, fn in CASES.items()}
    results["total_ms"] = round(sum(results.values()), 3)
    for k, v in results.items():
        print(f"{k:22s} {v:10.3f}")
    tmp = OUT + ".tmp"
    with open(tmp, "w") as f:
        json.dump(results, f)
    os.replace(tmp, OUT)


if __name__ == "__main__":
    main()
