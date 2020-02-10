
"""
Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
"""

class Solution(object):
    def canJump(self, nums):
        #贪心算法，比如索引1必须由0+1跳到，索引2必须由大于0+2或者大于1+1跳到，一直维护当前所能跳到的最大值
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:return False
        reach = 0
        for i in range(len(nums)):
            if i > reach:
                return False
            reach = max(reach,i+nums[i])
        return True