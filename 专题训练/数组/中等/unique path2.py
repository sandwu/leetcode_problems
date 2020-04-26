

"""

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
"""

class Solution(object):
    """
    直接按照62的解题思路来做
    Runtime: 24 ms, faster than 61.86% of Python online submissions for Unique Paths II.
    Memory Usage: 10.9 MB, less than 22.36% of Python online submissions for Unique Paths II.
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid or not obstacleGrid[0]:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0]*n for _ in range(m)]
        if obstacleGrid[0][0] == 0:
            dp[0][0] = 1
        else:
            return 0
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    continue
                if i > 0:
                    dp[i][j] += dp[i-1][j]
                if j > 0:
                    dp[i][j] += dp[i][j-1]
        return dp[-1][-1]

class Solution2(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        self.memo = {}
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        count = self.dfs(0,0,m-1,n-1,obstacleGrid)
        return count

    def dfs(self,i,j,m,n,obstacleGrid):
        if (i,j) in self.memo:return self.memo[i,j]
        if i > m or j > n:return 0
        if obstacleGrid[i][j] == 1: return 0
        if i==m and j ==n:return 1
        count = self.dfs(i+1,j,m,n,obstacleGrid) + self.dfs(i,j+1,m,n,obstacleGrid)
        self.memo[i,j] = count
        return count

class Solution3(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        dp = [[0 for i in range(cols)] for j in range(rows)]
        for i in range(rows-1, -1, -1):
            for j in range(cols-1, -1, -1):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if i == rows-1 and j == cols-1:
                        dp[i][j] = 1
                    elif i == rows - 1:
                        dp[i][j] = dp[i][j+1]
                    elif j == cols -1:
                        dp[i][j] = dp[i+1][j]
                    else:
                        dp[i][j] = dp[i+1][j] + dp[i][j+1]
        return dp[0][0]