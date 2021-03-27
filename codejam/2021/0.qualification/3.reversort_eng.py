import itertools


def cost(in_list):
    int_list = in_list.copy()
    length = len(int_list)
    cost = 0
    idx = 0
    while idx < length - 1:
        j_elem = min(int_list[idx:])
        j_pos = int_list.index(j_elem, idx) + 1
        int_list[idx:j_pos] = int_list[idx:j_pos][::-1]
        idx += 1
        cost += j_pos + 1 - idx
    return cost


def inner_main(i, N, C):
    """
    I qualified for CodeJam round 1 by passing test case 1 here and TLE on test 2.
    Not too bothered to speed it up right now, so I will leave as is.
    Can remove everything before the else statement and and will also TLE on test case 2.
    """
    if C > ((N - 1) * (N + 2) / 2) or C < (N - 1):
        # lets find a pattern in the max amounts to rule out and throw into wolfgram
        # > 0, 2, 5, 9, 14, 20
        print(f"Case #{i+1}: IMPOSSIBLE")
    elif C == (N - 1) * 2:
        # in order backwards
        test_l = [*range(N, 0, -1)]

        # TODO:: all occurences of the join can be done quicker
        test_str = [str(x) for x in test_l]
        test_str = " ".join(test_str)
        print(f"Case #{i+1}: {test_str}")
    elif C == (N - 1):
        # in order forwards
        test_l = [*range(1, N + 1, 1)]
        test_str = [str(x) for x in test_l]
        test_str = " ".join(test_str)
        print(f"Case #{i+1}: {test_str}")
    else:
        # Dirty brute force
        test_l = list(range(1, N + 1, 1))
        ans = None
        perms = itertools.permutations(test_l)
        for tup in perms:
            if cost(list(tup)) == C:
                ans = list(tup)
        if ans is None:
            print(f"Case #{i+1}: IMPOSSIBLE")
        else:
            test_str = [str(x) for x in ans]
            test_str = " ".join(test_str)
            print(f"Case #{i+1}: {test_str}")


def main1():
    T = int(input())
    for i in range(T):
        # size of the wanted list, desired cost
        N, C = input().split(" ")
        inner_main(i, int(N), int(C))


main1()
