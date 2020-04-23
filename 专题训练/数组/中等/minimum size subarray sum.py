
"""

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.

"""


class Solution:
    def minimum(self,s,nums):
        l = r = 0
        csum = 0
        res = float('inf')
        while r < len(nums):
            csum += nums[r]
            while csum >= s:
                res = min(res,r-l+1)
                csum -= nums[l]
                l += 1
            r += 1
        return res if res != float('inf') else 0



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