def checksum(rows):
    return sum([max(r) - min(r) for r in rows])


def test():
    assert checksum([
        [5, 1, 9, 5],
        [7, 5, 3],
        [2, 4, 6, 8],
    ]) == 18


if __name__ == '__main__':
    import sys
    lines = sys.stdin.readlines()
    rows = [list(map(int, line.split())) for line in lines]
    print(checksum(rows))
