import operator


PREC = {
    '*': 2,
    '/': 2,
    '+': 1,
    '-': 1,
}

OPERATOR = {
    '*': operator.mul,
    '/': operator.div,
    '+': operator.add,
    '-': operator.sub,
}


class Solution(object):
    def calculate(self, s):
        out_stack = []
        op_stack = []
        i = 0
        while i < len(s):
            if s[i] == ' ':
                i += 1
            elif s[i] in PREC:
                while op_stack and PREC[s[i]] <= PREC[op_stack[-1]]:
                    out_stack.append(op_stack.pop())
                op_stack.append(s[i])
                i += 1
            else:
                i_start = i
                while i < len(s) and s[i] in '0123456789':
                    i += 1
                out_stack.append(int(s[i_start:i]))
                
        out_stack.extend(reversed(op_stack))
        out = []
        i = 0
        print out_stack
        while i < len(out_stack):
            x = out_stack[i]
            if x in OPERATOR:
                op = OPERATOR[x]
                x1 = out.pop()
                x2 = out.pop()
                out.append(op(x2, x1))
            else:
                out.append(x)
            i += 1
        return out[0]
