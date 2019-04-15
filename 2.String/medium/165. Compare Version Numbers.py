import itertools

class Solution(object):
    """
    虽然用的是trick，但是还是很了不起，先用生成器获取version1和version2的列表集合
    然后izip_longest，这个是依次拼接两个集合，转换为两两集合，没有的填充为0，再用zip回复原来的两个集合
    最后用cmp比较即可
    def cmp(a, b):
        return (a > b) - (a < b)
    Runtime: 32 ms, faster than 8.53% of Python online submissions for Compare Version Numbers.
    Memory Usage: 11.7 MB, less than 5.71% of Python online submissions for Compare Version Numbers.
    """
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        splits = (map(int, v.split("")) for v in (version1,version2))
        return cmp(*zip(*itertools.izip_longest(*splits, fillvalue=0)))


class Solution2(object):
    """
    没有用trick的方法
    Runtime: 20 ms, faster than 76.17% of Python online submissions for Compare Version Numbers.
    Memory Usage: 11.7 MB, less than 5.71% of Python online submissions for Compare Version Numbers.
    """
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1, v2 = self.helper(version1), self.helper(version2)
        return 1 if v1 > v2 else (-1 if v1 < v2 else 0)

    def helper(self, v):
        v = map(int, v.split("."))
        # tackle tailing 0 case: 1.0.0 vs 1
        i = len(v)-1
        while i >= 0 and v[i] == 0:
            i -= 1
        return v[:i+1]