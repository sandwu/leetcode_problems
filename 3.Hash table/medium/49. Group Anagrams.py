


class Solution(object):
    """
    建立有序字典，比对每一个排序后的值，如果数值相同，则加入到dict的value里，
    最后再对dict.value进行排序，返回列表即可
    Runtime: 96 ms, faster than 92.77% of Python online submissions for Group Anagrams.
    Memory Usage: 17.5 MB, less than 5.13% of Python online submissions for Group Anagrams
    """
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = collections.defaultdict(list)
        for s in strs:
            groups[tuple(sorted(s))].append(s)
        return list(map(sorted, groups.values()))
