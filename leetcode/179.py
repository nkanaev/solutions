class Solution:
    def largestNumber(self, nums):
        nums = map(str, nums)
        nums = sorted(nums, cmp=lambda a, b: cmp(a+b, b+a), reverse=True)
        nums = ''.join(nums).lstrip('0')
        return nums or "0"
