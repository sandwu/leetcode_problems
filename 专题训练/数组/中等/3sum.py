
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i> 0 and nums[i] == nums[i - 1]: #要注意当当前数等于上一个数的时候，可能会重复，要跳过
                continue
            l = i + 1
            r = len(nums) - 1
            target = -nums[i]
            while l < r:
                if nums[l] + nums[r] == target:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:  #这里利用快排的思想节省时间
                        l += 1
                    l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        return res
