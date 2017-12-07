def cycles(nums):
    prev = set()
    im = nums.index(max(nums))
    c = 0
    while True:
        if tuple(nums) in prev:
            return c
        prev.add(tuple(nums))
        n = nums[im]
        nums[im] = 0
        for i in range(im + 1, im + n + 1):
            nums[i % len(nums)] += 1
        c += 1
        im = nums.index(max(nums))


def test():
    assert cycles([0, 2, 7, 0]) == 5


if __name__ == '__main__':
    import sys
    print(cycles(list(map(int, sys.stdin.readline().split()))))
