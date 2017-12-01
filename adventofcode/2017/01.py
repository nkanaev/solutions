def captchasum(data):
    nums = [int(d) for d in data]
    return sum((
        n for i, n in enumerate(nums)
        if nums[(i + 1) % len(nums)] == n))


def test():
    assert captchasum('1122') == 3
    assert captchasum('1111') == 4
    assert captchasum('1234') == 0
    assert captchasum('91212129') == 9


if __name__ == '__main__':
    import sys
    print(captchasum(sys.stdin.readline()))
