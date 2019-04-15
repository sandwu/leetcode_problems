
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


class Solution:
    """
    讨论区的一种解法直接判断是否为0，是的话就往后交换，
    Runtime: 44 ms, faster than 100.00% of Python3 online submissions for Move Zeroes.
    """
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero = 0  # records the position of "0"
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1