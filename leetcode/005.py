class Solution(object):
    def longestPalindrome(self, s):
        p = s[0]
        for i in xrange(0, len(s)-1):
            j = 1
            while i + j < len(s) and i - j >= 0:
                if s[i - j] != s[i + j]:
                    break
                j += 1
            c = s[i-j+1:i+j]
            if len(c) >= len(p):
                p = c

            j = 0
            while i + 1 + j < len(s) and i - j >= 0:
                if s[i-j] != s[i+1+j]:
                    break
                j += 1
            if j != 0:
                c = s[i-j+1:i+1+j]
                if len(c) >= len(p):
                    p = c
        return p



def test():
    s = Solution()
    assert s.longestPalindrome('abrakadabra') == 'ada'
    assert s.longestPalindrome('babba') == 'abba'
    assert s.longestPalindrome('abbab') == 'abba'
    assert s.longestPalindrome('akaaabaaa') == 'aaabaaa'
    assert s.longestPalindrome('aaabaaaka') == 'aaabaaa'
    assert s.longestPalindrome('s') == 's'


if __name__ == '__main__':
    test()
