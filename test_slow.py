"""Correctness gate: compares slow.py against simple reference implementations."""
import math
import random
import sys
from collections import Counter

import slow


def main():
    rng = random.Random(0)
    vocab = ["Alpha", "beta", "GAMMA", "delta", "eps"]

    text = "  ".join(" ".join(rng.choice(vocab) for _ in range(50)) for _ in range(4))
    assert slow.word_frequencies(text) == dict(Counter(w.lower() for w in text.split()))
    assert slow.word_frequencies("") == {}

    nums = [rng.randint(0, 100) for _ in range(300)]
    assert slow.find_duplicates(nums) == sorted(k for k, v in Counter(nums).items() if v > 1)
    assert slow.find_duplicates([1, 2, 3]) == []

    assert slow.primes_up_to(1) == []
    assert slow.primes_up_to(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    assert len(slow.primes_up_to(1000)) == 168

    assert [slow.fib(i) for i in range(10)] == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    assert slow.fib(25) == 75025

    xs = [rng.random() for _ in range(200)]
    got = slow.moving_average(xs, 7)
    want = [sum(xs[i:i + 7]) / 7 for i in range(len(xs) - 6)]
    assert len(got) == len(want)
    assert all(math.isclose(a, b, rel_tol=1e-9) for a, b in zip(got, want))

    print("all tests passed")


if __name__ == "__main__":
    try:
        main()
    except AssertionError:
        print("TEST FAILED", file=sys.stderr)
        raise
