# Codejam 2021, Round 1B: Broken Clock

import itertools

MAX_TICKS = 3600*12*10**9
HOUR = MAX_TICKS // 12
MIN = HOUR // 60
SEC = MIN // 60


def hms_to_time(h, m, s, n):
    return h*HOUR + m*MIN + s*SEC + n


def time_to_hms(n):
    h, n = n // HOUR, n % HOUR
    m, n = n // MIN, n % MIN
    s, n = n // SEC, n % SEC
    return h, m, s, n % SEC


def solve(A, B, C):
    for H, M, S in itertools.permutations([A, B, C], 3):
        for h in range(12):
            X = h * HOUR + M - H
            if X % 11 == 0:
                T = (h * HOUR + (X // 11)) % MAX_TICKS
                M_valid = (M == (11*T + H) % MAX_TICKS)
                S_valid = (S == (719*T + H) % MAX_TICKS)

                if M_valid and S_valid:
                    return time_to_hms(T)


# I/O Code
num_cases = int(input())

for case in range(1, num_cases + 1):
    A, B, C = list(map(int, input().split()))
    h, m, s, n = solve(A, B, C)
    print('Case #{}: {} {} {} {}'.format(case, h, m, s, n))
