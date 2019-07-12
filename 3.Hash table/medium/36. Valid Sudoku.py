



class Solution(object):
    """
    直接按题目大意，从横、竖、9宫格三方面来比较
    比较有意思的是9宫格的取得方式(每次取一个小九宫格)，另外比较的话直接定义字典(或集合)来存储，存在的话则说明有重复值
    Runtime: 84 ms, faster than 34.44% of Python online submissions for Valid Sudoku.
    Memory Usage: 11.7 MB, less than 5.11% of Python online submissions for Valid Sudoku.
    """
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            if not self.isValidNine(board[i]):
                return False
            col = [c[i] for c in board]
            if not self.isValidNine(col):
                return False
        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                block = [board[s][t] for s in [i, i+1, i+2] for t in [j, j+1, j+2]]
                if not self.isValidNine(block):
                    return False
        return True

    def isValidNine(self, row):
        map = {}
        for c in row:
            if c != '.':
                if c in map:
                    return False
                else:
                    map[c] = True
        return True





class Solution2(object):
    """
    可以说是上面的简化版，不过相对没那么好理解
    Runtime: 76 ms, faster than 42.37% of Python online submissions for Valid Sudoku.
    Memory Usage: 11.8 MB, less than 5.11% of Python online submissions for Valid Sudoku.
    """
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        seen = set()
        return not any(x in seen or seen.add(x)
                       for i, row in enumerate(board)
                       for j, c in enumerate(row)
                       if c != '.'
                       for x in ((c, i), (j, c), (i/3, j/3, c)))


class Solution3(object):
    """
    相对上面一种简化版，这个版本更好理解
    Runtime: 80 ms, faster than 40.20% of Python online submissions for Valid Sudoku.
    Memory Usage: 11.9 MB, less than 5.11% of Python online submissions for Valid Sudoku.
    """
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        seen = []
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                if c != '.':
                    seen += [(c,j),(i,c),(i/3,j/3,c)]
        return len(seen) == len(set(seen))
