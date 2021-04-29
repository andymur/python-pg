#!/usr/bin/python3

def perm_step(accum, l, r):

    if len(r) <= 1:
        return

    if not accum:
        accum.append(l + r)

    for ind in range(len(r)):
        r_copy = list(r)
        r_copy[0], r_copy[ind] = r_copy[ind], r_copy[0]
        if ind > 0:
            accum.append(l + r_copy)
        perm_step(accum, l + [r_copy[0]], r_copy[1:])

# returns list with all possible permutations (as a lists) with n elements
# e.g. [[1,2], [2,1]] if n = 2
def perm(n):
    res = []
    init = list(range(1, n + 1))
    perm_step(res, [], init)
    return res

if __name__ == "__main__":
    n = 4
    print("permutations for n: {0}".format(n))
    res = perm(n)
    print(res)
    print(len(res))
