

"""
Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right

"""


class Solution:
    def unique_path(self, m, n): #到每一个格子都是从左边和上边的加一步，所以只要计算到左边和上边的有多少种即可
        dp = [[1] * m for _ in range(n)]
        for i in range(1,n):
            for j in range(1,m):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]

