


class Solution(object):#仅一个答案满足
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