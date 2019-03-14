
class Solution(object):
    """
    用dp的思路来完成，因为triangle里的层次，每个位置相当于被上面的两个节点所共有，但从上到下的dp会导致元素变多，
    所以从下到上来实现，如下；
    minpath[k][i] = min( minpath[k+1][i], minpath[k+1][i+1]) + triangle[k][i];
    因为minpath[k][i]只使用一次，所以可以变成一维dp：
    minpath[i] = min( minpath[i], minpath[i+1]) + triangle[k][i];
    Runtime: 24 ms, faster than 92.56% of Python online submissions for Triangle.
    Memory Usage: 11.2 MB, less than 59.43% of Python online submissions for Triangle.
    """
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        dp = triangle[-1]
        for layer in range(n - 2, -1, -1):
            for i in range(layer + 1):
                dp[i] = min(dp[i], dp[i + 1]) + triangle[layer][i]
        return dp[0]
