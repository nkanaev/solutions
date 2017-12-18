def shortcircuit1(steps):
    state = [0]
    p = 0
    for n in range(1, 2017 + 1):
        p = ((p + steps) % len(state)) + 1
        state.insert(p, n)
    return state[(state.index(2017) + 1) % len(state)]


def shortcircuit2(steps):
    after_zero = None
    p = 0
    l = 1
    for i in range(1, 50000000 + 1):
        p = ((p + steps) % l) + 1
        l += 1
        if p == 1:
            after_zero = i
    return after_zero


def test1():
    assert shortcircuit1(3) == 638



if __name__ == '__main__':
    # solution 1
    print(shortcircuit1(314))
    # solution 2
    print(shortcircuit2(314))
