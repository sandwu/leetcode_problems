

"""
Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
"""

class Solution(object):
    """
    题意是给定一个集合，求将集合分片，而满足分片后各个片段都是回文的集合
    解法：果断dfs
    既然是分片，那么针对每次分片判断是否是回文，如果都是，那么假如结果集！
    如果第1个就不是回文，就直接跳过该分片
    Runtime: 72 ms, faster than 65.64% of Python online submissions for Palindrome Partitioning.
    Memory Usage: 12.2 MB, less than 70.59% of Python online submissions for Palindrome Partitioning.
    """
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if not s:
            return []

        output = []
        self.findPartition(s, output, [])

        return output

    def findPartition(self, s, output, temp):
        if not s:
            output.append(temp[:])
            return

        for i in range(1, len(s) + 1):
            if self.isPalindrome(s[:i]):
                temp.append(s[:i])
                self.findPartition(s[i:], output, temp)
                temp.pop()

    def isPalindrome(self, string):
        return string == string[::-1]