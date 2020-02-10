

"""
Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums: return -1
        if target == nums[0]: return 0
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) >> 1
            if nums[mid] == target:
                return mid
            if target > nums[0]:
                if target > nums[mid] and nums[mid] >= nums[0]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if target > nums[mid] or nums[mid] >= nums[0]:
                    left = mid + 1
                else:
                    right = mid - 1
        return - 1



"""
[4,5,6,0,1] 0  
[
"""