


"""
Example 1:

Input: [1,3,4,2,2]
Output: 2

"""

class Solution:
    def findthedup(self,nums):
        l,r = 0,len(nums)-1
        while l <= r:
            mid = (l+r) >> 1
            cnt = 0
            for num in nums:
                if num <= mid:
                    cnt += 1
            if cnt > mid:
                r = mid - 1
            else:
                l = mid + 1
        return l

nums = [1,3,4,2,2,5]
a = Solution()
print(a.findthedup(nums))