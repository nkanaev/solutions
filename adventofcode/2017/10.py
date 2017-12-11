def result(ls, nums):
    l = list(range(ls))
    skip = 0
    idx = 0
    for n in nums:
        for i in range(n // 2):
            s = (idx + i) % ls
            e = (idx + n - i - 1) % ls
            l[s], l[e] = l[e], l[s]
        idx = (idx + skip + n) % ls
        skip += 1
    return l[0] * l[1]


def test():
    assert result(5, [3, 4, 1, 5]) == 12


if __name__ == '__main__':
    import sys
    nums = list(map(int, sys.stdin.readline().split(',')))
    print(result(256, nums))
