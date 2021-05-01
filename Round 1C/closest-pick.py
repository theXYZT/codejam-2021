# Codejam 2021, Round 1C: Closest Pick

import itertools


def solve(N, K, P):
    P = sorted(set(P))
    intervals = [y - x - 1 for x, y in zip(P, P[1:])]
    winning = max(intervals, default=0)

    single = [P[0] - 1, K - P[-1]]
    for n in intervals:
        single.append((n + 1) // 2)

    for a, b in itertools.combinations(single, 2):
        if a + b > winning:
            winning = a + b

    return winning / K


# I/O Code
num_cases = int(input())

for case in range(1, num_cases + 1):
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    y = solve(N, K, P)
    print('Case #{}: {:.8f}'.format(case, y))
