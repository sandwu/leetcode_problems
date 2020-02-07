

class Solution:
    def rotateArray(self,nums,k):
        if not nums:return []
        k %= len(nums)   #当k远大于总长度时
        n = len(nums)
        nums[:] = nums[n-k:] + nums[:n-k] #强调要原地修改