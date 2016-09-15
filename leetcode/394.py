import string


class Solution(object):
    def decodeString(self, s):
        num_stack = []
        str_stack = ['']
        i = 0
        while i < len(s):
            if s[i] in string.digits:
                s_i = i
                while s[i] in string.digits:
                    i += 1
                n = int(s[s_i:i])
                num_stack.append(n)
            elif s[i] == '[':
                i += 1
                str_stack.append('')
            elif s[i] in string.ascii_lowercase:
                s_i = i
                while s[i] in string.ascii_lowercase:
                    i += 1
                    if i == len(s):
                        break
                str_stack[-1] += s[s_i:i]
            elif s[i] == ']':
                i += 1
                x = str_stack.pop() * num_stack.pop()
                str_stack[-1] += x
        return ''.join(str_stack)


def test():
    s = Solution()
    assert s.decodeString('2[2[b]]') == 'bbbb'
    assert s.decodeString('3[a]2[bc]') == 'aaabcbc'
    assert s.decodeString('3[a2[c]]') == 'accaccacc'
    assert s.decodeString('2[abc]3[cd]ef') == 'abcabccdcdcdef'


if __name__ == '__main__':
    test()
