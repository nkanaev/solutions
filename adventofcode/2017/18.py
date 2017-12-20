import collections
import string


registers = set(string.ascii_lowercase)


def freq(instructions):
    ops = [i.split() for i in instructions]
    reg = collections.defaultdict(lambda: 0)
    last = 0
    i = 0
    while 0 <= i < len(ops):
        op = ops[i][0]
        x = ops[i][1]
        y = ops[i][2] if len(ops[i]) == 3 else None
        if y is not None:
            y = reg[y] if y in registers else int(y)

        if op == 'snd':
            last = reg[x]
        elif op == 'set':
            reg[x] = y
        elif op == 'add':
            reg[x] += y
        elif op == 'mul':
            reg[x] *= y
        elif op == 'mod':
            reg[x] %= y
        elif op == 'rcv':
            if reg[x]:
                return last
        elif op == 'jgz':
            if reg[x]:
                i += y
                continue
        i += 1


def test1():
    assert freq([
        'set a 1',
        'add a 2',
        'mul a a',
        'mod a 5',
        'snd a',
        'set a 0',
        'rcv a',
        'jgz a -1',
        'set a 1',
        'jgz a -2',
    ]) == 4


if __name__ == '__main__':
    with open('18.txt') as f:
        instructions = f.readlines()
    # solution 1
    print(freq(instructions))
