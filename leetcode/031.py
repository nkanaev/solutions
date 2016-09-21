class Solution(object):
    def nextPermutation(self, nums):
        j = len(nums) - 2
        while True:
            if j < 0:
                return nums.sort()
            if nums[j] >= nums[j+1]:
                j -= 1
            else:
                break
        sub = sorted(nums[j+1:])
        for i in xrange(len(sub)):
            if nums[j] < sub[i]:
                nums[j], sub[i] = sub[i], nums[j]
                nums[j+1:] = sub
                return
