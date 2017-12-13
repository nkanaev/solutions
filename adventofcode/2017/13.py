def severity(layers):
    layers = dict(list(map(int, l.split(':'))) for l in layers)
    states = {g: (0, 1) for g in layers.keys()}
    result = 0
    for i in range(max(layers.keys()) + 1):
        if states.get(i, (None, None))[0] == 0:
            result += i * layers[i]
        for guard in states:
            states[guard] = (states[guard][0] + states[guard][1], states[guard][1])
            if states[guard] == (layers[guard], 1):
                states[guard] = (layers[guard] - 2, -1)
            elif states[guard] == (-1, -1):
                states[guard] = (1, 1)
    return result


def test():
    assert severity(['0: 3', '1: 2', '4: 4', '6: 4']) == 24


if __name__ == '__main__':
    import sys
    print(severity(sys.stdin.readlines()))
