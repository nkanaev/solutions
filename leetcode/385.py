class Solution(object):
    def deserialize(self, s):
        stack = []
        num = ''
        for c in s:
            if c == '[':
                stack.append(NestedInteger())
            elif c == ']':
                if num:
                    stack[-1].add(NestedInteger(int(num)))
                    num = ''
                l = stack.pop()
                if stack:
                    stack[-1].add(l)
                else:
                    stack.append(l)
            elif c == ',':
                if num:
                    stack[-1].add(NestedInteger(int(num)))
                num = ''
            else:
                num += c
        if num:
            stack.append(NestedInteger(int(num)))
        return stack[0]

