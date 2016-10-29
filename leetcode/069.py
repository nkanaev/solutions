class Solution(object):
    def mySqrt(self, x):
        x = float(x)
        s, e = 0, x
        for __ in xrange(1000):
            n = (s + e) / 2
            if n * n == x:
                break
            elif n * n < x:
                s = n
            else:
                e = n
        return int(n)
