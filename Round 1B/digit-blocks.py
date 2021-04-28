# Codejam 2021, Round 1B: Digit Blocks

import numpy as np


def get_strategy(N, B):
    """
    a = No. of towers with height B
    b = No. of towers with height B - 1
    c = No. of towers with height B - 2
    h = Height of growing tower (at position a + b + c)

    Strategies:
    0 = Add block to growing tower
    1 = Add block to tower of height B - 1
    2 = Add block to tower of height B - 2
    """
    DP = np.zeros((N+1, N+1, N+1, B - 2))
    STRATEGY = np.zeros((N+1, N+1, N+1, B - 2, 10), dtype=int)

    for a in reversed(range(N)):
        for b in reversed(range(N - a + 1)):
            for c in reversed(range(N - a - b + 1)):
                max_h = 0 if a + b + c == N else B - 3

                for h in reversed(range(max_h + 1)):
                    for d in range(10):
                        score = np.array([-np.inf, -np.inf, -np.inf])

                        if a + b + c < N:
                            score[0] = (DP[a, b, c+1, 0] if h == B - 3
                                        else DP[a, b, c, h+1]) + d*10**h

                        if b:
                            score[1] = DP[a+1, b-1, c, h] + d*10**(B-1)

                        if c:
                            score[2] = DP[a, b+1, c-1, h] + d*10**(B-2)

                        i = np.argmax(score)
                        STRATEGY[a, b, c, h, d] = i
                        DP[a, b, c, h] += score[i] / 10

    return STRATEGY


def solve(N, B):
    a, b, c, h = 0, 0, 0, 0

    for _ in range(N * B):
        d = int(input())
        s = STRATEGY[a, b, c, h, d]

        if s == 1:
            i = a
            a += 1
            b -= 1

        elif s == 2:
            i = a + b
            b += 1
            c -= 1

        else:
            i = a + b + c
            h += 1
            if h == B - 2:
                c += 1
                h = 0

        print(i + 1, flush=True)


# I/O Code
T, N, B, P = map(int, input().split())
STRATEGY = get_strategy(N, B)

for _ in range(1, T + 1):
    solve(N, B)
