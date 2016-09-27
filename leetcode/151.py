import re


class Solution(object):
    def reverseWords(self, s):
        return ' '.join(reversed(re.findall('[^ ]+', s)))
