# Codejam 2021, Round 1C: Double or NOTing

import itertools


def solve(S, E):
    if S == E:
        return 0

    E = E.lstrip('0')

    add = 0
    if S == '0':
        S, add = '1', 1

    result, X = [], 0
    while True:
        if E.startswith(S):
            suffix = E[len(S):]
            Z = len(list(itertools.groupby(suffix.rstrip('0'))))

            if Z <= X:
                result.append(X + len(suffix) + add)

        if S:
            S = S.translate(str.maketrans('01', '10')).lstrip('0')
            X += 1
        else:
            break

    return min(result, default=None)


# I/O Code
num_cases = int(input())

for case in range(1, num_cases + 1):
    S, E = input().split()
    y = solve(S, E)
    print('Case #{}: {}'.format(case, "IMPOSSIBLE" if y is None else y))
