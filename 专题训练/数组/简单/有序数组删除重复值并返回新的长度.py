


class Solution:
    def removeDuplicates(self, nums): #原地修改，不能新加空间
        if not nums:return 0
        read = write = 1
        while read < len(nums):
            if nums[read] != nums[read-1]:
                nums[write] = nums[read]
                write += 1
            read += 1
        return write

