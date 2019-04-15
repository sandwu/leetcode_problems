

class Solution(object):
    """
    这解法是真的牛逼，or 1是当列表里遇到0的时候，就乘以1，这样就能跳过0的存在
    同时需要计算翻转过来的另一个列表集合和，比如[-1,1,1]，如果是正向计算的话就是
    [-1,-1,-1]，反向计算就是：[1,1,-1]，所以需要反向计算
    Runtime: 24 ms, faster than 98.70% of Python online submissions for Maximum Product Subarray.
    Memory Usage: 12 MB, less than 17.74% of Python online submissions for Maximum Product Subarray.
    """
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rev_nums = nums[::-1]
        for i in range(1, len(nums)):
            nums[i] *= nums[i-1] or 1
            rev_nums[i] *= rev_nums[i-1] or 1
        return max(nums+rev_nums)

nums = [-2,0,-1]
a = Solution()
print(a.maxProduct(nums))