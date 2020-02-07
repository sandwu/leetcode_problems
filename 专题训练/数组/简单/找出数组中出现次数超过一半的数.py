


class Solution:
    def majorityelement(self,nums):
        if len(nums) == 1:
            return nums[0]
        dict1 = {}
        for num in nums:
            if num in dict1:
                dict1[num] += 1
                if dict1[num] >= len(nums) // 2:
                    return num
            else:
                dict1[num] = 0