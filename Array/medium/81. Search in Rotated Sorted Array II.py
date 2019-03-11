
class Solution(object):
    """
    英文注释写的比较清楚了，要注意的是代码核心是围绕分割成左边为有序序列或者右边为有序序列这条来实现的，那要达到左边是有序
    序列的前提则左边一开始不能有等于nums[mid]的数，所以嵌套了while来解决，而右边是不需要的，因为右边即使等同于nums[mid]，
    则也一直都是有序序列，如果套上while，反而使原本是O(logN)变成了O(N)
    Runtime: 20 ms, faster than 99.76% of Python online submissions for Search in Rotated Sorted Array II.
    Memory Usage: 11 MB, less than 5.66% of Python online submissions for Search in Rotated Sorted Array II.
    """
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        l, r = 0, len(nums)-1
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return True
            while l < mid and nums[l] == nums[mid]: # tricky part
                l += 1
            # the first half is ordered
            if nums[l] <= nums[mid]:
                # target is in the first half
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # the second half is ordered
            else:
                # target is in the second half
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False