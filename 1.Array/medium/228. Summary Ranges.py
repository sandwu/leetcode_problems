
class Solution(object):
    """
    []+[]=[],直接根据题目搞个集合，比如是[0,1,2,4,5,7],则for循环后集合为[[0,2],[4,5],[7]]
    代码里的range[-1][1:] = n,直接把列表里处于端点内的数字直接去除了，最后一步通过join拼接即可
    Runtime: 16 ms, faster than 100.00% of Python online submissions for Summary Ranges.
    Memory Usage: 10.7 MB, less than 55.79% of Python online submissions for Summary Ranges.
    """
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ranges = []
        for n in nums:
            if not ranges or n > ranges[-1][-1] + 1:
                ranges += [],
            ranges[-1][1:] = n,
        return ['->'.join(map(str, r)) for r in ranges]


class Solution2(object):
    """
    同上解法，不过用两列表，同时利用列表是可变序列来进行编辑
    Runtime: 16 ms, faster than 100.00% of Python online submissions for Summary Ranges.
    Memory Usage: 10.8 MB, less than 32.63% of Python online submissions for Summary Ranges.
    """
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ranges, r = [], []
        for n in nums:
            if n-1 not in r:
                r = []
                ranges += r,
            r[1:] = n,
        return ['->'.join(map(str, r)) for r in ranges]
            

nums = [0,1,2,4,5,7]
a = Solution()
a.summaryRanges(nums)