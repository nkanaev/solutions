class Solution(object):
    def generateParenthesis(self, n):
        r = self.parens(n, 0, 0)
        print r
        return r

    def parens(self, max_num, open_num, closed_num):
        if open_num == max_num:
            return [')' * (open_num - closed_num)]
        result = []
        for r in self.parens(max_num, open_num + 1, closed_num):
            result.append('(' + r)
        if closed_num < open_num:
            for r in self.parens(max_num, open_num, closed_num + 1):
                result.append(')' + r)
        return result


def test():
    s = Solution()
    assert s.generateParenthesis(3) == [
        "((()))",
        "(()())",
        "(())()",
        "()(())",
        "()()()"
    ]
    assert s.generateParenthesis(2) == [
        "(())",
        "()()"
    ]


if __name__ == '__main__':
    test()
