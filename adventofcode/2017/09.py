def score(line):
    x = 0
    i = 0
    s = 0
    while i < len(line):
        if line[i] == '{':
            x += 1
            i += 1
        elif line[i] == '<':
            gi = i
            while gi < len(line):
                if line[gi] == '>':
                    i = gi + 1
                    break
                elif line[gi] == '!':
                    gi += 2
                else:
                    gi += 1
        elif line[i] == ',':
            i += 1
        elif line[i] == '}':
            s += x
            x -= 1
            i += 1
    return s


def test():
    assert score('{}') == 1
    assert score('{{{}}}') == 6
    assert score('{{},{}}') == 5
    assert score('{{{},{},{{}}}}') == 16
    assert score('{<a>,<a>,<a>,<a>}') == 1
    assert score('{{<!!>},{<!!>},{<!!>},{<!!>}}') == 9
    assert score('{{<ab>},{<ab>},{<ab>},{<ab>}}') == 9
    assert score('{{<a!>},{<a!>},{<a!>},{<ab>}}') == 3


if __name__ == '__main__':
    import sys
    print(score(sys.stdin.readline()))
