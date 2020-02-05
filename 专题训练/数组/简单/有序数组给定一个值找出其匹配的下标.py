

class Solution:
    def searchInsert(self,nums,target):#如果不存在就返回它应该插入的下表
        start = 0
        end = len(nums)-1
        while start < end:
            mid = (start+end)>>1
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        if nums[start] < target:
            return start + 1
        else:
            return start
