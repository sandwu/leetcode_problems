

class Solution(object):
    """
    set(zip(s,t)) 来比较算是最常见的解法之一了
    Runtime: 20 ms, faster than 73.90% of Python online submissions for Word Pattern.
    Memory Usage: 11.8 MB, less than 5.15% of Python online submissions for Word Pattern.
    """
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        s = str.split()
        p = pattern
        return len(set(zip(s,p))) == len(set(s)) == len(set(p)) and len(s) == len(p)


class Solution2(object):
    """
    find对字符串集合，index对列表集合，如果找到的位置相等则说明一致
    Runtime: 20 ms, faster than 73.90% of Python online submissions for Word Pattern.
    Memory Usage: 11.8 MB, less than 5.15% of Python online submissions for Word Pattern.
    """
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        s = str.split()
        p = pattern
        return map(p.find, p) == map(s.index, s)