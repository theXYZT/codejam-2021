# Codejam 2021, Round 1C: Roaring Years

import math


def roaring_number(N, k):
    return int("".join(map(str, range(N, N+k))))


def bisection(func, low, high):
    if func(low) > 0:
        return low

    if high == low + 1:
        return high

    mid = (low + high) // 2

    if func(mid) > 0:
        return bisection(func, low, mid)
    else:
        return bisection(func, mid, high)


def solve(Y):
    result = math.inf
    max_k = max(2, len(str(Y)) + 1)

    for k in range(2, max_k + 1):
        n = bisection(lambda a: roaring_number(a, k) - Y, 1, 10**9)
        X = roaring_number(n, k)

        if Y < X < result:
            result = X

    return result


# I/O Code
num_cases = int(input())

for case in range(1, num_cases + 1):
    Y = int(input())
    z = solve(Y)
    print('Case #{}: {}'.format(case, z))
