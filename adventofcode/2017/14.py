import string


khash = __import__('10').khash
alphabet = string.digits + string.ascii_lowercase


def squares(key):
    c = 0
    for i in range(128):
        h = khash(key + '-' + str(i))
        c += bin(int(h, 16)).count('1')
    return c


def regions(key):
    disk = []
    for i in range(128):
        hash = khash(key + '-' + str(i))
        disk.append(list(map(int, bin(int(hash, 16))[2:].rjust(128, '0'))))
    count = 0
    for start_row in range(128):
        for start_col in range(128):
            if disk[start_row][start_col]:
                stack = [(start_row, start_col)]
                while stack:
                    row, col = stack.pop()
                    disk[row][col] = 0
                    if row > 0 and disk[row - 1][col]:
                        stack.append((row - 1, col))
                    if row < 127 and disk[row + 1][col]:
                        stack.append((row + 1, col))
                    if col > 0 and disk[row][col - 1]:
                        stack.append((row, col - 1))
                    if col < 127 and disk[row][col + 1]:
                        stack.append((row, col + 1))
                count += 1
    return count


def test_1():
    assert squares('flqrgnkx') == 8108
    assert 1 == 2


def test_2():
    assert regions('flqrgnkx') == 1242


def result_1():
    print(squares('vbqugkhl'))


def result_2():
    print(regions('vbqugkhl'))
