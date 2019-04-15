
class Solution(object):
    """
    讨论区大神一行解决，代码理解是and前后为真则返回后者，那当matrix为空的时候，执行pop会报错，此时返回matrix
    matrix.pop(0)每次返回第一行数，而后段代码递归调用，以示例为例，第一次返回[(6, 9), (5, 8), (4, 7)]，因为
    被下一次pop出(6,9)，第二次返回[(8,7),(5,4)]，最后拼接即是答案
    Runtime: 40 ms, faster than 31.27% of Python3 online submissions for Spiral Matrix.
    Memory Usage: 13.2 MB, less than 5.18% of Python3 online submissions for Spiral Matrix.
    """
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])
        

class Solution2(object):
    """
    正常思路，代码看的是真的舒服，即依次定义row、col，按照逻辑，先返回第一行，然后依次取每行的最后一个数，
    接着返回最后一行从后往前，最后返回每行的第一个数。然后循环此段操作。
    当l==r，说明只剩中间一行，直接reverse即可；当u==d，说明只剩中间一列，直接颠倒即可。
    Runtime: 36 ms, faster than 51.51% of Python3 online submissions for Spiral Matrix.
    Memory Usage: 13.2 MB, less than 5.18% of Python3 online submissions for Spiral Matrix.
    """
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        ans = []
        m, n = len(matrix), len(matrix[0])
        u, d, l, r = 0, m - 1, 0, n - 1
        while l < r and u < d:
            ans.extend([matrix[u][j] for j in range(l, r)])
            ans.extend([matrix[i][r] for i in range(u, d)])
            ans.extend([matrix[d][j] for j in range(r, l, -1)])
            ans.extend([matrix[i][l] for i in range(d, u, -1)])
            u, d, l, r = u + 1, d - 1, l + 1, r - 1
        if l == r:
            ans.extend([matrix[i][r] for i in range(u, d + 1)])
        elif u == d:
            ans.extend([matrix[u][j] for j in range(l, r + 1)])
        return ans