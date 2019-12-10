import sys
import itertools
import collections


def val(arr, idx, mode):
    # position mode
    if mode == 0:
        return arr[arr[idx]]
    # intermediate mode
    elif mode == 1:
        return arr[idx]
    raise RuntimeError('xxx')


def process(arr):
    arr = arr[:]
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
            x = yield
            if x is None:
                return
            arr[arr[pc+1]] = x
        elif op == 4:
            yield val(arr, pc+1, m1)
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


def sol1(arr):
    m = 0

    def call(arg1, arg2):
        vm = process(arr)
        next(vm)
        vm.send(arg1)
        return vm.send(arg2)

    for a, b, c, d, e in itertools.permutations([0, 1, 2, 3, 4]):
        r = call(e, call(d, call(c, call(b, call(a, 0)))))
        m = max(m, r)
    return m


def sol2(arr):
    m = 0

    def newvm(init):
        vm = process(arr)
        next(vm)
        vm.send(init)
        return vm
    return m


def main():
    data = [int(x) for x in sys.stdin.readline().split(',')]
    print(sol1(data))
    print(sol2(data))


main()
