class Solution(object):
    def sortColors(self, nums):
        c = [0] * 3
        for i, n in enumerate(nums):
            c[n] += 1
            if n == 0:
                nums[c[0] - 1], nums[i] = nums[i], nums[c[0] - 1]
                if nums[i] == 1:
                    nums[c[0] + c[1] - 1], nums[i] = nums[i], nums[c[0] + c[1] - 1]
            if n == 1:
                nums[c[0] + c[1] - 1], nums[i] = nums[i], nums[c[0] + c[1] - 1]
