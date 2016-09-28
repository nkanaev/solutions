class Solution(object):
    def restoreIpAddresses(self, s):
        n = len(s)
        result = []
        for a in xrange(1, min(n-2, 4)):
            for b in xrange(a+1, min(n-1, a+4)):
                for c in xrange(b+1, min(n, b + 4)):
                    is_ip = self.is_valid(s[:a])
                    is_ip = is_ip and self.is_valid(s[a:b])
                    is_ip = is_ip and self.is_valid(s[b:c])
                    is_ip = is_ip and self.is_valid(s[c:])
                    if is_ip:
                        result.append('.'.join((s[:a], s[a:b], s[b:c], s[c:])))
        return result

    def is_valid(self, n):
        if len(n) > 3:
            return False
        if 1 < len(n) <= 3 and n[0] == '0':
            return False
        return int(n) < 256


def test():
    s = Solution()
    assert s.restoreIpAddresses('25525511135') == ["255.255.11.135", "255.255.111.35"]
