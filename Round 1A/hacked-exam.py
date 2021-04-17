# Codejam 2021, Round 1A: Hacked Exam

from scipy.special import comb
import math


def flip(q):
    return q.translate(str.maketrans('FT', 'TF'))


def num_sequences(q, t):
    n = 1
    for s in q:
        n *= comb(q[s], t[s], exact=True)
    return n


def solve(answers, scores):
    q = {'TTT': 0, 'TTF': 0, 'TFT': 0, 'FTT': 0}

    for a, b, c in zip(*answers):
        s = a + b + c
        if s in q:
            q[s] += 1
        else:
            q[flip(s)] += 1

    S = [scores[0] - q['FTT'], scores[1] - q['TFT'], scores[2] - q['TTF']]

    total = 0
    n = {'TTT': 0, 'TTF': 0, 'TFT': 0, 'FTT': 0}
    for t1 in range(q['TTT'] + 1):
        t = {'TTT': t1,
             'TTF': (S[0] + S[1] - 2*t1) // 2,
             'TFT': (S[0] + S[2] - 2*t1) // 2,
             'FTT': (S[1] + S[2] - 2*t1) // 2}

        num_seq = num_sequences(q, t)
        total += num_seq
        for s in n:
            n[s] += num_seq * t[s]

    numerator = sum(max(n[s], total*q[s] - n[s]) for s in q)
    g = math.gcd(numerator, total)

    res = ""
    for a, b, c in zip(*answers):
        s = a + b + c

        if s in q:
            res += 'T' if 2*n[s] > total*q[s] else 'F'
        else:
            res += 'F' if 2*n[flip(s)] > total*q[flip(s)] else 'T'

    return res, numerator // g, total // g


# I/O Code
num_cases = int(input())

for case in range(1, num_cases + 1):
    N, Q = map(int, input().split())

    answers, scores = [], []
    for _ in range(N):
        answer, score = input().split()
        answers.append(answer)
        scores.append(int(score))

    while len(scores) < 3:
        answers.append(answers[-1])
        scores.append(scores[-1])

    res, n, d = solve(answers, scores)
    print("Case #{}: {} {}/{}".format(case, res, n, d))
