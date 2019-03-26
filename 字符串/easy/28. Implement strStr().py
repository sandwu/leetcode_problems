
class Solution(object):
    """
    直接遍历判断当前的haystack包含的与needle是否相等即可
    Runtime: 20 ms, faster than 80.25% of Python online submissions for Implement strStr().
    Memory Usage: 11.8 MB, less than 19.41% of Python online submissions for Implement strStr().
    """
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1


