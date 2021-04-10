# Codejam 2021, Round 1A: Hacked Exam


def solve(N, Q, exams):
    res, s = exams.pop()
    while exams:
        x = exams.pop()
        if x.score > s:
            res, s = x

    return res, s, 1


# I/O Code
num_cases = int(input())

for case in range(1, num_cases + 1):
    N, Q = map(int, input().split())

    exams = []
    for _ in range(N):
        answers, score = input().split()
        score = int(score)
        exams.append((answers, score))

    res, n, d = solve(N, Q, exams)
    print("Case #{}: {} {}/{}".format(case, res, n, d))
