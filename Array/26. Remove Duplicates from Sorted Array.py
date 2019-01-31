class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        read = 1
        write = 1
        while read < len(nums):
            if nums[read] != nums[read-1]:
                nums[write] = nums[read]
                write += 1
            read += 1
        return write

#第二种击败了97%      
class Solution2(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        index = 0
        for i in range(len(nums)):
            if nums[i] != nums[index]:
                index += 1
                nums[index] = nums[i]

        return index+1

