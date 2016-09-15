import operator
import string


class Solution(object):
    OPERATORS = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
    }

    def diffWaysToCompute(self, input):
        tokens = []
        i = 0
        while i < len(input):
            if input[i] in '+-*':
                tokens.append(input[i])
                i += 1
            else:
                s_i = i
                while input[i] in string.digits:
                    i += 1
                    if i == len(input):
                        break
                tokens.append(int(input[s_i:i]))

        if len(tokens) == 1:
            return tokens

        if tokens[0] == '-':
            tokens = [0] + tokens
        result = self.variations(tokens, 0, len(tokens)-1, {})
        return sorted(result)

    def variations(self, tokens, s, e, cache):
        if s == e:
            return [tokens[s]]
        if (s, e,) in cache:
            return cache[(s, e,)]

        result = []
        for i in range(s + 1, e + 1, 2):
            f = self.OPERATORS[tokens[i]]
            l_nums = self.variations(tokens, s, i - 1, cache)
            r_nums = self.variations(tokens, i + 1, e, cache)
            for l in l_nums:
                for r in r_nums:
                    result.append(f(l, r))

        cache[(s, e,)] = result
        return result


def test():
    s = Solution()
    assert s.diffWaysToCompute('10+5') == [15]
    assert s.diffWaysToCompute('2-1-1') == [0, 2]
    assert s.diffWaysToCompute('2*3-4*5') == [-34, -14, -10, -10, 10]
    assert s.diffWaysToCompute('11') == [11]


if __name__ == '__main__':
    test()
