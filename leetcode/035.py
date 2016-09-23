class Solution(object):
    def searchInsert(self, nums, target):
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) / 2
            if nums[m] < target:
                l = m + 1
            else:
                r = m
        print l
        if nums[l] == target or nums[l] > target:
            return l
        else:
            return l + 1


def test():
    s = Solution()
    assert s.searchInsert([1, 3, 5, 6], 5) == 2
    assert s.searchInsert([1, 3, 5, 6], 2) == 1
    assert s.searchInsert([1, 3, 5, 6], 7) == 4
    assert s.searchInsert([1, 3, 5, 6], 0) == 0


if __name__ == '__main__':
    test()
