class Solution(object):
    def maxArea(self, height):
        s_i, e_i = 0, len(height) - 1
        m = 0
        while s_i != e_i:
            m = max(m, min(height[s_i], height[e_i]) * (e_i - s_i))
            if height[s_i] < height[e_i]:
                s_i += 1
            else:
                e_i -= 1
        return m


def test():
    s = Solution()
    assert s.maxArea([1, 1]) == 1
    assert s.maxArea([2, 1, 1, 10]) == 6
    assert s.maxArea([2, 1, 10]) == 4
    assert s.maxArea([20, 1, 2]) == 4
    assert s.maxArea([1, 2, 4, 3]) == 4


if __name__ == '__main__':
    test()
