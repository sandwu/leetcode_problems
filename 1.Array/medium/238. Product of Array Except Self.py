
class Solution(object):
    """
    Runtime: 96 ms, faster than 70.90% of Python online submissions for Product of Array Except Self.
    Memory Usage: 18.7 MB, less than 28.32% of Python online submissions for Product of Array Except Self.
    """
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        re = list()
        re.append(1)
        temp = 1
        for i in range(0,len(nums)-1):
            temp = temp * nums[i] 
            re.append(temp)
        temp = 1
        for i in range(len(nums)-2,-1,-1):
            temp = temp * nums[i+1]
            re[i] = re[i] * temp
        return re

        