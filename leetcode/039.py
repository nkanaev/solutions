class Solution(object):
    def combinationSum(self, candidates, target):
        return self.combine(0, candidates, target)

    def combine(self, start_i, candidates, target):
        if target <= 0:
            return []
        result = []
        for i in xrange(start_i, len(candidates)):
            if candidates[i] == target:
                result.append([candidates[i]])
            for sub in self.combine(i, candidates, target - candidates[i]):
                result.append([candidates[i]] + sub)
        return result
