
class MySolution(object):
    """
    思路简单，从第2个开始比，如果和前两个来的一致，则删除该数，否则继续
    Runtime: 36 ms, faster than 86.94% of Python online submissions for Remove Duplicates from Sorted Array II.
    Memory Usage: 10.5 MB, less than 99.09% of Python online submissions for Remove Duplicates from Sorted Array II.
    """
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return
        index = 2
        while index and index <= len(nums)-1:
            if nums[index] == nums[index-1] and nums[index] == nums[index-2]:
                nums.pop(index)
            else:
                index += 1
        return index
        

class Solution(object):
    """
    讨论区答案，一次遍历，当i>2的时候，如果遍历到的数增大则交换i的位置，否则继续遍历
    Runtime: 32 ms, faster than 100.00% of Python online submissions for Remove Duplicates from Sorted Array II.
    Memory Usage: 10.9 MB, less than 5.45% of Python online submissions for Remove Duplicates from Sorted Array II.
    [1,1,1,2,2,3]
    """
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        for n in nums:
            if i < 2 or n > nums[i-2]:
                nums[i] = n
                i += 1
        return i
        