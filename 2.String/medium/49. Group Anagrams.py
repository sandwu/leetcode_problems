
class Solution(object):
    """
    利用grouby特性直接求解，但效率不高
    Runtime: 108 ms, faster than 100.00% of Python online submissions for Group Anagrams.
    Memory Usage: 15.6 MB, less than 17.48% of Python online submissions for Group Anagrams.
    """
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = itertools.groupby(sorted(strs, key=sorted), sorted)
        return [sorted(members) for _, members in groups]


class Solution2(object):
    """
    利用有序字典结合，以排序后的数为key，然后往对应的key值添加value，实际上也是利用了hash的特性
    Runtime: 96 ms, faster than 100.00% of Python online submissions for Group Anagrams.
    Memory Usage: 17.7 MB, less than 5.13% of Python online submissions for Group Anagrams.
    """
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = collections.defaultdict(list)
        for s in strs:
            groups[tuple(sorted(s))].append(s)
        return map(sorted, groups.values())
