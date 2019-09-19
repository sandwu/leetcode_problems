


class Solution(object):
    """
    题意是求给定字符串s，确认是否可拆分成wordDict里提供的所有
    解法利用DFS
    Runtime: 32 ms, faster than 40.86% of Python online submissions for Word Break.
    Memory Usage: 11.9 MB, less than 51.06% of Python online submissions for Word Break.
    """
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        starts = [0]
        for i in range(len(s)):
            for j in starts:
                if s[j:i+1] in wordDict:
                    starts.append(i+1)
                    break
        return starts[-1] == len(s)


class Solution2(object):
    """
    上面的简写
    Runtime: 32 ms, faster than 40.86% of Python online submissions for Word Break.
    Memory Usage: 11.8 MB, less than 70.21% of Python online submissions for Word Break.
    """
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        ok = [True]
        for i in range(1, len(s)+1):
            ok += any(ok[j] and s[j:i] in wordDict for j in range(i)),
        return ok[-1]