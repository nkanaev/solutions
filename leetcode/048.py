class Solution(object):
    def rotate(self, matrix):
        n = len(matrix) - 1
        for i in xrange(len(matrix)):
            for j in xrange(i, len(matrix)-i - 1):
                t = matrix[i][j]
                matrix[i][j] = matrix[n-j][i]
                matrix[n-j][i] = matrix[n-i][n-j]
                matrix[n-i][n-j] = matrix[j][n-i]
                matrix[j][n-i] = t
