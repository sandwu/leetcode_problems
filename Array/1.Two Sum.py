# 利用enumerate获取列表的下标和值，将值作为key，下标作为value存入字典，只需O(n)的时间复杂度
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict1 = {}
        for i, v in enumerate(nums):
            sub = target - v
            if sub in dict1:
                return [dict1[sub], i]
            else:
                dict1[v] = i
