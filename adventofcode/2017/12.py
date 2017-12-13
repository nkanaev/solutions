def connections(lines):
    c = {}
    for l in lines:
        src, dst = l.split('<->')
        src = int(src)
        dst = {int(d) for d in dst.split(',')}
        c[src] = c.get(src, set()).union(dst)
    n = 0
    stack = {*c[0]}
    seen = set()
    while stack:
        node = stack.pop()
        if node in seen:
            continue
        seen.add(node)
        stack = stack.union(c[node] - seen)
        n += 1
    return n


def test():
    assert connections([
        '0 <-> 2',
        '1 <-> 1',
        '2 <-> 0, 3, 4',
        '3 <-> 2, 4',
        '4 <-> 2, 3, 6',
        '5 <-> 6',
        '6 <-> 4, 5']) == 6


if __name__ == '__main__':
    import sys
    print(connections(sys.stdin.readlines()))
