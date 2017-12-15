import functools
import operator


def result(nums, ls=256):
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


def khash(string):
    l = list(range(256))
    nums = list(map(ord, string))
    nums.extend([17, 31, 73, 47, 23])
    skip = 0
    idx = 0
    for _ in range(64):
        for n in nums:
            for i in range(n // 2):
                s = (idx + i) % 256
                e = (idx + n - i - 1) % 256
                l[s], l[e] = l[e], l[s]
            idx = (idx + skip + n) % 256
            skip += 1
    result = []
    for i in range(0, 256, 16):
        result.append(functools.reduce(operator.xor, l[i:i + 16]))
    return ''.join(['%02x' % n for n in result])


def test_1():
    assert result([3, 4, 1, 5], 5) == 12


def test_2():
    assert khash('') == 'a2582a3a0e66e6e86e3812dcb672a272'
    assert khash('AoC 2017') == '33efeb34ea91902bb2f59c9920caa6cd'
    assert khash('1,2,3') == '3efbe78a8d82f29979031a4aa0b16a9d'
    assert khash('1,2,4') == '63960835bcdc130f0b66d7ff4f6a5a8e'


if __name__ == '__main__':
    with open('10.txt') as f:
        string = f.readline()
        nums = list(map(int, string.split(',')))
    print(result(nums))
    print(khash(string))
