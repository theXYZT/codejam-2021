# Codejam 2021, Round 1A: Append Sort

def append_sort(N, L):
    cost = 0

    for i in range(1, N):
        if L[i-1] >= L[i]:
            a, b = L[i-1], L[i]

            n = 0
            while a >= b + (10**n - 1):
                n += 1
                b *= 10

            L[i] = max(b, a+1)
            cost += n

    return cost


# I/O Code
num_cases = int(input())

for case in range(1, num_cases + 1):
    N = int(input().strip())
    L = list(map(int, input().split()))
    cost = append_sort(N, L)
    print('Case #{}: {}'.format(case, cost))
