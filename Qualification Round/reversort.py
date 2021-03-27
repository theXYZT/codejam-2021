# Codejam 2021, Qualification Round: Reversort

def reversort_cost(N, L):
    cost = 0
    for i in range(N - 1):
        j = L.index(i + 1) + 1
        L[i:j] = reversed(L[i:j])
        cost += (j - i)
    return cost


# I/O Code
num_cases = int(input())

for case in range(1, num_cases + 1):
    N = int(input().strip())
    L = list(map(int, input().split()))
    cost = reversort_cost(N, L)
    print('Case #{}: {}'.format(case, cost))
