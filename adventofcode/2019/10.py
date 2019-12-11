import sys, math, collections


Point = collections.namedtuple('Point', ['x', 'y'])
Config = collections.namedtuple('Config', ['star', 'angle', 'dist'])


def points_between(p1, p2):
    p1, p2 = sorted([p1, p2])
    w = int(abs(p1.x - p2.x))
    h = int(abs(p1.y - p2.y))
    sx = min(p1.x, p2.x)
    sy = min(p1.y, p2.y)
    if w >= h:
        d = 1 if p1.y <= p2.y else -1
        for ix in range(1, w):
            cx = sx + ix
            cy = p1.y + (ix / w) * h * d
            if int(cy) == cy:
                yield Point(float(cx), float(cy))
    else:
        d = 1 if p1.x <= p2.x else -1
        for iy in range(1, h):
            cy = sy + iy
            cx = p1.x + (iy / h) * w * d
            if int(cx) == cx:
                yield Point(float(cx), float(cy))


def cannon_config(p1, p2):
    angle = math.degrees(math.atan2(p2.x - p1.x, p1.y - p2.y))
    if angle < 0:
        angle = 360 + angle
    dist = math.hypot(p1.x - p2.x, p1.y - p2.y)
    return Config(p2, angle, dist)


def sol1(coords, w, h):
    map = {}
    for a1 in coords:
        for a2 in coords:
            if a1 == a2:
                continue
            if not set(points_between(a1, a2)).intersection(coords):
                c = (a1.x, a1.y)
                map[c] = map.get(c, 0) + 1
    max_coord, max_value = None, -1
    for coord, value in map.items():
        if value > max_value:
            max_coord, max_value = coord, value
    return Point(*max_coord), max_value


def sol2(coords, w, h, cannon):
    #from pprint import pprint
    configs = [cannon_config(cannon, coord) for coord in coords]
    configs = sorted(configs, key=lambda c: (c.angle, c.dist))
    ordered = []
    i = 0
    #pprint(configs)
    while configs:
        ordered.append(configs.pop(i))
        i = i % len(configs)
        if len(ordered) == 200:
            break
        if len(configs) == 1:
            ordered.append(configs.pop())
            break
        si = i
        while ordered[-1].angle == configs[i].angle:
            i = (i + 1) % len(configs)
            if i == si:
                ordered.extend(configs)
                break

    coord = ordered[200-1]
    return int(coord.star.x * 100 + coord.star.y)

    map = {}
    for i, config in enumerate(ordered):
        map[(config.star.x, config.star.y)] = i + 1
    for iy in range(h):
        for ix in range(w):
            print(str(map.get((ix, iy), '.')).rjust(3), end='')
        print('')
    #pprint(ordered)


def main():
    coords = set()
    w, h = 0, 0
    for y, line in enumerate(sys.stdin.readlines()):
        w = len(line)
        h += 1
        for x, ch in enumerate(line):
            if ch == '#':
                coords.add(Point(float(x), float(y)))
    coord, value = sol1(coords, w, h)
    print(value)
    print(sol2(coords, w, h, coord))


main()
