from collections import Counter


class Solution:
    def isValidSudoku(self, board):
        for i in range(9):
            if not self.isValid(board[i]):
                return False
            if not self.isValid([row[i] for row in board]):
                return False
            row = (i // 3) * 3
            col = (i % 3) * 3
            if not self.isValid(
                    board[row][col:col+3] +
                    board[row+1][col:col+3] +
                    board[row+2][col:col+3]):
                return False
        return True

    def isValid(self, entries):
        count = Counter(entries)
        count.pop('.', None)
        return all(v == 1 for v in count.values())


def test():
    valid = Solution().isValidSudoku
    assert valid([
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ])
    assert not valid([
        ["8","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ])
