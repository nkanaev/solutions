import sys


def fuel(mass):
    return int(mass / 3) - 2


def fuelfuel(f):
    t = 0
    while True:
        f = fuel(f)
        if f <= 0:
            break
        t += f
    return t


def sol1(masses):
    return sum(map(fuel, masses))


def sol2(masses):
    return sum(map(fuelfuel, masses))


if __name__ == '__main__':
    data = [int(line) for line in sys.stdin.readlines()]
    print(sol1(data))
    print(sol2(data))
