

"""
For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

"""

#[[-1],[2,3],[1,-1,-3]] --》expected：-1
class Solution:
    def minimumTotal(self,triangle):
        n = len(triangle)
        dp = triangle[-1]
        for i in range(n - 2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = min(dp[j + 1], dp[j]) + triangle[i][j]
        return dp[0]