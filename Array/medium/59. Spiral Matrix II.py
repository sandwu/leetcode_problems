class Solution:
    """
    解法沿用54，Sprial Matrix的解法，定义u\d\l\r四个变量，以3*3为例，分为上、右、下、左四层，然后每层循环遍历出各自的数，
    最后再得出9所在的中心位置，如果超过3*3，则在while里循环一次
    Runtime: 40 ms, faster than 51.34% of Python3 online submissions for Spiral Matrix II.
    Memory Usage: 13.1 MB, less than 5.40% of Python3 online submissions for Spiral Matrix II.
    """
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        x, u, d, l, r = 1, 0, n - 1, 0, n - 1
        # x is the next value to write
        # u and d are upper and lower bound of current square/rectangle
        # l and r are left and right bound of current square/rectangle
        while l < r and u < d:
            for j in range(l, r):
                matrix[u][j] = x
                x += 1
            for i in range(u, d):
                matrix[i][r] = x
                x += 1
            for j in range(r, l, -1):
                matrix[d][j] = x
                x += 1
            for i in range(d, u, -1):
                matrix[i][l] = x
                x += 1
            u, d, l, r = u + 1, d - 1, l + 1, r - 1
        if l == r:
            matrix[u][r] = x
        return matrix

class Solution1(object):
    """
    讨论区解法1,在上述解法上直接优化了三次遍历，牛皮！
    Runtime: 20 ms, faster than 100.00% of Python online submissions for Spiral Matrix II.
    Memory Usage: 10.8 MB, less than 26.97% of Python online submissions for Spiral Matrix II.
    """
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        A = [[0] * n for _ in range(n)]
        i, j, di, dj = 0, 0, 0, 1
        for k in xrange(n*n):
            A[i][j] = k + 1
            if A[(i+di)%n][(j+dj)%n]:
                di, dj = dj, -di
            i += di
            j += dj
        return A


class Solution2(object):
    """
    讨论区解法2，可以说很强大了
    Runtime: 20 ms, faster than 100.00% of Python online submissions for Spiral Matrix II.
    Memory Usage: 10.9 MB, less than 5.62% of Python online submissions for Spiral Matrix II.
    """
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        A = [[n*n]]
        while A[0][0] > 1:
            A = [range(A[0][0] - len(A), A[0][0])] + zip(*A[::-1])
        return A 