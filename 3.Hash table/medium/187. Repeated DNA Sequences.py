

class Solution(object):
    """
    直接依次遍历取值，判断是否存在定义的dict里，存在就val+1，不存在就为1，最后遍历取值val>1的
    Runtime: 72 ms, faster than 58.05% of Python online submissions for Repeated DNA Sequences.
    Memory Usage: 30.4 MB, less than 52.31% of Python online submissions for Repeated DNA Sequences.
    """
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        dict1 = {}
        for i,v in enumerate(s[:-9]):
            dict1[s[i:i+10]] = dict1.get(s[i:i+10],0) + 1
        return [k for k,v in dict1.iteritems() if v>1]


class Solution2(object):
    """
    用Counter来简化第一步行程dict的操作，并且效率也变高了
    Runtime: 68 ms, faster than 63.86% of Python online submissions for Repeated DNA Sequences.
    Memory Usage: 35 MB, less than 15.66% of Python online submissions for Repeated DNA Sequences
    """
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        from collections import Counter
        return [k for k,v in Counter([s[x:x+10] for x in range(len(s)-9)]).iteritems() if v > 1]