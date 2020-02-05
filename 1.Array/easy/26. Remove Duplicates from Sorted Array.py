

class Solution:
    """
    题目要求：在不创建新空间的情况下，从有序数组中移除重复值，然后返回不重复数组的长度
    解法是定义两个变量，然后一个依次往后检测，另一个当检测到不同值时就写入数组，逻辑还是蛮简单的
    Runtime: 56 ms, faster than 90.54% of Python3 online submissions for Remove Duplicates from Sorted Array.
    """
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

    
class Solution2(object):
    """
    讨论区的解法，直接定义索引0，如果当前值和第0个值不同，则index+=1,然后赋值到index也就是第一个值，依次类推
    Runtime: 56 ms, faster than 90.54% of Python3 online submissions for Remove Duplicates from Sorted Array.
    """
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

