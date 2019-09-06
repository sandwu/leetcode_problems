



class Solution(object):
    """
    题目是求给定一个由'X'和'O'构成的二维数组，求将其中的O转为X，不过需要满足该O不在边界，并且与边界O相连的O也不能转换
    解法：BFS
    先构造一个边界列表，即下面的save，仅包含边界的元素。然后将这些边界元素为'O'的转为S，并且将围绕O的四个元素都加入save
    再进行一轮的判断是否为O(典型的BFS)。这样最后将二维数组除了S的都转为X，S的转为O
    最后一行也是很巧妙的简写，'XO'[c == 'S']用c == S的布尔值来当下标选X或O
    Runtime: 132 ms, faster than 62.40% of Python online submissions for Surrounded Regions.
    Memory Usage: 16.7 MB, less than 85.71% of Python online submissions for Surrounded Regions.
    """
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not any(board): return

        m, n = len(board), len(board[0])
        save = [ij for k in range(max(m,n)) for ij in ((0, k), (m-1, k), (k, 0), (k, n-1))]
        while save:
            i, j = save.pop()
            if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
                board[i][j] = 'S'
                save += (i, j-1), (i, j+1), (i-1, j), (i+1, j)

        board[:] = [['XO'[c == 'S'] for c in row] for row in board]

a = Solution()

board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

a.solve(board)