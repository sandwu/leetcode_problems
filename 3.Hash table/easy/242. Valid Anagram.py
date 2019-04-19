


class Solution(object):
    """
    Counter 直接获取对应的集合里个数，如果相等，说明二者的各个字母数量一致，则顺序颠倒后一定相等
    Runtime: 64 ms, faster than 18.08% of Python online submissions for Valid Anagram.
    Memory Usage: 12.8 MB, less than 9.87% of Python online submissions for Valid Anagram.
    """
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        from collections import Counter
        return Counter(s) == Counter(t)


class Solution2(object):
    """
    用sorted分割成有序列表
    Runtime: 48 ms, faster than 59.81% of Python online submissions for Valid Anagram.
    Memory Usage: 13.3 MB, less than 5.06% of Python online submissions for Valid Anagram.
    """
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)


class Solution3(object):
    """
    根据个数用dict存储，比对存储后的dict是否相等
    Runtime: 44 ms, faster than 72.27% of Python online submissions for Valid Anagram.
    Memory Usage: 12.7 MB, less than 9.87% of Python online submissions for Valid Anagram.
    """
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic1, dic2 = {}, {}
        for item in s:
            dic1[item] = dic1.get(item, 0) + 1
        for item in t:
            dic2[item] = dic2.get(item, 0) + 1
        return dic1 == dic2