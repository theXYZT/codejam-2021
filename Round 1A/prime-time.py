# Codejam 2021, Round 1A: Prime Time

from collections import Counter


def factor_sum(n, deck):
    s = 0
    for p in deck:
        for _ in range(deck[p]):
            if n % p:
                break
            n //= p
            s += p

        if n == 1:
            return s
    return None


def solve(deck):
    total = sum(k * deck[k] for k in deck)

    for i in range(total, max(2, total - 4000), -1):
        group_sum = factor_sum(i, deck)
        if group_sum and total == i + group_sum:
            return i

    return 0


# I/O Code
num_cases = int(input())

for case in range(1, num_cases + 1):
    M = int(input().strip())

    deck = Counter()
    for _ in range(M):
        P, N = map(int, input().split())
        deck[P] += N

    res = solve(deck)
    print('Case #{}: {}'.format(case, res))
