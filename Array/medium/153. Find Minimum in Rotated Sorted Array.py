
class MySolution(object):
    """
    观察发现遍历时下一个数小于上一个数就说明是最小值，因此代码直接遍历即可得到；如果没有找到，则直接返回第一个
    Runtime: 16 ms, faster than 100.00% of Python online submissions for Find Minimum in Rotated Sorted Array.
    Memory Usage: 10.9 MB, less than 45.22% of Python online submissions for Find Minimum in Rotated Sorted Array.
    """
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return False
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                return nums[i+1]
        return nums[0]


class Solution(object):
    """
    讨论区。。
    Runtime: 16 ms, faster than 100.00% of Python online submissions for Find Minimum in Rotated Sorted Array.
    Memory Usage: 11.1 MB, less than 5.65% of Python online submissions for Find Minimum in Rotated Sorted Array.
    """
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return min(nums)

class Solution2(object):
    """
    二分法才是终极奥义
    Runtime: 16 ms, faster than 100.00% of Python online submissions for Find Minimum in Rotated Sorted Array.
    Memory Usage: 10.9 MB, less than 43.04% of Python online submissions for Find Minimum in Rotated Sorted Array.
    """
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo, hi = 0, len(nums)-1
        while lo <= hi:
            mid = lo + (hi-lo)//2
            if nums[mid] > nums[hi]:
                lo = mid+1
            elif mid == 0 or (mid-1 >= 0 and nums[mid-1] > nums[mid]):
                return nums[mid]
            else:
                hi = mid-1
        raise RuntimeError