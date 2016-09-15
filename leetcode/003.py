class Solution(object):
    def lengthOfLongestSubstring(self, s):
        s_i = -1
        last_seen = {}
        m = 0
        for i in range(0, len(s)):
            if s[i] in last_seen:
                s_i = max(s_i, last_seen[s[i]])
            last_seen[s[i]] = i
            m = max(m, i - s_i)
        return m


def test():
    s = Solution()
    assert s.lengthOfLongestSubstring('abcabcbb') == 3
    assert s.lengthOfLongestSubstring('bbbbb') == 1
    assert s.lengthOfLongestSubstring('pwwkew') == 3


if __name__ == '__main__':
    test()
