


class Solution(object):
    def canMakePaliQueries(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        cnt = [[0] * 26]
        for i, c in enumerate(s):
            cnt.append(cnt[i][:])
            cnt[i + 1][ord(c) - ord('a')] += 1
        return [sum((cnt[hi + 1][i] - cnt[lo][i]) % 2 for i in range(26)) // 2 <= k for lo, hi, k in queries]



class Solution2(object):
    def canMakePaliQueries(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        N = 26
        S = len(s) + 1
        ints = list(map(lambda c: ord(c) - ord('a'), s))

        dp = [0] * S
        for i in range(1, S):
            dp[i] = dp[i-1] ^ (1 << ints[i-1])

        ones = lambda x: bin(x).count('1')
        return [
            ones(dp[r+1] ^ dp[l]) >> 1 <= k
            for l, r, k in queries
        ]