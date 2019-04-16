


class Solution(object):
    """
    通过find找寻的位置是否一致就能判断，实在是叼
    Runtime: 52 ms, faster than 24.67% of Python online submissions for Isomorphic Strings.
    Memory Usage: 12.7 MB, less than 40.63% of Python online submissions for Isomorphic Strings.
    """
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return [s.find(i) for i in s] == [t.find(j) for j in t]


class Solution2(object):
    """
    讨论区精彩解法2
    Runtime: 28 ms, faster than 90.65% of Python online submissions for Isomorphic Strings.
    Memory Usage: 14.6 MB, less than 5.00% of Python online submissions for Isomorphic Strings.
    """
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))