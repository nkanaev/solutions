import operator


OPERATORS = {
    '<': operator.lt,
    '>': operator.gt,
    '<=': operator.le,
    '>=': operator.ge,
    '==': operator.eq,
    '!=': operator.ne,

    'inc': operator.add,
    'dec': operator.sub
}


def regmax(lines):
    register = {}
    for line in lines:
        reg, cmd, num, _, creg, op, cnum = line.split()
        num, cnum = int(num), int(cnum)
        if OPERATORS[op](register.get(creg, 0), cnum):
            register[reg] = OPERATORS[cmd](register.get(reg, 0), num)
    return max(register.values())


def test():
    assert regmax([
        'b inc 5 if a > 1',
        'a inc 1 if b < 5',
        'c dec -10 if a >= 1',
        'c inc -20 if c == 10',
    ]) == 1


if __name__ == '__main__':
    import sys
    print(regmax(sys.stdin.readlines()))
