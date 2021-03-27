# Codejam 2021, Qualification Round: Cheating Detection

import numpy as np


def find_cheater(x):
    Pq = x.mean(0)
    correct = np.array([Pq[x[i]].mean() for i in range(100)])
    wrong = np.array([Pq[~x[i]].mean() for i in range(100)])
    return np.argmin(correct - wrong) + 1


# I/O Code
num_cases = int(input())
_ = input()

for case in range(1, num_cases + 1):
    x = np.array([list(map(int, input().strip())) for _ in range(100)])
    cheater = find_cheater(x.astype(bool))
    print("Case #{}: {}".format(case, cheater))
