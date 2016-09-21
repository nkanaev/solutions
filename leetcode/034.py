import math


class Solution(object):
    def searchRange(self, nums, target):
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) / 2
            if nums[m] >= target:
                r = m
            else:
                l = m + 1
        if nums[l] != target:
            return [-1, -1]
        start = l
        l, r = 0, len(nums) - 1
        while l < r:
            m = int(math.ceil((float(l) + r) / 2))
            if nums[m] <= target:
                l = m
            else:
                r = m - 1
        end = l
        return [start, end]
