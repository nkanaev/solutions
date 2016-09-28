class Solution(object):
    def myPow(self, x, n):
        s = -1 if n < 0 else 1
        if n == 1:
            return x
        if n == 0:
            return 1
        n = abs(n)
        if n % 2 == 0:
            r = self.myPow(x, n/2)
            r *= r
        else:
            r = self.myPow(x, n/2) * self.myPow(x, n-n/2)
        return r if s > 0 else 1 / r
