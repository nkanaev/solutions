import re


class Solution(object):
    def simplifyPath(self, path):
        paths = re.findall(r'/[^\/]*', path)
        r = []
        for p in paths:
            if p == '/' or p == '/.':
                continue
            elif p == '/..':
                if r:
                    r.pop()
            else:
                r.append(p)
        return ''.join(r).rstrip('/') or '/'
