
class Solution2(object):
    """
    定义快慢指针，当快指针达到所在的位置>=s时，进行判断，将这个值减去慢指针，取满足条件的最小值ans，然后不断迭代该过程，
    Runtime: 28 ms, faster than 86.79% of Python online submissions for Minimum Size Subarray Sum.
    Memory Usage: 11.9 MB, less than 51.61% of Python online submissions for Minimum Size Subarray Sum.
    """
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        ans = n = len(nums)
        l = r = sr = 0
        while r < n:
            sr += nums[r]
            r += 1
            if sr >= s:
                while sr - nums[l] >= s:
                    sr -= nums[l]
                    l += 1
                ans = min(ans, r - l)
        return ans if sr >= s else 0