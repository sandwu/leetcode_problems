class Solution(object):
    def fourSum(self, nums, target):
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i> 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i+1,len(nums)):  #直接再来个for循环
                if j>i+1 and nums[j] == nums[j - 1]:
                    continue
                l = j + 1
                r = len(nums) - 1
                target_num = target - nums[i] - nums[j]
                while l < r:
                    if nums[l] + nums[r] == target_num:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l + 1]:  #这里利用快排的思想节省时间
                            l += 1
                        l += 1
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1
                        r -= 1
                    elif nums[l] + nums[r] < target_num:
                        l += 1
                    else:
                        r -= 1
        return res