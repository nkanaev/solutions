def checksum(rows):
    return sum([max(r) - min(r) for r in rows])


def checksum2(rows):
    result = 0
    for row in rows:
        for i in range(len(row) - 1):
            for j in range(i + 1, len(row)):
                if i == j:
                    continue
                a, b = max(row[i], row[j]), min(row[i], row[j])
                if a % b == 0:
                    result += a // b
                    break
    return result


def test1():
    assert checksum([
        [5, 1, 9, 5],
        [7, 5, 3],
        [2, 4, 6, 8],
    ]) == 18


def test2():
    assert checksum2([
        [5, 9, 2, 8],
        [9, 4, 7, 3],
        [3, 8, 6, 5],
    ]) == 9


if __name__ == '__main__':
    with open('02.txt') as f:
        lines = f.readlines()
        rows = [list(map(int, line.split())) for line in lines]
    print(checksum(rows))
    print(checksum2(rows))
