from collections import deque


class Solution(object):
    def spiralOrder(self, matrix):
        matrix = deque([deque(row) for row in matrix])
        result = []
        while matrix:
            # top
            result.extend(matrix.popleft())
            # right
            for i in xrange(len(matrix)):
                if matrix[i]:
                    result.append(matrix[i].pop())
            # bottom
            if matrix:
                result.extend(reversed(matrix.pop()))
            # left
            for i in xrange(len(matrix) - 1, -1, -1):
                if matrix[i]:
                    result.append(matrix[i].popleft())
        return result
