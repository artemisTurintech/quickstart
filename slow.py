"""Deliberately slow utilities - an Artemis discovery quickstart target."""


def word_frequencies(text):
    words = []
    current = ""
    for ch in text:
        if ch == " ":
            if current != "":
                words.append(current.lower())
            current = ""
        else:
            current = current + ch
    if current != "":
        words.append(current.lower())
    result = {}
    for w in words:
        result[w] = words.count(w)
    return result


def find_duplicates(nums):
    dupes = []
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j and nums[i] == nums[j] and nums[i] not in dupes:
                dupes.append(nums[i])
    return sorted(dupes)


def primes_up_to(n):
    primes = []
    for x in range(2, n + 1):
        is_prime = True
        for d in range(2, x):
            if x % d == 0:
                is_prime = False
        if is_prime:
            primes.append(x)
    return primes


def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


def moving_average(xs, k):
    out = []
    for i in range(len(xs) - k + 1):
        window = []
        for j in range(i, i + k):
            window.append(xs[j])
        out.append(sum(window) / len(window))
    return out
