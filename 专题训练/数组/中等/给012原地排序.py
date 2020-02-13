
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left ,right = 0 ,len(nums ) -1
        index = 0
        while index <= right:
            if left < index and nums[index] == 0: #定义前后指针来完成，要注意前指针一定要在移动指针前
                nums[left] ,nums[index] = nums[index] ,nums[left]
                left += 1
            elif nums[index] == 2:
                nums[right] ,nums[index] = nums[index] ,nums[right]
                right -= 1
            else:
                index += 1
        return nums


class Solution2(object):
    """
    这个解法太强了，因为题目的限制是原地变动，基本就没想过用额外空间的方法，而下述代码则直接绕过创空间来实现
    Runtime: 20 ms, faster than 98.75% of Python online submissions for Sort Colors.
    Memory Usage: 10.6 MB, less than 90.57% of Python online submissions for Sort Colors.
    """
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        c0 = c1 = c2 = 0
        for num in nums:
            if num == 0:
                c0 += 1
            elif num == 1:
                c1 += 1
            else:
                c2 += 1
        nums[:c0] = [0] * c0
        nums[c0:c1+c1] = [1] * c1
        nums[c0+c1:] = [2] * c2