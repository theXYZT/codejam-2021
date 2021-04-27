# Codejam 2021, Round 1B: Subtransmutation

from collections import Counter
import math


def valid(H, D, A, B):
    N = H & D
    H -= N
    D -= N

    if not D:
        return True
    elif not H:
        return False

    i = max(H)
    c = H.pop(i)

    for j in (i - A, i - B):
        if j > 0:
            H[j] += c

    return valid(H, D, A, B)


def solve(N, A, B, D):
    g = math.gcd(A, B)
    k = N % g
    if any(m % g != k for m in D):
        return None

    M = N + g
    while True:
        if valid(Counter([M]), +D, A, B):
            return M
        M += g


# I/O Code
num_cases = int(input())

for case in range(1, num_cases + 1):
    N, A, B = list(map(int, input().split()))
    D = +Counter(dict(enumerate(map(int, input().split()), 1)))
    y = solve(N, A, B, D)
    print('Case #{}: {}'.format(case, "IMPOSSIBLE" if y is None else y))
