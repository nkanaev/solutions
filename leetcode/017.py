class Solution(object):
    LETTERS = {
        '1': '*',
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }
    def letterCombinations(self, digits):
        if not digits:
            return []
        combinations = list(self.LETTERS[digits[0]])
        for i in xrange(1, len(digits)):
            newc = []
            for l in self.LETTERS[digits[i]]:
                newc.extend([c + l for c in combinations])
            print newc
            combinations = newc
        return sorted(combinations)

