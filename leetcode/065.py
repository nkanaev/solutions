import re


class Solution(object):
    def isNumber(self, s):
        s = s.strip()
        if not s:
            return False
        return self.num(s)
        
    def digit(self, s):
        return len(s) == 1 and s in '0123456789'
        
    def eol(self, s):
        return s == ''

    def num(self, s):
        if s[0] == '-' or s[0] == '+':
            s = s[1:]
        if self.float(s, strict=True):
            return True
        for i in xrange(len(s)):
            if not self.digit(s[i]):
                return False
            if self.eol(s[i+1:]) or self.float(s[i+1:]) or self.e(s[i+1:]):
                return True
        return False
    
    def float(self, s, strict=False):
        if s[0] != '.':
            return False
        if strict and (len(s) < 2 or not self.digit(s[1])):
            return False
        for i in xrange(1, len(s)+1):
            if self.eol(s[i:]) or self.e(s[i:]):
                return True
            if not self.digit(s[i]):
                return False
        return False
        
    def e(self, s):
        if len(s) <= 1:
            return False
        if s and s[0] == 'e':
            if len(s) > 1 and s[1] == '-' or s[1] == '+':
                return self.int(s[2:])
            return self.int(s[1:])
        return False
        
    def int(self, s):
        if len(s) == 0:
            return False
        return all(map(self.digit, s))
        
