
class Solution(object):
    """
    因为最后一步只有两种情况，要么从左到右，要么从上到下，所以可以去算前面两种情况的和
    解法事先定义一个集合，每一种路径则在目的地+1，到最后的[-1][-1]即能找到最后的路径总数
    Runtime: 16 ms, faster than 100.00% of Python online submissions for Unique Paths.
    Memory Usage: 10.8 MB, less than 31.15% of Python online submissions for Unique Paths.
    """
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        res = [[1 for _ in range(m)] for _ in range(n)]
        for i in range(1,n):
            for j in range(1,m):
                res[i][j] = res[i][j-1] + res[i-1][j]
        return res[-1][-1]


class Solution(object):
    """
    上面的优化！
    Runtime: 16 ms, faster than 100.00% of Python online submissions for Unique Paths.
    Memory Usage: 10.6 MB, less than 96.72% of Python online submissions for Unique Paths.
    """
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [1] + [0] * (n-1)
        for i in range(m):
            for j in range(1, n):
                dp[j] += dp[j-1]
        return dp[-1]