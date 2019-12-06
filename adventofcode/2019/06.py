import sys


def orbitcount(orbit, orbits, cache):
    if orbit not in orbits:
        return 0
    if orbit not in cache:
        cache[orbit] = orbitcount(orbits[orbit], orbits, cache) + 1
    return cache[orbit]


def shortestdistance(src, dst, orbits):
    src_path, dst_path = [], []
    cur_src, cur_dst = src, dst

    while cur_src:
        src_path.append(cur_src)
        cur_src = orbits.get(cur_src)
    while cur_dst:
        dst_path.append(cur_dst)
        cur_dst = orbits.get(cur_dst)

    for src_parent_idx, src_parent in enumerate(src_path):
        if src_parent in dst_path:
            dst_parent_idx = dst_path.index(src_parent)
            return src_parent_idx + dst_parent_idx - 2


def main():
    orbits = {}
    for line in sys.stdin.readlines():
        orbit, object = line.strip().split(')')
        orbits[object] = orbit

    sol1 = sum(orbitcount(orbit, orbits, {}) for orbit in orbits)
    print(sol1)

    sol2 = shortestdistance('YOU', 'SAN', orbits)
    print(sol2)


main()
