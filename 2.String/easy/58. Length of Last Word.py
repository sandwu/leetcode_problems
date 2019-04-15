

class Solution(object):
    """
    直接利用python的split获取最后一个即可
    Runtime: 24 ms, faster than 32.47% of Python online submissions for Length of Last Word.
    Memory Usage: 11.9 MB, less than 5.42% of Python online submissions for Length of Last Word.
    """
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split()[-1]) if s.split() else 0


class Solution2(object):
    """
    利用rstrip可以把判断语句都省略
    Runtime: 20 ms, faster than 70.08% of Python online submissions for Length of Last Word.
    Memory Usage: 11.8 MB, less than 5.42% of Python online submissions for Length of Last Word.
    """
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.rstrip().split(' ')[-1])