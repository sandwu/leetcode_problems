class MySolution:
    """
    这道题采用的解法和第一题Two Sum是一模一样的，唯一不同的是题目要求从1开始计数，所以在返回值上各加了一
    Runtime: 36 ms, faster than 99.77% of Python3 online submissions for Two Sum II - Input array is sorted.
    """
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        res_dict = {}
        for index,value in enumerate(numbers):
            sub = target - value
            if sub in res_dict:
                return [res_dict[sub]+1, index+1]
            else:
                res_dict[value] = index


class Solution:
    """
    讨论区看到的Two-pointer的解法，看起来很棒，因为是有序，所以计算第一个和最后一个的和，如果>target则说明后一个数大了，那就往前推移；
    如果小了，说明前一个数小了，那就往后推移；直到找到那个值；当然也有二分法，但我觉得这道题没必要用二分法来做。
    Runtime: 36 ms, faster than 99.77% of Python3 online submissions for Two Sum II - Input array is sorted.
    """
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, len(numbers)-1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l+1, r+1]
            elif s < target:
                l += 1
            else:
                r -= 1