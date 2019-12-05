import itertools


def meets_criteria(n):
    n = str(n)
    adj = False
    for i in range(len(n) - 1):
        if n[i] > n[i + 1]:
            return False
        if n[i] == n[i + 1]:
            adj = True
    return adj


def meets_criteria_2(n):
    if not meets_criteria(n):
        return False
    return 2 in {len(list(g)) for k, g in itertools.groupby(str(n))}


def main():
    a, b = 265275, 781584
    print(sum(1 for i in range(a, b + 1) if meets_criteria(i)))
    print(sum(1 for i in range(a, b + 1) if meets_criteria_2(i)))


main()
