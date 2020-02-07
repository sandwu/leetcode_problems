
class Solution(object):
    def moveZeroes(self, nums): #用读写两个指针来做
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        read = write = 0
        n = len(nums)
        while read < len(nums):
            if nums[read] != 0:
                nums[write] = nums[read]
                write += 1
            read += 1
        for i,v in enumerate(nums[write:],write):
            nums[i] = 0
        return nums


class MySolution:
    """
    思路很简单，定义首尾2个数，如果首部为0就删除首部，然后尾部插入0即可
    Runtime: 44 ms, faster than 100.00% of Python3 online submissions for Move Zeroes.
    """
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        start = 0
        end = len(nums) - 1
        while start < end:
            if nums[start] == 0:
                del nums[start]
                nums.append(0)
                end -= 1
            else:
                start += 1
