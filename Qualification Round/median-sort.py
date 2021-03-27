# Codejam 2021, Qualification Round: Median Sort

import sys


def query(*x):
    print(*x, sep=" ", flush=True)
    response = input()
    if response == '-1':
        sys.exit()
    return int(response)


def split_list(L, pivots):
    left, middle, right = [], [], []

    while L:
        val = L.pop()
        median = query(val, *pivots)
        if median == val:
            middle.append(val)
        elif median == pivots[0]:
            left.append(val)
        else:
            right.append(val)

    return left, middle, right


def order_list(L, left=None, right=None):
    if len(L) < 2:
        return L

    pivots = (L.pop(), L.pop())
    if left is not None:
        median = query(left, *pivots)
        if median != pivots[0]:
            pivots = pivots[::-1]
    elif right is not None:
        median = query(right, *pivots)
        if median != pivots[1]:
            pivots = pivots[::-1]

    left, middle, right = split_list(L, pivots)

    new_left = order_list(left, right=pivots[0]) + [pivots[0]]
    new_middle = order_list(middle, left=pivots[0], right=pivots[1])
    new_right = [pivots[1]] + order_list(right, left=pivots[1])
    return new_left + new_middle + new_right


# I/O Code
T, N, Q = map(int, input().split())

for _ in range(1, T + 1):
    L = order_list(list(range(1, N + 1)))
    _ = query(*L)

sys.exit()
