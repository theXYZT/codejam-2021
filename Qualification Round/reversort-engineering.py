# Codejam 2021, Qualification Round: Reversort Engineering


def unreversort(N, C):
    C -= N - 1

    if C < 0 or N * (N - 1) // 2 < C:
        return None

    L = list(range(1, N + 1))

    for i in range(N - 2, -1, -1):
        if C >= N - i - 1:
            L[i:] = reversed(L[i:])
            C -= N - i - 1
        else:
            j = C + i + 1
            L[i:j] = reversed(L[i:j])
            break

    return L


# I/O Code
num_cases = int(input())

for case in range(1, num_cases + 1):
    N, C = map(int, input().split())
    L = unreversort(N, C)
    result = "IMPOSSIBLE" if L is None else " ".join(map(str, L))
    print('Case #{}: {}'.format(case, result))
