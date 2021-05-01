# Codejam 2021, Round 1C: Closest Pick

import itertools


def solve(N, K, P):
    intervals = [y - x - 1 for x, y in zip(P, P[1:]) if y > x + 1]
    winning = max(intervals, default=0)

    single = [(n + 1) // 2 for n in intervals] + [P[0] - 1, K - P[-1]]

    for a, b in itertools.combinations(single, 2):
        winning = max(winning, a + b)

    return winning / K


# I/O Code
num_cases = int(input())

for case in range(1, num_cases + 1):
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    y = solve(N, K, sorted(P))
    print('Case #{}: {:.8f}'.format(case, y))
