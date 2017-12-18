def order(moves, programs='abcdefghijklmnop'):
    programs = list(programs)
    for move in moves:
        if move[0] == 's':
            x = int(move[1:])
            programs = programs[-x:] + programs[:len(programs) - x]
        elif move[0] == 'x':
            a, b = map(int, move[1:].split('/'))
            programs[a], programs[b] = programs[b], programs[a]
        elif move[0] == 'p':
            a, b = move[1:].split('/')
            ia, ib = programs.index(a), programs.index(b)
            programs[ia], programs[ib] = programs[ib], programs[ia]
    return ''.join(programs)


def test1():
    assert order('s1,x3/4,pe/b'.split(','), programs='abcde') == 'baedc'


def solution1():
    with open('16.txt') as f:
        moves = f.read().split(',')
    print(order(moves))


if __name__ == '__main__':
    solution1()
