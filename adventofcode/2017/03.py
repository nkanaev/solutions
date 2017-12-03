def steps(n):
    stepnext = {
        'right': ('up', 0, 1),
        'up': ('left', -1, 0),
        'left': ('down', 0, -1),
        'down': ('right', 1, 0),
    }
    stepsize = 0
    stepsleft, move = 0, 'right'
    x, y = 0, 0
    vx, vy = 0, 0
    for _ in range(1, n):
        if stepsleft == 0 and move == 'right':
            x += 1
            stepsize += 2
            stepsleft = stepsize - 1
            move, vx, vy = stepnext[move]
            continue
        elif stepsleft == 0:
            stepsleft = stepsize
            move, vx, vy = stepnext[move]
        x, y = x + vx, y + vy
        stepsleft -= 1
    return abs(x) + abs(y)


def test():
    assert steps(1) == 0
    assert steps(12) == 3
    assert steps(23) == 2
    assert steps(1024) == 31


if __name__ == '__main__':
    print(steps(277678))
