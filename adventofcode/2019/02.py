def process(arr):
    pc = 0
    while arr[pc] != 99:
        if arr[pc] == 1:
            arr[arr[pc + 3]] = arr[arr[pc + 1]] + arr[arr[pc + 2]]
        elif arr[pc] == 2:
            arr[arr[pc + 3]] = arr[arr[pc + 1]] * arr[arr[pc + 2]]
        else:
            raise RuntimeError('unknown command {} at position {}'.format(arr[pc], pc))
        pc += 4
    return arr[0]


def main():
    import sys
    input = [int(x) for x in sys.stdin.readline().split(',')]

    arr = input[:]
    arr[1], arr[2] = 12, 2
    print(process(arr))

    for n in range(100):
        for v in range(100):
            arr = input[:]
            arr[1], arr[2] = n, v
            if process(arr) == 19690720:
                print(100 * n + v)
                return


if __name__ == '__main__':
    main()
