

class Solution(object):
    """
    首先定义一个包含所有数用0替代的集合
    动态规划思想，当i-j<2时，只要判断s[i]==s[j]即可，当i-j>2时，要接着判断dp[j+1][i-1]。
    效率虽然不高，但是代码是真的少以及好理解
    Runtime: 2208 ms, faster than 36.90% of Python online submissions for Longest Palindromic Substring.
    Memory Usage: 19.5 MB, less than 9.90% of Python online submissions for Longest Palindromic Substring.
    """
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(set(s)) == 1: return s
        n = len(s)
        start, end, maxL = 0, 0, 0
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i):
                #这里等同于if (i-j<2) and s[j]==s[i]:return 1
                # elif dp[j+1][i-1] and s[j]==s[i]:return 1 else return 0
                dp[j][i] = (s[j] == s[i]) and ((i - j < 2) or dp[j + 1][i - 1])
                if dp[j][i] and maxL < i - j + 1:
                    maxL = i - j + 1
                    start = j
                    end = i
            dp[i][i] = 1
        return s[start: end + 1]



class Solution2(object):
    """
    solution看到的答案，这个代码量算是最少的了，可能也是因为palindromic的判断方法是通过s[i:j]==s[i:j][::-1]来判断的
    不过思路也是很不错的，直接判断当前的j-i是否会大于之前的长度，会就继续判断是够palindromic，不会就break
    Runtime: 5524 ms, faster than 14.15% of Python online submissions for Longest Palindromic Substring.
    Memory Usage: 11.9 MB, less than 29.29% of Python online submissions for Longest Palindromic Substring.
    """
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        m = ''  # Memory to remember a palindrome
        for i in range(len(s)):  # i = start, O = n
            for j in range(len(s), i, -1):  # j = end, O = n^2
                if len(m) >= j-i:  # To reduce time
                    break
                elif s[i:j] == s[i:j][::-1]:
                    m = s[i:j]
                    break
        return m
