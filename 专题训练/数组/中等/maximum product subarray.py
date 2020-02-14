

"""

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

"""

class Solution:
    def maximum(self,nums):
        rev_nums = nums[::-1]
        for i in range(1,len(nums)):
            nums[i] *= nums[i-1] or 1
            rev_nums[i] *= rev_nums[i-1] or 1
        return max(nums+rev_nums)







