
class Solution(object):
    """
    python trick完成，reverse+split
    Runtime: 20 ms, faster than 84.29% of Python online submissions for Reverse Words in a String.
    Memory Usage: 13.1 MB, less than 5.06% of Python online submissions for Reverse Words in a String.
    """
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(reversed(s.split()))

