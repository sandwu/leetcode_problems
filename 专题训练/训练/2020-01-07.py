



class Solution:
    def numtrees(self,n):
        dp = [0] * (n+1)
        dp[0] = 1
        for i in range(1,n+1):
            for j in range(i):
                dp[i] += dp[j] * dp[i-j-1]
        return dp.pop()

    def __init__(self):
        self.dp = {}

    def numtrees2(self,n):
        if n in self.dp:
            return self.dp[n]
        if n == 0 or n == 1:
            return 1
        ans = 0
        for i in range(1, n + 1):
            ans += self.numtrees2(i - 1) * self.numtrees2(n - i)
        self.dp[n] = ans
        return ans