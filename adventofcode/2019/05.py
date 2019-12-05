import sys


def val(arr, idx, mode):
    # position mode
    if mode == 0:
        return arr[arr[idx]]
    # intermediate mode
    elif mode == 1:
        return arr[idx]
    raise RuntimeError('xxx')


def process(arr, inputval):
    pc = 0
    length = {1: 4, 2: 4, 3: 2, 4: 2, 5: 3, 6: 3, 7: 4, 8: 4, 99: 0}
    while 1:
        mode, op = divmod(arr[pc], 100)
        m2, m1 = divmod(mode, 10)
        if op == 1:
            arr[arr[pc+3]] = val(arr, pc+1, m1) + val(arr, pc+2, m2)
        elif op == 2:
            arr[arr[pc+3]] = val(arr, pc+1, m1) * val(arr, pc+2, m2)
        elif op == 3:
            arr[arr[pc+1]] = inputval
            print(arr[arr[pc+1]])
        elif op == 4:
            print(val(arr, pc+1, m1))
        elif op == 5:
            if val(arr, pc+1, m1) != 0:
                pc = val(arr, pc+2, m2)
                continue
        elif op == 6:
            if val(arr, pc+1, m1) == 0:
                pc = val(arr, pc+2, m2)
                continue
        elif op == 7:
            arr[val(arr, pc+3, 1)] = 1 \
                if val(arr, pc+1, m1) < val(arr, pc+2, m2) \
                else 0
        elif op == 8:
            arr[val(arr, pc+3, 1)] = 1 \
                if val(arr, pc+1, m1) == val(arr, pc+2, m2) \
                else 0
        elif op == 99:
            return
        else:
            raise RuntimeError('yyy')
        pc += length[op]


def main():
    data = [int(x) for x in sys.stdin.readline().split(',')]
    process(data[:], inputval=1)
    process(data[:], inputval=5)


main()
