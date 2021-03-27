# Codejam 2021, Qualification Round: Moons and Umbrellas

from math import inf


def solve(X, Y, S):
    costs = [[0, X], [Y, 0]]
    dp = [[inf, inf] for _ in range(len(S))]

    for i in range(len(S)):
        for j in range(2):
            if (j == 0 and S[i] == "J") or (j == 1 and S[i] == "C"):
                continue

            if i == 0:
                dp[i][j] = 0
            else:
                dp[i][j] = min(dp[i-1][0] + costs[0][j],
                               dp[i-1][1] + costs[1][j])

    return min(dp[-1])


# I/O Code
num_cases = int(input())

for case in range(1, num_cases + 1):
    X, Y, S = input().split()
    res = solve(int(X), int(Y), S)
    print('Case #{}: {}'.format(case, res))
