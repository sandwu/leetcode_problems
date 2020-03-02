
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