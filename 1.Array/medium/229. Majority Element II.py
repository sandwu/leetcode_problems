
class Solution(object):
    """
    直接利用set、len、列表的count、等等python的内置函数结构来完成
    Runtime: 40 ms, faster than 23.57% of Python online submissions for Majority Element II.
    Memory Usage: 11.6 MB, less than 21.25% of Python online submissions for Majority Element II.
    """
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return [num for num in set(nums) if nums.count(num) > len(nums)/3]