
"""
Input: ["flower","flow","flight"]
Output: "fl"

"""

class Solution(object):
    """
    通过zip把每一个首字母拼接，然后判断set后是否为1即可知道是否相等，要注意的是当全部匹配成功后，取列表strs里面长度最短的数
    Runtime: 24 ms, faster than 64.14% of Python online submissions for Longest Common Prefix.
    Memory Usage: 12.1 MB, less than 5.66% of Python online submissions for Longest Common Prefix.
    """
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''

        for i, v in enumerate(zip(*strs)):
            if len(set(v)) > 1:
                return strs[0][:i]
        else:
            return min(strs)


class Solution2(object):
    """
    直接用暴力匹配法，取列表第一个单词，从后往前遍历，逐一匹配所有单词，符合即返回
    Runtime: 28 ms, faster than 38.54% of Python online submissions for Longest Common Prefix.
    Memory Usage: 12 MB, less than 5.66% of Python online submissions for Longest Common Prefix.
    """
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = strs[0] if strs else ''
        while True:
            if all(s.startswith(prefix) for s in strs):
                return prefix
            prefix = prefix[:-1]