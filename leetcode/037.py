class Solution(object):
    COLUMNS = [range(i % 9, 81, 9) for i in xrange(89)]
    ROWS = [range(9 * (i / 9), 9 * (i / 9) + 9) for i in xrange(81)]
    BLOCKS = [
        range(x, x + 3) + range(x + 9, x + 9 + 3) + range(x + 18, x + 18 + 3)
        for x in map(lambda i: 27 * (i / 27) + 3 * ((i % 9) / 3), xrange(81))
    ]
    PEERS = [set(COLUMNS[i] + ROWS[i] + BLOCKS[i]) - set([i]) for i in xrange(81)]
    UNITS = []

    def solveSudoku(self, board):
        board[:] = self.solve([''.join(row) for row in board])

    def solve(self, board):
        b = ''.join(board)
        v = ['123456789'] * 81
        for i, n in enumerate(b):
            if n != '.':
                if not self.assign(v, i, n):
                    return False
        return self.search(v)

    def search(self, v):
        if self.solved(v):
            v = ''.join(v)
            return [v[i:i+9] for i in xrange(0, 81, 9)]
        m = sorted([(len(v[i]), i) for i in xrange(81) if len(v[i]) > 1])
        for x in v[m[0][1]]:
            vv = v[:]
            if self.assign(vv, m[0][1], x):
                r = self.search(vv)
                if r:
                    return r

    def assign(self, v, i, n):
        v[i] = n
        for p in self.PEERS[i]:
            v[p] = v[p].replace(n, '')
            if len(v[p]) == 0:
                return False
            if len(v[p]) > 1:
                for nn in v[p]:
                    for unit in [self.COLUMNS[p], self.ROWS[p], self.BLOCKS[p]]:
                        x = [j for j in unit if (nn in v[j] and j != p)]
                        if len(x) == 0:
                            if not self.assign(v, p, nn):
                                return False
        return True

    def solved(self, v):
        return all(len(x) == 1 for x in v)

    def p(self, v):
        m = max(len(vv) for vv in v) + 1
        l = '+'.join('-' * (m * 3 + i % 2) for i in xrange(3))
        is_col = lambda x: (x + 1) % 3 == 0 and (x + 1) / 3 % 3 != 0
        for i in xrange(9):
            print ''.join(
                v[j].center(m) + ('| ' if is_col(j) else '') 
                for j in xrange(i*9,i*9+9)
            )
            if i in [2, 5]:
                print l
        print


def test():
    s = Solution()
    assert s.solve([
        "...2...63",
        "3....54.1",
        "..1..398.",
        ".......9.",
        "...538...",
        ".3.......",
        ".263..5..",
        "5.37....8",
        "47...1..."]
    ) == [
        "854219763",
        "397865421",
        "261473985",
        "785126394",
        "649538172",
        "132947856",
        "926384517",
        "513792648",
        "478651239"
    ]
    assert s.solve([
        "53..7....",
        "6..195...",
        ".98....6.",
        "8...6...3",
        "4..8.3..1",
        "7...2...6",
        ".6....28.",
        "...419..5",
        "....8..79"
    ]) == [
        "534678912",
        "672195348",
        "198342567",
        "859761423",
        "426853791",
        "713924856",
        "961537284",
        "287419635",
        "345286179"
    ]
    assert s.solve([
        "..9748...",
        "7........",
        ".2.1.9...",
        "..7...24.",
        ".64.1.59.",
        ".98...3..",
        "...8.3.2.",
        "........6",
        "...2759.."
    ]) == [
        "519748632",
        "783652419",
        "426139875",
        "357986241",
        "264317598",
        "198524367",
        "975863124",
        "832491756",
        "641275983"
    ]


test()
