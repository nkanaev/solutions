class Solution:
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        buckets = [[] for _ in range(numRows)]
        d = 1
        i = 0
        for c in s:
            buckets[i].append(c)
            i += d
            if i == 0:
                d = 1
            elif i == numRows - 1:
                d = -1
        return ''.join(''.join(b) for b in buckets)



def test():
    convert = Solution().convert
    assert convert('PAYPALISHIRING', 3) == 'PAHNAPLSIIGYIR'
    assert convert('PAYPALISHIRING', 4) == 'PINALSIGYAHRPI'
