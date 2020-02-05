

class Solution:
    def maxsubarray(self,nums):
        if not nums:return 0
        maxsum_now = maxsum_tonow = 0
        for i in range(len(nums)):
            maxsum_now = max(nums[i],maxsum_now+nums[i])
            maxsum_tonow = max(maxsum_tonow,maxsum_now)
        return maxsum_tonow

    def maxsubarray2(self,nums):
        if not nums:return 0
        for i in range(1,len(nums)):
            if nums[i-1]>0:
                nums[i] += nums[i-1]
        return max(nums)