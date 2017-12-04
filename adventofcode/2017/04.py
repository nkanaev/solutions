def valid(line):
    words = line.split()
    return len(words) == len(set(words))


def test():
    assert valid('aa bb cc dd ee')
    assert not valid('aa bb cc dd aa')
    assert valid('aa bb cc dd aaa')


if __name__ == '__main__':
    import sys
    print(len([l for l in sys.stdin.readlines() if valid(l)]))
