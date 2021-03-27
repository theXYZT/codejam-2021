# Codejam 2021, Qualification Round: Moons and Umbrellas

def min_cost(X, Y, S):
    cost_dict = {'CJ': X, 'JC': Y, 'CC': 0, 'JJ': 0}

    cost = 0
    S = "".join(S.split("?"))
    for i in range(len(S) - 1):
        cost += cost_dict[S[i:i+2]]
    return cost


# I/O Code
num_cases = int(input())

for case in range(1, num_cases + 1):
    X, Y, S = input().split()
    res = min_cost(int(X), int(Y), S)
    print('Case #{}: {}'.format(case, res))
