# Codejam 2021, Round 1B: Digit Blocks

import sys


def solve(N, B):
    def get_block():
        D = int(input())
        if D < 0:
            sys.exit()
        return D

    def send_tower(i):
        print(i+1, flush=True)
        TOWERS[i] += 1

    def best_tower(D):
        for i, T in enumerate(TOWERS):
            if (D == 9) and (T == B - 1):
                return i

        for i, T in enumerate(TOWERS):
            if (D >= 7) and (T == B - 2):
                return i

        for i, T in enumerate(TOWERS):
            if T < B - 2:
                return i

        for i, T in enumerate(TOWERS):
            if T < B:
                return i

    TOWERS = [0] * N

    for _ in range(N * B):
        D = get_block()
        i = best_tower(D)
        # print(i, D, TOWERS, file=sys.stderr)
        send_tower(i)


# I/O Code
T, N, B, P = map(int, input().split())

for _ in range(1, T + 1):
    _ = solve(N, B)

_ = input()
sys.exit()
