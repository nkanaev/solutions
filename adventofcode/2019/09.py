import sys, collections


def process(data, inputval):
    pc = 0
    rb = 0
    length = {1: 4, 2: 4, 3: 2, 4: 2, 5: 3, 6: 3, 7: 4, 8: 4, 9: 2, 99: 0}
    arr = collections.defaultdict(lambda: 0)
    for i, val in enumerate(data):
        arr[i] = val

    def validx(idx, mode):
        # position mode
        if mode == 0:
            return arr[idx]
        # intermediate mode
        elif mode == 1:
            return idx
        # relative mode
        elif mode == 2:
            return arr[idx] + rb
        raise RuntimeError('invalid mode: %d' % mode)

    def val(idx, mode):
        return arr[validx(idx, mode)]

    def setval(idx, mode, newval):
        arr[validx(idx, mode)] = newval

    while 1:
        mode, op = divmod(arr[pc], 100)
        m2, m1 = divmod(mode, 10)
        m3, m2 = divmod(m2, 10)
        print(f':: pc={pc:03} op={op} rb={rb} |', [arr[idx] for idx in range(pc, pc+length[op])], file=sys.stderr)
        if op == 1:
            setval(pc+3, m3, val(pc+1, m1) + val(pc+2, m2))
        elif op == 2:
            setval(pc+3, m3, val(pc+1, m1) * val(pc+2, m2))
        elif op == 3:
            if m1 == 0:
                arr[arr[pc+1]] = inputval
            elif m1 == 1:
                arr[pc+1] = inputval
            elif m1 == 2:
                arr[arr[pc+1]+rb] = inputval
        elif op == 4:
            print('>>', val(pc+1, m1), m1, pc, file=sys.stderr)
            print(val(pc+1, m1))
        elif op == 5:
            if val(pc+1, m1) != 0:
                pc = val(pc+2, m2)
                continue
        elif op == 6:
            if val(pc+1, m1) == 0:
                pc = val(pc+2, m2)
                continue
        elif op == 7:
            setval(pc+3, m3, 1 if val(pc+1, m1) < val(pc+2, m2) else 0)
        elif op == 8:
            setval(pc+3, m3, 1 if val(pc+1, m1) == val(pc+2, m2) else 0)
        elif op == 9:
            rb += val(pc+1, m1)
        elif op == 99:
            return
        else:
            raise RuntimeError('yyy')
        pc += length[op]


def main():
    data = [int(x) for x in sys.stdin.readline().split(',')]
    process(data[:], inputval=1)
    process(data[:], inputval=2)


main()
