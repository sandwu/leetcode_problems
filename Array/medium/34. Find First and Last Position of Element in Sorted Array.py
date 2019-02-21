

class MySolution(object):
    """
    正常思路，利用二分法来完成，缺点是在找到中间数后要一次从左、从右开始遍历，这也造成了时间复杂度不是很理想
    Runtime: 24 ms, faster than 82.77% of Python online submissions for Find First and Last Position of Element in Sorted Array.
    Memory Usage: 11.4 MB, less than 60.93% of Python online submissions for Find First and Last Position of Element in Sorted Array.
    """
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums == []:
            return [-1, -1]
        left_pos = 0
        right_pos = len(nums)
        
        while left_pos < right_pos:
            middle_pos = (right_pos - left_pos) // 2 + left_pos
            middle_val = nums[middle_pos]
            
            if middle_val == target:
                left = middle_pos
                while left >= 0 and nums[left] == target:
                    left -= 1
                right = middle_pos
                while right < len(nums) and nums[right] == target:
                    right += 1
                return [left + 1, right - 1]
            elif middle_val < target:
                left_pos = middle_pos + 1
            else:  # middle_val > target:
                right_pos = middle_pos
        return [-1, -1]


class Solution(object):
    """
    利用python语法的index来完成，通过两次index来定位目标位置即可，找不到报错就拦截
    Runtime: 20 ms, faster than 100.00% of Python online submissions for Find First and Last Position of Element in Sorted Array.
    Memory Usage: 11.9 MB, less than 5.30% of Python online submissions for Find First and Last Position of Element in Sorted Array.
    """
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        try:
            return [nums.index(target),len(nums)-list(reversed(nums)).index(target)-1]
        except:
            return [-1,-1]


        
