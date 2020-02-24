

"""
Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5
Explanation: Your function can return either index number 1 where the peak element is 2,
             or index number 5 where the peak element is 6.

"""

class Solution:
    def findpeakele(self,nums):
        l,r = 0,len(nums)-1
        while l < r:
            mid = (l+r) >> 1
            if nums[mid] > nums[mid+1]:
                r = mid
            else:
                l = mid + 1
        return l

a = Solution()
nums = [1,2,1,3,5,6,7]
print(a.findpeakele(nums))