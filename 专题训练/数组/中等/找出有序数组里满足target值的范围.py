

"""
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
"""

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums == [] :return [-1 ,-1]
        left = 0
        right = len(nums) -1
        while left <= right:
            mid = (left + right) >> 1
            if nums[mid] == target:
                left_position = right_position = mid
                while left_position >= 0 and nums[left_position] == target:
                    left_position -= 1
                while right_position < len(nums) and nums[right_position] == target:
                    right_position += 1
                return [left_position + 1, right_position - 1]
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return [-1, -1]

