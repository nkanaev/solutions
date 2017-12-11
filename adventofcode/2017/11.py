def steps(path):
    x, y, z = 0, 0, 0
    for step in path.split(','):
        if step == 'n':
            x -= 1
            y += 1
        elif step == 'ne':
            y += 1
            z -= 1
        elif step == 'se':
            x += 1
            z -= 1
        elif step == 's':
            x += 1
            y -= 1
        elif step == 'sw':
            y -= 1
            z += 1
        elif step == 'nw':
            x -= 1
            z += 1
    return max(abs(x), abs(y), abs(z))


def test():
    assert steps('ne,ne,ne') == 3
    assert steps('ne,ne,sw,sw') == 0
    assert steps('ne,ne,s,s') == 2
    assert steps('se,sw,se,sw,sw') == 3


if __name__ == '__main__':
    import sys
    print(steps(sys.stdin.readline().strip()))
