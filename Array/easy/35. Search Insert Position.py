class Solution:
    """
    碰到有序的简单做法就是一一比较过去，本题就是一次遍历，判断当有数>=target时再判断具体的是大于还是等于；
    第一次写遗忘了index += 1，limit time out，补上就成功运行了。
    最高达到：Runtime: 52 ms, faster than 98.62% of Python3 online submissions for Search Insert Position.
    """
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums == []:
            return 1
        index = 0
        while index < len(nums):
            if nums[index] >= target:
                if nums[index] == target:
                    return index
                else:
                    return index
            index += 1
        return len(nums)

class Solution2:
    """
    讨论区的解法，果然2分法还是有序数组解法的优先选择～
    Runtime: 20 ms, faster than 100.00% of Python online submissions for Search Insert Position.
    """
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums)-1
        while start < end:
            mid = (start+end)//2 
            if nums[mid] > target:
                end = mid-1
            elif nums[mid] < target:
                start = mid+1
            else:
                return mid
        if nums[start] < target:
            return start + 1
        else:
            return start