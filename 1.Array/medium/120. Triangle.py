
class Solution(object):
    """
    用dp的思路来完成，因为triangle里的层次，每个位置相当于被上面的两个节点所共有，但从上到下的dp会导致元素变多，
    所以从下到上来实现，如下；
    minpath[k][i] = min( minpath[k+1][i], minpath[k+1][i+1]) + triangle[k][i];
    因为minpath[k][i]只使用一次，所以可以变成一维dp：
    minpath[i] = min( minpath[i], minpath[i+1]) + triangle[k][i];
    Runtime: 20 ms, faster than 100.00% of Python online submissions for Triangle.
    Memory Usage: 11 MB, less than 97.17% of Python online submissions for Triangle.
    """
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        dp = triangle[-1]
        for i in range(n - 2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = min(dp[j+1], dp[j]) + triangle[i][j]
        return dp[0]
