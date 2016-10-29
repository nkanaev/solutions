class Solution(object):
    def setZeroes(self, matrix):
        n = len(matrix)
        m = len(matrix[0])
        for i in xrange(n):
            for j in xrange(m):
                if matrix[i][j] == 0:
                    matrix[i][j] = None
                    for k in xrange(n):
                        if matrix[k][j] != 0:
                            matrix[k][j] = None
                    for k in xrange(m):
                        if matrix[i][k] != 0:
                            matrix[i][k] = None
        for i in xrange(n):
            for j in xrange(m):
                if matrix[i][j] == None:
                    matrix[i][j] = 0

