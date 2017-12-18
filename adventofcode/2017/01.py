def captchasum(data):
    nums = [int(d) for d in data]
    return sum((
        n for i, n in enumerate(nums)
        if nums[(i + 1) % len(nums)] == n))


def captchasum2(data):
    nums = [int(d) for d in data]
    s = len(data) // 2
    return sum((
        n for i, n in enumerate(nums)
        if nums[(i + s) % len(nums)] == n))


def test1():
    assert captchasum('1122') == 3
    assert captchasum('1111') == 4
    assert captchasum('1234') == 0
    assert captchasum('91212129') == 9


def test2():
    assert captchasum2('1212') == 6
    assert captchasum2('1221') == 0
    assert captchasum2('123425') == 4
    assert captchasum2('123123') == 12
    assert captchasum2('12131415') == 4


if __name__ == '__main__':
    with open('01.txt') as f:
        data = f.readline()
    print(captchasum(data))
    print(captchasum2(data))
