
class MySolution:
    """
    用python的set差集来做，但效率很低
    Runtime: 52 ms, faster than 45.33% of Python3 online submissions for Missing Number.
    """
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) + 1
        res_list = list(range(n))
        res = set(res_list) - set(nums)
        return list(res)[0]


class Solution:
    """
    讨论区果然还是大神多，用求和的方法轻松拿到答案
    Runtime: 40 ms, faster than 100.00% of Python3 online submissions for Missing Number.
    """
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(range(len(nums) + 1)) - sum(nums)