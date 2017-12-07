def parent(lines):
    parent = {}
    for l in lines:
        words = l.split()
        node = words[0]
        if len(words) > 2:
            for child in [w.rstrip(',') for w in words[3:]]:
                parent[child] = node
        parent.setdefault(node, None)
    return next(node for node, parent in parent.items() if parent is None)


def test():
    import textwrap
    assert(parent(textwrap.dedent('''\
        pbga (66)
        xhth (57)
        ebii (61)
        havc (66)
        ktlj (57)
        fwft (72) -> ktlj, cntj, xhth
        qoyq (66)
        padx (45) -> pbga, havc, qoyq
        tknk (41) -> ugml, padx, fwft
        jptl (61)
        ugml (68) -> gyxo, ebii, jptl
        gyxo (61)
        cntj (57)''').split('\n'))) == 'tknk'


if __name__ == '__main__':
    import sys
    print(parent(sys.stdin.readlines()))
