

class Solution(object):
    """
    dp完成，s分为2种情况，
    1.s小于10是一种解法
    2.s大于10小于27是2种解法，比如16分为1+6和16本身
    代码如下所示
    Runtime: 36 ms, faster than 18.72% of Python online submissions for Decode Ways.
    Memory Usage: 11.8 MB, less than 14.03% of Python online submissions for Decode Ways.
    """
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        for i in range(1, len(dp)):
            if s[i-1] != '0':
                dp[i] = dp[i-1]
            if i != 1 and '09' < s[i-2:i] < '27':
                dp[i] += dp[i-2]
        return dp[-1]