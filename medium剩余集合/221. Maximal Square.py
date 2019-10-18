



class Solution(object):
    """
    题意是求matrix矩阵里的小矩形，满足小矩形全部都是1的特征
    解法是重新构造一个矩形，然后判断一个数，当它附件都是1的时候，就取2，最后取该最大值的平方即可
    Runtime: 200 ms, faster than 26.44% of Python online submissions for Maximal Square.
    Memory Usage: 19.7 MB, less than 12.50% of Python online submissions for Maximal Square.
    """
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0]) if m else 0
        maxn = 0
        f = [[0] * (n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if matrix[i-1][j-1] == '1':
                    f[i][j] = 1 + min(f[i-1][j], f[i][j-1], f[i-1][j-1])
                    maxn = max(maxn, f[i][j])
        return maxn**2

matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
a = Solution()
print(a.maximalSquare(matrix))