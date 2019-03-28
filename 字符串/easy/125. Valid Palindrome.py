

class Solution(object):
    """
    标准解法，通过while循环左侧和右侧，当碰到非字母数字就跳过，然后比对左右侧是否相等
    Runtime: 44 ms, faster than 64.81% of Python online submissions for Valid Palindrome.
    Memory Usage: 12.2 MB, less than 56.30% of Python online submissions for Valid Palindrome.
    """
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l,r = 0,len(s)-1
        while l < r:
            while l<r and not s[l].isalnum():
                l += 1
            while l<r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True