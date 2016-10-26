class Solution(object):
    def maxSubArray(self, nums):
        if not nums:
            return
        m = sm = nums[0]
        for i in xrange(1, len(nums)):
            sm = max(sm + nums[i], nums[i])
            m = max(m, sm)
        return m
