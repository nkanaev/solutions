def steps(jumps):
    i = 0
    n = 0
    while 0 <= i < len(jumps):
        jumps[i], i = jumps[i] + 1, jumps[i] + i
        n += 1
    return n


def test():
    assert steps([0, 3, 0, 1, -3]) == 5


if __name__ == '__main__':
    import sys
    print(steps(list(map(int, sys.stdin.readlines()))))
