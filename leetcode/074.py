class Solution(object):
    def searchMatrix(self, matrix, target):
        s, e = 0, len(matrix)
        while s != e:
            m = (s + e) / 2
            if matrix[m][0] == target:
                return True
            if matrix[m][0] < target:
                s = m + 1
            else:
                e = m
        c = max(0, s - 1)
        s, e = 0, len(matrix[c])
        while s != e:
            m = (s + e) / 2
            if matrix[c][m] == target:
                return True
            if matrix[c][m] < target:
                s = m + 1
            else:
                e = m
        return False
