


class Solution:
    def findMin(self,nums):
        for i in range(1,len(nums)):
            if nums[i] < nums[i-1]:
                return nums[i]
        return nums[0]

    #[4,5,6,7,0,1,2]
    def findMin2(self,nums):
        left,right = 0,len(nums)-1
        while left <= right:
            mid = (left + right ) >> 1
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid]==0 or (mid-1>=0 and nums[mid-1] > nums[mid]):
                return nums[mid]
            else:
                right = mid - 1
