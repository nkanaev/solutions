def coordinates(path):
    sx, sy = 0, 0
    for subpath in path.split(','):
        d, l = subpath[0], int(subpath[1:])
        dx, dy = 0, 0
        if d == 'L':
            dy = -1
        elif d == 'R':
            dy = 1
        elif d == 'U':
            dx = -1
        elif d == 'D':
            dx = 1
        for _ in range(l):
            sx, sy = sx + dx, sy + dy
            yield sx, sy


def coordinates_steps(path):
    i = 0
    for x, y in coordinates(path):
        i += 1
        yield (x, y), i


def closest(p1, p2):
    p1 = set(coordinates(p1))
    p2 = set(coordinates(p2))
    intersections = p1.intersection(p2)
    return min([abs(x) + abs(y) for x, y in intersections])


def shortest(p1, p2):
    p1_steps = {c: step for c, step in coordinates_steps(p1)}
    m = float('inf')
    for c2, step2 in coordinates_steps(p2):
        if c2 in p1_steps:
            m = min(m, step2 + p1_steps[c2])
    return m


def main():
    import sys
    p1 = sys.stdin.readline()
    p2 = sys.stdin.readline()
    print(closest(p1, p2))
    print(shortest(p1, p2))


main()
