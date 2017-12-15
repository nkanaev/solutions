def count(astate, bstate):
    c = 0
    mask = (1 << 16) - 1
    for _ in range(40000000):
        astate = astate * 16807 % 2147483647
        bstate = bstate * 48271 % 2147483647
        if (astate & mask) == (bstate & mask):
            c += 1
    return c


def test():
    assert count(65, 8921) == 588


if __name__ == '__main__':
    print(count(873, 583))
