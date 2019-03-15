

class Solution(object):
    """
    同153，利用二分法的思想
    Runtime: 16 ms, faster than 100.00% of Python online submissions for Find Peak Element.
    Memory Usage: 10.9 MB, less than 25.95% of Python online submissions for Find Peak Element.
    """
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            mid = lo + (hi-lo)//2
            if nums[mid] > nums[mid+1]:
                hi = mid
            else:
                lo = mid + 1
        return lo