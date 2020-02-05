


class Solution:
    def removeelements(self,nums,val):
        if not nums:return
        index = 0
        while index < len(nums):
            if nums[index] == val:
                del nums[index]
                continue
            index += 1
        return index