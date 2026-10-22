# Artemis Discovery Quickstart

A tiny Python project for showing Artemis discovery finding optimisations quickly, even with local LLMs.

`slow.py` has five short functions, each with a deliberate performance mistake:

| Function | Mistake |
|---|---|
| `word_frequencies` | string `+=` concatenation, `list.count` in a loop (O(n²)) |
| `find_duplicates` | nested loops plus `not in` on a list (O(n²)) |
| `primes_up_to` | trial division by every number, no √x bound, no early exit |
| `fib` | naive recursion, no memoisation |
| `moving_average` | rebuilds and sums every window from scratch |

## Files

- `slow.py` – the code to optimise
- `test_slow.py` – correctness gate (compares against reference implementations)
- `benchmark.py` – times each function and writes `artemis_results.json`

No dependencies beyond Python 3.

## Run locally

```bash
python -m py_compile slow.py   # compile
python test_slow.py            # test
python benchmark.py            # benchmark -> artemis_results.json
```

## Artemis validation script

| Phase | Command |
|---|---|
| setup | `python -m py_compile slow.py` |
| setup | `python test_slow.py` |
| benchmark | `python benchmark.py` |

Rank versions by **`total_ms`** (lower is better). Per-function metrics (`*_ms`) are also reported.
